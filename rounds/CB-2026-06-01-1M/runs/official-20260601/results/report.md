# CapitalBench Report: CB-2026-06-01-1M / official-20260601

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260601
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 1 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round scored from the latest available close before the June 1 decision deadline, using the May 29, 2026 adjusted close to the June 29, 2026 adjusted close.
- Decision date: 2026-06-01
- Decision deadline: 2026-06-02T00:00:00Z
- Horizon: one month
- Entry date: 2026-05-29
- Exit date: 2026-06-29
- Entry rule: Use adjusted close on Friday, May 29, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Monday, June 29, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Overweight semiconductors and tech where momentum and fundamentals align, with Taiwan supply-chain leverage, defense budget support, and SP500 ballast. | Sticky inflation (CPI 3.8% YoY, PCE 3.8%) and hawkish June FOMC could pressure high-multiple growth/tech names; Semiconductor/tech concentration leaves portfolio vulnerable to a sharp factor rotation out of momentum; Taiwan exposure carries geopolitical and currency risk that could spike independent of fundamentals; Weak May payrolls or GDP downgrade could trigger risk-off, hurting high-beta thematic holdings |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Overweight AI/semis and defense for momentum continuation; gold and bills hedge stagflationary macro and weak consumer signals before June 17 FOMC. | Hot May CPI (June 10) triggers hawkish repricing hurting growth/semis; Gold reverses on stronger dollar or risk-on rotation; Defense budget reconciliation delays cap ITA upside; Momentum factor crash on sudden rotation to value/defensives |
| xai-grok-4-3 | xai | portfolio | NASDAQ100 | 5 | 0.55 | Portfolio emphasizes growth and tech sectors showing strongest recent returns and structural spending support, while avoiding rate-sensitive or cyclical areas amid mixed macro data. | Hotter-than-expected May CPI or PPI releases on June 10-11 could pressure growth valuations; June 5 employment report weaker than 115k trend may increase recession fears; FOMC June 16-17 decision or dot plot shifts could trigger volatility in rate-sensitive tech |
| openai-gpt-5-5 | openai | portfolio | BROAD_AI_TECH | 5 | 0.58 | This allocation seeks alpha through concentrated exposure to AI-led technology momentum and semiconductor-linked markets. It accepts elevated valuation and reversal risk because the scoring horizon is short and recent leadership has been exceptionally strong. | A hotter-than-expected June CPI or PPI release could lift yields and trigger a sharp growth-stock de-rating before the exit date.; Crowded AI and semiconductor positioning could reverse after very strong trailing returns, especially in South Korea and cybersecurity.; Any disappointment in near-term technology earnings guidance, AI capex commentary, or chip-demand indicators could hit multiple holdings simultaneously.; A risk-off shock or geopolitical escalation in East Asia could disproportionately hurt semiconductor supply-chain and South Korea exposure. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 4 | 0.65 | Allocates heavily to semiconductors, AI technology, South Korea, and solar to capitalize on extreme short-term price momentum and strong underlying thematic fundamentals. | A sudden reversal in the AI and semiconductor momentum trade due to stretched valuations or profit-taking.; Geopolitical tensions in Asia disrupting semiconductor supply chains and negatively impacting South Korean equities.; A broader market correction triggered by high S&P 500 valuations (forward P/E of 25.9) dragging down high-beta sectors. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 136.5559539794922 | 158.30999755859375 | 0.15930498045049402 | 1 |
| HEALTHCARE | Healthcare Sector | 148.81369018554688 | 160.74000549316406 | 0.08014259503105503 | 2 |
| REGIONAL_BANKS | Regional Banks | 69.20526885986328 | 74.75 | 0.08012007223560502 | 3 |
| MOMENTUM | US Momentum Equities | 315.46148681640625 | 336.0 | 0.06510624606149418 | 4 |
| INDUSTRIALS | Industrials Sector | 172.70509338378906 | 182.75999450683594 | 0.058220061296644365 | 5 |
| SEMICONDUCTORS | Semiconductors | 598.9299926757812 | 631.97998046875 | 0.055181721064451184 | 6 |
| LOW_VOL | US Low Volatility Equities | 72.07366180419922 | 75.58999633789062 | 0.04878806551059034 | 7 |
| FINANCIALS | Financials Sector | 51.39994812011719 | 53.720001220703125 | 0.0451372654144353 | 8 |
| UTILITIES | Utilities Sector | 44.138153076171875 | 46.02000045776367 | 0.042635390256229755 | 9 |
| SMALL_VALUE | US Small-Cap Value | 213.1010284423828 | 221.27999877929688 | 0.03838071733720172 | 10 |
| SMALL_CAP | US Small-Cap Stocks | 289.740966796875 | 298.9700012207031 | 0.031852708044210365 | 11 |
| REAL_ESTATE | Real Estate Sector | 43.607872009277344 | 44.91999816894531 | 0.0300892040636338 | 12 |
| TAIWAN | Taiwan Equities | 102.77999877929688 | 105.79000091552734 | 0.0292858744111677 | 13 |
| MID_CAP | US Mid-Cap Stocks | 74.41458129882812 | 76.52999877929688 | 0.028427459290186974 | 14 |
| US_DOLLAR | US Dollar | 27.65999984741211 | 28.3700008392334 | 0.02566887186327005 | 15 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.33869171142578 | 84.37000274658203 | 0.024670188376024083 | 16 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.0243682861328 | 213.0500030517578 | 0.024158875265576363 | 17 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.42400360107422 | 87.44999694824219 | 0.023716909320116386 | 18 |
| LARGE_VALUE | US Large-Cap Value | 237.2121124267578 | 242.75 | 0.023345720067107 | 19 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.27484130859375 | 239.1300048828125 | 0.0163857875868767 | 20 |
| INDIA | India Equities | 48.560001373291016 | 49.18000030517578 | 0.012767687692566199 | 21 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.02300262451172 | 96.81999969482422 | 0.00830006403183492 | 22 |
| JAPAN | Japan Equities | 92.45764923095703 | 93.20999908447266 | 0.008137237532789499 | 23 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.33300018310547 | 95.05999755859375 | 0.007706713176482749 | 24 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.88999938964844 | 107.70999908447266 | 0.007671435115599978 | 25 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.94700622558594 | 109.69999694824219 | 0.006911532025920097 | 26 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.72899627685547 | 99.37000274658203 | 0.006492585703282705 | 27 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.215999603271484 | 48.52000045776367 | 0.006304978782842863 | 28 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.45700073242188 | 94.97000122070312 | 0.005431047823913904 | 29 |
| EUROPE | Europe Equities | 87.81395721435547 | 88.06999969482422 | 0.0029157378689101954 | 30 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.39100646972656 | 91.63999938964844 | 0.0027244794596321675 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.9010009765625 | 80.01000213623047 | 0.00136420268001336 | 32 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 109.93199920654297 | 109.9000015258789 | -0.0002910679410454975 | 34 |
| UNITED_KINGDOM | United Kingdom Equities | 46.267250061035156 | 46.150001525878906 | -0.0025341582869432555 | 35 |
| CYBERSECURITY | Cybersecurity | 88.9635009765625 | 88.5 | -0.005210012774616524 | 36 |
| MATERIALS | Materials Sector | 50.95945739746094 | 50.65999984741211 | -0.005876388119936071 | 37 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.39420318603516 | 70.91999816894531 | -0.006642066105201683 | 38 |
| DIVIDEND | US Dividend Equities | 32.24320602416992 | 31.93000030517578 | -0.009713851617589087 | 39 |
| EMERGING_MARKETS | Emerging Markets | 59.80891799926758 | 59.18000030517578 | -0.010515450122329573 | 40 |
| TOTAL_US_MARKET | Total US Stock Market | 371.4714660644531 | 367.1199951171875 | -0.011714145889500482 | 41 |
| MEXICO | Mexico Equities | 77.2925796508789 | 76.12000274658203 | -0.015170627110561719 | 42 |
| YEN | Japanese Yen | 57.619998931884766 | 56.65999984741211 | -0.016660866058111456 | 43 |
| CANADA | Canada Equities | 58.534767150878906 | 57.4900016784668 | -0.017848631219786526 | 44 |
| SP500 | S&P 500 | 754.5361328125 | 741.0 | -0.01793967475360614 | 45 |
| NASDAQ100 | Nasdaq 100 | 737.49951171875 | 724.0800170898438 | -0.018195936967648985 | 46 |
| EURO | Euro | 107.63499450683594 | 105.44999694824219 | -0.02030006661499839 | 47 |
| AUSTRALIA | Australia Equities | 28.844585418701172 | 28.110000610351562 | -0.02546699138457187 | 48 |
| AGRICULTURE | Agriculture Commodities | 27.25 | 26.510000228881836 | -0.027155954903418822 | 49 |
| TECHNOLOGY | Technology Sector | 190.79251098632812 | 185.41000366210938 | -0.028211313412634165 | 50 |
| BRAZIL | Brazil Equities | 35.57136154174805 | 34.54999923706055 | -0.028713050623288217 | 51 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 120.62963104248047 | 117.12000274658203 | -0.02909424712293529 | 52 |
| SOUTH_KOREA | South Korea Equities | 205.8300018310547 | 197.5 | -0.04047029955279291 | 53 |
| ENERGY | Energy Sector | 55.886959075927734 | 53.58000183105469 | -0.04127899035871363 | 54 |
| COPPER | Copper | 38.86000061035156 | 37.22999954223633 | -0.041945472015279206 | 55 |
| LARGE_GROWTH | US Large-Cap Growth | 127.73750305175781 | 121.9800033569336 | -0.045072899949291645 | 56 |
| BROAD_AI_TECH | Broad AI Technology | 67.31999969482422 | 64.22000122070312 | -0.04604870006200301 | 57 |
| COMMUNICATIONS | Communication Services Sector | 115.38981628417969 | 107.87999725341797 | -0.0650821647229829 | 58 |
| SOUTH_AFRICA | South Africa Equities | 67.9215316772461 | 63.41999816894531 | -0.06627550052450903 | 59 |
| CHINA | China Equities | 54.737220764160156 | 50.790000915527344 | -0.07211217145349291 | 60 |
| BROAD_COMMODITIES | Broad Commodities | 17.6200008392334 | 15.84000015258789 | -0.1010216005598642 | 61 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 142.8699951171875 | 128.38999938964844 | -0.10135085198023563 | 62 |
| SOFTWARE | Software | 101.64094543457031 | 89.88999938964844 | -0.1156123252758049 | 63 |
| GOLD | Gold | 85.48999786376953 | 75.52999877929688 | -0.11650484657098914 | 64 |
| METALS_MINING | Metals and Mining | 125.12439727783203 | 106.5199966430664 | -0.14868723478008483 | 65 |
| OIL | Crude Oil | 129.08999633789062 | 107.08000183105469 | -0.17050116299659035 | 66 |
| BITCOIN_ETF | Bitcoin ETF | 41.630001068115234 | 34.18000030517578 | -0.17895749631977476 | 67 |
| ETHEREUM_ETF | Ethereum ETF | 15.199999809265137 | 12.239999771118164 | -0.19473684705855776 | 68 |
| SOLAR | Solar Energy | 73.93000030517578 | 57.599998474121094 | -0.22088464444266254 | 69 |
| SILVER | Silver | 68.33000183105469 | 52.68000030517578 | -0.2290355789038817 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | 0.055181721064451184 | 0.016554516319335355 | Strong momentum, AI capex acceleration, Q1 global chip sales +25% QoQ. |
| anthropic-claude-opus-4-7 | GOLD | 25.0 | -0.11650484657098914 | -0.029126211642747285 | Hedge against re-accelerating inflation (CPI 3.8%, PPI 6%), weak sentiment, geopolitical risk. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | 0.0163857875868767 | 0.002457868138031505 | $1.5T FY27 defense budget tailwind, strong momentum. |
| anthropic-claude-opus-4-7 | MOMENTUM | 15.0 | 0.06510624606149418 | 0.009765936909224126 | Persistent momentum factor leadership in low-vol regime (VIX 15.7). |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.0027244794596321675 | 0.0004086719189448251 | Dry powder given stagflation risk: GDP revised down to 1.6%, CPI re-accelerating, consumer sentiment collapsing to 44.8. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | 0.055181721064451184 | 0.016554516319335355 | Strong momentum and earnings; SIA reported Q1 2026 global semi sales up 25% QoQ; AI capex surging 75% in 2026. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 25.0 | -0.028211313412634165 | -0.007052828353158541 | Tech sector leading with 20% 30d return; AI infrastructure and software spending tailwinds remain robust. |
| anthropic-claude-opus-4-8 | TAIWAN | 15.0 | 0.0292858744111677 | 0.0043928811616751546 | Semiconductor supply-chain leverage with strong trend; benefits from global electronics and AI chip demand. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 15.0 | 0.0163857875868767 | 0.002457868138031505 | FY2027 $1.5T defense budget request supports orders; steady momentum with lower beta than pure tech. |
| anthropic-claude-opus-4-8 | SP500 | 15.0 | -0.01793967475360614 | -0.002690951213040921 | Benchmark anchor to limit tracking error given sticky inflation and June FOMC/jobs catalysts. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | 0.055181721064451184 | 0.016554516319335355 | Global semiconductor sales surged 25% quarter-over-quarter, and the sector exhibits extreme price momentum that is likely to persist over a one-month horizon. |
| google-gemini-3-1-pro | SOUTH_KOREA | 30.0 | -0.04047029955279291 | -0.012141089865837873 | South Korean equities are showing massive trailing returns, heavily driven by their exposure to the global semiconductor and electronics supply chain. |
| google-gemini-3-1-pro | BROAD_AI_TECH | 20.0 | -0.04604870006200301 | -0.009209740012400602 | AI infrastructure spending forecasts remain robust, supporting continued momentum in broad AI technology equities. |
| google-gemini-3-1-pro | SOLAR | 20.0 | -0.22088464444266254 | -0.04417692888853251 | Solar equities have demonstrated exceptional recent momentum, supported by upward revisions in utility-scale generation forecasts. |
| openai-gpt-5-5 | BROAD_AI_TECH | 30.0 | -0.04604870006200301 | -0.013814610018600904 | Broad AI exposure has strong recent momentum and a near-term narrative supported by large forecast AI spending and infrastructure capex growth. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | 0.055181721064451184 | 0.013795430266112796 | Semiconductors remain a core AI infrastructure beneficiary, with strong trailing performance and Q1 global semiconductor sales up sharply versus the prior quarter. |
| openai-gpt-5-5 | CYBERSECURITY | 20.0 | -0.005210012774616524 | -0.0010420025549233048 | Cybersecurity has the strongest one-month trailing return among major technology themes and is supported by rising AI-related security spending forecasts. |
| openai-gpt-5-5 | SOUTH_KOREA | 15.0 | -0.04047029955279291 | -0.006070544932918936 | South Korea offers high-beta semiconductor and export exposure with very strong recent price momentum into the scoring window. |
| openai-gpt-5-5 | TECHNOLOGY | 10.0 | -0.028211313412634165 | -0.0028211313412634166 | Large-cap technology provides liquid, benchmark-relevant exposure to the same AI-led leadership while reducing single-theme concentration somewhat. |
| xai-grok-4-3 | NASDAQ100 | 30.0 | -0.018195936967648985 | -0.0054587810902946956 | Recent 30d outperformance and exposure to growth names likely to benefit from stable rates and AI spending trends into June. |
| xai-grok-4-3 | TECHNOLOGY | 25.0 | -0.028211313412634165 | -0.007052828353158541 | Strong trailing momentum in XLK amid semiconductor and software demand data points. |
| xai-grok-4-3 | SEMICONDUCTORS | 20.0 | 0.055181721064451184 | 0.011036344212890237 | Q1 sales growth and continued AI infrastructure capex support near-term price action. |
| xai-grok-4-3 | BROAD_AI_TECH | 15.0 | -0.04604870006200301 | -0.006907305009300452 | Gartner AI spending forecast and recent 30d gains position for continued rotation into tech. |
| xai-grok-4-3 | MOMENTUM | 10.0 | 0.06510624606149418 | 0.006510624606149418 | Factor exposure captures recent winners in high-momentum tech and growth equities. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | 0.055181721064451184 | 0.013661486052842552 | 0.03160116080644869 | 0.14564349439765145 |  | True | True |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | 0.055181721064451184 | 6.07816427885259e-05 | 0.018000456396394665 | 0.1592441988077055 |  | True | True |
| xai-grok-4-3 | NASDAQ100 | 5 | 0.55 | -0.018195936967648985 | -0.0018719456337140325 | 0.016067729119892106 | 0.16117692608420806 |  | True | False |
| openai-gpt-5-5 | BROAD_AI_TECH | 5 | 0.58 | -0.04604870006200301 | -0.009952858581593765 | 0.007986816172012374 | 0.16925783903208777 |  | True | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 4 | 0.65 | 0.055181721064451184 | -0.04897324244743563 | -0.031033567693829492 | 0.20827822289792963 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 8aa259bae9eabf3c2ec2253ec6a5255c99967dd15b8893b591382074aa64da2f |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 33bae462b97c4a3eadb0c01b875c98191002e966929695d7f80d2b20ba2bf7c4 |
| manifest.yaml | ce8d0664211caa69a128da86f3ee83811c65f0de8f79151374aa31ffc675e393 |
| market_data/universe_trailing_returns.csv | fdb3442013c59fdb7ec29bb96281f2be982b988d7f756cb5e7b267679066b967 |
| market_data/universe_trailing_returns.md | f02895ae6e085bbbdad0d5a4f52f9df31b7492efd484e127026be1a4ddca9f59 |
| market_data/universe_trailing_returns.json | d8aa9b6c5a7153852eff4bb5abd9c34ef174269cf93f8a9466ef9e610a82eb86 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a5f0682504fa0e5e7e3f188aad475c64bfe4ead309af47a636c813620c5ed937 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 24256f252bedd3fa45234e070a1106483a277e92f1cbbab34974453f71e599a6 | yes |
| Final briefing | research/final_briefing.md | model-facing | 8aa259bae9eabf3c2ec2253ec6a5255c99967dd15b8893b591382074aa64da2f | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
