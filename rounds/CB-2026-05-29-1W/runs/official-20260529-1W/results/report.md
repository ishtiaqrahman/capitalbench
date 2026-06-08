# CapitalBench Report: CB-2026-05-29-1W / official-20260529-1W

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260529-1W
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench May 29 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round scored Friday-to-Friday from the May 29, 2026 adjusted close to the June 5, 2026 adjusted close.
- Decision date: 2026-05-29
- Decision deadline: 2026-05-30T00:00:00Z
- Horizon: one week
- Entry date: 2026-05-29
- Exit date: 2026-06-05
- Entry rule: Use adjusted close on Friday, May 29, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Friday, June 5, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Overweight semis, tech, software and momentum given AI capex strength and benign macro; SP500 anchor limits downside vs benchmark. | June 5 May payrolls surprise could trigger sharp rate-driven rotation out of high-beta growth/tech.; Concentrated AI/tech exposure means a single-week factor reversal or megacap drawdown hits the whole book.; Sticky CPI (3.8% YoY) and hot PPI could revive rate fears and compress high-multiple growth names. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | MOMENTUM | 5 | 0.55 | Concentrated in momentum and AI/semis leadership riding strong trend, complemented by gold as inflation/risk hedge. | Hot May NFP (June 5) could spike yields and hit growth/tech multiples; Momentum reversal/factor rotation into value or defensives; Geopolitical Taiwan headline risk; Gold pullback on stronger dollar or risk-on continuation |
| xai-grok-4-3 | xai | portfolio | MOMENTUM | 5 | 0.55 | Recent factor and sector returns plus semiconductor sales growth favor momentum and tech exposure over the one-week window ending June 5. | May employment report on June 5 could trigger broad equity rotation if weaker than expected; ISM services and manufacturing releases on June 1-3 may disappoint given low consumer sentiment; Elevated inflation prints could pressure growth valuations if services data surprises hot |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 4 | 0.65 | Overweighting high-momentum technology and semiconductor sectors to maximize short-term relative returns against the S&P 500. | A hotter-than-expected May Employment Situation report on June 5 could spike yields and disproportionately hurt high-valuation tech stocks.; Weak ISM Manufacturing or Services data could trigger a sudden growth scare, leading to a sharp rotation out of high-beta tech into defensive sectors.; Extreme concentration in technology exposes the portfolio to severe underperformance if the current momentum trend abruptly reverses. |
| openai-gpt-5-5 | openai | portfolio | SOFTWARE | 5 | 0.58 | I favor high-beta technology and AI momentum over the S&P 500 for the close-to-close week. The allocation seeks to exploit recent leadership while spreading exposure across software, chips, broad tech, and Korea semiconductor beta. | A hot June 5 employment report or stronger ISM data could push yields higher and trigger a growth-stock selloff before the exit close.; Recent high-beta technology and Korea gains could reverse sharply due to profit-taking after strong trailing returns.; Any negative AI, semiconductor, or mega-cap technology news could disproportionately hurt the concentrated thematic exposure.; A risk-off move from weak macro data could cause the portfolio to underperform the broader S&P 500 due to higher beta. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 129.09 | 133.02000427246094 | 0.03044390946208786 | 1 |
| ENERGY | Energy Sector | 56.29 | 57.66999816894531 | 0.02451586727563182 | 2 |
| HEALTHCARE | Healthcare Sector | 149.47 | 153.00999450683594 | 0.023683645593336022 | 3 |
| LOW_VOL | US Low Volatility Equities | 72.21 | 73.47000122070312 | 0.0174491236768195 | 4 |
| REAL_ESTATE | Real Estate Sector | 43.99 | 44.70000076293945 | 0.016140049168889448 | 5 |
| FINANCIALS | Financials Sector | 51.58 | 52.29999923706055 | 0.013958884006602279 | 6 |
| US_DOLLAR | US Dollar | 27.66 | 28.020000457763672 | 0.013015200931441484 | 7 |
| REGIONAL_BANKS | Regional Banks | 69.61 | 70.16999816894531 | 0.008044794841909342 | 8 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.91 | 83.44000244140625 | 0.006392503213198175 | 9 |
| INDUSTRIALS | Industrials Sector | 173.13 | 174.17999267578125 | 0.006064764487848651 | 10 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 11 |
| UTILITIES | Utilities Sector | 44.42 | 44.349998474121094 | -0.0015759010778682025 | 12 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.17 | 106.97000122070312 | -0.0018661825072023852 | 13 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.66 | 91.44999694824219 | -0.002291109008922154 | 14 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.83 | 207.8300018310547 | -0.004788575247547389 | 15 |
| YEN | Japanese Yen | 57.62 | 57.310001373291016 | -0.005380052528791812 | 16 |
| DIVIDEND | US Dividend Equities | 32.5 | 32.29999923706055 | -0.006153869628906294 | 17 |
| LARGE_VALUE | US Large-Cap Value | 237.96 | 236.4199981689453 | -0.006471683606718348 | 18 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.33 | 48.0099983215332 | -0.0066211810152451145 | 19 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.76 | 85.05999755859375 | -0.008162341900725956 | 20 |
| MID_CAP | US Mid-Cap Stocks | 74.6 | 73.94999694824219 | -0.008713177637504121 | 21 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 99.06 | 98.16999816894531 | -0.008984472350642925 | 22 |
| BROAD_COMMODITIES | Broad Commodities | 17.62 | 17.459999084472656 | -0.009080642197919708 | 23 |
| MATERIALS | Materials Sector | 51.15 | 50.630001068115234 | -0.010166157026095135 | 24 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.43 | 95.4000015258789 | -0.01068130741596085 | 25 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.36 | 108.16999816894531 | -0.01088150906231422 | 26 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.65 | 93.62000274658203 | -0.010882168551695437 | 27 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 80.31 | 79.43000030517578 | -0.010957535734332224 | 28 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.79 | 93.73999786376953 | -0.011077140375888583 | 29 |
| UNITED_KINGDOM | United Kingdom Equities | 46.93 | 46.380001068115234 | -0.011719559596947926 | 30 |
| CHINA | China Equities | 55.1 | 54.439998626708984 | -0.011978246339219956 | 31 |
| EURO | Euro | 107.7 | 106.29000091552734 | -0.013091913504852948 | 32 |
| CANADA | Canada Equities | 58.81 | 58.029998779296875 | -0.013263071258342585 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 111.21 | 109.25 | -0.017624314360219384 | 34 |
| COPPER | Copper | 38.86 | 38.08000183105469 | -0.020072006406209764 | 35 |
| SMALL_VALUE | US Small-Cap Value | 213.87 | 209.44000244140625 | -0.020713506142019722 | 36 |
| EUROPE | Europe Equities | 89.01 | 87.12999725341797 | -0.02112125319157443 | 37 |
| JAPAN | Japan Equities | 92.96 | 90.72000122070312 | -0.024096372410680633 | 38 |
| TOTAL_US_MARKET | Total US Stock Market | 372.54 | 363.3800048828125 | -0.024587950601781094 | 39 |
| SP500 | S&P 500 | 756.48 | 737.5499877929688 | -0.025023810552864956 | 40 |
| INDIA | India Equities | 48.56 | 47.34000015258789 | -0.02512355534209454 | 41 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.44 | 229.4499969482422 | -0.02544173909173386 | 42 |
| CYBERSECURITY | Cybersecurity | 89.04 | 86.69999694824219 | -0.026280357724144388 | 43 |
| MOMENTUM | US Momentum Equities | 315.81 | 306.4700012207031 | -0.02957474044297803 | 44 |
| SMALL_CAP | US Small-Cap Stocks | 290.43 | 281.6499938964844 | -0.030231057754073754 | 45 |
| EMERGING_MARKETS | Emerging Markets | 59.88 | 58.029998779296875 | -0.030895143966318095 | 46 |
| AGRICULTURE | Agriculture Commodities | 27.25 | 26.399999618530273 | -0.03119267454934771 | 47 |
| COMMUNICATIONS | Communication Services Sector | 115.69 | 111.66999816894531 | -0.03474804936515419 | 48 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.77 | 69.16999816894531 | -0.03622686123804775 | 49 |
| LARGE_GROWTH | US Large-Cap Growth | 127.85 | 122.69000244140625 | -0.04035977754081932 | 50 |
| AUSTRALIA | Australia Equities | 29.25 | 28.059999465942383 | -0.040683778942140814 | 51 |
| MEXICO | Mexico Equities | 78.43 | 75.0999984741211 | -0.042458262474549424 | 52 |
| NASDAQ100 | Nasdaq 100 | 738.31 | 705.0599975585938 | -0.045035286588839596 | 53 |
| TAIWAN | Taiwan Equities | 102.78 | 98.08000183105469 | -0.04572872318491261 | 54 |
| SEMICONDUCTORS | Semiconductors | 598.93 | 569.6900024414062 | -0.04882039229725299 | 55 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 120.87 | 114.86000061035156 | -0.04972283767393437 | 56 |
| GOLD | Gold | 85.49 | 81.22000122070312 | -0.04994734798569267 | 57 |
| METALS_MINING | Metals and Mining | 125.21 | 118.5999984741211 | -0.05279132278475285 | 58 |
| BRAZIL | Brazil Equities | 35.91 | 34.0099983215332 | -0.05291009965098281 | 59 |
| TECHNOLOGY | Technology Sector | 191.02 | 180.3000030517578 | -0.056119762057597056 | 60 |
| SOFTWARE | Software | 101.66 | 95.8499984741211 | -0.05715130361871834 | 61 |
| BIOTECH | Biotechnology | 136.69 | 128.6699981689453 | -0.05867292289892956 | 62 |
| BROAD_AI_TECH | Broad AI Technology | 67.32 | 62.52000045776367 | -0.07130124097201906 | 63 |
| SOUTH_AFRICA | South Africa Equities | 69.41 | 64.37000274658203 | -0.07261197598930935 | 64 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 142.87 | 129.60000610351562 | -0.0928815979315768 | 65 |
| SILVER | Silver | 68.33 | 61.56999969482422 | -0.09893165966889772 | 66 |
| SOLAR | Solar Energy | 73.93 | 64.05000305175781 | -0.13363988838417684 | 67 |
| SOUTH_KOREA | South Korea Equities | 205.83 | 175.19000244140625 | -0.14886069843362848 | 68 |
| BITCOIN_ETF | Bitcoin ETF | 41.63 | 34.13999938964844 | -0.17991834279009278 | 69 |
| ETHEREUM_ETF | Ethereum ETF | 15.2 | 11.869999885559082 | -0.2190789548974288 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | MOMENTUM | 25.0 | -0.02957474044297803 | -0.007393685110744508 | Strong trend persistence with +4% week and +13.7% month, riding tech leadership into a benign macro week. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 25.0 | -0.04882039229725299 | -0.012205098074313248 | Powerful momentum (+70% 6m, Q1 chip sales +25% QoQ) with continued AI capex tailwinds. |
| anthropic-claude-opus-4-7 | BROAD_AI_TECH | 20.0 | -0.07130124097201906 | -0.014260248194403814 | Broad AI exposure with strong momentum (+7.2% week) diversifies single-industry risk within the tech theme. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | -0.04994734798569267 | -0.0074921021978539 | Hedge against sticky inflation (CPI 3.8%, PPI 6%) and weak consumer sentiment; softer dollar supportive. |
| anthropic-claude-opus-4-7 | TAIWAN | 15.0 | -0.04572872318491261 | -0.0068593084777368914 | Semis supply-chain leverage with strong momentum into a tech-friendly week. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.04882039229725299 | -0.014646117689175897 | Strong momentum, 25% QoQ global chip sales growth, AI capex tailwind likely to persist into exit close. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 25.0 | -0.056119762057597056 | -0.014029940514399264 | Tech sector leading with strong breadth; low VIX and soft inflation support growth. |
| anthropic-claude-opus-4-8 | MOMENTUM | 20.0 | -0.02957474044297803 | -0.005914948088595606 | Momentum factor leading with persistent trend, benign macro backdrop favors continuation. |
| anthropic-claude-opus-4-8 | SOFTWARE | 15.0 | -0.05715130361871834 | -0.00857269554280775 | Software prices rising sharply; strong recent momentum with room to run after lagging. |
| anthropic-claude-opus-4-8 | SP500 | 10.0 | -0.025023810552864956 | -0.0025023810552864956 | Benchmark anchor to limit tracking error given jobs report risk on June 5. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | -0.04882039229725299 | -0.014646117689175897 | Strong momentum and fundamental support from a 25% quarter-over-quarter increase in global chip sales. |
| google-gemini-3-1-pro | BROAD_AI_TECH | 30.0 | -0.07130124097201906 | -0.02139037229160572 | Captures the ongoing AI theme which has shown persistent strength and high beta relative to the broader market. |
| google-gemini-3-1-pro | TECHNOLOGY | 20.0 | -0.056119762057597056 | -0.011223952411519411 | Provides broad exposure to the tech sector, which continues to lead market returns. |
| google-gemini-3-1-pro | NASDAQ100 | 20.0 | -0.045035286588839596 | -0.00900705731776792 | Offers diversified mega-cap growth exposure to anchor the high-beta thematic allocations. |
| openai-gpt-5-5 | SOFTWARE | 30.0 | -0.05715130361871834 | -0.0171453910856155 | Strongest short-term relative momentum among liquid technology themes, with recent 7-day and 30-day gains suggesting continued risk-on rotation into software. |
| openai-gpt-5-5 | BROAD_AI_TECH | 25.0 | -0.07130124097201906 | -0.017825310243004766 | Broad AI technology exposure captures the dominant growth and momentum theme while diversifying beyond a single subsector. |
| openai-gpt-5-5 | SEMICONDUCTORS | 20.0 | -0.04882039229725299 | -0.009764078459450598 | Semiconductor sales data were strong and the group retains high AI-linked earnings sensitivity, supported by robust trailing momentum. |
| openai-gpt-5-5 | TECHNOLOGY | 15.0 | -0.056119762057597056 | -0.008417964308639558 | Large-cap technology provides liquid beta to the same leadership trend with somewhat broader diversification than thematic funds. |
| openai-gpt-5-5 | SOUTH_KOREA | 10.0 | -0.14886069843362848 | -0.014886069843362848 | South Korea showed exceptional recent momentum and offers leveraged exposure to global semiconductor and export sentiment. |
| xai-grok-4-3 | MOMENTUM | 25.0 | -0.02957474044297803 | -0.007393685110744508 | Strong 7d trailing return of 4.02% and factor persistence likely to continue into jobs and ISM releases. |
| xai-grok-4-3 | TECHNOLOGY | 25.0 | -0.056119762057597056 | -0.014029940514399264 | 5.89% 7d return plus semiconductor sales growth of 25% QoQ supports near-term momentum ahead of June data. |
| xai-grok-4-3 | SEMICONDUCTORS | 20.0 | -0.04882039229725299 | -0.009764078459450598 | Q1 global chip sales surge and 3.92% 7d return position sector for continued outperformance on positive macro prints. |
| xai-grok-4-3 | BROAD_AI_TECH | 20.0 | -0.07130124097201906 | -0.014260248194403814 | 7.18% 7d return and software price acceleration indicate AI exposure benefits from short-term risk appetite. |
| xai-grok-4-3 | NASDAQ100 | 10.0 | -0.045035286588839596 | -0.00450352865888396 | 2.89% 7d return provides concentrated growth tilt aligned with tech leadership into the scoring window. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.04882039229725299 | -0.04566608289026501 | -0.020642272337400056 | 0.07610999235235287 |  | False | False |
| anthropic-claude-opus-4-7 | MOMENTUM | 5 | 0.55 | -0.02957474044297803 | -0.048210442055052365 | -0.02318663150218741 | 0.07865435151714023 |  | False | False |
| xai-grok-4-3 | MOMENTUM | 5 | 0.55 | -0.02957474044297803 | -0.049951480937882146 | -0.02492767038501719 | 0.08039539039997001 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 4 | 0.65 | -0.04882039229725299 | -0.05626749971006895 | -0.03124368915720399 | 0.0867114091721568 |  | False | False |
| openai-gpt-5-5 | SOFTWARE | 5 | 0.58 | -0.05715130361871834 | -0.06803881394007327 | -0.04301500338720832 | 0.09848272340216113 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 8806638efca7d1984912e0d7d1a247c91589e2faf82ea06a4d4314b5e81625aa |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7179513a4ffe58e840de4f87caeb6dcea0fa2f1c2ac8d04067c1abffb76013ab |
| manifest.yaml | baacebc60aa9b313bcce6ef003f0adf1685979625f9b9e022a61b334ce800613 |
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
| Market fact report | research/market_fact_report.md | audit-only | 0eb368280381cddffb13e97f6e0772629ed8c1db9c79283b0be1143d239d1bed | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | b1aaa87bb47e885d1e1f5b739682b98b1d4fca98b44e32a335ba376bb6594564 | yes |
| Final briefing | research/final_briefing.md | model-facing | 8806638efca7d1984912e0d7d1a247c91589e2faf82ea06a4d4314b5e81625aa | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
