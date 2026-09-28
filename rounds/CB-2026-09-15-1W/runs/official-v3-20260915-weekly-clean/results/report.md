# CapitalBench Report: CB-2026-09-15-1W / official-v3-20260915-weekly-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260915-weekly-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-15-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-15
- Decision deadline: 2026-09-15T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-15
- Exit date: 2026-09-22
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.58 | The market is facing a key FOMC decision with recent weakness in semiconductors and some commodities, while oil has surged on supply disruptions. | The FOMC decision could cause broad market volatility.; The Saudi pipeline disruption could be resolved quickly, reversing oil's gains. |
| anthropic-claude-opus-5 | anthropic | portfolio | TAIWAN | 3 | 0.5767 | Breadth is very weak (positive asset share 16% over 5 sessions) with high cross-sectional dispersion (2.6%). The week's damage is concentrated in semis/AI supply chain (SOX -5.9%) and precious/industrial metals, while oil spiked on a Saudi pipeline outage. FOMC on Sept 16 is the dominant in-window catalyst and can trigger a sharp mean-reversion in the oversold high-beta complex. I treat the deepest single-week drawdowns with strong prior trends (Taiwan, Korea, silver, copper, metals-mining) as overreaction candidates, while the crowded oil and cybersecurity spikes look like already-extended moves. | A hawkish FOMC outcome on Sept 16 could extend the sell-off in high-beta EM and precious metals rather than reverse it.; Taiwan and South Korea carry beta of 2.3 and 3.4, so a further semiconductor drawdown magnifies losses within the one-week window.; The Saudi pipeline disruption could escalate, driving an oil-led risk-off shock that hits metals and EM equity simultaneously.; China fixed-asset investment -7.2% and real estate -19.9% argue that copper and metals weakness may be demand-driven rather than technical. |
| xai-grok-4-5 | xai | portfolio | METALS_MINING | 3 | 0.6 | Low cross-sectional dispersion with SPY near flat; sharp pullbacks in metals, Korea, silver, semis and copper after prior strength create selective reversal setups ahead of FOMC, while oil shows supported strength on supply disruption and crypto retains medium-term momentum. | FOMC decision and press conference on Sep 16 could reverse risk assets broadly; Unresolved Saudi pipeline disruption may extend oil volatility and spill into commodities; High-beta EM and semi names remain vulnerable to further tech/AI rotation or dollar strength; Low positive-asset share indicates fragile breadth if macro data disappoints mid-week |
| openai-gpt-6-astra | openai | portfolio | SP500 | 2 | 0.55 | Dispersion of 2.61 percentage points and only 15.94% positive five-session returns indicate a concentrated, risk-sensitive market. The unresolved pipeline disruption independently supports oil, whereas weak Chinese investment and a stronger dollar challenge industrial-metal rebounds. Selected technology-linked pullbacks merit reversal consideration, but the September 16 FOMC decision makes broad mean reversion uncertain. Estimates concern the entry-close-to-exit-close window, not recovery before entry. | A rapid pipeline restart could unwind oil strength, while prolonged disruption could intensify inflation pressure and hurt energy-importing markets.; The September 16 FOMC decision could raise yields and strengthen the dollar, overwhelming reversal signals.; Semiconductor selling could persist; Taiwan and South Korea share substantial technology and global-trade sensitivity.; Weak Chinese investment could transmit further demand pressure to metals and emerging-market assets.; A rebound before the September 15 entry close would consume some of the forecast reversal opportunity. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | TAIWAN | 3 | 0.57 | SPY is down 1.2% over five sessions with only 16% of assets positive, a semiconductor-led shock (SOX -5.9% on Sept 14) and a broad breadth-negative tape. The FOMC decision on Sept 16 sits inside the window with the 10y at 4.97% and oil spiking to ~$106 Brent on a Saudi pipeline disruption; this is an event-driven, high-dispersion week where sharp one-week losers with intact prior trends (Taiwan, EM, South Africa, Korea, metals) offer the cleanest mean-reversion setups, while oil continuation is real but late and headline-dependent. | FOMC decision Sept 16 with the 10y at 4.97% could drive a hawkish repricing that hits high-beta EM and Asian equities harder than SPY; Semiconductor selloff may continue, dragging Taiwan and Korea further regardless of prior trend; Oil above $105 from the Saudi pipeline disruption could either extend (hurting EM importers) or collapse if repaired, adding two-way volatility; Dollar strength (DXY 99.41, rising) pressures unhedged EM and South Africa returns; China data show weak retail sales and -19.9% real-estate investment, limiting EM demand tailwinds |
| xai-grok-4-6 | xai | portfolio | TAIWAN | 3 | 0.5633 | SPY is only mildly negative with very low 5-session active-return dispersion and weak breadth, while an unknown FOMC outcome hits mid-window. Shock-lane Asia/tech and metals sold off hard versus a still-positive prior active trend, so the week is mixed: possible mean-reversion in quality pullbacks versus event-driven continuation risk in oil and crypto. | Unknown Sep 16 FOMC decision and press conference can reverse high-beta Asia and metals mean-reversion.; Semiconductor-index shock may continue into Taiwan/Korea rather than fade.; Unresolved Saudi pipeline disruption can keep oil volatile and crowd out EM/metals rebounds.; China PMI below 50 and weak fixed-asset investment can cap copper and mining rebounds. |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | FOMC decision and oil supply disruption create short-term volatility; recent equity pullbacks in Asia and metals show mixed reversal potential while oil and cyber show continuation signals. | FOMC outcome uncertainty on September 16; Oil pipeline disruption duration unresolved; Weekly volatility in crypto and semiconductors |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 18.2 | 20.76 | 0.14065934065934083 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 43.11 | 48.83 | 0.1326838320575272 | 2 |
| SEMICONDUCTORS | Semiconductors | 542.11 | 607.46 | 0.12054749036173473 | 3 |
| SOUTH_KOREA | South Korea Equities | 176.49 | 192.62 | 0.09139328007252523 | 4 |
| TAIWAN | Taiwan Equities | 106.67 | 115.11 | 0.07912252742101811 | 5 |
| COPPER | Copper | 38.67 | 41.43 | 0.07137315748642359 | 6 |
| TECHNOLOGY | Technology Sector | 183.74 | 196.27 | 0.06819418743877215 | 7 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 118.95 | 126.47 | 0.0632198402690205 | 8 |
| MOMENTUM | US Momentum Equities | 299.51 | 317.9 | 0.06140028713565493 | 9 |
| NASDAQ100 | Nasdaq 100 | 704.54 | 747.46 | 0.060919181309790904 | 10 |
| BROAD_AI_TECH | Broad AI Technology | 62.96 | 66.72 | 0.05972045743329102 | 11 |
| SILVER | Silver | 57.53 | 60.73 | 0.05562315313749333 | 12 |
| LARGE_GROWTH | US Large-Cap Growth | 120.45 | 126.7 | 0.051888750518887417 | 13 |
| BIOTECH | Biotechnology | 154.03 | 161.87 | 0.05089917548529499 | 14 |
| EMERGING_MARKETS | Emerging Markets | 59.22 | 61.1 | 0.031746031746031855 | 15 |
| SOLAR | Solar Energy | 45.09 | 46.5 | 0.031270791749833604 | 16 |
| CHINA | China Equities | 52.91 | 54.25 | 0.02532602532602546 | 17 |
| METALS_MINING | Metals and Mining | 109.44 | 111.94 | 0.02284356725146197 | 18 |
| TOTAL_US_MARKET | Total US Stock Market | 372.84 | 381.27 | 0.022610234953331254 | 19 |
| SP500 | S&P 500 | 757.39 | 773.38 | 0.0211119766566763 | 20 |
| JAPAN | Japan Equities | 96.92 | 98.78 | 0.01919108543128356 | 21 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.53 | 72.71 | 0.01649657486369338 | 22 |
| CYBERSECURITY | Cybersecurity | 101.0 | 102.575 | 0.015594059405940719 | 23 |
| GOLD | Gold | 80.78 | 82.03 | 0.015474127259222481 | 24 |
| INDIA | India Equities | 47.59 | 48.29 | 0.01470897247320857 | 25 |
| HEALTHCARE | Healthcare Sector | 167.66 | 169.89 | 0.01330072766312762 | 26 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 110.88 | 112.33 | 0.013077200577200632 | 27 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 80.71 | 81.75 | 0.012885639945483973 | 28 |
| BRAZIL | Brazil Equities | 37.78 | 38.26 | 0.012705134992059275 | 29 |
| SOFTWARE | Software | 105.55 | 106.75 | 0.0113690194220748 | 30 |
| US_DOLLAR | US Dollar | 28.22 | 28.48 | 0.009213323883770386 | 31 |
| INDUSTRIALS | Industrials Sector | 168.85 | 170.27 | 0.008409831211134255 | 32 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.87 | 47.26 | 0.008320887561339863 | 33 |
| CANADA | Canada Equities | 60.29 | 60.76 | 0.007795654337369395 | 34 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 104.28 | 105.09 | 0.007767548906789434 | 35 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 92.99 | 93.71 | 0.007742768039574077 | 36 |
| SMALL_CAP | US Small-Cap Stocks | 285.14 | 287.21 | 0.00725959177947666 | 37 |
| AUSTRALIA | Australia Equities | 28.89 | 29.09 | 0.00692281066112832 | 38 |
| MEXICO | Mexico Equities | 74.03 | 74.46 | 0.005808456031338505 | 39 |
| EUROPE | Europe Equities | 88.96 | 89.43 | 0.005283273381295084 | 40 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.85 | 96.25 | 0.004173187271778955 | 41 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 90.82 | 91.16 | 0.0037436687954195413 | 42 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.38 | 78.67 | 0.00369992344985981 | 43 |
| SOUTH_AFRICA | South Africa Equities | 68.92 | 69.15 | 0.0033372025536855254 | 44 |
| MID_CAP | US Mid-Cap Stocks | 73.23 | 73.47 | 0.0032773453502661365 | 45 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.24 | 91.45 | 0.0023016220955722755 | 46 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.51 | 91.57 | 0.0006556660474263953 | 47 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 48 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 214.0 | 214.0 | 0.0 | 48 |
| MUNICIPAL_BONDS | Municipal Bonds | 102.87 | 102.75 | -0.0011665208515602155 | 50 |
| TIPS | Treasury Inflation-Protected Securities | 105.79 | 105.56 | -0.002174118536723779 | 51 |
| UNITED_KINGDOM | United Kingdom Equities | 47.8 | 47.67 | -0.0027196652719664316 | 52 |
| LARGE_VALUE | US Large-Cap Value | 253.49 | 252.67 | -0.003234841611108985 | 53 |
| MATERIALS | Materials Sector | 50.73 | 50.53 | -0.0039424403705893285 | 54 |
| COMMUNICATIONS | Communication Services Sector | 114.03 | 113.53 | -0.0043848110146452735 | 55 |
| SMALL_VALUE | US Small-Cap Value | 217.68 | 216.69 | -0.004547960308710075 | 56 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.96 | 212.8 | -0.005421574126004858 | 57 |
| EURO | Euro | 106.49 | 105.65 | -0.007888064607005196 | 58 |
| AGRICULTURE | Agriculture Commodities | 28.88 | 28.55 | -0.011426592797783908 | 59 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.73 | 82.73 | -0.011943150603129116 | 60 |
| REAL_ESTATE | Real Estate Sector | 43.07 | 42.5 | -0.013234269793359621 | 61 |
| YEN | Japanese Yen | 59.13 | 58.21 | -0.015558937933367156 | 62 |
| DIVIDEND | US Dividend Equities | 34.33 | 33.74 | -0.01718613457617235 | 63 |
| UTILITIES | Utilities Sector | 41.32 | 40.53 | -0.019119070667957372 | 64 |
| LOW_VOL | US Low Volatility Equities | 73.42 | 71.94 | -0.020157995096703907 | 65 |
| FINANCIALS | Financials Sector | 56.85 | 54.8 | -0.036059806508355385 | 66 |
| BROAD_COMMODITIES | Broad Commodities | 20.1 | 19.36 | -0.03681592039801007 | 67 |
| REGIONAL_BANKS | Regional Banks | 74.05 | 71.19 | -0.038622552329507065 | 68 |
| ENERGY | Energy Sector | 65.93 | 61.78 | -0.0629455483088125 | 69 |
| OIL | Crude Oil | 161.86 | 144.08 | -0.10984801680464595 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | TAIWAN | 35.0 | 0.07912252742101811 | 0.027692884597356335 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | EMERGING_MARKETS | 35.0 | 0.031746031746031855 | 0.011111111111111148 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SOUTH_AFRICA | 30.0 | 0.0033372025536855254 | 0.0010011607661056575 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | TAIWAN | 35.0 | 0.07912252742101811 | 0.027692884597356335 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SOUTH_KOREA | 35.0 | 0.09139328007252523 | 0.03198764802538383 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SILVER | 30.0 | 0.05562315313749333 | 0.016686945941247998 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 35.0 | 0.12054749036173473 | 0.042191621626607154 | V3 selected model rank 2: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | METALS_MINING | 35.0 | 0.02284356725146197 | 0.007995248538011689 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOUTH_KOREA | 30.0 | 0.09139328007252523 | 0.027417984021757567 | V3 selected model rank 4: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | TAIWAN | 35.0 | 0.07912252742101811 | 0.027692884597356335 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 65.0 | 0.0211119766566763 | 0.013722784826839597 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | SP500 | 100.0 | 0.0211119766566763 | 0.0211119766566763 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | METALS_MINING | 35.0 | 0.02284356725146197 | 0.007995248538011689 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | SOUTH_KOREA | 35.0 | 0.09139328007252523 | 0.03198764802538383 | V3 selected model rank 2: overreaction with 60% estimated probability of beating SPY. |
| xai-grok-4-5 | COPPER | 30.0 | 0.07137315748642359 | 0.021411947245927074 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | TAIWAN | 35.0 | 0.07912252742101811 | 0.027692884597356335 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | SOUTH_AFRICA | 35.0 | 0.0033372025536855254 | 0.0011680208937899339 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | EMERGING_MARKETS | 30.0 | 0.031746031746031855 | 0.009523809523809556 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.58 | 0.12054749036173473 | 0.07760485418637642 | 0.056492877529700114 | 0.06305448647296441 |  | True | True |
| anthropic-claude-opus-5 | TAIWAN | 3 | 0.5767 | 0.07912252742101811 | 0.07636747856398815 | 0.05525550190731185 | 0.06429186209535268 |  | True | True |
| xai-grok-4-5 | METALS_MINING | 3 | 0.6 | 0.02284356725146197 | 0.061394843809322586 | 0.040282867152646284 | 0.07926449685001824 |  | True | True |
| openai-gpt-6-astra | SP500 | 2 | 0.55 | 0.0211119766566763 | 0.04141566942419593 | 0.02030369276751963 | 0.0992436712351449 |  | True | True |
| anthropic-claude-fable-5-1 | TAIWAN | 3 | 0.57 | 0.07912252742101811 | 0.039805156474573146 | 0.018693179817896845 | 0.10085418418476769 |  | True | True |
| xai-grok-4-6 | TAIWAN | 3 | 0.5633 | 0.07912252742101811 | 0.03838471501495583 | 0.017272738358279527 | 0.102274625644385 |  | True | True |
| xai-grok-4-3 | SP500 | 1 | 0.5 | 0.0211119766566763 | 0.0211119766566763 | 0.0 | 0.11954736400266452 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c1c7548c0f9112f28aa9d443589af76d1b1ebaed1e3a888d75613a1f44b4a493 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 0805f88862698fd79519a590a0c3a4955d4b57de5ecdbd5f09d3113687a2ae4b |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | c4fd71918229a9f4d2446e5b2473e7e4c5e096980911a1af6f968414683e8dea |
| market_data/universe_decision_context.md | 50d32f2b1b22ff918c265457e4503655b770a00b83930c3d92f4b48715924d92 |
| market_data/universe_decision_context.json | 77802714f86f56bb2de0e74acee97750d99261cc188db6527394bae2b0aaa29c |
| market_data/decision_context_source_history.json | 8f8e737a69bd1e796f01c575170ca6c416f9a2b142f84d0fe156bed573f17863 |
| market_data/universe_quality_evidence.md | af11868649a704c3722cf59eb4be004a3117c00884b9799fe01854bd6fb0bffa |
| market_data/universe_quality_evidence.json | 89755645b476817f5f11f0ff454177714a3deb21925cea7c59384eba5c0a211b |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a4e8208ba51f7c117beac0ca95bb60d9f736d4c6823de16063aef1ff5aeee26c | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c595c5eb1264cdf104cf396280f12b30dc27a95bc430da49d282eba687055ea5 | yes |
| Final briefing | research/final_briefing.md | model-facing | c1c7548c0f9112f28aa9d443589af76d1b1ebaed1e3a888d75613a1f44b4a493 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
