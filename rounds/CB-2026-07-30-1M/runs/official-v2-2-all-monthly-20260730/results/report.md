# CapitalBench Report: CB-2026-07-30-1M / official-v2-2-all-monthly-20260730

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260730
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-30-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-30
- Decision deadline: 2026-07-31T12:30:00Z
- Horizon: one month
- Entry date: 2026-07-30
- Exit date: 2026-08-28
- Entry rule: Use the Thursday, July 30, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Friday, August 28, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

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

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 25.0 | 0.026368481985852288 | 0.006592120496463072 | Strongest prior trend (+49.5% prior active) with deep -17% recent pullback into Nvidia results Aug 26; strong AI capex confirmation from Microsoft, Amazon, Meta guidance. |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 30.0 | 0.024654076501096966 | 0.00739622295032909 | Breadth broadening: RSP beat SPY +1.16% (5d) and +1.91% (21d) with lowest equity volatility (11.2%) and shallow drawdown. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | 0.030393654349941457 | 0.0060787308699882915 | +4.1% 21d active return, near 52-week high, low volatility (12.2%) and shallow -2.4% drawdown; benefits from sticky-inflation, higher-yield regime. |
| anthropic-claude-fable-5 | FINANCIALS | 15.0 | 0.019298245614035148 | 0.002894736842105272 | +7.0% 21d active return, only -1.0% off 52-week high, steepening curve (30y 5.22%) supports banks. |
| anthropic-claude-fable-5 | SP500 | 10.0 | 0.03729320533854552 | 0.003729320533854552 | Benchmark ballast at record-adjacent levels with solid mega-cap earnings. |
| anthropic-claude-opus-4-8 | FINANCIALS | 30.0 | 0.019298245614035148 | 0.005789473684210544 | Strong 21-day active return (+7.0%), low drawdown, deep recent pullback rank suggests continued broadening leadership with steepening curve. |
| anthropic-claude-opus-4-8 | DIVIDEND | 25.0 | 0.044597430691197815 | 0.011149357672799454 | Defensive dividend equity with strongest 21-day active return (+6.0%), low beta 0.26, minimal drawdown; benefits from broadening rally away from mega-cap tech. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 25.0 | 0.024654076501096966 | 0.006163519125274242 | Equal-weight outperforming cap-weight (rsp_minus_spy_21s +1.91%), lowest volatility and drawdown; captures market breadth improvement. |
| anthropic-claude-opus-4-8 | SP500 | 20.0 | 0.03729320533854552 | 0.007458641067709104 | Core benchmark anchor providing broad large-cap exposure at recovery highs. |
| anthropic-claude-opus-5 | SP500 | 40.0 | 0.03729320533854552 | 0.014917282135418208 | Core benchmark exposure amid strong mega-cap earnings (Microsoft, Apple, Amazon beats) and Nvidia catalyst Aug 26. |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.024654076501096966 | 0.006163519125274242 | Broadening breadth: RSP beating SPY on 5- and 21-session windows with lowest volatility and shallow drawdown. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | 0.019298245614035148 | 0.00385964912280703 | Strong 21-session active return (+7.0%), low volatility, minimal drawdown, near 52-week high, steep curve with 30-year at 5.22%. |
| anthropic-claude-opus-5 | HEALTHCARE | 15.0 | 0.04672208615411422 | 0.007008312923117132 | Defensive diversifier with positive 21-session active return, shallowest drawdown (-3.7%) and low SPY beta. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.03729320533854552 | 0.014917282135418208 | Core holding providing broad US equity exposure amid solid economic activity and resilient mega-cap tech earnings. |
| google-gemini-3-1-pro | FINANCIALS | 30.0 | 0.019298245614035148 | 0.005789473684210544 | Benefiting from a stable rate environment and solid economic growth, with strong recent momentum. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.04672208615411422 | 0.014016625846234265 | Defensive growth characteristics offer a buffer against potential volatility while maintaining upside potential. |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 35.0 | 0.024654076501096966 | 0.008628926775383938 | Equal-weight S&P 500 has better near-term breadth than cap-weighted SPY, with positive 5-session and 21-session relative returns, lower volatility, and a shallower drawdown. |
| openai-gpt-5-5 | FINANCIALS | 25.0 | 0.019298245614035148 | 0.004824561403508787 | Financials show strong 21-session active return, moderate volatility, shallow drawdown, and benefit if solid activity and resilient consumer data outweigh rate and credit concerns. |
| openai-gpt-5-5 | EUROPE | 20.0 | 0.010880340251383513 | 0.0021760680502767027 | Europe has positive recent absolute and active performance, a 52-week-high reading, and ECB policy is on hold with inflation data scheduled immediately after cutoff. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | 0.04672208615411422 | 0.009344417230822844 | Healthcare offers lower beta diversification with positive recent active performance and a shallow drawdown, which can help if macro releases challenge higher-beta cyclicals. |
| openai-gpt-5-6-sol | EQUAL_WEIGHT_SP500 | 35.0 | 0.024654076501096966 | 0.008628926775383938 | Broadening participation, positive benchmark-relative returns, and lower volatility support continued outperformance versus cap-weighted SPY. |
| openai-gpt-5-6-sol | CYBERSECURITY | 30.0 | 0.09486784798265568 | 0.028460354394796702 | Strong prior relative trend and a recent positive active return provide a less concentrated technology-growth opportunity. |
| openai-gpt-5-6-sol | BIOTECH | 20.0 | 0.07209819623712588 | 0.014419639247425176 | Strong prior active performance and a recent relative pullback create a tactical rebound setup outside technology. |
| openai-gpt-5-6-sol | YEN | 15.0 | -0.005731188269547882 | -0.0008596782404321823 | Recent strength, low equity correlation, and a dissenting BOJ vote support a modest diversifying allocation. |
| xai-grok-4-3 | SP500 | 40.0 | 0.03729320533854552 | 0.014917282135418208 | Broad diversified US equity exposure with solid recent recovery and scheduled data releases. |
| xai-grok-4-3 | LARGE_VALUE | 20.0 | 0.030393654349941457 | 0.0060787308699882915 | Value tilt shows stronger recent relative performance and lower drawdown. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.019298245614035148 | 0.00385964912280703 | Financials exhibit positive active return and quality evidence support. |
| xai-grok-4-3 | HEALTHCARE | 20.0 | 0.04672208615411422 | 0.009344417230822844 | Healthcare provides defensive balance with moderate quality score. |
| xai-grok-4-5 | SOFTWARE | 35.0 | 0.1735076933341444 | 0.060727692666950536 | Strong recent software rebound and mega-cap cloud/software earnings support higher base return than SPY over the one-month window. |
| xai-grok-4-5 | FINANCIALS | 30.0 | 0.019298245614035148 | 0.005789473684210544 | Positive active returns, solid relative strength, and stable rates backdrop favor financials outperformance versus SPY base case. |
| xai-grok-4-5 | EUROPE | 20.0 | 0.010880340251383513 | 0.0021760680502767027 | Recent outperformance, zero distance to 52w high, and ECB hold provide edge over SPY base for the scoring window. |
| xai-grok-4-5 | EQUAL_WEIGHT_SP500 | 15.0 | 0.024654076501096966 | 0.003698111475164545 | Breadth improvement and lower concentration risk with positive active 21s return support modest edge to cap-weighted SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | SOFTWARE | 4 | 0.58 | 0.1735076933341444 | 0.07239134587660233 | 0.03509814053805681 | 0.19363206626883112 |  | True | True |
| openai-gpt-5-6-sol | EQUAL_WEIGHT_SP500 | 4 | 0.59 | 0.024654076501096966 | 0.050649242177173634 | 0.013356036838628113 | 0.2153741699682598 |  | True | True |
| google-gemini-3-1-pro | SP500 | 3 | 0.65 | 0.03729320533854552 | 0.034723381665863015 | -0.0025698236726825058 | 0.23130003047957043 |  | False | True |
| xai-grok-4-3 | SP500 | 4 | 0.55 | 0.03729320533854552 | 0.03420007935903638 | -0.0030931259795091426 | 0.23182333278639708 |  | False | True |
| anthropic-claude-opus-5 | SP500 | 4 | 0.53 | 0.03729320533854552 | 0.03194876330661661 | -0.005344442031928909 | 0.23407464883881685 |  | False | True |
| anthropic-claude-opus-4-8 | FINANCIALS | 4 | 0.55 | 0.019298245614035148 | 0.030560991549993345 | -0.006732213788552176 | 0.23546242059544012 |  | False | True |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 5 | 0.58 | 0.024654076501096966 | 0.026691131692740278 | -0.010602073645805243 | 0.23933228045269317 |  | False | True |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 4 | 0.55 | 0.024654076501096966 | 0.024973973459992273 | -0.012319231878553247 | 0.24104943868544118 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 2bbb950ee42704752b3e45a09db9712d67a1126f5ad90eb27fa6874876298234 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | edae737f9e107be9ed97b403113a3c727ce199f62a13ebc3385a2647dd09ccf7 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | f39620ac63afc14e61d4a7d41c8adea0528ee9c8366fc2969b24a88c1ea89444 |
| market_data/universe_decision_context.md | e2a588184058e65082c1b5ce7669cd8712a9d0081452e9fe847907158b6c8e79 |
| market_data/universe_decision_context.json | 2e625f61322ee021c62e2a225483beb1ad13cc174ca65ab454a54afe1c05fc19 |
| market_data/decision_context_source_history.json | b9fdda7aff8bda97fcd68ebed7c5bce7771cbaf96d0cc25da9f59af37441381d |
| market_data/universe_quality_evidence.md | 2f5bdef255cfa69d8bb497339083183ec2aae6420ecf96a6492fa656152e9650 |
| market_data/universe_quality_evidence.json | d58bf57d814e4229743952064956e145acfd7a257f6df1d0948076014d93a6be |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a15a0a36c3925c4f53cd8baad0484ebded55acf929ac80f0d98276e30b2e7359 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | e78cf86d924270fb76ac756bb4eafb0db322a9a0fd507349d087175c1a2969ed | yes |
| Final briefing | research/final_briefing.md | model-facing | 2bbb950ee42704752b3e45a09db9712d67a1126f5ad90eb27fa6874876298234 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
