# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-17-1M
- Decision deadline: 2026-07-18T09:30:00Z
- Horizon: one month
- Official run ID: official-v2-all-final-20260717
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | SPY base modest given recent weakness and mixed data; energy, financials, healthcare and small-value offer higher base forecasts from supplied relative strength and macro schedule. Equal 25% weights balance exposures. | FOMC hawkish surprise or upside inflation reprint reversing value/energy leadership; Oil price mean-reversion per EIA Q3 forecast undercutting energy; Growth scare from weak payrolls/GDP hitting small-value and financials; Broad equity drawdown from high starting levels despite sector tilts |
| xai-grok-4-3 | xai | portfolio | ENERGY | 4 | 0.62 | Four holdings across distinct clusters with bases above SPY forecast; 40% energy cap respected. | Further equity market decline on weak payroll revisions; Oil price reversal below $80; FOMC signals tighter policy than expected |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 4 | 0.57 | Defensive rotation is underway with tech clusters down heavily while healthcare, financials, and dividends show positive active returns and low drawdowns. | Tech mega-caps rebound sharply, reversing defensive leadership and dragging SPY up faster; Hawkish FOMC July 29 hits rate-sensitive and cyclical sectors; Energy/oil spike feeds inflation and pressures broad equities |
| google-gemini-3-1-pro | google | portfolio | OIL | 3 | 0.65 | Overweight energy and financials for growth, with healthcare for defense. | A sudden economic downturn could negatively impact oil demand and regional bank loan portfolios.; Unexpectedly hawkish Fed policy could pressure equity valuations across all sectors.; A rapid rotation back into mega-cap technology stocks could cause this portfolio to underperform the S&P 500. |
| anthropic-claude-fable-5 | anthropic | portfolio | LARGE_VALUE | 4 | 0.6 | Overweight value, equal-weight, healthcare, and financials to capture the ongoing rotation out of concentrated tech, staying within the 50% cluster cap on diversified US equity. | Sharp mega-cap tech rebound would reverse the rotation and cause underperformance vs SPY; Hawkish July 29 FOMC or hot August CPI could hit all equity holdings; Healthcare policy headlines could derail XLV strength; Oil-driven inflation resurgence (Brent +4.6% on Jul 17) pressuring rate-sensitive value |
| openai-gpt-5-6-sol | openai | portfolio | SMALL_VALUE | 4 | 0.59 | A softer labor market and benign monthly core CPI favor rotation and defensive exposure, while still-elevated inflation and long yields constrain broad-market upside. The allocation targets four distinct clusters with supplied relative-strength or macro support. | July CPI or PPI reaccelerates, lifting yields and pressuring rate-sensitive equities.; Payroll weakness develops into a sharper growth or credit scare, hurting small-value and regional banks.; The recent rotation reverses and mega-cap growth resumes leadership before the exit close.; Crude oil reverses as the EIA's lower third-quarter Brent forecast becomes dominant. |
| openai-gpt-5-5 | openai | portfolio | HEALTHCARE | 5 | 0.56 | Base forecasts favor active holdings over SPY because SPY and Nasdaq entered the window weak while several non-mega-cap sectors showed positive relative strength. Allocation is capped by cluster and volatility risk, with no non-SPY cluster above 50%. | Mega-cap technology rebounds sharply and SPY outperforms the sector/value/defensive tilt.; July CPI/PPI or PCE/ECI data reaccelerate inflation and lift yields, hurting real estate and equities.; Labor or credit data weaken enough to pressure financials, cyclicals, and broad risk appetite.; Oil reverses after its sharp July 17 gain, dragging energy holdings. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SP500 | 4 | 0.58 | Tech/semis just suffered severe drawdowns (SMH -8.9%, AIQ -7.5%) while defensives and financials showed positive active returns. Overweight the leadership rotation rather than chasing broken momentum. | FOMC surprise hawkish tilt hits rate-sensitive defensives; Tech mean-reversion bounce leaves defensive tilt behind SPY; Hot CPI on Aug 12 causes broad equity selloff |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| METALS_MINING | Metals and Mining | 98.35 | 118.1 | 0.20081342145399095 | 1 |
| SILVER | Silver | 50.78 | 59.57 | 0.173099645529736 | 2 |
| SOUTH_KOREA | South Korea Equities | 162.54 | 185.1 | 0.13879660391288295 | 3 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 116.14 | 130.47 | 0.12338556914069221 | 4 |
| TAIWAN | Taiwan Equities | 97.33 | 107.8 | 0.10757217712935363 | 5 |
| GOLD | Gold | 75.5 | 83.11 | 0.100794701986755 | 6 |
| SOFTWARE | Software | 92.8 | 101.99 | 0.09903017241379297 | 7 |
| SOUTH_AFRICA | South Africa Equities | 62.36 | 68.19 | 0.09348941629249508 | 8 |
| BROAD_AI_TECH | Broad AI Technology | 58.7 | 64.0 | 0.09028960817717202 | 9 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 230.73 | 251.2 | 0.0887184154639622 | 10 |
| ENERGY | Energy Sector | 57.68 | 62.58 | 0.08495145631067968 | 11 |
| JAPAN | Japan Equities | 90.49 | 98.17 | 0.0848712564924301 | 12 |
| TECHNOLOGY | Technology Sector | 175.59 | 190.32 | 0.08388860413463184 | 13 |
| SEMICONDUCTORS | Semiconductors | 556.53 | 594.07 | 0.06745368623434511 | 14 |
| MOMENTUM | US Momentum Equities | 302.09 | 322.07 | 0.0661392300307857 | 15 |
| CYBERSECURITY | Cybersecurity | 92.36 | 97.79 | 0.058791684711996695 | 16 |
| COPPER | Copper | 37.92 | 40.13 | 0.05828059071729963 | 17 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.7 | 73.69 | 0.05724533715925384 | 18 |
| BROAD_COMMODITIES | Broad Commodities | 17.25 | 18.21 | 0.05565217391304356 | 19 |
| OIL | Crude Oil | 123.96 | 130.29 | 0.05106485963213947 | 20 |
| NASDAQ100 | Nasdaq 100 | 695.33 | 729.87 | 0.0496742553895273 | 21 |
| LARGE_GROWTH | US Large-Cap Growth | 119.38 | 125.08 | 0.0477466912380633 | 22 |
| CANADA | Canada Equities | 59.45 | 62.18 | 0.04592094196804042 | 23 |
| EMERGING_MARKETS | Emerging Markets | 57.84 | 60.39 | 0.044087136929460424 | 24 |
| DIVIDEND | US Dividend Equities | 32.91 | 34.29 | 0.04193254329990892 | 25 |
| TOTAL_US_MARKET | Total US Stock Market | 367.01 | 382.13 | 0.04119778752622549 | 26 |
| CHINA | China Equities | 52.95 | 55.06 | 0.03984891406987723 | 27 |
| EUROPE | Europe Equities | 88.59 | 92.1 | 0.039620724686759035 | 28 |
| SP500 | S&P 500 | 743.29 | 772.67 | 0.03952696793983512 | 29 |
| MID_CAP | US Mid-Cap Stocks | 75.54 | 78.48 | 0.038919777601270855 | 30 |
| INDUSTRIALS | Industrials Sector | 179.41 | 186.32 | 0.03851513293573383 | 31 |
| HEALTHCARE | Healthcare Sector | 161.09 | 167.05 | 0.036997951455707945 | 32 |
| ETHEREUM_ETF | Ethereum ETF | 13.91 | 14.4 | 0.035226455787203514 | 33 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.37 | 220.79 | 0.03477527299995309 | 34 |
| LARGE_VALUE | US Large-Cap Value | 248.03 | 256.62 | 0.03463290730959967 | 35 |
| BIOTECH | Biotechnology | 154.26 | 159.53 | 0.03416310125761712 | 36 |
| SMALL_CAP | US Small-Cap Stocks | 294.04 | 304.06 | 0.03407699632703021 | 37 |
| MATERIALS | Materials Sector | 50.53 | 52.24 | 0.03384128240649131 | 38 |
| AUSTRALIA | Australia Equities | 28.75 | 29.55 | 0.027826086956521667 | 39 |
| UNITED_KINGDOM | United Kingdom Equities | 46.94 | 48.16 | 0.025990626331487077 | 40 |
| FINANCIALS | Financials Sector | 56.26 | 57.58 | 0.02346249555634561 | 41 |
| SMALL_VALUE | US Small-Cap Value | 222.34 | 226.46 | 0.018530179005127323 | 42 |
| YEN | Japanese Yen | 56.51 | 57.53 | 0.0180499026720935 | 43 |
| INDIA | India Equities | 48.91 | 49.58 | 0.013698630136986356 | 44 |
| EURO | Euro | 105.5277164053 | 106.86 | 0.012624963754385599 | 45 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.44 | 116.75 | 0.011347886347886416 | 46 |
| AGRICULTURE | Agriculture Commodities | 27.84 | 28.14 | 0.010775862068965525 | 47 |
| REGIONAL_BANKS | Regional Banks | 76.69 | 77.39 | 0.009127656800104411 | 48 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.2659245633 | 79.61 | 0.004340773650160612 | 49 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.2774745356 | 91.55 | 0.0029856814705548906 | 50 |
| BITCOIN_ETF | Bitcoin ETF | 36.35 | 36.42 | 0.0019257221458046647 | 51 |
| COMMUNICATIONS | Communication Services Sector | 110.65 | 110.82 | 0.0015363759602349258 | 52 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 53 |
| MEXICO | Mexico Equities | 75.11 | 74.91 | -0.0026627612834509984 | 54 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.8115704203 | 47.65 | -0.0033793163219629774 | 55 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.4360280407 | 93.05 | -0.004131468864792098 | 56 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.1148195463 | 94.7 | -0.004361250415852114 | 57 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.19 | 84.68 | -0.005986618147669764 | 58 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.8603483234 | 97.25 | -0.0062369318509165605 | 59 |
| TIPS | Treasury Inflation-Protected Securities | 107.4810572561 | 106.77 | -0.0066156518576639955 | 60 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.2914175414 | 105.56 | -0.0068812474075351515 | 61 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.5200560195 | 92.84 | -0.0072717665968699 | 62 |
| US_DOLLAR | US Dollar | 28.33 | 28.1 | -0.008118602188492696 | 63 |
| LOW_VOL | US Low Volatility Equities | 76.428022067 | 75.74 | -0.00900222259313288 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.42 | 44.83 | -0.012989872302950345 | 65 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.0981657807 | 105.7 | -0.013054992777028152 | 66 |
| UTILITIES | Utilities Sector | 45.17 | 44.18 | -0.02191720168253275 | 67 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.1815387976 | 81.35 | -0.03363610166841868 | 68 |
| BRAZIL | Brazil Equities | 35.23 | 33.97 | -0.03576497303434567 | 69 |
| SOLAR | Solar Energy | 53.9 | 50.92 | -0.055287569573283846 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | portfolio | ENERGY | 4 | 0.58 | 0.08495145631067968 | 0.04098552058196514 | 0.0014585526421300177 | 0.1598279008720258 |  | True | True |
| xai-grok-4-3 | portfolio | ENERGY | 4 | 0.62 | 0.08495145631067968 | 0.039781142975976395 | 0.00025417503614127285 | 0.16103227847801455 |  | True | True |
| anthropic-claude-opus-4-8 | portfolio | HEALTHCARE | 4 | 0.57 | 0.036997951455707945 | 0.03535353873874304 | -0.00417342920109208 | 0.16545988271524792 |  | False | True |
| google-gemini-3-1-pro | portfolio | OIL | 3 | 0.65 | 0.05106485963213947 | 0.03426362632959949 | -0.005263341610235631 | 0.16654979512439144 |  | False | True |
| anthropic-claude-fable-5 | portfolio | LARGE_VALUE | 4 | 0.6 | 0.03463290730959967 | 0.03246715683040158 | -0.007059811109433545 | 0.16834626462358937 |  | False | True |
| openai-gpt-5-6-sol | portfolio | SMALL_VALUE | 4 | 0.59 | 0.018530179005127323 | 0.031683071784878634 | -0.007843896154956488 | 0.1691303496691123 |  | False | True |
| openai-gpt-5-5 | portfolio | HEALTHCARE | 5 | 0.56 | 0.036997951455707945 | 0.030587280611805975 | -0.008939687328029147 | 0.17022614084218496 |  | False | True |
| anthropic-claude-opus-4-7 | portfolio | SP500 | 4 | 0.58 | 0.03952696793983512 | 0.028402440762160225 | -0.011124527177674898 | 0.17241098069183072 |  | False | True |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1M has no scored official run.
- Round CB-2026-07-21-1M has no scored official run.
- Round CB-2026-07-22-1M has no scored official run.
- Round CB-2026-07-23-1M has no scored official run.
- Round CB-2026-07-24-1M has no scored official run.
- Round CB-2026-07-27-1M has no scored official run.
- Round CB-2026-07-28-1M has no scored official run.
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
- Round example-round has no scored official run.
- Round example-round-2 has no scored official run.
