# CapitalBench Protocol

CapitalBench evaluates one thing: given the same frozen market context, which
single market option does a model choose for the next month?

Models may use their internal learned knowledge and general market priors. They
must not browse, call tools, retrieve live data, or intentionally rely on facts,
market prices, news, or events dated after the research cutoff. The common
briefing, options, and market-data artifacts are supplied to every model, but
CapitalBench does not treat models as blank slates.

Each round is a directory under `rounds/<round_id>/`. The round contains the
briefing, option list, prompt, hashes, price files, and isolated runs.
Market data and scoring are offline. Operators supply all round inputs and all
prices. Model calls can be run in mock mode or real API mode.

## Round Inputs

The public inputs are:

- `manifest.yaml`: round metadata, decision deadline, horizon, entry rule, and exit rule
- `briefing.md`: information available to every model at decision time
- `options.yaml`: the only choices models may select
- `prompt.md`: the exact task instruction
- `market_data/universe_trailing_returns.md`, if present: a mechanical full-universe trailing-return table

Before collecting submissions, run `capitalbench hash-round`. This freezes the
input files by writing SHA256 hashes to `hashes.json`.

## Research Artifacts And Model-Facing Briefing

Deep Research outputs should be stored as round research artifacts, not pasted
directly into the model prompt. CapitalBench expects:

```text
research/
  market_fact_report.md
  briefing_audit_report.md
  final_briefing.md
  research_manifest.yaml
  research_hashes.json
```

`final_briefing.md` is the only model-facing research artifact. The import
command copies it to round-level `briefing.md`, and the prompt builder reads
only `prompt.md`, `briefing.md`, and `options.yaml`. The market fact report and
audit report are audit-only reproducibility artifacts.

```bash
capitalbench import-research \
  --round rounds/<id> \
  --market-fact-report market_fact_report.md \
  --audit-report briefing_audit_report.md \
  --final-briefing final_briefing.md \
  --research-cutoff-utc "YYYY-MM-DDTHH:MM:SSZ"
```

The final briefing should contain facts, dates, values, forecasts labeled as
forecasts, scheduled catalysts, and source-reported uncertainties. It should not
contain interpretation, opinion, scenario analysis, "why it matters" commentary,
affected-market mapping, recommendations, or option rankings. Source links and
source ledgers should stay out of the model-facing briefing. All research
artifacts are hashed, and `briefing.md` must match `research/final_briefing.md`.

## Full-Universe Trailing Returns

CapitalBench can add one mechanical market-data artifact to the model prompt:

```bash
capitalbench fetch-universe-performance \
  --round rounds/<id> \
  --as-of-date YYYY-MM-DD
```

This command requires `TIINGO_API_KEY`, fetches every non-CASH option in
`options.yaml`, and writes `market_data/universe_trailing_returns.csv`,
`market_data/universe_trailing_returns.md`, and
`market_data/universe_trailing_returns.json`. The table shows 7-day, 30-day,
6-month, and 1-year trailing returns from adjusted close data. It is sorted in
option order, not by performance. CASH is shown as 0.00%.

This artifact is factual prompt context. It is not used for scoring, it is not a
leaderboard, and it should not include commentary. Re-run `hash-round` after
generating it.

## Runs

`round_id` identifies the frozen market question. `run_id` identifies one model
collection attempt for that round. Run artifacts live under:

```text
rounds/<round_id>/runs/<run_id>/
  submissions/raw/
  submissions/parsed/
  raw_responses/
  run_log.jsonl
  run_manifest.yaml
  validation_summary.json
  results/
```

`raw_responses/` stores the exact text returned by the provider for each call.
`submissions/raw/` stores the normalized raw submission payload used for
validation, and `submissions/parsed/` stores only validated submissions.
`run_log.jsonl` records the path and SHA256 hash of each raw response text file.

Repeated runs must use different run ids. If a run id already exists,
`capitalbench run-round` fails unless `--overwrite-run` is passed. Overwrite only
deletes that selected run folder; it never deletes round-level files.

Use `capitalbench list-runs --round rounds/<id>` to see available runs. Commands
such as validation, scoring, reporting, and run audit accept `--run-id`. If a
round has multiple runs and no run id is supplied, those commands fail clearly.

Each run also has a `run_type`:

- `official`: one call per model; this is the headline benchmark leaderboard.
- `stability`: repeated calls per model; this measures decision consistency.
- `mock`: deterministic dry-run output for testing the framework.
- `provider_smoke`: private provider checks outside benchmark runs.
- `retrospective`: manual old-round exploration that is not official.

The official result and stability analysis are separate. Do not combine them
into one weighted score.

## Public Leaderboards

CapitalBench publishes three result views:

- Latest Round Leaderboard: the newest resolved round's official one-shot result.
- Cumulative Official Leaderboard: average official alpha versus the S&P 500 across resolved rounds where each model participated.
- Cumulative Stability Leaderboard: average repeated-run alpha and average consistency across resolved rounds where each model participated.

There is no qualified leaderboard and no weighted mega-score. Official and
stability results stay separate.

## CapitalBench Universe v1.5

Public rounds should use the fixed ETF universe in
`configs/universes/capitalbench_universe_v1_5.yaml`. The model sees a readable
neutral list of option ids, names, symbols, asset classes, categories, groups,
risk buckets, and exposure descriptions. Tiingo symbols and internal fields
such as `include_in_universe` are not shown to the model.

All non-cash options are US-listed ETF tickers and must pass Tiingo EOD
validation before a public round is frozen. CASH has no ticker and is skipped
by Tiingo validation. If a ticker fails validation, remove or replace it before
running `hash-round`.

```bash
capitalbench validate-universe \
  --round rounds/<id> \
  --start-date YYYY-MM-DD \
  --end-date YYYY-MM-DD
```

`validate-universe` requires `TIINGO_API_KEY` in the environment and does not
print the key.

## Submission Rule

Each model must submit one JSON or YAML object. It must include:

- `round_id`
- `model_id`
- `provider`
- `mode: closed_capability`
- `run_type`
- `replicate_index`
- `replicate_count`
- `is_official_score`
- `selected_option_id`
- `confidence`
- `rationale_summary`
- `key_risks`

The selected option must exist in `options.yaml`. A submission that includes
multiple selections is invalid. Invalid raw submissions are preserved but are
not scored.

Official runs require `replicate_index: 1`, `replicate_count: 1`, and
`is_official_score: true`. Stability runs require `replicate_index` from `1` to
`replicate_count`, allow repeated `model_id` values only when replicate indexes
are unique, and require `is_official_score: false`.

## Official One-Shot Result

The official leaderboard uses one valid submission per model from one selected
official run. The model gets one attempt. The selected asset from that attempt
is the official score.

```bash
capitalbench run-round \
  --round rounds/<id> \
  --models configs/models.local.yaml \
  --run-id official-20260601 \
  --run-type official \
  --allow-real-api-calls
```

For mock testing, add `--mock` and use an example model config. Mock official
runs are useful for rehearsal but are not public benchmark results.

## Provider-Native Execution Policy

CapitalBench does not require every provider to expose identical internal
reasoning controls. It uses provider-native settings and records what happened:

- All models receive the same prompt, briefing, option universe, and frozen
  market-data artifact.
- Models may use internal learned knowledge and general market priors.
- Temperature is set to `0` where supported.
- Tools, browsing, web search, code execution, and external retrieval are
  disabled at the API level where supported.
- Live data retrieval and intentional use of post-cutoff facts, prices, news,
  or events are not allowed.
- Reasoning or thinking is set to the lowest provider-supported setting that
  still allows valid structured output.
- If a provider requires hidden reasoning tokens, those tokens are allowed only
  because the provider requires them.
- Run logs record input, output, reasoning, total tokens, latency, and cost when
  available.
- Hidden reasoning token counts are not treated as directly comparable across
  providers.

For Google Gemini models that reject `thinkingBudget: 0`, use a small positive
budget through `reasoning_effort: low` rather than leaving thinking unbounded.

## Official Retry Policy

An official retry is allowed only when no valid decision can be parsed because
of an infrastructure or format failure:

- malformed JSON
- truncated response
- provider transport or API failure
- schema output failure

A retry is not allowed because of the selected asset, low confidence, or weak
rationale. Failed raw responses must remain in `submissions/raw/`, and the
failed attempt must remain ineligible for public official scoring. Public
reporting should identify exactly one clean official run for the round.

## Multi-Run Stability Analysis

Stability runs call each model multiple times with the same prompt, briefing,
and option list. The default stability design is five replicates.

```bash
capitalbench run-round \
  --round rounds/<id> \
  --models configs/models.local.yaml \
  --run-id stability-20260601 \
  --run-type stability \
  --replicates 5 \
  --allow-real-api-calls
```

Stability analysis reports pick distribution, modal pick, consistency rate,
average repeated return, average repeated alpha, and best/worst repeated
result. It is secondary analysis and does not alter the official leaderboard.

## Cumulative Leaderboards

Each resolved round is one game. Across resolved rounds, CapitalBench can publish
two cumulative leaderboards:

- Cumulative official leaderboard: average official one-shot alpha versus the
  S&P 500 across resolved rounds.
- Cumulative stability leaderboard: average repeated-run alpha and average
  consistency across resolved rounds.

These leaderboards stay separate. There is no weighted mega-score.

```bash
capitalbench publish-latest --rounds-dir rounds --output latest
capitalbench publish-cumulative --rounds-dir rounds --output cumulative
capitalbench cumulative-status --rounds-dir rounds
```

If a round has multiple official-score-eligible runs, cumulative publishing
skips that round unless a selection file identifies the exact official and
stability runs:

```yaml
rounds:
  CB-2026-06-01-1M:
    official_run_id: official-20260601
    stability_run_id: stability-20260601
```

## Adding New Models

New models are added only to future rounds. A model config can include
`first_eligible_round`, `first_eligible_date_utc`, `model_release_date`, and
`notes`. When a round is run, CapitalBench skips models that are disabled, whose
mode does not match the run, or whose first eligible round/date is in the
future.

Previous round leaderboards remain unchanged. New models are not backfilled
into old official rounds because old market outcomes may already be knowable.
If an operator manually runs a new model on an old round, the run must use
`run_type: retrospective`; retrospective runs are excluded from official and
cumulative leaderboards.

Example:

```text
Round 1:
GPT, Claude, Gemini, Grok participate.

Round 2:
A new model is released.
GPT, Claude, Gemini, Grok, New Model participate.

Latest leaderboard:
Round 2 only.

Cumulative leaderboard:
GPT, Claude, Gemini, Grok have 2 rounds.
New Model has 1 round.
```

## Provider Smoke Tests

`capitalbench smoke-provider` sends one tiny private request to a selected
provider and saves the output under `provider-smoke-tests/`. Smoke tests do not
write into `runs/<run_id>/`, do not affect validation summaries, and do not
change leaderboards. They are for checking API keys, provider wiring, latency,
usage metadata, and structured-output behavior before a real run.

Provider adapters also disable tool and search capabilities at the API request
level where the provider exposes that control:

- OpenAI Responses API: sends no tools and `tool_choice: none`.
- Anthropic Messages API: sends `tool_choice: {"type": "none"}` and no tools.
- Google Gemini API: sends no tools, `functionCallingConfig.mode: NONE`, and a bounded thinking budget when configured.
- xAI chat completions: sends no tools, `tool_choice: none`, and live search mode `off`.

## Scoring Window

CapitalBench is time-resolved. The decision is made before the outcome window is
known. After the window ends, the operator adds local entry and exit prices and
runs `capitalbench score-round`.

For Tiingo scoring prices, `capitalbench fetch-prices` defaults to selected-only
fetching: selected options, the S&P 500 benchmark, and CASH. Add
`--full-universe` when the round report should include `regret_vs_best_option`
and `rank_among_options`; this fetches every option in the frozen
`options.yaml`. Scoring price fetches require Tiingo rows to exactly match the
requested entry and exit dates, and do not silently use nearest available dates.

The first public version supports a one-month single-option decision only. It
does not support portfolios or live data fetching.
