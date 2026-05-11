from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from .audit import audit_round
from .cumulative import cumulative_status, publish_cumulative, publish_latest
from .hashing import write_round_hashes
from .performance import fetch_universe_performance
from .prices import fetch_selected_prices
from .provider_smoke import check_provider_keys, smoke_provider
from .research import import_research_artifacts
from .report import publish_report, publish_round_summary
from .rounds import init_round
from .run_store import list_runs
from .runner import run_round
from .scoring import score_round
from .universe import validate_universe
from .validation import validate_submissions


def _load_local_env_file(path: Path = Path(".env")) -> None:
    """Load simple KEY=VALUE pairs from a local .env file without overriding env vars."""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def _cmd_init_round(args: argparse.Namespace) -> int:
    round_path = init_round(args.round_id, args.rounds_dir, universe_path=args.universe)
    print(f"initialized round: {round_path}")
    return 0


def _cmd_hash_round(args: argparse.Namespace) -> int:
    hashes = write_round_hashes(args.round)
    print(f"wrote hashes.json with {len(hashes['files'])} file hashes")
    return 0


def _cmd_import_research(args: argparse.Namespace) -> int:
    summary = import_research_artifacts(
        round_path=args.round,
        market_fact_report=args.market_fact_report,
        audit_report=args.audit_report,
        final_briefing=args.final_briefing,
        research_cutoff_utc=args.research_cutoff_utc,
    )
    print(f"research directory: {summary.research_dir}")
    for copied_file in summary.copied_files:
        print(f"copied: {copied_file}")
    print("copied final_briefing.md to briefing.md")
    print(f"wrote research manifest: {summary.research_manifest_path}")
    print(f"wrote research hashes: {summary.research_hashes_path}")
    print(f"updated round hashes: {summary.round_hashes_path}")
    for warning in summary.warnings:
        print(f"warning: {warning}", file=sys.stderr)
    return 0


def _cmd_validate_submissions(args: argparse.Namespace) -> int:
    summary = validate_submissions(args.round, run_id=args.run_id)
    print(f"raw submissions: {summary.raw_count}")
    print(f"valid submissions: {summary.valid_count}")
    print(f"invalid submissions: {summary.invalid_count}")
    return 0 if summary.invalid_count == 0 else 1


def _cmd_validate_universe(args: argparse.Namespace) -> int:
    output = validate_universe(
        options_path=args.options,
        round_path=args.round,
        start_date=args.start_date,
        end_date=args.end_date,
    )
    failed_count = len(output.report["failed_tickers"])
    print(f"validated options: {output.report['total_options']}")
    print(f"validated tickers: {len(output.report['validated_tickers'])}")
    print(f"failed tickers: {failed_count}")
    print(f"wrote universe validation JSON: {output.json_path}")
    print(f"wrote universe validation report: {output.markdown_path}")
    return 0 if failed_count == 0 else 1


def _cmd_fetch_prices(args: argparse.Namespace) -> int:
    output = fetch_selected_prices(
        round_path=args.round,
        run_id=args.run_id,
        entry_date=args.entry_date,
        exit_date=args.exit_date,
        overwrite_prices=args.overwrite_prices,
        full_universe=args.full_universe,
        price_side=args.side,
    )
    print(f"price scope: {output.price_scope}")
    print(f"price side: {output.price_side}")
    print(f"option ids: {', '.join(output.option_ids)}")
    print(f"fetched Tiingo symbols: {', '.join(output.fetched_symbols) if output.fetched_symbols else 'none'}")
    print(f"cash option ids: {', '.join(output.cash_option_ids) if output.cash_option_ids else 'none'}")
    if output.entry_prices_path is not None:
        print(f"wrote entry prices: {output.entry_prices_path}")
    if output.exit_prices_path is not None:
        print(f"wrote exit prices: {output.exit_prices_path}")
    return 0


def _cmd_fetch_universe_performance(args: argparse.Namespace) -> int:
    output = fetch_universe_performance(
        round_path=args.round,
        as_of_date=args.as_of_date,
        overwrite_performance=args.overwrite_performance,
    )
    print(f"universe options: {output.total_options}")
    print(f"fetched Tiingo symbols: {', '.join(output.fetched_symbols) if output.fetched_symbols else 'none'}")
    print(f"failed options: {', '.join(output.failed_options) if output.failed_options else 'none'}")
    print(f"wrote universe performance CSV: {output.csv_path}")
    print(f"wrote universe performance report: {output.markdown_path}")
    print(f"wrote universe performance JSON: {output.json_path}")
    return 0 if not output.failed_options else 1


def _cmd_score_round(args: argparse.Namespace) -> int:
    scores = score_round(args.round, run_id=args.run_id)
    print(f"wrote scoring results for {len(scores)} submissions")
    return 0


def _cmd_publish_report(args: argparse.Namespace) -> int:
    report_path = publish_report(args.round, run_id=args.run_id)
    print(f"wrote report: {report_path}")
    return 0


def _cmd_publish_round_summary(args: argparse.Namespace) -> int:
    summary_path = publish_round_summary(
        args.round,
        official_run_id=args.official_run_id,
        stability_run_id=args.stability_run_id,
    )
    print(f"wrote round summary: {summary_path}")
    return 0


def _cmd_publish_cumulative(args: argparse.Namespace) -> int:
    output = publish_cumulative(args.rounds_dir, args.output, selection_path=args.selection)
    for warning in output.status.warnings:
        print(f"warning: {warning}", file=sys.stderr)
    print(f"wrote official cumulative leaderboard: {output.official_leaderboard_path}")
    print(f"wrote stability cumulative leaderboard: {output.stability_leaderboard_path}")
    print(f"wrote round index: {output.round_index_path}")
    print(f"wrote cumulative report: {output.cumulative_report_path}")
    return 0


def _cmd_publish_latest(args: argparse.Namespace) -> int:
    output = publish_latest(args.rounds_dir, args.output, selection_path=args.selection)
    for warning in output.status.warnings:
        print(f"warning: {warning}", file=sys.stderr)
    print(f"wrote latest round leaderboard: {output.latest_leaderboard_path}")
    print(f"wrote latest round report: {output.latest_report_path}")
    return 0


def _cmd_cumulative_status(args: argparse.Namespace) -> int:
    status = cumulative_status(args.rounds_dir, selection_path=args.selection)
    print(f"discovered rounds: {len(status.selections) + len(status.skipped_rounds)}")
    for selected in status.selections:
        print(
            f"{selected.round_id}: "
            f"official={selected.official_run_id or 'none'} "
            f"stability={selected.stability_run_id or 'none'} "
            f"warnings={' | '.join(selected.warnings) if selected.warnings else 'none'}"
        )
    for round_id, warnings in status.skipped_rounds.items():
        print(f"{round_id}: skipped ({' | '.join(warnings)})")
    return 0


def _cmd_audit_round(args: argparse.Namespace) -> int:
    audit = audit_round(args.round, run_id=args.run_id)
    for line in audit.lines:
        print(line)
    return 0 if audit.ok else 1


def _cmd_run_round(args: argparse.Namespace) -> int:
    summary = run_round(
        round_path=args.round,
        models_path=args.models,
        pricing_path=args.pricing,
        mode=args.mode,
        mock=args.mock,
        allow_real_api_calls=args.allow_real_api_calls,
        run_id=args.run_id,
        overwrite_run=args.overwrite_run,
        run_type=args.run_type,
        replicates=args.replicates,
    )
    print(f"run_id: {summary.run_id}")
    print(f"models loaded: {summary.loaded_models}")
    print(f"models skipped: {summary.skipped_models}")
    for reason in summary.skipped_reasons:
        print(reason)
    print(f"models attempted: {summary.attempted_models}")
    print(f"valid submissions: {summary.valid_submissions}")
    print(f"invalid submissions: {summary.invalid_submissions}")
    print(f"run log: {summary.run_log_path}")
    return 0 if summary.invalid_submissions == 0 else 1


def _cmd_list_runs(args: argparse.Namespace) -> int:
    runs = list_runs(args.round)
    if not runs:
        print("no runs found")
        return 0
    print(
        "run_id\trun_type\treplicates\tcreated_at_utc\tmodel_count\tvalid\tinvalid\t"
        "scored\treport\tofficial_score_eligible"
    )
    for item in runs:
        print(
            "\t".join(
                [
                    item.run_id,
                    item.run_type,
                    "" if item.replicates is None else str(item.replicates),
                    item.created_at_utc,
                    "" if item.model_count is None else str(item.model_count),
                    "" if item.valid_submissions is None else str(item.valid_submissions),
                    "" if item.invalid_submissions is None else str(item.invalid_submissions),
                    "yes" if item.scored else "no",
                    "yes" if item.report_exists else "no",
                    "yes" if item.official_score_eligible else "no",
                ]
            )
        )
    return 0


def _cmd_check_providers(args: argparse.Namespace) -> int:
    for env_var, present in check_provider_keys().items():
        print(f"{env_var}: {'present' if present else 'missing'}")
    return 0


def _cmd_smoke_provider(args: argparse.Namespace) -> int:
    summary = smoke_provider(
        provider=args.provider,
        api_model_name=args.model,
        round_path=args.round,
        allow_real_api_calls=args.allow_real_api_calls,
    )
    print(f"provider: {summary.provider}")
    print(f"smoke_dir: {summary.smoke_dir}")
    print(f"validation_status: {summary.validation_status}")
    if summary.error:
        print(f"error: {summary.error}", file=sys.stderr)
    return 0 if summary.validation_status == "valid" else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="capitalbench")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init-round", help="create a round directory")
    init_parser.add_argument("--round-id", required=True)
    init_parser.add_argument("--rounds-dir", type=Path, default=Path("rounds"))
    init_parser.add_argument("--universe", type=Path)
    init_parser.set_defaults(func=_cmd_init_round)

    hash_parser = subparsers.add_parser("hash-round", help="hash round input files")
    hash_parser.add_argument("--round", type=Path, required=True)
    hash_parser.set_defaults(func=_cmd_hash_round)

    import_research_parser = subparsers.add_parser(
        "import-research",
        help="copy and hash round research artifacts",
    )
    import_research_parser.add_argument("--round", type=Path, required=True)
    import_research_parser.add_argument("--market-fact-report", type=Path, required=True)
    import_research_parser.add_argument("--audit-report", type=Path, required=True)
    import_research_parser.add_argument("--final-briefing", type=Path, required=True)
    import_research_parser.add_argument("--research-cutoff-utc", required=True)
    import_research_parser.set_defaults(func=_cmd_import_research)

    validate_parser = subparsers.add_parser("validate-submissions", help="validate raw submissions")
    validate_parser.add_argument("--round", type=Path, required=True)
    validate_parser.add_argument("--run-id")
    validate_parser.set_defaults(func=_cmd_validate_submissions)

    universe_parser = subparsers.add_parser("validate-universe", help="validate option tickers with Tiingo EOD data")
    universe_source = universe_parser.add_mutually_exclusive_group(required=True)
    universe_source.add_argument("--options", type=Path)
    universe_source.add_argument("--round", type=Path)
    universe_parser.add_argument("--start-date", required=True)
    universe_parser.add_argument("--end-date", required=True)
    universe_parser.set_defaults(func=_cmd_validate_universe)

    fetch_prices_parser = subparsers.add_parser(
        "fetch-prices",
        help="fetch Tiingo scoring prices",
    )
    fetch_prices_parser.add_argument("--round", type=Path, required=True)
    fetch_prices_parser.add_argument("--run-id")
    fetch_prices_parser.add_argument("--entry-date")
    fetch_prices_parser.add_argument("--exit-date")
    fetch_prices_parser.add_argument(
        "--side",
        choices=["entry", "exit", "both"],
        default="both",
        help="which price file to fetch; defaults to both entry and exit",
    )
    fetch_prices_parser.add_argument("--overwrite-prices", action="store_true")
    fetch_prices_parser.add_argument(
        "--full-universe",
        action="store_true",
        help="fetch every option in options.yaml instead of only selected options plus SP500 and cash",
    )
    fetch_prices_parser.set_defaults(func=_cmd_fetch_prices)

    fetch_performance_parser = subparsers.add_parser(
        "fetch-universe-performance",
        help="fetch Tiingo trailing returns for every option for prompt context",
    )
    fetch_performance_parser.add_argument("--round", type=Path, required=True)
    fetch_performance_parser.add_argument("--as-of-date", required=True)
    fetch_performance_parser.add_argument("--overwrite-performance", action="store_true")
    fetch_performance_parser.set_defaults(func=_cmd_fetch_universe_performance)

    score_parser = subparsers.add_parser("score-round", help="score parsed submissions")
    score_parser.add_argument("--round", type=Path, required=True)
    score_parser.add_argument("--run-id")
    score_parser.set_defaults(func=_cmd_score_round)

    report_parser = subparsers.add_parser("publish-report", help="write a Markdown report")
    report_parser.add_argument("--round", type=Path, required=True)
    report_parser.add_argument("--run-id")
    report_parser.set_defaults(func=_cmd_publish_report)

    round_summary_parser = subparsers.add_parser(
        "publish-round-summary",
        help="write a Markdown summary for separate official and stability runs",
    )
    round_summary_parser.add_argument("--round", type=Path, required=True)
    round_summary_parser.add_argument("--official-run-id", required=True)
    round_summary_parser.add_argument("--stability-run-id", required=True)
    round_summary_parser.set_defaults(func=_cmd_publish_round_summary)

    cumulative_parser = subparsers.add_parser(
        "publish-cumulative",
        help="aggregate official and stability results across resolved rounds",
    )
    cumulative_parser.add_argument("--rounds-dir", type=Path, required=True)
    cumulative_parser.add_argument("--output", type=Path, required=True)
    cumulative_parser.add_argument("--selection", type=Path)
    cumulative_parser.set_defaults(func=_cmd_publish_cumulative)

    latest_parser = subparsers.add_parser(
        "publish-latest",
        help="publish the newest resolved round's official one-shot leaderboard",
    )
    latest_parser.add_argument("--rounds-dir", type=Path, required=True)
    latest_parser.add_argument("--output", type=Path, required=True)
    latest_parser.add_argument("--selection", type=Path)
    latest_parser.set_defaults(func=_cmd_publish_latest)

    cumulative_status_parser = subparsers.add_parser(
        "cumulative-status",
        help="show cumulative round/run discovery status",
    )
    cumulative_status_parser.add_argument("--rounds-dir", type=Path, required=True)
    cumulative_status_parser.add_argument("--selection", type=Path)
    cumulative_status_parser.set_defaults(func=_cmd_cumulative_status)

    audit_parser = subparsers.add_parser("audit-round", help="audit round reproducibility and artifacts")
    audit_parser.add_argument("--round", type=Path, required=True)
    audit_parser.add_argument("--run-id")
    audit_parser.set_defaults(func=_cmd_audit_round)

    run_parser = subparsers.add_parser("run-round", help="run configured models for a round")
    run_parser.add_argument("--round", type=Path, required=True)
    run_parser.add_argument("--models", type=Path, required=True)
    run_parser.add_argument("--pricing", type=Path, default=None)
    run_parser.add_argument("--mode", default="closed_capability", choices=["closed_capability"])
    run_parser.add_argument("--run-id")
    run_parser.add_argument("--run-type", choices=["official", "stability", "mock", "retrospective"])
    run_parser.add_argument("--replicates", type=int)
    run_parser.add_argument("--overwrite-run", action="store_true")
    run_parser.add_argument("--mock", action="store_true", help="use deterministic mock responses")
    run_parser.add_argument(
        "--allow-real-api-calls",
        action="store_true",
        help="permit real provider API calls; costs may be incurred",
    )
    run_parser.set_defaults(func=_cmd_run_round)

    list_runs_parser = subparsers.add_parser("list-runs", help="list isolated runs for a round")
    list_runs_parser.add_argument("--round", type=Path, required=True)
    list_runs_parser.set_defaults(func=_cmd_list_runs)

    check_providers_parser = subparsers.add_parser("check-providers", help="check provider API key presence")
    check_providers_parser.set_defaults(func=_cmd_check_providers)

    smoke_parser = subparsers.add_parser("smoke-provider", help="run a private real-provider smoke test")
    smoke_parser.add_argument("--provider", required=True, choices=["openai", "anthropic", "google", "xai"])
    smoke_parser.add_argument("--model", required=True)
    smoke_parser.add_argument("--round", type=Path, required=True)
    smoke_parser.add_argument("--allow-real-api-calls", action="store_true")
    smoke_parser.set_defaults(func=_cmd_smoke_provider)

    return parser


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        _load_local_env_file()
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
