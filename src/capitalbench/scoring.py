from __future__ import annotations

import csv
import json
import math
import warnings
from collections import Counter, defaultdict
from pathlib import Path

from .io import load_manifest, load_options, read_json
from .run_store import RunPaths, get_selected_run_paths, read_run_manifest
from .schemas import MarketOption, ModelSubmission, PriceRecord, ScoreRecord
from .validation import iter_submission_files, validate_submission_payload


def read_price_records(path: Path) -> dict[str, PriceRecord]:
    if not path.exists():
        raise FileNotFoundError(f"missing price file: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError(f"{path} must contain a header row")
        identifiers = {"option_id", "symbol"}
        price_columns = {"price", "close", "adj_close", "adjClose"}
        if not identifiers.intersection(reader.fieldnames) or not price_columns.intersection(reader.fieldnames):
            raise ValueError(f"{path} must contain option_id or symbol plus price, close, or adj_close columns")
        records = [PriceRecord.model_validate(row) for row in reader]
    prices: dict[str, PriceRecord] = {}
    for record in records:
        key = record.option_id or record.symbol
        if key is None:
            raise ValueError(f"{path} contains a price row without option_id or symbol")
        if key in prices:
            raise ValueError(f"{path} contains duplicate price key: {key}")
        if record.price_source == "close":
            warnings.warn(
                f"{path} row for {key} uses close because adj_close is missing",
                UserWarning,
                stacklevel=2,
            )
        prices[key] = record
    return prices


def _is_sp500_option(option: MarketOption) -> bool:
    aliases = {"sp500", "s&p500", "s_and_p_500", "spy", "spx"}
    return (
        option.is_benchmark
        or option.option_id.lower() in aliases
        or option.asset_symbol.upper() in {"SPY", "SPX", "^GSPC"}
    )


def _is_cash_option(option: MarketOption) -> bool:
    return option.is_cash or option.option_id.lower() == "cash" or option.asset_symbol.upper() in {"USD", "CASH"}


def _missing_price_message(option: MarketOption, side: str, selected_option_ids: set[str]) -> str:
    if _is_sp500_option(option):
        return f"missing {side} price for SP500 benchmark option_id: {option.option_id}"
    if option.option_id in selected_option_ids:
        return f"missing {side} price for selected option_id: {option.option_id}"
    return f"missing {side} price for option_id: {option.option_id}"


def _lookup_price(prices: dict[str, PriceRecord], option: MarketOption) -> PriceRecord | None:
    for key in [option.option_id, option.symbol, option.tiingo_symbol, option.asset_symbol]:
        if key and key in prices:
            return prices[key]
    return None


def calculate_option_returns(
    options: list[MarketOption],
    entry_prices: dict[str, PriceRecord],
    exit_prices: dict[str, PriceRecord],
    selected_option_ids: set[str] | None = None,
    required_option_ids: set[str] | None = None,
) -> dict[str, float]:
    selected_option_ids = selected_option_ids or set()
    required_option_ids = required_option_ids or {option.option_id for option in options}
    returns: dict[str, float] = {}
    for option in options:
        entry_record = _lookup_price(entry_prices, option)
        exit_record = _lookup_price(exit_prices, option)
        if entry_record is None:
            if _is_cash_option(option):
                returns[option.option_id] = 0.0
                continue
            if option.option_id in required_option_ids:
                raise ValueError(_missing_price_message(option, "entry", selected_option_ids))
            continue
        if exit_record is None:
            if _is_cash_option(option):
                returns[option.option_id] = 0.0
                continue
            if option.option_id in required_option_ids:
                raise ValueError(_missing_price_message(option, "exit", selected_option_ids))
            continue
        entry_price = entry_record.price
        exit_price = exit_record.price
        if entry_price is None or exit_price is None:
            if option.option_id in required_option_ids:
                raise ValueError(f"missing usable price for option_id: {option.option_id}")
            continue
        returns[option.option_id] = (exit_price / entry_price) - 1
    return returns


def rank_options(option_returns: dict[str, float]) -> dict[str, int]:
    ranked = sorted(option_returns.items(), key=lambda item: (-item[1], item[0]))
    ranks: dict[str, int] = {}
    current_rank = 0
    previous_return: float | None = None
    for index, (option_id, option_return) in enumerate(ranked, start=1):
        if previous_return is None or not math.isclose(option_return, previous_return):
            current_rank = index
        ranks[option_id] = current_rank
        previous_return = option_return
    return ranks


def _find_sp500_option(options: list[MarketOption]) -> MarketOption:
    for option in options:
        if _is_sp500_option(option):
            return option
    raise ValueError("options.yaml must define an S&P 500 benchmark option")


def _find_cash_return(options: list[MarketOption], option_returns: dict[str, float]) -> float:
    for option in options:
        if _is_cash_option(option):
            return option_returns[option.option_id]
    return 0.0


def _load_parsed_submissions(
    run_paths: RunPaths,
    options: list[MarketOption],
    round_id: str,
    run_type: str,
    replicate_count: int,
) -> list[ModelSubmission]:
    submissions: list[ModelSubmission] = []
    for parsed_file in iter_submission_files(run_paths.parsed_dir):
        try:
            payload = read_json(parsed_file)
            submissions.append(
                validate_submission_payload(
                    payload,
                    options,
                    round_id,
                    run_type=run_type,
                    replicate_count=replicate_count,
                    require_run_metadata=run_type in {"official", "stability", "retrospective"},
                )
            )
        except Exception:
            continue
    _enforce_scoring_submission_set(submissions, run_type, replicate_count)
    return submissions


def _enforce_scoring_submission_set(
    submissions: list[ModelSubmission],
    run_type: str,
    replicate_count: int,
) -> None:
    if run_type == "official":
        if replicate_count != 1:
            raise ValueError("official run has replicates > 1")
        seen_model_ids: set[str] = set()
        for submission in submissions:
            if submission.model_id in seen_model_ids:
                raise ValueError(f"duplicate model_id in official parsed submissions: {submission.model_id}")
            seen_model_ids.add(submission.model_id)
    elif run_type == "stability":
        seen_replicates: set[tuple[str, int | None]] = set()
        for submission in submissions:
            key = (submission.model_id, submission.replicate_index)
            if key in seen_replicates:
                raise ValueError(
                    "duplicate replicate_index for model_id in stability parsed submissions: "
                    f"{submission.model_id} replicate {submission.replicate_index}"
                )
            seen_replicates.add(key)


def _price_for_csv(prices: dict[str, PriceRecord], option: MarketOption) -> float | str:
    record = _lookup_price(prices, option)
    if record is not None:
        return record.price if record.price is not None else ""
    if _is_cash_option(option):
        return ""
    raise ValueError(f"missing price for option_id: {option.option_id}")


def _price_source_for_csv(prices: dict[str, PriceRecord], option: MarketOption) -> str:
    record = _lookup_price(prices, option)
    if record is not None:
        return record.price_source
    return ""


def _write_returns_csv(
    path: Path,
    options: list[MarketOption],
    entry_prices: dict[str, PriceRecord],
    exit_prices: dict[str, PriceRecord],
    option_returns: dict[str, float],
    ranks: dict[str, int],
    full_universe_priced: bool = True,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "option_id",
        "label",
        "asset_symbol",
        "entry_price",
        "exit_price",
        "entry_price_source",
        "exit_price_source",
        "return",
        "rank",
        "is_benchmark",
        "is_cash",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        available_options = [option for option in options if option.option_id in option_returns]
        for option in sorted(available_options, key=lambda item: ranks.get(item.option_id, 10**9)):
            writer.writerow(
                {
                    "option_id": option.option_id,
                    "label": option.label,
                    "asset_symbol": option.asset_symbol,
                    "entry_price": _price_for_csv(entry_prices, option),
                    "exit_price": _price_for_csv(exit_prices, option),
                    "entry_price_source": _price_source_for_csv(entry_prices, option),
                    "exit_price_source": _price_source_for_csv(exit_prices, option),
                    "return": option_returns[option.option_id],
                    "rank": ranks[option.option_id] if full_universe_priced else "",
                    "is_benchmark": option.is_benchmark,
                    "is_cash": option.is_cash,
                }
            )


def _write_price_warnings(path: Path, entry_prices: dict[str, PriceRecord], exit_prices: dict[str, PriceRecord]) -> None:
    warning_rows: list[dict[str, str]] = []
    for side, prices in [("entry", entry_prices), ("exit", exit_prices)]:
        for key, record in sorted(prices.items()):
            if record.price_source == "close":
                warning_rows.append(
                    {
                        "side": side,
                        "key": key,
                        "message": "close used because adj_close was not available",
                    }
                )
    if not warning_rows:
        if path.exists():
            path.unlink()
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump({"warnings": warning_rows}, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _write_leaderboard_csv(path: Path, scores: list[ScoreRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(ScoreRecord.model_fields.keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for score in scores:
            row = score.model_dump(mode="json")
            row["key_risks"] = "; ".join(row["key_risks"])
            writer.writerow(row)


def _score_submission(
    submission: ModelSubmission,
    option_returns: dict[str, float],
    ranks: dict[str, int],
    sp500_return: float,
    cash_return: float,
    best_return: float | None,
    full_universe_priced: bool,
) -> ScoreRecord:
    if submission.selected_option_id not in option_returns:
        raise ValueError(f"missing price data for selected option_id: {submission.selected_option_id}")
    selected_return = option_returns[submission.selected_option_id]
    alpha_vs_sp500 = selected_return - sp500_return
    alpha_per_dollar = None
    if submission.cost_usd is not None and submission.cost_usd > 0:
        alpha_per_dollar = alpha_vs_sp500 / submission.cost_usd
    return ScoreRecord(
        round_id=submission.round_id,
        model_id=submission.model_id,
        provider=submission.provider,
        mode=submission.mode,
        selected_option_id=submission.selected_option_id,
        confidence=submission.confidence,
        rationale_summary=submission.rationale_summary,
        key_risks=submission.key_risks,
        selected_asset_return=selected_return,
        sp500_return=sp500_return,
        alpha_vs_sp500=alpha_vs_sp500,
        regret_vs_best_option=(best_return - selected_return) if best_return is not None else None,
        rank_among_options=ranks.get(submission.selected_option_id) if full_universe_priced else None,
        beats_sp500=selected_return > sp500_return,
        beats_cash=selected_return > cash_return,
        cost_usd=submission.cost_usd,
        alpha_per_dollar=alpha_per_dollar,
    )


def _write_stability_returns_csv(
    path: Path,
    submissions: list[ModelSubmission],
    scores: list[ScoreRecord],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_key = {
        (score.model_id, submission.replicate_index): (submission, score)
        for submission, score in zip(submissions, scores)
    }
    fieldnames = [
        "model_id",
        "provider",
        "replicate_index",
        "replicate_count",
        "selected_option_id",
        "confidence",
        "selected_asset_return",
        "sp500_return",
        "alpha_vs_sp500",
        "regret_vs_best_option",
        "rank_among_options",
        "beats_sp500",
        "beats_cash",
        "cost_usd",
    ]
    rows = [
        (submission, score)
        for _key, (submission, score) in sorted(
            by_key.items(),
            key=lambda item: (item[0][0], item[0][1] or 0),
        )
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for submission, score in rows:
            writer.writerow(
                {
                    "model_id": score.model_id,
                    "provider": score.provider,
                    "replicate_index": submission.replicate_index,
                    "replicate_count": submission.replicate_count,
                    "selected_option_id": score.selected_option_id,
                    "confidence": score.confidence,
                    "selected_asset_return": score.selected_asset_return,
                    "sp500_return": score.sp500_return,
                    "alpha_vs_sp500": score.alpha_vs_sp500,
                    "regret_vs_best_option": score.regret_vs_best_option,
                    "rank_among_options": score.rank_among_options,
                    "beats_sp500": score.beats_sp500,
                    "beats_cash": score.beats_cash,
                    "cost_usd": "" if score.cost_usd is None else score.cost_usd,
                }
            )


def _raw_attempt_counts(run_paths: RunPaths) -> dict[str, dict[str, object]]:
    attempts: dict[str, dict[str, object]] = {}
    for raw_file in iter_submission_files(run_paths.raw_dir):
        try:
            payload = read_json(raw_file)
        except Exception:
            continue
        model_id = str(payload.get("model_id") or raw_file.stem)
        provider = str(payload.get("provider") or "")
        entry = attempts.setdefault(model_id, {"provider": provider, "raw_count": 0})
        entry["raw_count"] = int(entry["raw_count"]) + 1
        if provider and not entry.get("provider"):
            entry["provider"] = provider
    return attempts


def _write_stability_csv(
    path: Path,
    run_paths: RunPaths,
    submissions: list[ModelSubmission],
    scores: list[ScoreRecord],
    option_returns: dict[str, float],
    sp500_return: float,
    replicate_count: int,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "model_id",
        "provider",
        "replicate_count",
        "valid_replicates",
        "invalid_replicates",
        "selected_option_ids",
        "pick_distribution",
        "modal_pick",
        "modal_pick_count",
        "consistency_rate",
        "average_repeated_return",
        "average_repeated_alpha_vs_sp500",
        "best_replicate_return",
        "worst_replicate_return",
        "best_replicate_option_id",
        "worst_replicate_option_id",
        "modal_pick_return",
        "modal_pick_alpha_vs_sp500",
        "total_cost_usd",
        "average_cost_usd",
        "notes",
    ]
    raw_attempts = _raw_attempt_counts(run_paths)
    by_model: dict[str, list[tuple[ModelSubmission, ScoreRecord]]] = defaultdict(list)
    for submission, score in zip(submissions, scores):
        by_model[submission.model_id].append((submission, score))

    model_ids = sorted(set(raw_attempts) | set(by_model))
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for model_id in model_ids:
            pairs = sorted(by_model.get(model_id, []), key=lambda item: item[0].replicate_index or 0)
            valid_replicates = len(pairs)
            raw_count = int(raw_attempts.get(model_id, {}).get("raw_count") or valid_replicates)
            invalid_replicates = max(0, raw_count - valid_replicates)
            provider = str(raw_attempts.get(model_id, {}).get("provider") or (pairs[0][1].provider if pairs else ""))
            if not pairs:
                writer.writerow(
                    {
                        "model_id": model_id,
                        "provider": provider,
                        "replicate_count": replicate_count,
                        "valid_replicates": 0,
                        "invalid_replicates": invalid_replicates,
                        "notes": "No valid stability replicates.",
                    }
                )
                continue

            selected_option_ids = [score.selected_option_id for _submission, score in pairs]
            distribution = Counter(selected_option_ids)
            max_count = max(distribution.values())
            tied_modal_picks = sorted(
                [option_id for option_id, count in distribution.items() if count == max_count],
                key=lambda option_id: (-option_returns[option_id], option_id),
            )
            modal_pick = tied_modal_picks[0]
            notes = ""
            if len(tied_modal_picks) > 1:
                notes = "Modal pick tie resolved by highest realized return."

            returns = [score.selected_asset_return for _submission, score in pairs]
            best_pair = max(pairs, key=lambda item: (item[1].selected_asset_return, item[1].selected_option_id))
            worst_pair = min(pairs, key=lambda item: (item[1].selected_asset_return, item[1].selected_option_id))
            total_cost = sum(score.cost_usd for _submission, score in pairs if score.cost_usd is not None)
            has_cost = any(score.cost_usd is not None for _submission, score in pairs)
            average_return = sum(returns) / valid_replicates
            writer.writerow(
                {
                    "model_id": model_id,
                    "provider": provider,
                    "replicate_count": replicate_count,
                    "valid_replicates": valid_replicates,
                    "invalid_replicates": invalid_replicates,
                    "selected_option_ids": json.dumps(selected_option_ids),
                    "pick_distribution": json.dumps(dict(sorted(distribution.items())), sort_keys=True),
                    "modal_pick": modal_pick,
                    "modal_pick_count": max_count,
                    "consistency_rate": max_count / valid_replicates,
                    "average_repeated_return": average_return,
                    "average_repeated_alpha_vs_sp500": average_return - sp500_return,
                    "best_replicate_return": best_pair[1].selected_asset_return,
                    "worst_replicate_return": worst_pair[1].selected_asset_return,
                    "best_replicate_option_id": best_pair[1].selected_option_id,
                    "worst_replicate_option_id": worst_pair[1].selected_option_id,
                    "modal_pick_return": option_returns[modal_pick],
                    "modal_pick_alpha_vs_sp500": option_returns[modal_pick] - sp500_return,
                    "total_cost_usd": total_cost if has_cost else "",
                    "average_cost_usd": (total_cost / valid_replicates) if has_cost and valid_replicates else "",
                    "notes": notes,
                }
            )


def score_round(round_path: Path, run_id: str | None = None) -> list[ScoreRecord]:
    manifest = load_manifest(round_path)
    options = load_options(round_path)
    run_paths = get_selected_run_paths(round_path, run_id)
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    replicate_count = int(run_manifest.get("replicates") or 1)
    submissions = _load_parsed_submissions(run_paths, options, manifest.round_id, run_type, replicate_count)
    entry_prices = read_price_records(round_path / "prices" / "entry_prices.csv")
    exit_prices = read_price_records(round_path / "prices" / "exit_prices.csv")
    sp500_option = _find_sp500_option(options)
    selected_option_ids = {submission.selected_option_id for submission in submissions}
    required_option_ids = {sp500_option.option_id} | selected_option_ids
    required_option_ids.update(option.option_id for option in options if _is_cash_option(option))
    option_returns = calculate_option_returns(
        options,
        entry_prices,
        exit_prices,
        selected_option_ids,
        required_option_ids=required_option_ids,
    )
    ranks = rank_options(option_returns)
    if sp500_option.option_id not in option_returns:
        raise ValueError(f"missing return for SP500 benchmark option_id: {sp500_option.option_id}")
    sp500_return = option_returns[sp500_option.option_id]
    cash_return = _find_cash_return(options, option_returns)
    full_universe_priced = all(
        _is_cash_option(option) or option.option_id in option_returns
        for option in options
    )
    best_return = max(option_returns.values()) if full_universe_priced else None

    scores: list[ScoreRecord] = []
    for submission in submissions:
        scores.append(
            _score_submission(
                submission,
                option_returns,
                ranks,
                sp500_return,
                cash_return,
                best_return,
                full_universe_priced,
            )
        )

    scores.sort(
        key=lambda score: (
            -score.alpha_vs_sp500,
            score.regret_vs_best_option if score.regret_vs_best_option is not None else 0.0,
            -score.confidence,
            score.model_id,
        )
    )

    results_dir = run_paths.results_dir
    _write_price_warnings(results_dir / "price_warnings.json", entry_prices, exit_prices)
    if run_type == "stability":
        scores_by_submission = [
            _score_submission(
                submission,
                option_returns,
                ranks,
                sp500_return,
                cash_return,
                best_return,
                full_universe_priced,
            )
            for submission in submissions
        ]
        _write_stability_returns_csv(results_dir / "returns.csv", submissions, scores_by_submission)
        _write_stability_csv(
            results_dir / "stability.csv",
            run_paths,
            submissions,
            scores_by_submission,
            option_returns,
            sp500_return,
            replicate_count,
        )
        leaderboard_path = results_dir / "leaderboard.csv"
        if leaderboard_path.exists():
            leaderboard_path.unlink()
    else:
        _write_returns_csv(
            results_dir / "returns.csv",
            options,
            entry_prices,
            exit_prices,
            option_returns,
            ranks,
            full_universe_priced=full_universe_priced,
        )
        _write_leaderboard_csv(results_dir / "leaderboard.csv", scores)
        stability_path = results_dir / "stability.csv"
        if stability_path.exists():
            stability_path.unlink()
    return scores
