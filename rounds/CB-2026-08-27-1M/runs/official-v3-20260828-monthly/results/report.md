# CapitalBench Report: CB-2026-08-27-1M / official-v3-20260828-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260828-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-27-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-27
- Decision deadline: 2026-08-28T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-28
- Exit date: 2026-09-28
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | SP500 | 1 | 0.5 | Tech/AI strength from NVIDIA results supports growth continuation while rate-sensitive defensives and low-vol lag amid sticky inflation, soft labor, and elevated yields; mixed cross-section with limited clean one-month edges versus SPY. | Sticky PCE/CPI and elevated Treasury yields could pressure duration-sensitive and growth multiples before September FOMC; Soft July payrolls and retail sales raise recession-scare risk that hits high-beta tech/semis; High horizon volatility in semis, cyber, Korea, and crypto can reverse quickly on any AI or risk-off headline; September employment, CPI, and FOMC SEP releases inside the scoring window may drive sharp factor rotation |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is near a 52-week high with mega-cap/tech leadership while equal-weight and rate-sensitive defensives lag; inflation remains elevated, the Fed is on hold with hawkish dissent, and a dense September data/FOMC calendar argues against a clean one-month continuation or reversal regime. | September 16 FOMC and SEP could reprice duration and growth stocks if the Committee stays restrictive.; August CPI/PPI and September 4 payrolls can reverse both mega-cap continuation and rate-sensitive mean reversion.; High-vol semiconductors, Korea, oil, and crypto can gap versus SPY on inventory, China PMI, or risk-off flows. |
| anthropic-claude-opus-5 | anthropic | portfolio | REGIONAL_BANKS | 3 | 0.575 | Narrow mega-cap/AI led tape: SPY +5.71% over 21 sessions while equal-weight lagged by 3.06pp, defensives (XLU, XLP, SPLV, XLRE) deeply negative on an active basis, and rates drifting higher with sticky 3.3-3.7% core PCE. Fed on hold with hawkish dissents; September FOMC, August payrolls and CPI all fall inside the window. Dispersion is high (crypto, metals, Korea +20% active vs defensives -9%). Best risk-adjusted setups are quality names with strong prior trend plus a fresh relative pullback (REGIONAL_BANKS, REAL_ESTATE), not chasing extended momentum. | Continued mega-cap/AI leadership keeps low-beta defensives and banks lagging SPY for another month; Hawkish September FOMC or hot August CPI pushes yields higher, hurting REAL_ESTATE and REGIONAL_BANKS; Credit or CRE deterioration turns the KRE pullback into fundamental repricing rather than overreaction; Weak August payrolls trigger a broad risk-off move where high-beta rebound in defensives is insufficient to offset index decline |
| openai-gpt-5-6-sol | openai | portfolio | LARGE_VALUE | 3 | 0.56 | Narrow mega-cap leadership, weak breadth, softer labor and consumption data, elevated inflation, and high Treasury yields favor selective reversal and diversification over broad continuation. Scheduled CPI, employment, and FOMC events create substantial one-month dispersion risk. | Sticky August inflation or a hawkish September FOMC could keep yields elevated and pressure real estate and regional banks.; Further labor-market or credit deterioration could turn the financial-sector pullback into fundamental weakness.; Mega-cap technology leadership could remain narrow and prevent value-oriented reversals from beating SPY.; High-impact employment, CPI, retail-sales, and housing releases could cause abrupt factor rotations before the exit close. |
| xai-grok-4-3 | xai | portfolio | REGIONAL_BANKS | 3 | 0.57 | Defensive sectors show deep recent pullbacks with high quality scores while select tech names exhibit continuation; one-month window offers limited broad catalysts beyond scheduled data releases. | Scheduled September employment and inflation releases; NVIDIA outlook assumptions on China revenue; Treasury yield volatility impacting defensives |
| anthropic-claude-fable-5 | anthropic | portfolio | REGIONAL_BANKS | 3 | 0.5633 | SPY up 5.7% over 21 sessions led by mega-cap tech (NVIDIA blowout quarter), but breadth is weak (RSP -3.1% active, majority of S&P decliners on 8/27). Defensives and rate-sensitives lagged sharply while yields drifted up. Weak payrolls (-23k) and a September FOMC with SEP raise odds of a dovish tilt that could lift lagging rate-sensitive quality pullbacks like regional banks and REITs. | FOMC holds or signals hawkish SEP on elevated PCE (3.7% y/y), hurting rate-sensitive reversal picks; AI/tech rally persists, extending laggard underperformance of banks, REITs, and low-vol; August CPI/PPI prints hot mid-September, pushing yields higher; Regional banks exposed to credit deterioration if labor weakness broadens |
| google-gemini-3-1-pro | google | portfolio | UTILITIES | 3 | 0.58 | The market is showing mixed signals with solid economic growth but elevated inflation, leading to a cautious stance from the Fed. Recent tech earnings (NVIDIA) were strong, but broader market participation is mixed. | Interest rates remain elevated, which could pressure rate-sensitive sectors like Utilities and Real Estate.; Inflation data could surprise to the upside, leading to a more hawkish Fed stance. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 129.7 | 150.00999450683594 | 0.15659209334491875 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 18.37 | 20.149999618530273 | 0.09689709409527891 | 2 |
| SEMICONDUCTORS | Semiconductors | 553.11 | 600.01 | 0.0847932599302128 | 3 |
| BITCOIN_ETF | Bitcoin ETF | 43.9 | 47.209999084472656 | 0.07539861240256629 | 4 |
| TAIWAN | Taiwan Equities | 107.9 | 114.16999816894531 | 0.05810934354907604 | 5 |
| BROAD_COMMODITIES | Broad Commodities | 18.39 | 19.37 | 0.05328983143012511 | 6 |
| MOMENTUM | US Momentum Equities | 299.71 | 315.59 | 0.05298455173334227 | 7 |
| TECHNOLOGY | Technology Sector | 185.69 | 194.53 | 0.04760622542947934 | 8 |
| CYBERSECURITY | Cybersecurity | 98.56 | 101.67 | 0.03155438311688319 | 9 |
| NASDAQ100 | Nasdaq 100 | 716.43 | 736.53 | 0.028055776558770562 | 10 |
| LARGE_GROWTH | US Large-Cap Growth | 122.75 | 125.2 | 0.019959266802443976 | 11 |
| SOUTH_KOREA | South Korea Equities | 180.2 | 183.5800018310547 | 0.018756946898194737 | 12 |
| BRAZIL | Brazil Equities | 35.55 | 36.209999084472656 | 0.01856537509065137 | 13 |
| US_DOLLAR | US Dollar | 28.18 | 28.700000762939453 | 0.0184528304804632 | 14 |
| YEN | Japanese Yen | 57.25 | 58.220001220703125 | 0.016943252763373273 | 15 |
| JAPAN | Japan Equities | 95.87 | 96.83 | 0.01001356002920617 | 16 |
| BROAD_AI_TECH | Broad AI Technology | 64.22 | 64.71 | 0.0076300218000622255 | 17 |
| HEALTHCARE | Healthcare Sector | 171.16 | 171.26 | 0.0005842486562279703 | 18 |
| COPPER | Copper | 39.67 | 39.68000030517578 | 0.00025208735003223737 | 19 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 20 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.65 | 91.63 | -0.00021822149481731667 | 21 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.32 | 121.87 | -0.003678875081752686 | 22 |
| SP500 | S&P 500 | 769.35 | 765.61 | -0.004861246506791428 | 23 |
| ENERGY | Energy Sector | 62.68 | 62.1 | -0.009253350350989176 | 24 |
| TOTAL_US_MARKET | Total US Stock Market | 379.36 | 375.84 | -0.009278785322648808 | 25 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.6 | 46.84000015258789 | -0.015966383348993918 | 26 |
| COMMUNICATIONS | Communication Services Sector | 112.99 | 111.18 | -0.01601911673599421 | 27 |
| EMERGING_MARKETS | Emerging Markets | 60.79 | 59.69 | -0.018095081427866422 | 28 |
| EURO | Euro | 106.978 | 104.90499877929688 | -0.019377827410337778 | 29 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.06 | 71.31 | -0.023952915411990183 | 30 |
| UNITED_KINGDOM | United Kingdom Equities | 48.55 | 47.27 | -0.026364572605561132 | 31 |
| TIPS | Treasury Inflation-Protected Securities | 106.94 | 104.09 | -0.026650458200860205 | 32 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.74 | 77.54 | -0.027589666415851366 | 33 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.49 | 94.65 | -0.029131192942865813 | 34 |
| LARGE_VALUE | US Large-Cap Value | 258.33 | 250.05 | -0.03205202647776095 | 35 |
| AGRICULTURE | Agriculture Commodities | 29.19 | 28.25 | -0.03220280918122653 | 36 |
| BIOTECH | Biotechnology | 162.38 | 156.61 | -0.03553393275033856 | 37 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.85 | 89.53 | -0.035756596661281614 | 38 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.35 | 102.47 | -0.036483309826046084 | 39 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.45 | 82.28 | -0.03709771796372152 | 40 |
| SOFTWARE | Software | 109.5 | 105.43 | -0.037168949771689386 | 41 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.89 | 91.33999633789062 | -0.03741177850257538 | 42 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.17 | 89.66000366210938 | -0.037673031425250914 | 43 |
| EUROPE | Europe Equities | 91.98 | 88.38 | -0.0391389432485324 | 44 |
| CANADA | Canada Equities | 61.73 | 59.07 | -0.04309087963712943 | 45 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.22 | 100.61000061035156 | -0.04381295751424097 | 46 |
| MID_CAP | US Mid-Cap Stocks | 75.76 | 72.44 | -0.043822597676874464 | 47 |
| INDUSTRIALS | Industrials Sector | 177.14 | 168.78 | -0.047194309585638416 | 48 |
| CHINA | China Equities | 55.23 | 52.54 | -0.04870541372442505 | 49 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.69 | 209.74 | -0.04961710997326563 | 50 |
| INDIA | India Equities | 49.56 | 47.09 | -0.04983857949959647 | 51 |
| AUSTRALIA | Australia Equities | 30.0 | 28.5 | -0.050000000000000044 | 52 |
| REGIONAL_BANKS | Regional Banks | 74.3 | 70.55 | -0.05047106325706596 | 53 |
| SMALL_VALUE | US Small-Cap Value | 223.14 | 211.8 | -0.05082011293358424 | 54 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.88 | 78.62 | -0.05139961389961378 | 55 |
| LOW_VOL | US Low Volatility Equities | 75.08 | 71.12 | -0.05274374001065518 | 56 |
| SMALL_CAP | US Small-Cap Stocks | 295.75 | 280.02 | -0.053186813186813287 | 57 |
| MEXICO | Mexico Equities | 76.48 | 72.37000274658203 | -0.05373950383653203 | 58 |
| DIVIDEND | US Dividend Equities | 34.9 | 33.01 | -0.054154727793696344 | 59 |
| FINANCIALS | Financials Sector | 58.1 | 54.19 | -0.0672977624784854 | 60 |
| MATERIALS | Materials Sector | 53.18 | 49.47 | -0.06976306882286576 | 61 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.21 | 109.0 | -0.07004521798481356 | 62 |
| REAL_ESTATE | Real Estate Sector | 44.48 | 41.35 | -0.07036870503597115 | 63 |
| GOLD | Gold | 83.82 | 77.5 | -0.07539966595084702 | 64 |
| UTILITIES | Utilities Sector | 42.73 | 39.25 | -0.08144161010999296 | 65 |
| SILVER | Silver | 60.02 | 54.95000076293945 | -0.08447183000767322 | 66 |
| SOUTH_AFRICA | South Africa Equities | 70.72 | 64.47000122070312 | -0.08837667957150552 | 67 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 232.82 | 209.26 | -0.10119405549351435 | 68 |
| METALS_MINING | Metals and Mining | 118.74 | 105.42 | -0.11217786760990389 | 69 |
| SOLAR | Solar Energy | 48.65 | 43.0 | -0.11613566289825283 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | REGIONAL_BANKS | 35.0 | -0.05047106325706596 | -0.017664872139973087 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | REAL_ESTATE | 35.0 | -0.07036870503597115 | -0.0246290467625899 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | LOW_VOL | 30.0 | -0.05274374001065518 | -0.015823122003196553 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 35.0 | -0.05047106325706596 | -0.017664872139973087 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | REAL_ESTATE | 35.0 | -0.07036870503597115 | -0.0246290467625899 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 30.0 | -0.004861246506791428 | -0.0014583739520374283 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | UTILITIES | 35.0 | -0.08144161010999296 | -0.02850456353849753 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | LOW_VOL | 35.0 | -0.05274374001065518 | -0.018460309003729313 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | REAL_ESTATE | 30.0 | -0.07036870503597115 | -0.021110611510791345 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | LARGE_VALUE | 35.0 | -0.03205202647776095 | -0.011218209267216332 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REAL_ESTATE | 35.0 | -0.07036870503597115 | -0.0246290467625899 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 30.0 | -0.05047106325706596 | -0.015141318977119789 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | REGIONAL_BANKS | 35.0 | -0.05047106325706596 | -0.017664872139973087 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | REAL_ESTATE | 35.0 | -0.07036870503597115 | -0.0246290467625899 | V3 selected model rank 4: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-3 | LOW_VOL | 30.0 | -0.05274374001065518 | -0.015823122003196553 | V3 selected model rank 5: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-5 | SP500 | 100.0 | -0.004861246506791428 | -0.004861246506791428 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-6 | SP500 | 100.0 | -0.004861246506791428 | -0.004861246506791428 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | SP500 | 1 | 0.5 | -0.004861246506791428 | -0.004861246506791428 | 0.0 | 0.16145333985171018 |  | False | False |
| xai-grok-4-6 | SP500 | 1 | 0.5 | -0.004861246506791428 | -0.004861246506791428 | 0.0 | 0.16145333985171018 |  | False | False |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 3 | 0.575 | -0.05047106325706596 | -0.04375229285460041 | -0.03889104634780898 | 0.20034438619951916 |  | False | False |
| openai-gpt-5-6-sol | LARGE_VALUE | 3 | 0.56 | -0.03205202647776095 | -0.050988575006926024 | -0.046127328500134596 | 0.20758066835184477 |  | False | False |
| xai-grok-4-3 | REGIONAL_BANKS | 3 | 0.57 | -0.05047106325706596 | -0.05811704090575953 | -0.053255794398968104 | 0.21470913425067828 |  | False | False |
| anthropic-claude-fable-5 | REGIONAL_BANKS | 3 | 0.5633 | -0.05047106325706596 | -0.05811704090575953 | -0.053255794398968104 | 0.21470913425067828 |  | False | False |
| google-gemini-3-1-pro | UTILITIES | 3 | 0.58 | -0.08144161010999296 | -0.06807548405301819 | -0.06321423754622676 | 0.22466757739793694 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 476f8cf287a725b98185b8ff865f5ecca9b16aca118b251bd5daef058bf361b4 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | a9450adf6338039241d21a6bc1023488448fa1d512b6a9e8aa0be12732bf2890 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 701f594d2409fdca38a7233bbef57b8db2e668e488ffdb8ef87767b2fded33eb |
| market_data/universe_decision_context.md | 72e3b15549e497d876b9e2373f7986315900cccc25611bb3c60cc8dcd90a5cc8 |
| market_data/universe_decision_context.json | 0c8a73f3fb93e7b63c86ff3803c1b41cd50046c55b241e6ec6916491d39f8574 |
| market_data/decision_context_source_history.json | 2e93c105ed6652055e9f1ebf9eee2a227cbad2ffe5ef23f8a3078bf059c7ef51 |
| market_data/universe_quality_evidence.md | d707870081d1825d0f8429262edff8def207ebb9f802ffab3bcc877602884716 |
| market_data/universe_quality_evidence.json | f9d87b6fa7d6f18f6bd23a1573bceee0d1f381c76560eafc2ede3d0983784cf8 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 29bd932c4f3f9db30c6c44a9705cd852072ba705b74f491d0dcd4f0d0bc4eade | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | bffa50a130b1039a87192290de9b44d17bc9de7079f86169cee9b67cf6dc7c4b | yes |
| Final briefing | research/final_briefing.md | model-facing | 476f8cf287a725b98185b8ff865f5ecca9b16aca118b251bd5daef058bf361b4 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
