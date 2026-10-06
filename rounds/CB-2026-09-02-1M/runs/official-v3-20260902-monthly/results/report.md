# CapitalBench Report: CB-2026-09-02-1M / official-v3-20260902-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260902-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-02-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-02
- Decision deadline: 2026-09-03T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-03
- Exit date: 2026-10-05
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.57 | Oil spike from geopolitics and mixed equity pullbacks with quality signals in financials and banks suggest selective reversal opportunities amid normal dispersion. | Geopolitical escalation in Strait of Hormuz; FOMC rate decision volatility; Oil price reversal after spike; Equity sector rotation away from energy |
| xai-grok-4-6 | xai | portfolio | FINANCIALS | 3 | 0.56 | SPY is slightly lower after a three-day decline while crude spiked above $90, yields rose, and FedWatch priced a 66% chance of a September hike. Short-horizon breadth is weak (about 25% of assets positive over 5 sessions) against still-positive 21-session breadth, so oil continuation coexists with rate-sensitive and cyclical pullbacks rather than a single regime. | September 15-16 FOMC and 66% implied hike odds can extend the equity and duration selloff.; Oil/Hormuz geopolitics can dominate one-month returns and crowd out quality-pullback mean reversion.; August Employment Situation on September 4 and CPI on September 11 can reverse the labor/inflation narrative quickly.; High-vol names (oil, semis, crypto, solar) have wide 80% excess ranges that can overwhelm ranked edges. |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 3 | 0.5767 | Equities fell three straight sessions on rising yields (10y ~4.79%) and 66% implied odds of a September Fed hike, while crude spiked above $90 on renewed US-Iran conflict and Strait of Hormuz disruption. Energy is the clearest supported theme; rate-sensitive and quality financials pulled back modestly and look like overreaction given solid credit and fundamentals; long-duration growth faces hike risk into the FOMC. | Rapid US-Iran de-escalation could collapse crude toward EIA's $78-85 forecast, reversing the energy thesis; A hawkish Fed hike Sept 15-16 with rising yields could pressure all equities including financials via credit and duration fears; Weak Sept 4 payrolls could trigger growth-scare selling in banks and small caps; Broadcom results and mega-cap tech swings could drive SPY sharply either way relative to picks |
| google-gemini-3-1-pro | google | portfolio | REGIONAL_BANKS | 3 | 0.58 | The market is experiencing a broad pullback with recent declines in major indexes, while energy prices have surged due to geopolitical tensions and supply constraints. | Further escalation in Middle East tensions could disrupt markets broadly.; Upcoming employment and inflation data could shift Federal Reserve rate expectations. |
| anthropic-claude-opus-5 | anthropic | portfolio | FINANCIALS | 3 | 0.5733 | Backdrop is late-cycle with re-accelerating inflation (CPI 3.4%, PCE 3.7%, euro-area 3.3%) and a market-implied 66% odds of a September Fed hike, with 10-year yields near 4.79%. Oil spiked on Strait of Hormuz/Iran escalation, which supports energy but pressures duration, rate-sensitive defensives and consumer cyclicals. Breadth is weak in the last week (24.6% positive) but healthy over 21 sessions (63.8%), so the pattern is mixed. Best asymmetry sits in high-quality pullbacks with strong prior trends and low volatility (financials, small value, regional banks) rather than in extended commodity or crypto momentum. | A September 15-16 Fed hike or hawkish surprise could hit small caps and rate-sensitive bank credit expectations rather than help margins; Escalation around the Strait of Hormuz could spike oil further, compress margins and rotate leadership into energy at the expense of financials and small value; Weak August employment report on September 4 or October 2 could trigger a cyclical and small-cap derating; Concentrated mega-cap tech leadership means SPY can outperform equal-weight and value cohorts on a single AI earnings catalyst such as Broadcom; Credit-quality surprise in regional bank commercial real estate exposure would invalidate the overreaction thesis |
| openai-gpt-5-6-sol | openai | portfolio | REGIONAL_BANKS | 3 | 0.57 | Strong manufacturing and private-demand indicators coexist with sticky inflation, rising yields, a probable September rate increase, and geopolitical energy risk. This favors selective pullback reversals over broad risk-on continuation. | A September rate increase or hawkish guidance could tighten financial conditions and hurt smaller companies and banks; Credit deterioration or renewed commercial-real-estate concerns could prevent the financial-sector reversal; Oil-supply disruption could intensify inflation and drive Treasury yields materially higher; Employment, CPI, or retail-sales releases could reveal sharper domestic-demand deterioration |
| xai-grok-4-5 | xai | portfolio | REGIONAL_BANKS | 3 | 0.59 | Elevated cross-asset dispersion with oil spike on Hormuz/Iran risks, rising yields, mixed ISM/labor data, and Fed hike odds near 66% create mixed continuation/reversal setup; quality pullbacks in financials/banks favored over stretched momentum or rate-sensitive losers for 1M window. | September FOMC 25bp hike probability at 66% could extend equity and rate-sensitive pressure; Further Hormuz escalation or OPEC+ surprise may reverse oil/defense correlations unpredictably; August employment and CPI prints inside window could shift growth/inflation narrative sharply; High active-return dispersion raises single-name/sector gap risk versus SPY |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SEMICONDUCTORS | Semiconductors | 552.6 | 633.9 | 0.14712269272529843 | 1 |
| BRAZIL | Brazil Equities | 38.13 | 42.97999954223633 | 0.12719642124931352 | 2 |
| CYBERSECURITY | Cybersecurity | 95.32 | 106.01 | 0.11214855224506937 | 3 |
| TECHNOLOGY | Technology Sector | 185.97 | 200.93 | 0.08044308221756191 | 4 |
| MOMENTUM | US Momentum Equities | 299.42 | 323.14 | 0.07921982499499025 | 5 |
| ETHEREUM_ETF | Ethereum ETF | 19.02 | 20.43000030517578 | 0.07413250815855843 | 6 |
| TAIWAN | Taiwan Equities | 110.13 | 118.0 | 0.07146100063561245 | 7 |
| SOUTH_KOREA | South Korea Equities | 180.56 | 191.4600067138672 | 0.0603677819775541 | 8 |
| NASDAQ100 | Nasdaq 100 | 717.67 | 756.2 | 0.05368762801844862 | 9 |
| BITCOIN_ETF | Bitcoin ETF | 46.35 | 48.560001373291016 | 0.04768072002785351 | 10 |
| LARGE_GROWTH | US Large-Cap Growth | 123.43 | 128.35 | 0.039860649760998124 | 11 |
| BROAD_AI_TECH | Broad AI Technology | 64.3 | 66.85 | 0.03965785381026432 | 12 |
| US_DOLLAR | US Dollar | 28.01 | 28.989999771118164 | 0.03498749629125886 | 13 |
| SOFTWARE | Software | 106.95 | 109.72 | 0.02589995324918193 | 14 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.81 | 125.84 | 0.024672257959449606 | 15 |
| JAPAN | Japan Equities | 97.9 | 99.3 | 0.01430030643513791 | 16 |
| OIL | Crude Oil | 142.09 | 143.99000549316406 | 0.013371845261201054 | 17 |
| BROAD_COMMODITIES | Broad Commodities | 19.09 | 19.25 | 0.00838135149292829 | 18 |
| SP500 | S&P 500 | 773.17 | 774.83 | 0.0021470051864402873 | 19 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.42 | 91.44 | 0.00021877050973517775 | 20 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 21 |
| TOTAL_US_MARKET | Total US Stock Market | 380.93 | 380.6 | -0.0008663008951775852 | 22 |
| COPPER | Copper | 39.91 | 39.86000061035156 | -0.0012528035491965461 | 23 |
| EMERGING_MARKETS | Emerging Markets | 60.99 | 60.61 | -0.006230529595015577 | 24 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.4 | 46.790000915527344 | -0.012869178997313435 | 25 |
| YEN | Japanese Yen | 58.87 | 58.02000045776367 | -0.014438585735286669 | 26 |
| COMMUNICATIONS | Communication Services Sector | 113.38 | 111.61 | -0.015611218909860614 | 27 |
| ENERGY | Energy Sector | 64.62 | 63.45 | -0.01810584958217276 | 28 |
| AGRICULTURE | Agriculture Commodities | 29.09 | 28.459999084472656 | -0.021656958251197733 | 29 |
| INDUSTRIALS | Industrials Sector | 174.56 | 170.1 | -0.02554995417048589 | 30 |
| MID_CAP | US Mid-Cap Stocks | 75.75 | 73.68 | -0.02732673267326724 | 31 |
| MUNICIPAL_BONDS | Municipal Bonds | 104.0 | 101.12000274658203 | -0.02769228128286505 | 32 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.21 | 76.98 | -0.02815301098346157 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 107.0 | 103.98 | -0.028224299065420566 | 34 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.95 | 94.13 | -0.029087158329035634 | 35 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.44 | 71.13 | -0.03145424836601307 | 36 |
| HEALTHCARE | Healthcare Sector | 173.26 | 167.37 | -0.03399515179499013 | 37 |
| EURO | Euro | 107.28 | 103.58999633789062 | -0.03439600729035586 | 38 |
| LARGE_VALUE | US Large-Cap Value | 259.38 | 250.36 | -0.034775233248515613 | 39 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.5 | 101.83 | -0.03478672985781994 | 40 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.28 | 88.92 | -0.03641092327698314 | 41 |
| CHINA | China Equities | 54.37 | 52.28 | -0.038440316350928705 | 42 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.66 | 89.08999633789062 | -0.038527991173207154 | 43 |
| SMALL_CAP | US Small-Cap Stocks | 295.19 | 283.38 | -0.04000813035671946 | 44 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.05 | 211.12 | -0.04058168598045897 | 45 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.45 | 90.33999633789062 | -0.04351512612079811 | 46 |
| SMALL_VALUE | US Small-Cap Value | 223.72 | 213.27 | -0.04671017343107453 | 47 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.26 | 81.04 | -0.04949566033309871 | 48 |
| BIOTECH | Biotechnology | 164.38 | 156.19 | -0.04982357951088934 | 49 |
| UNITED_KINGDOM | United Kingdom Equities | 48.68 | 46.19 | -0.05115036976170917 | 50 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.46 | 110.42 | -0.05186330070410439 | 51 |
| LOW_VOL | US Low Volatility Equities | 75.24 | 71.09 | -0.05515683147262085 | 52 |
| CANADA | Canada Equities | 62.47 | 58.78 | -0.05906835280934841 | 53 |
| MATERIALS | Materials Sector | 52.62 | 49.5 | -0.05929304446978334 | 54 |
| EUROPE | Europe Equities | 91.74 | 86.28 | -0.059516023544800456 | 55 |
| REGIONAL_BANKS | Regional Banks | 74.87 | 70.39 | -0.059837050888206234 | 56 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.07 | 77.11 | -0.060436212988911886 | 57 |
| AUSTRALIA | Australia Equities | 30.37 | 28.43000030517578 | -0.06387881774198945 | 58 |
| MEXICO | Mexico Equities | 76.97 | 71.87000274658203 | -0.06625954597139105 | 59 |
| INDIA | India Equities | 49.92 | 46.57 | -0.0671073717948718 | 60 |
| DIVIDEND | US Dividend Equities | 35.08 | 32.72 | -0.06727480045610035 | 61 |
| UTILITIES | Utilities Sector | 43.03 | 39.97 | -0.07111317685335816 | 62 |
| GOLD | Gold | 84.1 | 77.82 | -0.0746730083234245 | 63 |
| FINANCIALS | Financials Sector | 58.56 | 53.88 | -0.07991803278688525 | 64 |
| REAL_ESTATE | Real Estate Sector | 44.25 | 40.67 | -0.08090395480225987 | 65 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 225.98 | 206.98 | -0.08407823701212502 | 66 |
| SOLAR | Solar Energy | 47.72 | 43.67 | -0.08487007544006697 | 67 |
| SILVER | Silver | 60.55 | 55.130001068115234 | -0.08951278169917032 | 68 |
| METALS_MINING | Metals and Mining | 118.38 | 107.76 | -0.08971109984794723 | 69 |
| SOUTH_AFRICA | South Africa Equities | 71.82 | 63.16999816894531 | -0.1204400143560942 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 35.0 | -0.01810584958217276 | -0.006337047353760466 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | REGIONAL_BANKS | 35.0 | -0.059837050888206234 | -0.02094296781087218 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | FINANCIALS | 30.0 | -0.07991803278688525 | -0.023975409836065574 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | FINANCIALS | 35.0 | -0.07991803278688525 | -0.027971311475409835 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SMALL_VALUE | 35.0 | -0.04671017343107453 | -0.016348560700876084 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 30.0 | -0.059837050888206234 | -0.01795111526646187 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 35.0 | -0.059837050888206234 | -0.02094296781087218 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | INDUSTRIALS | 35.0 | -0.02554995417048589 | -0.00894248395967006 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 30.0 | -0.08407823701212502 | -0.025223471103637506 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 35.0 | -0.059837050888206234 | -0.02094296781087218 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | FINANCIALS | 35.0 | -0.07991803278688525 | -0.027971311475409835 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SMALL_VALUE | 30.0 | -0.04671017343107453 | -0.014013052029322359 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | REGIONAL_BANKS | 35.0 | -0.059837050888206234 | -0.02094296781087218 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 65.0 | 0.0021470051864402873 | 0.0013955533711861867 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | REGIONAL_BANKS | 35.0 | -0.059837050888206234 | -0.02094296781087218 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | FINANCIALS | 35.0 | -0.07991803278688525 | -0.027971311475409835 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 30.0 | -0.08407823701212502 | -0.025223471103637506 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | FINANCIALS | 35.0 | -0.07991803278688525 | -0.027971311475409835 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SMALL_VALUE | 35.0 | -0.04671017343107453 | -0.016348560700876084 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 30.0 | 0.0021470051864402873 | 0.0006441015559320862 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 2 | 0.57 | 0.0021470051864402873 | -0.019547414439685995 | -0.021694419626126282 | 0.16667010716498443 |  | False | False |
| xai-grok-4-6 | FINANCIALS | 3 | 0.56 | -0.07991803278688525 | -0.04367577062035383 | -0.04582277580679412 | 0.19079846334565226 |  | False | False |
| anthropic-claude-fable-5 | ENERGY | 3 | 0.5767 | -0.01810584958217276 | -0.051255425000698226 | -0.053402430187138514 | 0.19837811772599667 |  | False | False |
| google-gemini-3-1-pro | REGIONAL_BANKS | 3 | 0.58 | -0.059837050888206234 | -0.05510892287417975 | -0.057255928060620034 | 0.20223161559947817 |  | False | False |
| anthropic-claude-opus-5 | FINANCIALS | 3 | 0.5733 | -0.07991803278688525 | -0.06227098744274779 | -0.06441799262918807 | 0.20939368016804621 |  | False | False |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 3 | 0.57 | -0.059837050888206234 | -0.06292733131560438 | -0.06507433650204467 | 0.2100500240409028 |  | False | False |
| xai-grok-4-5 | REGIONAL_BANKS | 3 | 0.59 | -0.059837050888206234 | -0.07413775038991952 | -0.0762847555763598 | 0.22126044311521795 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 27964a4e4b193047d90e60b3065e0f8bcd93fee3688f6a973f90e504d853f2a3 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 3d3fd1a1e41a6e39e8547f4cfd44b60bf0a73dc0cae369149291cae40957931a |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | edbc4942057a0531f2990b375811bae0ae2a89f4707577ccc5b6d0e0b1eb92b1 |
| market_data/universe_decision_context.md | 100bee44716409b70b4db2ce6f8ad159bbb2a2a1d30e8e07c1dd816201115e9e |
| market_data/universe_decision_context.json | 1a0dfa2eea40a3bc6cc280970963f8ee18015b272a8f1304d14cf7cc2d06dc48 |
| market_data/decision_context_source_history.json | 8daa67b23206c31393b477d49e72053c69383ede566ef5c00f96eb1f139d5bbc |
| market_data/universe_quality_evidence.md | 04e80f965ae2a9e027900fa6968514f8d8a45bb5125625cdffd54100c95c865f |
| market_data/universe_quality_evidence.json | 81f69b982de3aaddccbbe234587fcdd1db6df34f6bceac5f25ab93a29ef54d94 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 0d992d076b8828c3866e5759b630ea318038b9b9dd21ff6967081552d53a1b3f | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | efd6cc94ef43bc8610242dd03aefef4813d59d70f402fd982bfd3fe0ad328072 | yes |
| Final briefing | research/final_briefing.md | model-facing | 27964a4e4b193047d90e60b3065e0f8bcd93fee3688f6a973f90e504d853f2a3 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
