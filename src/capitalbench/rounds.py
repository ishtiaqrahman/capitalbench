from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from .io import write_json, write_yaml

ROUND_FILES = ["manifest.yaml", "briefing.md", "options.yaml", "prompt.md", "hashes.json"]
ROUND_DIRS = ["prices", "runs"]
DEFAULT_UNIVERSE_PATH = Path("configs/universes/capitalbench_universe_v2_1.yaml")
DEFAULT_UNIVERSE_VERSION = "v2.1"
SubmissionFormat = Literal["single_pick", "portfolio"]


def init_round(
    round_id: str,
    rounds_dir: Path = Path("rounds"),
    universe_path: Path | None = None,
    universe_version: str | None = None,
    submission_format: SubmissionFormat = "single_pick",
    horizon: str = "one month",
) -> Path:
    round_id = round_id.strip()
    if not round_id:
        raise ValueError("round_id is required")
    if submission_format not in {"single_pick", "portfolio"}:
        raise ValueError("submission_format must be one of: single_pick, portfolio")
    horizon = _normalize_horizon(horizon)
    horizon_label = horizon.replace(" ", "-").capitalize()
    if universe_path is None and (default_universe_path := _default_universe_path()) is not None:
        universe_path = default_universe_path
        universe_version = universe_version or DEFAULT_UNIVERSE_VERSION

    round_path = rounds_dir / round_id
    for dirname in ROUND_DIRS:
        (round_path / dirname).mkdir(parents=True, exist_ok=True)
    resolved_universe_version = (universe_version or (universe_path.stem if universe_path is not None else "")).strip()

    manifest_path = round_path / "manifest.yaml"
    if not manifest_path.exists():
        write_yaml(
            manifest_path,
            {
                "round_id": round_id,
                "title": f"CapitalBench {round_id}",
                "description": f"{horizon_label} market allocation evaluation round.",
                "decision_date": None,
                "decision_deadline": None,
                "horizon": horizon,
                "methodology_version": "portfolio-v1.0" if submission_format == "portfolio" else "single_pick-v1.0",
                "universe_version": resolved_universe_version or None,
                "submission_format": submission_format,
                "portfolio_constraints": {
                    "min_holdings": 1,
                    "max_holdings": 5,
                    "allocation_increment_pct": 5,
                    "min_allocation_pct": 5,
                    "max_total_allocation_pct": 100,
                    "allow_cash": True,
                    "allow_benchmark_asset": True,
                },
                "entry_rule": "Use the official entry prices supplied in prices/entry_prices.csv.",
                "exit_rule": "Use the official exit prices supplied in prices/exit_prices.csv.",
                "entry_date": None,
                "exit_date": None,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "notes": "",
            },
        )

    briefing_path = round_path / "briefing.md"
    if not briefing_path.exists():
        briefing_path.write_text(
            "# Market Briefing\n\nAdd the time-resolved market briefing for this round.\n",
            encoding="utf-8",
        )

    prompt_path = round_path / "prompt.md"
    if not prompt_path.exists():
        prompt_path.write_text(
            _default_prompt_text(submission_format, horizon),
            encoding="utf-8",
        )

    options_path = round_path / "options.yaml"
    if universe_path is not None and not options_path.exists():
        options_path.write_text(universe_path.read_text(encoding="utf-8"), encoding="utf-8")
    elif not options_path.exists():
        write_yaml(
            options_path,
            {
                "options": [
                    {
                        "option_id": "sp500",
                        "label": "S&P 500",
                        "asset_symbol": "SPY",
                        "asset_name": "S&P 500 ETF proxy",
                        "description": "Benchmark equity exposure.",
                        "kind": "benchmark",
                        "is_benchmark": True,
                        "is_cash": False,
                    },
                    {
                        "option_id": "cash",
                        "label": "Cash",
                        "asset_symbol": "USD",
                        "asset_name": "US dollar cash",
                        "description": "Uninvested cash position.",
                        "kind": "cash",
                        "is_benchmark": False,
                        "is_cash": True,
                    },
                ]
            },
        )

    hashes_path = round_path / "hashes.json"
    if not hashes_path.exists():
        write_json(hashes_path, {})

    return round_path


def _normalize_horizon(horizon: str) -> str:
    normalized = " ".join(str(horizon or "one month").strip().lower().split())
    return normalized or "one month"


def _default_universe_path() -> Path | None:
    candidates = [
        DEFAULT_UNIVERSE_PATH,
        Path(__file__).resolve().parents[2] / DEFAULT_UNIVERSE_PATH,
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def _apply_horizon(prompt: str, horizon: str) -> str:
    horizon = _normalize_horizon(horizon)
    if horizon == "one month":
        return prompt
    return prompt.replace("one-month", horizon.replace(" ", "-")).replace("one month", horizon)


def _default_prompt_text(submission_format: SubmissionFormat = "single_pick", horizon: str = "one month") -> str:
    if submission_format == "portfolio":
        return _apply_horizon("""# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make saved market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

The scoring timeline is central to the task: the portfolio is measured from the adjusted close on the entry date to the adjusted close on the exit date, calculated after regular trading ends on the exit date. Optimize for facts, catalysts, positioning, liquidity, and risks that can plausibly affect prices before that exit close.

Optimize only for the portfolio you expect to perform best over this close-to-close one-month scoring window. Use longer-horizon facts only when they are likely to affect prices before the exit close.

Briefing-bias discipline: the briefing may group facts by broad asset area and include a mechanical return table. Treat inclusion, section order, grouping, row count, and trailing-return table order as context, not recommendation signals.

Your objective is to allocate 100% across the allowed options to maximize expected one-month realized portfolio return, measured from the entry date to the exit date, relative to the S&P 500 benchmark. Use the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by realized weighted portfolio return relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official leaderboard.

Your portfolio is scored by the weighted realized percentage return over the one-month round window. Alpha is portfolio return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

You may use your internal learned knowledge and general market priors. Do not browse, use tools, request updated market data, use external retrieval, or intentionally rely on facts, market prices, news, or events dated after the research cutoff. If your internal knowledge conflicts with the briefing, prioritize the briefing.

You must allocate exactly 100% across allowed options. Use only the holding count, allocation increment, minimum allocation, and cash or benchmark constraints stated in the round metadata. Do not short, use leverage, or choose an option outside the allowed option list.

Return only valid JSON. Do not include markdown, prose, citations, or commentary outside the JSON.

Required JSON format:

{
  "round_id": "<round_id>",
  "model_id": "<model_id>",
  "provider": "<provider>",
  "mode": "closed_capability",
  "portfolio": [
    {
      "option_id": "<one allowed option ID>",
      "allocation_pct": <integer percentage>,
      "rationale": "<brief holding-level rationale>"
    }
  ],
  "confidence": <number from 0 to 1>,
  "portfolio_rationale": "<1-3 sentence allocation rationale>",
  "rationale_summary": "<1-3 sentence rationale>",
  "key_risks": [
    "<risk 1>",
    "<risk 2>"
  ]
}

Rules:
- portfolio must contain only IDs from the allowed option list.
- allocation_pct values must be integers in the stated allocation increment.
- allocation_pct values must sum to exactly 100.
- confidence must be between 0 and 1.
- confidence should reflect your confidence that this is the best portfolio decision under the round constraints.
- portfolio_rationale and rationale_summary are required and should be concise.
- key_risks must be a list of 2-5 concrete risks that could cause the portfolio to underperform; do not only list generic market risk.
- Do not provide a ranked list, backup portfolio, second-best portfolio, or alternative recommendation.
- Do not include financial-advice disclaimers. This is a benchmark response, not advice to a person.
- The JSON object must contain no extra fields.
""", horizon)
    return _apply_horizon("""# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make saved market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

The scoring timeline is central to the task: the selected option is measured from the adjusted close on the entry date to the adjusted close on the exit date, calculated after regular trading ends on the exit date. Optimize for facts, catalysts, positioning, liquidity, and risks that can plausibly affect prices before that exit close.

Optimize only for the option you expect to perform best over this close-to-close one-month scoring window. Use longer-horizon facts only when they are likely to affect prices before the exit close.

Briefing-bias discipline: the briefing may group facts by broad asset area and include a mechanical return table. Treat inclusion, section order, grouping, row count, and trailing-return table order as context, not recommendation signals.

Your objective is to choose the single allowed option you expect to produce the strongest expected one-month realized return, measured from the entry date to the exit date, relative to the S&P 500 benchmark. Use the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by the realized return of its selected option relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official leaderboard.

Your selected option is scored by its realized percentage return over the one-month round window. Alpha is selected option return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

You may use your internal learned knowledge and general market priors. Do not browse, use tools, request updated market data, use external retrieval, or intentionally rely on facts, market prices, news, or events dated after the research cutoff. If your internal knowledge conflicts with the briefing, prioritize the briefing.

You must select exactly one option. Do not allocate across multiple options. Do not hedge. CASH is a valid option.

Return only valid JSON. Do not include markdown, prose, citations, or commentary outside the JSON.

Required JSON format:

{
  "round_id": "<round_id>",
  "model_id": "<model_id>",
  "provider": "<provider>",
  "mode": "closed_capability",
  "selected_option_id": "<one allowed option ID>",
  "confidence": <number from 0 to 1>,
  "rationale_summary": "<1-3 sentence rationale>",
  "key_risks": [
    "<risk 1>",
    "<risk 2>"
  ]
}

Rules:
- selected_option_id must be exactly one ID from the allowed option list.
- confidence must be between 0 and 1.
- confidence should reflect your confidence that this is the best single choice among the allowed options for this round.
- rationale_summary is required and should be 1-3 concise sentences.
- key_risks must be a list of 2-5 concrete risks that could cause the selected option to underperform; do not only list generic market risk.
- Do not provide a ranked list, backup choice, second-best option, or alternative recommendation.
- Do not include financial-advice disclaimers. This is a benchmark response, not advice to a person.
- The JSON object must contain no extra fields.
- Do not recommend a portfolio.
- Do not choose multiple options.
""", horizon)
