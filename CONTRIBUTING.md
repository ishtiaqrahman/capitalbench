# Contributing To CapitalBench

CapitalBench is an evaluation framework. Changes should preserve
reproducibility, auditability, and clear separation between benchmark results
and exploratory work.

## Development

Run tests before submitting changes:

```bash
python3 -m pytest
```

Use mock mode for framework tests. Tests must not require real API keys or
network access.

## Rounds

Each public round must freeze:

- `manifest.yaml`
- `briefing.md`
- `options.yaml`
- `prompt.md`
- `hashes.json`
- any model-facing `market_data/` artifact

Research-only artifacts belong under `research/`. Only `briefing.md` is shown
to evaluated models.

## Methodology Changes

Methodology changes are allowed across rounds, but not inside a completed
round. If a prompt, universe, provider policy, retry policy, or scoring rule
changes, document it in `docs/methodology_versions.md` and in the round README.

Do not change a completed round's option universe after seeing model choices in
order to force variety.

## Provider Calls

Real provider calls require `--allow-real-api-calls`. Use private smoke tests
before official runs when changing provider adapters.

Official retries are allowed only for infrastructure or format failures, such
as malformed JSON, truncation, transport errors, or schema failures. Do not
retry because of the selected asset, confidence, or rationale quality.

## Secrets

Never commit `.env`, private local configs, API keys, provider smoke-test
outputs, or credentials.
