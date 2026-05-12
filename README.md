# CapitalBench

![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License: Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-green)
![Data License: CC BY 4.0](https://img.shields.io/badge/data-CC%20BY%204.0-lightgrey)
![Offline First](https://img.shields.io/badge/default-offline--first-black)

CapitalBench is an offline, auditable benchmark for one-shot LLM market
decisions.

In each round, every model receives the same frozen briefing, prompt, option
universe, and mechanical market-data table. The model must choose exactly one
investable option. After the one-month horizon resolves, CapitalBench scores
the decision against local entry and exit prices.

CapitalBench is designed for evaluation research, not investment advice. It is
not a trading system, recommendation engine, or portfolio optimizer.

```text
Status: research benchmark framework
Default behavior: offline and dry-run safe
Official score: one-shot alpha versus S&P 500
Secondary analysis: repeated-call stability
Code license: Apache License 2.0
Public artifact license: CC BY 4.0
```

## At A Glance

| Area | CapitalBench behavior |
|---|---|
| Core task | Pick exactly one option from a frozen investable universe |
| Evaluation horizon | One month |
| Model input | Frozen briefing, prompt, options, and optional mechanical market-data table |
| Model output | Strict JSON submission |
| Official result | One call per model, one selected asset, one official score |
| Stability result | Multiple calls per model, usually five, reported separately |
| Benchmark scoring | Alpha versus S&P 500, cash comparison, regret where full prices exist |
| API calls | Never made unless `--allow-real-api-calls` is passed |
| Market data fetching | Explicit only, through operator-run commands |
| Public result views | Latest round, cumulative official, cumulative stability |

## Why This Exists

LLMs increasingly produce market commentary, forecasts, and investment-related
reasoning. Many evaluations of that behavior are subjective, prompt-only, or
not time-resolved. CapitalBench makes the question concrete:

> Given the same information at the same decision time, which single market
> exposure does a model select, and how does that choice perform one month
> later?

The framework emphasizes reproducibility:

- round inputs are frozen and hashed before model calls
- research artifacts are separated from model-facing briefing text
- model submissions are schema-validated
- invalid submissions are preserved but excluded from scoring
- raw provider text is preserved for current and future runs
- each run is isolated under its own `run_id`
- official and stability results are never combined into a weighted score

## Current Public Round Status

The first official CapitalBench round has model submissions collected and is
awaiting price resolution.

| Field | Value |
|---|---|
| Round | `CB-2026-05-10-1M` |
| Official run | `official-round-1-clean` |
| Methodology | `round1-v1.0` |
| Status | Submissions collected, unscored until exit prices are available |
| Round README | `rounds/CB-2026-05-10-1M/README.md` |

## Core Protocol

Each CapitalBench round is one standalone benchmark event.

1. Create a round.
2. Import the research artifacts.
3. Freeze the model-facing briefing.
4. Freeze the option universe.
5. Optionally generate a mechanical trailing-return table.
6. Hash all round inputs.
7. Run the official one-shot model calls.
8. Optionally run a separate multi-shot stability analysis.
9. Wait for the horizon to resolve.
10. Fetch or provide entry and exit prices.
11. Score the run.
12. Publish per-round, latest, and cumulative reports.

A round is stored like this:

```text
rounds/<round_id>/
  manifest.yaml
  briefing.md
  options.yaml
  prompt.md
  hashes.json
  market_data/
  research/
  prices/
  runs/
```

Each model run is isolated:

```text
rounds/<round_id>/runs/<run_id>/
  submissions/
    raw/
    parsed/
  raw_responses/
  run_log.jsonl
  run_manifest.yaml
  validation_summary.json
  results/
```

This prevents repeated tests, retries, and mock runs from contaminating an
official result.

## Public Leaderboards

CapitalBench has exactly three public result views.

| View | Source | Purpose |
|---|---|---|
| Latest Round Leaderboard | Newest resolved round's official one-shot run | Headline result for the most recent round |
| Cumulative Official Leaderboard | Official one-shot runs across resolved rounds | Long-term one-shot decision quality |
| Cumulative Stability Leaderboard | Stability runs across resolved rounds | Repeated-call robustness and consistency |

CapitalBench does not create:

- a qualified leaderboard
- maturity tiers
- provisional, tracking, or qualified labels
- a weighted mega-score
- retroactive official backfills
- portfolio allocations

New models become eligible only for future rounds. They are not penalized for
missing older rounds, and older round leaderboards remain unchanged.

## Official Versus Stability

Official and stability tracks answer different questions and stay separate.

| Track | Calls per model | Output | Public role |
|---|---:|---|---|
| Official one-shot | 1 | `leaderboard.csv` | Headline score for the round |
| Multi-shot stability | Usually 5 | `stability.csv` | Secondary robustness analysis |

Official one-shot runs measure the first and only decision. Stability runs
measure whether the model keeps making the same decision when called repeatedly
with the same prompt, same briefing, and same options.

Example stability interpretation:

```text
Model picks: QQQ, QQQ, SPY, QQQ, TLT
Asset returns: QQQ +4%, SPY +2%, TLT -1%
Average repeated return: (4 + 4 + 2 + 4 - 1) / 5 = 2.6%
Modal pick: QQQ
Consistency: 3 / 5 = 60%
```

The stability result does not affect the official leaderboard.

## CapitalBench Universe v1.5

CapitalBench Universe v1.5 is a fixed 40-option ETF universe covering cash,
short-duration Treasuries, US equities, US style and size factors, US sectors,
bonds, credit, international equities, commodities, and AI or technology themes.

All non-cash options are public US-listed ETFs intended to be validated through
Tiingo EOD data before a public round. Descriptions shown to models are neutral
exposure descriptions, not performance predictions or recommendations.

Canonical universe file:

```text
configs/universes/capitalbench_universe_v1_5.yaml
```

| ID | Symbol | Name | Group |
|---|---:|---|---|
| `CASH` |  | Cash / Do Not Invest | cash |
| `SHORT_TREASURY` | `BIL` | Short-Term Treasury Bills | cash_and_short_duration |
| `SP500` | `SPY` | S&P 500 | us_broad_market |
| `TOTAL_US_MARKET` | `VTI` | Total US Stock Market | us_broad_market |
| `NASDAQ100` | `QQQ` | Nasdaq 100 | us_growth_and_technology |
| `LARGE_GROWTH` | `IWF` | US Large-Cap Growth | us_style_factor |
| `LARGE_VALUE` | `IWD` | US Large-Cap Value | us_style_factor |
| `MID_CAP` | `IJH` | US Mid-Cap Stocks | us_size_factor |
| `SMALL_CAP` | `IWM` | US Small-Cap Stocks | us_size_factor |
| `SMALL_VALUE` | `IWN` | US Small-Cap Value | us_style_factor |
| `DIVIDEND` | `SCHD` | US Dividend Equities | us_factor_equity |
| `LOW_VOL` | `SPLV` | US Low Volatility Equities | us_factor_equity |
| `MOMENTUM` | `MTUM` | US Momentum Equities | us_factor_equity |
| `TECHNOLOGY` | `XLK` | Technology Sector | us_sector |
| `COMMUNICATIONS` | `XLC` | Communication Services Sector | us_sector |
| `CONSUMER_DISCRETIONARY` | `XLY` | Consumer Discretionary Sector | us_sector |
| `CONSUMER_STAPLES` | `XLP` | Consumer Staples Sector | us_sector |
| `HEALTHCARE` | `XLV` | Healthcare Sector | us_sector |
| `FINANCIALS` | `XLF` | Financials Sector | us_sector |
| `INDUSTRIALS` | `XLI` | Industrials Sector | us_sector |
| `ENERGY` | `XLE` | Energy Sector | us_sector |
| `MATERIALS` | `XLB` | Materials Sector | us_sector |
| `UTILITIES` | `XLU` | Utilities Sector | us_sector |
| `REAL_ESTATE` | `XLRE` | Real Estate Sector | us_sector |
| `INTERMEDIATE_TREASURY` | `IEF` | Intermediate-Term US Treasury Bonds | bonds_and_rates |
| `LONG_TREASURY` | `TLT` | Long-Term US Treasury Bonds | bonds_and_rates |
| `TIPS` | `TIP` | Treasury Inflation-Protected Securities | bonds_and_rates |
| `INVESTMENT_GRADE_CREDIT` | `LQD` | Investment Grade Corporate Bonds | credit |
| `HIGH_YIELD_CREDIT` | `HYG` | High Yield Corporate Bonds | credit |
| `AGGREGATE_BONDS` | `AGG` | US Aggregate Bond Market | bonds_and_rates |
| `DEVELOPED_EX_US` | `VEA` | Developed Markets ex-US | international_equity |
| `EMERGING_MARKETS` | `VWO` | Emerging Markets | international_equity |
| `EUROPE` | `VGK` | Europe Equities | international_equity |
| `JAPAN` | `EWJ` | Japan Equities | international_equity |
| `CHINA` | `MCHI` | China Equities | international_equity |
| `INDIA` | `INDA` | India Equities | international_equity |
| `GOLD` | `IAU` | Gold | commodities |
| `BROAD_COMMODITIES` | `PDBC` | Broad Commodities | commodities |
| `SEMICONDUCTORS` | `SMH` | Semiconductors | ai_and_technology |
| `SOFTWARE` | `IGV` | Software | ai_and_technology |

Validate the universe before a public round:

```bash
capitalbench validate-universe \
  --options configs/universes/capitalbench_universe_v1_5.yaml \
  --start-date 2026-01-01 \
  --end-date 2026-01-31
```

`validate-universe` requires `TIINGO_API_KEY`. It never prints the key.

## Quickstart

Install locally:

```bash
python3 -m pip install --user .
```

Run tests:

```bash
python3 -m pytest
```

Run the fake example round in safe mock mode:

```bash
capitalbench run-round \
  --round rounds/example-round \
  --models configs/models.example.yaml \
  --mock \
  --run-id official-mock \
  --run-type official \
  --overwrite-run

capitalbench validate-submissions \
  --round rounds/example-round \
  --run-id official-mock

capitalbench score-round \
  --round rounds/example-round \
  --run-id official-mock

capitalbench publish-report \
  --round rounds/example-round \
  --run-id official-mock
```

The sample round uses fake prices and fake model decisions. It exists to
exercise the protocol and test the framework.

You can also run commands without installing:

```bash
PYTHONPATH=src python3 -m capitalbench --help
```

## Operating A Real Round

This is the high-level operator workflow.

1. Create a round:

```bash
capitalbench init-round \
  --round-id CB-2026-06-01-1M \
  --universe configs/universes/capitalbench_universe_v1_5.yaml
```

2. Import research artifacts:

```bash
capitalbench import-research \
  --round rounds/CB-2026-06-01-1M \
  --market-fact-report path/to/market_fact_report.md \
  --audit-report path/to/briefing_audit_report.md \
  --final-briefing path/to/final_briefing.md \
  --research-cutoff-utc "2026-06-01T21:00:00Z"
```

3. Optionally fetch mechanical trailing returns for the full universe:

```bash
capitalbench fetch-universe-performance \
  --round rounds/CB-2026-06-01-1M \
  --as-of-date 2026-06-01
```

4. Hash the frozen round inputs:

```bash
capitalbench hash-round --round rounds/CB-2026-06-01-1M
```

5. Audit before model calls:

```bash
capitalbench audit-round --round rounds/CB-2026-06-01-1M
```

6. Run the official one-shot evaluation:

```bash
capitalbench run-round \
  --round rounds/CB-2026-06-01-1M \
  --models configs/models.local.yaml \
  --pricing configs/pricing.local.yaml \
  --run-id official-20260601 \
  --run-type official \
  --allow-real-api-calls
```

7. Validate submissions:

```bash
capitalbench validate-submissions \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601
```

8. After the horizon resolves, fetch selected scoring prices:

```bash
capitalbench fetch-prices \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601 \
  --entry-date 2026-06-02 \
  --exit-date 2026-07-02
```

If the entry date has resolved but the exit date has not, fetch only the entry
side and leave exit prices untouched:

```bash
capitalbench fetch-prices \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601 \
  --entry-date 2026-06-02 \
  --side entry
```

9. Score and publish:

```bash
capitalbench score-round \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601

capitalbench publish-report \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601
```

## Research Artifacts

CapitalBench separates model-facing input from audit-only research material.

```text
rounds/<round_id>/research/
  market_fact_report.md
  briefing_audit_report.md
  final_briefing.md
  research_manifest.yaml
  research_hashes.json
```

| File | Role | Model-facing |
|---|---|---|
| `market_fact_report.md` | Source research report | No |
| `briefing_audit_report.md` | Independent audit and gap check | No |
| `final_briefing.md` | Final cleaned briefing | Yes |
| `briefing.md` | Frozen copy used by the runner | Yes |

Only `briefing.md`, `options.yaml`, `prompt.md`, and approved mechanical
market-data artifacts are included in the model prompt. Source links, source
ledgers, URLs, and audit material should remain outside `briefing.md`.

The final briefing should contain facts, dates, values, forecasts labeled as
forecasts, scheduled catalysts, and explicit uncertainties from the source
reports. It should not contain recommendations, rankings, interpretation,
scenario-to-asset mapping, or language like "best pick", "top option", "should
buy", or "will outperform".

## Model Configuration

Copy the examples before editing:

```bash
cp .env.example .env
cp configs/models.example.yaml configs/models.local.yaml
cp configs/pricing.example.yaml configs/pricing.local.yaml
```

API keys are read from environment variables:

```bash
export OPENAI_API_KEY=replace_with_openai_api_key
export ANTHROPIC_API_KEY=replace_with_anthropic_api_key
export GOOGLE_API_KEY=replace_with_google_api_key
export XAI_API_KEY=replace_with_xai_api_key
export TIINGO_API_KEY=replace_with_tiingo_api_key
```

Never commit real API keys. `.env`, `.env.*`, `configs/models.local.yaml`,
`configs/*.local.yaml`, generated local output, raw provider responses, and
provider smoke-test output are ignored by default.

Audit public-repo contents before publishing a branch:

```bash
python scripts/public_repo_audit.py
```

Check key presence without printing values:

```bash
capitalbench check-providers
```

Model configs can also define future-only eligibility:

```yaml
models:
  - model_id: "openai-gpt-5-5-pro-2026-05"
    provider: "openai"
    api_model_name: "gpt-5.5-pro"
    enabled: true
    mode: "closed_capability"
    temperature: 0
    max_completion_tokens: 3000
    max_wall_clock_seconds: 120
    reasoning_effort: null
    first_eligible_round: "CB-2026-05-15-1M"
    first_eligible_date_utc: "2026-05-15T21:00:00Z"
    model_release_date: "2026-05-08"
    notes: "Added after public release. Eligible for future rounds only."
```

Disabled models are skipped. Models whose `first_eligible_round` or
`first_eligible_date_utc` is later than the current round are also skipped.

## Provider Execution Policy

CapitalBench uses provider-native APIs and explicit safety controls.

- Real API calls require `--allow-real-api-calls`.
- Mock mode never calls external APIs.
- Tools, browsing, search, code execution, and external retrieval are disabled
  in provider payloads where the provider exposes those controls.
- Temperature is set to `0` where supported.
- Structured JSON output is requested where the provider supports it.
- Models may use internal learned knowledge and general priors.
- Models must not use live data, tools, browsing, or facts dated after the
  research cutoff.
- Reasoning or thinking is set to the lowest provider-supported setting that
  still permits valid structured output.
- Hidden reasoning tokens are logged when exposed but are not treated as
  directly comparable across providers.

Provider smoke tests are private adapter checks. They do not affect benchmark
runs or leaderboards:

```bash
capitalbench smoke-provider \
  --provider openai \
  --model REPLACE_WITH_MODEL \
  --round rounds/example-round \
  --allow-real-api-calls
```

Smoke outputs are written under:

```text
rounds/<round_id>/provider-smoke-tests/<provider>-<timestamp>/
```

Provider smoke tests may cost money.

## Validation And Audit

Validate submissions for a specific run:

```bash
capitalbench validate-submissions \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601
```

Audit the round-level artifacts:

```bash
capitalbench audit-round --round rounds/CB-2026-06-01-1M
```

Audit a specific run:

```bash
capitalbench audit-round \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601
```

Audit checks include required files, hashes, research artifacts, run manifests,
raw and parsed submissions, validation summaries, price files, results, and
reports.

## Scoring

Scoring uses local price files:

```text
prices/entry_prices.csv
prices/exit_prices.csv
```

Preferred format:

```text
option_id,symbol,date,close,adj_close
SP500,SPY,2026-06-02,500.00,500.00
NASDAQ100,QQQ,2026-06-02,430.00,430.00
CASH,,2026-06-02,1.00,1.00
```

CapitalBench prefers `adj_close` when present. If only `close` is present, it
can score the round but records a warning. CASH return is treated as `0` unless
explicitly provided.

For scoring-price fetches, CapitalBench fetches only the unique selected assets
from parsed submissions, plus the S&P 500 benchmark and CASH. It does not fetch
the full 40-option universe for scoring unless the operator explicitly passes
`--full-universe`.

```bash
capitalbench fetch-prices \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601 \
  --entry-date 2026-06-02 \
  --exit-date 2026-07-02
```

To calculate `regret_vs_best_option` and `rank_among_options`, fetch every
option in the frozen universe:

```bash
capitalbench fetch-prices \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601 \
  --entry-date 2026-06-02 \
  --exit-date 2026-07-02 \
  --full-universe
```

If only one side of the pricing window is available, add `--side entry` or
`--side exit`. For example, `--side entry --full-universe` locks starting
prices for every frozen option without creating `exit_prices.csv`.

CapitalBench requires Tiingo to return rows exactly matching the requested
entry and exit dates. It does not silently substitute the nearest trading day.

Score an official run:

```bash
capitalbench score-round \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601
```

Official run outputs:

```text
runs/<run_id>/results/returns.csv
runs/<run_id>/results/leaderboard.csv
```

Stability run outputs:

```text
runs/<run_id>/results/returns.csv
runs/<run_id>/results/stability.csv
```

## Publishing

Publish one run report:

```bash
capitalbench publish-report \
  --round rounds/CB-2026-06-01-1M \
  --run-id official-20260601
```

Publish a single-round summary combining separate official and stability runs:

```bash
capitalbench publish-round-summary \
  --round rounds/CB-2026-06-01-1M \
  --official-run-id official-20260601 \
  --stability-run-id stability-20260601
```

Publish the newest resolved round's official one-shot leaderboard:

```bash
capitalbench publish-latest \
  --rounds-dir rounds \
  --output latest
```

Publish cumulative official and stability leaderboards:

```bash
capitalbench publish-cumulative \
  --rounds-dir rounds \
  --output cumulative

capitalbench cumulative-status \
  --rounds-dir rounds
```

When `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` are configured, scoring
and publishing commands also sync published website rows to Supabase. Without
those variables, local publishing continues and prints a skip message.

Manual website sync:

```bash
capitalbench sync-web \
  --round rounds/CB-2026-05-10-1M \
  --run-id official-round-1-clean

capitalbench sync-web \
  --rounds-dir rounds \
  --include-cumulative
```

Use the dedicated CapitalBench Supabase project for production sync. Keep the
project ref, account details, and service credentials in local CLI state,
GitHub Actions secrets, Supabase secrets, or Cloudflare Pages env vars, not in
committed documentation.

### Automated Resolution

Provider model runs are still started manually. After a run is valid, accept it
once; acceptance creates the round-specific resolution job:

```bash
capitalbench accept-run \
  --round rounds/CB-2026-05-10-1M \
  --run-id official-round-1-clean
```

Acceptance refuses runs unless they are non-mock official runs with
`official_score_eligible: true`, zero invalid submissions, a valid parsed
submission for every enabled model, matching round hashes, and required round
files.

When Supabase service credentials are configured, `accept-run` upserts a
service-role-only `automation_jobs` row. The permanent GitHub Actions resolver
checks due jobs on a schedule, claims one atomically, fetches exit prices,
scores the round, publishes reports, updates latest and cumulative leaderboards,
syncs Supabase, commits generated artifacts, and optionally triggers a
Cloudflare Pages rebuild.

Manual resolver commands are available for recovery and dry operations:

```bash
capitalbench automation-status --rounds-dir rounds

capitalbench automation-run \
  --rounds-dir rounds \
  --max-jobs 3

capitalbench automation-resolve \
  --rounds-dir rounds \
  --round-id CB-2026-05-10-1M \
  --run-id official-round-1-clean

capitalbench automation-retry --round rounds/CB-2026-05-10-1M
capitalbench automation-cancel --round rounds/CB-2026-05-10-1M
```

If a round has multiple official-score-eligible runs, CapitalBench will not
guess. Provide an explicit selection file:

```yaml
rounds:
  CB-2026-06-01-1M:
    official_run_id: official-20260601
    stability_run_id: stability-20260601
```

## Command Reference

| Command | Purpose |
|---|---|
| `init-round` | Create a new round directory |
| `import-research` | Import and hash research artifacts |
| `hash-round` | Hash frozen round inputs |
| `fetch-universe-performance` | Fetch mechanical trailing returns for prompt context |
| `validate-universe` | Validate option tickers through Tiingo |
| `run-round` | Run mock or real provider calls |
| `list-runs` | List isolated runs for a round |
| `validate-submissions` | Validate raw submissions |
| `fetch-prices` | Fetch selected or full-universe scoring prices |
| `score-round` | Score parsed submissions |
| `publish-report` | Generate a run report |
| `publish-round-summary` | Generate a round summary with official and stability sections |
| `publish-latest` | Publish latest resolved official leaderboard |
| `publish-cumulative` | Publish cumulative official and stability leaderboards |
| `accept-run` | Accept a valid official run and schedule automated resolution |
| `automation-run` | Claim and run due automated resolution jobs |
| `automation-resolve` | Resolve one accepted round immediately |
| `automation-status` | List local automation jobs |
| `automation-retry` | Retry a local automation job |
| `automation-cancel` | Cancel a local automation job |
| `sync-web` | Sync public benchmark rows and artifacts to Supabase |
| `cumulative-status` | Show cumulative discovery and selection status |
| `audit-round` | Audit reproducibility artifacts |
| `check-providers` | Check API key presence without printing values |
| `smoke-provider` | Run a private provider adapter smoke test |

## Repository Layout

```text
configs/
  models.example.yaml
  pricing.example.yaml
  universes/
docs/
  protocol.md
  scoring.md
  fairness.md
  limitations.md
  first_round_checklist.md
  methodology_versions.md
rounds/
  example-round/
  CB-2026-05-10-1M/
apps/web/
supabase/
src/capitalbench/
tests/
```

## Documentation

- `docs/protocol.md`: round lifecycle and public result model
- `docs/scoring.md`: scoring formulas and output files
- `docs/fairness.md`: fairness rules and provider policy
- `docs/limitations.md`: known limitations and non-goals
- `docs/first_round_checklist.md`: operator checklist for a public round
- `docs/methodology_versions.md`: methodology version history

## Non-Goals

CapitalBench does not:

- provide investment advice
- recommend assets
- fetch live market prices automatically
- call live model APIs by default
- support portfolios, leverage, shorting, or multiple selections
- backfill new models into old official rounds
- combine official and stability results into one score
- include a website in this repository

## Contributing

See `CONTRIBUTING.md`.

Before proposing methodology changes, keep these principles intact:

- one official pick per model per round
- official and stability results stay separate
- completed rounds remain unchanged
- new models enter future rounds only
- secrets are never committed
- public reports must be reproducible from committed artifacts

## License

Code is licensed under the Apache License 2.0. See `LICENSE`.

Public benchmark artifacts are licensed under CC BY 4.0 unless a file says
otherwise. See `DATA_LICENSE.md`.

The CapitalBench name and branding are not licensed as trademarks.

CapitalBench is not financial advice.
