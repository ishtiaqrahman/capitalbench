# CapitalBench Portfolio V2 Task

You are participating in an offline, time-resolved CapitalBench methodology experiment. This is a single-turn, non-agentic decision. Do not browse, use tools, request more information, or make a follow-up call.

CapitalBench gives participating models the same frozen market facts, mechanical market context, allowed options, and portfolio constraints. Your saved portfolio will be measured from the adjusted close on the entry date to the adjusted close on the exit date after regular trading ends.

Your objective is to allocate exactly 100% across the allowed options to maximize expected realized portfolio return over this one-week close-to-close window relative to the S&P 500 / SPY. The official score uses the submitted weights exactly as returned. There is no later optimization, rebalancing, leverage, shorting, or after-the-fact edit.

Use only facts available by the stated research cutoff. You may use internal learned knowledge and general market priors, but do not intentionally rely on prices, news, releases, or events after the cutoff. If internal knowledge conflicts with the frozen briefing, prioritize the briefing.

Treat briefing inclusion, section order, option order, and table order as context rather than recommendation signals. The mechanical table contains descriptive price and risk history, not forecasts. It contains no rank or buy score.

Make the decision in this order:

1. Estimate SPY's percentage return over the exact scoring window.
2. Separate the latest five-session move from the preceding sixteen-session trend. A recent winner is not sufficient evidence by itself.
3. Select only holdings whose expected return is supported by the frozen facts, a plausible catalyst inside the window, general priors, or an explicitly stated limited-information judgment.
4. Consider correlated exposure when multiple holdings depend on the same industry, factor, commodity, macro event, or geopolitical outcome.
5. Estimate each selected holding's return, calculate the weighted portfolio forecast, and compare it with the SPY forecast.

SPY is an allowed option and must be evaluated under the same expected-return criteria as every other option. A holding with no identifiable event catalyst may use `none identified` for `time_window_catalyst`; do not invent one.

Return only valid JSON. Do not include markdown, citations, hidden reasoning, a ranked list, a backup portfolio, or commentary outside the JSON.

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
      "expected_return_pct": <number in percentage points>,
      "time_window_catalyst": "<brief catalyst inside the window, or none identified>",
      "invalidation_condition": "<brief observable condition that would weaken this holding case>",
      "rationale": "<brief holding-level rationale>"
    }
  ],
  "benchmark_expected_return_pct": <SPY expected return in percentage points>,
  "portfolio_expected_return_pct": <weighted portfolio expected return in percentage points>,
  "expected_alpha_vs_sp500_pct": <portfolio forecast minus SPY forecast in percentage points>,
  "confidence": <number from 0 to 1>,
  "portfolio_rationale": "<1-3 concise sentences>",
  "rationale_summary": "<1-3 concise sentences>",
  "key_risks": [
    "<concrete risk 1>",
    "<concrete risk 2>"
  ]
}

Rules:

- Use only allowed option IDs and 1-5 holdings.
- Allocation percentages must use 5% increments and sum to exactly 100%.
- Percentage-point units are literal: `1.25` means an expected return of positive 1.25%, and `-0.40` means negative 0.40%.
- `expected_alpha_vs_sp500_pct` must equal `portfolio_expected_return_pct - benchmark_expected_return_pct` within 0.10 percentage point.
- The allocation-weighted holding expected returns must equal `portfolio_expected_return_pct` within 0.20 percentage point.
- `confidence` is your probability from 0 to 1 that this portfolio beats SPY during this scoring window.
- Each selected holding requires a catalyst field, invalidation condition, expected return, and concise rationale.
- Include 2-5 concrete risks that could cause the portfolio to underperform SPY.
- Do not add fields, disclaimers, or alternative portfolios.
