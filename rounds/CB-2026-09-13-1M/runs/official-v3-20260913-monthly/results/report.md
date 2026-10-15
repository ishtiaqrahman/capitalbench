# CapitalBench Report: CB-2026-09-13-1M / official-v3-20260913-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260913-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-13-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-13
- Decision deadline: 2026-09-14T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-14
- Exit date: 2026-10-14
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SP500 | 2 | 0.57 | Stagflationary backdrop: August CPI 3.4% headline with re-accelerating core, Brent above $100 on unresolved Iran conflict, 10y at 4.96% and 30y at 5.35%, consumer sentiment collapsing to 47.8 with inflation expectations jumping to 4.6%. Breadth is poor (equal-weight lagging SPY by 1.75% over 21 sessions, only ~23% of assets positive). The FOMC on Sept 15-16 is a binary catalyst; high rates and oil favor cap-weighted mega-cap resilience over cyclicals and small caps. Dispersion is high (oil, crypto, Korea, Brazil far from the pack) but most equity sub-groups are in shallow drawdowns rather than shock lows, so genuine reversal setups are scarce. Cybersecurity is the one candidate combining a strong prior relative trend, modest pullback, low volume stress and low beta to an oil/rates shock. | FOMC on Sept 15-16 could signal a more hawkish path given 3.4% CPI and 4.6% inflation expectations, hitting growth and high-beta tech including cybersecurity; Brent above $100 with the Iran conflict unresolved could spike further, compressing margins and pushing yields higher across the window; Consumer sentiment at 47.8 and weak Russell 2000 breadth may herald a broader risk-off that pushes SPY lower and widens losses in anything with beta above 1; Cybersecurity's 31% volatility means a single sector earnings or guidance disappointment could erase the expected modest edge |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | Breadth is weak with only about one-fifth of assets positive over 5 and 21 sessions, SPY is modestly negative into an FOMC week, CPI is 3.4% with rising Michigan inflation expectations, and oil remains elevated. That mix favors mixed reversal-versus-continuation rather than a clean one-month trend. | Unknown FOMC September 15–16 outcome and SEP can reprice duration, growth, and high-beta tech in the scoring window.; CPI 3.4% and Michigan year-ahead inflation expectations at 4.6% can keep real-rate pressure on cyclicals and small caps.; Unresolved Iran-related oil supply conditions after Brent near $104–110 can shock industrials, defense, and risk appetite.; Weak 5-session positive-asset share near 20% raises gap-down and correlation-spike risk for high-beta slate names. |
| anthropic-claude-opus-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.565 | Broad market slightly weak into an FOMC meeting with sticky 3.4% headline CPI, 2.4% core, and deteriorating consumer sentiment (47.8). Oil spike from unresolved Iran conflict is boosting energy/commodities while pressuring cyclicals and small caps. Breadth is poor (positive asset share ~20-23%, RSP lagging SPY by 1.75% over 21 sessions), so mega-cap cap-weighted SPY is a hard benchmark. Best asymmetric setups are high-quality prior leaders that pulled back modestly (CYBERSECURITY) and quality small-cap pullbacks that could re-rate if the FOMC leans dovish. | Hawkish FOMC on September 15-16 with sticky 3.4% CPI would hurt small caps and high-beta growth; Continued narrow breadth (positive asset share ~20%) means cap-weighted SPY can outperform diversified pullback trades; Oil above $100 from unresolved Iran conflict could squeeze margins and consumer demand further; Consumer sentiment collapse to 47.8 with rising inflation expectations signals stagflationary demand risk; Cybersecurity's high 31% volatility can overwhelm a modest expected reversion edge in one month |
| openai-gpt-6-astra | openai | portfolio | CYBERSECURITY | 3 | 0.555 | Energy-supply stress, rising inflation expectations and weak household sentiment favor selective exposures rather than a broad rebound. Dispersion appears high from the option-level spreads, although the aggregate dispersion field is missing. Quality pullbacks offer limited reversal opportunities, but the supplied quality scores measure price behavior rather than business fundamentals. The September FOMC and subsequent economic releases can materially change relative returns before October 14. | A hawkish September FOMC or further inflation pressure could prolong growth-stock and financing-sensitive equity weakness.; Iran-related de-escalation could rapidly reverse energy leadership and weaken the defense sentiment thesis.; Cybersecurity and aerospace weakness may reflect information absent from the briefing rather than temporary overreaction.; Entry-close repricing may absorb part of the inferred edge, and scheduled data releases may overturn the macro assessment before October 14. |
| google-gemini-3-1-pro | google | portfolio | AEROSPACE_DEFENSE | 3 | 0.6 | The market is facing uncertainty ahead of the FOMC meeting, with mixed economic data and unresolved geopolitical tensions. | Unexpected hawkishness from the FOMC could negatively impact equities.; Escalation of geopolitical tensions could lead to increased market volatility. |
| xai-grok-4-3 | xai | portfolio | CYBERSECURITY | 3 | 0.5833 | Quality pullbacks amid elevated rates and upcoming FOMC create selective reversal potential; broad equity dispersion remains contained. | FOMC policy surprise; CPI revision impact on rates; Iran supply shock persistence |
| xai-grok-4-5 | xai | portfolio | CYBERSECURITY | 3 | 0.59 | Sticky CPI, weak sentiment, elevated yields, unresolved oil supply shock and imminent FOMC create cross-asset dispersion; recent breadth is poor with many quality names in pullback while mega-cap and energy/crypto show divergent paths, favoring selective reversal over pure continuation into the one-month window. | FOMC Sept 15-16 decision and SEP could reprice yields sharply against duration-sensitive and high-beta names; Unresolved Iran-related oil supply keeps energy volatility elevated and may pressure risk assets; Sticky CPI 3.4% and rising consumer inflation expectations risk further equity multiple compression; Narrow market breadth (~20% positive assets) can persist, delaying small-cap and industrial catch-up |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 19.170000076293945 | 54.88999938964844 | 1.8633280736147024 | 1 |
| BRAZIL | Brazil Equities | 37.720001220703125 | 42.599998474121094 | 0.12937426021978804 | 2 |
| ENERGY | Energy Sector | 64.52999877929688 | 67.63 | 0.04803969129622376 | 3 |
| SEMICONDUCTORS | Semiconductors | 541.5 | 564.74 | 0.04291782086795948 | 4 |
| HEALTHCARE | Healthcare Sector | 167.75 | 173.96 | 0.03701937406855449 | 5 |
| CYBERSECURITY | Cybersecurity | 100.05000305175781 | 103.74 | 0.03688152759309027 | 6 |
| COPPER | Copper | 38.2599983215332 | 39.65999984741211 | 0.03659178220849446 | 7 |
| TAIWAN | Taiwan Equities | 107.20999908447266 | 110.94000244140625 | 0.03479156224966151 | 8 |
| US_DOLLAR | US Dollar | 28.170000076293945 | 29.1200008392334 | 0.03372384665837869 | 9 |
| BITCOIN_ETF | Bitcoin ETF | 44.7400016784668 | 46.2400016784668 | 0.033527043891952824 | 10 |
| TECHNOLOGY | Technology Sector | 184.27999877929688 | 190.43 | 0.033373134694171025 | 11 |
| NASDAQ100 | Nasdaq 100 | 709.1799926757812 | 728.95 | 0.027877277318026472 | 12 |
| LARGE_GROWTH | US Large-Cap Growth | 121.26000213623047 | 124.27 | 0.02482267698121854 | 13 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.41999816894531 | 86.06 | 0.019426698254276564 | 14 |
| MOMENTUM | US Momentum Equities | 299.70001220703125 | 304.875 | 0.01726722583312368 | 15 |
| SP500 | S&P 500 | 760.8800048828125 | 769.6 | 0.011460407766308078 | 16 |
| SOFTWARE | Software | 106.63999938964844 | 107.65 | 0.009471123557129424 | 17 |
| BROAD_AI_TECH | Broad AI Technology | 63.470001220703125 | 63.94 | 0.007405053887781676 | 18 |
| TOTAL_US_MARKET | Total US Stock Market | 374.67999267578125 | 376.88 | 0.005871696827224104 | 19 |
| BROAD_COMMODITIES | Broad Commodities | 19.780000686645508 | 19.86 | 0.004044454528684849 | 20 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.93000030517578 | 47.04999923706055 | 0.0025569770105355882 | 21 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5 | 91.52 | 0.00021857923497270448 | 22 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 23 |
| UTILITIES | Utilities Sector | 41.81999969482422 | 41.72 | -0.0023911931026769917 | 24 |
| LARGE_VALUE | US Large-Cap Value | 255.3699951171875 | 254.2 | -0.004581568467550867 | 25 |
| LOW_VOL | US Low Volatility Equities | 73.81999969482422 | 73.29 | -0.0071796220132113175 | 26 |
| TIPS | Treasury Inflation-Protected Securities | 105.81999969482422 | 104.82 | -0.009450006593348492 | 27 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.88999938964844 | 94.82 | -0.011158612957129277 | 28 |
| EMERGING_MARKETS | Emerging Markets | 59.61000061035156 | 58.9 | -0.011910763346448805 | 29 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.8499984741211 | 111.5 | -0.01196276909503613 | 30 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.22000122070312 | 90.0 | -0.013374273233689005 | 31 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 90.93000030517578 | 89.71 | -0.013416917420887131 | 32 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.00999450683594 | 212.09 | -0.013580738483964239 | 33 |
| MUNICIPAL_BONDS | Municipal Bonds | 103.11000061035156 | 101.6500015258789 | -0.014159626377948875 | 34 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 104.30000305175781 | 102.66 | -0.0157239022413449 | 35 |
| MATERIALS | Materials Sector | 50.4900016784668 | 49.67 | -0.016240872473896384 | 36 |
| INDUSTRIALS | Industrials Sector | 169.92999267578125 | 167.04 | -0.017006960515176583 | 37 |
| JAPAN | Japan Equities | 97.58000183105469 | 95.84 | -0.01783154128309239 | 38 |
| AUSTRALIA | Australia Equities | 29.059999465942383 | 28.540000915527344 | -0.017893962834530153 | 39 |
| DIVIDEND | US Dividend Equities | 34.34000015258789 | 33.71 | -0.018345956604208458 | 40 |
| OIL | Crude Oil | 156.66000366210938 | 153.55999755859375 | -0.019788114586042238 | 41 |
| CANADA | Canada Equities | 60.5 | 59.26 | -0.020495867768595022 | 42 |
| MID_CAP | US Mid-Cap Stocks | 73.79000091552734 | 72.27 | -0.02059900930571068 | 43 |
| UNITED_KINGDOM | United Kingdom Equities | 47.90999984741211 | 46.91 | -0.020872466094698394 | 44 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.22000122070312 | 91.20999908447266 | -0.021561919222374715 | 45 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.52999877929688 | 76.81 | -0.021902442455536186 | 46 |
| AGRICULTURE | Agriculture Commodities | 28.959999084472656 | 28.260000228881836 | -0.02417123196547799 | 47 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 80.93000030517578 | 78.89 | -0.02520697266135208 | 48 |
| YEN | Japanese Yen | 59.43000030517578 | 57.880001068115234 | -0.026081090848077193 | 49 |
| MEXICO | Mexico Equities | 74.81999969482422 | 72.69999694824219 | -0.028334706699132517 | 50 |
| INDIA | India Equities | 48.43000030517578 | 47.04 | -0.02870122437367051 | 51 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 119.59500122070312 | 115.84 | -0.031397643566837385 | 52 |
| EURO | Euro | 106.55000305175781 | 102.9800033569336 | -0.03350539270364972 | 53 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.72000122070312 | 69.3 | -0.03374234773443585 | 54 |
| CHINA | China Equities | 53.31999969482422 | 51.44 | -0.03525880918200219 | 55 |
| EUROPE | Europe Equities | 89.2300033569336 | 85.99 | -0.03631069410558119 | 56 |
| COMMUNICATIONS | Communication Services Sector | 115.06999969482422 | 110.82 | -0.03693403759533853 | 57 |
| REAL_ESTATE | Real Estate Sector | 43.119998931884766 | 41.49 | -0.03780146039566512 | 58 |
| GOLD | Gold | 80.54000091552734 | 77.07 | -0.04308419265064056 | 59 |
| FINANCIALS | Financials Sector | 57.029998779296875 | 54.52 | -0.044011903086486726 | 60 |
| SMALL_VALUE | US Small-Cap Value | 219.4499969482422 | 207.71 | -0.053497366650732237 | 61 |
| SMALL_CAP | US Small-Cap Stocks | 287.9100036621094 | 271.37 | -0.05744852020328095 | 62 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 216.77000427246094 | 204.24 | -0.05780322012039918 | 63 |
| BIOTECH | Biotechnology | 157.60000610351562 | 146.77 | -0.06871831017825081 | 64 |
| REGIONAL_BANKS | Regional Banks | 74.11000061035156 | 68.54 | -0.075158555720934 | 65 |
| SOUTH_AFRICA | South Africa Equities | 68.48999786376953 | 63.279998779296875 | -0.07606948820228665 | 66 |
| SOLAR | Solar Energy | 46.220001220703125 | 42.64 | -0.07745567127115416 | 67 |
| SOUTH_KOREA | South Korea Equities | 176.22000122070312 | 159.8300018310547 | -0.09300873496829187 | 68 |
| METALS_MINING | Metals and Mining | 110.16999816894531 | 99.86 | -0.09358262993827926 | 69 |
| SILVER | Silver | 56.84000015258789 | 50.220001220703125 | -0.11646725746152842 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | CYBERSECURITY | 35.0 | 0.03688152759309027 | 0.012908534657581593 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 65.0 | 0.011460407766308078 | 0.007449265048100251 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | CYBERSECURITY | 35.0 | 0.03688152759309027 | 0.012908534657581593 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SMALL_VALUE | 35.0 | -0.053497366650732237 | -0.018724078327756282 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 30.0 | 0.011460407766308078 | 0.0034381223298924233 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 35.0 | -0.05780322012039918 | -0.02023112704213971 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | CYBERSECURITY | 35.0 | 0.03688152759309027 | 0.012908534657581593 | V3 selected model rank 2: overreaction with 65% estimated probability of beating SPY. |
| google-gemini-3-1-pro | INDUSTRIALS | 30.0 | -0.017006960515176583 | -0.005102088154552975 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | CYBERSECURITY | 35.0 | 0.03688152759309027 | 0.012908534657581593 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | AEROSPACE_DEFENSE | 35.0 | -0.05780322012039918 | -0.02023112704213971 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | 0.011460407766308078 | 0.0034381223298924233 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | CYBERSECURITY | 35.0 | 0.03688152759309027 | 0.012908534657581593 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_VALUE | 35.0 | -0.053497366650732237 | -0.018724078327756282 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_CAP | 30.0 | -0.05744852020328095 | -0.017234556060984285 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | 0.03688152759309027 | 0.012908534657581593 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 35.0 | -0.053497366650732237 | -0.018724078327756282 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 30.0 | -0.05780322012039918 | -0.017340966036119752 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.011460407766308078 | 0.011460407766308078 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SP500 | 2 | 0.57 | 0.011460407766308078 | 0.020357799705681842 | 0.008897391939373764 | 1.8429702739090206 |  | True | True |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.011460407766308078 | 0.011460407766308078 | 0.0 | 1.8518676658483944 |  | False | True |
| anthropic-claude-opus-5 | CYBERSECURITY | 3 | 0.565 | 0.03688152759309027 | -0.002377421340282266 | -0.013837829106590344 | 1.8657054949549847 |  | False | False |
| openai-gpt-6-astra | CYBERSECURITY | 3 | 0.555 | 0.03688152759309027 | -0.003884470054665694 | -0.015344877820973771 | 1.867212543669368 |  | False | False |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 3 | 0.6 | -0.05780322012039918 | -0.012424680539111093 | -0.02388508830541917 | 1.8757527541538135 |  | False | False |
| xai-grok-4-3 | CYBERSECURITY | 3 | 0.5833 | 0.03688152759309027 | -0.023050099731158975 | -0.03451050749746705 | 1.8863781733458613 |  | False | False |
| xai-grok-4-5 | CYBERSECURITY | 3 | 0.59 | 0.03688152759309027 | -0.023156509706294442 | -0.034616917472602524 | 1.8864845833209969 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | b9ac7fb7f90a1baa6a921c4bc325ee0106a666f42a2ad92dfac735a03d81eaee |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | d8bd0b6e6072fed0b61fa9060f88c049042bb26f5e5e9c05370143b391a5a3f8 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | ff0aeacb87dae3820c72ced54f51388fe038f52e1f74bb532b9cbee0657e9b06 |
| market_data/universe_decision_context.md | a2ded79d8bf68481e2797eb6585063ccb61ebc209e1f96642a776a2336daea84 |
| market_data/universe_decision_context.json | d3d92bb008409518397434902f7f9d99185209f654a8547739a5d9ed777854e4 |
| market_data/decision_context_source_history.json | 15f3e8e369dd9af684734db1eb1f1fd7fbbfb832d6a20650ed66c6fcf6901711 |
| market_data/universe_quality_evidence.md | 33285df6f5e529c3de224f1bbb761988d64c31e8f830320f711cc660b8374106 |
| market_data/universe_quality_evidence.json | 411b5c9e1fce4b2de41425ba6dc6d7d1a5d47ba35558975f858abb878ddf31fa |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | fb1d3eb7614ae479bb67c3844d6cb4d2826b26d96598cbf5552b87bb67d5d1c6 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 616dae7c607a6c8212aec11eb32fbfd211117b717bce498f38af81b077cceb0b | yes |
| Final briefing | research/final_briefing.md | model-facing | b9ac7fb7f90a1baa6a921c4bc325ee0106a666f42a2ad92dfac735a03d81eaee | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
