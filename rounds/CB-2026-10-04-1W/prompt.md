# CapitalBench portfolio-v3.0 Task

You are participating in an offline, time-resolved CapitalBench evaluation round. Every model receives the same frozen information and makes one single-turn, non-agentic judgment without tools, browsing, retrieval, or follow-up.

Your objective is to rank assets for realized return over exactly one week and identify candidates that can beat SPY. CapitalBench, not you, constructs the scored portfolio from your judgment using the fixed rule below.

The deterministic candidate slate exists to prevent omission; it is not a recommendation. Assess every slate candidate. You may add at most two wildcard options from the complete allowed universe, but only when the frozen briefing supplies a specific reason the mechanical slate missed.

Use only facts and mechanical market data supplied in this input. You may use internal learned knowledge and general priors, but do not intentionally rely on facts, prices, news, or events after the research cutoff. Treat section order, mention count, option order, table order, and slate inclusion as neutral presentation choices rather than recommendation signals.

Do not extrapolate recent returns mechanically. A recent winner has no positive edge without independent in-window support. Give extreme recent losers a fair reversal test, but distinguish temporary price overreaction from fundamental deterioration. Use the supplied cross-sectional dispersion, medium-horizon relative strength, volatility, drawdown, volume, briefing evidence, and quality evidence. Optimize for the stated close-to-close scoring window only.

For every assessed candidate, provide probabilities and an 80% excess-return range relative to SPY. Rank every assessment without ties. top3_option_ids must be the options ranked 1, 2, and 3. prefer_spy is a diagnostic judgment and does not override the deterministic rule.

CapitalBench applies this rule after your response:

1. Preserve your candidate ranks.
2. A non-SPY candidate is eligible only when you label its recent return as overreaction and give it at least a 55% probability of beating SPY.
3. Select at most the first three eligible candidates in your rank order.
4. Fill fixed portfolio slots of 35%, 35%, and 30% in that order.
5. Put every unused slot in SPY.

You do not submit allocations or an alternative portfolio. Return only valid JSON. Do not include markdown, citations, prose, or commentary outside the JSON.

Required JSON format:

{
  "round_id": "<round_id>",
  "model_id": "<model_id>",
  "provider": "<provider>",
  "mode": "closed_capability",
  "dispersion_state": "low, normal, or high",
  "dominant_pattern": "continuation, reversal, or mixed",
  "market_rationale": "<concise market-level judgment>",
  "candidate_assessments": [
    {
      "option_id": "<allowed option ID>",
      "origin_lanes": ["<exact lane or lanes from the deterministic slate, or wildcard>"],
      "mechanism": "continuation, reversal, catalyst, defensive, or no_edge",
      "p_beat_spy_pct": <integer 0-100>,
      "p_top3_pct": <integer 0-100>,
      "excess_return_p10_pct": <number>,
      "excess_return_p50_pct": <number>,
      "excess_return_p90_pct": <number>,
      "recent_return_interpretation": "overreaction, fundamental_deterioration, supported_continuation, or no_edge",
      "evidence": ["<1-3 concise facts from the supplied input>"],
      "rank": <unique contiguous integer beginning at 1>
    }
  ],
  "top3_option_ids": ["<rank 1>", "<rank 2>", "<rank 3>"],
  "prefer_spy": <boolean>,
  "portfolio_rationale": "<concise explanation of the ranked judgment>",
  "key_risks": ["<risk 1>", "<risk 2>"]
}

Rules:
- assess every deterministic slate candidate and no more than two optional wildcards;
- use origin_lanes exactly as shown for slate candidates and ["wildcard"] for additions;
- probabilities are whole percentages from 0 to 100;
- excess-return estimates are percentage points relative to SPY and must satisfy p10 <= p50 <= p90;
- ranks must be unique and contiguous from 1 through the number of assessments;
- evidence must refer only to supplied input and contain no URLs;
- key_risks must contain 2-5 concrete risks;
- do not output portfolio allocations, a second ranking, a financial-advice disclaimer, or extra fields.
