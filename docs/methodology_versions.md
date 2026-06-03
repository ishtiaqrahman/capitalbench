# Methodology Versions

CapitalBench methodology can evolve across rounds. Each public round should
state the methodology version used for that round.

Methodology must not be changed inside a completed round after model calls have
started. Future rounds may use improved prompt wording, option universes,
provider settings, retry policies, reporting, or scoring rules, as long as those
changes are documented before the future round is frozen.

## round1-v1.0

Used for `CB-2026-05-10-1M`.

Key properties:

- One official one-shot run.
- One selected option per model.
- CapitalBench Universe v1.5.
- Model-facing final briefing imported from `research/final_briefing.md`.
- Full-universe trailing returns included as a mechanical prompt artifact.
- Real provider calls used OpenAI, Anthropic, Google, and xAI adapters.
- Tools, browsing, web search, code execution, and external retrieval were
  disabled through provider payloads where supported.
- The frozen Round 1 prompt instructed models to use only information in the
  prompt. Later methodology versions allow internal learned knowledge and
  general market priors while still forbidding tools, live data retrieval, and
  intentional use of post-cutoff facts.
- Earlier failed or exploratory attempts are excluded from public official
  scoring.
- Exact raw provider response text was not persisted for the official Round 1
  run because `raw_responses/` sidecar preservation was added afterward. The
  run log preserves SHA256 hashes of the original provider text seen at runtime.

## v1.1 Planned Default

Use for future rounds unless superseded.

Changes from `round1-v1.0`:

- Prompts explicitly allow internal learned knowledge and general market priors.
- Prompts continue to forbid browsing, tools, live data retrieval, external
  retrieval, and intentional use of post-cutoff facts, prices, news, or events.
- `raw_responses/` sidecars preserve exact provider text for every model call.
- Run logs include raw response sidecar paths and SHA256 hashes.

## portfolio-v1.0 Planned Protocol

Use for future portfolio-allocation rounds when the round manifest sets
`submission_format: portfolio`.

Changes from `v1.1`:

- Models submit one official allocation decision instead of one selected asset.
- The default portfolio constraint set allows 1 to 5 holdings.
- Allocations must be whole percentages in 5% increments and must total 100%.
- No shorting, leverage, negative weights, or unfrozen option ids are allowed.
- CASH and benchmark allocations are controlled by the round manifest and must
  be present in `options.yaml`.
- Scoring records weighted realized portfolio return, S&P 500 comparison, and max-possible-return context.
- Public artifacts include holding-level allocation rows, portfolio rationale,
  holding count, largest allocation, cash allocation, benchmark allocation, and
  concentration HHI.
- Single-pick and portfolio rounds remain labeled by methodology and submission
  format in reports and website tables.

## Universe v2.1 Future-Round Update

Use for future rounds unless superseded. Do not apply this universe to
completed or already-frozen rounds.

Changes from `v2.0`:

- Keeps all 65 `v2.0` options unchanged and in the same order.
- Adds five Tiingo-validated ETFs after the original AI/technology theme block:
  `BROAD_AI_TECH` (`AIQ`), `AUTONOMOUS_ROBOTICS` (`ARKQ`),
  `CYBERSECURITY` (`CIBR`), `SOLAR` (`TAN`), and `METALS_MINING` (`XME`).
- Descriptions remain neutral exposure descriptions and do not reference recent
  performance, rankings, or expected returns.
- `capitalbench init-round` now defaults to
  `configs/universes/capitalbench_universe_v2_1.yaml` when no explicit universe
  file is provided.
