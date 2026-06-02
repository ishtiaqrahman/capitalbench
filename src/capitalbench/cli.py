from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from .audit import audit_round
from .automation import (
    accept_run,
    automation_run,
    automation_status,
    cancel_local_job,
    resolve_accepted_round,
    retry_local_job,
)
from .cumulative import cumulative_status, publish_cumulative, publish_latest
from .hashing import write_round_hashes
from .interim import DEFAULT_SNAPSHOTS_DIR, update_interim_performance
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
from .web_sync import (
    SUPABASE_SKIP_MESSAGE,
    configured_sink_from_env,
    optional_sync_cumulative,
    optional_sync_latest,
    optional_sync_round,
    sync_round,
    sync_rounds_dir,
)
from .weekly import update_weekly_performance


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


def _load_local_env_files() -> None:
    _load_local_env_file(Path(".env"))
    _load_local_env_file(Path(".env.local"))


def _cmd_init_round(args: argparse.Namespace) -> int:
    round_path = init_round(
        args.round_id,
        args.rounds_dir,
        universe_path=args.universe,
        universe_version=args.universe_version,
        submission_format=args.submission_format,
        horizon=args.horizon,
    )
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
    optional_sync_round(args.round, run_id=args.run_id, event_type="score_round")
    return 0


def _cmd_update_weekly_performance(args: argparse.Namespace) -> int:
    output = update_weekly_performance(
        args.round,
        args.run_id,
        snapshot_price_files=args.snapshot_price_file,
        snapshot_dates=args.snapshot_date,
    )
    print(f"weekly snapshots: {output.snapshot_count}")
    print(f"models: {output.model_count}")
    print(f"wrote weekly prices: {output.weekly_prices_path}")
    print(f"wrote weekly performance: {output.weekly_performance_path}")
    if not args.no_sync:
        optional_sync_round(args.round, run_id=args.run_id, event_type="update_weekly_performance")
    return 0


def _cmd_update_interim_performance(args: argparse.Namespace) -> int:
    output = update_interim_performance(
        rounds_dir=args.rounds_dir,
        snapshot_date=args.snapshot_date,
        snapshots_dir=args.snapshots_dir,
        universe_round=args.universe_round,
        track=args.track,
        skip_fetch=args.skip_fetch,
        overwrite_snapshot=args.overwrite_snapshot,
        sync=not args.no_sync,
        soft_fail=args.soft_fail,
    )
    print(f"snapshot date: {output.snapshot_date}")
    print(f"snapshot file: {output.snapshot_path}")
    print(f"snapshot status: {output.snapshot_status}")
    print(f"discovered reusable snapshots: {output.discovered_snapshot_count}")
    print(f"updated rounds: {len(output.updated_rounds)}")
    for item in output.updated_rounds:
        sync_note = f", sync={item.sync_status}" if item.sync_status else ""
        print(
            f"updated {item.round_id}/{item.run_id}: "
            f"{item.latest_snapshot_date}, snapshots={item.snapshot_count}, rows={item.performance_row_count}{sync_note}"
        )
        if item.sync_status == "failed" and item.sync_message:
            print(f"warning: {item.round_id} Supabase sync failed: {item.sync_message}", file=sys.stderr)
    skipped = [item for item in output.skipped_rounds if item.status != "skipped" or item.message != "not a monthly round"]
    print(f"skipped rounds: {len(skipped)}")
    for item in skipped:
        label = f"{item.round_id}/{item.run_id}" if item.run_id else item.round_id
        print(f"skipped {label}: {item.status}: {item.message}")
    for warning in output.warnings:
        print(f"warning: {warning}", file=sys.stderr)
    return 0


def _cmd_publish_report(args: argparse.Namespace) -> int:
    report_path = publish_report(args.round, run_id=args.run_id)
    print(f"wrote report: {report_path}")
    optional_sync_round(args.round, run_id=args.run_id, event_type="publish_report")
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
    output = publish_cumulative(args.rounds_dir, args.output, selection_path=args.selection, track=args.track)
    for warning in output.status.warnings:
        print(f"warning: {warning}", file=sys.stderr)
    print(f"wrote official cumulative leaderboard: {output.official_leaderboard_path}")
    print(f"wrote stability cumulative leaderboard: {output.stability_leaderboard_path}")
    print(f"wrote round index: {output.round_index_path}")
    print(f"wrote cumulative report: {output.cumulative_report_path}")
    optional_sync_cumulative(args.rounds_dir, selection_path=args.selection, event_type="publish_cumulative", track=args.track)
    return 0


def _cmd_publish_latest(args: argparse.Namespace) -> int:
    output = publish_latest(args.rounds_dir, args.output, selection_path=args.selection, track=args.track)
    for warning in output.status.warnings:
        print(f"warning: {warning}", file=sys.stderr)
    print(f"wrote latest round leaderboard: {output.latest_leaderboard_path}")
    print(f"wrote latest round report: {output.latest_report_path}")
    optional_sync_latest(args.rounds_dir, selection_path=args.selection, event_type="publish_latest", track=args.track)
    return 0


def _cmd_cumulative_status(args: argparse.Namespace) -> int:
    status = cumulative_status(args.rounds_dir, selection_path=args.selection, track=args.track)
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


def _cmd_accept_run(args: argparse.Namespace) -> int:
    summary = accept_run(
        args.round,
        run_id=args.run_id,
        schedule_resolution=not args.no_schedule_resolution,
        due_at_utc=args.due_at_utc,
        sync_pending=not args.no_sync,
    )
    _print_automation_summary(summary)
    return 0


def _cmd_automation_resolve(args: argparse.Namespace) -> int:
    summary = resolve_accepted_round(
        args.rounds_dir,
        round_id=args.round_id,
        run_id=args.run_id,
        latest_output=args.latest_output,
        cumulative_output=args.cumulative_output,
        selection_path=args.selection,
        fetch_exit_prices=not args.skip_fetch_prices,
        overwrite_prices=args.overwrite_prices,
        full_universe_prices=not args.selected_prices_only,
        sync=not args.no_sync,
    )
    _print_automation_summary(summary)
    return 0


def _cmd_automation_run(args: argparse.Namespace) -> int:
    summaries = automation_run(
        args.rounds_dir,
        due_before_utc=args.due_before_utc,
        max_jobs=args.max_jobs,
        latest_output=args.latest_output,
        cumulative_output=args.cumulative_output,
        selection_path=args.selection,
        worker_id=args.worker_id,
    )
    if not summaries:
        print("no due automation jobs")
    for summary in summaries:
        _print_automation_summary(summary)
    return 1 if any(summary.status == "failed" for summary in summaries) else 0


def _cmd_automation_status(args: argparse.Namespace) -> int:
    rows = automation_status(args.rounds_dir)
    if not rows:
        print("no local automation jobs found")
        return 0
    print("round_id\trun_id\tstatus\tdue_at_utc\tnext_attempt_at_utc\tlast_error")
    for row in rows:
        print(
            "\t".join(
                [
                    str(row.get("round_id") or ""),
                    str(row.get("run_id") or ""),
                    str(row.get("status") or ""),
                    str(row.get("due_at_utc") or ""),
                    str(row.get("next_attempt_at_utc") or ""),
                    str(row.get("last_error") or ""),
                ]
            )
        )
    return 0


def _cmd_automation_retry(args: argparse.Namespace) -> int:
    summary = retry_local_job(args.round, next_attempt_at_utc=args.next_attempt_at_utc)
    _print_automation_summary(summary)
    return 0


def _cmd_automation_cancel(args: argparse.Namespace) -> int:
    summary = cancel_local_job(args.round)
    _print_automation_summary(summary)
    return 0


def _cmd_sync_web(args: argparse.Namespace) -> int:
    sink = configured_sink_from_env()
    if sink is None:
        print(SUPABASE_SKIP_MESSAGE)
        return 0
    if args.round is not None:
        summary = sync_round(args.round, run_id=args.run_id, event_type="sync_web", sink=sink)
        _print_sync_summary(summary)
        return 0
    if args.run_id:
        raise ValueError("--run-id can only be used with --round")
    summaries = sync_rounds_dir(
        args.rounds_dir,
        include_cumulative=args.include_cumulative,
        selection_path=args.selection,
        event_type="sync_web",
        sink=sink,
    )
    for summary in summaries:
        _print_sync_summary(summary)
    return 0


def _print_sync_summary(summary) -> None:
    label = summary.round_id or "global"
    if summary.run_id:
        label = f"{label}/{summary.run_id}"
    row_counts = ", ".join(f"{table}={count}" for table, count in summary.row_counts.items()) or "no rows"
    print(f"synced {label}: {summary.status} ({row_counts})")
    if summary.message:
        print(summary.message)


def _print_automation_summary(summary) -> None:
    label = f"{summary.round_id}/{summary.run_id}"
    due = f" due_at_utc={summary.due_at_utc}" if summary.due_at_utc else ""
    job = f" job_id={summary.job_id}" if summary.job_id else ""
    message = f" {summary.message}" if summary.message else ""
    print(f"automation {label}: {summary.status}{job}{due}{message}")
    for key, value in summary.outputs.items():
        print(f"{key}: {value}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="capitalbench")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init-round", help="create a round directory")
    init_parser.add_argument("--round-id", required=True)
    init_parser.add_argument("--rounds-dir", type=Path, default=Path("rounds"))
    init_parser.add_argument("--universe", type=Path)
    init_parser.add_argument(
        "--universe-version",
        help="version label written to manifest.yaml; defaults to v2.1 when using the built-in latest universe, or to the --universe filename stem when a custom file is passed",
    )
    init_parser.add_argument("--submission-format", choices=["single_pick", "portfolio"], default="single_pick")
    init_parser.add_argument("--horizon", default="one month", help='round horizon label, for example "one week"')
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

    weekly_parser = subparsers.add_parser(
        "update-weekly-performance",
        help="calculate interim weekly model performance from existing price snapshots",
    )
    weekly_parser.add_argument("--round", type=Path, required=True)
    weekly_parser.add_argument("--run-id", required=True)
    weekly_parser.add_argument(
        "--snapshot-price-file",
        type=Path,
        action="append",
        default=[],
        help="price CSV for a weekly snapshot after the entry date; repeat with --snapshot-date",
    )
    weekly_parser.add_argument(
        "--snapshot-date",
        action="append",
        default=[],
        help="target date for the corresponding --snapshot-price-file in YYYY-MM-DD format",
    )
    weekly_parser.add_argument("--no-sync", action="store_true", help="write local artifacts without Supabase sync")
    weekly_parser.set_defaults(func=_cmd_update_weekly_performance)

    interim_parser = subparsers.add_parser(
        "update-interim-performance",
        help="fetch one reusable daily snapshot and update active interim performance charts",
    )
    interim_parser.add_argument("--rounds-dir", type=Path, required=True)
    interim_parser.add_argument("--snapshot-date", required=True, help="daily close date to fetch or reuse, YYYY-MM-DD")
    interim_parser.add_argument(
        "--snapshots-dir",
        type=Path,
        default=DEFAULT_SNAPSHOTS_DIR,
        help=f"directory for reusable full-universe daily snapshots; defaults to {DEFAULT_SNAPSHOTS_DIR}",
    )
    interim_parser.add_argument(
        "--universe-round",
        type=Path,
        help="round whose options.yaml should define the daily snapshot universe; defaults to newest round",
    )
    interim_parser.add_argument("--track", choices=["monthly", "all"], default="monthly")
    interim_parser.add_argument(
        "--skip-fetch",
        action="store_true",
        help="reuse existing central/round price snapshots without calling Tiingo",
    )
    interim_parser.add_argument(
        "--overwrite-snapshot",
        action="store_true",
        help="replace an existing central daily snapshot for the requested date",
    )
    interim_parser.add_argument("--no-sync", action="store_true", help="write local artifacts without Supabase sync")
    interim_parser.add_argument(
        "--soft-fail",
        action="store_true",
        help="log snapshot-fetch failures and keep the workflow green when market data is unavailable",
    )
    interim_parser.set_defaults(func=_cmd_update_interim_performance)

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
    cumulative_parser.add_argument("--track", choices=["weekly", "monthly"])
    cumulative_parser.set_defaults(func=_cmd_publish_cumulative)

    latest_parser = subparsers.add_parser(
        "publish-latest",
        help="publish the newest resolved round's official one-shot leaderboard",
    )
    latest_parser.add_argument("--rounds-dir", type=Path, required=True)
    latest_parser.add_argument("--output", type=Path, required=True)
    latest_parser.add_argument("--selection", type=Path)
    latest_parser.add_argument("--track", choices=["weekly", "monthly"])
    latest_parser.set_defaults(func=_cmd_publish_latest)

    cumulative_status_parser = subparsers.add_parser(
        "cumulative-status",
        help="show cumulative round/run discovery status",
    )
    cumulative_status_parser.add_argument("--rounds-dir", type=Path, required=True)
    cumulative_status_parser.add_argument("--selection", type=Path)
    cumulative_status_parser.add_argument("--track", choices=["weekly", "monthly"])
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

    accept_parser = subparsers.add_parser(
        "accept-run",
        help="accept a valid official run and schedule automated resolution",
    )
    accept_parser.add_argument("--round", type=Path, required=True)
    accept_parser.add_argument("--run-id", required=True)
    accept_parser.add_argument(
        "--due-at-utc",
        help="override resolution due time, e.g. 2026-06-10T23:30:00+00:00",
    )
    accept_parser.add_argument(
        "--no-schedule-resolution",
        action="store_true",
        help="accept the run without creating an automation job",
    )
    accept_parser.add_argument("--no-sync", action="store_true", help="skip pending Supabase sync during acceptance")
    accept_parser.set_defaults(func=_cmd_accept_run)

    automation_resolve_parser = subparsers.add_parser(
        "automation-resolve",
        help="resolve one accepted due round immediately",
    )
    automation_resolve_parser.add_argument("--rounds-dir", type=Path, required=True)
    automation_resolve_parser.add_argument("--round-id", required=True)
    automation_resolve_parser.add_argument("--run-id", required=True)
    automation_resolve_parser.add_argument("--latest-output", type=Path, default=Path("latest"))
    automation_resolve_parser.add_argument("--cumulative-output", type=Path, default=Path("cumulative"))
    automation_resolve_parser.add_argument("--selection", type=Path)
    automation_resolve_parser.add_argument("--skip-fetch-prices", action="store_true")
    automation_resolve_parser.add_argument("--overwrite-prices", action="store_true")
    automation_resolve_parser.add_argument("--selected-prices-only", action="store_true")
    automation_resolve_parser.add_argument("--no-sync", action="store_true")
    automation_resolve_parser.set_defaults(func=_cmd_automation_resolve)

    automation_run_parser = subparsers.add_parser(
        "automation-run",
        help="claim and run due automated resolution jobs",
    )
    automation_run_parser.add_argument("--rounds-dir", type=Path, required=True)
    automation_run_parser.add_argument("--due-before-utc")
    automation_run_parser.add_argument("--max-jobs", type=int, default=3)
    automation_run_parser.add_argument("--latest-output", type=Path, default=Path("latest"))
    automation_run_parser.add_argument("--cumulative-output", type=Path, default=Path("cumulative"))
    automation_run_parser.add_argument("--selection", type=Path)
    automation_run_parser.add_argument("--worker-id")
    automation_run_parser.set_defaults(func=_cmd_automation_run)

    automation_status_parser = subparsers.add_parser("automation-status", help="list local automation jobs")
    automation_status_parser.add_argument("--rounds-dir", type=Path, required=True)
    automation_status_parser.set_defaults(func=_cmd_automation_status)

    automation_retry_parser = subparsers.add_parser("automation-retry", help="retry a local automation job")
    automation_retry_parser.add_argument("--round", type=Path, required=True)
    automation_retry_parser.add_argument("--next-attempt-at-utc")
    automation_retry_parser.set_defaults(func=_cmd_automation_retry)

    automation_cancel_parser = subparsers.add_parser("automation-cancel", help="cancel a local automation job")
    automation_cancel_parser.add_argument("--round", type=Path, required=True)
    automation_cancel_parser.set_defaults(func=_cmd_automation_cancel)

    sync_parser = subparsers.add_parser(
        "sync-web",
        help="sync published benchmark artifacts to Supabase for the public website",
    )
    sync_source = sync_parser.add_mutually_exclusive_group(required=True)
    sync_source.add_argument("--round", type=Path)
    sync_source.add_argument("--rounds-dir", type=Path)
    sync_parser.add_argument("--run-id")
    sync_parser.add_argument(
        "--include-cumulative",
        action="store_true",
        help="also sync latest and cumulative leaderboard read tables when using --rounds-dir",
    )
    sync_parser.add_argument("--selection", type=Path)
    sync_parser.set_defaults(func=_cmd_sync_web)

    return parser


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        _load_local_env_files()
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
