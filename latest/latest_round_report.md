# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-30-1M
- Decision deadline: 2026-07-31T12:30:00Z
- Horizon: one month
- Official run ID: official-v2-2-all-monthly-20260730
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | SOFTWARE | 4 | 0.58 | Selected holdings clear the active hurdle with higher base forecasts driven by recent earnings, breadth and international relative strength. Allocations stay within cluster caps and sum to 100% for one-month alpha versus SPY. | Elevated inflation prints (CPI/PPI Aug 12-13) or hawkish Fed minutes could pressure equities broadly; Growth-stock reversal after mega-cap earnings if guidance disappoints or Nvidia Aug 26 weakens tech; USD strength or European data miss reversing international allocation; Sudden risk-off move favoring pure SPY concentration over equal-weight and sector tilts |
| openai-gpt-5-6-sol | openai | portfolio | EQUAL_WEIGHT_SP500 | 4 | 0.59 | Favor broadening participation and selective rebound candidates rather than chasing the most volatile recent winners. The yen reduces dependence on a single US equity outcome. | A renewed mega-cap rally could cause equal-weight equities to lag SPY.; Hot August inflation or rising long yields could pressure biotechnology and growth equities.; Cybersecurity's elevated volatility could overwhelm its trend support.; A widening US-Japan rate differential could reverse the yen rally. |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | A balanced approach combining core S&P 500 exposure with overweights in Financials and Healthcare to capture upside while mitigating volatility. | Inflation re-accelerating, forcing the Fed to hike rates.; Mega-cap tech earnings disappointing, dragging down the broader market.; A sudden deterioration in credit conditions impacting Financials. |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.55 | Selected holdings with base forecasts exceeding SPY while respecting cluster caps and allocation rules. | Elevated inflation readings could pressure equities; Labor market softening may trigger risk-off rotation; Volatility in growth-sensitive sectors |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.53 | Breadth is improving (positive asset share 68% over 5 sessions, RSP beating SPY) while high-beta AI leadership has sharply reversed. We hold SPY as core and add lower-volatility, positive-trend exposures. | Hot July CPI on Aug 12 lifting yields and pressuring all equity exposure; Nvidia results Aug 26 re-igniting mega-cap tech leadership and causing SPY to outrun our diversifiers; Labor-market deterioration (payrolls 57k, downward revisions) hitting cyclicals and financials; Hawkish FOMC minutes given three members favored a hike |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 4 | 0.55 | Overweight value/breadth themes with strong recent active returns and low drawdown, anchored by SPY, avoiding overextended semis and momentum. | Mega-cap tech re-accelerates after strong earnings (MSFT, Amazon), pulling SPY above value tilts; Hot August CPI drives yields higher, hurting rate-sensitive financials and dividend names; Broadening rotation reverses and concentration resumes |
| anthropic-claude-fable-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.58 | Breadth is rotating away from cap-weighted mega-cap concentration while AI capex remains robust; semis' -17% active pullback into Nvidia's Aug 26 report offers asymmetric upside, funded by resilient value/financials/equal-weight sleeves. | Nvidia guidance disappointment could send SMH sharply lower given 55% volatility; Hot July CPI (Aug 12) with three FOMC dissenters favoring hikes could hit all equities; Breadth rotation could reverse, with mega-cap growth reasserting leadership over RSP/value; Payroll weakness (57k June, negative revisions) could morph into growth-scare selloff |
| openai-gpt-5-5 | openai | portfolio | EQUAL_WEIGHT_SP500 | 4 | 0.55 | Base case expects modest positive alpha from continued breadth and selected sector/international relative strength through the one-month macro-event window. The allocation avoids overconcentration in technology despite strong single-day mega-cap earnings reactions because volatility and drawdowns are elevated there. | A renewed mega-cap technology rally could cause cap-weighted SPY to outperform diversified and defensive tilts.; Hot July inflation data or hawkish Fed minutes could pressure equities and financials.; Weak labor data or deteriorating loan conditions could reverse cyclicals and regional breadth.; International equity exposure could lag if the U.S. dollar strengthens or European inflation surprises negatively. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.510000228881836 | 18.37 | 0.26602341214543346 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 36.70000076293945 | 43.9 | 0.19618526123659596 | 2 |
| SOFTWARE | Software | 93.30999755859375 | 109.5 | 0.1735076933341444 | 3 |
| METALS_MINING | Metals and Mining | 101.86000061035156 | 118.74 | 0.16571764469372097 | 4 |
| TAIWAN | Taiwan Equities | 94.0 | 107.9 | 0.147872340425532 | 5 |
| SILVER | Silver | 53.5 | 60.02 | 0.1218691588785048 | 6 |
| SOUTH_KOREA | South Korea Equities | 161.2100067138672 | 180.2 | 0.11779661618548465 | 7 |
| SOUTH_AFRICA | South Africa Equities | 64.11000061035156 | 70.72 | 0.10310402942939834 | 8 |
| CYBERSECURITY | Cybersecurity | 90.0199966430664 | 98.56 | 0.09486784798265568 | 9 |
| BROAD_AI_TECH | Broad AI Technology | 58.689998626708984 | 64.22 | 0.09422391383008799 | 10 |
| GOLD | Gold | 77.30000305175781 | 83.82 | 0.0843466583549366 | 11 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 113.9800033569336 | 122.32 | 0.0731707001003441 | 12 |
| BIOTECH | Biotechnology | 151.4600067138672 | 162.38 | 0.07209819623712588 | 13 |
| ENERGY | Energy Sector | 58.959999084472656 | 62.68 | 0.06309363930276968 | 14 |
| AGRICULTURE | Agriculture Commodities | 27.479999542236328 | 29.19 | 0.06222709193045772 | 15 |
| COMMUNICATIONS | Communication Services Sector | 106.58000183105469 | 112.99 | 0.06014259766204666 | 16 |
| TECHNOLOGY | Technology Sector | 175.72999572753906 | 185.69 | 0.05667788376836613 | 17 |
| BROAD_COMMODITIES | Broad Commodities | 17.5 | 18.39 | 0.050857142857142934 | 18 |
| NASDAQ100 | Nasdaq 100 | 683.5499877929688 | 716.43 | 0.048101840091012926 | 19 |
| HEALTHCARE | Healthcare Sector | 163.52000427246094 | 171.16 | 0.04672208615411422 | 20 |
| LARGE_GROWTH | US Large-Cap Growth | 117.43000030517578 | 122.75 | 0.04530358239801302 | 21 |
| EMERGING_MARKETS | Emerging Markets | 58.189998626708984 | 60.79 | 0.044681241358504264 | 22 |
| DIVIDEND | US Dividend Equities | 33.40999984741211 | 34.9 | 0.044597430691197815 | 23 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.38999938964844 | 117.21 | 0.042886383455176924 | 24 |
| SP500 | S&P 500 | 741.6900024414062 | 769.35 | 0.03729320533854552 | 25 |
| TOTAL_US_MARKET | Total US Stock Market | 366.2699890136719 | 379.36 | 0.035738693802291 | 26 |
| CANADA | Canada Equities | 59.790000915527344 | 61.73 | 0.03244688166527254 | 27 |
| LARGE_VALUE | US Large-Cap Value | 250.7100067138672 | 258.33 | 0.030393654349941457 | 28 |
| MATERIALS | Materials Sector | 51.63999938964844 | 53.18 | 0.029821855703977107 | 29 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.08999633789062 | 73.06 | 0.02771140474879119 | 30 |
| JAPAN | Japan Equities | 93.29000091552734 | 95.87 | 0.02765568720284195 | 31 |
| SEMICONDUCTORS | Semiconductors | 538.9000244140625 | 553.11 | 0.026368481985852288 | 32 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.3800048828125 | 220.69 | 0.024654076501096966 | 33 |
| FINANCIALS | Financials Sector | 57.0 | 58.1 | 0.019298245614035148 | 34 |
| OIL | Crude Oil | 127.4800033569336 | 129.7 | 0.0174144695999936 | 35 |
| EUROPE | Europe Equities | 90.98999786376953 | 91.98 | 0.010880340251383513 | 36 |
| SMALL_CAP | US Small-Cap Stocks | 292.5899963378906 | 295.75 | 0.0108001083484075 | 37 |
| COPPER | Copper | 39.34000015258789 | 39.67 | 0.008388404833048924 | 38 |
| SMALL_VALUE | US Small-Cap Value | 221.7899932861328 | 223.14 | 0.00608686935720093 | 39 |
| AUSTRALIA | Australia Equities | 29.81999969482422 | 30.0 | 0.006036227599526933 | 40 |
| MID_CAP | US Mid-Cap Stocks | 75.3499984741211 | 75.76 | 0.005441294415151621 | 41 |
| EURO | Euro | 106.47000122070312 | 106.978 | 0.004771285559054705 | 42 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.47000122070312 | 79.74 | 0.003397493081030989 | 43 |
| MOMENTUM | US Momentum Equities | 298.7699890136719 | 299.71 | 0.003146269775727406 | 44 |
| US_DOLLAR | US Dollar | 28.139999389648438 | 28.18 | 0.001421485828684066 | 45 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.79000091552734 | 94.89 | 0.0010549539350861448 | 46 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.80000305175781 | 82.88 | 0.0009661466822914466 | 47 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 48 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.6500015258789 | 91.65 | -1.6648978418132288e-08 | 49 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.47000122070312 | 85.45 | -0.00023401451289883912 | 50 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.41000366210938 | 106.35 | -0.0005638911760581511 | 51 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.29000091552734 | 93.17 | -0.0012863213029229437 | 52 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.62000274658203 | 97.49 | -0.0013317224229086877 | 53 |
| UNITED_KINGDOM | United Kingdom Equities | 48.68000030517578 | 48.55 | -0.002670507484815343 | 54 |
| INDIA | India Equities | 49.70000076293945 | 49.56 | -0.0028169167161028463 | 55 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.20999908447266 | 92.85 | -0.003862236755805659 | 56 |
| CHINA | China Equities | 55.5 | 55.23 | -0.004864864864864926 | 57 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.76000213623047 | 105.22 | -0.005105920247003071 | 58 |
| YEN | Japanese Yen | 57.58000183105469 | 57.25 | -0.005731188269547882 | 59 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.880001068115234 | 47.6 | -0.005847975394087768 | 60 |
| INDUSTRIALS | Industrials Sector | 178.38999938964844 | 177.14 | -0.0070071158356704855 | 61 |
| TIPS | Treasury Inflation-Protected Securities | 107.73999786376953 | 106.94 | -0.0074252634084982505 | 62 |
| MEXICO | Mexico Equities | 77.11000061035156 | 76.48 | -0.00817015439456481 | 63 |
| LOW_VOL | US Low Volatility Equities | 76.37999725341797 | 75.08 | -0.0170201269987581 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.29999923706055 | 44.48 | -0.018101528716797377 | 65 |
| REGIONAL_BANKS | Regional Banks | 75.9000015258789 | 74.3 | -0.021080388586466214 | 66 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 238.1300048828125 | 232.82 | -0.022298764430906726 | 67 |
| SOLAR | Solar Energy | 49.84000015258789 | 48.65 | -0.023876407482837925 | 68 |
| BRAZIL | Brazil Equities | 36.529998779296875 | 35.55 | -0.026827232741444385 | 69 |
| UTILITIES | Utilities Sector | 44.65999984741211 | 42.73 | -0.04321540201536633 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | portfolio | SOFTWARE | 4 | 0.58 | 0.1735076933341444 | 0.07239134587660233 | 0.03509814053805681 | 0.19363206626883112 |  | True | True |
| openai-gpt-5-6-sol | portfolio | EQUAL_WEIGHT_SP500 | 4 | 0.59 | 0.024654076501096966 | 0.050649242177173634 | 0.013356036838628113 | 0.2153741699682598 |  | True | True |
| google-gemini-3-1-pro | portfolio | SP500 | 3 | 0.65 | 0.03729320533854552 | 0.034723381665863015 | -0.0025698236726825058 | 0.23130003047957043 |  | False | True |
| xai-grok-4-3 | portfolio | SP500 | 4 | 0.55 | 0.03729320533854552 | 0.03420007935903638 | -0.0030931259795091426 | 0.23182333278639708 |  | False | True |
| anthropic-claude-opus-5 | portfolio | SP500 | 4 | 0.53 | 0.03729320533854552 | 0.03194876330661661 | -0.005344442031928909 | 0.23407464883881685 |  | False | True |
| anthropic-claude-opus-4-8 | portfolio | FINANCIALS | 4 | 0.55 | 0.019298245614035148 | 0.030560991549993345 | -0.006732213788552176 | 0.23546242059544012 |  | False | True |
| anthropic-claude-fable-5 | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.58 | 0.024654076501096966 | 0.026691131692740278 | -0.010602073645805243 | 0.23933228045269317 |  | False | True |
| openai-gpt-5-5 | portfolio | EQUAL_WEIGHT_SP500 | 4 | 0.55 | 0.024654076501096966 | 0.024973973459992273 | -0.012319231878553247 | 0.24104943868544118 |  | False | True |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1M has no scored official run.
- Round CB-2026-07-31-1M has no scored official run.
- Round CB-2026-08-04-1M has no scored official run.
- Round CB-2026-08-05-1M has no scored official run.
- Round CB-2026-08-07-1M has no scored official run.
- Round CB-2026-08-09-1M has no scored official run.
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
- Round example-round has no scored official run.
- Round example-round-2 has no scored official run.
