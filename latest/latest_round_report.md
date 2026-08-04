# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-27-1W
- Decision deadline: 2026-07-28T12:30:00Z
- Horizon: one week
- Official run ID: official-v2-2-all-weekly-20260727-clean
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.52 | SP500 base forecast 0.5; selected holdings exceed that threshold with diversified clusters under 50% cap. | FOMC outcome volatility on July 29; Q2 GDP surprise on July 30; Sector rotation away from value and healthcare |
| openai-gpt-5-6-sol | openai | portfolio | HEALTHCARE | 4 | 0.59 | Each active holding has a base forecast above SPY's 0.30% forecast. The weighted base return is 0.73%, implying 0.43 percentage point expected alpha. | A hawkish FOMC surprise could pressure equities and reverse the recent decline in Treasury yields.; Weak GDP or labor-cost data could hurt financials and broad cyclical participation.; Mega-cap earnings disappointments could overwhelm breadth and drag cybersecurity lower.; Recent healthcare and equal-weight strength could mean-revert during a technology-led rebound. |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.6 | Balanced approach with defensive and cyclical tilts. | Hawkish Fed surprise; Tech earnings disappointment; Weak GDP data |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.6 | Overweight defensive value and breadth (healthcare, dividend, equal-weight, financials) into a hawkish-risk FOMC and concentrated mega-cap earnings week; small SPY anchor. | Dovish FOMC plus strong mega-cap earnings could reignite growth leadership and hurt the value/defensive tilt; A 25bp hike could pressure all equities including defensives; Financials exposed to weak Senior Loan Officer Survey or credit deterioration; Healthcare's recent strength may mean-revert |
| xai-grok-4-5 | xai | portfolio | HEALTHCARE | 4 | 0.58 | SPY base is modest given recent negative 5-session return and mega-cap drag; selected names show superior recent active returns, shallower relative drawdowns in several cases, and catalysts (FOMC, GDP, earnings) that can sustain rotation. Allocations stay diversified across four clusters. | Hawkish FOMC or hot PCE/GDP triggering rates spike and equity drawdown; Mega-cap earnings disappointment cascading into broader risk-off; Reversal of recent value/defensive/industrial leadership back to growth; Geopolitical re-escalation affecting energy and risk assets |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Breadth is rotating away from mega-cap growth (RSP beating SPY) into defensives and cyclicals; portfolio overweights those leaders while keeping SPY core. | Hawkish FOMC surprise (38% priced hike) hits all equities; Strong Microsoft/Meta/Apple/Amazon earnings drive tech-led rally that leaves defensive tilt behind; Yield spike pressures rate-sensitive and financial names |
| anthropic-claude-opus-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.55 | Broadening-breadth tilt: RSP, XLV, XLF, SCHD plus gold hedge, avoiding concentrated mega-cap tech risk into FOMC and megacap earnings. | A dovish FOMC or blowout mega-cap earnings could drive a cap-weighted melt-up that RSP and defensives lag; A 25bp hike surprise (38% priced) hits rate-sensitive defensives and gold simultaneously; Oil's 7% slide and unresolved US-Iran talks could spark cross-asset volatility; Defensive sectors near 52-week highs are crowded and prone to mean reversion |
| openai-gpt-5-5 | openai | portfolio | HEALTHCARE | 4 | 0.56 | SPY was flat with mixed mega-cap technology weakness, while breadth was positive and several defensive/value sectors led. The selected holdings seek one-week alpha from breadth continuation, defensive rotation, and financial leadership around scheduled macro and policy catalysts. | Mega-cap technology earnings could strongly lift SPY and leave the defensive/breadth tilt behind.; A hawkish FOMC surprise or hot inflation/wage data could pressure equities and financials simultaneously.; Recent defensive and equal-weight outperformance could mean-revert within the short one-week window.; Unexpected geopolitical or oil-price reversal could shift leadership toward energy and away from selected sectors. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOFTWARE | Software | 90.91 | 97.42 | 0.07160928390716093 | 1 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 110.84 | 118.21 | 0.06649224106820628 | 2 |
| CYBERSECURITY | Cybersecurity | 89.1 | 93.91 | 0.053984287317620616 | 3 |
| YEN | Japanese Yen | 56.01 | 58.5 | 0.04445634708087853 | 4 |
| BROAD_AI_TECH | Broad AI Technology | 58.3 | 60.57 | 0.03893653516295026 | 5 |
| SOUTH_AFRICA | South Africa Equities | 61.94 | 64.33 | 0.03858572812399097 | 6 |
| COMMUNICATIONS | Communication Services Sector | 107.66 | 111.34 | 0.0341816830763515 | 7 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 114.87 | 118.62 | 0.03264559937320444 | 8 |
| LARGE_GROWTH | US Large-Cap Growth | 117.13 | 120.87 | 0.0319303338171264 | 9 |
| CHINA | China Equities | 54.26 | 55.9 | 0.030224843346848607 | 10 |
| NASDAQ100 | Nasdaq 100 | 682.12 | 700.07 | 0.026315017885416125 | 11 |
| INDIA | India Equities | 48.89 | 50.16 | 0.025976682348128444 | 12 |
| SP500 | S&P 500 | 739.09 | 757.67 | 0.02513902231122045 | 13 |
| TOTAL_US_MARKET | Total US Stock Market | 365.18 | 373.84 | 0.023714332657867265 | 14 |
| EUROPE | Europe Equities | 88.84 | 90.93 | 0.023525438991445435 | 15 |
| COPPER | Copper | 38.77 | 39.64 | 0.02244003095176672 | 16 |
| TECHNOLOGY | Technology Sector | 174.3 | 178.04 | 0.0214572576018357 | 17 |
| REGIONAL_BANKS | Regional Banks | 75.52 | 77.06 | 0.020391949152542388 | 18 |
| UNITED_KINGDOM | United Kingdom Equities | 47.37 | 48.23 | 0.01815495039054249 | 19 |
| LARGE_VALUE | US Large-Cap Value | 249.74 | 254.24 | 0.018018739489068736 | 20 |
| AUSTRALIA | Australia Equities | 28.88 | 29.4 | 0.018005540166204925 | 21 |
| BRAZIL | Brazil Equities | 35.87 | 36.42 | 0.01533314747700043 | 22 |
| JAPAN | Japan Equities | 91.51 | 92.91 | 0.015298874439951815 | 23 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.0 | 71.04 | 0.014857142857142902 | 24 |
| EMERGING_MARKETS | Emerging Markets | 58.23 | 59.06 | 0.014253821054439397 | 25 |
| EURO | Euro | 104.8682306291 | 106.19 | 0.012604097189117924 | 26 |
| SMALL_CAP | US Small-Cap Stocks | 292.91 | 296.22 | 0.011300399440101083 | 27 |
| SMALL_VALUE | US Small-Cap Value | 222.16 | 224.45 | 0.010307886208138273 | 28 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.18 | 217.11 | 0.008969235059020475 | 29 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 243.91 | 246.08 | 0.008896724201549855 | 30 |
| FINANCIALS | Financials Sector | 56.88 | 57.38 | 0.008790436005625901 | 31 |
| ENERGY | Energy Sector | 58.36 | 58.79 | 0.007368060315284364 | 32 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 27.79 | 0.0061549601737871384 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.8877569383 | 79.31 | 0.005352453639038579 | 34 |
| CANADA | Canada Equities | 59.39 | 59.65 | 0.004377841387438908 | 35 |
| DIVIDEND | US Dividend Equities | 33.43 | 33.56 | 0.0038887227041579653 | 36 |
| TIPS | Treasury Inflation-Protected Securities | 106.6074696475 | 106.86 | 0.0023687866650901057 | 37 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.5472968085 | 94.75 | 0.0021439342883653456 | 38 |
| TAIWAN | Taiwan Equities | 97.81 | 97.98 | 0.001738063592679806 | 39 |
| MID_CAP | US Mid-Cap Stocks | 76.0 | 76.11 | 0.0014473684210525306 | 40 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.8015951291 | 47.84 | 0.000803422371079554 | 41 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3472661601 | 91.42 | 0.0007962344463874338 | 42 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.0526742032 | 106.11 | 0.0005405407947578489 | 43 |
| MEXICO | Mexico Equities | 76.54 | 76.55 | 0.00013065064018791261 | 44 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 45 |
| METALS_MINING | Metals and Mining | 103.11 | 103.11 | 0.0 | 45 |
| INDUSTRIALS | Industrials Sector | 183.2 | 183.16 | -0.00021834061135361793 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.5135295166 | 105.45 | -0.0006020982985883716 | 48 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.3521122985 | 97.26 | -0.0009461766809698569 | 49 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.9619653186 | 92.82 | -0.001527133361622246 | 50 |
| MOMENTUM | US Momentum Equities | 302.33 | 301.78 | -0.0018192041808620107 | 51 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.0275318635 | 92.72 | -0.0033058155724398075 | 52 |
| BROAD_COMMODITIES | Broad Commodities | 17.34 | 17.25 | -0.00519031141868509 | 53 |
| SEMICONDUCTORS | Semiconductors | 548.55 | 545.46 | -0.005633032540333427 | 54 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.36 | 84.86 | -0.005857544517338331 | 55 |
| SOUTH_KOREA | South Korea Equities | 161.2 | 160.24 | -0.005955334987592931 | 56 |
| SOLAR | Solar Energy | 51.56 | 51.24 | -0.006206361520558534 | 57 |
| HEALTHCARE | Healthcare Sector | 163.4 | 162.24 | -0.007099143206854341 | 58 |
| MATERIALS | Materials Sector | 51.39 | 51.01 | -0.00739443471492518 | 59 |
| GOLD | Gold | 76.78 | 76.19 | -0.007684292784579383 | 60 |
| SILVER | Silver | 52.93 | 52.46 | -0.008879652371056146 | 61 |
| REAL_ESTATE | Real Estate Sector | 45.76 | 45.18 | -0.0126748251748251 | 62 |
| LOW_VOL | US Low Volatility Equities | 77.22 | 76.21 | -0.013079513079513161 | 63 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.4146222705 | 82.19 | -0.014681146268681222 | 64 |
| US_DOLLAR | US Dollar | 28.6 | 28.17 | -0.015034965034965042 | 65 |
| BITCOIN_ETF | Bitcoin ETF | 36.77 | 36.16 | -0.01658961109600232 | 66 |
| OIL | Crude Oil | 124.76 | 122.12 | -0.021160628406540538 | 67 |
| BIOTECH | Biotechnology | 150.59 | 147.31 | -0.021780994753967775 | 68 |
| UTILITIES | Utilities Sector | 45.68 | 44.36 | -0.02889667250437833 | 69 |
| ETHEREUM_ETF | Ethereum ETF | 14.71 | 14.11 | -0.04078857919782475 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | portfolio | SP500 | 4 | 0.52 | 0.02513902231122045 | 0.013997615382056242 | -0.011141406929164207 | 0.05761166852510469 |  | False | True |
| openai-gpt-5-6-sol | portfolio | HEALTHCARE | 4 | 0.59 | -0.007099143206854341 | 0.013107032267629416 | -0.012031990043591033 | 0.05850225163953151 |  | False | True |
| google-gemini-3-1-pro | portfolio | SP500 | 3 | 0.6 | 0.02513902231122045 | 0.010740140201058235 | -0.014398882110162214 | 0.06086914370610269 |  | False | True |
| anthropic-claude-fable-5 | portfolio | HEALTHCARE | 5 | 0.6 | -0.007099143206854341 | 0.005517256936120352 | -0.019621765375100096 | 0.06609202697104058 |  | False | True |
| xai-grok-4-5 | portfolio | HEALTHCARE | 4 | 0.58 | -0.007099143206854341 | 0.004085894101541732 | -0.021053128209678716 | 0.0675233898056192 |  | False | True |
| anthropic-claude-opus-4-8 | portfolio | HEALTHCARE | 5 | 0.55 | -0.007099143206854341 | 0.0026709697229762137 | -0.022468052588244237 | 0.06893831418418471 |  | False | True |
| anthropic-claude-opus-5 | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.55 | 0.008969235059020475 | 0.002459693565397242 | -0.022679328745823207 | 0.06914959034176368 |  | False | True |
| openai-gpt-5-5 | portfolio | HEALTHCARE | 4 | 0.56 | -0.007099143206854341 | 0.0011386659006376255 | -0.024000356410582825 | 0.0704706180065233 |  | False | True |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1W has no scored official run.
- Round CB-2026-07-28-1W has no scored official run.
- Round CB-2026-07-29-1W has no scored official run.
- Round CB-2026-07-30-1W has no scored official run.
- Round CB-2026-07-31-1W has no scored official run.
