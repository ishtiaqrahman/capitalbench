# CapitalBench Report: CB-2026-06-09-1M / official-20260609

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260609
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 9 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round scored from the June 9, 2026 adjusted close to the July 9, 2026 adjusted close.
- Decision date: 2026-06-09
- Decision deadline: 2026-06-09T23:30:00Z
- Horizon: one month
- Entry date: 2026-06-09
- Exit date: 2026-07-09
- Entry rule: Use adjusted close on Tuesday, June 9, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Thursday, July 9, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Defensive, value-tilted equity allocation favoring sectors with positive recent momentum and lower drawdown risk into June CPI and the FOMC, with short-duration Treasury ballast. | A dovish surprise at the June FOMC or cool May CPI could spark a tech/growth rebound, causing this defensive tilt to lag SPY.; Healthcare could give back its recent sharp outperformance on adverse MedPAC/policy headlines.; Persistent inflation prints could pressure rate-sensitive dividend and value names.; Short Treasury allocation caps upside if equities rally broadly. |
| openai-gpt-5-5 | openai | portfolio | HEALTHCARE | 5 | 0.56 | Hot inflation readings and a likely higher-for-longer policy backdrop make energy, financials, healthcare, and defense more attractive than concentrated growth for the next month. Equal-weight exposure provides some participation if breadth improves without relying heavily on the largest S&P 500 technology names. | A softer-than-expected CPI/PPI and dovish FOMC could trigger a sharp rebound in mega-cap technology and Nasdaq exposure, causing this value/defensive tilt to lag.; Oil prices could fall on weaker demand data or easing geopolitical risk, hurting the energy allocation.; Healthcare could reverse if policy headlines, reimbursement concerns, or profit-taking follow its recent strong move.; Financials and regional credit sentiment could deteriorate if yield-curve, commercial real estate, or deposit concerns re-emerge.; Broad risk-off conditions around inflation or labor data could pull all equity sectors down despite defensive tilts. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Defensive equity tilt (healthcare, dividend, low-vol, staples) plus aerospace/defense to navigate hot inflation prints and FOMC risk within the one-month window. | Soft CPI print on June 10 sparks growth/tech rally, leaving defensives behind SPY; Dovish FOMC surprise re-rates long duration/growth above defensives; Healthcare policy headline risk from MedPAC June report; Energy/oil spike feeds back into cyclicals outperforming defensives |
| xai-grok-4-3 | xai | portfolio | HEALTHCARE | 3 | 0.55 | Select holdings with recent positive momentum and event-driven support from inflation data, oil levels, and budget requests within the scoring window. | June 10 CPI release could shift rate expectations and pressure equities; FOMC June 16-17 decision may increase volatility across sectors; July 2 employment report could alter growth outlook before exit |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Stagflationary data and tech weakness favor defensive and inflation-beneficiary sectors over the growth-heavy benchmark into CPI and the June FOMC. | A soft May CPI print or dovish FOMC could spark a sharp growth/tech rebound, leaving this defensive-value tilt behind SPY; Oil price pullback (OPEC supply, demand worries) would hit the 25% energy weight; Healthcare-specific policy headlines (e.g., drug pricing, MedPAC follow-through) could reverse its momentum; Mean reversion: recent defensive outperformance may fade if risk appetite returns |
| google-gemini-3-1-pro | google | portfolio | SHORT_TREASURY | 5 | 0.75 | A defensive allocation favoring short-term Treasuries, gold, and defensive equities to navigate a slowing economy with sticky inflation. | A sudden dovish pivot by the Federal Reserve could spark a broad rally in growth and cyclical equities, causing this defensive portfolio to underperform the S&P 500.; A sharp decline in crude oil prices would negatively impact the energy allocation.; If economic data shows a re-acceleration of growth, cyclical sectors could outperform the selected defensive sectors. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 131.2557326947 | 164.28 | 0.25160247577234784 | 1 |
| CYBERSECURITY | Cybersecurity | 84.2673765497 | 94.26 | 0.11858234894029795 | 2 |
| FINANCIALS | Financials Sector | 52.2778714892 | 55.54 | 0.06239979589593503 | 3 |
| ETHEREUM_ETF | Ethereum ETF | 12.48 | 13.19 | 0.05689102564102555 | 4 |
| AGRICULTURE | Agriculture Commodities | 26.28 | 27.71 | 0.054414003044140014 | 5 |
| REGIONAL_BANKS | Regional Banks | 70.8299840246 | 74.65 | 0.05393218744865558 | 6 |
| HEALTHCARE | Healthcare Sector | 153.8969679262 | 162.17 | 0.053756953013962105 | 7 |
| SMALL_CAP | US Small-Cap Stocks | 284.349149674 | 297.24 | 0.045334583700282094 | 8 |
| TAIWAN | Taiwan Equities | 100.8 | 105.05 | 0.042162698412698374 | 9 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 230.2913182231 | 239.62 | 0.04050817828860853 | 10 |
| BRAZIL | Brazil Equities | 33.5992320887 | 34.96 | 0.040499970585865075 | 11 |
| SMALL_VALUE | US Small-Cap Value | 211.4062513806 | 219.5 | 0.03828528516325003 | 12 |
| LARGE_VALUE | US Large-Cap Value | 237.4283553566 | 246.38 | 0.03770250874186987 | 13 |
| INDUSTRIALS | Industrials Sector | 175.1720963863 | 181.11 | 0.03389754268057277 | 14 |
| JAPAN | Japan Equities | 90.4681556001 | 93.52 | 0.03373390757948225 | 15 |
| UTILITIES | Utilities Sector | 43.7020590091 | 45.13 | 0.032674455695615334 | 16 |
| MOMENTUM | US Momentum Equities | 311.2959150928 | 321.2 | 0.03181565972122535 | 17 |
| INDIA | India Equities | 47.54 | 49.02 | 0.031131678586453493 | 18 |
| SEMICONDUCTORS | Semiconductors | 591.01 | 607.73 | 0.02829055345933229 | 19 |
| LOW_VOL | US Low Volatility Equities | 73.5018077699 | 75.5 | 0.027185620200735894 | 20 |
| TECHNOLOGY | Technology Sector | 180.555834376 | 185.35 | 0.026552260914572967 | 21 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.3846357834 | 213.5 | 0.024547703324524495 | 22 |
| TOTAL_US_MARKET | Total US Stock Market | 362.6251326516 | 371.45 | 0.024336061000158837 | 23 |
| NASDAQ100 | Nasdaq 100 | 707.0505724369 | 723.28 | 0.022953701185990383 | 24 |
| SP500 | S&P 500 | 735.175961906 | 751.71 | 0.022489905751453376 | 25 |
| EUROPE | Europe Equities | 86.702197742 | 88.41 | 0.019697335274959427 | 26 |
| BITCOIN_ETF | Bitcoin ETF | 35.14 | 35.81 | 0.01906659077973827 | 27 |
| EMERGING_MARKETS | Emerging Markets | 58.3817902401 | 59.49 | 0.018982113349768737 | 28 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.4775751439 | 70.73 | 0.018026317894745514 | 29 |
| UNITED_KINGDOM | United Kingdom Equities | 45.6222225275 | 46.41 | 0.017267406734188473 | 30 |
| MID_CAP | US Mid-Cap Stocks | 74.5445576885 | 75.7 | 0.015500022366867539 | 31 |
| US_DOLLAR | US Dollar | 28.01 | 28.36 | 0.012495537308104154 | 32 |
| AUSTRALIA | Australia Equities | 27.8556794815 | 28.2 | 0.012360873075405454 | 33 |
| LARGE_GROWTH | US Large-Cap Growth | 121.9153230096 | 123.3 | 0.011357694473655089 | 34 |
| CANADA | Canada Equities | 57.759972862 | 58.38 | 0.010734546906408182 | 35 |
| BROAD_AI_TECH | Broad AI Technology | 63.1595554637 | 63.83 | 0.010615092702565443 | 36 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.6353690554 | 116.85 | 0.010503974298884833 | 37 |
| SOFTWARE | Software | 92.9331220295 | 93.88 | 0.010188810510416646 | 38 |
| MEXICO | Mexico Equities | 73.681841173 | 74.24 | 0.00757525623836508 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.2733722482 | 95.96 | 0.007206921888009088 | 40 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.2527715933 | 79.75 | 0.006273956061140895 | 41 |
| DIVIDEND | US Dividend Equities | 32.1342028306 | 32.26 | 0.003914743740902837 | 42 |
| SOUTH_KOREA | South Korea Equities | 184.05 | 184.75 | 0.00380331431676173 | 43 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.8796991393 | 48.02 | 0.002930278661355201 | 44 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.1929841488 | 91.46 | 0.0029280306340706552 | 45 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.5543704621 | 93.82 | 0.0028393065613925295 | 46 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.4707909098 | 93.71 | 0.002559185472505776 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.7529961512 | 106.94 | 0.00175174332845085 | 48 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.0408534645 | 98.18 | 0.0014192709526992253 | 49 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 50 |
| TIPS | Treasury Inflation-Protected Securities | 108.2610860768 | 108.12 | -0.0013032021191797805 | 51 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.0299816804 | 107.71 | -0.0029619710697226243 | 52 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.804630302 | 84.49 | -0.0037100604162717543 | 53 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.5164741149 | 83.2 | -0.003789361539192959 | 54 |
| COMMUNICATIONS | Communication Services Sector | 111.1847704111 | 110.51 | -0.006068910414664397 | 55 |
| MATERIALS | Materials Sector | 50.5806478857 | 50.26 | -0.0063393392355233225 | 56 |
| SOUTH_AFRICA | South Africa Equities | 63.7406034284 | 63.28 | -0.007226216942194386 | 57 |
| REAL_ESTATE | Real Estate Sector | 44.5839688649 | 44.23 | -0.007939375383394287 | 58 |
| EURO | Euro | 106.4588921549 | 105.42 | -0.00975862263706806 | 59 |
| YEN | Japanese Yen | 57.23 | 56.48 | -0.01310501485235016 | 60 |
| CHINA | China Equities | 53.9451825102 | 53.19 | -0.013999072300055926 | 61 |
| COPPER | Copper | 38.6 | 37.75 | -0.022020725388601115 | 62 |
| GOLD | Gold | 80.07 | 77.51 | -0.03197202447858105 | 63 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 128.87 | 124.7 | -0.032358190424458755 | 64 |
| ENERGY | Energy Sector | 56.9843046387 | 54.82 | -0.03798071508325729 | 65 |
| BROAD_COMMODITIES | Broad Commodities | 17.38 | 16.42 | -0.05523590333716899 | 66 |
| SILVER | Silver | 59.01 | 54.14 | -0.08252838501948823 | 67 |
| METALS_MINING | Metals and Mining | 116.019278897 | 103.24 | -0.11014789109614487 | 68 |
| SOLAR | Solar Energy | 61.83 | 54.95 | -0.11127284489729894 | 69 |
| OIL | Crude Oil | 131.3 | 109.01 | -0.16976389946686976 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 30.0 | 0.053756953013962105 | 0.01612708590418863 | Strongest recent momentum (+5.6% 7d, +7.7% 30d), defensive sector resilient to hot inflation and Fed-on-hold rate pressure. |
| anthropic-claude-fable-5 | ENERGY | 25.0 | -0.03798071508325729 | -0.009495178770814322 | Brent ~$92 with stagflationary CPI/PPI prints; energy equities benefit from elevated oil and inflation hedging flows. |
| anthropic-claude-fable-5 | LOW_VOL | 15.0 | 0.027185620200735894 | 0.004077843030110384 | Defensive factor outperforming amid tech selloff; cushions downside vs SPY if inflation surprises keep rates elevated. |
| anthropic-claude-fable-5 | CONSUMER_STAPLES | 15.0 | -0.003789361539192959 | -0.0005684042308789439 | Defensive holding showing positive recent returns while growth-heavy benchmark corrects. |
| anthropic-claude-fable-5 | LARGE_VALUE | 15.0 | 0.03770250874186987 | 0.00565537631128048 | Value over growth in a high-rate, reaccelerating-inflation regime; outperforming SPY over 30d and 6m. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.053756953013962105 | 0.01612708590418863 | Defensive leadership with strong recent momentum (+7.7% 30d) amid sticky inflation and pre-FOMC uncertainty. |
| anthropic-claude-opus-4-7 | DIVIDEND | 25.0 | 0.003914743740902837 | 0.0009786859352257093 | Quality dividend tilt outperforming in choppy tape; defensive carry with reasonable valuation. |
| anthropic-claude-opus-4-7 | LOW_VOL | 20.0 | 0.027185620200735894 | 0.005437124040147179 | Defensive factor outperforming sharply in recent week; hedges drawdown risk into hot CPI/FOMC. |
| anthropic-claude-opus-4-7 | CONSUMER_STAPLES | 15.0 | -0.003789361539192959 | -0.0005684042308789439 | Defensive sector with positive recent return; cushions against growth/tech rollover. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 10.0 | 0.04050817828860853 | 0.004050817828860853 | Elevated defense budget catalyst ($200B Iran request) supports orders; steady momentum. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.053756953013962105 | 0.01612708590418863 | Strong recent momentum (+7.7% 30d, +5.6% 7d) as a defensive sector outperforming during broad market pullback; MedPAC report catalyst within window. |
| anthropic-claude-opus-4-8 | DIVIDEND | 20.0 | 0.003914743740902837 | 0.0007829487481805675 | Defensive quality dividend tilt holding up well (+2.4% 30d) amid sticky inflation and recent equity weakness. |
| anthropic-claude-opus-4-8 | LARGE_VALUE | 20.0 | 0.03770250874186987 | 0.007540501748373974 | Value held up far better than growth during the tech-led selloff; sticky inflation and elevated rates favor value over growth. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 15.0 | 0.04050817828860853 | 0.00607622674329128 | Defense budget tailwind ($200B request) and geopolitical risk; steady positive momentum with low recent drawdown. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.0029280306340706552 | 0.0004392045951105983 | Cash-like ballast given hot CPI/PCE/PPI prints, FOMC on hold, and broad equity/tech drawdown risk into June CPI and FOMC. |
| google-gemini-3-1-pro | SHORT_TREASURY | 30.0 | 0.0029280306340706552 | 0.0008784091902211966 | Provides a high risk-free yield and capital preservation in a late-cycle environment with elevated rates. |
| google-gemini-3-1-pro | HEALTHCARE | 25.0 | 0.053756953013962105 | 0.013439238253490526 | A defensive equity sector that tends to outperform during periods of slowing economic growth and rising unemployment. |
| google-gemini-3-1-pro | GOLD | 20.0 | -0.03197202447858105 | -0.006394404895716211 | Acts as a hedge against persistent inflation and potential market volatility. |
| google-gemini-3-1-pro | ENERGY | 15.0 | -0.03798071508325729 | -0.005697107262488593 | Benefits from elevated crude oil prices and provides a hedge against supply-side inflation shocks. |
| google-gemini-3-1-pro | CONSUMER_STAPLES | 10.0 | -0.003789361539192959 | -0.00037893615391929595 | Offers defensive equity exposure with stable demand despite a weakening consumer environment. |
| openai-gpt-5-5 | HEALTHCARE | 30.0 | 0.053756953013962105 | 0.01612708590418863 | Recent relative strength and defensive characteristics should help if hot inflation data or the FOMC pressures high-duration growth equities. |
| openai-gpt-5-5 | ENERGY | 25.0 | -0.03798071508325729 | -0.009495178770814322 | High oil price backdrop and persistent inflation favor energy-sector earnings and provide a hedge against renewed commodity or geopolitical risk. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.06239979589593503 | 0.012479959179187006 | Value-oriented exposure with recent positive momentum; higher-for-longer rates and proposed capital requirement relief can support bank and capital-markets sentiment. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 15.0 | 0.04050817828860853 | 0.00607622674329128 | Defense budget and geopolitical-risk support offer idiosyncratic demand drivers with better recent trend than broad equities. |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 10.0 | 0.024547703324524495 | 0.0024547703324524495 | Adds diversified US equity exposure while reducing mega-cap growth concentration after recent Nasdaq and technology weakness. |
| xai-grok-4-3 | HEALTHCARE | 40.0 | 0.053756953013962105 | 0.021502781205584843 | Strong recent 30d return of +7.72% and defensive positioning amid elevated CPI at 3.8% YoY. |
| xai-grok-4-3 | ENERGY | 30.0 | -0.03798071508325729 | -0.011394214524977186 | Positive 30d return of +3.03% with oil prices at WTI ~$88.68 and Brent ~$92.25. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 30.0 | 0.04050817828860853 | 0.01215245348658256 | Pentagon requested $200B additional defense funding, providing sector-specific catalyst. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.053756953013962105 | 0.030965967739145048 | 0.008476061987691672 | 0.22063650803320278 |  | True | True |
| openai-gpt-5-5 | HEALTHCARE | 5 | 0.56 | 0.053756953013962105 | 0.027642863388305045 | 0.005152957636851668 | 0.2239596123840428 |  | True | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.053756953013962105 | 0.02602530947754343 | 0.003535403726090052 | 0.22557716629480443 |  | True | True |
| xai-grok-4-3 | HEALTHCARE | 3 | 0.55 | 0.053756953013962105 | 0.022261020167190216 | -0.00022888558426316027 | 0.22934145560515762 |  | False | True |
| anthropic-claude-fable-5 | HEALTHCARE | 5 | 0.55 | 0.053756953013962105 | 0.015796722243886226 | -0.00669318350756715 | 0.23580575352846161 |  | False | True |
| google-gemini-3-1-pro | SHORT_TREASURY | 5 | 0.75 | 0.0029280306340706552 | 0.001847199131587623 | -0.020642706619865753 | 0.24975527664076022 |  | False | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | -0.00669318350756715 | 0.47968999999999995 | -0.013953143712746046 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | ece8832897fc671b878a78d24f00b0b9df3c55be8fdcd9dab7a47d1c6017b85e |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | 23452c2b688f91ed943bb18b028f5784198d52656f1859277ed7471072fc8028 |
| market_data/universe_trailing_returns.csv | fb0445899b63879e4c6319181b3a43900b50b5067d75898ce0bb26545c15b23f |
| market_data/universe_trailing_returns.md | 9c4216da7bd6ce198b94fe517555b225a3a2edabfdc27c4369e4a0a9d7cf1bbd |
| market_data/universe_trailing_returns.json | af72be0d0f88f61681228f00b7d0e92e61b2db9dd90eb5678f6320b5cd7e0c43 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 0bd98511aab2393526d4be003d288d2b9707db842432f87e9f88c3f360d85d5f | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 26687ca779e2f9f1756761870e3871c238bbeb621476454a94de8cf9eda7aae8 | yes |
| Final briefing | research/final_briefing.md | model-facing | ece8832897fc671b878a78d24f00b0b9df3c55be8fdcd9dab7a47d1c6017b85e | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
