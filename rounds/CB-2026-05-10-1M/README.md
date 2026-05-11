# CapitalBench Round 1

Round id: `CB-2026-05-10-1M`

Status: official run complete, entry prices fetched, exit prices unresolved.

Official run id: `official-round-1-clean`

Methodology version: `round1-v1.0`

## What This Round Contains

- Frozen round manifest, prompt, briefing, options, and hashes.
- Research artifacts under `research/`.
- Full-universe trailing-return prompt artifact under `market_data/`.
- One official one-shot run under `runs/official-round-1-clean/`.
- Operator declaration in `official_selection.yaml`.

## Official Decisions

All four participating models selected `SEMICONDUCTORS`, represented by ETF
symbol `SMH` in the option universe.

| Model | Provider | Selected Option | Confidence |
| --- | --- | --- | --- |
| openai-gpt-5-5 | openai | SEMICONDUCTORS | 0.34 |
| anthropic-claude-opus-4-7 | anthropic | SEMICONDUCTORS | 0.58 |
| google-gemini-3-1-pro | google | SEMICONDUCTORS | 0.60 |
| xai-grok-4-3 | xai | SEMICONDUCTORS | 0.55 |

## Resolution Status

This round is not scored yet.

Entry prices use Tiingo EOD adjusted close from Friday May 8, 2026, the last
trading close before the Sunday May 10, 2026 decision deadline.

Missing until the market window resolves:

- `prices/exit_prices.csv`
- `runs/official-round-1-clean/results/leaderboard.csv`
- `runs/official-round-1-clean/results/report.md`

The entry rule and exit rule are defined in `manifest.yaml`.

## Audit Notes

Earlier real attempts and mock/preflight attempts are preserved locally but are
not part of the public official result. They are not official-score eligible and
should not be included in the first public commit.

The official run predates `raw_responses/` sidecar preservation. Exact raw
provider text cannot be reconstructed retroactively. `run_log.jsonl` records
the SHA256 hash of the provider text seen at runtime, and
`submissions/raw/*.json` contains the normalized raw submission payloads used
for validation. Future runs preserve exact provider text under `raw_responses/`.

This is not financial advice.
