# CapitalBench Report: CB-2026-06-17-1M / official-20260617-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260617-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-17-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-17
- Decision deadline: 2026-06-18T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-17
- Exit date: 2026-07-17
- Entry rule: Use adjusted close prices on Wednesday, June 17, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, July 17, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.6 | Concentrate in trend-leading semiconductors, momentum, and Taiwan while balancing with industrials and short-duration cash to manage rate/inflation risk over the close-to-close month. | Hawkish FOMC dots and rising 10Y yield (4.43%) could trigger a growth/semiconductor drawdown before exit; Semiconductor and Taiwan concentration creates correlated downside if AI sentiment or July earnings disappoint; Sticky inflation (4.2% CPI, energy +23.5% YoY) could pressure multiples broadly; July CPI (7/14) and June jobs (7/2) surprises could spike volatility within the window |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.58 | Momentum-led equity tilt in semis/industrials/defense plus gold hedge; positioned for trend persistence into July CPI and earnings while hedging inflation/rate risk. | Semiconductor sentiment reversal after 84% 6m run; crowded positioning risk; Hawkish FOMC repricing lifts yields further, pressuring growth-heavy book; Hot June CPI print (July 14) triggers risk-off before exit close; Gold continues correcting if USD strength persists (DXY +0.85%); Geopolitical de-escalation hurts defense names |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 4 | 0.65 | Recent trailing returns favor semiconductors, momentum, aerospace/defense, and biotech; these exposures are positioned to benefit from AI, defense, and growth sentiment before July 17 exit. | Hotter-than-expected June CPI on July 14 could pressure rate-sensitive growth holdings; Post-FOMC dot plot repricing may trigger broad equity rotation away from momentum names; Semiconductor supply chain or China export restrictions could reverse recent gains |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.59 | Favor recent winners with clear near-term narratives: AI semiconductors, Asian tech supply chains, momentum factor exposure, and defense. The allocation is intentionally aggressive because the objective is maximizing one-month return relative to SPY, not minimizing drawdown. | A sharp reversal in crowded AI, semiconductor, or momentum trades could cause large underperformance versus the S&P 500.; Hot CPI/PPI data and higher Treasury yields could pressure high-valuation growth and technology exposures before the July exit.; South Korea and Taiwan country ETFs add currency and regional geopolitical risk, including China/Taiwan or North Korea-related shocks.; A broad risk-off move around the June employment report or July CPI release could hit high-beta equities more than SPY.; Semiconductor supply-chain earnings revisions or export-control headlines could specifically hurt the largest portfolio exposures. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.7 | Overweight technology and semiconductors to capture AI momentum. | A sudden reversal in AI sentiment or semiconductor demand.; Higher-than-expected inflation leading to a hawkish Fed surprise.; Geopolitical tensions impacting Asian markets and semiconductor supply chains. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 139.2581563428 | 154.26 | 0.10772685816887617 | 1 |
| CYBERSECURITY | Cybersecurity | 84.1574712685 | 92.36 | 0.09746643533680155 | 2 |
| OIL | Crude Oil | 114.23 | 123.96 | 0.08517902477457762 | 3 |
| REGIONAL_BANKS | Regional Banks | 70.7405020122 | 76.69 | 0.08410313495900756 | 4 |
| HEALTHCARE | Healthcare Sector | 150.0537752226 | 161.09 | 0.07354846461562281 | 5 |
| ETHEREUM_ETF | Ethereum ETF | 13.07 | 13.91 | 0.06426931905126243 | 6 |
| ENERGY | Energy Sector | 54.2835325771 | 57.68 | 0.06256901976812079 | 7 |
| LOW_VOL | US Low Volatility Equities | 73.1724270453 | 76.57 | 0.046432421226052956 | 8 |
| FINANCIALS | Financials Sector | 53.8623513913 | 56.26 | 0.04451436943926801 | 9 |
| BROAD_COMMODITIES | Broad Commodities | 16.54 | 17.25 | 0.04292623941958884 | 10 |
| REAL_ESTATE | Real Estate Sector | 43.5925530574 | 45.42 | 0.041921080882638906 | 11 |
| SOFTWARE | Software | 89.16 | 92.8 | 0.04082548227904881 | 12 |
| SMALL_VALUE | US Small-Cap Value | 213.69 | 222.34 | 0.0404791988394404 | 13 |
| DIVIDEND | US Dividend Equities | 31.67783564 | 32.91 | 0.03889673442348829 | 14 |
| AGRICULTURE | Agriculture Commodities | 26.84 | 27.84 | 0.037257824143070106 | 15 |
| BRAZIL | Brazil Equities | 34.11 | 35.23 | 0.0328349457637056 | 16 |
| LARGE_VALUE | US Large-Cap Value | 240.38 | 248.03 | 0.03182461103253176 | 17 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.0993882751 | 85.19 | 0.025157967685382365 | 18 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.1854057668 | 213.37 | 0.024903735274352412 | 19 |
| UTILITIES | Utilities Sector | 44.1790255467 | 45.17 | 0.022430880741189707 | 20 |
| UNITED_KINGDOM | United Kingdom Equities | 45.92 | 46.94 | 0.022212543554006814 | 21 |
| CANADA | Canada Equities | 58.19 | 59.45 | 0.021653205018044464 | 22 |
| COMMUNICATIONS | Communication Services Sector | 108.9108084759 | 110.65 | 0.015968952470726272 | 23 |
| SMALL_CAP | US Small-Cap Stocks | 289.88 | 294.04 | 0.014350765834138413 | 24 |
| MID_CAP | US Mid-Cap Stocks | 74.98 | 75.54 | 0.0074686583088823255 | 25 |
| EUROPE | Europe Equities | 88.0341045121 | 88.59 | 0.0063145469699597 | 26 |
| TOTAL_US_MARKET | Total US Stock Market | 364.7091278319 | 367.01 | 0.006308786900339092 | 27 |
| SP500 | S&P 500 | 739.0760202617 | 743.29 | 0.005701686460897193 | 28 |
| US_DOLLAR | US Dollar | 28.18 | 28.33 | 0.005322924059616652 | 29 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.3622642443 | 79.65 | 0.0036255991237130747 | 30 |
| AUSTRALIA | Australia Equities | 28.65 | 28.75 | 0.003490401396160525 | 31 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.262779785 | 91.55 | 0.0031471780245642123 | 32 |
| TIPS | Treasury Inflation-Protected Securities | 107.973895124 | 108.27 | 0.0027423746791754855 | 33 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.2561385364 | 115.44 | 0.001595242265920005 | 34 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.7099995878 | 93.84 | 0.0013872629684328341 | 35 |
| INDUSTRIALS | Industrials Sector | 179.1623491514 | 179.41 | 0.0013822706041364263 | 36 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 37 |
| BITCOIN_ETF | Bitcoin ETF | 36.36 | 36.35 | -0.0002750275027502136 | 38 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.853298049 | 93.78 | -0.0007809853305499326 | 39 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.2800504232 | 98.2 | -0.0008145134526823528 | 40 |
| CHINA | China Equities | 53.0 | 52.95 | -0.0009433962264150386 | 41 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.6931570277 | 106.58 | -0.0010605837417541064 | 42 |
| INDIA | India Equities | 49.06 | 48.91 | -0.0030574806359561224 | 43 |
| EURO | Euro | 105.9792125507 | 105.61 | -0.003483820475863264 | 44 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.8808433161 | 95.53 | -0.0036591596815991334 | 45 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.198963647 | 47.93 | -0.005580278633578906 | 46 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.3887197434 | 107.56 | -0.007645811716956441 | 47 |
| YEN | Japanese Yen | 57.09 | 56.51 | -0.010159397442634499 | 48 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.0101472506 | 84.52 | -0.017325249383172148 | 49 |
| LARGE_GROWTH | US Large-Cap Growth | 121.6 | 119.38 | -0.01825657894736843 | 50 |
| COPPER | Copper | 38.64 | 37.92 | -0.01863354037267073 | 51 |
| MATERIALS | Materials Sector | 51.8259858778 | 50.53 | -0.02500648768854663 | 52 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.6263661277 | 69.7 | -0.026894651115841106 | 53 |
| MEXICO | Mexico Equities | 77.31 | 75.11 | -0.028456861984219373 | 54 |
| EMERGING_MARKETS | Emerging Markets | 59.7402031525 | 57.84 | -0.03180777855156114 | 55 |
| NASDAQ100 | Nasdaq 100 | 721.7144075433 | 695.33 | -0.036557961525407134 | 56 |
| JAPAN | Japan Equities | 94.45 | 90.49 | -0.04192694547379572 | 57 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 242.79 | 230.73 | -0.049672556530334866 | 58 |
| GOLD | Gold | 79.64 | 75.5 | -0.05198392767453541 | 59 |
| TECHNOLOGY | Technology Sector | 185.5798751289 | 175.59 | -0.053830595165349826 | 60 |
| SOUTH_AFRICA | South Africa Equities | 66.51 | 62.36 | -0.062396632085400805 | 61 |
| TAIWAN | Taiwan Equities | 105.11 | 97.33 | -0.07401769574731232 | 62 |
| SOLAR | Solar Energy | 58.45 | 53.9 | -0.07784431137724557 | 63 |
| MOMENTUM | US Momentum Equities | 328.27 | 302.09 | -0.07975142413257386 | 64 |
| BROAD_AI_TECH | Broad AI Technology | 64.329547229 | 58.7 | -0.08751106562214661 | 65 |
| SEMICONDUCTORS | Semiconductors | 623.97 | 556.53 | -0.10808211933266032 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 131.44 | 116.14 | -0.11640292148508824 | 67 |
| SILVER | Silver | 60.61 | 50.78 | -0.1621844580102293 | 68 |
| METALS_MINING | Metals and Mining | 118.3076867236 | 98.35 | -0.16869306869490885 | 69 |
| SOUTH_KOREA | South Korea Equities | 205.08 | 162.54 | -0.20743124634289067 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | -0.10808211933266032 | -0.03782874176643111 | Strongest momentum with AI capex cycle intact; SMH leading with 14% 30d return and broad-based chip demand. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | 0.0013822706041364263 | 0.0002764541208272853 | Strong momentum with aerospace/defense tailwind; benefits from capex and reshoring without rate sensitivity. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | -0.049672556530334866 | -0.0074508834795502295 | Geopolitical tailwinds and strong trend; 10% 30d return shows persistent flows. |
| anthropic-claude-opus-4-7 | MOMENTUM | 20.0 | -0.07975142413257386 | -0.015950284826514772 | Factor with strongest persistence; captures broad winners across sectors during this regime. |
| anthropic-claude-opus-4-7 | GOLD | 10.0 | -0.05198392767453541 | -0.005198392767453541 | Hedge against sticky inflation (CPI 4.2%) and hawkish Fed disappointment; recent pullback offers entry. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.10808211933266032 | -0.032424635799798096 | Strongest momentum across all timeframes (84% 6m, 14% 30d); AI capex cycle and semiconductor supply chain remain dominant earnings driver heading into July earnings season. |
| anthropic-claude-opus-4-8 | MOMENTUM | 20.0 | -0.07975142413257386 | -0.015950284826514772 | Momentum factor leading broad market with persistent trend; captures rotation winners with lower single-sector concentration risk than pure semis. |
| anthropic-claude-opus-4-8 | TAIWAN | 15.0 | -0.07401769574731232 | -0.011102654362096847 | Strong semiconductor-linked momentum (14.5% 30d) with TSMC earnings as a catalyst in mid-July; benefits from same AI demand theme. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | 0.0013822706041364263 | 0.0002764541208272853 | Broad strength (5.8% 7d, 5.2% 30d) supported by aerospace/defense and resilient retail sales; cyclical exposure with less rate sensitivity. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.0031471780245642123 | 0.0004720767036846318 | Hedge against sticky inflation (CPI 4.2% YoY, hawkish dots) and rising yields; provides ballast given elevated VIX and FOMC hawkish tilt risk to equities. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | -0.10808211933266032 | -0.04323284773306413 | Strong recent momentum and AI tailwinds support continued outperformance in the near term. |
| google-gemini-3-1-pro | SOUTH_KOREA | 30.0 | -0.20743124634289067 | -0.0622293739028672 | High correlation with semiconductor strength and strong recent performance. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | -0.053830595165349826 | -0.01614917854960495 | Broad technology exposure to capture ongoing AI and growth themes. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.10808211933266032 | -0.03782874176643111 | Strongest AI-linked momentum in the universe with very large 7-day, 30-day, 6-month, and 1-year relative strength; likely to benefit if risk appetite and AI capex narratives persist into July. |
| openai-gpt-5-5 | SOUTH_KOREA | 25.0 | -0.20743124634289067 | -0.05185781158572267 | Exceptional recent and medium-term momentum with heavy semiconductor/export sensitivity, offering high beta to the same global electronics and AI cycle. |
| openai-gpt-5-5 | TAIWAN | 15.0 | -0.07401769574731232 | -0.011102654362096847 | Semiconductor supply-chain exposure with strong 30-day and 6-month performance, complementing direct US semiconductor exposure. |
| openai-gpt-5-5 | MOMENTUM | 15.0 | -0.07975142413257386 | -0.011962713619886078 | Broad factor exposure to recent winners, which may continue to outperform during a one-month trend-following window. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 10.0 | -0.049672556530334866 | -0.004967255653033487 | Recent strong relative performance and a differentiated catalyst set tied to defense budgets and geopolitical risk, adding some diversification away from pure AI chips. |
| xai-grok-4-3 | SEMICONDUCTORS | 40.0 | -0.10808211933266032 | -0.04323284773306413 | Strongest 30-day momentum among options at +14.25%, driven by AI supply chain demand likely to persist through July window. |
| xai-grok-4-3 | MOMENTUM | 30.0 | -0.07975142413257386 | -0.023925427239772156 | Leading factor performer at +11.66% 30d; trend persistence expected to capture continued rotation into high-momentum names before exit. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 20.0 | -0.049672556530334866 | -0.009934511306066974 | Solid +10.32% 30d return with defense budget visibility and geopolitical support likely to hold through mid-July. |
| xai-grok-4-3 | BIOTECH | 10.0 | 0.10772685816887617 | 0.010772685816887617 | Recent +9.18% 30d rebound in sector with clinical catalysts and risk-on flows that can extend into the scoring period. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.6 | -0.10808211933266032 | -0.05872904416389779 | -0.06443073062479499 | 0.16645590233277396 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.58 | -0.10808211933266032 | -0.06615184871912237 | -0.07185353518001956 | 0.17387870688799856 |  | False | False |
| xai-grok-4-3 | SEMICONDUCTORS | 4 | 0.65 | -0.10808211933266032 | -0.06632010046201564 | -0.07202178692291283 | 0.1740469586308918 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.59 | -0.10808211933266032 | -0.11771917698717019 | -0.12342086344806738 | 0.22544603515604636 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.7 | -0.10808211933266032 | -0.12161140018553628 | -0.12731308664643348 | 0.22933825835441246 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 04e0d7ac3ce6f3b67a916c35394fccc913537a534fcded2c9af7587120180f8b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | b3723469bc763138dba77e896fe8a1ae181b37b613816ad1564eb1bba22f60e3 |
| market_data/universe_trailing_returns.csv | 8484381f73e409ff4c8e15b17071e17bcaac3b829942225b60e1a019ba5f6981 |
| market_data/universe_trailing_returns.md | 91452b51c171ea470098a12a1ffbe35e131fef5599da894053747e045df5f433 |
| market_data/universe_trailing_returns.json | 45b8aaa0061ca5a562dc7a9d135d9da10d604fecaf962483c6227ad341f16f7c |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 9786a39d65e7d9d88e47397edbe747c3331126b9ff6c9d2c319718223f5e2ec6 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | b66fd001e089b7e687b7f5bf775008deb61635a9c9a2129a791d940e7c072478 | yes |
| Final briefing | research/final_briefing.md | model-facing | 04e0d7ac3ce6f3b67a916c35394fccc913537a534fcded2c9af7587120180f8b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
