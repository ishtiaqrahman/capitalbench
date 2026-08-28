# CapitalBench Report: CB-2026-08-20-1W / official-v3-20260820-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260820-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-20-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-20
- Decision deadline: 2026-08-20T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-20
- Exit date: 2026-08-27
- Entry rule: Use the Thursday, August 20, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Thursday, August 27, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.5933 | SPY down ~1% on the week with equal-weight outperforming (+0.89% active 5s), VIX low (~15.7), and breadth positive over 21 sessions. High-quality tech and defense names with strong prior relative trends pulled back sharply; NVIDIA earnings Aug 26 and Jackson Hole Aug 27 are key catalysts inside the window. Pattern favors quality-pullback mean reversion over chasing crypto continuation. | NVIDIA Aug 26 earnings disappointment could drag all tech-adjacent picks below SPY; Jackson Hole hawkish signals on Aug 27 exit date could hit growth multiples; Continued rotation into value/defensives would extend tech underperformance; Japan/Korea equity shock spilling into global risk sentiment |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.58 | The market is experiencing a mixed environment with some recent pullbacks in technology and international equities, while defensive and commodity sectors show some strength. The upcoming NVIDIA earnings and Jackson Hole symposium are key catalysts. | NVIDIA earnings disappoint, leading to further weakness in semiconductors and broader tech.; Jackson Hole symposium signals a more hawkish Fed, negatively impacting equities.; Continued weakness in international markets, particularly Japan, due to global growth concerns. |
| xai-grok-4-3 | xai | portfolio | CYBERSECURITY | 3 | 0.5833 | Cross-sectional pullbacks in quality names amid mixed macro signals and low dispersion favor selective reversals over broad continuation. | persistent inflation signals in minutes; weak July payrolls and revisions; NVIDIA earnings on exit date |
| openai-gpt-5-6-sol | openai | portfolio | CYBERSECURITY | 3 | 0.5767 | Breadth is healthier than cap-weighted performance, but the one-week window includes major macro releases and NVIDIA earnings. Favor high-quality pullback reversals while avoiding unsupported extrapolation of crypto and commodity gains. | NVIDIA earnings could trigger a broad technology-factor move that overwhelms cross-sectional signals; August 26 inflation, income, GDP, and durable-goods releases could sharply reprice rates; Jackson Hole communication on the exit date could reverse equity and currency moves; Recent pullbacks may reflect durable de-risking rather than temporary overreaction |
| xai-grok-4-6 | xai | portfolio | CYBERSECURITY | 3 | 0.5633 | SPY is only modestly lower on the week with VIX still mid-teens, equal-weight outperforming, and 5-session active dispersion at 2.58%. Shock pullbacks in quality names sit next to stretched crypto continuation and a high-vol NVIDIA/Jackson Hole week, so the one-week pattern is mixed rather than a clean trend or crash bounce. | NVIDIA earnings on August 26 can reprice high-beta tech, semis, and software inside the window.; Jackson Hole begins August 27 on the exit date after hawkish-leaning July minutes.; Japan bounce can fail if the Nikkei shock continues or the yen move reverses.; Energy inventories rose and Brent is volatile, which can spill into risk appetite and miners. |
| anthropic-claude-opus-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.5667 | SPY fell 1.0% week-to-date while equal-weight outperformed, indicating a narrow tech-led drawdown rather than broad risk-off. VIX near 15.7 is calm, credit spreads stable (HYG flat/positive), and long yields fell modestly. NVIDIA earnings on Aug 26 and Jackson Hole Aug 27 sit inside the window, raising path risk for high-beta semis/AI names into the exit close. Quality-pullback names with strong prior trend and shallow drawdowns (CIBR, ITA, EWJ) offer the cleanest short-horizon mean-reversion setups; crypto's 9-12% weekly spike is a stretched continuation without in-window catalyst support. | NVIDIA fiscal Q2 results on Aug 26 could drive a broad tech/AI move that dominates single-week relative returns for CIBR and Japan; Jackson Hole commentary on Aug 27 lands on the exit close and could reprice rates and equity risk premia abruptly; Yen strength or another Nikkei shock could extend Japan's decline rather than reverse it; Quality-pullback reversal may fail if the tech drawdown is the start of a longer de-risking phase; Low-volume selling signals can persist for more than one week, leaving mean-reversion timing wrong |
| xai-grok-4-5 | xai | portfolio | CYBERSECURITY | 3 | 0.5633 | Equity indices modestly lower WTD with low VIX near 15.7, stable Fed funds after July hold, mixed inflation prints, and Asia equity shock; one-week window includes NVDA results and Jackson Hole start, favoring selective quality pullback reversals over crowded crypto continuation or high-beta semis. | NVIDIA earnings August 26 can reverse tech and semiconductor beta sharply before exit; Jackson Hole symposium August 27–29 may reprice rates and growth expectations on the exit date; Further Asia equity weakness after Nikkei/Kospi drops could pressure Japan and global risk assets; Elevated crypto and silver volatility can unwind recent gains without fundamental support |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BITCOIN_ETF | Bitcoin ETF | 41.2 | 45.290000915527344 | 0.09927186688173162 | 1 |
| SOFTWARE | Software | 101.91 | 110.31999969482422 | 0.08252379251127673 | 2 |
| CYBERSECURITY | Cybersecurity | 93.45 | 100.79000091552734 | 0.07854468609446053 | 3 |
| ETHEREUM_ETF | Ethereum ETF | 17.55 | 18.8700008392334 | 0.07521372303324214 | 4 |
| METALS_MINING | Metals and Mining | 114.7 | 123.0 | 0.07236268526591094 | 5 |
| BRAZIL | Brazil Equities | 34.14 | 35.7599983215332 | 0.04745162043155249 | 6 |
| TAIWAN | Taiwan Equities | 104.07 | 108.62999725341797 | 0.043816635470529164 | 7 |
| TECHNOLOGY | Technology Sector | 183.1 | 188.61000061035156 | 0.03009284877308338 | 8 |
| BIOTECH | Biotechnology | 163.38 | 168.22999572753906 | 0.02968536985885084 | 9 |
| BROAD_AI_TECH | Broad AI Technology | 63.03 | 64.54000091552734 | 0.02395686047163803 | 10 |
| SOUTH_KOREA | South Korea Equities | 178.16 | 182.13999938964844 | 0.02233946671333875 | 11 |
| MEXICO | Mexico Equities | 75.5 | 77.16000366210938 | 0.021986803471647276 | 12 |
| SEMICONDUCTORS | Semiconductors | 562.65 | 573.0 | 0.018395094641429077 | 13 |
| SILVER | Silver | 61.66 | 62.77000045776367 | 0.018001953580338625 | 14 |
| GOLD | Gold | 85.13 | 86.62000274658203 | 0.017502675279948754 | 15 |
| LARGE_GROWTH | US Large-Cap Growth | 121.82 | 123.88999938964844 | 0.016992278686984497 | 16 |
| JAPAN | Japan Equities | 94.27 | 95.83999633789062 | 0.01665425201963111 | 17 |
| EMERGING_MARKETS | Emerging Markets | 60.02 | 61.0099983215332 | 0.016494473867597392 | 18 |
| FINANCIALS | Financials Sector | 56.95 | 57.880001068115234 | 0.016330132890522098 | 19 |
| COPPER | Copper | 39.35 | 39.97999954223633 | 0.01601015355111368 | 20 |
| AGRICULTURE | Agriculture Commodities | 28.38 | 28.81999969482422 | 0.0155038652157935 | 21 |
| SOUTH_AFRICA | South Africa Equities | 70.47 | 71.55999755859375 | 0.015467540209929798 | 22 |
| MATERIALS | Materials Sector | 52.42 | 53.22999954223633 | 0.015452108779784979 | 23 |
| NASDAQ100 | Nasdaq 100 | 710.93 | 721.1099853515625 | 0.01431925133495926 | 24 |
| AUSTRALIA | Australia Equities | 29.75 | 30.110000610351562 | 0.012100860852153339 | 25 |
| SP500 | S&P 500 | 762.6 | 771.0999755859375 | 0.011146047188483443 | 26 |
| TOTAL_US_MARKET | Total US Stock Market | 376.58 | 380.6300048828125 | 0.010754699885316521 | 27 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.34 | 83.12999725341797 | 0.00959433147216382 | 28 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.84 | 73.41999816894531 | 0.00796263274224751 | 29 |
| CANADA | Canada Equities | 61.77 | 62.2599983215332 | 0.007932626218766448 | 30 |
| SMALL_CAP | US Small-Cap Stocks | 297.67 | 299.80999755859375 | 0.0071891610125096594 | 31 |
| COMMUNICATIONS | Communication Services Sector | 110.68 | 111.41000366210938 | 0.006595623980026888 | 32 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.06 | 106.7300033569336 | 0.006317210606577417 | 33 |
| LARGE_VALUE | US Large-Cap Value | 256.17 | 257.5799865722656 | 0.00550410497820053 | 34 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.28 | 221.4499969482422 | 0.005311407972771853 | 35 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.67 | 95.12999725341797 | 0.004858954826428397 | 36 |
| SMALL_VALUE | US Small-Cap Value | 223.81 | 224.74000549316406 | 0.004155334851722703 | 37 |
| US_DOLLAR | US Dollar | 27.91 | 28.020000457763672 | 0.003941256100453927 | 38 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.56 | 79.87000274658203 | 0.0038964648891657294 | 39 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.68 | 124.16000366210938 | 0.0038810127919579607 | 40 |
| MID_CAP | US Mid-Cap Stocks | 76.37 | 76.6500015258789 | 0.0036663811166544047 | 41 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.49 | 97.83000183105469 | 0.0034875559652753907 | 42 |
| EUROPE | Europe Equities | 92.01 | 92.27999877929688 | 0.002934450378185849 | 43 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.0 | 93.2300033569336 | 0.0024731543756300045 | 44 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.3 | 93.5199966430664 | 0.0023579490146452553 | 45 |
| UNITED_KINGDOM | United Kingdom Equities | 48.54 | 48.630001068115234 | 0.0018541629195556464 | 46 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.65 | 47.70000076293945 | 0.001049333954658005 | 47 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.57 | 91.62999725341797 | 0.0006552064368021693 | 48 |
| SOLAR | Solar Energy | 49.73 | 49.7400016784668 | 0.00020111961525848265 | 49 |
| DIVIDEND | US Dividend Equities | 34.83 | 34.83000183105469 | 5.257119406465449e-08 | 50 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 51 |
| INDIA | India Equities | 49.55 | 49.529998779296875 | -0.0004036573300327806 | 52 |
| TIPS | Treasury Inflation-Protected Securities | 107.52 | 107.44000244140625 | -0.000744024912516239 | 53 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.47 | 105.38999938964844 | -0.0007585153157444458 | 54 |
| EURO | Euro | 107.8 | 107.54000091552734 | -0.0024118653476127294 | 55 |
| YEN | Japanese Yen | 57.66 | 57.5 | -0.0027748872702045846 | 56 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.32 | 85.08000183105469 | -0.0028129180607747717 | 57 |
| MOMENTUM | US Momentum Equities | 305.11 | 304.2300109863281 | -0.0028841696885447687 | 58 |
| HEALTHCARE | Healthcare Sector | 172.39 | 171.5800018310547 | -0.004698637791898053 | 59 |
| REGIONAL_BANKS | Regional Banks | 74.71 | 74.3499984741211 | -0.0048186524679280085 | 60 |
| INDUSTRIALS | Industrials Sector | 179.77 | 178.8000030517578 | -0.0053957665252388765 | 61 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.68 | 115.87999725341797 | -0.0068563828126674276 | 62 |
| BROAD_COMMODITIES | Broad Commodities | 18.55 | 18.420000076293945 | -0.007008082140488203 | 63 |
| LOW_VOL | US Low Volatility Equities | 75.66 | 75.12000274658203 | -0.007137156402563627 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.08 | 44.65999984741211 | -0.009316773571159898 | 65 |
| CHINA | China Equities | 55.51 | 54.900001525878906 | -0.01098898350065014 | 66 |
| UTILITIES | Utilities Sector | 43.77 | 43.18000030517578 | -0.013479545232447432 | 67 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 237.56 | 234.25999450683594 | -0.013891250602643845 | 68 |
| ENERGY | Energy Sector | 63.75 | 62.290000915527344 | -0.022901946423100505 | 69 |
| OIL | Crude Oil | 134.54 | 130.00999450683594 | -0.03367032475965548 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | CYBERSECURITY | 35.0 | 0.07854468609446053 | 0.02749064013306118 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SOFTWARE | 35.0 | 0.08252379251127673 | 0.028883327378946853 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | AEROSPACE_DEFENSE | 30.0 | -0.013891250602643845 | -0.004167375180793153 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | CYBERSECURITY | 35.0 | 0.07854468609446053 | 0.02749064013306118 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | AEROSPACE_DEFENSE | 35.0 | -0.013891250602643845 | -0.004861937710925346 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | JAPAN | 30.0 | 0.01665425201963111 | 0.004996275605889333 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 35.0 | 0.018395094641429077 | 0.006438283124500177 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | CYBERSECURITY | 35.0 | 0.07854468609446053 | 0.02749064013306118 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | JAPAN | 30.0 | 0.01665425201963111 | 0.004996275605889333 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | CYBERSECURITY | 35.0 | 0.07854468609446053 | 0.02749064013306118 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | JAPAN | 35.0 | 0.01665425201963111 | 0.005828988206870889 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | AEROSPACE_DEFENSE | 30.0 | -0.013891250602643845 | -0.004167375180793153 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | CYBERSECURITY | 35.0 | 0.07854468609446053 | 0.02749064013306118 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | JAPAN | 35.0 | 0.01665425201963111 | 0.005828988206870889 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 30.0 | -0.013891250602643845 | -0.004167375180793153 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | 0.07854468609446053 | 0.02749064013306118 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 35.0 | -0.013891250602643845 | -0.004861937710925346 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-5 | JAPAN | 30.0 | 0.01665425201963111 | 0.004996275605889333 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | 0.07854468609446053 | 0.02749064013306118 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | JAPAN | 35.0 | 0.01665425201963111 | 0.005828988206870889 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 30.0 | -0.013891250602643845 | -0.004167375180793153 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | CYBERSECURITY | 3 | 0.5933 | 0.07854468609446053 | 0.05220659233121488 | 0.041060545142731435 | 0.04706527455051674 |  | True | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.58 | 0.018395094641429077 | 0.038925198863450694 | 0.02777915167496725 | 0.060346668018280925 |  | True | True |
| xai-grok-4-3 | CYBERSECURITY | 3 | 0.5833 | 0.07854468609446053 | 0.02915225315913892 | 0.018006205970655477 | 0.0701196137225927 |  | True | True |
| openai-gpt-5-6-sol | CYBERSECURITY | 3 | 0.5767 | 0.07854468609446053 | 0.02915225315913892 | 0.018006205970655477 | 0.0701196137225927 |  | True | True |
| xai-grok-4-6 | CYBERSECURITY | 3 | 0.5633 | 0.07854468609446053 | 0.02915225315913892 | 0.018006205970655477 | 0.0701196137225927 |  | True | True |
| anthropic-claude-opus-5 | CYBERSECURITY | 3 | 0.5667 | 0.07854468609446053 | 0.027624978028025167 | 0.016478930839541724 | 0.07164688885370646 |  | True | True |
| xai-grok-4-5 | CYBERSECURITY | 3 | 0.5633 | 0.07854468609446053 | 0.027624978028025167 | 0.016478930839541724 | 0.07164688885370646 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 4ad11240b473c99230551b0bc157ddcf090ed4d882ab174ff983565818e67531 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 201c8074c0104f6596bea1df5b29986e5bd43190d9a5752c197ac7ad03fb39f9 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 62b78bdcbca4a6dcc4310f3e7df646a791e25e0ed155c52ce6940c15d3fccdef |
| market_data/universe_decision_context.md | defaaf248980216cbeee3b3d855bb95b06c5f36f6236df19514ca491e79332e1 |
| market_data/universe_decision_context.json | 21e9454a58b406615a29463b7ff726bcbc7aef60e6904dab4f6fcd3bc2fd35f4 |
| market_data/decision_context_source_history.json | d070413425fd0517edead61163a57197ca2bff0d9ad572f0deebeda513ff075e |
| market_data/universe_quality_evidence.md | 18c482aff755cd719debc04fe510bb2c9f45e8c88dc728af832a3d8deb5b0ae3 |
| market_data/universe_quality_evidence.json | 309eaff911070f41a2847ebbd999a3d47427cb84ddc1d233cb132ddcc1c307be |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | eaeaa350102a156008b5437e8e63108d2100b59865c6a32284413f2901ed448b | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | aaf4c8267fded99b7bd7599ca4d9ad9e8edea283e38d3337d6dfc5d277c86d84 | yes |
| Final briefing | research/final_briefing.md | model-facing | 4ad11240b473c99230551b0bc157ddcf090ed4d882ab174ff983565818e67531 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
