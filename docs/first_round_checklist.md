# First Round Checklist

Use this checklist before running a public CapitalBench round.

## Before The Decision Deadline

- Choose a `round_id`.
- Create the round with `capitalbench init-round --round-id <id>`.
- Fill in `manifest.yaml`, including decision deadline, horizon, entry rule, and exit rule.
- Write the briefing using only information available before the deadline.
- Define the complete option list in `options.yaml`. `capitalbench init-round` defaults to the latest future-round universe, currently `configs/universes/capitalbench_universe_v2_1.yaml`; pass `--universe` only when intentionally using an older or custom universe.
- Confirm one option is the S&P 500 benchmark.
- Confirm cash is present if you want a cash comparison.
- Run `capitalbench validate-universe --round rounds/<id> --start-date <date> --end-date <date>` with `TIINGO_API_KEY` set. When the prompt includes one-year price context, validate a window long enough to prove all required lookbacks are available.
- Remove or replace any non-cash ticker that fails Tiingo validation before freezing the round.
- Import research artifacts with `capitalbench import-research`.
- Confirm `research/final_briefing.md` is copied to `briefing.md`.
- Confirm `market_fact_report.md` and `briefing_audit_report.md` are audit-only and not included in the model prompt.
- Keep source links and source ledgers in audit artifacts, not in `final_briefing.md`.
- Confirm `briefing.md` is facts-only: no interpretation, scenario analysis, "why it matters" commentary, affected-market mapping, recommendations, or rankings.
- Confirm the final briefing passes a salience-bias check: no performance-sorted return table, no one theme dominating row count, no direct option recommendations, and counterbalancing source-reported facts preserved where available.
- Optionally run `capitalbench fetch-universe-performance --round rounds/<id> --as-of-date <cutoff-date>` to add mechanical full-universe price, risk, and benchmark-relative context.
- If generated, confirm `market_data/universe_trailing_returns.md` is sorted by option order, covers all options, and contains no recommendations, rankings, or interpretive commentary.
- Write the exact model prompt in `prompt.md`.
- Confirm the prompt allows internal learned knowledge and general market priors, while forbidding browsing, tools, live data retrieval, and intentional use of post-cutoff facts.
- Run `capitalbench hash-round --round rounds/<id>`.
- Save or publish `hashes.json`.

## Collecting Submissions

- Use the same prompt and round files for every model.
- Require `mode: closed_capability`.
- Require exactly one `selected_option_id`.
- Choose a unique `run_id` for each collection attempt.
- Decide which run will be the official public run.
- Use `--run-type official` for the public leaderboard.
- Use `--run-type stability --replicates 5` only for secondary stability analysis.
- Do not combine the official leaderboard and stability table into one score.
- If adding a newly released model, set `first_eligible_round` or `first_eligible_date_utc` so it starts with a future round.
- Do not run new models on old rounds for official scoring.
- Do not change the option universe after seeing model picks just to force more variety. Any universe change belongs in a future round.
- Use `--run-type retrospective` for any manual old-round exploration; retrospective runs are excluded from public leaderboards.
- For manual collection, save raw submissions in `runs/<run_id>/submissions/raw/`.
- For simple dry-run testing, run `capitalbench run-round --round rounds/<id> --models configs/models.example.yaml --mock --run-id <run_id> --run-type mock`.
- Use `capitalbench list-runs --round rounds/<id>` to confirm run isolation.
- For real API calls, create local copies of `.env.example`, `configs/models.example.yaml`, and `configs/pricing.example.yaml`.
- Export API keys with `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, and `XAI_API_KEY`.
- Run `capitalbench check-providers` to verify whether keys are present without printing secrets.
- Confirm model configs use deterministic provider-native settings: temperature `0`, tools/search disabled by the adapters, and the lowest provider-supported reasoning or thinking setting that still allows valid structured JSON.
- For Gemini models that reject zero thinking budget, use a small positive setting such as `reasoning_effort: low`.
- Optionally run a private provider smoke test with `capitalbench smoke-provider --provider <provider> --model <api_model_name> --round rounds/<id> --allow-real-api-calls`.
- Remember that smoke tests are private API checks; they write under `provider-smoke-tests/` and do not affect benchmark runs or leaderboards.
- Never commit `.env`, real API keys, or provider response files that contain confidential data.
- Remember that real API mode can cost money and requires `--allow-real-api-calls`.
- Inspect `runs/<run_id>/submissions/raw/`, `runs/<run_id>/submissions/parsed/`, `runs/<run_id>/raw_responses/`, and `runs/<run_id>/run_log.jsonl` after a run.
- Run `capitalbench validate-submissions --round rounds/<id> --run-id <run_id>`.
- Review `_validation_errors.json` if any submissions are invalid.
- If an official attempt has malformed JSON, truncation, provider transport failure, or schema failure, preserve the raw response and mark that attempt ineligible before retrying.
- Do not retry an official call because of the model's selected asset, confidence, or rationale quality.

## Official And Stability Runs

Official mock rehearsal:

```bash
capitalbench run-round \
  --round rounds/<id> \
  --models configs/models.example.yaml \
  --mock \
  --run-id official-mock \
  --run-type official
```

Stability mock rehearsal:

```bash
capitalbench run-round \
  --round rounds/<id> \
  --models configs/models.example.yaml \
  --mock \
  --run-id stability-mock \
  --run-type stability \
  --replicates 5
```

The official run gives each model one attempt. The stability run repeats the
same prompt to measure whether the model keeps picking the same asset. Stability
does not replace the official leaderboard.

## Private Provider Smoke Tests

- Smoke tests are not benchmark runs.
- Smoke tests do not write into `runs/<run_id>/`.
- Smoke tests do not affect validation summaries, scores, reports, or leaderboards.
- Smoke tests may cost money because they can call real provider APIs.
- API keys must come from environment variables; do not write keys into config files.
- Smoke-test outputs are stored separately under `provider-smoke-tests/`.
- Run smoke tests only with `--allow-real-api-calls`.

## After The Horizon

- Add `prices/entry_prices.csv`.
- Add `prices/exit_prices.csv`.
- Prefer price columns `option_id,symbol,date,close,adj_close`.
- Use adjusted close prices when available.
- If using Tiingo for selected-only scoring prices, run `capitalbench fetch-prices --round rounds/<id> --run-id <run_id> --entry-date YYYY-MM-DD --exit-date YYYY-MM-DD`; this fetches only picked assets plus S&P 500 and CASH.
- Confirm every selected non-cash option and the S&P 500 benchmark have entry and exit prices.
- To populate `regret_vs_best_option` and `rank_among_options`, run the same fetch command with `--full-universe` so every option in the frozen universe is priced.
- If the entry date has resolved but the exit date has not, use `--side entry --full-universe` to write only full-universe entry prices as the model-facing starting snapshot. After the exit date resolves, fetch both entry and exit prices together before official scoring.
- Confirm the requested entry and exit dates are the round's intended pricing dates. Manual price fetching requires Tiingo rows to exactly match those dates; scheduled resolution can fall back to the most recent prior Tiingo exit row, but manifests should still use the intended trading close.
- Run `capitalbench score-round --round rounds/<id> --run-id <run_id>`.
- Run `capitalbench publish-report --round rounds/<id> --run-id <run_id>`.
- If both official and stability runs exist, run
  `capitalbench publish-round-summary --round rounds/<id> --official-run-id <official_run_id> --stability-run-id <stability_run_id>`.
- Run `capitalbench audit-round --round rounds/<id> --run-id <run_id>`.
- Publish the report, hashes, options, prompt, briefing, and price source notes.

## Cumulative Publishing

- Publish the newest completed round's official leaderboard with
  `capitalbench publish-latest --rounds-dir rounds --output latest`.
- After more than one round is resolved, publish cumulative outputs with
  `capitalbench publish-cumulative --rounds-dir rounds --output cumulative`.
- Check discovery with `capitalbench cumulative-status --rounds-dir rounds`.
- If any round has multiple official-score-eligible runs, create
  `cumulative_selection.yaml` and identify the exact official and stability run
  for each included round.
- Remember that the latest leaderboard is only the newest resolved round.
- Remember that the cumulative official scorecard compares total model return with total oracle return
  across all resolved rounds in the track and labels shorter model histories.
- Remember that the cumulative stability leaderboard averages repeated-run alpha
  and consistency across resolved rounds where each model participated.
- Models can have different `resolved_rounds` counts. This is expected for new
  future-only models.
- Do not create a weighted mega-score from official and stability results.
