# CapitalBench Briefing Audit — 2026-08-30

Research cutoff: **2026-08-30T20:32:22Z**

## Scope and provenance

- Fresh-research requirement: **pass**. The source set was browsed on August 30, 2026; no prior CapitalBench input report was opened or copied.
- Latest completed U.S. session: **August 28, 2026**.
- Primary-source preference: **pass**. Treasury, Federal Reserve, BEA, BLS, Census, EIA, NYSE, ECB, Eurostat, China's NBS, and NVIDIA Investor Relations support the underlying facts. AP supports the market-close recap.
- Cutoff control: **pass**. Every included publication or datapoint was public by 2026-08-30T20:32:22Z.
- Forecast labeling: **pass**. NVIDIA's outlook is identified as company guidance. No consensus estimate or model-created forecast is included.
- Revision labeling: **pass**. Advance, preliminary, revised, estimated, and company-reported figures retain those labels where material.

## Claim verification matrix

| Topic | Verification result | Notes |
|---|---|---|
| August 28 U.S. index closes | Pass | AP index recap and main market story agree on final levels and daily changes. |
| August 28 Treasury curve | Pass | Official Treasury par-yield table; 2-, 10-, and 30-year changes also align with AP's rounded market account. |
| Chair Warsh remarks | Pass | Taken from the Federal Reserve's prepared speech; statements are attributed to the Chair and not represented as an FOMC decision. |
| Q2 GDP and corporate profits | Pass | BEA second estimate dated August 26. Annualized and quarterly concepts are not mixed. |
| July income, PCE, and inflation | Pass | BEA release dated August 26. Nominal spending, real spending, and price-index measures remain distinct. |
| July CPI and PPI | Pass | BLS releases dated August 12 and 13. Monthly changes are seasonally adjusted; year-over-year changes are the published 12-month rates. |
| July employment | Pass | BLS release dated August 7, including May/June revisions. |
| March 2026 CES benchmark | Pass | BLS preliminary benchmark release dated August 28. It is not substituted into current monthly payroll levels. |
| June JOLTS | Pass | BLS release dated August 4; July release remains scheduled for September 1. |
| July retail sales | Pass | Census advance estimate dated August 14; explicitly nominal and not price-adjusted. |
| July production and utilization | Pass | Federal Reserve G.17 dated August 18; July values marked preliminary in the source table. |
| July goods trade and inventories | Pass | Census advance indicators dated August 27. |
| July housing | Pass | Census/HUD release dated August 18; confidence-interval uncertainty retained. |
| August 21 petroleum stocks | Pass | EIA weekly data released August 26. August 28 correction applied to distillate direction. |
| Euro-area data and ECB decision | Pass | Eurostat flash/estimate releases and ECB July 23 decision. |
| China July activity | Pass | National Bureau of Statistics English releases dated August 18. |
| NVIDIA fiscal Q2 | Pass | Company investor-relations release dated August 26; outlook is labeled as company-issued. |
| Event calendar | Pass | Cross-checked against BLS, Census, BEA, Federal Reserve, EIA, and NYSE calendars. |

## Corrections and conflicts handled

1. **EIA distillates:** the August 26 summary initially used the wrong direction. EIA's August 28 correction says distillate inventories fell 2.2 million barrels; the corrected direction is used.
2. **Treasury intraday versus close:** AP's intraday/rounded descriptions are not substituted for the Treasury's official daily par-yield estimates. The briefing identifies the official August 28 curve separately.
3. **Payroll benchmark versus current series:** the preliminary -79,000 total-nonfarm benchmark estimate is not treated as a revision already applied to monthly payroll data.
4. **GDP frequency:** BEA's 1.5% Q2 real GDP figure is an annualized quarterly rate. Eurostat's 0.4% Q2 figure is a quarter-over-quarter rate. They are labeled separately.
5. **Inflation measures:** CPI, PPI, and PCE figures are kept as different indexes and are not directly merged.

## Balance and completeness checks

- Growth: GDP, GDI, private domestic demand, production, retail, housing, and trade covered.
- Inflation: CPI, PPI, monthly PCE, quarterly PCE prices, energy, and Treasury real yields covered.
- Labor: payrolls, unemployment, revisions, JOLTS, and the preliminary benchmark covered.
- Policy/rates: nominal and real Treasury curves, Chair speech, latest minutes, and upcoming FOMC meeting covered.
- Markets: large-cap, technology-heavy, industrial, and small-cap U.S. index closes covered without option-level mapping.
- International: euro-area growth/inflation/policy and China production/consumption covered.
- Company information: one high-salience AI-infrastructure issuer update included and labeled as company-issued.
- Catalysts: all major scheduled U.S. releases inside the weekly and monthly windows covered.
- Conflicting signals preserved: stronger private domestic demand and industrial production coexist with weaker payrolls, retail sales, and housing; CPI/core CPI differ from PCE/core PCE; inflation expectations in the Chair's remarks are described as stable while current inflation is described as too high.

## Model-facing artifact checks

- Contains source URLs or citation ledger: **no**.
- Contains a recommendation, ranking, preferred security, or allocation: **no**.
- Maps facts to CapitalBench options or sectors: **no**.
- Contains manually selected price-return rows: **no**.
- Contains or summarizes V3 quality scores, ranks, or slate rows: **no**.
- Includes the required neutrality statement: **yes**.
- Includes cutoff, latest market session, release status, and event dates: **yes**.
- Leaves full-universe price, risk, benchmark, quality, and V3 slate data to deterministic CapitalBench artifacts: **yes**.

## Excluded material

- Market-implied policy probabilities reported by third parties, because the value can change continuously and is not needed for the fixed briefing.
- Analyst earnings estimates, price targets, newsletter commentary, and social-media claims.
- Any fact published after the research cutoff.
- Any recommendation or inference assigning a fact to a particular CapitalBench option.

Audit conclusion: **adequate for a new Portfolio V3.0 weekly and monthly run, subject to successful research import, full-universe validation, deterministic decision-context generation, and round hashing.**
