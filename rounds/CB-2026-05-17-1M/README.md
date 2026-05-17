# CapitalBench Round 2

Round id: `CB-2026-05-17-1M`

Status: official portfolio run complete, entry prices fetched, exit prices unresolved.

Official run id: `official-20260517`

Methodology version: `portfolio-v1.0`

Universe version: `v2.0`

## What This Round Contains

- Frozen round manifest, prompt, briefing, options, and hashes.
- Research artifacts under `research/`.
- Full-universe trailing-return prompt artifact under `market_data/`.
- One official one-shot portfolio run under `runs/official-20260517/`.
- Operator declaration in `official_selection.yaml`.
- Local automation job for scheduled resolution after the exit window.

## Official Allocations

All four participating models submitted valid portfolios with one to five
holdings, 5% allocation increments, and total allocation of 100%.

| Model | Provider | Allocation | Confidence |
| --- | --- | --- | --- |
| openai-gpt-5-5 | openai | OIL 30%; ENERGY 25%; BROAD_COMMODITIES 20%; SEMICONDUCTORS 20%; US_DOLLAR 5% | 0.54 |
| anthropic-claude-opus-4-7 | anthropic | ENERGY 30%; GOLD 25%; SHORT_TREASURY 20%; SEMICONDUCTORS 15%; CONSUMER_STAPLES 10% | 0.62 |
| google-gemini-3-1-pro | google | ENERGY 30%; SEMICONDUCTORS 25%; OIL 20%; GOLD 15%; SHORT_TREASURY 10% | 0.70 |
| xai-grok-4-3 | xai | ENERGY 40%; SEMICONDUCTORS 35%; BROAD_COMMODITIES 25% | 0.60 |

## Resolution Status

This round is not scored yet.

Entry prices use Tiingo EOD adjusted close from Friday May 15, 2026, the last
trading close before the Sunday May 17, 2026 decision deadline.

Missing until the market window resolves:

- `prices/exit_prices.csv`
- `runs/official-20260517/results/leaderboard.csv`
- `runs/official-20260517/results/report.md`

The entry rule and exit rule are defined in `manifest.yaml`.

## Audit Notes

Exact raw provider response text is preserved locally under `raw_responses/`
for private operator audit. Those text sidecars are excluded from the public
repository. Public audit material should use the recorded SHA256 hashes,
normalized submissions, parsed submissions, and run log.

This is not financial advice.
