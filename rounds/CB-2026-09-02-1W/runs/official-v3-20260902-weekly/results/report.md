# CapitalBench Report: CB-2026-09-02-1W / official-v3-20260902-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260902-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-02-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-02
- Decision deadline: 2026-09-03T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-03
- Exit date: 2026-09-11
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.55 | Oil price surge supports energy continuation while metals show pullbacks after prior gains; equities mixed with broad index declines. | Oil price reversal after sharp move; Geopolitical escalation in Strait of Hormuz; FOMC policy surprise on September 15; Broad equity volatility from labor data |
| anthropic-claude-fable-5 | anthropic | portfolio | GOLD | 3 | 0.6 | Renewed US-Iran strikes and Strait of Hormuz incidents drove crude sharply higher while rising yields (10y near 4.79%, 66% implied odds of a September Fed hike) pressured equities for a third straight session. Gold and silver fell hard despite escalating geopolitical risk and prior strong uptrends, which looks like a temporary rate-driven overreaction given the live safe-haven catalyst set (CPI Sept 11, PPI Sept 10, payrolls Sept 4) inside the window. | Rapid Middle East de-escalation would reverse oil gains and remove the safe-haven bid for gold and silver; Hot CPI/PPI or strong payrolls could push real yields higher, extending the precious-metals drawdown; A confirmed September Fed hike repricing could hit all high-beta assets and drag SPY-relative comparisons; Silver's 40% volatility makes the one-week outcome distribution very wide |
| google-gemini-3-1-pro | google | portfolio | GOLD | 3 | 0.5767 | The market is experiencing a broad pullback, with major indexes down for three consecutive days. Economic data is mixed, with manufacturing PMI down but still expanding, and job openings little changed. Inflation data shows moderate increases. The upcoming week has significant catalysts, including the ADP employment report, ISM Services PMI, and the August Employment Situation, which could drive volatility. | Geopolitical tensions in the Middle East could escalate or de-escalate rapidly, impacting oil prices.; Upcoming employment data (ADP, Employment Situation) could surprise the market, leading to increased volatility and potential shifts in interest rate expectations. |
| xai-grok-4-5 | xai | portfolio | SILVER | 3 | 0.5867 | Equities posted a third down day with rising yields and 66% September hike odds; oil surged on Hormuz/geopolitical reports while gold/silver sold off sharply after strong priors; labor and ISM data plus OPEC+ sit inside the one-week window, favoring selective mean-reversion in high-quality pullbacks over pure momentum continuation. | September 4 Employment Situation and Fed hike odds could extend equity and rate pressure; OPEC+ Sept 6 and Hormuz developments may reverse oil or amplify commodity vol; Broadcom results and ISM Services on Sept 2-3 can swing tech-adjacent risk appetite; Labor Day holiday thins liquidity into the exit window |
| anthropic-claude-opus-5 | anthropic | portfolio | SILVER | 3 | 0.5667 | Rates are rising with a 66% implied probability of a September hike, inflation is re-accelerating (CPI 3.4%, PCE 3.7%, euro-area 3.3%), and oil has spiked on Strait of Hormuz disruption. Equities fell three sessions in a row with only 25% of assets positive over five days, while the prior month was broadly positive. That mix argues for a partial unwind of the sharp precious-metals flush (silver -7.7%, gold -5.8% in a week against a strongly positive prior trend and no fundamental change) and against chasing the oil/Taiwan momentum into OPEC+ and heavy macro prints. Cross-sectional dispersion of 2.75% is elevated, so selective reversal beats broad beta. | A hawkish September repricing after ADP, payrolls, and CPI could push real yields higher and extend the gold and silver decline.; OPEC+ supply news or Hormuz de-escalation could reverse the energy shock and drag broad commodity and materials sentiment.; Silver's 40% volatility means a single adverse session can dominate the one-week excess return.; Broad equity beta rebound would let SPY outperform low-beta and defensive commodity positions.; Only four scoring sessions plus a holiday-shortened week reduces the chance mean reversion completes. |
| xai-grok-4-6 | xai | portfolio | SILVER | 3 | 0.5633 | SPY is in a three-session decline into a dense labor/inflation week with rising Treasury yields, while oil jumped on Hormuz-related supply news and precious metals sold off after strong prior-window gains. Short-horizon breadth is weak (about 25% of assets positive over 5 sessions) but 21-session breadth remains majority-positive, so the week is mixed continuation in energy versus pullback/reversal tests in metals and cyclicals. | September 4 Employment Situation and September 11 CPI can extend the equity and duration selloff, dragging even oversold cyclicals.; Hormuz/oil news and the September 6 OPEC+ meeting can reverse oil or further strengthen the dollar, delaying a metals bounce.; Silver and gold 21s volatilities near 30–40% can produce large negative excess versus SPY even if the overreaction thesis is directionally right. |
| openai-gpt-5-6-sol | openai | portfolio | HEALTHCARE | 3 | 0.5767 | High cross-sectional dispersion, weak equity breadth, rising yields, and an oil-driven inflation shock favor selective pullback reversals over broad risk taking; major labor and inflation releases create substantial one-week event risk. | Stronger-than-expected employment, PPI, or CPI data could push yields and the dollar higher, hurting gold and broader equities.; A rapid de-escalation around Iran or normalization of Hormuz shipping could reverse commodity and inflation-sensitive trades.; Broadcom results and technology-weighted index moves could cause SPY to outperform defensive and materials exposures.; The short scoring window and Labor Day closure amplify gap risk and reduce time for pullback reversals to develop. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 142.09 | 154.9 | 0.09015412766556419 | 1 |
| SOUTH_KOREA | South Korea Equities | 180.56 | 188.72 | 0.04519273371732391 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 19.09 | 19.79 | 0.03666841278156108 | 3 |
| SEMICONDUCTORS | Semiconductors | 552.6 | 568.53 | 0.02882736156351773 | 4 |
| MOMENTUM | US Momentum Equities | 299.42 | 307.04 | 0.02544920179012755 | 5 |
| YEN | Japanese Yen | 58.87 | 59.68000030517578 | 0.0137591354709663 | 6 |
| TECHNOLOGY | Technology Sector | 185.97 | 187.67 | 0.009141259342904773 | 7 |
| ENERGY | Energy Sector | 64.62 | 65.14 | 0.008047044258743252 | 8 |
| ETHEREUM_ETF | Ethereum ETF | 19.02 | 19.15999984741211 | 0.007360664953317997 | 9 |
| TAIWAN | Taiwan Equities | 110.13 | 110.91 | 0.007082538817760886 | 10 |
| JAPAN | Japan Equities | 97.9 | 98.56 | 0.006741573033707926 | 11 |
| US_DOLLAR | US Dollar | 28.01 | 28.06999969482422 | 0.0021420812147168178 | 12 |
| BRAZIL | Brazil Equities | 38.13 | 38.19 | 0.0015735641227379027 | 13 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.42 | 91.5 | 0.0008750820389411551 | 14 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 15 |
| EURO | Euro | 107.28 | 107.01000213623047 | -0.002516758610827119 | 16 |
| NASDAQ100 | Nasdaq 100 | 717.67 | 714.88 | -0.003887580642913835 | 17 |
| BROAD_AI_TECH | Broad AI Technology | 64.3 | 63.98 | -0.004976671850699832 | 18 |
| AGRICULTURE | Agriculture Commodities | 29.09 | 28.93 | -0.0055001718803712185 | 19 |
| COMMUNICATIONS | Communication Services Sector | 113.38 | 112.6 | -0.006879520197565769 | 20 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.21 | 78.6 | -0.007701047847494036 | 21 |
| MUNICIPAL_BONDS | Municipal Bonds | 104.0 | 103.17 | -0.00798076923076918 | 22 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.4 | 46.99 | -0.008649789029535837 | 23 |
| LARGE_GROWTH | US Large-Cap Growth | 123.43 | 122.27 | -0.00939803937454431 | 24 |
| CYBERSECURITY | Cybersecurity | 95.32 | 94.4 | -0.00965169953839684 | 25 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.95 | 95.98 | -0.010005157297576006 | 26 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.44 | 72.69 | -0.010212418300653558 | 27 |
| EMERGING_MARKETS | Emerging Markets | 60.99 | 60.35 | -0.010493523528447346 | 28 |
| TIPS | Treasury Inflation-Protected Securities | 107.0 | 105.84 | -0.010841121495327122 | 29 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.5 | 104.32 | -0.011184834123222798 | 30 |
| SP500 | S&P 500 | 773.17 | 764.29 | -0.011485184370836898 | 31 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.45 | 93.34 | -0.011752249867654885 | 32 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.81 | 121.36 | -0.011806856119208509 | 33 |
| SOLAR | Solar Energy | 47.72 | 47.15 | -0.011944677284157601 | 34 |
| TOTAL_US_MARKET | Total US Stock Market | 380.93 | 376.31 | -0.012128212532486304 | 35 |
| INDUSTRIALS | Industrials Sector | 174.56 | 172.37 | -0.01254582951420713 | 36 |
| REGIONAL_BANKS | Regional Banks | 74.87 | 73.9 | -0.012955790036062509 | 37 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.28 | 91.01 | -0.013762462071954862 | 38 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.66 | 91.38 | -0.013813943449168975 | 39 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.07 | 80.87 | -0.014621664432801107 | 40 |
| LARGE_VALUE | US Large-Cap Value | 259.38 | 255.58 | -0.014650319993831373 | 41 |
| UTILITIES | Utilities Sector | 43.03 | 42.39 | -0.014873344178480186 | 42 |
| UNITED_KINGDOM | United Kingdom Equities | 48.68 | 47.94 | -0.015201314708299107 | 43 |
| MID_CAP | US Mid-Cap Stocks | 75.75 | 74.44 | -0.017293729372937272 | 44 |
| SMALL_VALUE | US Small-Cap Value | 223.72 | 219.69 | -0.018013588414089066 | 45 |
| COPPER | Copper | 39.91 | 39.18 | -0.01829115509897261 | 46 |
| EUROPE | Europe Equities | 91.74 | 90.02 | -0.01874863745367339 | 47 |
| REAL_ESTATE | Real Estate Sector | 44.25 | 43.42 | -0.018757062146892656 | 48 |
| LOW_VOL | US Low Volatility Equities | 75.24 | 73.79 | -0.019271664008505995 | 49 |
| MEXICO | Mexico Equities | 76.97 | 75.38 | -0.020657398986618225 | 50 |
| SMALL_CAP | US Small-Cap Stocks | 295.19 | 288.89 | -0.021342186388427886 | 51 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.26 | 83.38 | -0.022050199390101 | 52 |
| FINANCIALS | Financials Sector | 58.56 | 57.25 | -0.022370218579235046 | 53 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.05 | 214.87 | -0.023540104521699634 | 54 |
| SOUTH_AFRICA | South Africa Equities | 71.82 | 70.1 | -0.023948760790866053 | 55 |
| CHINA | China Equities | 54.37 | 52.96 | -0.025933419164980598 | 56 |
| INDIA | India Equities | 49.92 | 48.57 | -0.027043269230769273 | 57 |
| DIVIDEND | US Dividend Equities | 35.08 | 34.12 | -0.027366020524515422 | 58 |
| GOLD | Gold | 84.1 | 81.71 | -0.02841854934601662 | 59 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.46 | 112.96 | -0.030053237162974367 | 60 |
| CANADA | Canada Equities | 62.47 | 60.58 | -0.03025452217064195 | 61 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 225.98 | 219.01 | -0.03084343747234264 | 62 |
| MATERIALS | Materials Sector | 52.62 | 50.95 | -0.03173698213606979 | 63 |
| AUSTRALIA | Australia Equities | 30.37 | 29.27 | -0.03621995390187693 | 64 |
| METALS_MINING | Metals and Mining | 118.38 | 113.63 | -0.04012502111843219 | 65 |
| SILVER | Silver | 60.55 | 58.12 | -0.04013212221304707 | 66 |
| HEALTHCARE | Healthcare Sector | 173.26 | 165.36 | -0.045596213782754136 | 67 |
| BIOTECH | Biotechnology | 164.38 | 156.2 | -0.04976274485947196 | 68 |
| SOFTWARE | Software | 106.95 | 101.52 | -0.05077138849929885 | 69 |
| BITCOIN_ETF | Bitcoin ETF | 46.35 | 43.77000045776367 | -0.05566342054447315 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | GOLD | 35.0 | -0.02841854934601662 | -0.009946492271105816 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SILVER | 35.0 | -0.04013212221304707 | -0.014046242774566474 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SP500 | 30.0 | -0.011485184370836898 | -0.0034455553112510695 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | SILVER | 35.0 | -0.04013212221304707 | -0.014046242774566474 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | GOLD | 35.0 | -0.02841854934601662 | -0.009946492271105816 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | MATERIALS | 30.0 | -0.03173698213606979 | -0.009521094640820937 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | GOLD | 35.0 | -0.02841854934601662 | -0.009946492271105816 | V3 selected model rank 2: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SILVER | 35.0 | -0.04013212221304707 | -0.014046242774566474 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | INDUSTRIALS | 30.0 | -0.01254582951420713 | -0.003763748854262139 | V3 selected model rank 4: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | HEALTHCARE | 35.0 | -0.045596213782754136 | -0.015958674823963948 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | MATERIALS | 35.0 | -0.03173698213606979 | -0.011107943747624426 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | GOLD | 30.0 | -0.02841854934601662 | -0.008525564803804985 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | SILVER | 35.0 | -0.04013212221304707 | -0.014046242774566474 | V3 selected model rank 10: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 65.0 | -0.011485184370836898 | -0.007465369841043984 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | SILVER | 35.0 | -0.04013212221304707 | -0.014046242774566474 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | GOLD | 35.0 | -0.02841854934601662 | -0.009946492271105816 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | MATERIALS | 30.0 | -0.03173698213606979 | -0.009521094640820937 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SILVER | 35.0 | -0.04013212221304707 | -0.014046242774566474 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | GOLD | 35.0 | -0.02841854934601662 | -0.009946492271105816 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | MATERIALS | 30.0 | -0.03173698213606979 | -0.009521094640820937 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 2 | 0.55 | -0.011485184370836898 | -0.021511612615610458 | -0.01002642824477356 | 0.11166574028117465 |  | False | False |
| anthropic-claude-fable-5 | GOLD | 3 | 0.6 | -0.02841854934601662 | -0.02743829035692336 | -0.01595310598608646 | 0.11759241802248754 |  | False | False |
| google-gemini-3-1-pro | GOLD | 3 | 0.5767 | -0.02841854934601662 | -0.027756483899934428 | -0.01627129952909753 | 0.11791061156549862 |  | False | False |
| xai-grok-4-5 | SILVER | 3 | 0.5867 | -0.04013212221304707 | -0.033513829686493225 | -0.022028645315656327 | 0.1236679573520574 |  | False | False |
| anthropic-claude-opus-5 | SILVER | 3 | 0.5667 | -0.04013212221304707 | -0.033513829686493225 | -0.022028645315656327 | 0.1236679573520574 |  | False | False |
| xai-grok-4-6 | SILVER | 3 | 0.5633 | -0.04013212221304707 | -0.033513829686493225 | -0.022028645315656327 | 0.1236679573520574 |  | False | False |
| openai-gpt-5-6-sol | HEALTHCARE | 3 | 0.5767 | -0.045596213782754136 | -0.03559218337539336 | -0.024106999004556463 | 0.12574631104095754 |  | False | False |

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
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | d8de23091b094a590d38988ac7e4339a24b6625b43c8aca723e24e3e98271848 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | a5daa3a00a65bc5616f5673c83ea091228eb1d3660fdcd95f48b69ef9923db0a |
| market_data/universe_decision_context.md | 3fa65aab5fc7aa516093db1f7966700af3ea1a974dd1461e8d521a25176967e1 |
| market_data/universe_decision_context.json | 6e90ba02b8495400981189196fb9fc65a25d782202c59212e116563e474e8e6f |
| market_data/decision_context_source_history.json | 645eaba870e709a87c2073c78ef54cb656c15c6a6cb3ba3cbd874cbd3502ba88 |
| market_data/universe_quality_evidence.md | 60f20f2de0b1a5e8b1fd05ac98f6635a98e0ea356a43b7ecd6ed3a8cdbdcf2df |
| market_data/universe_quality_evidence.json | f8661a1f22c3ab27b6e7f7af8d1e361af5daabbc63dae2398e2764e653ba7b23 |

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
