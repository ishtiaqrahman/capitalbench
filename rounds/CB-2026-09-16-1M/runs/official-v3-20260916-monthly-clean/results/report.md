# CapitalBench Report: CB-2026-09-16-1M / official-v3-20260916-monthly-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260916-monthly-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-16-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-16
- Decision deadline: 2026-09-17T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-17
- Exit date: 2026-10-19
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.55 | Rate hike with resilient demand supports defensive and reversal candidates over pure continuation amid mixed equity breadth. | Further rate volatility from FOMC projections; Equity breadth contraction in growth sectors; Oil supply shocks affecting energy reversal |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.555 | The Fed hiked to 3.75-4.00% with inflation projections revised up and the 10-year at 5.01%; Brent at $105.83 and import prices +7.0% y/y keep an inflationary, hawkish backdrop. SPY is down 2.4% over 21 sessions with only 22% of assets positive, breadth weak (RSP lagging), and rate-sensitive and small-cap groups under pressure. Prior AI/semiconductor leadership has pulled back sharply but the briefing shows Nvidia and AMD holding up, so the leadership pullback looks more like a shakeout than a regime break, while regional banks show idiosyncratic weakness (Huntington -5.6%, Citizens -4.8%) consistent with credit stress rather than overreaction. | Further hawkish Fed repricing with 10-year yields above 5% compresses high-beta semiconductor and growth multiples; Brent reversal from $105 removes the geopolitical bid for defense and energy; Regional-bank credit stress (Huntington, Citizens declines) broadens into a risk-off move that hits all cyclicals; Semiconductor drawdown of -24.6% continues if AI capex sentiment deteriorates before the October 19 exit |
| openai-gpt-6-astra | openai | portfolio | SEMICONDUCTORS | 3 | 0.5667 | The rate increase and higher inflation projections justify some repricing, but resilient demand and strong capital investment argue against treating every cyclical pullback as fundamental deterioration. Cross-sectional return spreads are large, although the aggregate dispersion statistic is missing. Favor selective reversals rather than broad dip-buying or extrapolation of oil and crypto strength; confidence over the one-month window is modest. | Inflation or spending releases before October 19 could reinforce further tightening and overwhelm the reversal theses.; Semiconductor volatility and high beta could produce a much larger drawdown than the broad benchmark.; Higher financing costs could turn industrial and small-company pullbacks into persistent earnings pressure.; No company-specific earnings or valuation evidence is supplied, and moves before the September 17 entry close could absorb part of the anticipated rebound. |
| xai-grok-4-6 | xai | portfolio | SMALL_VALUE | 3 | 0.5633 | Hawkish unanimous 25bp hike with higher 2026 inflation and funds-rate medians, weak 5-session breadth (14.5% positive), and a modest SPY pullback create mixed one-month dynamics: quality pullbacks may mean-revert while high-beta growth, crypto, and solar remain rate- and vol-sensitive. | Further upside surprises in inflation or a higher path for the funds rate after the 3.7% 2026 PCE median.; Continuation of weak breadth (14.49% 5-session positive share) that keeps quality pullbacks from reversing.; High-vol names (semis, oil, ETH) gap on scheduled data (claims, IP, retail sales) inside the scoring window.; Regional-bank idiosyncratic news after Huntington and Citizens declines could spill into small-value. |
| xai-grok-4-5 | xai | portfolio | SMALL_VALUE | 3 | 0.5733 | Post-hike environment with elevated inflation projections, solid activity, and recent broad equity softness creates mixed continuation/reversal setup; high cross-asset dispersion favors selective quality pullbacks over pure momentum or deep losers with fundamental stress. | Further Fed hawkishness or higher terminal rate path if inflation stays sticky near 3.7% PCE; Growth scare from elevated rates pressuring small-caps and regionals via credit; Oil volatility spillover if crude reverses from recent strength; Tech/semiconductor beta amplification on any risk-off move |
| google-gemini-3-1-pro | google | portfolio | SMALL_VALUE | 3 | 0.58 | The FOMC raised rates by 25 bps to 3.75%-4.00% and noted resilient domestic spending and elevated inflation. The market is digesting this hawkish move alongside solid retail sales data, leading to a mixed environment where defensive and quality assets may outperform while highly rate-sensitive sectors face headwinds. | Higher interest rates could disproportionately impact small-cap companies and regional banks if financing costs rise significantly.; A broader market downturn driven by inflation concerns could overwhelm the reversal potential of the selected quality pullback candidates. |
| anthropic-claude-opus-5 | anthropic | portfolio | SMALL_VALUE | 3 | 0.5633 | Fed hiked 25bp to 3.75-4.00% with elevated inflation (3.7% PCE median) and a higher projected year-end path; 10y at 5.01% and 30y at 5.35% pressure duration and rate-sensitive equity. Growth data are solid (retail sales +1.2% m/m), so this is a rate/inflation repricing rather than a growth scare: positive_asset_share is low (14% over 5 sessions, 22% over 21), breadth is weak, and SPY is only 3% from highs. That argues for selective mean-reversion in high-quality domestic cyclicals that pulled back on rate fears rather than broad risk-taking in long-duration growth or crypto. | Further upward rate repricing if inflation data surprise, extending pressure on small caps and banks; Bank-specific credit or deposit news (HBAN/CFG weakness) proving fundamental rather than sentiment-driven; Mega-cap leadership resuming so cap-weighted SPY outruns breadth-sensitive baskets; Dollar strength and falling oil signaling global demand slowdown that hits domestic cyclicals |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 18.47 | 54.11000061035156 | 1.9296156258988395 | 1 |
| BRAZIL | Brazil Equities | 37.74 | 41.93000030517578 | 0.11102279557964434 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 43.3 | 46.29999923706055 | 0.06928404704527824 | 3 |
| ENERGY | Energy Sector | 64.48 | 67.8 | 0.051488833746898166 | 4 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.49 | 87.21 | 0.04455623427955446 | 5 |
| HEALTHCARE | Healthcare Sector | 168.81 | 175.65 | 0.04051892660387413 | 6 |
| OIL | Crude Oil | 155.31 | 160.80999755859375 | 0.03541302915841693 | 7 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 111.39 | 114.46 | 0.027560822335936708 | 8 |
| US_DOLLAR | US Dollar | 28.38 | 29.0 | 0.021846370683580085 | 9 |
| BROAD_COMMODITIES | Broad Commodities | 19.71 | 20.07 | 0.0182648401826484 | 10 |
| MEXICO | Mexico Equities | 74.29 | 75.36000061035156 | 0.014403023426457828 | 11 |
| DIVIDEND | US Dividend Equities | 33.89 | 34.24 | 0.010327530244909955 | 12 |
| LARGE_VALUE | US Large-Cap Value | 252.82 | 255.43 | 0.010323550352029143 | 13 |
| LOW_VOL | US Low Volatility Equities | 73.06 | 73.57 | 0.006980563920065519 | 14 |
| SP500 | S&P 500 | 762.6 | 766.48 | 0.005087857330186241 | 15 |
| MATERIALS | Materials Sector | 50.71 | 50.95 | 0.0047327943206467715 | 16 |
| NASDAQ100 | Nasdaq 100 | 716.92 | 718.36 | 0.0020085923115551463 | 17 |
| SOFTWARE | Software | 105.78 | 105.99 | 0.001985252410663607 | 18 |
| LARGE_GROWTH | US Large-Cap Growth | 122.53 | 122.61 | 0.0006529013302865039 | 19 |
| TOTAL_US_MARKET | Total US Stock Market | 375.34 | 375.54 | 0.0005328502158044035 | 20 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.53 | 91.57 | 0.0004370151862775895 | 21 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.31 | 213.4 | 0.0004219211476255147 | 22 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 23 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.11 | 47.029998779296875 | -0.0016981791700939608 | 24 |
| CANADA | Canada Equities | 60.41 | 60.28 | -0.002151961595762253 | 25 |
| COPPER | Copper | 39.66 | 39.56999969482422 | -0.002269296650927344 | 26 |
| TIPS | Treasury Inflation-Protected Securities | 105.71 | 105.26 | -0.004256929334972903 | 27 |
| AGRICULTURE | Agriculture Commodities | 28.42 | 28.200000762939453 | -0.007741000600300807 | 28 |
| UTILITIES | Utilities Sector | 41.69 | 41.36 | -0.0079155672823219 | 29 |
| MUNICIPAL_BONDS | Municipal Bonds | 103.16 | 102.33999633789062 | -0.007948852870389378 | 30 |
| AUSTRALIA | Australia Equities | 29.13 | 28.829999923706055 | -0.010298663793132268 | 31 |
| TECHNOLOGY | Technology Sector | 188.06 | 185.96 | -0.011166648941827062 | 32 |
| MID_CAP | US Mid-Cap Stocks | 73.21 | 72.38 | -0.011337249009698125 | 33 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.33 | 95.11 | -0.012664798089899287 | 34 |
| INDIA | India Equities | 48.01 | 47.4 | -0.012705686315350961 | 35 |
| UNITED_KINGDOM | United Kingdom Equities | 47.95 | 47.34 | -0.012721584984358714 | 36 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 91.25 | 90.08 | -0.012821917808219174 | 37 |
| INDUSTRIALS | Industrials Sector | 169.01 | 166.68 | -0.013786166499023644 | 38 |
| FINANCIALS | Financials Sector | 55.88 | 55.06 | -0.014674302075876833 | 39 |
| YEN | Japanese Yen | 58.76 | 57.790000915527344 | -0.016507812873938987 | 40 |
| CYBERSECURITY | Cybersecurity | 101.66 | 99.92 | -0.017115876450914724 | 41 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.81 | 90.22000122070312 | -0.017318361608723243 | 42 |
| COMMUNICATIONS | Communication Services Sector | 112.35 | 110.09 | -0.02011570983533595 | 43 |
| SEMICONDUCTORS | Semiconductors | 560.61 | 548.46 | -0.021672820677476334 | 44 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.16 | 102.88 | -0.021681247622670208 | 45 |
| BROAD_AI_TECH | Broad AI Technology | 64.37 | 62.96 | -0.021904613950598173 | 46 |
| EURO | Euro | 105.91 | 103.4800033569336 | -0.022943977368203194 | 47 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.72 | 76.83 | -0.02400914634146345 | 48 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.66 | 91.08999633789062 | -0.027439714521774183 | 49 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.78 | 79.46 | -0.028368794326241176 | 50 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 213.88 | 207.755 | -0.028637553768468327 | 51 |
| REAL_ESTATE | Real Estate Sector | 42.94 | 41.67 | -0.02957615277130876 | 52 |
| JAPAN | Japan Equities | 97.91 | 94.99 | -0.02982330711878256 | 53 |
| TAIWAN | Taiwan Equities | 110.64 | 107.26000213623047 | -0.030549510699290794 | 54 |
| EMERGING_MARKETS | Emerging Markets | 59.91 | 58.03 | -0.03138040393924213 | 55 |
| EUROPE | Europe Equities | 89.37 | 86.43 | -0.03289694528365217 | 56 |
| MOMENTUM | US Momentum Equities | 306.12 | 295.71 | -0.03400627205017648 | 57 |
| CHINA | China Equities | 52.67 | 50.87 | -0.03417505221188544 | 58 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.15 | 69.36 | -0.03866943866943873 | 59 |
| SMALL_VALUE | US Small-Cap Value | 216.73 | 207.85 | -0.04097263876712964 | 60 |
| GOLD | Gold | 81.69 | 77.85 | -0.04700697759823724 | 61 |
| REGIONAL_BANKS | Regional Banks | 72.74 | 69.26 | -0.04784162771514966 | 62 |
| SMALL_CAP | US Small-Cap Stocks | 285.43 | 271.28 | -0.049574326454822626 | 63 |
| SOUTH_AFRICA | South Africa Equities | 68.69 | 64.61000061035156 | -0.05939728329667249 | 64 |
| BIOTECH | Biotechnology | 158.25 | 147.86 | -0.06565560821484984 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.52 | 113.51 | -0.07353901403852425 | 66 |
| METALS_MINING | Metals and Mining | 111.32 | 101.37 | -0.08938196191160608 | 67 |
| SOLAR | Solar Energy | 46.36 | 41.31 | -0.10893011216565995 | 68 |
| SILVER | Silver | 58.97 | 51.540000915527344 | -0.12599625376416235 | 69 |
| SOUTH_KOREA | South Korea Equities | 182.39 | 156.5800018310547 | -0.14150994116423765 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 35.0 | -0.021672820677476334 | -0.007585487237116716 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | AEROSPACE_DEFENSE | 35.0 | -0.028637553768468327 | -0.010023143818963914 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 30.0 | 0.005087857330186241 | 0.0015263571990558722 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | SMALL_VALUE | 35.0 | -0.04097263876712964 | -0.014340423568495374 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 35.0 | -0.04784162771514966 | -0.01674456970030238 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SMALL_CAP | 30.0 | -0.049574326454822626 | -0.014872297936446788 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_VALUE | 35.0 | -0.04097263876712964 | -0.014340423568495374 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 35.0 | -0.04784162771514966 | -0.01674456970030238 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_CAP | 30.0 | -0.049574326454822626 | -0.014872297936446788 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | SEMICONDUCTORS | 35.0 | -0.021672820677476334 | -0.007585487237116716 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-6-astra | INDUSTRIALS | 35.0 | -0.013786166499023644 | -0.004825158274658275 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | SMALL_VALUE | 30.0 | -0.04097263876712964 | -0.012291791630138892 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_VALUE | 35.0 | -0.04097263876712964 | -0.014340423568495374 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 65.0 | 0.005087857330186241 | 0.0033071072646210565 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | SMALL_VALUE | 35.0 | -0.04097263876712964 | -0.014340423568495374 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| xai-grok-4-5 | REGIONAL_BANKS | 35.0 | -0.04784162771514966 | -0.01674456970030238 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-5 | INDUSTRIALS | 30.0 | -0.013786166499023644 | -0.004135849949707093 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SMALL_VALUE | 35.0 | -0.04097263876712964 | -0.014340423568495374 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | INDUSTRIALS | 35.0 | -0.013786166499023644 | -0.004825158274658275 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 30.0 | -0.028637553768468327 | -0.008591266130540497 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 2 | 0.55 | 0.005087857330186241 | -0.011033316303874318 | -0.016121173634060557 | 1.9406489422027138 |  | False | False |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 3 | 0.555 | -0.021672820677476334 | -0.016082273857024758 | -0.021170131187211 | 1.9456978997558643 |  | False | False |
| openai-gpt-6-astra | SEMICONDUCTORS | 3 | 0.5667 | -0.021672820677476334 | -0.024702437141913884 | -0.029790294472100125 | 1.9543180630407533 |  | False | False |
| xai-grok-4-6 | SMALL_VALUE | 3 | 0.5633 | -0.04097263876712964 | -0.027756847973694147 | -0.03284470530388039 | 1.9573724738725335 |  | False | False |
| xai-grok-4-5 | SMALL_VALUE | 3 | 0.5733 | -0.04097263876712964 | -0.03522084321850485 | -0.04030870054869109 | 1.9648364691173443 |  | False | False |
| google-gemini-3-1-pro | SMALL_VALUE | 3 | 0.58 | -0.04097263876712964 | -0.04595729120524454 | -0.05104514853543078 | 1.9755729171040841 |  | False | False |
| anthropic-claude-opus-5 | SMALL_VALUE | 3 | 0.5633 | -0.04097263876712964 | -0.04595729120524454 | -0.05104514853543078 | 1.9755729171040841 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 36bf2018cbdfa3960935b9d1d4b1831c4a248e534d9be22d4f667c8317fb4146 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | f16a9fae0fb55843a94de48718368e01a8367206796295e747a05d4a2f6223b2 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 11b6848bc3a7d0a749ecfa97222067d24726d841d3f06f359d75d33f935e3dc2 |
| market_data/universe_decision_context.md | c0f2e86b4b2819fa7acb633cf37e01488c22385313319329682fb2827047ed0b |
| market_data/universe_decision_context.json | 961c3c249499d04d8fae9a1d927b1a649d7085a85e1351b352718b1aef92638d |
| market_data/decision_context_source_history.json | bdd53bafc107c67172e356f47aa37dc97bd169ec471e8c204ff3b9f057b3179b |
| market_data/universe_quality_evidence.md | 654235c9389afe97b5624b0e5fb823ee2438addc4532cbefc776f1da2f41797e |
| market_data/universe_quality_evidence.json | cbdea657eb5d4bee37620d89cad19da7037f210e37b4ba1cfca5e2953e6dd22d |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a931712ea50a3787e2eae635b8d8a931b62d8e530c30d488de4e3dd98c985829 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 0c9f9d92f5a0710fd057177ab09ab78a27c26aedc5ee829046700f139617a9e7 | yes |
| Final briefing | research/final_briefing.md | model-facing | 36bf2018cbdfa3960935b9d1d4b1831c4a248e534d9be22d4f667c8317fb4146 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
