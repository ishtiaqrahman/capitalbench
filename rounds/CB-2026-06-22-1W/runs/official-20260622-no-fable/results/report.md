# CapitalBench Report: CB-2026-06-22-1W / official-20260622-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260622-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-22-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-22
- Decision deadline: 2026-06-23T02:30:00Z
- Horizon: one week
- Entry date: 2026-06-22
- Exit date: 2026-06-29
- Entry rule: Use adjusted close prices on Monday, June 22, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Monday, June 29, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Momentum continuation in semis/momentum factor plus benchmark core, hedged with short-duration Treasuries. | Semiconductor/momentum cohort reverses sharply on tech profit-taking after Nasdaq's -1.3% day; Sticky inflation (core PCE 3.3%, hawkish SEP) triggers risk-off and yield spike hurting growth tilts; Biotech high-beta volatility reverses its recent +6.94% spike; PCE data on June 25 surprises hawkish, pressuring equities into the exit close |
| xai-grok-4-3 | xai | portfolio | SP500 | 3 | 0.55 | SP500 provides baseline; momentum and semiconductors add edge from observed short-term strength without over-concentration. | Reversal in momentum factor after recent gains; Sector-specific pullback in semiconductors on profit-taking; Broader equity weakness if upcoming GDP data disappoints |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 4 | 0.65 | Allocating to high-momentum sectors (Semiconductors, Biotech) and regions (Taiwan, South Korea) to capitalize on strong recent trends over a one-week horizon. | A sudden reversal in the recent strong momentum of semiconductor and technology stocks.; Geopolitical tensions or trade issues affecting Taiwan and South Korea.; High volatility inherent in the biotechnology sector leading to sharp short-term drawdowns.; A broader market risk-off event that disproportionately impacts high-beta, high-growth equities. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.57 | Recent price action favors high-beta momentum, especially semiconductors and Asian tech supply-chain equities. Biotech adds a separate high-upside risk-on sleeve, while avoiding weak commodity, crypto, and software trends. | A hotter-than-expected May PCE report or further rise in Treasury yields could trigger a growth and high-multiple tech selloff.; Semiconductor and Taiwan/Korea exposures are highly correlated, so any AI-chip profit-taking could materially hurt the portfolio.; A broad rotation into value, defensives, or small domestic cyclicals could leave mega-cap tech supply-chain exposure lagging the S&P 500.; Taiwan or Korea currency weakness or regional geopolitical headlines could reduce returns of the country ETFs over the scoring week. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrated in momentum leaders with semiconductor/Asia tech tailwinds; small defensive sleeve against rate and inflation risk into PCE print. | Semiconductor/Asia tech mean-reversion after strong run; Hot May PCE print on 2026-06-26 pressuring rate-sensitive growth; USD strength weighing on Korea/Taiwan ETFs; Geopolitical headline risk around Taiwan Strait; Momentum factor crash if leadership rotates to defensives |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 145.86000061035156 | 158.30999755859375 | 0.08535579937025317 | 1 |
| HEALTHCARE | Healthcare Sector | 150.05999755859375 | 160.74000549316406 | 0.0711715854213586 | 2 |
| CYBERSECURITY | Cybersecurity | 83.50818634033203 | 88.5 | 0.05977633904446411 | 3 |
| REGIONAL_BANKS | Regional Banks | 71.98999786376953 | 74.75 | 0.038338688958615696 | 4 |
| LOW_VOL | US Low Volatility Equities | 73.23999786376953 | 75.58999633789062 | 0.03208627174583234 | 5 |
| SOFTWARE | Software | 87.30999755859375 | 89.88999938964844 | 0.029549901537029077 | 6 |
| UTILITIES | Utilities Sector | 44.720001220703125 | 46.02000045776367 | 0.029069749587992133 | 7 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.18000030517578 | 84.37000274658203 | 0.026648849273225528 | 8 |
| REAL_ESTATE | Real Estate Sector | 44.02000045776367 | 44.91999816894531 | 0.02044519995053551 | 9 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.94000244140625 | 117.12000274658203 | 0.018966419513407384 | 10 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 209.61000061035156 | 213.0500030517578 | 0.016411442351937033 | 11 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.08999633789062 | 87.44999694824219 | 0.0157974290649725 | 12 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.50999450683594 | 239.1300048828125 | 0.01537094161781516 | 13 |
| SMALL_VALUE | US Small-Cap Value | 217.99000549316406 | 221.27999877929688 | 0.01509240425353342 | 14 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.0 | 95.05999755859375 | 0.01127656977227387 | 15 |
| UNITED_KINGDOM | United Kingdom Equities | 45.689998626708984 | 46.150001525878906 | 0.010067912300198989 | 16 |
| COMMUNICATIONS | Communication Services Sector | 106.86000061035156 | 107.87999725341797 | 0.009545167857388126 | 17 |
| DIVIDEND | US Dividend Equities | 31.63802719116211 | 31.93000030517578 | 0.009228549942432274 | 18 |
| TIPS | Treasury Inflation-Protected Securities | 108.94000244140625 | 109.9000015258789 | 0.008812181594993085 | 19 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.77999877929688 | 109.69999694824219 | 0.008457420291131834 | 20 |
| BRAZIL | Brazil Equities | 34.27000045776367 | 34.54999923706055 | 0.008170375709272593 | 21 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.25 | 94.97000122070312 | 0.0076392702461869355 | 22 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.62999725341797 | 99.37000274658203 | 0.00750284410190849 | 23 |
| MID_CAP | US Mid-Cap Stocks | 76.06999969482422 | 76.52999877929688 | 0.006047049905587798 | 24 |
| INDUSTRIALS | Industrials Sector | 181.8000030517578 | 182.75999450683594 | 0.005280480962394751 | 25 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.27000045776367 | 48.52000045776367 | 0.005179200282352303 | 26 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.4000015258789 | 96.81999969482422 | 0.004356827409723207 | 27 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.31999969482422 | 107.70999908447266 | 0.003633986123345423 | 28 |
| SMALL_CAP | US Small-Cap Stocks | 298.17999267578125 | 298.9700012207031 | 0.0026494351208226075 | 29 |
| MEXICO | Mexico Equities | 75.95999908447266 | 76.12000274658203 | 0.002106420011030341 | 30 |
| LARGE_GROWTH | US Large-Cap Growth | 121.76000213623047 | 121.9800033569336 | 0.0018068431081084135 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.94000244140625 | 80.01000213623047 | 0.0008756528982536427 | 32 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.56999969482422 | 91.63999938964844 | 0.0007644391728460764 | 33 |
| FINANCIALS | Financials Sector | 53.70000076293945 | 53.720001220703125 | 0.00037244799775626447 | 34 |
| US_DOLLAR | US Dollar | 28.360000610351562 | 28.3700008392334 | 0.0003526173718835235 | 35 |
| EURO | Euro | 105.43000030517578 | 105.44999694824219 | 0.0001896674856163294 | 36 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 37 |
| TOTAL_US_MARKET | Total US Stock Market | 367.75213623046875 | 367.1199951171875 | -0.0017189325390759569 | 38 |
| EUROPE | Europe Equities | 88.25 | 88.06999969482422 | -0.00203966351473972 | 39 |
| YEN | Japanese Yen | 56.790000915527344 | 56.65999984741211 | -0.0022891541824168193 | 40 |
| LARGE_VALUE | US Large-Cap Value | 243.52999877929688 | 242.75 | -0.0032028858177910458 | 41 |
| SP500 | S&P 500 | 744.3900146484375 | 741.0 | -0.004554083990552349 | 42 |
| AGRICULTURE | Agriculture Commodities | 26.649999618530273 | 26.510000228881836 | -0.005253260474761601 | 43 |
| CANADA | Canada Equities | 57.88999938964844 | 57.4900016784668 | -0.00690961678008184 | 44 |
| ENERGY | Energy Sector | 54.060001373291016 | 53.58000183105469 | -0.008879014614185277 | 45 |
| AUSTRALIA | Australia Equities | 28.450000762939453 | 28.110000610351562 | -0.011950795904047684 | 46 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.0399932861328 | 128.38999938964844 | -0.012688357287544805 | 47 |
| INDIA | India Equities | 49.91999816894531 | 49.18000030517578 | -0.014823675699368821 | 48 |
| MATERIALS | Materials Sector | 51.619998931884766 | 50.65999984741211 | -0.018597425500520126 | 49 |
| NASDAQ100 | Nasdaq 100 | 737.9500122070312 | 724.0800170898438 | -0.01879530440782251 | 50 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.38999938964844 | 70.91999816894531 | -0.020306689226375796 | 51 |
| SOUTH_AFRICA | South Africa Equities | 65.13999938964844 | 63.41999816894531 | -0.026404685858447463 | 52 |
| MOMENTUM | US Momentum Equities | 345.2200012207031 | 336.0 | -0.02670761018510248 | 53 |
| BROAD_COMMODITIES | Broad Commodities | 16.360000610351562 | 15.84000015258789 | -0.031784867870643496 | 54 |
| EMERGING_MARKETS | Emerging Markets | 61.2400016784668 | 59.18000030517578 | -0.03363816650604945 | 55 |
| TECHNOLOGY | Technology Sector | 192.14999389648438 | 185.41000366210938 | -0.035076713236878776 | 56 |
| JAPAN | Japan Equities | 96.97000122070312 | 93.20999908447266 | -0.03877490037019515 | 57 |
| CHINA | China Equities | 52.86000061035156 | 50.790000915527344 | -0.039160039177503325 | 58 |
| COPPER | Copper | 38.810001373291016 | 37.22999954223633 | -0.04071120265772632 | 59 |
| GOLD | Gold | 78.80000305175781 | 75.52999877929688 | -0.04149751454087025 | 60 |
| BROAD_AI_TECH | Broad AI Technology | 67.08999633789062 | 64.22000122070312 | -0.042778286985337144 | 61 |
| OIL | Crude Oil | 112.69000244140625 | 107.08000183105469 | -0.04978259374223115 | 62 |
| TAIWAN | Taiwan Equities | 111.52999877929688 | 105.79000091552734 | -0.05146595469016568 | 63 |
| SEMICONDUCTORS | Semiconductors | 668.9099731445312 | 631.97998046875 | -0.05520921223849329 | 64 |
| SOLAR | Solar Energy | 61.11000061035156 | 57.599998474121094 | -0.057437442336335076 | 65 |
| ETHEREUM_ETF | Ethereum ETF | 13.0600004196167 | 12.239999771118164 | -0.06278718393200489 | 66 |
| BITCOIN_ETF | Bitcoin ETF | 36.5 | 34.18000030517578 | -0.06356163547463611 | 67 |
| METALS_MINING | Metals and Mining | 115.22000122070312 | 106.5199966430664 | -0.07550776328297304 | 68 |
| SOUTH_KOREA | South Korea Equities | 219.02000427246094 | 197.5 | -0.09825588463458368 | 69 |
| SILVER | Silver | 58.90999984741211 | 52.68000030517578 | -0.1057545333283515 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.05520921223849329 | -0.016562763671547985 | Strong momentum with +3.37% 7d and +16.07% 30d; AI capex cycle and Asia tech strength support continuation. |
| anthropic-claude-opus-4-7 | TAIWAN | 20.0 | -0.05146595469016568 | -0.010293190938033138 | Semi supply chain leverage; +4.85% 7d momentum amid global chip demand. |
| anthropic-claude-opus-4-7 | SOUTH_KOREA | 15.0 | -0.09825588463458368 | -0.014738382695187551 | Strongest country momentum (+3.58% 7d, +20% 30d); chip and export tailwinds. |
| anthropic-claude-opus-4-7 | MOMENTUM | 20.0 | -0.02670761018510248 | -0.0053415220370204965 | Factor with persistent leadership (+3.47% 7d, +13.83% 30d) into quiet pre-payrolls week. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.0007644391728460764 | 0.00011466587592691146 | Ballast given sticky inflation, hawkish FOMC SEP, and elevated 10y yields. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.05520921223849329 | -0.016562763671547985 | Strong momentum (+3.37% 7d, +16% 30d) led by Taiwan/Korea strength; semis remain the leading risk-on trade. |
| anthropic-claude-opus-4-8 | SP500 | 30.0 | -0.004554083990552349 | -0.0013662251971657045 | Core benchmark exposure; balances active tilts and limits tracking error against the scoring benchmark. |
| anthropic-claude-opus-4-8 | MOMENTUM | 20.0 | -0.02670761018510248 | -0.0053415220370204965 | Persistent factor strength (+3.47% 7d, +13.83% 30d) tends to carry forward over short windows. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 10.0 | 0.0007644391728460764 | 7.644391728460765e-05 | Stable cash-like ballast given sticky inflation, hawkish FOMC SEP, and elevated yields. |
| anthropic-claude-opus-4-8 | BIOTECH | 10.0 | 0.08535579937025317 | 0.008535579937025318 | Sharp positive momentum (+6.94% 7d) suggests near-term continuation in a recovering risk segment. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | -0.05520921223849329 | -0.016562763671547985 | Strong recent momentum with 3.37% 7-day and 16.07% 30-day returns suggests continued outperformance in the short term. |
| google-gemini-3-1-pro | TAIWAN | 25.0 | -0.05146595469016568 | -0.01286648867254142 | Benefiting from semiconductor supply chain strength, showing 4.85% 7-day and 15.17% 30-day returns. |
| google-gemini-3-1-pro | SOUTH_KOREA | 25.0 | -0.09825588463458368 | -0.02456397115864592 | Strong tech and export exposure driving 3.58% 7-day and 20.32% 30-day returns. |
| google-gemini-3-1-pro | BIOTECH | 20.0 | 0.08535579937025317 | 0.017071159874050636 | Leading recent performance with a 6.94% 7-day return, indicating strong short-term sector rotation into biotech. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.05520921223849329 | -0.019323224283472648 | Semiconductors show very strong multi-horizon momentum and remain the clearest liquid expression of AI and hardware leadership over a short window. |
| openai-gpt-5-5 | TAIWAN | 25.0 | -0.05146595469016568 | -0.01286648867254142 | Taiwan equities provide concentrated exposure to the semiconductor supply chain with strong recent relative strength versus the S&P 500. |
| openai-gpt-5-5 | MOMENTUM | 20.0 | -0.02670761018510248 | -0.0053415220370204965 | Momentum factor exposure captures broad trend persistence while diversifying beyond a single industry or country. |
| openai-gpt-5-5 | SOUTH_KOREA | 10.0 | -0.09825588463458368 | -0.009825588463458369 | South Korea has strong recent and longer-term performance, with semiconductor and export cyclicality that can benefit if the risk-on tech trade continues. |
| openai-gpt-5-5 | BIOTECH | 10.0 | 0.08535579937025317 | 0.008535579937025318 | Biotech has the strongest one-week trailing return in the universe and can add differentiated high-beta upside if speculative risk appetite persists. |
| xai-grok-4-3 | SP500 | 50.0 | -0.004554083990552349 | -0.0022770419952761745 | Core benchmark exposure for stability over the one-week window with limited catalysts. |
| xai-grok-4-3 | MOMENTUM | 25.0 | -0.02670761018510248 | -0.00667690254627562 | Recent 7-day outperformance suggests potential trend continuation into exit close. |
| xai-grok-4-3 | SEMICONDUCTORS | 25.0 | -0.05520921223849329 | -0.013802303059623322 | Strong recent performance and sector momentum likely to persist short-term. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.05520921223849329 | -0.01465848705142426 | -0.010104403060871911 | 0.10001428642167744 |  | False | False |
| xai-grok-4-3 | SP500 | 3 | 0.55 | -0.004554083990552349 | -0.022756247601175117 | -0.018202163610622768 | 0.10811204697142829 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 4 | 0.65 | -0.05520921223849329 | -0.03692206362868469 | -0.032367979638132344 | 0.12227786299893786 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.57 | -0.05520921223849329 | -0.03882124351946761 | -0.034267159528915264 | 0.12417704288972078 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.05520921223849329 | -0.04682119346586226 | -0.042267109475309914 | 0.13217699283611545 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 318e3134692a3ab8402c796c9d817f944f76565c75a12f550fa5305bf973d9e6 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 68a143201b250285b114b2001bcdfdd6269a744b9b3595e63fe6b846177dc887 |
| manifest.yaml | 9783595ad06cfe5ed4bb521498ac4ec9f54a1b0f947fce01ba9f73df314649c4 |
| market_data/universe_trailing_returns.csv | 2bedb275edea2668fe45a6c3eb557974e6dd98f5dd96deb20acb8f23b9a2a033 |
| market_data/universe_trailing_returns.md | 12d2ab6cfe977f390311f19cbc554861bbd823e84fe3e6c0c13713d69fcedf94 |
| market_data/universe_trailing_returns.json | e85e84d3c86a8516f7616962ea42a4983038d2a170525239da191e1a0c65ea42 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 7d8b51ca282f6ca230567d846ec207d3cb92fb9dbdaadbd7d11fed9bcfd72f13 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 61759a1657b19d22f00594f23589b9bdd8d80a2088fdcd4989ec2bb7c6fbe0b6 | yes |
| Final briefing | research/final_briefing.md | model-facing | 318e3134692a3ab8402c796c9d817f944f76565c75a12f550fa5305bf973d9e6 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
