# CapitalBench Report: CB-2026-07-14-1W / official-20260714

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260714
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-14-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-14
- Decision deadline: 2026-07-15T07:30:00Z
- Horizon: one week
- Entry date: 2026-07-14
- Exit date: 2026-07-21
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.55 | One-week window dominated by unresolved Hormuz blockade and rising oil prices, with supportive bank earnings providing secondary tailwind; weak jobs data secondary to energy flow risks. | Rapid de-escalation or diplomatic resolution in Strait of Hormuz could reverse oil gains before July 21 close.; July 15 PPI and retail sales releases could shift rate-cut expectations and pressure energy rotation.; Profit-taking after recent sharp energy and oil moves may cap upside within the scoring window. |
| google-gemini-3-1-pro | google | portfolio | OIL | 4 | 0.75 | Allocating to OIL and ENERGY to capitalize on the Strait of Hormuz blockade. Adding FINANCIALS and SEMICONDUCTORS based on strong recent corporate results. | A rapid de-escalation in the Strait of Hormuz could cause a sharp reversal in oil prices.; TSMC's earnings conference could disappoint, negatively impacting the semiconductor sector.; Broader market volatility could offset sector-specific gains. |
| openai-gpt-5-5 | openai | portfolio | OIL | 4 | 0.59 | Oil and energy have direct support from renewed Middle East supply disruption risk, while semiconductors have TSMC and AI-linked revenue momentum. Financials add exposure to strong reported bank profits and healthier consumer-credit data. | A de-escalation around Iran or improved Strait of Hormuz shipping conditions could sharply reverse oil and energy gains.; TSMC earnings commentary could disappoint despite strong monthly revenue, pressuring semiconductor equities.; Hot PPI, strong retail sales, or hawkish Warsh testimony could lift yields and hurt high-beta equities.; A broad risk-off move from geopolitical escalation could reduce equity exposure benefits even if crude rises. |
| xai-grok-4-5 | xai | portfolio | OIL | 5 | 0.48 | Hormuz military developments and oil price spikes dominate short-term risk premium while TSMC results and bank earnings provide equity catalysts; portfolio overweight these over broad beta or defensive assets for the scoring window. | Rapid Hormuz de-escalation or diplomatic resolution could reverse oil and energy gains sharply; TSMC earnings or guidance disappointment would pressure semiconductors and technology; Hotter-than-expected PPI or Warsh testimony hawkishness could lift yields and hit growth/tech; Broader risk-off from soft labor data revisions or inventory releases could compress high-beta holdings |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Bank earnings strength and geopolitical oil supply risk are the clearest near-term catalysts before the exit close, balanced with core equity beta. | Rapid de-escalation or reopening of the Strait of Hormuz reverses energy/oil gains sharply; Bank earnings enthusiasm fades or profit-taking hits financials after strong run; Hot PPI or hawkish Warsh testimony pressures rate-sensitive equities; Oil futures curve contango erodes USO returns even if spot holds |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.55 | Geopolitical oil catalyst plus concrete earnings catalysts (TSMC, banks) drive tilts toward energy, semiconductors, and financials over the one-week window. | Rapid Hormuz de-escalation or diplomatic resolution could unwind oil and energy gains quickly; TSMC earnings or guidance disappointment could hit high-beta semiconductors hard; Hot PPI or hawkish Warsh Senate testimony could pressure risk assets broadly; Citigroup's decline shows bank earnings reactions are uneven; remaining financial reports may disappoint |
| anthropic-claude-opus-4-7 | anthropic | portfolio | ENERGY | 5 | 0.6 | Tilt toward near-term catalysts: oil/geopolitics (XLE), bank earnings (XLF), TSMC earnings (SMH), and momentum in CIBR. | Sudden Hormuz de-escalation could crush energy trade; Bank earnings disappointment or guidance cuts after strong run-up; TSMC guidance miss hits semis sharply given high beta; Hot PPI or hawkish Warsh testimony pressures risk assets |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 4 | 0.64 | Energy and semiconductors receive the largest weights because their catalysts are both immediate and potentially price-sensitive before July 21. Financial earnings strength and cybersecurity momentum broaden the sources of prospective alpha versus the S&P 500. | A ceasefire, restored Hormuz shipping, or unexpectedly bearish EIA data could sharply reverse oil and energy gains.; TSMC guidance could disappoint elevated expectations, triggering a semiconductor selloff after extreme six-month appreciation.; Warsh testimony or hotter PPI could lift yields and pressure high-duration technology and cybersecurity shares.; Post-earnings profit-taking or renewed concern about bank credit quality could reverse financial-sector strength. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 120.17 | 128.85 | 0.07223100607472732 | 1 |
| BROAD_COMMODITIES | Broad Commodities | 17.08 | 17.65 | 0.03337236533957855 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 36.58 | 37.67 | 0.029797703663204 | 3 |
| ENERGY | Energy Sector | 56.95 | 58.5 | 0.027216856892010588 | 4 |
| COPPER | Copper | 38.54 | 39.53 | 0.02568759730150494 | 5 |
| ETHEREUM_ETF | Ethereum ETF | 14.18 | 14.53 | 0.024682651622002894 | 6 |
| DIVIDEND | US Dividend Equities | 32.2 | 32.82 | 0.019254658385092993 | 7 |
| AGRICULTURE | Agriculture Commodities | 27.63 | 28.15 | 0.01882012305465075 | 8 |
| REAL_ESTATE | Real Estate Sector | 44.48 | 45.2 | 0.01618705035971235 | 9 |
| SMALL_VALUE | US Small-Cap Value | 219.6 | 222.91 | 0.015072859744990952 | 10 |
| CHINA | China Equities | 53.23 | 54.0 | 0.014465526958482133 | 11 |
| REGIONAL_BANKS | Regional Banks | 75.0 | 75.98 | 0.013066666666666782 | 12 |
| HEALTHCARE | Healthcare Sector | 158.29 | 160.25 | 0.012382336218333512 | 13 |
| UNITED_KINGDOM | United Kingdom Equities | 46.31 | 46.77 | 0.009933059814295042 | 14 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.42 | 84.06 | 0.0076720210980580905 | 15 |
| GOLD | Gold | 76.27 | 76.82 | 0.007211223285695567 | 16 |
| SMALL_CAP | US Small-Cap Stocks | 294.51 | 296.54 | 0.006892804998132496 | 17 |
| MEXICO | Mexico Equities | 75.34 | 75.84 | 0.006636580833554451 | 18 |
| EUROPE | Europe Equities | 88.3 | 88.76 | 0.005209513023782586 | 19 |
| LARGE_VALUE | US Large-Cap Value | 246.37 | 247.44 | 0.004343061249340474 | 20 |
| US_DOLLAR | US Dollar | 28.39 | 28.48 | 0.0031701303275801784 | 21 |
| MID_CAP | US Mid-Cap Stocks | 75.57 | 75.72 | 0.001984914648670122 | 22 |
| INDIA | India Equities | 48.73 | 48.78 | 0.001026061974143344 | 23 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.51 | 91.56 | 0.0005463883728553665 | 24 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 25 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.68 | 79.65 | -0.00037650602409644573 | 26 |
| LOW_VOL | US Low Volatility Equities | 75.7692458549 | 75.73 | -0.0005179654945379752 | 27 |
| AUSTRALIA | Australia Equities | 28.71 | 28.68 | -0.0010449320794149175 | 28 |
| TIPS | Treasury Inflation-Protected Securities | 108.01 | 107.88 | -0.0012035922599760163 | 29 |
| FINANCIALS | Financials Sector | 56.18 | 56.11 | -0.0012459950160199629 | 30 |
| EURO | Euro | 105.39 | 105.23 | -0.0015181706044216092 | 31 |
| SILVER | Silver | 53.17 | 53.08 | -0.001692683844273124 | 32 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.6 | 70.47 | -0.0018413597733710763 | 33 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.57 | 95.38 | -0.001988071570576566 | 34 |
| CANADA | Canada Equities | 59.18 | 59.05 | -0.0021966880702940506 | 35 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.55 | 93.31 | -0.00256547300908605 | 36 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.0 | 97.74 | -0.0026530612244898277 | 37 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.96 | 47.83 | -0.0027105921601334737 | 38 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.67 | 93.41 | -0.0027757019323155774 | 39 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.45 | 212.76 | -0.0032326071679550372 | 40 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.21 | 106.85 | -0.003357895718682946 | 41 |
| EMERGING_MARKETS | Emerging Markets | 59.08 | 58.86 | -0.003723764387271511 | 42 |
| TOTAL_US_MARKET | Total US Stock Market | 371.16 | 369.45 | -0.004607177497575221 | 43 |
| SP500 | S&P 500 | 751.83 | 748.28 | -0.004721812111780688 | 44 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.08 | 83.66 | -0.004995242626070429 | 45 |
| BIOTECH | Biotechnology | 155.45 | 154.5 | -0.006111289803795383 | 46 |
| YEN | Japanese Yen | 56.57 | 56.22 | -0.006187024924871887 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.95 | 106.17 | -0.0072931276297335534 | 48 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.9 | 114.87 | -0.008886971527178655 | 49 |
| INDUSTRIALS | Industrials Sector | 180.45 | 178.66 | -0.009919645331116556 | 50 |
| MATERIALS | Materials Sector | 50.64 | 50.1 | -0.010663507109004766 | 51 |
| BRAZIL | Brazil Equities | 36.03 | 35.62 | -0.011379406050513574 | 52 |
| JAPAN | Japan Equities | 93.89 | 92.74 | -0.012248375758866836 | 53 |
| COMMUNICATIONS | Communication Services Sector | 111.45 | 110.03 | -0.01274113952445044 | 54 |
| TAIWAN | Taiwan Equities | 101.88 | 100.58 | -0.012760109933254826 | 55 |
| NASDAQ100 | Nasdaq 100 | 719.69 | 708.97 | -0.014895302143978717 | 56 |
| LARGE_GROWTH | US Large-Cap Growth | 123.23 | 121.33 | -0.015418323460196448 | 57 |
| TECHNOLOGY | Technology Sector | 183.62 | 180.78 | -0.015466724757651651 | 58 |
| BROAD_AI_TECH | Broad AI Technology | 61.96 | 61.0 | -0.015493867010974882 | 59 |
| MOMENTUM | US Momentum Equities | 319.76 | 314.48 | -0.01651238428821611 | 60 |
| UTILITIES | Utilities Sector | 45.69 | 44.92 | -0.01685270299846786 | 61 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.28 | 120.1 | -0.01782793588485454 | 62 |
| SOUTH_AFRICA | South Africa Equities | 63.45 | 62.28 | -0.018439716312056764 | 63 |
| SOFTWARE | Software | 93.63 | 91.82 | -0.01933141087258361 | 64 |
| SOUTH_KOREA | South Korea Equities | 176.98 | 172.9 | -0.023053452367499117 | 65 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.27 | 229.74 | -0.02350490925319848 | 66 |
| SOLAR | Solar Energy | 55.13 | 53.74 | -0.02521313259568292 | 67 |
| METALS_MINING | Metals and Mining | 104.42 | 101.6 | -0.02700632062823216 | 68 |
| SEMICONDUCTORS | Semiconductors | 600.31 | 584.08 | -0.027036031383784853 | 69 |
| CYBERSECURITY | Cybersecurity | 94.73 | 90.58 | -0.04380871951863197 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | 0.027216856892010588 | 0.008165057067603176 | Reimposed Iranian port blockade and Hormuz disruption support oil prices; XLE benefits with lower volatility than USO and negative beta hedges equity downside from the conflict. |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 25.0 | -0.027036031383784853 | -0.006759007845946213 | TSMC June revenue up 67.9% y/y with Q2 earnings call July 16 as a concrete catalyst; Nvidia and Micron momentum confirms strong AI demand. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | -0.0012459950160199629 | -0.0002491990032039926 | Record bank profits and strong markets revenue mid-earnings season; more big-bank and asset-manager reports (BlackRock July 15) can extend sector strength. |
| anthropic-claude-fable-5 | BROAD_COMMODITIES | 15.0 | 0.03337236533957855 | 0.005005854800936782 | Energy-heavy commodity exposure with negative equity beta hedges escalation risk in the Strait of Hormuz while capturing upside if disruption persists. |
| anthropic-claude-fable-5 | SP500 | 10.0 | -0.004721812111780688 | -0.0004721812111780688 | Benchmark ballast to limit tracking error given geopolitical uncertainty. |
| anthropic-claude-opus-4-7 | ENERGY | 35.0 | 0.027216856892010588 | 0.009525899912203706 | Strait of Hormuz blockade reimposed, oil at highs since mid-June, XLE has momentum with catalysts through the week. |
| anthropic-claude-opus-4-7 | FINANCIALS | 30.0 | -0.0012459950160199629 | -0.00037379850480598884 | Record bank profits, JPM/GS strength, strong Q2 earnings momentum continuing with more bank reports and BlackRock July 15. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 20.0 | -0.027036031383784853 | -0.005407206276756971 | TSMC Q2 earnings July 16 with June revenue +67.9% YoY; positive catalyst for SMH. |
| anthropic-claude-opus-4-7 | CYBERSECURITY | 10.0 | -0.04380871951863197 | -0.0043808719518631965 | Strong momentum, +11% 30d, near 52w high, low drawdown; robust trend. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 5.0 | 0.0005463883728553665 | 2.7319418642768323e-05 | Small cash-like ballast against geopolitical/oil reversal risk. |
| anthropic-claude-opus-4-8 | FINANCIALS | 30.0 | -0.0012459950160199629 | -0.00037379850480598884 | Record bank earnings above expectations, strong markets revenue, healthy consumer; strongest 30d relative momentum and near 52w high with earnings tailwind continuing this week. |
| anthropic-claude-opus-4-8 | ENERGY | 25.0 | 0.027216856892010588 | 0.006804214223002647 | Strait of Hormuz blockade reimposed, Brent/WTI at multi-week highs; oil supply risk supports energy equities near-term with low beta to broad market. |
| anthropic-claude-opus-4-8 | OIL | 15.0 | 0.07223100607472732 | 0.010834650911209097 | Direct crude exposure benefits from renewed blockade and unresolved military situation; strong recent momentum tied to geopolitical supply disruption. |
| anthropic-claude-opus-4-8 | SP500 | 20.0 | -0.004721812111780688 | -0.0009443624223561376 | Broad market core exposure given cooling headline inflation and stable labor supporting equities; anchors portfolio to benchmark. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 10.0 | 0.012382336218333512 | 0.0012382336218333513 | Defensive sector with positive 30d relative return and low beta; oversold 7d dip offers rebound potential amid rate uncertainty. |
| google-gemini-3-1-pro | OIL | 40.0 | 0.07223100607472732 | 0.02889240242989093 | The reimposed blockade of Iranian ports and the strategic importance of the Strait of Hormuz present a significant near-term catalyst for crude oil prices. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.027216856892010588 | 0.008165057067603176 | Energy equities are positioned to benefit directly from rising crude prices driven by the Strait of Hormuz blockade and geopolitical tensions. |
| google-gemini-3-1-pro | FINANCIALS | 15.0 | -0.0012459950160199629 | -0.00018689925240299442 | Large U.S. banks reported record profits and strong consumer spending, providing a solid fundamental backdrop for the sector. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 15.0 | -0.027036031383784853 | -0.004055404707567728 | TSMC's strong unaudited June revenue and upcoming earnings conference provide a positive catalyst for the semiconductor sector. |
| openai-gpt-5-5 | OIL | 35.0 | 0.07223100607472732 | 0.025280852126154562 | Renewed blockade of Iranian ports and unresolved Strait of Hormuz conditions create a near-term upside catalyst for crude prices over the one-week window. |
| openai-gpt-5-5 | ENERGY | 25.0 | 0.027216856892010588 | 0.006804214223002647 | Energy equities should benefit if oil strength persists, while offering less direct futures volatility than crude exposure. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | -0.027036031383784853 | -0.006759007845946213 | Strong TSMC June and first-half revenue, a scheduled TSMC earnings conference, and recent strength in Nvidia and Micron support near-term semiconductor sentiment. |
| openai-gpt-5-5 | FINANCIALS | 15.0 | -0.0012459950160199629 | -0.00018689925240299442 | Large-bank earnings exceeded expectations with record profits and strong markets revenue, providing a near-term sector catalyst with lower beta than high-growth technology. |
| openai-gpt-5-6-sol | ENERGY | 35.0 | 0.027216856892010588 | 0.009525899912203706 | The renewed Iranian-port blockade and unresolved Hormuz shipping conditions support near-term oil prices and energy-company cash-flow expectations. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 30.0 | -0.027036031383784853 | -0.008110809415135456 | TSMC's 67.9% June revenue growth and imminent Q2 conference provide a strong near-window catalyst for chip equities. |
| openai-gpt-5-6-sol | FINANCIALS | 20.0 | -0.0012459950160199629 | -0.0002491990032039926 | Record large-bank profits, strong trading revenue, resilient consumer activity, and benign credit metrics support continued earnings-driven strength. |
| openai-gpt-5-6-sol | CYBERSECURITY | 15.0 | -0.04380871951863197 | -0.006571307927794795 | Strong benchmark-relative monthly momentum and limited recent drawdown offer a diversifying growth exposure amid elevated geopolitical tensions. |
| xai-grok-4-3 | ENERGY | 40.0 | 0.027216856892010588 | 0.010886742756804235 | Oil prices at multi-week highs after Hormuz blockade reimposed; unresolved military and shipping risks support further near-term gains in energy equities. |
| xai-grok-4-3 | OIL | 35.0 | 0.07223100607472732 | 0.025280852126154562 | Direct crude exposure benefits from Brent/WTI surge to highest levels since mid-June amid ongoing Strait tensions likely to persist through the week. |
| xai-grok-4-3 | FINANCIALS | 25.0 | -0.0012459950160199629 | -0.0003114987540049907 | Major banks posted record Q2 profits and strong consumer spending data; sector positioned for continued momentum into next week. |
| xai-grok-4-5 | OIL | 35.0 | 0.07223100607472732 | 0.025280852126154562 | Direct crude exposure positioned for continued Hormuz blockade, ship attacks, and unresolved strait control that already lifted WTI/Brent to multi-week highs. |
| xai-grok-4-5 | ENERGY | 25.0 | 0.027216856892010588 | 0.006804214223002647 | Sector leverage to elevated oil prices and geopolitical supply risk with recent price strength and positive 7d momentum. |
| xai-grok-4-5 | SEMICONDUCTORS | 20.0 | -0.027036031383784853 | -0.005407206276756971 | TSMC June revenue surge and scheduled Q2 earnings conference provide near-term catalyst; Nvidia/Micron strength supports AI/chip demand. |
| xai-grok-4-5 | TECHNOLOGY | 10.0 | -0.015466724757651651 | -0.0015466724757651651 | Broad tech exposure capturing Nasdaq leadership, mega-cap AI momentum, and spillover from strong semiconductor results. |
| xai-grok-4-5 | FINANCIALS | 10.0 | -0.0012459950160199629 | -0.0001245995016019963 | Record bank profits, markets-revenue growth, and rising consumer spending reported by major banks support near-term sector resilience. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | ENERGY | 3 | 0.55 | 0.027216856892010588 | 0.03585609612895381 | 0.0405779082407345 | 0.03637490994577351 |  | True | True |
| google-gemini-3-1-pro | OIL | 4 | 0.75 | 0.07223100607472732 | 0.032815155537523386 | 0.03753696764930407 | 0.039415850537203936 |  | True | True |
| openai-gpt-5-5 | OIL | 4 | 0.59 | 0.07223100607472732 | 0.025139159250808004 | 0.029860971362588692 | 0.047091846823919314 |  | True | True |
| xai-grok-4-5 | OIL | 5 | 0.48 | 0.07223100607472732 | 0.025006588095033082 | 0.02972840020681377 | 0.04722441797969424 |  | True | True |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.55 | -0.0012459950160199629 | 0.01755893782888297 | 0.022280749940663657 | 0.05467206824584435 |  | True | True |
| anthropic-claude-fable-5 | ENERGY | 5 | 0.55 | 0.027216856892010588 | 0.0056905238082116845 | 0.010412335919992372 | 0.06654048226651564 |  | True | True |
| anthropic-claude-opus-4-7 | ENERGY | 5 | 0.6 | 0.027216856892010588 | -0.0006086574025796819 | 0.004113154709201006 | 0.072839663477307 |  | True | False |
| openai-gpt-5-6-sol | ENERGY | 4 | 0.64 | 0.027216856892010588 | -0.005405416433930537 | -0.0006836043221498493 | 0.07763642250865786 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 6ad3a950d557dd3259b4d18e28e9b1a5b34a8c3f880340c049e34fe7cdd84dbf |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 03b5e9792d4c6bade89526a62f43cbdf51184fe03753997a0637de246e708b81 |
| manifest.yaml | 1a07ddb34544782e660ed459137f6f34e65ff6002326a6ec2762bc60cc086ddd |
| market_data/universe_trailing_returns.csv | 9e16b248d8cf1fad3108b9f68e4f3dbf01c7b2ec3b9443bf8a868581a872f186 |
| market_data/universe_trailing_returns.md | 7d38f392b65b872feba3d042db6ca21ddd4f7ae599e26f416dec7a01df4a5e18 |
| market_data/universe_trailing_returns.json | 18982ae0e2a6e9c6d4cc881273a50d2e79a03d969d0fa5034a7dbd47a332b9b6 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | b67abd6e7dbd7c70b2e7423532a8c12f4d40f3bf9baf5dd529bf964310c8b382 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | f4b0c4dd9763b7b2f5bfda0dc04a61711c40b94b78143c46d5b1a6664d04d38b | yes |
| Final briefing | research/final_briefing.md | model-facing | 6ad3a950d557dd3259b4d18e28e9b1a5b34a8c3f880340c049e34fe7cdd84dbf | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
