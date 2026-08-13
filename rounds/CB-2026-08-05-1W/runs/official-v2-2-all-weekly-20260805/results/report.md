# CapitalBench Report: CB-2026-08-05-1W / official-v2-2-all-weekly-20260805

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260805
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-05-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-05
- Decision deadline: 2026-08-06T12:30:00Z
- Horizon: one week
- Entry date: 2026-08-05
- Exit date: 2026-08-12
- Entry rule: Use the Wednesday, August 5, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Wednesday, August 12, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | TECHNOLOGY | 5 | 0.58 | Selected holdings clear the SPY base hurdle on recent relative trends, quality ranks, and near-term catalysts including jobs, CPI, and Hormuz news; weighted base targets modest alpha over the one-week window. | Hotter July CPI on Aug 12 triggers rate-hike fears and equity selloff; Weaker-than-expected Employment Situation on Aug 7 sparks growth scare; Treasury auction supply on Aug 11-12 pressures yields and risk assets; Failure of Hormuz draft leads to renewed energy volatility drag |
| openai-gpt-5-6-sol | openai | portfolio | DIVIDEND | 4 | 0.57 | Each selected active holding has a base forecast above SPY's 0.15% forecast. The weighted base return is 0.55%, implying expected one-week alpha of 0.40 percentage point. | A strong employment or hot CPI report could lift yields and pressure real estate and software.; Final approval of the Strait of Hormuz arrangement could extend the decline in crude and energy equities.; The recent mega-cap-led SPY rally could continue while dividend and other lagging exposures remain weak.; Software's recent strength may reverse because its quality evidence score is low and volatility is elevated. |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.5 | Modest positive SPY base case into jobs and CPI, with a rotation tilt toward defensively-ranked, recently-lagging exposures and gold rather than extended momentum/tech. | Tech momentum continues and mega-cap leadership extends SPY gains beyond our tilts; Hot July CPI on Aug 12 hurts gold-adjacent and rate-sensitive names simultaneously; Financials give back gains if Treasury auctions go poorly and curve flattens; Healthcare defensive bid fades if risk appetite stays elevated |
| openai-gpt-5-5 | openai | portfolio | ENERGY | 5 | 0.56 | SPY has strong recent gains but faces reversal risk around payrolls, CPI, and Treasury auctions. The selected holdings each have base forecasts above SPY and span multiple clusters for one-week alpha potential. | July payrolls or CPI surprise in a way that favors mega-cap SPY over active sector tilts.; A rapid geopolitical de-escalation could hurt the energy allocation.; Technology leadership could reverse after recent sharp gains, weighing on software.; Treasury refunding or inflation data could push yields higher and pressure real estate. |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 4 | 0.52 | Core SPY plus overweight to lagging defensive equity segments with the strongest supplied quality-evidence scores, positioned for mean reversion after a sharp growth-led rally into a data-heavy week. | Hot July CPI on Aug 12 could pressure all equities including defensives; Continued mega-cap tech momentum would leave defensive tilt lagging SPY; Weak Treasury auction demand Aug 11-12 could lift yields and hit rate-sensitive dividend payers; Hormuz deal completion could spark broad risk-on cyclical rally |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.5 | Blend of benchmark plus recent leaders in technology/growth for modest alpha over the one-week window. | Hot July CPI Aug 12 triggers rate-driven equity selloff especially high-beta tech; Jobs report Aug 7 surprise shifts Fed expectations; Tech momentum reverses after strong run |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.52 | SPY base forecast set at 0.4% given recent close and scheduled data releases; portfolio expected return equals benchmark with zero alpha. | July CPI release on August 12 could trigger volatility; FOMC dissent signals persistent inflation concerns; Weak June payrolls and ADP data point to labor softening |
| google-gemini-3-1-pro | google | portfolio | SP500 | 1 | 0.5 | A 100% SPY allocation is selected due to the lack of compelling active opportunities with a higher base forecast over the one-week scoring window. | Unexpected inflation data from the July CPI report.; Geopolitical escalation impacting global markets.; A sudden shift in Federal Reserve rate expectations. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 114.88 | 127.3 | 0.10811281337047363 | 1 |
| ENERGY | Energy Sector | 57.31 | 61.03 | 0.064910137846798 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 16.98 | 17.969999313354492 | 0.05830384648730802 | 3 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.4 | 128.92999267578125 | 0.053349613364225945 | 4 |
| SILVER | Silver | 56.07 | 59.060001373291016 | 0.05332622388605346 | 5 |
| TAIWAN | Taiwan Equities | 101.7 | 106.18000030517578 | 0.04405113377753955 | 6 |
| METALS_MINING | Metals and Mining | 111.92 | 116.79000091552734 | 0.04351323191143086 | 7 |
| BIOTECH | Biotechnology | 153.01 | 159.38999938964844 | 0.04169661714690842 | 8 |
| SOUTH_KOREA | South Korea Equities | 169.14 | 175.8699951171875 | 0.03978949460321335 | 9 |
| GOLD | Gold | 79.85 | 82.9800033569336 | 0.03919853922271255 | 10 |
| CYBERSECURITY | Cybersecurity | 97.57 | 100.38999938964844 | 0.028902320279270644 | 11 |
| JAPAN | Japan Equities | 95.16 | 97.79 | 0.027637662883564618 | 12 |
| SEMICONDUCTORS | Semiconductors | 569.7 | 584.8300170898438 | 0.026557867456281636 | 13 |
| HEALTHCARE | Healthcare Sector | 164.16 | 168.44 | 0.026072124756335358 | 14 |
| BROAD_AI_TECH | Broad AI Technology | 62.36 | 63.77000045776367 | 0.022610655191848572 | 15 |
| SOUTH_AFRICA | South Africa Equities | 66.85 | 68.33000183105469 | 0.022139144817572065 | 16 |
| SOLAR | Solar Energy | 51.27 | 52.33000183105469 | 0.02067489430572822 | 17 |
| DIVIDEND | US Dividend Equities | 33.64 | 34.26 | 0.01843043995243754 | 18 |
| SOFTWARE | Software | 101.31 | 103.08000183105469 | 0.017471146294094186 | 19 |
| CANADA | Canada Equities | 60.78 | 61.77000045776367 | 0.01628826024619401 | 20 |
| TECHNOLOGY | Technology Sector | 185.91 | 188.86 | 0.015867893066537686 | 21 |
| MOMENTUM | US Momentum Equities | 309.98 | 314.73 | 0.015323569262533088 | 22 |
| MID_CAP | US Mid-Cap Stocks | 77.0 | 78.06 | 0.01376623376623387 | 23 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.35 | 73.3 | 0.013130615065653162 | 24 |
| SMALL_CAP | US Small-Cap Stocks | 299.77 | 302.71 | 0.00980751909797517 | 25 |
| NASDAQ100 | Nasdaq 100 | 717.3 | 723.7 | 0.008922347692736698 | 26 |
| AGRICULTURE | Agriculture Commodities | 27.63 | 27.84 | 0.007600434310532034 | 27 |
| EMERGING_MARKETS | Emerging Markets | 60.01 | 60.41 | 0.0066655557407098165 | 28 |
| LARGE_VALUE | US Large-Cap Value | 256.13 | 257.77 | 0.00640299847733572 | 29 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 219.73 | 221.0800018310547 | 0.006143912215240022 | 30 |
| TOTAL_US_MARKET | Total US Stock Market | 379.65 | 381.83 | 0.005742130910048715 | 31 |
| EUROPE | Europe Equities | 91.85 | 92.25 | 0.004354926510615087 | 32 |
| LARGE_GROWTH | US Large-Cap Growth | 123.89 | 124.42 | 0.004277988538219368 | 33 |
| UTILITIES | Utilities Sector | 43.66 | 43.84 | 0.0041227668346313084 | 34 |
| US_DOLLAR | US Dollar | 28.09 | 28.2 | 0.00391598433606255 | 35 |
| SMALL_VALUE | US Small-Cap Value | 225.08 | 225.93 | 0.003776435045317106 | 36 |
| SP500 | S&P 500 | 769.79 | 772.49 | 0.0035074500837890543 | 37 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.82 | 105.9800033569336 | 0.0015120332350557764 | 38 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.52 | 79.61 | 0.0011317907444667874 | 39 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.43 | 91.51 | 0.0008749863283386006 | 40 |
| REGIONAL_BANKS | Regional Banks | 77.34 | 77.37999725341797 | 0.0005171612802943315 | 41 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 42 |
| UNITED_KINGDOM | United Kingdom Equities | 48.37 | 48.369998931884766 | -2.208218385923999e-08 | 43 |
| TIPS | Treasury Inflation-Protected Securities | 107.0 | 106.92 | -0.0007476635514018781 | 44 |
| MATERIALS | Materials Sector | 52.64 | 52.58 | -0.0011398176291793627 | 45 |
| FINANCIALS | Financials Sector | 58.0 | 57.92 | -0.0013793103448275223 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.34 | 93.19000244140625 | -0.0016070019133678226 | 47 |
| EURO | Euro | 106.585 | 106.337 | -0.002326781442041459 | 48 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.17 | 94.94000244140625 | -0.002416702307384222 | 49 |
| INDUSTRIALS | Industrials Sector | 186.35 | 185.88 | -0.0025221357660316635 | 50 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 252.28 | 251.6199951171875 | -0.0026161601506758947 | 51 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.71 | 97.43 | -0.002865622761232034 | 52 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.33 | 85.08 | -0.0029298019453884994 | 53 |
| MEXICO | Mexico Equities | 76.69 | 76.45999908447266 | -0.0029990991723476412 | 54 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.99 | 47.81999969482422 | -0.0035424110267927578 | 55 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.31 | 92.96 | -0.0037509377344336903 | 56 |
| COMMUNICATIONS | Communication Services Sector | 110.87 | 110.27 | -0.005411743483358933 | 57 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.74 | 106.12 | -0.00580850665167687 | 58 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.64 | 117.89 | -0.006321645313553614 | 59 |
| LOW_VOL | US Low Volatility Equities | 76.33 | 75.82 | -0.006681514476614803 | 60 |
| INDIA | India Equities | 50.31 | 49.95000076293945 | -0.007155619897844301 | 61 |
| AUSTRALIA | Australia Equities | 30.14 | 29.889999389648438 | -0.008294645333495776 | 62 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.0 | 82.11 | -0.010722891566265047 | 63 |
| YEN | Japanese Yen | 58.15 | 57.52 | -0.0108340498710231 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.2 | 44.49 | -0.01570796460176993 | 65 |
| CHINA | China Equities | 56.01 | 55.08 | -0.016604177825388367 | 66 |
| COPPER | Copper | 40.85 | 40.02000045776367 | -0.020318226248135396 | 67 |
| ETHEREUM_ETF | Ethereum ETF | 14.48 | 14.16 | -0.02209944751381221 | 68 |
| BITCOIN_ETF | Bitcoin ETF | 36.74 | 35.89 | -0.023135547087642983 | 69 |
| BRAZIL | Brazil Equities | 36.11 | 33.86000061035156 | -0.06230959262388358 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SP500 | 35.0 | 0.0035074500837890543 | 0.001227607529326169 | Core benchmark exposure amid strong ISM data and solid earnings season; anchors portfolio through jobs and CPI prints. |
| anthropic-claude-fable-5 | DIVIDEND | 30.0 | 0.01843043995243754 | 0.005529131985731261 | Highest quality-evidence score among equities (0.86), strong prior trend with deep recent relative pullback, near-zero beta cushions CPI-week risk. |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | 0.026072124756335358 | 0.005214424951267072 | Quality score 0.73, prior positive relative trend with recent -6.8% relative pullback offers mean-reversion into a data-heavy week. |
| anthropic-claude-fable-5 | CONSUMER_STAPLES | 15.0 | -0.0029298019453884994 | -0.0004394702918082749 | Quality score 0.81 with the deepest recent relative pullback (0.955 rank) among defensives; low correlation to SPY hedges macro-event risk. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | 0.0035074500837890543 | 0.0017537250418945272 | Core broad US large-cap; strong 5s momentum and near 52w high, benchmark anchor. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 25.0 | 0.015867893066537686 | 0.0039669732666344215 | Tech sector showing strong recent 3s/5s active return, Nvidia earnings tailwind, momentum after deep prior pullback. |
| anthropic-claude-opus-4-8 | LARGE_GROWTH | 25.0 | 0.004277988538219368 | 0.001069497134554842 | Large-cap growth leading with positive 5s active return and rebound after prior weakness. |
| anthropic-claude-opus-5 | SP500 | 40.0 | 0.0035074500837890543 | 0.0014029800335156218 | Core benchmark exposure given a strong tape and record Dow; limits tracking error. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | 0.026072124756335358 | 0.005214424951267072 | Defensive sector with strong prior relative trend and deep recent relative pullback; negative SPY beta offers CPI-day hedge. |
| anthropic-claude-opus-5 | GOLD | 20.0 | 0.03919853922271255 | 0.00783970784454251 | Sticky inflation (core PCE 3.3%, disinflation stalled), weak dollar 5s/21s, hedge into CPI print. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | -0.0013793103448275223 | -0.00027586206896550446 | At 52-week high with strong prior active return, low volatility and shallow drawdown; lagged last week so mean-reversion room. |
| google-gemini-3-1-pro | SP500 | 100.0 | 0.0035074500837890543 | 0.0035074500837890543 | Given the mixed economic data and lack of clear catalysts for active outperformance over a one-week horizon, a 100% allocation to the S&P 500 is the most prudent approach. |
| openai-gpt-5-5 | ENERGY | 25.0 | 0.064910137846798 | 0.0162275344616995 | Energy has the strongest prior active return and high quality evidence, with crude-related geopolitical supply constraints still unresolved despite recent weakness. |
| openai-gpt-5-5 | REAL_ESTATE | 25.0 | -0.01570796460176993 | -0.003926991150442483 | Real estate combines high quality evidence with a recent pullback and shallow drawdown, offering rebound potential if CPI or labor data ease rate pressure. |
| openai-gpt-5-5 | SOFTWARE | 25.0 | 0.017471146294094186 | 0.004367786573523547 | Software has strong short-term price action and a positive prior active return, with less severe drawdown than the most speculative technology subsectors. |
| openai-gpt-5-5 | CHINA | 15.0 | -0.016604177825388367 | -0.002490626673808255 | China has a very strong prior active trend and moderate pullback evidence, providing differentiated international equity exposure. |
| openai-gpt-5-5 | FINANCIALS | 10.0 | -0.0013793103448275223 | -0.00013793103448275223 | Financials have positive prior relative performance, low volatility versus SPY, and are near a 52-week high, supported by firm domestic activity data. |
| openai-gpt-5-6-sol | DIVIDEND | 30.0 | 0.01843043995243754 | 0.005529131985731261 | Strong quality evidence, prior relative strength, and a sharp recent relative pullback favor defensive rotation if market breadth improves. |
| openai-gpt-5-6-sol | ENERGY | 30.0 | 0.064910137846798 | 0.0194730413540394 | Energy combines high quality evidence and strong prior relative trend with a deep pullback that may reverse if geopolitical de-escalation remains incomplete. |
| openai-gpt-5-6-sol | REAL_ESTATE | 20.0 | -0.01570796460176993 | -0.003141592920353986 | High pullback and quality ranks support a rebound, with weak labor or benign CPI offering a plausible near-term rates catalyst. |
| openai-gpt-5-6-sol | SOFTWARE | 20.0 | 0.017471146294094186 | 0.0034942292588188376 | Software has both recent strength and positive prior active performance, though low quality evidence warrants a limited allocation. |
| xai-grok-4-3 | SP500 | 100.0 | 0.0035074500837890543 | 0.0035074500837890543 | No active option base forecast exceeds SPY; broad equity exposure aligns with neutral one-week outlook amid mixed macro data. |
| xai-grok-4-5 | TECHNOLOGY | 30.0 | 0.015867893066537686 | 0.004760367919961306 | Recent relative strength and mega-cap earnings support with Nvidia bounce; base exceeds SPY for weekly alpha. |
| xai-grok-4-5 | ENERGY | 25.0 | 0.064910137846798 | 0.0162275344616995 | High quality score and prior active strength plus Hormuz draft news support mean-reversion bounce from recent oil weakness. |
| xai-grok-4-5 | GOLD | 20.0 | 0.03919853922271255 | 0.00783970784454251 | Positive 5s return and inflation still elevated vs 2% target provide weekly support above SPY base. |
| xai-grok-4-5 | FINANCIALS | 15.0 | -0.0013793103448275223 | -0.00020689655172412836 | Solid quality rank, at 52w high, and stable labor data support modest outperformance vs SPY base. |
| xai-grok-4-5 | LARGE_VALUE | 10.0 | 0.00640299847733572 | 0.000640299847733572 | High quality evidence score and shallower drawdown favor mild continuation above SPY base in risk-on week. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | TECHNOLOGY | 5 | 0.58 | 0.015867893066537686 | 0.029261013522212758 | 0.025753563438423704 | 0.07885179984826086 |  | True | True |
| openai-gpt-5-6-sol | DIVIDEND | 4 | 0.57 | 0.01843043995243754 | 0.02535480967823551 | 0.021847359594446454 | 0.08275800369223812 |  | True | True |
| anthropic-claude-opus-5 | SP500 | 4 | 0.5 | 0.0035074500837890543 | 0.014181250760359698 | 0.010673800676570644 | 0.09393156261011393 |  | True | True |
| openai-gpt-5-5 | ENERGY | 5 | 0.56 | 0.064910137846798 | 0.014039772176489556 | 0.010532322092700502 | 0.09407304119398407 |  | True | True |
| anthropic-claude-fable-5 | SP500 | 4 | 0.52 | 0.0035074500837890543 | 0.011531694174516228 | 0.008024244090727174 | 0.0965811191959574 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.5 | 0.0035074500837890543 | 0.006790195443083791 | 0.0032827453592947364 | 0.10132261792738984 |  | True | True |
| xai-grok-4-3 | SP500 | 1 | 0.52 | 0.0035074500837890543 | 0.0035074500837890543 | 0.0 | 0.10460536328668457 |  | False | True |
| google-gemini-3-1-pro | SP500 | 1 | 0.5 | 0.0035074500837890543 | 0.0035074500837890543 | 0.0 | 0.10460536328668457 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 8a76c6e6ce6b3fe08a83e293601adca9ec61fd9fbab061267c7005b07e268e29 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 3ace5097a2ef327d9b86a5eae6c916528d603e0a13af38421538cc333ec68151 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | e505dcc9bdebab90104a2633962e1c8af9ca8ff5065669fe8a52ef419d7053c7 |
| market_data/universe_decision_context.md | 4e731484be4ff52ac953325e549bfdfdc0505eb4f9f1cb266766a1bfc41937f8 |
| market_data/universe_decision_context.json | 8b41b37c274cc8ed126fca5fc5f10dc82104ae74a105a7137c1a6723471657eb |
| market_data/decision_context_source_history.json | 01452f0b6605b6a5bbb41aeac7cb0ceae01707a3b50e4e67e8677f110dfd57bb |
| market_data/universe_quality_evidence.md | 9a5c810361acd46195ff712a92d9da3fec28bea41209304e92f94ff15525fbde |
| market_data/universe_quality_evidence.json | ce923c92767a7f877b296afcf6699160d4e64114d8e46691bd329df3597f0a0a |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 3c0b4c1cb23a494fcddf289ba5d11dbfb52f9a0549c507459224b5f1e8021a66 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 11e7d225e63bc14636dd954888b98832a223c0d38eee09db1f4f8083b60638cd | yes |
| Final briefing | research/final_briefing.md | model-facing | 8a76c6e6ce6b3fe08a83e293601adca9ec61fd9fbab061267c7005b07e268e29 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
