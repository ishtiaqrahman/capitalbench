# Prompt 2 Briefing Audit Report - CB-2026-06-16

## Scope

This audit checks the prompt 1 market fact report and prompt 3 final briefing for freshness, source traceability, neutrality, and round readiness. It was prepared manually by Codex. No model API was used to generate the research artifacts.

## Audit Summary

| check | result | note |
| --- | --- | --- |
| Research artifacts prepared manually without report-generation API calls | pass | Browser-based public source gathering only |
| Fresh weekly round folder created | pass | `rounds/CB-2026-06-16-1W` |
| Fresh monthly round folder created | pass | `rounds/CB-2026-06-16-1M` |
| Fable 5 excluded from model roster | pass | Per-round no-Fable configs copied from the prior no-Fable run and renamed for June 16 |
| Decision and entry dates set to June 16, 2026 | pass | Both manifests patched |
| Weekly exit date | pass | June 23, 2026 |
| Monthly exit date | pass | July 16, 2026 |
| Full-universe trailing returns generated without API keys | pass | Yahoo Finance public chart data, 70 rows, 0 failed options |
| Entry prices generated without API keys | pass | Yahoo Finance public chart data, 70 rows for each horizon |
| Official macro source traceability | pass | BLS, BEA, Federal Reserve, Census, ISM, DOL, Conference Board, University of Michigan |
| Final briefing avoids recommendations and rankings | pass | Factual tables only |
| Final briefing avoids URLs | pass | URLs kept in audit-only prompt 1 report |
| Prompt builder can append return table | pending | To be verified after import |

## Freshness Review

| area | latest available item used | freshness note |
| --- | --- | --- |
| Market close / ETF context | 2026-06-16 adjusted close rows from Yahoo public chart data | same decision date |
| Major U.S. indexes | AP June 16 close data | same decision date |
| VIX | June 16 close or displayed close table | same decision date |
| Brent crude | June 16 Brent historical table and market reports | same decision date |
| Housing starts / permits | Census / HUD May 2026 release dated 2026-06-16 | same decision date |
| Industrial production | Federal Reserve G.17 released 2026-06-15 | one day old |
| H.15 rates | Federal Reserve H.15 released 2026-06-16 with observations through 2026-06-15 | latest official H.15 table before cutoff |
| CPI | BLS May CPI released 2026-06-10 | latest CPI before cutoff |
| PPI | BLS May PPI released 2026-06-11 | latest PPI before cutoff |
| Employment | BLS May Employment Situation released 2026-06-05 | latest employment report before cutoff |
| Retail sales | Census April retail sales released 2026-05-14; May release scheduled 2026-06-17 | latest available before cutoff |
| PCE | BEA April Personal Income and Outlays released 2026-05-28 | latest PCE before cutoff |

## Coverage Gaps

| gap | treatment |
| --- | --- |
| H.15 does not yet include June 16 observations | Labeled as June 16 release with June 15 observations |
| May retail sales were not yet released at the cutoff | Used April release and labeled May release as scheduled after cutoff |
| Market news around oil and geopolitical developments is not official government data | Labeled as public market-news reporting in prompt 1; final briefing keeps the close-level facts |
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
| `PYTHONPATH=src python3 -m capitalbench import-research --round rounds/CB-2026-06-16-1W ...` | copy prompt artifacts into weekly round |
| `PYTHONPATH=src python3 -m capitalbench import-research --round rounds/CB-2026-06-16-1M ...` | copy prompt artifacts into monthly round |
| `PYTHONPATH=src python3 -m capitalbench audit-round --round rounds/CB-2026-06-16-1W` | validate weekly round package |
| `PYTHONPATH=src python3 -m capitalbench audit-round --round rounds/CB-2026-06-16-1M` | validate monthly round package |
| `PYTHONPATH=src python3 - <<'PY' ... build_prompt(...) ... PY` | verify model input can be assembled |
| `rg -n "fable|anthropic-claude-fable-5|claude-fable-5" rounds/CB-2026-06-16-1W/configs rounds/CB-2026-06-16-1M/configs` | confirm no Fable model remains in configs |

## Model Run Configuration

Use these model config files when the actual official calls are made:

- Weekly: `rounds/CB-2026-06-16-1W/configs/models.official-20260616-no-fable.yaml`
- Monthly: `rounds/CB-2026-06-16-1M/configs/models.official-20260616-no-fable.yaml`

These configs include:

- OpenAI GPT-5.5
- Claude Opus 4.7
- Claude Opus 4.8
- Gemini 3.1 Pro
- Grok 4.3

They exclude:

- Anthropic Claude Fable 5
