# CapitalBench Insights Engine Plan

Status: deterministic v1 implemented; NVIDIA LLM rewrite layer implemented
Last updated: 2026-06-16

This document defines the CapitalBench Insights engine. The deterministic v1
pipeline publishes static artifacts, a website page, and API responses. The
NVIDIA LLM rewrite layer is implemented as an optional clarity pass over
validated deterministic candidates.

## Decisions

- V1 insights use CapitalBench data only. They do not ingest market news,
  analyst commentary, or external web data.
- Deterministic calculations are the source of truth. The LLM can summarize,
  prioritize, and explain calculated facts, but it cannot invent facts or create
  unsupported investment commentary.
- The insights engine runs as a separate audited pipeline, not inside the normal
  frontend build. The website and Data API read its generated artifacts.
- The engine must still publish deterministic insights when the LLM is
  unavailable or no NVIDIA key is configured.
- Every public insight must answer three questions: what happened, why it may
  matter for benchmark interpretation, and where the reader can verify it.
- All copy must stay inside the benchmark frame. It may describe model behavior,
  positioning, performance, and benchmark context. It must not recommend trades
  or tell readers what to buy or sell.

## Implemented V1

- `src/capitalbench/insights.py` builds canonical input packets, generates
  deterministic insights, validates public insight artifacts, and writes dated
  run outputs.
- CLI commands:
  - `capitalbench build-insights-input --rounds-dir rounds --output <temp>/input.json --run-date <date>`
  - `capitalbench generate-insights --input <temp>/input.json --output insights`
  - `capitalbench validate-insights --insights-dir insights`
- Public artifacts:
  - `insights/latest.json`
  - `insights/index.json`
  - `insights/<date>/input.json`
  - `insights/<date>/deterministic_candidates.json`
  - `insights/<date>/insights.json`
  - `insights/<date>/run_manifest.json`
  - `insights/<date>/report.md`
- Website/API:
  - `/insights`
  - `GET /api/v1/insights?category=&limit=&cursor=`
  - `GET /api/v1/insights/{insight_id}`
- NVIDIA LLM rewrite:
  - Default model: `meta/llama-3.1-8b-instruct`
  - Default base URL: `https://integrate.api.nvidia.com/v1`
  - Default CLI mode: `--llm auto`
  - The LLM receives only the compact candidate packet, not raw repository files.
  - The LLM can rewrite title, summary, and `why_it_matters`; calculations,
    evidence, IDs, and source rows remain deterministic.
  - If the key is absent or the LLM fails in `auto` mode, deterministic insights
    still publish and the run manifest records the LLM status.
- Automation:
  - The prepared `.github/workflows/insights.yml` automation is coordinated by
    `workflow_run` after successful `CapitalBench Resolver` or `Interim
    Performance Refresh` completions once the repository token has
    workflow-file write scope.
  - A `06:12 UTC` Tuesday-Saturday cron is a backstop for late corrections or
    missed dispatches.
  - The workflow must compute a stable benchmark-data fingerprint before
    calling NVIDIA. If the newest input matches the latest published
    fingerprint, it skips the LLM call and does not rewrite public insight
    artifacts.
  - When artifacts change, the workflow validates, commits, and deploys the
    website when credentials are configured.

## Current System Findings

CapitalBench already generates most of the raw material needed for useful
insights:

- Round files under `rounds/<round_id>/` hold manifests, prompts, model-facing
  briefings, saved options, hashes, run manifests, submissions, allocations,
  price files, live weekly performance, and resolved results.
- `latest/` and `cumulative/` hold latest official and cumulative leaderboard
  artifacts.
- `benchmark_sets.yaml` plus the generated website read model define fair
  equal-run benchmark sets and current weekly/monthly benchmark status.
- `configs/asset_risk_model.yaml` is the shared asset-risk source used by AI
  Risk Appetite and historical model risk profiles.
- `apps/web/scripts/generate-api-read-model.mjs` turns local artifacts into the
  static website/API read model used by pages and API handlers.
- The generated read model includes `model_behavior`, a deterministic profile
  layer with archetype labels, risk-taking score, concentration, turnover, peer
  similarity, resolved performance context, and methodology links.
- `apps/web/src/lib/dataApi.js` already exposes positioning, risk appetite,
  live performance, rounds, models, assets, benchmark sets, latest results, and
  cumulative results, plus model behavior profile endpoints.
- GitHub Actions already refresh active interim performance after market close
  and resolve due rounds. The Insights workflow should be published once the
  repository token has workflow-file write scope; it should run after those
  workflows complete, not merely at a standalone time, so it summarizes settled
  official results and the newest available live mark-to-market state.

NVIDIA API research:

- NVIDIA's NIM LLM API docs describe OpenAI-compatible chat completions at
  `POST /v1/chat/completions`.
- NVIDIA's API catalog uses the hosted base URL
  `https://integrate.api.nvidia.com/v1`.
- The implementation uses an explicit NVIDIA env namespace:
  `NVIDIA_API_KEY`, `NVIDIA_BASE_URL`, and `NVIDIA_MODEL_ID`.
- `meta/llama-3.1-8b-instruct` is the default because this task needs clear
  financial-benchmark wording, JSON instruction following, and reliable weekday
  latency on NVIDIA's hosted free endpoint. `NVIDIA_MODEL_ID` can override it
  without code changes.

References:

- https://docs.api.nvidia.com/nim/reference/llm-apis
- https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html
- https://docs.api.nvidia.com/nim/reference/create_chat_completion_v1_chat_completions_post

## Data Map

| Data source | Canonical location | Refresh cadence | Insight use |
| --- | --- | --- | --- |
| Active model portfolios | `rounds/*/runs/*/submissions/parsed`, read model `allocations` | On accepted official runs | Current positioning, consensus, concentration, risk appetite |
| Resolved round results | `rounds/*/runs/*/results/leaderboard.csv` and `returns.csv` | On final scoring | Winners, oracle-scaled scores, S&P 500 comparison, regret |
| Live interim performance | `rounds/*/runs/*/results/weekly_performance.csv` | After eligible market closes | Provisional live leaders, live alpha, drawdowns |
| Latest leaderboards | `latest/latest_round_*` | On scoring | Most recent official result summary |
| Cumulative leaderboards | `cumulative/*` | On scoring | Long-run performance context |
| Benchmark sets | `benchmark_sets.yaml` plus generated sets | On website data generation | Fair equal-run comparisons, current benchmark, excluded rounds |
| Risk appetite | `configs/asset_risk_model.yaml` plus generated allocation snapshots | On new live portfolios | Risk-taking score, model agreement, regime mix |
| Asset metadata | `configs/universes/*` and saved round `options.yaml` | On new universe or round | Human-readable asset names, tickers, categories |
| Model metadata | Generated read model and model profile config | On model config or run data change | Model labels, providers, model pages |
| Price snapshots | `market_data/daily_price_snapshots/*` | After market close | Freshness checks, live mark-to-market dates |
| Public API read model | `apps/web/src/generated/apiReadModel.js` | During site/API build | Unified source for website and API consumers |

## Insight Taxonomy

V1 should generate a ranked list of insight candidates across these categories.
Each candidate receives an `importance_score` from 0 to 100 and a plain-English
reason for the score.

| Category | Primary audience | Example insight |
| --- | --- | --- |
| Current positioning | Investors, traders | "Models are most concentrated in Semiconductors (SMH), with 3 of 5 live portfolios holding it." |
| Risk regime | Allocators, traders | "The current AI Risk Appetite score is 81.4 out of 100, indicating aggressive allocation behavior." |
| Model agreement | Allocators, AI researchers | "Agreement is tight because model risk scores have a standard deviation below 5 points." |
| Live performance | Traders, allocators | "Live weekly portfolios are trailing the S&P 500 by 0.6 percentage points using the latest available close." |
| Latest official result | Investors, AI researchers | "No model beat the S&P 500 in the latest resolved weekly round." |
| Oracle comparison | Researchers, allocators | "The current weekly benchmark leader has captured 42% of the hindsight oracle return across shared rounds." |
| Benchmark-set fairness | Allocators, researchers | "The current weekly benchmark uses 6 shared rounds across 5 models; newer models appear in separate forming sets." |
| Model behavior shift | Researchers, traders | "GPT-5.5 moved from defensive healthcare exposure to higher-beta technology exposure versus its prior live portfolio." |
| Crowding and concentration | Traders, allocators | "The top live asset accounts for 24% of aggregate model allocation, above the recent live average." |
| Data quality and freshness | All audiences | "Latest price close is June 12; no newer eligible close has been ingested." |
| Consensus portfolio | Investors, allocators, researchers | "The average AI portfolio captured 12% of the hindsight oracle return in the latest weekly round." |
| Benchmark difficulty | Investors, allocators, researchers | "The latest weekly round had a wide opportunity set: the best asset beat the worst asset by 24 percentage points." |
| Outcome regime | Investors, traders | "The resolved window rewarded growth and technology while models were positioned defensively." |
| Missed-oracle analysis | Investors, researchers | "The oracle asset was Semiconductors (SMH); three models held it, but average allocation was only 12%." |
| Confidence calibration | AI researchers, allocators | "High-confidence submissions have not outperformed lower-confidence submissions so far." |
| Momentum behavior | Traders, researchers | "Models allocated 71% to assets in the top 20% of prior 30-day momentum." |
| Model similarity | AI researchers, allocators | "Claude Opus 4.7 and Claude Opus 4.8 have the closest live allocation vectors." |
| Portfolio attribution | Traders, allocators | "The winning model's result was helped most by Semiconductors and hurt most by Gold." |

## Deterministic Insight Rules

Programmatic insights should be generated before any LLM call. The generator
should build a candidate set using explicit formulas and thresholds.

Required candidate families:

- Risk Appetite: current combined score, weekly score, monthly score, change
  versus the previous live portfolio set, top regime, top assets, and agreement.
- Model Agreement: standard deviation of model risk-taking scores. Use the
  existing public thresholds: below 5 points is tight, 5 to 12 is mixed, above
  12 is divided.
- Active Positioning: top asset, top category, number of models holding each,
  aggregate allocation percentage, and change versus the prior comparable
  active round.
- Live Performance: live portfolio return, S&P 500 return, alpha in percentage
  points, latest price date, and whether a live value is provisional.
- Latest Official Result: winner, loser, score spread, models beating S&P 500,
  models with positive return, and oracle gap.
- AI Consensus Portfolio: average all model allocations in a round, score the
  resulting consensus portfolio, and compare it with the S&P 500, the average
  model, the winning model, and the hindsight oracle.
- Benchmark Difficulty: oracle return, worst asset return, best-worst spread,
  percent of the scored universe with positive returns, S&P 500 rank inside the
  saved universe, and whether the round was broad, narrow, high-opportunity, or
  low-opportunity.
- Outcome Regime: regime group of the best and worst assets after scoring, then
  compare the winning regime with the regime models favored before the outcome.
- Missed-Oracle Analysis: whether each model held the eventual oracle asset,
  average allocation to that asset, largest holder, and whether the consensus
  portfolio found or missed the best asset.
- Portfolio Attribution: per-model and consensus contribution by holding using
  `allocation * asset return`, including top helper, top detractor, and no-drag
  cases where every holding contributed positively.
- Confidence Calibration: compare submitted confidence with realized return,
  CapitalBench Score, S&P 500 alpha, and oracle gap across resolved official
  rounds.
- Momentum Behavior: compare allocations with pre-run mechanical trailing
  return tables, especially allocation to top/bottom prior 7-day and 30-day
  return groups.
- Model Similarity: compare live or resolved model portfolios as allocation
  vectors to identify closest model pairs, outliers, clustering, and convergence
  over time.
- Live Path Dynamics: use interim performance rows to show live alpha leaders,
  laggards, leader changes, and how often interim leaders remain final winners.
- Benchmark Sets: current weekly/monthly set, qualification status, included
  rounds, excluded rounds, leader, score spread, and models with short history.
- Model-Level Behavior: per-model risk style, recent allocation changes, live
  performance rank, current set membership, and score trend.
- Anomaly/Freshness: stale price date, missing active round data, missing model
  in a set round, failed LLM run, no new insight-worthy movement.

Candidate ranking:

```text
importance_score =
  magnitude_score * 0.35
  + audience_breadth_score * 0.25
  + freshness_score * 0.20
  + evidence_quality_score * 0.20
```

Default scoring rules:

- Magnitude score: size of change, spread, concentration, alpha, or risk move
  scaled against historical CapitalBench values when enough history exists.
- Audience breadth score: 100 for insights useful to all target audiences, 70
  for two or more audiences, 50 for one specialized audience.
- Freshness score: 100 when tied to the latest price close, latest live set, or
  latest official result; 60 for historical context; 20 for unchanged carryover.
- Evidence quality score: 100 for fully deterministic calculations with direct
  source rows; 80 for LLM-assisted wording based only on deterministic
  candidates; 0 for unsupported output.

## Public Insight Contract

Every generated insight should conform to this shape:

```json
{
  "id": "risk-appetite-2026-06-16",
  "date": "2026-06-16",
  "generated_at": "2026-06-16T04:35:00Z",
  "data_as_of": "2026-06-12",
  "category": "risk_regime",
  "audiences": ["investors", "capital_allocators", "traders"],
  "source_type": "deterministic",
  "title": "AI portfolios moved more aggressive",
  "summary": "The current risk-taking score is 81.4 out of 100, up 11.2 points from the previous live portfolio set.",
  "why_it_matters": "It shows the benchmark models are allocating more to growth, momentum, cyclical, and technology assets than before.",
  "importance_score": 88,
  "confidence": "high",
  "status": "published",
  "calculations": [
    {
      "name": "risk_appetite_change",
      "value": 11.2,
      "unit": "points",
      "formula": "current_score - previous_live_set_score"
    }
  ],
  "evidence": [
    {
      "label": "AI Risk Appetite",
      "href": "/risk-appetite",
      "source": "api_read_model.risk_appetite.current_decision_pulse"
    }
  ],
  "related": [
    { "label": "Data API", "href": "/api" }
  ]
}
```

Rules:

- `source_type` is `deterministic`, `llm_assisted`, or `system`.
- LLM-assisted insights must reference deterministic candidate IDs. They cannot
  introduce new numbers.
- `data_as_of` must be the most relevant close date or generated read-model
  timestamp, not the calendar run date.
- `why_it_matters` must explain benchmark interpretation, not investment action.
- Every public insight needs at least one evidence link.

## LLM Input And Output Contract

The NVIDIA LLM receives a compact JSON packet, not raw repository files.

Input packet:

```json
{
  "run_date": "2026-06-16",
  "generated_at": "2026-06-16T04:35:00Z",
  "benchmark_context": {
    "name": "CapitalBench",
    "description": "Live benchmark for AI capital allocation",
    "not_financial_advice": true
  },
  "style_rules": [
    "Use plain English.",
    "Explain benchmark meaning, not trading advice.",
    "Do not invent facts.",
    "Do not mention unsupported causes.",
    "Use asset names before tickers, for example Semiconductors (SMH)."
  ],
  "candidate_insights": [],
  "required_output_schema": "InsightLlmOutputV1"
}
```

Output packet:

```json
{
  "version": "insight_llm_output_v1",
  "selected_candidate_ids": ["risk-appetite-2026-06-16"],
  "rewrites": [
    {
      "candidate_id": "risk-appetite-2026-06-16",
      "title": "AI portfolios moved more aggressive",
      "summary": "Models are taking more risk than in the prior live portfolio set.",
      "why_it_matters": "This helps readers see the current market posture implied by model allocations."
    }
  ],
  "rejected_candidate_ids": []
}
```

LLM guardrails:

- Temperature should default to 0 or the lowest provider-supported deterministic
  setting. If a small nonzero value is required, cap it at 0.2.
- Disable streaming for the daily job.
- Do not send tools.
- Reject responses that are not valid JSON, reference unknown candidates,
  introduce new numbers, mention unsupported external facts, or contain buy/sell
  recommendations.
- Keep the original deterministic candidate text when validation fails.

## Pipeline Design

Add a dedicated Insights workflow after the implementation phase.

Proposed commands:

```bash
capitalbench build-insights-input --rounds-dir rounds --output /tmp/capitalbench-insights-input.json
capitalbench generate-insights --input /tmp/capitalbench-insights-input.json --output insights
capitalbench validate-insights --insights-dir insights
```

The commands write a canonical input packet, generate dated public artifacts,
update `latest.json` and `index.json`, and validate the public insight contract.
`generate-insights` defaults to `--llm auto`, which attempts NVIDIA rewriting
only when `NVIDIA_API_KEY` is configured. In scheduled automation the input
packet is built in runner temp storage; it is copied into `insights/YYYY-MM-DD/`
only when the benchmark-data fingerprint has changed.

Proposed artifacts:

```text
insights/
  latest.json
  index.json
  YYYY-MM-DD/
    run_manifest.json
    input.json
    deterministic_candidates.json
    llm_request.redacted.json
    llm_response.json
    insights.json
    report.md
```

Automation workflow:

- Primary trigger: run after successful `CapitalBench Resolver` completion.
  This captures newly settled official weekly or monthly results.
- Primary trigger: run after successful `Interim Performance Refresh`
  completion. This captures the newest live mark-to-market portfolios after the
  U.S. market-close data refresh.
- Backstop trigger: run at `06:12 UTC` Tuesday-Saturday. This summarizes the
  prior U.S. trading day and leaves time for the `03:15 UTC` interim refresh and
  several resolver cycles to finish.
- Manual trigger: allow `workflow_dispatch` with optional `run_date`.
- If no benchmark data changed since the previous published run, skip NVIDIA,
  do not overwrite `insights/latest.json`, do not create dated public artifacts,
  and let the workflow finish without a commit or deploy.
- If NVIDIA fails, publish deterministic insights and record the LLM failure in
  the run manifest.
- Commit only generated `insights/` artifacts and deploy the website only when
  public insight artifacts changed.

Required secrets:

- `NVIDIA_API_KEY`: optional. If absent, run deterministic-only mode. Store this
  in GitHub Secrets, not in the repo.
- `NVIDIA_MODEL_ID`: optional. Defaults to
  `meta/llama-3.1-8b-instruct`.
- `NVIDIA_BASE_URL`: optional. Default to
  `https://integrate.api.nvidia.com/v1`.

Secrets must never be written to artifacts. `llm_request.redacted.json` should
keep model name, endpoint host, prompt text, and input hashes, but not the
authorization header.

## Website And API Placement

V1 public surfaces:

- `/insights`: daily insight feed with data freshness, priority ordering, and
  evidence links.
- `/api`: API documentation now includes the insight feed endpoint and example
  payloads.
- `/risk-appetite`: show risk-regime and model-agreement insights near the
  existing calculation explanation in a future page-specific integration.
- `/leaderboards/latest-weekly` and `/leaderboards/latest-monthly`: show latest
  official result insights, including oracle and S&P 500 context in a future
  page-specific integration.
- `/leaderboards/benchmark-sets`: show benchmark-set fairness and current-set
  insights in a future page-specific integration.
- `/models/<model_id>`: show model-specific behavior/performance insights in a
  dedicated behavior-vs-peers section.
- `/models`: show behavior labels and compact behavior metrics on each model
  card.
- `/`: show the highest-signal behavior patterns near historical model risk
  style.
- `/risk-appetite`: documents the model behavior formulas because they share the
  same asset-risk framework as AI Risk Appetite.

Implemented Data API endpoints:

- `GET /api/v1/insights?category=&limit=&cursor=`
- `GET /api/v1/insights/{insight_id}`
- `GET /api/v1/models/behavior`
- `GET /api/v1/models/{model_id}/behavior`

Future Data API endpoints:

- `GET /api/v1/insights/latest`
- `GET /api/v1/insights/{date}`
- `GET /api/v1/models/{model_id}/insights`

The API should return the same public `Insight` objects used by the website.
Do not expose raw LLM prompts by default. Link to audit artifacts from each
insight run instead.

## Supabase Storage

Static `insights/` artifacts are the v1 source of truth. Supabase sync can be
added after the static artifact flow is stable.

Optional future tables:

- `insight_runs`: run date, generated timestamp, input hash, deterministic
  candidate count, LLM provider, LLM model, LLM status, validation status.
- `insights`: public insight rows keyed by `id`, `date`, `category`, and
  `source_type`.
- `insight_evidence`: normalized evidence links and source references.

## Validation And Tests

Required tests for implementation:

- Unit tests for deterministic candidate formulas.
- Fixture test that generates insights from a frozen small read model.
- Test with no NVIDIA key: deterministic insights still publish.
- Test with malformed LLM JSON: deterministic fallback remains valid.
- Test that LLM output cannot introduce numbers not present in candidate facts.
- Test that every public insight has title, summary, why-it-matters text,
  evidence link, `generated_at`, and `data_as_of`.
- Test that no insight uses a bare ticker without asset name when asset metadata
  is available.
- Test that stale price data generates a system insight or warning.
- Test API examples once endpoints are added.
- Run `python3 scripts/public_repo_audit.py`.
- Run `npm --prefix apps/web run build` and `npm --prefix apps/web run seo:check`
  once website/API surfaces are added.

## Implementation Phases

Phase 1: deterministic engine and artifacts - implemented

- Add insight input builder, deterministic candidate generator, validator, and
  `insights/` artifact format.
- Acceptance: deterministic `latest.json` can be generated from current repo
  data and validated locally.

Phase 2: NVIDIA LLM narrative layer - implemented

- Add NVIDIA-compatible chat completion client behind explicit env vars.
- Add JSON output validation and deterministic fallback.
- Acceptance: successful LLM run rewrites only allowed text fields and failed
  LLM run still publishes deterministic output.

Phase 3: website and Data API - partially implemented

- Add `/insights`, homepage cards, contextual page modules, and API endpoints.
- Add OpenAPI and docs examples.
- Acceptance: website and API read from the same public insight artifacts.

Phase 4: scheduling and operations - prepared

- Add daily Insights workflow, manual dispatch, run manifests, audit logging,
  and deployment on artifact change once workflow-file publication is available.
- Add runbook instructions and health checks.
- Acceptance: a scheduled run updates or no-ops cleanly without stale public
  insight data.

## Non-Goals For V1

- No external market/news ingestion.
- No investment recommendations.
- No user-personalized insights.
- No paid LLM dependency.
- No rewriting benchmark results or scores.
- No hidden private data in LLM prompts.
