# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make one-shot market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

Your objective is to choose the single allowed option you expect to have the highest total return over the round horizon, using the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by the realized return of its selected option relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official one-shot leaderboard.

Your selected option is scored by its realized percentage return over the round window. Alpha is selected option return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

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
