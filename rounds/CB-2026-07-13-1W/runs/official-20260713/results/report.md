# CapitalBench Report: CB-2026-07-13-1W / official-20260713

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260713
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-13-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-13
- Decision deadline: 2026-07-14T07:30:00Z
- Horizon: one week
- Entry date: 2026-07-13
- Exit date: 2026-07-20
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | OIL | 1 | 0.65 | Geopolitical supply risk dominates the short scoring window; oil exposure offers the clearest path to outperformance versus SPX. | Rapid diplomatic de-escalation reversing oil gains; Higher-than-expected OPEC supply response; Weaker global demand data released during the window |
| openai-gpt-5-5 | openai | portfolio | OIL | 3 | 0.58 | Position for continued geopolitical risk premium in crude oil through the July 14 blockade resumption and related uncertainty, with energy equities as secondary beneficiaries. Avoid rate-sensitive bonds and growth-heavy equities given rising yields, CPI risk, and recent semiconductor weakness. | A rapid diplomatic de-escalation or uninterrupted Strait of Hormuz shipping could erase the oil geopolitical premium and cause a sharp crude reversal.; June CPI could come in benign, boosting growth equities and the S&P 500 while reducing the relative appeal of oil and the dollar.; Energy equities may lag crude if investors focus on demand destruction, windfall-tax risk, or broader equity-market weakness.; Oil futures exposure can be hurt by curve movements, inventory data, or position unwinds even if spot geopolitical risk remains elevated. |
| xai-grok-4-5 | xai | portfolio | OIL | 4 | 0.62 | Allocate heavily to oil and energy equities for Hormuz/blockade risk premium, add broad commodities for spillover, and keep a smaller financials sleeve for July 14 bank results and higher yields. | Rapid de-escalation or free transit restoration in the Strait of Hormuz could reverse the oil premium before July 20; USO futures roll and high volatility can produce large drawdowns even if spot crude stays elevated; June CPI or Fed-related testimony could reprice rates and risk assets, pressuring financials and equity energy names; Bank earnings misses on July 14 would undercut the FINANCIALS allocation |
| google-gemini-3-1-pro | google | portfolio | OIL | 3 | 0.85 | Allocating to oil, energy, and defense to capture the upside from the Strait of Hormuz blockade and rising geopolitical tensions. | A rapid diplomatic resolution or lifting of the blockade could cause a sharp reversal in oil prices.; Broader market sell-offs driven by rising Treasury yields and inflation fears could drag down energy equities despite high commodity prices.; Scheduled bank earnings or CPI data could shift market focus away from geopolitical events, reducing momentum in defense and energy. |
| openai-gpt-5-6-sol | openai | portfolio | OIL | 5 | 0.58 | Geopolitical supply risk favors oil-linked assets, while elevated inflation and yields favor the dollar over duration-sensitive assets. Diversifying with financials and Treasury bills reduces dependence on a single commodity outcome. | Rapid de-escalation or uninterrupted Hormuz transit could reverse crude's geopolitical premium after its sharp weekly gain.; A softer-than-expected CPI report could lower yields and weaken the dollar while reducing the relative appeal of value and financial exposures.; Weak JPMorgan or Wells Fargo results, especially on credit quality or net interest income, could pressure financials.; A broad risk-off selloff caused by military escalation could outweigh higher oil prices for energy equities.; Oil's high recent volatility and futures-curve effects could produce a sharp reversal even if geopolitical uncertainty persists. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | ENERGY | 5 | 0.6 | Energy/oil tilt for geopolitical supply shock, defensive equity ballast, and short-duration cash to manage event risk over the one-week window. | Sudden Iran de-escalation or blockade reversal collapses oil premium; Hot June CPI print triggers broad risk-off including energy equities; Healthcare/defensive rotation reverses if bank earnings drive cyclical rally; Oil ETF contango drag if front-month futures roll unfavorably |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.55 | Overweight energy and crude on Hormuz escalation, hedge with T-bills, low-vol equity, and the dollar given inflation and rate risks into CPI and Warsh testimony. | Rapid de-escalation or negotiated Hormuz resolution collapses the oil risk premium, hitting XLE and USO hard; A soft June CPI sparks a broad risk-on rally where underweight tech/beta lags SPY; USO futures-curve backwardation/roll effects and its -22% recent drawdown history show extreme volatility; Dovish Warsh testimony weakens the dollar position and boosts growth equities we don't hold |
| anthropic-claude-opus-4-8 | anthropic | portfolio | ENERGY | 5 | 0.6 | Overweight energy on Hormuz blockade catalyst, balanced with low-beta defensives (healthcare, utilities), financials for earnings, and dollar hedge. | De-escalation in the Strait of Hormuz could reverse the oil and energy rally sharply; Bank earnings disappointment July 14 could drag financials lower; Hot June CPI could pressure rate-sensitive utilities and broad equities |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 13.37 | 14.33 | 0.0718025430067315 | 1 |
| OIL | Crude Oil | 117.79 | 125.51 | 0.06554036845233036 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 35.22 | 36.89 | 0.047416240772288454 | 3 |
| CHINA | China Equities | 52.53 | 54.08 | 0.029506948410432 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 16.9 | 17.38 | 0.028402366863905293 | 5 |
| ENERGY | Energy Sector | 56.74 | 57.94 | 0.021149101163200568 | 6 |
| MEXICO | Mexico Equities | 74.15 | 75.09 | 0.012677006068779528 | 7 |
| COPPER | Copper | 37.94 | 38.42 | 0.01265155508697946 | 8 |
| REAL_ESTATE | Real Estate Sector | 44.7 | 45.23 | 0.011856823266219063 | 9 |
| AGRICULTURE | Agriculture Commodities | 27.72 | 28.02 | 0.010822510822510845 | 10 |
| REGIONAL_BANKS | Regional Banks | 75.12 | 75.89 | 0.010250266240681594 | 11 |
| AUSTRALIA | Australia Equities | 28.35 | 28.52 | 0.005996472663139185 | 12 |
| DIVIDEND | US Dividend Equities | 32.56 | 32.75 | 0.005835380835380821 | 13 |
| SMALL_VALUE | US Small-Cap Value | 219.78 | 220.85 | 0.004868504868504875 | 14 |
| EURO | Euro | 105.01 | 105.37 | 0.003428244929054358 | 15 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.26 | 93.57 | 0.003324040317392196 | 16 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.59 | 84.86 | 0.003191866650904318 | 17 |
| SOFTWARE | Software | 92.7 | 92.98 | 0.0030204962243798317 | 18 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.29 | 93.54 | 0.0026798156286846897 | 19 |
| BRAZIL | Brazil Equities | 35.39 | 35.48 | 0.002543091268719877 | 20 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.71 | 97.95 | 0.002456248081056378 | 21 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.52 | 79.68 | 0.00201207243460777 | 22 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.96 | 107.15 | 0.0017763649962603267 | 23 |
| GOLD | Gold | 75.25 | 75.35 | 0.0013289036544850141 | 24 |
| TIPS | Treasury Inflation-Protected Securities | 107.91 | 108.05 | 0.0012973774441664698 | 25 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5 | 91.56 | 0.0006557377049181135 | 26 |
| UNITED_KINGDOM | United Kingdom Equities | 46.36 | 46.39 | 0.000647109577221805 | 27 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 28 |
| YEN | Japanese Yen | 56.46 | 56.46 | 0.0 | 28 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.38 | 95.37 | -0.00010484378276354178 | 30 |
| FINANCIALS | Financials Sector | 56.07 | 56.04 | -0.0005350454788657366 | 31 |
| CYBERSECURITY | Cybersecurity | 91.84 | 91.79 | -0.000544425087107947 | 32 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.97 | 83.89 | -0.0009527212099559312 | 33 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.89 | 47.82 | -0.0014616830235957279 | 34 |
| CANADA | Canada Equities | 58.73 | 58.62 | -0.0018729780350758007 | 35 |
| EUROPE | Europe Equities | 87.86 | 87.69 | -0.0019348964261325374 | 36 |
| LOW_VOL | US Low Volatility Equities | 76.2683187429 | 76.09 | -0.0023380447588087216 | 37 |
| LARGE_VALUE | US Large-Cap Value | 247.62 | 246.96 | -0.0026653743639447613 | 38 |
| US_DOLLAR | US Dollar | 28.5 | 28.39 | -0.0038596491228070073 | 39 |
| SMALL_CAP | US Small-Cap Stocks | 293.48 | 292.31 | -0.003986643042115379 | 40 |
| MID_CAP | US Mid-Cap Stocks | 75.24 | 74.93 | -0.004120148856990857 | 41 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.9 | 106.4 | -0.004677268475210439 | 42 |
| INDIA | India Equities | 48.79 | 48.55 | -0.004919040787046525 | 43 |
| COMMUNICATIONS | Communication Services Sector | 111.59 | 110.8 | -0.007079487409266116 | 44 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.76 | 69.23 | -0.007597477064220204 | 45 |
| SOLAR | Solar Energy | 53.12 | 52.69 | -0.008094879518072307 | 46 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.23 | 212.42 | -0.008448863371143145 | 47 |
| SP500 | S&P 500 | 749.17 | 742.09 | -0.009450458507414772 | 48 |
| TOTAL_US_MARKET | Total US Stock Market | 369.78 | 366.25 | -0.009546216669370944 | 49 |
| MATERIALS | Materials Sector | 50.58 | 50.03 | -0.01087386318703043 | 50 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.04 | 114.61 | -0.012323336780420635 | 51 |
| INDUSTRIALS | Industrials Sector | 180.37 | 178.12 | -0.012474358263569352 | 52 |
| HEALTHCARE | Healthcare Sector | 161.41 | 159.25 | -0.013382070503686228 | 53 |
| EMERGING_MARKETS | Emerging Markets | 58.79 | 57.93 | -0.014628338152747111 | 54 |
| UTILITIES | Utilities Sector | 45.72 | 44.94 | -0.017060367454068248 | 55 |
| LARGE_GROWTH | US Large-Cap Growth | 121.59 | 119.47 | -0.01743564437864964 | 56 |
| SOUTH_AFRICA | South Africa Equities | 62.76 | 61.63 | -0.018005098789037555 | 57 |
| NASDAQ100 | Nasdaq 100 | 711.74 | 696.06 | -0.02203051676173895 | 58 |
| SILVER | Silver | 52.16 | 50.98 | -0.022622699386503076 | 59 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.05 | 229.27 | -0.024590512656881502 | 60 |
| JAPAN | Japan Equities | 92.72 | 90.43 | -0.02469801553062978 | 61 |
| BIOTECH | Biotechnology | 155.34 | 150.94 | -0.0283249645937943 | 62 |
| SOUTH_KOREA | South Korea Equities | 168.02 | 162.86 | -0.030710629686942048 | 63 |
| TECHNOLOGY | Technology Sector | 181.28 | 175.71 | -0.030725948808473014 | 64 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 120.7 | 116.63 | -0.03371996685998346 | 65 |
| BROAD_AI_TECH | Broad AI Technology | 61.3 | 59.14 | -0.03523654159869494 | 66 |
| MOMENTUM | US Momentum Equities | 314.63 | 302.64 | -0.03810825413978325 | 67 |
| METALS_MINING | Metals and Mining | 102.09 | 97.74 | -0.04260946223920081 | 68 |
| SEMICONDUCTORS | Semiconductors | 585.62 | 558.83 | -0.045746388443017594 | 69 |
| TAIWAN | Taiwan Equities | 101.88 | 95.94 | -0.05830388692579502 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 35.0 | 0.021149101163200568 | 0.007402185407120198 | Energy equities benefit directly from Brent at $83 and the announced US blockade of Iranian shipping resuming July 14, with unresolved Strait of Hormuz control keeping supply-risk premium elevated. |
| anthropic-claude-fable-5 | OIL | 15.0 | 0.06554036845233036 | 0.009831055267849553 | Direct crude exposure to further escalation; negative beta hedges equity downside from the geopolitical shock. |
| anthropic-claude-fable-5 | LOW_VOL | 15.0 | -0.0023380447588087216 | -0.0003507067138213082 | Defensive equity with positive 30d benchmark-relative return; likely to outperform SPY if risk-off from war escalation or a hot June CPI persists. |
| anthropic-claude-fable-5 | SHORT_TREASURY | 25.0 | 0.0006557377049181135 | 0.00016393442622952836 | Cash-like ballast amid rising yields (10y 4.61%), hot inflation data, and Waller flagging possible tightening — duration and equity beta both unattractive. |
| anthropic-claude-fable-5 | US_DOLLAR | 10.0 | -0.0038596491228070073 | -0.0003859649122807008 | Dollar benefits from safe-haven flows and hawkish repricing if June CPI prints hot on energy pass-through. |
| anthropic-claude-opus-4-7 | ENERGY | 35.0 | 0.021149101163200568 | 0.007402185407120198 | Strait of Hormuz blockade resumes July 14; Brent +9.6%, oil supply risk elevated through exit close. XLE beta to oil positive with capital discipline. |
| anthropic-claude-opus-4-7 | OIL | 20.0 | 0.06554036845233036 | 0.013108073690466071 | Direct exposure to crude with blockade reinstatement and unresolved Iran conflict driving supply premium into the scoring window. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 20.0 | -0.013382070503686228 | -0.0026764141007372456 | Defensive sector with strong 30d relative strength (+4.14% vs SPY), low beta, insulated from tech selloff and geopolitical shock. |
| anthropic-claude-opus-4-7 | LOW_VOL | 15.0 | -0.0023380447588087216 | -0.0003507067138213082 | Defensive factor tilt amid elevated volatility from Iran conflict, sticky inflation (CPI 4.2%), and rising 10Y yields. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 10.0 | 0.0006557377049181135 | 6.557377049181135e-05 | Dry powder given rate volatility, hawkish Waller alt-case, and event risk from CPI, bank earnings, TSMC, and Warsh testimony. |
| anthropic-claude-opus-4-8 | ENERGY | 30.0 | 0.021149101163200568 | 0.0063447303489601705 | Hormuz blockade resumes July 14, oil spiked and Brent up 9.6%; energy equities have strong momentum with negative beta to broad market, providing catalyst-driven upside. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | -0.013382070503686228 | -0.0026764141007372456 | Defensive sector with strong recent relative outperformance (+4.14% vs SPX 30d), low beta 0.35, insulated from tech and geopolitical volatility. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | -0.0005350454788657366 | -0.00010700909577314733 | JPMorgan and Wells Fargo Q2 earnings July 14 catalyst with 23.6% forecast S&P EPS growth; strong 30d relative strength and steepening curve support. |
| anthropic-claude-opus-4-8 | US_DOLLAR | 15.0 | -0.0038596491228070073 | -0.0005789473684210511 | Rising 10yr yields, geopolitical risk-off, and blockade escalation favor dollar strength; low volatility hedge with negative beta. |
| anthropic-claude-opus-4-8 | UTILITIES | 15.0 | -0.017060367454068248 | -0.002559055118110237 | Defensive low-beta sector outperforming SPX by 2.07% over 30d, insulated from semiconductor/Asia selloff and geopolitical shock. |
| google-gemini-3-1-pro | OIL | 50.0 | 0.06554036845233036 | 0.03277018422616518 | Directly benefits from the announced US blockade on Iranian shipping and the resulting spike in crude prices. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.021149101163200568 | 0.0063447303489601705 | Energy equities are positioned to capture upside from the 9.6% surge in Brent crude and ongoing Strait of Hormuz tensions. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 20.0 | -0.024590512656881502 | -0.004918102531376301 | Geopolitical escalation and active military involvement in the Strait of Hormuz provide a strong near-term catalyst for defense equities. |
| openai-gpt-5-5 | OIL | 65.0 | 0.06554036845233036 | 0.04260123949401473 | Direct exposure to crude oil, the asset most immediately tied to the unresolved Strait of Hormuz blockade and transit-risk catalyst during the scoring week. |
| openai-gpt-5-5 | ENERGY | 25.0 | 0.021149101163200568 | 0.005287275290800142 | Energy equities should benefit if higher crude prices persist, while providing somewhat less futures-specific volatility than a pure oil position. |
| openai-gpt-5-5 | US_DOLLAR | 10.0 | -0.0038596491228070073 | -0.0003859649122807008 | Dollar exposure offers a modest hedge against risk-off conditions, higher US yields, and inflation-surprise dynamics that could pressure broad equities. |
| openai-gpt-5-6-sol | OIL | 40.0 | 0.06554036845233036 | 0.026216147380932142 | The announced blockade resumption and unresolved Hormuz control create an immediate supply-risk catalyst, with crude offering the most direct upside exposure. |
| openai-gpt-5-6-sol | ENERGY | 25.0 | 0.021149101163200568 | 0.005287275290800142 | Energy equities should benefit from sustained oil-price strength while providing less futures-specific volatility than direct crude exposure. |
| openai-gpt-5-6-sol | US_DOLLAR | 15.0 | -0.0038596491228070073 | -0.0005789473684210511 | Elevated geopolitical risk, higher Treasury yields, and potentially firm CPI support safe-haven and rate-differential demand for the dollar. |
| openai-gpt-5-6-sol | FINANCIALS | 10.0 | -0.0005350454788657366 | -5.350454788657366e-05 | Major-bank earnings are an immediate catalyst, while higher yields and recent sector-relative strength may support financial shares. |
| openai-gpt-5-6-sol | SHORT_TREASURY | 10.0 | 0.0006557377049181135 | 6.557377049181135e-05 | Low-duration Treasury bills preserve capital through a catalyst-heavy week and limit exposure to inflation-driven increases in longer-term yields. |
| xai-grok-4-3 | OIL | 100.0 | 0.06554036845233036 | 0.06554036845233036 | US-Iran blockade resumption July 14 and Strait of Hormuz control assertions create near-term supply disruption risk likely to lift crude prices before July 20 close. |
| xai-grok-4-5 | OIL | 40.0 | 0.06554036845233036 | 0.026216147380932142 | Hormuz control claims, US blockade restart July 14, and Brent already +9.6% create near-term supply-risk premium that can lift crude proxies into the July 20 close. |
| xai-grok-4-5 | ENERGY | 30.0 | 0.021149101163200568 | 0.0063447303489601705 | XLE captures equity leverage to the same oil spike and geopolitical premium while diversifying pure futures-curve risk in USO. |
| xai-grok-4-5 | BROAD_COMMODITIES | 15.0 | 0.028402366863905293 | 0.004260355029585793 | PDBC provides diversified commodity beta that benefits if energy disruption broadens inflation and commodity risk premia this week. |
| xai-grok-4-5 | FINANCIALS | 15.0 | -0.0005350454788657366 | -8.025682182986048e-05 | JPM and WFC report July 14; higher 10y yields and solid bank positioning offer a catalyst path independent of pure energy beta. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | OIL | 1 | 0.65 | 0.06554036845233036 | 0.06554036845233036 | 0.07499082695974513 | 0.006262174554401145 |  | True | True |
| openai-gpt-5-5 | OIL | 3 | 0.58 | 0.06554036845233036 | 0.047502549872534175 | 0.05695300837994895 | 0.024299993134197326 |  | True | True |
| xai-grok-4-5 | OIL | 4 | 0.62 | 0.06554036845233036 | 0.036740975937648246 | 0.04619143444506302 | 0.035061567069083255 |  | True | True |
| google-gemini-3-1-pro | OIL | 3 | 0.85 | 0.06554036845233036 | 0.03419681204374905 | 0.043647270551163825 | 0.03760573096298245 |  | True | True |
| openai-gpt-5-6-sol | OIL | 5 | 0.58 | 0.06554036845233036 | 0.030936544525916473 | 0.040387003033331245 | 0.04086599848081503 |  | True | True |
| anthropic-claude-opus-4-7 | ENERGY | 5 | 0.6 | 0.021149101163200568 | 0.017548712053519527 | 0.0269991705609343 | 0.05425383095321197 |  | True | True |
| anthropic-claude-fable-5 | ENERGY | 5 | 0.55 | 0.021149101163200568 | 0.01666050347509727 | 0.026110961982512042 | 0.05514203953163423 |  | True | True |
| anthropic-claude-opus-4-8 | ENERGY | 5 | 0.6 | 0.021149101163200568 | 0.00042330466591848984 | 0.009873763173333262 | 0.07137923834081301 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | de22781c9668468d55a17811335bc21bcf84f195f66bc969d25f3de32f2ccd0b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 03b5e9792d4c6bade89526a62f43cbdf51184fe03753997a0637de246e708b81 |
| manifest.yaml | 44ff29484957e404e47d6b2e6533fde7c0fb22afdae0edae096e2d854b06d145 |
| market_data/universe_trailing_returns.csv | 3143d3d3a51ee7eb219e7c8bf7e4908568aa4e1d3375a0660c359488744cd8b2 |
| market_data/universe_trailing_returns.md | 36556b4c86167e1ef6c6b0fca3e489889d2705afe148df8ba4a39bf8df092961 |
| market_data/universe_trailing_returns.json | f81b44add4dc75e5716f1a4606a6b70d9c3306deb10d643a7fc5d3d0bf94fc65 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 598d82b383370521b5dbca23c09c84e32c38ae951df3a93a77090b6794af9c22 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 414198418f63d1ba4bd6ad23fbd17d8e01b213627c359bbdc73555b9fa64ea3e | yes |
| Final briefing | research/final_briefing.md | model-facing | de22781c9668468d55a17811335bc21bcf84f195f66bc969d25f3de32f2ccd0b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
