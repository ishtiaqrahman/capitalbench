from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from .io import write_json, write_yaml
from .methodology import PORTFOLIO_V2_VERSION, is_production_portfolio_v2

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
    methodology_version: str | None = None,
) -> Path:
    round_id = round_id.strip()
    if not round_id:
        raise ValueError("round_id is required")
    if submission_format not in {"single_pick", "portfolio"}:
        raise ValueError("submission_format must be one of: single_pick, portfolio")
    horizon = _normalize_horizon(horizon)
    resolved_methodology_version = (
        methodology_version.strip()
        if methodology_version
        else (PORTFOLIO_V2_VERSION if submission_format == "portfolio" else "single_pick-v1.0")
    )
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
                "methodology_version": resolved_methodology_version,
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
                    "max_economic_exposure_pct": (
                        50 if is_production_portfolio_v2(resolved_methodology_version) else None
                    ),
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
            _default_prompt_text(submission_format, horizon, resolved_methodology_version),
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

    submission_schema_path = round_path / "submission_schema.json"
    if (
        is_production_portfolio_v2(resolved_methodology_version)
        and not submission_schema_path.exists()
    ):
        write_json(
            submission_schema_path,
            _portfolio_v2_submission_schema(resolved_methodology_version),
        )

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


def _portfolio_v2_submission_schema(methodology_version: str = PORTFOLIO_V2_VERSION) -> dict[str, object]:
    candidate_properties = {
        "option_id": {"type": "string", "minLength": 1},
        "decision": {"enum": ["selected", "rejected"]},
        "forecast_low_pct": {"type": "number"},
        "forecast_base_pct": {"type": "number"},
        "forecast_high_pct": {"type": "number"},
        "evidence": {
            "type": "array",
            "minItems": 1,
            "maxItems": 3,
            "items": {"type": "string", "minLength": 1},
        },
        "continuation_case": {"type": "string", "minLength": 1},
        "reversal_case": {"type": "string", "minLength": 1},
        "time_window_catalyst": {"type": "string", "minLength": 1},
        "invalidation_condition": {"type": "string", "minLength": 1},
    }
    holding_properties = {
        "option_id": {"type": "string", "minLength": 1},
        "allocation_pct": {"type": "integer", "minimum": 5, "maximum": 100, "multipleOf": 5},
        "expected_return_pct": {"type": "number"},
        "time_window_catalyst": {"type": "string", "minLength": 1},
        "invalidation_condition": {"type": "string", "minLength": 1},
        "rationale": {"type": "string", "minLength": 1},
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://capitalbench.org/schemas/portfolio_submission_v2.json",
        "title": f"CapitalBench {methodology_version} Submission",
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "round_id": {"type": "string", "minLength": 1},
            "model_id": {"type": "string", "minLength": 1},
            "provider": {"enum": ["openai", "anthropic", "google", "xai"]},
            "mode": {"const": "closed_capability"},
            "candidate_ledger": {
                "type": "array",
                "minItems": 6,
                "maxItems": 8,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": candidate_properties,
                    "required": list(candidate_properties),
                },
            },
            "portfolio": {
                "type": "array",
                "minItems": 1,
                "maxItems": 5,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": holding_properties,
                    "required": list(holding_properties),
                },
            },
            "benchmark_expected_return_pct": {"type": "number"},
            "portfolio_expected_return_pct": {"type": "number"},
            "expected_alpha_vs_sp500_pct": {"type": "number"},
            "confidence": {"type": "number", "minimum": 0, "maximum": 1},
            "portfolio_rationale": {"type": "string", "minLength": 1},
            "rationale_summary": {"type": "string", "minLength": 1},
            "key_risks": {
                "type": "array",
                "minItems": 2,
                "maxItems": 5,
                "items": {"type": "string", "minLength": 1},
            },
        },
        "required": [
            "round_id",
            "model_id",
            "provider",
            "mode",
            "candidate_ledger",
            "portfolio",
            "benchmark_expected_return_pct",
            "portfolio_expected_return_pct",
            "expected_alpha_vs_sp500_pct",
            "confidence",
            "portfolio_rationale",
            "rationale_summary",
            "key_risks",
        ],
    }


def _default_prompt_text(
    submission_format: SubmissionFormat = "single_pick",
    horizon: str = "one month",
    methodology_version: str | None = None,
) -> str:
    if submission_format == "portfolio":
        if is_production_portfolio_v2(methodology_version):
            return _portfolio_v2_prompt_text(horizon, methodology_version)
        return _apply_horizon("""# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make saved market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

The scoring timeline is central to the task: the portfolio is measured from the adjusted close on the entry date to the adjusted close on the exit date, calculated after regular trading ends on the exit date. Optimize for facts, catalysts, positioning, liquidity, and risks that can plausibly affect prices before that exit close.

Optimize only for the portfolio you expect to perform best over this close-to-close one-month scoring window. Use longer-horizon facts only when they are likely to affect prices before the exit close.

Briefing-bias discipline: the briefing may group facts by broad asset area and include a mechanical price-context table. Treat inclusion, section order, grouping, row count, and price-context table order as context, not recommendation signals.

Price-history discipline: trailing returns are descriptive data, not forecasts. Use price history as one input, not as a standalone reason to allocate to an option. When recent performance matters to a holding, compare it with the briefing's catalysts, macro context, valuation or fundamental facts if supplied, volatility, drawdown, and reversal risk before the exit close.

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
- If a holding rationale cites momentum, recent returns, or trailing performance, do not present price history alone as independent evidence. Mention any independent support present in the briefing, or state that support is limited, and include the relevant reversal or positioning risk in key_risks.
- key_risks must be a list of 2-5 concrete risks that could cause the portfolio to underperform; do not only list generic market risk.
- Do not provide a ranked list, backup portfolio, second-best portfolio, or alternative recommendation.
- Do not include financial-advice disclaimers. This is a benchmark response, not advice to a person.
- The JSON object must contain no extra fields.
""", horizon)
    return _single_pick_prompt_text(horizon)


def _portfolio_v2_prompt_text(horizon: str, methodology_version: str | None = None) -> str:
    version = methodology_version or PORTFOLIO_V2_VERSION
    template = """# CapitalBench __METHODOLOGY_VERSION__ Task

You are participating in an offline, time-resolved CapitalBench evaluation round. Every model receives the same frozen information and makes one single-turn, non-agentic decision without tools, browsing, retrieval, or follow-up.

Your objective is to allocate 100% across the allowed options to maximize expected realized portfolio return over the close-to-close one-month scoring window. The official comparison is the S&P 500 (SPY): alpha equals portfolio return minus SPY return. A 100% SPY portfolio is valid when no active option has a stronger base-case forecast.

Use only facts and mechanical market data supplied in this input. You may use internal learned knowledge and general priors, but do not intentionally rely on facts, prices, news, or events after the research cutoff. Treat section order, mention count, option order, and table order as neutral presentation choices rather than recommendation signals.

Price history is descriptive, not a forecast. Test both continuation and reversal for every finalist. A recent winner needs independent support in the supplied briefing or an explicitly stated weak-evidence caveat. Optimize for the stated horizon only.

Complete the decision in this order:

1. Assess SPY and 5-7 additional finalists, for a total candidate ledger of 6-8 unique options.
2. Include SPY in the ledger and span at least four listed economic-exposure clusters.
3. Give every candidate a low, base, and high return forecast in percentage points, with low <= base <= high.
4. Record concise supplied evidence, the continuation case, reversal case, time-window catalyst, and invalidation condition for every candidate. Keep rejected finalists in the ledger.
5. Select only active holdings whose base forecast is greater than SPY's base forecast. CASH is not an active holding. If no active option clears that hurdle, use SPY and/or CASH.
6. Construct the final 1-5 holding portfolio in the stated allocation increments. Outside SPY and CASH, no economic-exposure cluster may exceed the round's stated maximum.
7. Set each holding's expected_return_pct equal to that candidate's base forecast. Calculate the weighted portfolio base return and expected alpha versus SPY.

Return only valid JSON. Do not include markdown, citations, prose, or commentary outside the JSON.

Required JSON format:

{
  "round_id": "<round_id>",
  "model_id": "<model_id>",
  "provider": "<provider>",
  "mode": "closed_capability",
  "candidate_ledger": [
    {
      "option_id": "<allowed option ID>",
      "decision": "selected or rejected",
      "forecast_low_pct": <number>,
      "forecast_base_pct": <number>,
      "forecast_high_pct": <number>,
      "evidence": ["<1-3 concise facts from the supplied input>"],
      "continuation_case": "<what supports continuation>",
      "reversal_case": "<what could reverse the signal>",
      "time_window_catalyst": "<catalyst before the exit close, or none identified>",
      "invalidation_condition": "<observable condition that would invalidate the case>"
    }
  ],
  "portfolio": [
    {
      "option_id": "<selected candidate option ID>",
      "allocation_pct": <integer percentage>,
      "expected_return_pct": <same number as candidate forecast_base_pct>,
      "time_window_catalyst": "<same time-window catalyst>",
      "invalidation_condition": "<same invalidation condition>",
      "rationale": "<brief holding-level rationale>"
    }
  ],
  "benchmark_expected_return_pct": <SPY base forecast>,
  "portfolio_expected_return_pct": <weighted portfolio base forecast>,
  "expected_alpha_vs_sp500_pct": <portfolio forecast minus SPY forecast>,
  "confidence": <probability from 0 to 1 that the portfolio beats SPY>,
  "portfolio_rationale": "<1-3 concise sentences>",
  "rationale_summary": "<1-3 concise sentences>",
  "key_risks": ["<risk 1>", "<risk 2>"]
}

Rules:
- candidate_ledger must contain 6-8 unique allowed option IDs, include SPY, and span at least four economic-exposure clusters.
- candidate forecasts are percentage points, so 1.25 means +1.25%.
- candidate evidence must refer only to the supplied input and must not contain URLs.
- portfolio must contain exactly the candidates marked selected; all other ledger candidates must be marked rejected.
- portfolio allocations must be whole integers in the stated increment and sum to exactly 100.
- selected non-SPY, non-CASH holdings must have a base forecast strictly greater than the SPY base forecast.
- no non-SPY, non-CASH economic-exposure cluster may exceed the stated cap.
- benchmark_expected_return_pct must equal the SPY candidate's base forecast.
- portfolio_expected_return_pct must equal the allocation-weighted holding forecasts.
- expected_alpha_vs_sp500_pct must equal portfolio_expected_return_pct minus benchmark_expected_return_pct.
- confidence is the probability that the submitted portfolio beats SPY over this scoring window; do not use confidence to change allocation size.
- key_risks must contain 2-5 concrete risks.
- Do not include a second portfolio, backup allocation, financial-advice disclaimer, or extra field.
"""
    return _apply_horizon(template.replace("__METHODOLOGY_VERSION__", version), horizon)


def _single_pick_prompt_text(horizon: str) -> str:
    return _apply_horizon("""# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make saved market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

The scoring timeline is central to the task: the selected option is measured from the adjusted close on the entry date to the adjusted close on the exit date, calculated after regular trading ends on the exit date. Optimize for facts, catalysts, positioning, liquidity, and risks that can plausibly affect prices before that exit close.

Optimize only for the option you expect to perform best over this close-to-close one-month scoring window. Use longer-horizon facts only when they are likely to affect prices before the exit close.

Briefing-bias discipline: the briefing may group facts by broad asset area and include a mechanical price-context table. Treat inclusion, section order, grouping, row count, and price-context table order as context, not recommendation signals.

Price-history discipline: trailing returns are descriptive data, not forecasts. Use price history as one input, not as a standalone reason to choose an option. When recent performance matters to the selection, compare it with the briefing's catalysts, macro context, valuation or fundamental facts if supplied, volatility, drawdown, and reversal risk before the exit close.

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
- If the rationale cites momentum, recent returns, or trailing performance, do not present price history alone as independent evidence. Mention any independent support present in the briefing, or state that support is limited, and include the relevant reversal or positioning risk in key_risks.
- key_risks must be a list of 2-5 concrete risks that could cause the selected option to underperform; do not only list generic market risk.
- Do not provide a ranked list, backup choice, second-best option, or alternative recommendation.
- Do not include financial-advice disclaimers. This is a benchmark response, not advice to a person.
- The JSON object must contain no extra fields.
- Do not recommend a portfolio.
- Do not choose multiple options.
""", horizon)
