# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-28-1M
- Decision deadline: 2026-07-29T12:30:00Z
- Horizon: one month
- Official run ID: official-v2-2-all-monthly-20260728-clean
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | EQUAL_WEIGHT_SP500 | 3 | 0.59 | Equal weight has the strongest breadth confirmation, healthcare supplies defensive relative strength, and Nasdaq-100 offers event-driven rebound potential after a material pullback. | A hawkish FOMC outcome or renewed inflation pressure lifts yields and compresses equity valuations.; Mega-cap or Nvidia earnings disappoint, extending the technology drawdown.; Weak employment or consumption data turns broadening into a cyclical selloff.; Recent defensive and equal-weight leadership reverses abruptly back toward cap-weighted mega-caps. |
| anthropic-claude-opus-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.56 | Rotation from megacap tech/semis toward equal-weight, financials and defensives is supported by breadth data (RSP-SPY +3.3% in 5 days) and shallow drawdowns at 52-week highs; a gold sleeve hedges FOMC hike risk. | FOMC surprise hike (31.5% implied) hits all risk assets; Sharp mean-reversion rally in semis/momentum leaves SPY ahead; Hot July CPI lifts yields, pressuring financials and gold; Megacap earnings beats re-concentrate leadership into cap-weighted SPY |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 4 | 0.58 | Rotation trade favoring value/defensive sectors over growth given the sharp tech drawdown and macro uncertainty around FOMC. | FOMC surprise hike (31.5% implied) triggers broad equity selloff; Rapid tech rebound reverses value leadership; Credit stress in financials from Senior Loan Officer Survey |
| anthropic-claude-fable-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.6 | Overweight equal-weight, value, financials, and healthcare versus a small SPY anchor to capture the ongoing breadth rotation while tech corrects from a ~9% Nasdaq drawdown. | Surprise dovish outcome or strong mega-cap earnings reignite tech leadership, reversing the rotation; A hawkish 25bp hike (31.5% priced) hits all equities including financials; July CPI reaccelerates, lifting yields and pressuring the whole portfolio; Value/breadth trade is crowded after strong 5-session run and mean-reverts |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.55 | Favors recent positive performers in defensive areas over growth sectors showing sharp pullbacks. | FOMC outcome and July CPI surprise; Further tech sector weakness extending to broader market; Oil price volatility from unresolved Hormuz negotiations |
| openai-gpt-5-5 | openai | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.56 | Selected holdings all have base forecasts above SPY and are supported by recent breadth, 52-week highs or positive active returns. The one-month edge depends on continued rotation away from cap-weighted technology weakness into broader and more defensive equity leadership. | Mega-cap technology and SPY rebound sharply after major earnings, causing the active portfolio to lag.; FOMC, CPI, PPI, GDP, or employment data revive rate fears and pressure financials, dividend equities, real assets, and broad equities.; Recent breadth and sector rotation reverse, with equal-weight and defensive sectors giving back their short-term active gains.; Aerospace and defense strength proves a short-term spike and reverses without supportive earnings or geopolitical follow-through. |
| xai-grok-4-5 | xai | portfolio | FINANCIALS | 4 | 0.58 | Value, financials, healthcare, and aerospace exhibit better recent active performance and positioning than cap-weighted SPY amid mixed rates and data. Selection favors continuation of breadth with defined invalidation levels. | FOMC or GDP surprise triggers broad equity selloff; Tech earnings contagion reverses value/financial leadership; Geopolitical escalation hits energy-linked or risk assets; Higher-than-expected inflation data lifts yields sharply |
| google-gemini-3-1-pro | google | portfolio | AEROSPACE_DEFENSE | 2 | 0.65 | Allocated to Aerospace & Defense and Healthcare for defensive positioning and recent strength. | Market rotation back into high-growth technology stocks.; Unexpected positive economic data reducing the appeal of defensive sectors.; Specific sector risks such as regulatory changes in healthcare or defense budget cuts. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.49 | 18.37 | 0.26777087646652875 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 36.14 | 43.9 | 0.21472053126729373 | 2 |
| SOFTWARE | Software | 91.78 | 109.5 | 0.1930703857049465 | 3 |
| SOUTH_KOREA | South Korea Equities | 151.45 | 180.2 | 0.18983162759986794 | 4 |
| METALS_MINING | Metals and Mining | 101.44 | 118.74 | 0.17054416403785488 | 5 |
| SILVER | Silver | 51.7 | 60.02 | 0.16092843326885875 | 6 |
| TAIWAN | Taiwan Equities | 93.95 | 107.9 | 0.14848323576370404 | 7 |
| SOUTH_AFRICA | South Africa Equities | 61.98 | 70.72 | 0.1410132300742175 | 8 |
| BROAD_AI_TECH | Broad AI Technology | 57.24 | 64.22 | 0.12194269741439556 | 9 |
| GOLD | Gold | 75.7 | 83.82 | 0.10726552179656523 | 10 |
| CYBERSECURITY | Cybersecurity | 89.28 | 98.56 | 0.10394265232974909 | 11 |
| ENERGY | Energy Sector | 57.57 | 62.68 | 0.08876150772972036 | 12 |
| TECHNOLOGY | Technology Sector | 171.09 | 185.69 | 0.0853352036939623 | 13 |
| BIOTECH | Biotechnology | 149.78 | 162.38 | 0.08412338095873939 | 14 |
| BROAD_COMMODITIES | Broad Commodities | 17.06 | 18.39 | 0.07796014067995327 | 15 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 113.59 | 122.32 | 0.07685535698565005 | 16 |
| OIL | Crude Oil | 120.49 | 129.7 | 0.07643787866212959 | 17 |
| JAPAN | Japan Equities | 89.83 | 95.87 | 0.0672381164421687 | 18 |
| NASDAQ100 | Nasdaq 100 | 675.49 | 716.43 | 0.06060785503856447 | 19 |
| LARGE_GROWTH | US Large-Cap Growth | 116.48 | 122.75 | 0.053828983516483575 | 20 |
| EMERGING_MARKETS | Emerging Markets | 57.74 | 60.79 | 0.052822999653619584 | 21 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.6 | 73.06 | 0.04971264367816097 | 22 |
| AGRICULTURE | Agriculture Commodities | 27.84 | 29.19 | 0.04849137931034497 | 23 |
| SEMICONDUCTORS | Semiconductors | 529.6 | 553.11 | 0.04439199395770399 | 24 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.48 | 117.21 | 0.04205192034139382 | 25 |
| SP500 | S&P 500 | 740.86 | 769.35 | 0.03845530869530012 | 26 |
| TOTAL_US_MARKET | Total US Stock Market | 365.99 | 379.36 | 0.03653105276100432 | 27 |
| COPPER | Copper | 38.33 | 39.67 | 0.03495956170101766 | 28 |
| CANADA | Canada Equities | 59.84 | 61.73 | 0.0315842245989304 | 29 |
| EUROPE | Europe Equities | 89.23 | 91.98 | 0.03081923120026886 | 30 |
| COMMUNICATIONS | Communication Services Sector | 109.67 | 112.99 | 0.030272636090088456 | 31 |
| DIVIDEND | US Dividend Equities | 33.89 | 34.9 | 0.029802301563883082 | 32 |
| MOMENTUM | US Momentum Equities | 292.32 | 299.71 | 0.025280514504652407 | 33 |
| LARGE_VALUE | US Large-Cap Value | 252.04 | 258.33 | 0.024956356133946977 | 34 |
| HEALTHCARE | Healthcare Sector | 167.26 | 171.16 | 0.023316991510223595 | 35 |
| AUSTRALIA | Australia Equities | 29.32 | 30.0 | 0.023192360163710735 | 36 |
| YEN | Japanese Yen | 56.0 | 57.25 | 0.022321428571428603 | 37 |
| EURO | Euro | 105.11 | 106.978 | 0.017771858053467815 | 38 |
| MATERIALS | Materials Sector | 52.34 | 53.18 | 0.016048910966755647 | 39 |
| UNITED_KINGDOM | United Kingdom Equities | 47.82 | 48.55 | 0.015265579255541617 | 40 |
| CHINA | China Equities | 54.41 | 55.23 | 0.01507075905164501 | 41 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 217.69 | 220.69 | 0.013781064816941413 | 42 |
| FINANCIALS | Financials Sector | 57.6 | 58.1 | 0.00868055555555558 | 43 |
| SMALL_CAP | US Small-Cap Stocks | 293.37 | 295.75 | 0.008112622285850524 | 44 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.42 | 79.74 | 0.004029211785444353 | 45 |
| INDIA | India Equities | 49.38 | 49.56 | 0.0036452004860267895 | 46 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.63 | 91.65 | 0.0002182691258323377 | 47 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 48 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.19 | 94.89 | -0.0031515915537345673 | 49 |
| MID_CAP | US Mid-Cap Stocks | 76.03 | 75.76 | -0.003551229777719267 | 50 |
| MEXICO | Mexico Equities | 76.78 | 76.48 | -0.0039072675175826355 | 51 |
| SMALL_VALUE | US Small-Cap Value | 224.11 | 223.14 | -0.004328231671946958 | 52 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.92 | 97.49 | -0.004391339869281086 | 53 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.83 | 106.35 | -0.004493119910137677 | 54 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.67 | 93.17 | -0.005337888331376162 | 55 |
| TIPS | Treasury Inflation-Protected Securities | 107.66 | 106.94 | -0.00668772060189482 | 56 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.0 | 105.22 | -0.0073584905660377675 | 57 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.56 | 92.85 | -0.007588713125267321 | 58 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.99 | 47.6 | -0.008126693061054402 | 59 |
| SOLAR | Solar Energy | 49.1 | 48.65 | -0.009164969450101923 | 60 |
| BRAZIL | Brazil Equities | 36.05 | 35.55 | -0.01386962552011095 | 61 |
| US_DOLLAR | US Dollar | 28.58 | 28.18 | -0.013995801259622076 | 62 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.24 | 82.88 | -0.01614434947768284 | 63 |
| CONSUMER_STAPLES | Consumer Staples Sector | 87.06 | 85.45 | -0.018492993337927865 | 64 |
| INDUSTRIALS | Industrials Sector | 182.49 | 177.14 | -0.029316674886295302 | 65 |
| REGIONAL_BANKS | Regional Banks | 76.79 | 74.3 | -0.032426097148066324 | 66 |
| REAL_ESTATE | Real Estate Sector | 46.01 | 44.48 | -0.033253640512932 | 67 |
| LOW_VOL | US Low Volatility Equities | 77.97 | 75.08 | -0.0370655380274465 | 68 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 244.98 | 232.82 | -0.0496367050371459 | 69 |
| UTILITIES | Utilities Sector | 45.52 | 42.73 | -0.061291739894551944 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | portfolio | EQUAL_WEIGHT_SP500 | 3 | 0.59 | 0.013781064816941413 | 0.03068987989141299 | -0.007765428803887128 | 0.23708099657511578 |  | False | True |
| anthropic-claude-opus-5 | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.56 | 0.013781064816941413 | 0.028951442776954807 | -0.00950386591834531 | 0.23881943368957395 |  | False | True |
| anthropic-claude-opus-4-8 | portfolio | FINANCIALS | 4 | 0.58 | 0.00868055555555558 | 0.021606649457515517 | -0.0168486592377846 | 0.24616422700901325 |  | False | True |
| anthropic-claude-fable-5 | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.6 | 0.013781064816941413 | 0.02068631137966177 | -0.017768997315638347 | 0.247084565086867 |  | False | True |
| xai-grok-4-3 | portfolio | SP500 | 4 | 0.55 | 0.03845530869530012 | 0.0118542918838467 | -0.026601016811453417 | 0.25591658458268207 |  | False | True |
| openai-gpt-5-5 | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.56 | 0.013781064816941413 | 0.00861475563766521 | -0.029840553057634906 | 0.2591561208288635 |  | False | True |
| xai-grok-4-5 | portfolio | FINANCIALS | 4 | 0.58 | 0.00868055555555558 | 0.001015509511725494 | -0.037439799183574624 | 0.26675536695480323 |  | False | True |
| google-gemini-3-1-pro | portfolio | AEROSPACE_DEFENSE | 2 | 0.65 | -0.0496367050371459 | -0.013159856763461153 | -0.05161516545876127 | 0.2809307332299899 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1M has no scored official run.
- Round CB-2026-07-29-1M has no scored official run.
- Round CB-2026-07-30-1M has no scored official run.
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
