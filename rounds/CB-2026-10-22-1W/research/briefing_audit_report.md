# Briefing audit — October 22, 2026

This is the operator/Codex audit, not an external-model review. Direct browsing
supports the source ledger. Only final_briefing.md is model-facing; this audit
and the fact report remain audit-only.

## Factual and salience checks

- Reviewed dates distinguish publications from observation periods and forecast
  years. All facts precede the import cutoff. Claims revisions, nominal sales,
  forecasts, and uncertainty are labeled; pending contracts are not closed sales.
- Final briefing contains no links, citations, source ledger, option ranking,
  allocation recommendation, expected-return mapping, scenario analysis, or
  selected mechanical return rows. Neutrality statements appear at both ends.
- Positive constituent breadth is preserved beside negative cap-weighted index
  observations. Claims levels and continuing-claims direction both remain.
  Inflation subcomponents and policy uncertainty are retained. No sector or
  issuer receives a recommendation or a disproportionate series of rows.
- Price history remains descriptive, not predictive. Neither Q1 ranks/scores nor
  candidate-slate interpretations appear in the research. Static exposure
  clusters are supplied by the mechanical option table, not relabeled here.
- FOMC, GDP, income/outlays, and ECI occur within both windows; November releases
  are explicitly monthly-window information. October 23 entry and all exits are
  prospective. No historical round is revised or rerun.

## Pre-call machine checks

Fresh full histories through October 22 are available for all 69 non-cash
tickers: 49 from Tiingo, 20 from the existing Yahoo fallback after Tiingo HTTP
429 responses. Every history contains 298 observations; generated profiles
contain all 70 options and have 100% Q1 coverage. The ticker set exactly matches
the retained successful Tiingo validation evidence. The fallback and prior
validation are disclosed in universe_validation_cached_evidence.json rather
than misrepresented as a new full-universe Tiingo validation.

The separate input_verification.json records full-universe row coverage and
option order, fresh history sources, Q1 coverage of at least 90%, the unchanged
45/30/15/10 formula, and exactly one complete context appendix, quality table,
and five-lane V3 slate in each effective prompt. SPY must be present in the
slate. No Q2 selection quotas, continuation eligibility, tools, or agent loop.
Preserve ticker-validation evidence and original source histories; disclose
fallback data providers if needed. Freeze hashes before calling any model and
require one valid decision for every model in the exact six-model frozen roster.
