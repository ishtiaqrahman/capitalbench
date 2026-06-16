# Prompt 2 Briefing Audit Report - CB-2026-06-15

## Scope

This audit checks the prompt 1 market fact report and the prompt 3 final briefing for freshness, source traceability, neutrality, and round readiness. It was prepared manually by Codex. No model API was used to generate the research artifacts.

## Audit Summary

| check | result | note |
| --- | --- | --- |
| Research artifacts prepared manually without report-generation API calls | pass | Browser-based source gathering only |
| Fresh round folders created | pass | `rounds/CB-2026-06-15-1W` and `rounds/CB-2026-06-15-1M` |
| Fable 5 excluded from model roster | pass | Per-round no-Fable configs added |
| Decision / entry dates set to June 15, 2026 | pass | Manifests patched for both horizons |
| Weekly exit date | pass | June 22, 2026 |
| Monthly exit date | pass | July 15, 2026 |
| Full-universe trailing returns generated without API keys | pass | Yahoo Finance public chart data, 70 rows, 0 failed options |
| Official macro source traceability | pass | BLS, BEA, Federal Reserve, Census, ISM, DOL, NAR, Conference Board, University of Michigan |
| Final briefing avoids recommendations and rankings | pass | Factual tables only |
| Final briefing avoids URLs | pass | Source URLs kept in audit-only prompt 1 report |
| Prompt builder can append return table | pass | Final briefing does not duplicate the full table; `market_data/universe_trailing_returns.md` exists |

## Freshness Review

| area | latest available item used | freshness note |
| --- | --- | --- |
| Market close / ETF context | 2026-06-15 adjusted close rows from Yahoo public chart data | same decision date |
| VIX | Cboe page as of 2026-06-15, displayed 8:15 PM ET data timestamp | same decision date |
| Industrial production | Federal Reserve G.17 released 2026-06-15 | same decision date |
| H.15 rates | Federal Reserve H.15 released 2026-06-15 with rows through 2026-06-12 | latest official table available on page |
| CPI | BLS May CPI released 2026-06-10 | latest CPI before decision |
| PPI | BLS May PPI released 2026-06-11 | latest PPI before decision |
| Employment | BLS May Employment Situation released 2026-06-05 | latest employment report before decision |
| Retail sales | Census April retail sales released 2026-05-14; May release scheduled 2026-06-17 | latest available before decision |
| Housing | Existing-home May release 2026-06-09; starts/new-home releases from May | latest available before decision |

## Coverage Gaps

| gap | treatment |
| --- | --- |
| Some credit-spread and flow indicators were not collected in this research cycle | Kept out of final briefing rather than filling with weak secondary estimates |
| H.15 rates do not show June 15 rate observations | Labeled as June 15 release with June 12 observations |
| Market news around Iran / Strait of Hormuz is not official government data | Labeled as public market-news reporting |
| Full source URLs are not included in the model-facing briefing | Kept in prompt 1 audit artifact to reduce model-facing clutter |
| Full-universe return table is not duplicated in final briefing | Prompt builder appends `market_data/universe_trailing_returns.md` to the model input |

## Final Briefing Neutrality Check

The final briefing:

- states that it is factual context only;
- does not select or rank CapitalBench options;
- does not provide portfolio construction guidance;
- does not include source URLs;
- labels forecasts and estimates where present;
- labels scheduled events separately from observed data;
- keeps weekly and monthly timeline facts explicit.

## Round Readiness Checks To Run After Import

| command | purpose |
| --- | --- |
| `PYTHONPATH=src python3 -m capitalbench import-research --round rounds/CB-2026-06-15-1W ...` | copy prompt artifacts into weekly round |
| `PYTHONPATH=src python3 -m capitalbench import-research --round rounds/CB-2026-06-15-1M ...` | copy prompt artifacts into monthly round |
| `PYTHONPATH=src python3 -m capitalbench audit-round --round rounds/CB-2026-06-15-1W` | validate weekly round package |
| `PYTHONPATH=src python3 -m capitalbench audit-round --round rounds/CB-2026-06-15-1M` | validate monthly round package |
| `PYTHONPATH=src python3 - <<'PY' ... build_prompt(...) ... PY` | verify model input can be assembled |

## Model Run Configuration

Use these model config files when the actual official calls are made:

- Weekly: `rounds/CB-2026-06-15-1W/configs/models.official-20260615-no-fable.yaml`
- Monthly: `rounds/CB-2026-06-15-1M/configs/models.official-20260615-no-fable.yaml`

These configs include:

- OpenAI GPT-5.5
- Claude Opus 4.7
- Claude Opus 4.8
- Gemini 3.1 Pro
- Grok 4.3

They exclude:

- Anthropic Claude Fable 5
