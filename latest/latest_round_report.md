# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-08-09-1M
- Decision deadline: 2026-08-10T13:25:00Z
- Horizon: one month
- Official run ID: official-v2-2-all-monthly-20260809-clean
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 4 | 0.57 | SPY has positive broad-market momentum but is already at a record high, so selected active holdings target stronger pullback-plus-trend setups and a distinct oil supply catalyst. The portfolio expected base return is 1.90%, versus a 1.00% SPY base forecast. | A hotter CPI/PPI print or hawkish FOMC/Jackson Hole communication could lift yields and reverse growth, biotech, and semiconductor exposure.; Recent strength in high-beta technology and Taiwan could fail as a crowded rebound trade, causing beta-adjusted underperformance versus SPY.; Resolution of Strait of Hormuz disruptions or weaker demand data could quickly reverse the oil allocation.; The weak July payroll print and large downward revisions could shift markets from soft-landing optimism to growth-scare pricing. |
| openai-gpt-5-6-sol | openai | portfolio | BIOTECH | 4 | 0.56 | SPY enters at a record after a strong week, while weak payrolls and hawkish inflation-policy risks create an uneven benchmark setup. The selected mix targets stronger tactical signals while diversifying technology, healthcare, energy, and currency exposure. | A rapid normalization of Strait of Hormuz oil flows could sharply reverse oil exposure.; Hot inflation or rising long-term yields could pressure biotech and cybersecurity valuations.; Recent high-beta rebounds may reverse after the S&P 500 and Nasdaq's strong entry-week gains.; A dovish policy repricing could weaken the U.S. dollar and offset equity gains. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.65 | A balanced approach targeting high-quality growth sectors (Semiconductors, Biotech) while utilizing Gold as a hedge against geopolitical and economic uncertainty. | A resurgence in inflation could lead to a hawkish Fed surprise, negatively impacting growth sectors.; Geopolitical tensions in the Middle East could escalate, causing broader market volatility.; A sharper-than-expected economic slowdown could hurt semiconductor demand. |
| xai-grok-4-5 | xai | portfolio | SP500 | 3 | 0.58 | SPY base case is modest given record levels and softening payrolls; SEMICONDUCTORS and BIOTECH clear the active hurdle on quality ranks, prior trends, and pullback depth with catalysts before September 10. | Further labor market deterioration from negative payroll revisions; Sticky core inflation delaying any policy easing narrative; Geopolitical oil supply disruption from unresolved Strait of Hormuz; High-volatility reversal in momentum tech/biotech names |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.58 | Overweight semis and software on intact AI-cycle momentum with recent pullback entry, biotech on rate-cut sensitivity and pullback, gold as geopolitical/inflation hedge, 20% SPY core. | Hot July CPI (Aug 12) triggers hawkish repricing hitting high-beta tech and biotech; Fed dissenters gain traction at Jackson Hole, pushing yields higher and hurting gold and duration plays; Semiconductor volatility (55% annualized) can produce large drawdowns in a month; Middle East de-escalation removes gold's geopolitical bid |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.5 | Market is at record highs with soft labor data and sticky inflation; portfolio keeps benchmark beta while adding two uncorrelated alpha sleeves capped well under cluster limits. | Hot July CPI/PPI on Aug 12-13 lifting yields and hitting equities; Gold reversal if the Strait of Hormuz reopens; Biotech's high volatility and factor-reversal risk after a sharp bounce; Further labor-market deterioration triggering a growth scare |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.55 | Weak labor data and revisions favor benchmark exposure only over the one-month window. | Downward payroll revisions may trigger further equity volatility; FOMC uncertainty from Middle East conflict |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.5 | Overweight SPY plus biotech and software tilts that clear the SPY base hurdle, exploiting strong quality-evidence scores while respecting cluster caps. | Hot July CPI on Aug 12 reprices rates and hits high-beta growth/biotech; Middle East oil supply shock triggers broad risk-off; High-beta tech sleeves amplify any market drawdown |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.14 | 18.559999465942383 | 0.3125883639280327 | 1 |
| OIL | Crude Oil | 125.92 | 158.38 | 0.2577827191867852 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 36.23 | 43.68000030517578 | 0.20563070121931504 | 3 |
| BROAD_COMMODITIES | Broad Commodities | 17.83 | 20.05 | 0.12450925406618074 | 4 |
| SOUTH_KOREA | South Korea Equities | 163.12 | 182.78 | 0.1205247670426679 | 5 |
| BRAZIL | Brazil Equities | 35.19 | 38.56 | 0.09576584256891185 | 6 |
| ENERGY | Energy Sector | 60.18 | 64.93 | 0.0789298770355602 | 7 |
| TAIWAN | Taiwan Equities | 102.18 | 108.92 | 0.06596202779408888 | 8 |
| AGRICULTURE | Agriculture Commodities | 27.82 | 29.32 | 0.053918044572250245 | 9 |
| YEN | Japanese Yen | 57.62 | 59.400001525878906 | 0.030892077852809896 | 10 |
| EURO | Euro | 106.51 | 107.12999725341797 | 0.0058210238796165825 | 11 |
| JAPAN | Japan Equities | 96.05 | 96.44 | 0.0040603852160332465 | 12 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 13 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.48 | 91.47 | -0.00010931351115006649 | 14 |
| SOUTH_AFRICA | South Africa Equities | 69.73 | 69.54 | -0.0027247956403269047 | 15 |
| COMMUNICATIONS | Communication Services Sector | 111.83 | 111.5 | -0.0029509076276490465 | 16 |
| US_DOLLAR | US Dollar | 28.14 | 28.03 | -0.003909026297086005 | 17 |
| TIPS | Treasury Inflation-Protected Securities | 106.86 | 106.33 | -0.004959760434212979 | 18 |
| DIVIDEND | US Dividend Equities | 34.19 | 33.99 | -0.005849663644340364 | 19 |
| TECHNOLOGY | Technology Sector | 186.32 | 185.22 | -0.00590382138256762 | 20 |
| EMERGING_MARKETS | Emerging Markets | 60.33 | 59.94 | -0.006464445549477893 | 21 |
| BROAD_AI_TECH | Broad AI Technology | 63.51 | 63.08 | -0.0067705873090851965 | 22 |
| BIOTECH | Biotechnology | 158.03 | 156.82 | -0.0076567740302474485 | 23 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.5 | 71.92 | -0.008000000000000007 | 24 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.48 | 78.62 | -0.010820332159033663 | 25 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.24 | 96.05 | -0.012237762237762184 | 26 |
| MOMENTUM | US Momentum Equities | 307.32 | 303.15 | -0.013568918391253515 | 27 |
| UTILITIES | Utilities Sector | 43.13 | 42.52 | -0.014143287734755372 | 28 |
| GOLD | Gold | 82.51 | 81.27 | -0.015028481396194504 | 29 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.84 | 93.41 | -0.015078026149304202 | 30 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.96 | 104.36 | -0.015100037750094275 | 31 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.92 | 91.48 | -0.01549720189410242 | 32 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.06 | 80.78 | -0.015598342676090726 | 33 |
| SEMICONDUCTORS | Semiconductors | 569.41 | 560.28 | -0.016034140601675406 | 34 |
| FINANCIALS | Financials Sector | 57.81 | 56.87 | -0.016260162601626105 | 35 |
| HEALTHCARE | Healthcare Sector | 168.44 | 165.66 | -0.016504393255758698 | 36 |
| NASDAQ100 | Nasdaq 100 | 720.87 | 708.69 | -0.016896250364143217 | 37 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.76 | 91.18 | -0.017033203967227184 | 38 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.79 | 46.965 | -0.017263025737601967 | 39 |
| LARGE_VALUE | US Large-Cap Value | 258.31 | 253.33 | -0.019279160698385645 | 40 |
| SP500 | S&P 500 | 773.03 | 757.83 | -0.01966288501093094 | 41 |
| CANADA | Canada Equities | 61.5 | 60.29 | -0.01967479674796746 | 42 |
| UNITED_KINGDOM | United Kingdom Equities | 48.49 | 47.53 | -0.01979789647349972 | 43 |
| MEXICO | Mexico Equities | 76.93 | 75.25 | -0.021838034576888155 | 44 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.95 | 83.09 | -0.021895232489699823 | 45 |
| TOTAL_US_MARKET | Total US Stock Market | 381.63 | 373.24 | -0.021984644813038745 | 46 |
| LARGE_GROWTH | US Large-Cap Growth | 124.17 | 121.32 | -0.022952403962309798 | 47 |
| METALS_MINING | Metals and Mining | 117.54 | 114.77 | -0.023566445465373564 | 48 |
| SMALL_VALUE | US Small-Cap Value | 224.29 | 218.97 | -0.023719291988051117 | 49 |
| LOW_VOL | US Low Volatility Equities | 75.7 | 73.67 | -0.026816380449141364 | 50 |
| COPPER | Copper | 40.18 | 39.04 | -0.028372324539571947 | 51 |
| REGIONAL_BANKS | Regional Banks | 76.03 | 73.81 | -0.02919900039458112 | 52 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.85 | 102.72 | -0.029570146433632427 | 53 |
| REAL_ESTATE | Real Estate Sector | 44.4 | 43.05 | -0.030405405405405483 | 54 |
| EUROPE | Europe Equities | 92.26 | 89.42 | -0.030782570995014136 | 55 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.22 | 213.17 | -0.032013441104350226 | 56 |
| SILVER | Silver | 59.41 | 57.5 | -0.03214946978623123 | 57 |
| AUSTRALIA | Australia Equities | 30.05 | 29.08 | -0.0322795341098171 | 58 |
| SOFTWARE | Software | 105.01 | 101.2 | -0.03628225883249214 | 59 |
| INDIA | India Equities | 50.14 | 48.11 | -0.04048663741523739 | 60 |
| SMALL_CAP | US Small-Cap Stocks | 299.98 | 287.7 | -0.04093606240416037 | 61 |
| MATERIALS | Materials Sector | 53.18 | 50.76 | -0.045505829259120056 | 62 |
| MID_CAP | US Mid-Cap Stocks | 77.54 | 73.86 | -0.04745937580603565 | 63 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.89 | 120.49 | -0.057862225349910146 | 64 |
| CYBERSECURITY | Cybersecurity | 100.6 | 94.16 | -0.06401590457256456 | 65 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 119.67 | 111.96 | -0.06442717473050896 | 66 |
| CHINA | China Equities | 56.93 | 52.8 | -0.07254523098542076 | 67 |
| INDUSTRIALS | Industrials Sector | 184.6 | 170.55 | -0.07611050920910067 | 68 |
| SOLAR | Solar Energy | 51.86 | 47.04 | -0.09294253760123405 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 251.13 | 218.32 | -0.13064946442081793 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | portfolio | SEMICONDUCTORS | 4 | 0.57 | -0.016034140601675406 | 0.057222806678026567 | 0.07688569168895751 | 0.2553655572500061 |  | True | True |
| openai-gpt-5-6-sol | portfolio | BIOTECH | 4 | 0.56 | -0.0076567740302474485 | 0.04536286618506372 | 0.06502575119599466 | 0.26722549774296894 |  | True | True |
| google-gemini-3-1-pro | portfolio | SEMICONDUCTORS | 3 | 0.65 | -0.016034140601675406 | -0.01321923286860275 | 0.006443652142328192 | 0.32580759679663546 |  | True | False |
| xai-grok-4-5 | portfolio | SP500 | 3 | 0.58 | -0.01966288501093094 | -0.014972428393949234 | 0.004690456616981708 | 0.32756079232198193 |  | True | False |
| anthropic-claude-fable-5 | portfolio | SEMICONDUCTORS | 5 | 0.58 | -0.016034140601675406 | -0.01792050206276725 | 0.0017423829481636906 | 0.3305088659907999 |  | True | False |
| anthropic-claude-opus-5 | portfolio | SP500 | 4 | 0.5 | -0.01966288501093094 | -0.018804893310530812 | 0.0008579917004001292 | 0.3313932572385635 |  | True | False |
| xai-grok-4-3 | portfolio | SP500 | 1 | 0.55 | -0.01966288501093094 | -0.01966288501093094 | 0.0 | 0.33225124893896363 |  | False | False |
| anthropic-claude-opus-4-8 | portfolio | SP500 | 3 | 0.5 | -0.01966288501093094 | -0.021647169412228426 | -0.001984284401297484 | 0.3342355333402611 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1M has no scored official run.
- Round CB-2026-08-11-1M has no scored official run.
- Round CB-2026-08-13-1M has no scored official run.
- Round CB-2026-08-15-1M has no scored official run.
- Round CB-2026-08-18-1M has no scored official run.
- Round CB-2026-08-19-1M has no scored official run.
- Round CB-2026-08-20-1M has no scored official run.
- Round CB-2026-08-21-1M has no scored official run.
- Round CB-2026-08-23-1M has no scored official run.
- Round CB-2026-08-24-1M has no scored official run.
- Round CB-2026-08-25-1M has no scored official run.
- Round CB-2026-08-26-1M has no scored official run.
- Round CB-2026-08-27-1M has no scored official run.
- Round CB-2026-08-30-1M has no scored official run.
- Round CB-2026-09-01-1M has no scored official run.
- Round CB-2026-09-02-1M has no scored official run.
- Round CB-2026-09-03-1M has no scored official run.
- Round CB-2026-09-04-1M has no scored official run.
- Round CB-2026-09-09-1M has no scored official run.
- Round CB-2026-09-10-1M has no scored official run.
- Round CB-2026-09-11-1M has no scored official run.
- Round example-round has no scored official run.
- Round example-round-2 has no scored official run.
