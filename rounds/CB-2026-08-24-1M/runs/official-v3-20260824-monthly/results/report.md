# CapitalBench Report: CB-2026-08-24-1M / official-v3-20260824-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260824-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-24-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-24
- Decision deadline: 2026-08-25T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-25
- Exit date: 2026-09-25
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.5667 | SPY fell 1.19% in the recent window while equal-weight outperformed (+1.71% 5s vs SPY), suggesting rotation out of concentrated tech rather than broad risk-off. Prior-window leaders (semis, cyber, oil) pulled back sharply, offering pullback-in-trend setups ahead of Jackson Hole and a major semiconductor earnings catalyst on Aug 26. | Weak semiconductor earnings on Aug 26 could extend the tech drawdown; Hawkish Jackson Hole or Sep FOMC guidance pressures high-beta growth positions; Rising petroleum inventories could reverse the oil trend further; September CPI/PPI surprises may drive sharp factor rotation against momentum names |
| xai-grok-4-3 | xai | portfolio | OIL | 3 | 0.5833 | Mixed reversal signals in defensives and commodities amid stable macro data and moderate dispersion; recent pullbacks in high-quality names show limited fundamental deterioration. | Macro data revisions post-cutoff; Volatility spikes in commodities; Rate path uncertainty at Jackson Hole; Crypto drawdown amplification |
| anthropic-claude-opus-5 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.565 | Index-level weakness is concentrated in mega-cap tech/semis while breadth is positive (RSP beat SPY by 1.7% over 5 sessions and a majority of S&P constituents rose on a down day). Macro is stagflationary-lite: 3.4% headline CPI, 4.7% PPI, payrolls -23k, GDP 1.5%, with a hawkish 9-3 FOMC hold. Jackson Hole, the Sept 4 jobs report, Sept CPI and the Sept 15-16 FOMC dominate the window. That argues against duration and against high-beta AI/crypto extensions, and modestly favors broad/quality equity with a deep-pullback semis reversal test. | Aug 26 semiconductor earnings disappointment extends the SMH drawdown given 53.7% volatility and 2.37 beta; A hawkish Jackson Hole address or hot Sept 11 CPI lifts real yields and hits small caps and high-beta tech together; Sept 4 payrolls after a -23k July print could confirm labor deterioration, compressing small-cap and cyclical valuations; Mega-cap-led index rebound would let SPY outperform both selected pullback candidates; Sept 15-16 FOMC with three members favoring a hike could trigger a broad risk-off repricing |
| openai-gpt-5-6-sol | openai | portfolio | SMALL_VALUE | 3 | 0.5767 | Broadening beneath a weak cap-weighted index favors selective pullback reversals, but high-volatility leadership and major macro events make continuation unreliable. Weak labor data supports rate-sensitive rebounds, while hawkish FOMC dissent and elevated inflation limit conviction. | The August employment report or inflation releases could materially shift rate expectations.; The September FOMC and projections could reinforce hawkish policy after three members favored a rate increase.; Semiconductor earnings could validate the recent selloff rather than reverse it.; Weak labor, retail sales, and housing data could worsen small-company and bank credit expectations. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.6233 | The market is experiencing a mixed environment with recent pullbacks in tech and small caps, while defensive and value sectors show some resilience. The Fed holding rates steady and mixed economic data suggest a cautious near-term outlook. | Continued weakness in the technology sector could negatively impact Semiconductors.; A broader market downturn or economic slowdown could disproportionately affect Small Caps. |
| xai-grok-4-5 | xai | portfolio | SEMICONDUCTORS | 3 | 0.57 | Soft labor print, sticky-but-cooling inflation, and Jackson Hole create two-way rate risk; equal-weight and value held up while mega-tech/semis sold off and crypto ripped, so one-month edge is selective mean-reversion in quality pullbacks rather than broad continuation. | Hawkish Jackson Hole or Sep FOMC path could extend growth/tech drawdowns; Semiconductor earnings miss on Aug 26 could invalidate SMH reversal; Oil inventory builds and Brent weakness could spill into risk assets; Crypto volatility spillover if bitcoin/ethereum mean-revert sharply |
| xai-grok-4-6 | xai | portfolio | UTILITIES | 3 | 0.5633 | SPY slipped 1.19% while equal-weight breadth was positive, rates eased slightly, and a hawkish FOMC dissent plus Jackson Hole and September FOMC sit inside the window. Cross-section is split between crypto short-horizon spikes and rate/tech shock pullbacks, so one-month outcomes are mixed rather than a clean trend or clean mean-reversion tape. | A hawkish Jackson Hole or September FOMC surprise could extend the utilities and aerospace drawdowns instead of reversing them.; Semiconductor earnings on August 26 can widen SMH's already 50%+ horizon volatility against SPY.; Soft July payrolls, retail sales, and housing starts can keep small-cap and cyclical mean-reversion from arriving inside one month.; Crypto 20-30% short-window spikes raise the chance that risk appetite rotates abruptly and lifts SPY relative to defensive reversals. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 126.15 | 148.33 | 0.17582243361078076 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 18.6 | 20.31 | 0.09193548387096762 | 2 |
| CYBERSECURITY | Cybersecurity | 92.46 | 100.95 | 0.0918234912394551 | 3 |
| SEMICONDUCTORS | Semiconductors | 555.82 | 606.56 | 0.09128854665179365 | 4 |
| TAIWAN | Taiwan Equities | 105.4 | 114.78 | 0.08899430740037939 | 5 |
| TECHNOLOGY | Technology Sector | 181.74 | 196.27 | 0.07994937823264014 | 6 |
| BROAD_COMMODITIES | Broad Commodities | 18.17 | 19.5 | 0.07319757842597685 | 7 |
| BITCOIN_ETF | Bitcoin ETF | 44.72 | 47.57 | 0.06372987477638636 | 8 |
| MOMENTUM | US Momentum Equities | 302.4 | 318.5 | 0.05324074074074092 | 9 |
| NASDAQ100 | Nasdaq 100 | 710.72 | 744.5 | 0.047529266096352885 | 10 |
| BROAD_AI_TECH | Broad AI Technology | 63.08 | 65.97 | 0.04581483830057076 | 11 |
| SOFTWARE | Software | 101.85 | 106.01 | 0.04084437898870896 | 12 |
| SOUTH_KOREA | South Korea Equities | 180.15 | 187.18 | 0.03902303635859017 | 13 |
| LARGE_GROWTH | US Large-Cap Growth | 121.83 | 126.25 | 0.03628006238200765 | 14 |
| BRAZIL | Brazil Equities | 35.88 | 36.82 | 0.02619843924191745 | 15 |
| US_DOLLAR | US Dollar | 27.94 | 28.62 | 0.024337866857551793 | 16 |
| JAPAN | Japan Equities | 95.63 | 97.93 | 0.024051030011502883 | 17 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.74 | 124.42 | 0.013687469447612788 | 18 |
| YEN | Japanese Yen | 57.63 | 58.3 | 0.01162588929377062 | 19 |
| AGRICULTURE | Agriculture Commodities | 28.28 | 28.54 | 0.009193776520509234 | 20 |
| SP500 | S&P 500 | 765.91 | 771.35 | 0.00710266219268596 | 21 |
| TOTAL_US_MARKET | Total US Stock Market | 378.15 | 379.77 | 0.004284014280047543 | 22 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 23 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.62 | 91.62 | 0.0 | 23 |
| ENERGY | Energy Sector | 62.06 | 62.04 | -0.00032226877215602023 | 25 |
| COMMUNICATIONS | Communication Services Sector | 113.18 | 112.96 | -0.0019438063262061656 | 26 |
| COPPER | Copper | 40.76 | 40.61 | -0.003680078508341511 | 27 |
| EMERGING_MARKETS | Emerging Markets | 60.64 | 60.16 | -0.007915567282322011 | 28 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.91 | 46.94 | -0.02024629513671461 | 29 |
| LARGE_VALUE | US Large-Cap Value | 258.27 | 251.93 | -0.024547953691872793 | 30 |
| EURO | Euro | 107.8 | 105.15 | -0.024582560296845912 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.92 | 77.86 | -0.025775775775775833 | 32 |
| HEALTHCARE | Healthcare Sector | 175.29 | 170.7 | -0.02618517884648297 | 33 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.79 | 71.84 | -0.026426345033202403 | 34 |
| TIPS | Treasury Inflation-Protected Securities | 107.64 | 104.54 | -0.028799702712746122 | 35 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.01 | 95.12 | -0.029486787062544595 | 36 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.38 | 92.18 | -0.03355001048437811 | 37 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.86 | 103.21 | -0.03415684072618386 | 38 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.77 | 90.34 | -0.03657886317585579 | 39 |
| REGIONAL_BANKS | Regional Banks | 74.33 | 71.55 | -0.037400780304049475 | 40 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.51 | 90.0 | -0.037536092396535214 | 41 |
| MID_CAP | US Mid-Cap Stocks | 76.14 | 72.99 | -0.0413711583924351 | 42 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.58 | 101.17 | -0.04176927448380374 | 43 |
| UNITED_KINGDOM | United Kingdom Equities | 49.39 | 47.32 | -0.041911318080583126 | 44 |
| INDUSTRIALS | Industrials Sector | 178.4 | 170.43 | -0.044674887892376725 | 45 |
| CHINA | China Equities | 55.12 | 52.62 | -0.045355587808417974 | 46 |
| INDIA | India Equities | 50.23 | 47.86 | -0.04718295839139952 | 47 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 221.77 | 211.11 | -0.048067818009649654 | 48 |
| CANADA | Canada Equities | 62.64 | 59.59 | -0.048690932311621915 | 49 |
| EUROPE | Europe Equities | 93.19 | 88.63 | -0.04893228887219658 | 50 |
| SMALL_VALUE | US Small-Cap Value | 224.64 | 213.49 | -0.049634971509971426 | 51 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.47 | 79.32 | -0.04971846172277472 | 52 |
| CONSUMER_STAPLES | Consumer Staples Sector | 86.52 | 82.06 | -0.05154877484974563 | 53 |
| DIVIDEND | US Dividend Equities | 35.11 | 33.21 | -0.05411563657077756 | 54 |
| LOW_VOL | US Low Volatility Equities | 75.64 | 71.3 | -0.05737704918032793 | 55 |
| SMALL_CAP | US Small-Cap Stocks | 299.23 | 281.97 | -0.05768138221435015 | 56 |
| MEXICO | Mexico Equities | 77.85 | 73.34 | -0.05793192035966588 | 57 |
| FINANCIALS | Financials Sector | 58.31 | 54.84 | -0.05950951809295146 | 58 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.95 | 110.56 | -0.06265366680796947 | 59 |
| AUSTRALIA | Australia Equities | 30.43 | 28.43 | -0.06572461386789352 | 60 |
| SILVER | Silver | 62.32 | 58.14 | -0.06707317073170727 | 61 |
| MATERIALS | Materials Sector | 53.58 | 49.8 | -0.07054871220604708 | 62 |
| GOLD | Gold | 87.76 | 80.66 | -0.0809024612579764 | 63 |
| SOUTH_AFRICA | South Africa Equities | 72.51 | 66.48 | -0.08316094331816304 | 64 |
| BIOTECH | Biotechnology | 169.1 | 155.03 | -0.08320520402128917 | 65 |
| REAL_ESTATE | Real Estate Sector | 45.36 | 41.56 | -0.08377425044091702 | 66 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 234.3 | 213.81 | -0.0874519846350833 | 67 |
| UTILITIES | Utilities Sector | 43.31 | 39.51 | -0.08773955206649742 | 68 |
| SOLAR | Solar Energy | 48.85 | 44.06 | -0.09805527123848512 | 69 |
| METALS_MINING | Metals and Mining | 120.94 | 108.33 | -0.10426657846866216 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 35.0 | 0.09128854665179365 | 0.03195099132812777 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | CYBERSECURITY | 35.0 | 0.0918234912394551 | 0.03213822193380928 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | OIL | 30.0 | 0.17582243361078076 | 0.052746730083234224 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 35.0 | 0.09128854665179365 | 0.03195099132812777 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SMALL_VALUE | 35.0 | -0.049634971509971426 | -0.01737224002849 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 30.0 | 0.00710266219268596 | 0.002130798657805788 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 35.0 | 0.09128854665179365 | 0.03195099132812777 | V3 selected model rank 1: overreaction with 65% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_VALUE | 35.0 | -0.049634971509971426 | -0.01737224002849 | V3 selected model rank 2: overreaction with 62% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_CAP | 30.0 | -0.05768138221435015 | -0.017304414664305046 | V3 selected model rank 3: overreaction with 60% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SMALL_VALUE | 35.0 | -0.049634971509971426 | -0.01737224002849 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 35.0 | 0.09128854665179365 | 0.03195099132812777 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 30.0 | -0.037400780304049475 | -0.011220234091214842 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | OIL | 35.0 | 0.17582243361078076 | 0.061537851763773264 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | US_DOLLAR | 35.0 | 0.024337866857551793 | 0.008518253400143127 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_VALUE | 30.0 | -0.049634971509971426 | -0.014890491452991428 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | SEMICONDUCTORS | 35.0 | 0.09128854665179365 | 0.03195099132812777 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | UTILITIES | 35.0 | -0.08773955206649742 | -0.030708843223274093 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 30.0 | -0.0874519846350833 | -0.02623559539052499 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | UTILITIES | 35.0 | -0.08773955206649742 | -0.030708843223274093 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 35.0 | -0.0874519846350833 | -0.030608194622279154 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SEMICONDUCTORS | 30.0 | 0.09128854665179365 | 0.027386563995538092 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 3 | 0.5667 | 0.09128854665179365 | 0.11683594334517128 | 0.10973328115248532 | 0.05898649026560948 |  | True | True |
| xai-grok-4-3 | OIL | 3 | 0.5833 | 0.17582243361078076 | 0.05516561371092496 | 0.048062951518239 | 0.1206568198998558 |  | True | True |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 3 | 0.565 | 0.09128854665179365 | 0.016709549957443563 | 0.009606887764757602 | 0.1591128836533372 |  | True | True |
| openai-gpt-5-6-sol | SMALL_VALUE | 3 | 0.5767 | -0.049634971509971426 | 0.003358517208422932 | -0.0037441449842630283 | 0.17246391640235784 |  | False | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.6233 | 0.09128854665179365 | -0.0027256633646672718 | -0.009828325557353232 | 0.17854809697544805 |  | False | False |
| xai-grok-4-5 | SEMICONDUCTORS | 3 | 0.57 | 0.09128854665179365 | -0.02499344728567131 | -0.03209610947835727 | 0.20081588089645208 |  | False | False |
| xai-grok-4-6 | UTILITIES | 3 | 0.5633 | -0.08773955206649742 | -0.03393047385001515 | -0.04103313604270111 | 0.20975290746079592 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | b84edd792fddb7ed4a904c8d7f2528e94221960015a8eccaa37a3ddc43484bf3 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | a8271d603c8fb1f199b91c049ce80cf62edc40ed4681af1b0612be487e01a03d |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 73f99140c177fce4ff493b844db9572e97066cb7458335affb5705ee41c11d1e |
| market_data/universe_decision_context.md | 627353216d1f09c83f17a41e814bde010de9329a457b28d6bb509ad42b2f1d6e |
| market_data/universe_decision_context.json | 888047d90906faacd129f555e168569e1fc5f97ec7d806ff48a571492efc9b37 |
| market_data/decision_context_source_history.json | 7af31bd44ad83cccf728e530adb1bb2ba7fcfa03548ae0d8e391e109e476bcbd |
| market_data/universe_quality_evidence.md | 18d398a254a843c4208f93373fcc892abacf31ff917cbf22746b32c978e4f77f |
| market_data/universe_quality_evidence.json | e15f92f4e9f10cc01175a7a928e6f18e72a7f65c601792c60d7180f7695b02a0 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 1c8c0c90dbea6a54704bdba4c593845e7bc67061d47003f270d769e86346e398 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 0db7e8a41b57f8b4727ca5ba0df8d4036dea0f8af445694095185eda4cd98b21 | yes |
| Final briefing | research/final_briefing.md | model-facing | b84edd792fddb7ed4a904c8d7f2528e94221960015a8eccaa37a3ddc43484bf3 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
