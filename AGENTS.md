# CapitalBench Agent Notes

## Current Production Methodology

All newly initialized portfolio rounds use `portfolio-v2.0` by default. This
production adoption was explicitly directed by the operator on July 17, 2026;
it is not an evidence-based acceptance of the unresolved July 13 pilot. Before
creating, running, resolving, or changing a new portfolio round, read:

- `docs/portfolio_v2_methodology.md`
- `docs/research_prompt_workflow.md`
- `docs/protocol.md`
- `docs/first_round_checklist.md`

Use `capitalbench init-round --submission-format portfolio`. Do not manually
downgrade the generated manifest to `portfolio-v1.0`. Production V2 requires a
single-turn, non-agentic call, the complete compact decision-context table, a
6-8 option candidate ledger including SP500 and at least four economic
exposure clusters, low/base/high forecasts, the active-holding SPY hurdle, and
the 50% non-benchmark economic-exposure cap. Score only the final frozen
portfolio; retain the candidate ledger for calibration and audit.

The tracked production roster is the complete eight-model roster in
`configs/models.v2.yaml`: GPT-5.5, GPT-5.6 SOL, Grok 4.3, Grok 4.5, Gemini
3.1 Pro, Claude Opus 4.8, Claude Opus 4.7, and Claude Fable 5. Every official
`portfolio-v2.0` run must use all enabled models in that canonical file. The
runner and acceptance gate reject partial rosters, and a production round is
incomplete unless every enabled model has one valid submission. Never
substitute or reuse the separate July 13 four-model pilot roster. Model keys
must come from local environment files or environment variables and must never
be committed.

The first complete official production V2 rounds are:

- `CB-2026-07-17-1W`, accepted run
  `official-v2-all-weekly-final-20260717`, due for resolution after the July
  24, 2026 close.
- `CB-2026-07-17-1M`, accepted run `official-v2-all-final-20260717`, due for
  resolution after the August 17, 2026 close.

Both are primary-stream unresolved rounds and contain all eight production
models. Preserve their frozen research, decision context, candidate ledgers,
forecasts, portfolios, entry prices, and hashes. Resolve them with the normal
pricing and scoring pipeline; do not rerun or revise them after observing
market outcomes.

The July 16 weekly and monthly V2 runs contain only four of the eight required
models. They are retained as audit artifacts but are not official-score
eligible and must not enter latest, cumulative, market-environment, or insight
calculations. Their resolution jobs are cancelled. Do not add retrospective
submissions or otherwise repair those partial rounds after their decision
window.

## Resolved Historical Experiment

The weekly-only Portfolio V2 pilot paired with the July 13, 2026 V1 weekly
round was resolved and **rejected** under its frozen acceptance rule on July
21. Before interpreting, publishing, or changing either round, read:

- `docs/experiments/portfolio-v2-2026-07-13.md`
- `experiments/portfolio-v2-2026-07-13.yaml`

V2 beat SPY but underperformed paired V1 by 2.13 percentage points on average,
and 0 of 4 models improved. Preserve both V1 and V2 artifacts without
retroactive edits. Do not add the four-model pilot to primary latest,
cumulative, market-environment, or insight data. Production V2 remains active
because it was separately adopted by operator direction; do not rewrite the
rejected pilot as having caused or reversed that adoption.

## Active V2 Diagnostics

The zero-cost diagnostic program is frozen in:

- `docs/experiments/v2-next-research-2026-07-21.md`
- `experiments/v2-next-research-2026-07-21.yaml`

The July 13 pilot lacked candidate ledgers. Its selected sets captured strong
assets, but equal-weight and holding-cap counterfactuals did not improve mean
return. Do not create a retrospective ledger. The complete July 17 production
weekly round remains the next clean production-ledger diagnostic after the
July 24 close.

On July 21, the operator separately authorized private historical research on
balanced candidate search, structured event evidence, pairwise ranking, and
abstention. This does not alter production V2 or official scores. Before
continuing return-improvement research, read:

- `research/README.md`
- `research/registry.yaml`
- `research/PROTOCOL.md`

The registry is the canonical cross-session memory. Raw `output/` files are
not canonical. Before paid calls, register and freeze the experiment. After
scoring, save a tracked report and machine-readable summary, update the
registry with the result and next action, and run
`python scripts/validate_research_registry.py`. Never describe adaptive
development episodes as sealed confirmation data.

That event-register search was completed and rejected on July 21. H7 improved
mean top-five alpha over balanced H4 by 0.16 percentage points, improved 8 of
13 valid pairs and 2 of 4 episodes, increased top-three capture by 2, but
worsened mean shortlist regret by 0.48 points. H8 pairwise ranking was not run
because the frozen search gate failed. Do not resume or reframe this branch as
a pass. The current next program is the no-call July 17 complete-ledger
diagnostic after the July 24 close, as recorded in `research/registry.yaml`.

CapitalBench prompt and model-input changes affect benchmark fairness. Before
editing round prompts, research import rules, market-data appendices, or model
input assembly, read:

- `docs/research_prompt_workflow.md`
- `docs/protocol.md`
- `docs/first_round_checklist.md`
- Relevant tests in `tests/test_universe.py`, `tests/test_research.py`, and `tests/test_prices.py`

## Prompt And Input Contract

Prompt 1, Prompt 2, and Prompt 3 generate research artifacts only:

- Prompt 1 -> `market_fact_report.md`, audit-only.
- Prompt 2 -> `briefing_audit_report.md`, audit-only.
- Prompt 3 -> `final_briefing.md`, model-facing briefing only.

The effective production V2 model input is assembled by
`capitalbench.prompting.build_prompt` from:

- `prompt.md`
- round metadata
- `briefing.md`, copied from Prompt 3's `final_briefing.md`
- `market_data/universe_decision_context.md`, generated mechanically and kept
  complete in frozen option order
- `options.yaml`, rendered as a compact neutral table with static economic
  exposure clusters

The mechanical price-context appendix is generated by:

```bash
capitalbench fetch-universe-decision-context --round rounds/<id> --as-of-date <date>
```

The expected appended section title is:

```text
Full-Universe Horizon-Specific Decision Context
```

## API Use

When preparing Prompt 1, Prompt 2, or Prompt 3 research, do not use model APIs,
agent APIs, model search tools, or provider-hosted browsing/search features to
collect or synthesize the report. The research report must be prepared from
direct public-source browsing and source review.

Mechanical pricing APIs are allowed for price data. Use the existing
CapitalBench pricing pipeline, such as Tiingo-backed commands, to generate
entry prices, exit prices, and full-universe trailing-return context when those
artifacts are required. Pricing API output is mechanical market data, not model
research.

## Hard Rules

- Do not paste selected mechanical return rows into `final_briefing.md`.
- Do not use model APIs or model search features to prepare research reports.
- Do use the pricing pipeline/API when mechanical price context is required.
- Do not manually rank, recommend, or map allowed options in model-facing briefing text.
- For production V2, enforce the neutral SPY forecast hurdle defined in
  `docs/portfolio_v2_methodology.md`; do not reintroduce the old V1 benchmark
  allocation wording.
- Keep source URLs, citations, and source ledgers out of `final_briefing.md`.
- Treat price history as descriptive context, not as a forecast.
- Keep the price-context appendix complete, mechanically generated, and sorted by option order rather than performance.
- Do not remove rejected finalists, alter forecasts, or optimize a submitted
  portfolio after the one model call.
- Do not modify frozen historical rounds unless the user explicitly asks for regeneration and re-hashing.
- Do not push or deploy unless the user explicitly asks.

## Where To Change Things

- Initialized round prompt wording: `src/capitalbench/rounds.py`
- Model input assembly and guardrails: `src/capitalbench/prompting.py`
- Mechanical price-context generation: `src/capitalbench/performance.py`
- V2 horizon-specific decision context: `src/capitalbench/decision_context.py`
- Static economic exposure clusters: `src/capitalbench/exposures.py`
- V2 provider schema and validation: `src/capitalbench/submission_schema.py`
  and `src/capitalbench/validation.py`
- Research import validation: `src/capitalbench/research.py`
- Operator prompt workflow docs: `docs/research_prompt_workflow.md`

## Verification

For prompt, research, or market-data appendix changes, run:

```bash
pytest tests/test_universe.py tests/test_research.py tests/test_prices.py tests/test_decision_context.py tests/test_validation.py
```

For broader behavior changes, run:

```bash
pytest
```

For return-improvement research records, also run:

```bash
python scripts/validate_research_registry.py
pytest tests/test_research_registry.py
```
