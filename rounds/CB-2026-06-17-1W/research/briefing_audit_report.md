# Prompt 2 Briefing Audit Report - CB-2026-06-17

## Scope

This audit checks the prompt 1 market fact report and prompt 3 final briefing for freshness, source traceability, neutrality, and round readiness. It was prepared manually by Codex. No model API was used to generate the research artifacts.

## Audit Summary

| check | result | note |
| --- | --- | --- |
| Research artifacts prepared manually without report-generation API calls | pass | Browser-based public source gathering only |
| Fresh weekly round folder created | pass | `rounds/CB-2026-06-17-1W` |
| Fresh monthly round folder created | pass | `rounds/CB-2026-06-17-1M` |
| Fable 5 excluded from model roster | pass | Per-round no-Fable configs copied from the prior no-Fable run and renamed for June 17 |
| Decision and entry dates set to June 17, 2026 | pass | Both manifests patched |
| Weekly exit date | pass | June 24, 2026 |
| Monthly exit date | pass | July 17, 2026 |
| Full-universe trailing returns generated without API keys | pass | Yahoo Finance public chart data, 70 rows, 0 failed options |
| Entry prices generated without API keys | pass | Yahoo Finance public chart data, 70 rows for each horizon |
| Official macro source traceability | pass | BLS, BEA, Federal Reserve, Census, DOL |
| Final briefing avoids recommendations and rankings | pass | Factual tables only |
| Final briefing avoids URLs | pass | URLs kept in audit-only prompt 1 report |
| Prompt builder can append return table | pending | To be verified after import |

## Freshness Review

| area | latest available item used | freshness note |
| --- | --- | --- |
| Market close / ETF context | 2026-06-17 adjusted close rows from Yahoo public chart data | same decision date |
| Major U.S. indexes | AP June 17 close data | same decision date |
| FOMC statement and projections | Federal Reserve June 17 statement and SEP tables | same decision date |
| Retail sales | Census May 2026 advance retail sales released 2026-06-17 | same decision date |
| VIX | June 17 Yahoo Finance historical close | same decision date |
| Brent crude and DXY | June 17 public market-data tables | same decision date |
| H.15 rates | Federal Reserve H.15 released 2026-06-17 with observations through 2026-06-16 | latest official H.15 table before cutoff |
| Housing starts / permits | Census / HUD May 2026 release dated 2026-06-16 | one day old |
| Industrial production | Federal Reserve G.17 released 2026-06-15 | two days old |
| CPI | BLS May CPI released 2026-06-10 | latest CPI before cutoff |
| PPI | BLS May PPI released 2026-06-11 | latest PPI before cutoff |
| Employment | BLS May Employment Situation released 2026-06-05 | latest employment report before cutoff |
| PCE | BEA April Personal Income and Outlays released 2026-05-28 | latest PCE before cutoff |

## Coverage Gaps

| gap | treatment |
| --- | --- |
| H.15 June 17 release does not include June 17 Treasury observations | Labeled as June 17 release with June 16 observations |
| June jobless claims were not yet released at the cutoff | June 18 claims release listed as scheduled after cutoff |
| May PCE was not yet released at the cutoff | April PCE used and May release listed as scheduled |
| Market news around FOMC and commodities is not official government data | Labeled as public market-news or market-data reporting in prompt 1; final briefing keeps factual close-level rows |
| Full source URLs are not included in the model-facing briefing | Kept in prompt 1 audit artifact to reduce model-facing clutter |
| Full-universe return table is not duplicated in final briefing | Prompt builder appends `market_data/universe_trailing_returns.md` to the model input |

## Final Briefing Neutrality Check

The final briefing:

- states that it is factual context only;
- does not select or rank CapitalBench options;
- does not provide portfolio construction guidance;
- does not include source URLs;
- labels scheduled events separately from observed data;
- keeps weekly and monthly timeline facts explicit;
- keeps the full mechanical return table outside the briefing body so it can be appended by the prompt builder.

## Round Readiness Checks To Run After Import

| command | purpose |
| --- | --- |
| `PYTHONPATH=src python3 -m capitalbench import-research --round rounds/CB-2026-06-17-1W ...` | copy prompt artifacts into weekly round |
| `PYTHONPATH=src python3 -m capitalbench import-research --round rounds/CB-2026-06-17-1M ...` | copy prompt artifacts into monthly round |
| `PYTHONPATH=src python3 -m capitalbench audit-round --round rounds/CB-2026-06-17-1W` | validate weekly round package |
| `PYTHONPATH=src python3 -m capitalbench audit-round --round rounds/CB-2026-06-17-1M` | validate monthly round package |
| `PYTHONPATH=src python3 - <<'PY' ... build_prompt(...) ... PY` | verify model input can be assembled |
| `rg -n "fable|anthropic-claude-fable-5|claude-fable-5" rounds/CB-2026-06-17-1W/configs rounds/CB-2026-06-17-1M/configs` | confirm no Fable model remains in configs |

## Model Run Configuration

Use these model config files when the actual official calls are made:

- Weekly: `rounds/CB-2026-06-17-1W/configs/models.official-20260617-no-fable.yaml`
- Monthly: `rounds/CB-2026-06-17-1M/configs/models.official-20260617-no-fable.yaml`

These configs include:

- OpenAI GPT-5.5
- Claude Opus 4.7
- Claude Opus 4.8
- Gemini 3.1 Pro
- Grok 4.3

They exclude:

- Anthropic Claude Fable 5
