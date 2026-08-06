# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-29-1W
- Decision deadline: 2026-07-30T12:30:00Z
- Horizon: one week
- Official run ID: official-v2-2-all-weekly-20260729-clean
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.57 | Barbell of benchmark plus defensive/value/energy tilts supported by breadth rotation (RSP-SPY +3.8% over 5 sessions), rising oil, and elevated policy uncertainty. | Sharp mega-cap tech rebound on Apple/Amazon results would reverse the rotation; Hot Q2 GDP/PCE prints lifting yields and hurting defensives; Oil reversal if Hormuz risk premium unwinds; Crowded defensive positioning prone to mean reversion |
| openai-gpt-5-5 | openai | portfolio | AGRICULTURE | 5 | 0.57 | SPY has mild rebound potential after a weak close, but several active exposures have stronger one-week base forecasts based on supplied quality, relative strength, and catalysts. The allocation targets diversified alpha versus SPY rather than a single momentum bet. | Scheduled GDP, PCE, labor-cost, and loan-officer data could trigger a broad equity or rates reversal unfavorable to selected sectors.; Commodity exposures may reverse quickly if Middle East risk premium fades or global growth expectations weaken.; A sharp rebound in mega-cap technology would likely help SPY more than this portfolio and reduce alpha.; Financials could lag if long yields fall, credit concerns rise, or the loan survey signals tighter lending conditions. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | LARGE_VALUE | 4 | 0.6 | Tilt to defensive equity leaders that resisted the selloff while keeping SP500 core exposure. | Sharp tech rebound reverses defensive rotation; Strong GDP/PCE prints trigger broad risk-on rally; Middle East escalation spikes volatility across all equities |
| xai-grok-4-5 | xai | portfolio | ENERGY | 5 | 0.58 | SPY base is modest after the 1.5% drop and elevated uncertainty; selected holdings clear the active hurdle via quality scores, prior active returns and catalysts inside the window. Allocations stay diversified across five clusters under the cap. | Further equity selloff on soft GDP/PCE or weak Apple/Amazon results dragging cyclicals and EM; Sudden Middle East de-escalation removing energy premium; Dollar strength or real-yield rise pressuring gold and commodities; High volatility in oil and EM reversing recent relative strength |
| xai-grok-4-3 | xai | portfolio | LARGE_VALUE | 4 | 0.62 | Portfolio tilts toward large value, dividend, healthcare and financials clusters for one-week alpha versus SP500. | FOMC dissent signals potential policy volatility; Middle East conflict escalation affecting energy and risk assets; Weaker than expected Q2 GDP print |
| anthropic-claude-fable-5 | anthropic | portfolio | LARGE_VALUE | 5 | 0.66 | Defensive rotation portfolio: value, staples, healthcare, energy, and gold to exploit ongoing breadth divergence (RSP-SPY +3.83% over 5 sessions) and geopolitical oil/gold support while avoiding stressed growth exposure. | Sharp mega-cap tech rebound after Apple/Amazon earnings would lift SPY above defensive sectors; Middle East de-escalation could reverse energy and gold gains quickly; Hot PCE/ECI prints could push yields higher, pressuring all equity holdings; Defensive sectors have already run 5-7% active in a week and may mean-revert |
| openai-gpt-5-6-sol | openai | portfolio | DIVIDEND | 4 | 0.61 | Dividend equities, financials, energy, and China each have base forecasts above SPY, supported by relative strength plus distinct near-term drivers. The weighted base return is 0.66%, implying 0.46 percentage point expected alpha. | A benign inflation or growth surprise could trigger a sharp rebound in mega-cap technology and reverse the value and defensive rotation.; De-escalation in the Middle East could rapidly unwind energy-sector strength.; Weak GDP, labor, or lending data could hurt financials and broader cyclical risk appetite.; China-specific policy or geopolitical stress could overwhelm recent relative momentum. |
| google-gemini-3-1-pro | google | portfolio | CONSUMER_STAPLES | 2 | 0.65 | Defensive positioning with Consumer Staples and Healthcare. | A sudden risk-on rally could lead to underperformance.; Sector-specific earnings misses could drag down returns.; Macro data surprises could shift market sentiment rapidly. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 144.21 | 169.13999938964844 | 0.1728728894643119 | 1 |
| METALS_MINING | Metals and Mining | 97.58 | 111.91999816894531 | 0.14695632474836362 | 2 |
| TAIWAN | Taiwan Equities | 89.41 | 101.69999694824219 | 0.13745662619664678 | 3 |
| SEMICONDUCTORS | Semiconductors | 504.22 | 569.7000122070312 | 0.12986397248627823 | 4 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 109.56 | 122.4000015258789 | 0.1171960708824289 | 5 |
| TECHNOLOGY | Technology Sector | 166.57 | 185.91000366210938 | 0.11610736424391788 | 6 |
| BROAD_AI_TECH | Broad AI Technology | 55.98 | 62.36000061035156 | 0.11396928564400799 | 7 |
| CYBERSECURITY | Cybersecurity | 88.79 | 97.56999969482422 | 0.09888500613609885 | 8 |
| SOFTWARE | Software | 92.37 | 101.30999755859375 | 0.09678464391678832 | 9 |
| MOMENTUM | US Momentum Equities | 283.11 | 309.9800109863281 | 0.09491014441852319 | 10 |
| LARGE_GROWTH | US Large-Cap Growth | 114.05 | 123.88999938964844 | 0.08627794291668955 | 11 |
| NASDAQ100 | Nasdaq 100 | 661.73 | 717.2999877929688 | 0.08397683011646562 | 12 |
| SILVER | Silver | 51.77 | 56.06999969482422 | 0.08305968118261964 | 13 |
| SOUTH_AFRICA | South Africa Equities | 62.08 | 66.8499984741211 | 0.0768363156269507 | 14 |
| SOLAR | Solar Energy | 47.68 | 51.27000045776367 | 0.07529363376182197 | 15 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.26 | 252.27999877929688 | 0.06780664851983786 | 16 |
| COPPER | Copper | 38.35 | 40.849998474121094 | 0.0651890084516582 | 17 |
| JAPAN | Japan Equities | 89.35 | 95.16000366210938 | 0.06502522285516932 | 18 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 111.61 | 118.63999938964844 | 0.06298718205938925 | 19 |
| SP500 | S&P 500 | 729.46 | 769.7899780273438 | 0.055287442803366504 | 20 |
| INDUSTRIALS | Industrials Sector | 176.66 | 186.35000610351562 | 0.05485116100710763 | 21 |
| EMERGING_MARKETS | Emerging Markets | 56.92 | 60.0099983215332 | 0.05428668871281106 | 22 |
| TOTAL_US_MARKET | Total US Stock Market | 360.42 | 379.6499938964844 | 0.05335440290906268 | 23 |
| GOLD | Gold | 76.04 | 79.8499984741211 | 0.05010518771858341 | 24 |
| DEVELOPED_EX_US | Developed Markets ex-US | 68.95 | 72.3499984741211 | 0.049311072866150774 | 25 |
| SMALL_CAP | US Small-Cap Stocks | 288.57 | 299.7699890136719 | 0.038812035255473054 | 26 |
| YEN | Japanese Yen | 56.13 | 58.150001525878906 | 0.03598791245107624 | 27 |
| AUSTRALIA | Australia Equities | 29.11 | 30.139999389648438 | 0.0353830089195617 | 28 |
| BIOTECH | Biotechnology | 147.91 | 153.00999450683594 | 0.03448039014830595 | 29 |
| EUROPE | Europe Equities | 88.86 | 91.8499984741211 | 0.03364841856989753 | 30 |
| MID_CAP | US Mid-Cap Stocks | 74.73 | 77.0 | 0.030376020339890175 | 31 |
| LARGE_VALUE | US Large-Cap Value | 249.52 | 256.1300048828125 | 0.026490882024737372 | 32 |
| CANADA | Canada Equities | 59.29 | 60.779998779296875 | 0.02513069285371694 | 33 |
| FINANCIALS | Financials Sector | 56.68 | 58.0 | 0.023288637967536996 | 34 |
| INDIA | India Equities | 49.17 | 50.310001373291016 | 0.02318489675190194 | 35 |
| BITCOIN_ETF | Bitcoin ETF | 36.0 | 36.7400016784668 | 0.020555602179633148 | 36 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.73 | 219.72999572753906 | 0.018541675833398497 | 37 |
| BRAZIL | Brazil Equities | 35.47 | 36.11000061035156 | 0.0180434341796325 | 38 |
| MATERIALS | Materials Sector | 51.74 | 52.63999938964844 | 0.01739465383935901 | 39 |
| CHINA | China Equities | 55.07 | 56.0099983215332 | 0.017069154195264336 | 40 |
| ETHEREUM_ETF | Ethereum ETF | 14.24 | 14.479999542236328 | 0.016853900437944436 | 41 |
| SMALL_VALUE | US Small-Cap Value | 221.6 | 225.0800018310547 | 0.01570397938201573 | 42 |
| REGIONAL_BANKS | Regional Banks | 76.18 | 77.33999633789062 | 0.015227045653591675 | 43 |
| MEXICO | Mexico Equities | 75.57 | 76.69000244140625 | 0.014820728349957069 | 44 |
| COMMUNICATIONS | Communication Services Sector | 109.51 | 110.87000274658203 | 0.012418982253511235 | 45 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.1490352381 | 95.16999816894531 | 0.010844114634455115 | 46 |
| UNITED_KINGDOM | United Kingdom Equities | 47.9 | 48.369998931884766 | 0.009812086260642339 | 47 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.7639193866 | 106.73999786376953 | 0.009228841771659946 | 48 |
| EURO | Euro | 105.6176462839 | 106.58499908447266 | 0.00915900736864006 | 49 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.8579015994 | 79.5199966430664 | 0.008396052015559263 | 50 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.6918669266 | 47.9900016784668 | 0.006251270312517709 | 51 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.5182263297 | 83.0 | 0.005838391004371335 | 52 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.212596527 | 97.70999908447266 | 0.005116647175806177 | 53 |
| AGRICULTURE | Agriculture Commodities | 27.49 | 27.6299991607666 | 0.005092730475322105 | 54 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.8523403595 | 93.30999755859375 | 0.004928870907527028 | 55 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.888045364 | 93.33999633789062 | 0.0048655450991519356 | 56 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.4836107464 | 105.81999969482422 | 0.003189016246637033 | 57 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3672066242 | 91.43 | 0.0006872638238606399 | 58 |
| TIPS | Treasury Inflation-Protected Securities | 106.9847006603 | 107.0 | 0.00014300493066365938 | 59 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 60 |
| DIVIDEND | US Dividend Equities | 33.83 | 33.63999938964844 | -0.0056163349202352775 | 61 |
| US_DOLLAR | US Dollar | 28.42 | 28.09000015258789 | -0.011611535799159411 | 62 |
| HEALTHCARE | Healthcare Sector | 166.24 | 164.16000366210938 | -0.012512008769794525 | 63 |
| LOW_VOL | US Low Volatility Equities | 77.54 | 76.33000183105469 | -0.015604825495812769 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.96 | 45.20000076293945 | -0.016536101763719446 | 65 |
| ENERGY | Energy Sector | 58.65 | 57.310001373291016 | -0.02284737641447543 | 66 |
| CONSUMER_STAPLES | Consumer Staples Sector | 87.36 | 85.33000183105469 | -0.023237158527304347 | 67 |
| UTILITIES | Utilities Sector | 44.91 | 43.65999984741211 | -0.02783344806474919 | 68 |
| BROAD_COMMODITIES | Broad Commodities | 17.57 | 16.979999542236328 | -0.03357999190459149 | 69 |
| OIL | Crude Oil | 129.31 | 114.87999725341797 | -0.11159231881975129 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | portfolio | SP500 | 5 | 0.57 | 0.055287442803366504 | 0.01567833774754181 | -0.0396091050558247 | 0.15719455171677008 |  | False | True |
| openai-gpt-5-5 | portfolio | AGRICULTURE | 5 | 0.57 | 0.005092730475322105 | 0.014617453828511363 | -0.040669988974855145 | 0.15825543563580052 |  | False | True |
| anthropic-claude-opus-4-8 | portfolio | LARGE_VALUE | 4 | 0.6 | 0.026490882024737372 | 0.009163890792763828 | -0.04612355201060268 | 0.16370899867154806 |  | False | True |
| xai-grok-4-5 | portfolio | ENERGY | 5 | 0.58 | -0.02284737641447543 | 0.008070049539445578 | -0.04721739326392092 | 0.16480283992486633 |  | False | True |
| xai-grok-4-3 | portfolio | LARGE_VALUE | 4 | 0.62 | 0.026490882024737372 | 0.007912794075561141 | -0.04737464872780536 | 0.16496009538875075 |  | False | True |
| anthropic-claude-fable-5 | portfolio | LARGE_VALUE | 5 | 0.66 | 0.026490882024737372 | 0.004886102843617633 | -0.050401339959748874 | 0.16798678662069427 |  | False | True |
| openai-gpt-5-6-sol | portfolio | DIVIDEND | 4 | 0.61 | -0.0056163349202352775 | 0.0018392457512476754 | -0.053448197052118826 | 0.17103364371306423 |  | False | True |
| google-gemini-3-1-pro | portfolio | CONSUMER_STAPLES | 2 | 0.65 | -0.023237158527304347 | -0.017874583648549436 | -0.07316202645191594 | 0.19074747311286133 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1W has no scored official run.
- Round CB-2026-07-30-1W has no scored official run.
- Round CB-2026-07-31-1W has no scored official run.
- Round CB-2026-08-04-1W has no scored official run.
