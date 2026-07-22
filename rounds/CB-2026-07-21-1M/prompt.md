# CapitalBench portfolio-v2.2 Task

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
