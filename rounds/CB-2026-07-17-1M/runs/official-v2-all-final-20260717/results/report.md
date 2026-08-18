# CapitalBench Report: CB-2026-07-17-1M / official-v2-all-final-20260717

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-all-final-20260717
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-17-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-17
- Decision deadline: 2026-07-18T09:30:00Z
- Horizon: one month
- Entry date: 2026-07-17
- Exit date: 2026-08-17
- Entry rule: Use adjusted close prices on Friday, July 17, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Monday, August 17, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

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

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.03463290730959967 | 0.008658226827399917 | Value rotation underway: +2.77% active over 21 sessions, low drawdown, near 52w high, supported by soft CPI and cooling labor data favoring lower-beta value. |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.03477527299995309 | 0.008693818249988272 | Breadth broadening: RSP-SPY spread +1.64% over 21 sessions with lowest volatility among equity options; benefits from concentration unwind. |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | 0.036997951455707945 | 0.009249487863926986 | Strongest sector active return (+6.48% over 21s) with low beta (0.33) and modest drawdown; defensive rotation beneficiary after prior underperformance. |
| anthropic-claude-fable-5 | FINANCIALS | 25.0 | 0.02346249555634561 | 0.005865623889086402 | +4.56% active over 21 sessions, near 52w high, supported by steep 2s/30s curve (4.18%/5.06%) benefiting net interest margins. |
| anthropic-claude-opus-4-7 | SP500 | 40.0 | 0.03952696793983512 | 0.01581078717593405 | Core benchmark exposure amid tech-led pullback |
| anthropic-claude-opus-4-7 | HEALTHCARE | 25.0 | 0.036997951455707945 | 0.009249487863926986 | Strong 21s active return (+6.48%), defensive, low beta, near highs |
| anthropic-claude-opus-4-7 | FINANCIALS | 20.0 | 0.02346249555634561 | 0.004692499111269122 | Positive momentum (+4.56% 21s), steep curve, resilient in weak tape |
| anthropic-claude-opus-4-7 | LOW_VOL | 15.0 | -0.00900222259313288 | -0.001350333388969932 | Defensive factor showing +3.66% active return, low drawdown |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.036997951455707945 | 0.011099385436712383 | Defensive sector with strong 21s active return (+6.48%), low beta (0.33), and low drawdown; benefits from rotation out of tech. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.02346249555634561 | 0.005865623889086402 | Positive momentum (+4.56% 21s active), low volatility, steepening curve supportive of bank margins. |
| anthropic-claude-opus-4-8 | DIVIDEND | 25.0 | 0.04193254329990892 | 0.01048313582497723 | Low beta defensive dividend equity with positive 5s (+1.57%) and 21s (+2.66%) active returns amid market decline. |
| anthropic-claude-opus-4-8 | SP500 | 20.0 | 0.03952696793983512 | 0.007905393587967024 | Core benchmark exposure to hedge against a tech rebound. |
| google-gemini-3-1-pro | OIL | 40.0 | 0.05106485963213947 | 0.020425943852855788 | Strong recent momentum and tight supply dynamics support continued outperformance. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 30.0 | 0.009127656800104411 | 0.002738297040031323 | Stable rates and positive economic growth provide a favorable environment for regional banks. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.036997951455707945 | 0.011099385436712383 | Defensive characteristics offer downside protection while maintaining positive expected returns. |
| openai-gpt-5-5 | HEALTHCARE | 30.0 | 0.036997951455707945 | 0.011099385436712383 | Healthcare has strong 21-session active performance with lower beta than SPY and can benefit if weak labor data and disinflation support defensive rotation. |
| openai-gpt-5-5 | FINANCIALS | 25.0 | 0.02346249555634561 | 0.005865623889086402 | Financials show positive recent breadth/relative strength, low distance from 52-week high, and may benefit from a still-positive nominal-rate backdrop if credit fears do not rise. |
| openai-gpt-5-5 | REAL_ESTATE | 20.0 | -0.012989872302950345 | -0.002597974460590069 | Real estate is near a 52-week high and has positive 5- and 21-session active returns; softer inflation and payroll data could support rate-sensitive assets. |
| openai-gpt-5-5 | ENERGY | 15.0 | 0.08495145631067968 | 0.012742718446601952 | Energy has strong 5- and 21-session active returns and supplied oil-market facts include a sharp Brent move, but position size is limited by volatility and reversal risk. |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 10.0 | 0.03477527299995309 | 0.003477527299995309 | Equal-weight S&P 500 has outperformed SPY over 5 and 21 sessions, consistent with rotation away from mega-cap weakness while retaining broad US equity exposure. |
| openai-gpt-5-6-sol | SMALL_VALUE | 30.0 | 0.018530179005127323 | 0.005559053701538197 | Recent small-value strength and broader market participation support continued rotation away from concentrated large-cap growth, while the weak labor backdrop limits conviction. |
| openai-gpt-5-6-sol | HEALTHCARE | 30.0 | 0.036997951455707945 | 0.011099385436712383 | Healthcare offers defensive exposure amid softer payroll growth and has demonstrated strong benchmark-relative momentum, though its weak preceding trend warrants moderation. |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 25.0 | 0.009127656800104411 | 0.002281914200026103 | Strong recent relative performance and a positively sloped two-to-ten-year Treasury segment support the near-term case, balanced against credit sensitivity. |
| openai-gpt-5-6-sol | ENERGY | 15.0 | 0.08495145631067968 | 0.012742718446601952 | Energy has positive short- and medium-term momentum with support from the latest Brent surge, but the lower EIA third-quarter price forecast argues for a smaller allocation. |
| xai-grok-4-3 | ENERGY | 40.0 | 0.08495145631067968 | 0.03398058252427188 | Strong recent performance and energy price data support outperformance versus SPY. |
| xai-grok-4-3 | SMALL_VALUE | 20.0 | 0.018530179005127323 | 0.0037060358010254646 | Positive recent returns and value tilt amid weak growth data. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.02346249555634561 | 0.004692499111269122 | Positive recent active returns and rate environment support. |
| xai-grok-4-3 | REAL_ESTATE | 20.0 | -0.012989872302950345 | -0.002597974460590069 | Recent positive returns in rate-sensitive defensive sector. |
| xai-grok-4-5 | ENERGY | 25.0 | 0.08495145631067968 | 0.02123786407766992 | Recent oil strength and energy outperformance supported by supply dynamics into FOMC and data window. |
| xai-grok-4-5 | FINANCIALS | 25.0 | 0.02346249555634561 | 0.005865623889086402 | Relative strength in financials and regional banks amid stable rates and soft but non-recession labor data. |
| xai-grok-4-5 | HEALTHCARE | 25.0 | 0.036997951455707945 | 0.009249487863926986 | Strong 21-session active return and defensive characteristics with upcoming inflation and GDP data. |
| xai-grok-4-5 | SMALL_VALUE | 25.0 | 0.018530179005127323 | 0.004632544751281831 | Positive recent active returns and value tilt favored in equal-weight/value leadership vs mega-cap growth. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | ENERGY | 4 | 0.58 | 0.08495145631067968 | 0.04098552058196514 | 0.0014585526421300177 | 0.1598279008720258 |  | True | True |
| xai-grok-4-3 | ENERGY | 4 | 0.62 | 0.08495145631067968 | 0.039781142975976395 | 0.00025417503614127285 | 0.16103227847801455 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 4 | 0.57 | 0.036997951455707945 | 0.03535353873874304 | -0.00417342920109208 | 0.16545988271524792 |  | False | True |
| google-gemini-3-1-pro | OIL | 3 | 0.65 | 0.05106485963213947 | 0.03426362632959949 | -0.005263341610235631 | 0.16654979512439144 |  | False | True |
| anthropic-claude-fable-5 | LARGE_VALUE | 4 | 0.6 | 0.03463290730959967 | 0.03246715683040158 | -0.007059811109433545 | 0.16834626462358937 |  | False | True |
| openai-gpt-5-6-sol | SMALL_VALUE | 4 | 0.59 | 0.018530179005127323 | 0.031683071784878634 | -0.007843896154956488 | 0.1691303496691123 |  | False | True |
| openai-gpt-5-5 | HEALTHCARE | 5 | 0.56 | 0.036997951455707945 | 0.030587280611805975 | -0.008939687328029147 | 0.17022614084218496 |  | False | True |
| anthropic-claude-opus-4-7 | SP500 | 4 | 0.58 | 0.03952696793983512 | 0.028402440762160225 | -0.011124527177674898 | 0.17241098069183072 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 24a4830b88430256c498b886dda20035a1c1a8d2160716bf9ac483b57ce98300 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 10a5f0e81e2dcdbba8e44b52c31962cb717c65728ec80fad5f1a4c0ce1bce58e |
| manifest.yaml | 5e8d5944f6508d6bbe08081b796a973d23aa88b6fcff95cbdc6081dec12144c9 |
| submission_schema.json | f74e11a346ede06b8dd5aabf1008dc1d51b36b7920a525a9f7c592f84031ce88 |
| market_data/universe_decision_context.csv | 3ab48e99149d530e9a244be318f6521d1f48d738f84151eb985a4569e0140c38 |
| market_data/universe_decision_context.md | 9d3b822878f92d1b869208f213c68f9dc9036b7b3b5481a3ed73454ab55d01cb |
| market_data/universe_decision_context.json | 10b851807b1ace664080c811027dd5ee59c654af50e84b05e5073a71ddcc0f5f |
| market_data/decision_context_source_history.json | a1c3eb9f5214963cca87c641fc3053300c6c70d668ec10e9eeb6a32b404dee3f |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 7a13fef3c88749d41b4f13e834cb1ef156f023dc49873250eace6b975db521db | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 5934e8fc1696a91d53ac7719ebf90f0600c6c8b7c8b3eafb6a65ce45130d6064 | yes |
| Final briefing | research/final_briefing.md | model-facing | 24a4830b88430256c498b886dda20035a1c1a8d2160716bf9ac483b57ce98300 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
