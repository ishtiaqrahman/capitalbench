# CapitalBench Report: CB-2026-06-01-1W / official-20260601

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260601
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 1 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round scored from the latest available close before the June 1 decision deadline, using the May 29, 2026 adjusted close to the June 5, 2026 adjusted close.
- Decision date: 2026-06-01
- Decision deadline: 2026-06-02T00:00:00Z
- Horizon: one week
- Entry date: 2026-05-29
- Exit date: 2026-06-05
- Entry rule: Use adjusted close on Friday, May 29, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Friday, June 5, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrate in high-momentum semiconductor and technology exposure backed by surging chip sales and AI spending forecasts, complemented by defense for diversification. | Tech/semiconductor momentum could sharply reverse on a profit-taking rotation, hitting the heavily tech-weighted book; Friday May employment report (June 5) could trigger a risk-off move disproportionately impacting high-beta tech and semis; Taiwan exposure carries geopolitical and currency tail risk that could spike independent of fundamentals; Stretched S&P 500 forward P/E (25.9) and negative AAII sentiment raise odds of a broad equity pullback |
| xai-grok-4-3 | xai | portfolio | TECHNOLOGY | 3 | 0.65 | Recent 7-day leadership in tech, momentum, and semiconductors is expected to persist over the narrow scoring window given calm volatility and no major negative catalysts before exit. | June 5 employment report surprise could trigger broad equity reversal on exit close; Higher-than-expected CPI and PPI prints may revive rate-hike concerns; Profit-taking after sharp recent gains in tech and momentum names |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Momentum-led tech/AI overweight with gold inflation hedge and defense diversifier targeting one-week alpha vs SPY through the June 5 payrolls catalyst. | Hot May NFP on June 5 spikes yields and hits long-duration growth/tech; AI/semis momentum reversal or profit-taking after sharp recent run; Gold sells off if dollar bounces or real yields rise on hawkish data; Oil spike from EIA/geopolitics lifts energy and pressures growth multiples |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 4 | 0.75 | Overweighting high-momentum tech and AI sectors to maximize short-term returns. | A stronger-than-expected employment report on June 5 could lead to higher yields, disproportionately impacting high-valuation tech stocks.; Profit-taking or a sudden reversal in momentum factors could lead to significant underperformance.; Weakness in the ISM Services PMI on June 3 could trigger broader market risk-off sentiment. |
| openai-gpt-5-5 | openai | portfolio | BROAD_AI_TECH | 5 | 0.37 | This is an aggressive one-week alpha portfolio tilted toward AI/technology momentum plus selective high-beta satellite exposure. It aims to beat the S&P 500 through continued leadership in software, chips, Korean tech, and solar rather than broad diversification. | A hotter-than-expected jobs report or ISM services prices reading could push yields higher and trigger a reversal in expensive growth and AI equities.; Recent extreme momentum in South Korea, solar, software, and AI themes could mean crowded positioning and abrupt profit-taking during the scoring week.; A risk-off move from weak labor data interpreted as recessionary rather than rate-friendly would likely hurt high-beta thematic equities more than the S&P 500.; Semiconductor or AI-leadership rotation into defensive or value sectors could cause concentrated underperformance versus the benchmark. |

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
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.04882039229725299 | -0.014646117689175897 | Strong momentum, AI capex acceleration, Q1 chip sales +25% QoQ; leading tech tape into payrolls week. |
| anthropic-claude-opus-4-7 | BROAD_AI_TECH | 25.0 | -0.07130124097201906 | -0.017825310243004766 | AI spending forecast +47% YoY 2026; persistent thematic momentum (+22% 30d). |
| anthropic-claude-opus-4-7 | NASDAQ100 | 20.0 | -0.045035286588839596 | -0.00900705731776792 | Growth leadership with strong breadth in tech/comms; benefits if jobs report cools rates. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | -0.04994734798569267 | -0.0074921021978539 | Hedge against hot CPI/PPI reacceleration, weakening dollar, sticky inflation expectations. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 10.0 | -0.02544173909173386 | -0.002544173909173386 | FY27 $1.5T defense budget tailwind; strong momentum with lower beta than pure tech. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.04882039229725299 | -0.014646117689175897 | Strong semiconductor momentum with SIA reporting Q1 2026 global chip sales up 25% QoQ; sustained AI-infrastructure demand supports continued near-term outperformance. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 25.0 | -0.056119762057597056 | -0.014029940514399264 | XLK leads sectors with broad AI/software tailwinds and robust momentum; benefits from strong recent trend and AI capex acceleration. |
| anthropic-claude-opus-4-8 | TAIWAN | 15.0 | -0.04572872318491261 | -0.0068593084777368914 | Semiconductor supply-chain exposure with very strong trailing momentum; rides global AI/electronics demand into the week. |
| anthropic-claude-opus-4-8 | MOMENTUM | 15.0 | -0.02957474044297803 | -0.004436211066446705 | Factor with strongest recent trend persistence (+4% 7d) and broad tech tilt, providing diversified momentum exposure. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 15.0 | -0.02544173909173386 | -0.0038162608637600792 | FY2027 $1.5T defense budget request supports orders backdrop; strong momentum and lower correlation to pure tech provides ballast. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | -0.04882039229725299 | -0.014646117689175897 | Strong recent momentum and structural growth in AI infrastructure support continued outperformance over a short horizon. |
| google-gemini-3-1-pro | SOFTWARE | 30.0 | -0.05715130361871834 | -0.0171453910856155 | High recent returns and strong AI-driven spending forecasts provide a favorable setup for the week. |
| google-gemini-3-1-pro | SOUTH_KOREA | 20.0 | -0.14886069843362848 | -0.029772139686725697 | Exceptional recent performance driven by semiconductor exports and global tech demand. |
| google-gemini-3-1-pro | BROAD_AI_TECH | 20.0 | -0.07130124097201906 | -0.014260248194403814 | Provides diversified exposure to the dominant AI theme, which continues to attract capital. |
| openai-gpt-5-5 | BROAD_AI_TECH | 30.0 | -0.07130124097201906 | -0.02139037229160572 | Strongest near-term thematic setup from AI spending forecasts and recent price momentum, with broad exposure across AI infrastructure and applications. |
| openai-gpt-5-5 | SOFTWARE | 25.0 | -0.05715130361871834 | -0.014287825904679585 | Software had exceptional 7-day and 30-day momentum and may benefit if upcoming labor/services data lowers rate pressure on growth equities. |
| openai-gpt-5-5 | SEMICONDUCTORS | 20.0 | -0.04882039229725299 | -0.009764078459450598 | Global semiconductor sales growth and AI infrastructure capex support continued leadership in chip-related equities over a short horizon. |
| openai-gpt-5-5 | SOUTH_KOREA | 15.0 | -0.14886069843362848 | -0.02232910476504427 | Very strong trailing momentum and heavy semiconductor/export sensitivity offer high beta to the same AI and chip cycle leadership. |
| openai-gpt-5-5 | SOLAR | 10.0 | -0.13363988838417684 | -0.013363988838417684 | Recent breakout momentum is the strongest in the universe, and a small allocation captures upside while limiting idiosyncratic clean-energy volatility. |
| xai-grok-4-3 | TECHNOLOGY | 40.0 | -0.056119762057597056 | -0.022447904823038822 | Strongest 7-day trailing return at 5.89% among sectors with continued AI and chip demand tailwinds into early June. |
| xai-grok-4-3 | MOMENTUM | 35.0 | -0.02957474044297803 | -0.010351159155042311 | 4.02% 7-day return and factor persistence likely to extend over the one-week window amid low VIX. |
| xai-grok-4-3 | SEMICONDUCTORS | 25.0 | -0.04882039229725299 | -0.012205098074313248 | 3.92% 7-day return and semiconductor sales growth provide concentrated exposure to the same growth theme. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.04882039229725299 | -0.04378783861151884 | -0.018764028058653882 | 0.07423174807360669 |  | False | False |
| xai-grok-4-3 | TECHNOLOGY | 3 | 0.65 | -0.056119762057597056 | -0.04500416205239438 | -0.019980351499529425 | 0.07544807151448224 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.04882039229725299 | -0.05151476135697587 | -0.026490950804110916 | 0.08195867081906373 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 4 | 0.75 | -0.04882039229725299 | -0.0758238966559209 | -0.05080008610305595 | 0.10626780611800876 |  | False | False |
| openai-gpt-5-5 | BROAD_AI_TECH | 5 | 0.37 | -0.07130124097201906 | -0.08113537025919786 | -0.0561115597063329 | 0.11157927972128572 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 946be403631922daf09efa27679432f26ff97624e0353fe6971e7138b0529ccc |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 4900201e33d76620905e229966724117d4209e7a454a0ecfff542ce6939779ff |
| manifest.yaml | c22f386d288731d50f2d2694462f2f0bfc546c7e302c1cabfaf2f20cb9f9b8a9 |
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
| Market fact report | research/market_fact_report.md | audit-only | 2f7a3c027caae9986cf7bcfa2affaa8b86940a369a0621db3b79e4d7fbc0f980 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 376ec056bd07849053be6c6552f8879f1a2b6fbe7a36b70d563f0776581a209d | yes |
| Final briefing | research/final_briefing.md | model-facing | 946be403631922daf09efa27679432f26ff97624e0353fe6971e7138b0529ccc | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
