# CapitalBench Report: CB-2026-06-02-1W / official-20260602-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260602-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 2 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round scored from the June 1, 2026 adjusted close to the June 8, 2026 adjusted close.
- Decision date: 2026-06-02
- Decision deadline: 2026-06-02T08:00:00Z
- Horizon: one week
- Entry date: 2026-06-01
- Exit date: 2026-06-08
- Entry rule: Use adjusted close on Monday, June 1, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Monday, June 8, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrate in semiconductor/tech momentum leaders supported by AI capex and strong trailing returns, anchored by SP500 to manage benchmark-relative risk. | Sharp tech/semiconductor pullback or factor rotation reversing recent momentum; Friday May jobs report (June 5) surprise shifting rate expectations and hitting growth stocks; Elevated forward P/E (25.9) leaves rich valuations vulnerable to any negative catalyst; Taiwan/semiconductor geopolitical or currency shock |
| xai-grok-4-3 | xai | portfolio | TECHNOLOGY | 5 | 0.6 | Recent 7-day returns and positive ISM manufacturing data favor overweighting technology, semiconductors, software, AI, and momentum factors for alpha versus the S&P 500. | June 5 employment report surprise could trigger broad equity rotation away from growth; Rising inflation prints may increase rate sensitivity and pressure high-valuation tech holdings; Profit-taking after outsized 7-day gains in AI-related names could reverse momentum quickly |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Momentum-led tech/semis with gold hedge to capture continuation while inflation prints stay hot. | Hot May payrolls (June 5) could spike yields and hit growth/tech; Momentum reversal/profit-taking in semis after strong run; Geopolitical Taiwan risk; Gold weakness if dollar rebounds |
| openai-gpt-5-5 | openai | portfolio | SOFTWARE | 5 | 0.33 | Allocate to the clearest short-term winners with supportive AI spending and semiconductor demand facts. The portfolio intentionally accepts high volatility to maximize one-week alpha versus the S&P 500. | A stronger-than-expected June 5 employment report could push yields higher and trigger a sharp selloff in high-valuation growth and AI equities.; The recent software, cybersecurity, and Korea rallies could reverse on profit-taking after very large trailing gains.; A weak ISM Services or labor-market deterioration could shift markets from growth leadership to defensive assets before the exit close.; Any adverse semiconductor supply-chain, export-control, or geopolitical headlines involving Korea or Taiwan could pressure AI-linked exposures.; High S&P 500 valuation and low VIX leave the portfolio vulnerable to a rapid risk-off move from crowded positioning. |
| google-gemini-3-1-pro | google | portfolio | SOUTH_KOREA | 3 | 0.65 | Allocation prioritizes assets with the highest 7-day and 30-day trailing returns to capture ongoing momentum in the technology and semiconductor-adjacent sectors. | Mean reversion risk if the recent extreme outperformance in South Korea and tech sectors reverses sharply.; Concentration risk in technology and semiconductor-adjacent themes, making the portfolio highly sensitive to shifts in AI sentiment.; Geopolitical or currency risks affecting South Korean equities. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| HEALTHCARE | Healthcare Sector | 147.84 | 152.65 | 0.03253517316017307 | 1 |
| REGIONAL_BANKS | Regional Banks | 68.31 | 70.36 | 0.03001024740155178 | 2 |
| ENERGY | Energy Sector | 57.3 | 58.33 | 0.01797556719022686 | 3 |
| REAL_ESTATE | Real Estate Sector | 43.27 | 44.03 | 0.017564132193205406 | 4 |
| LOW_VOL | US Low Volatility Equities | 71.31 | 72.47 | 0.016267003225354015 | 5 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.03 | 83.07 | 0.012678288431061668 | 6 |
| FINANCIALS | Financials Sector | 51.43 | 51.97 | 0.010499708341434877 | 7 |
| UTILITIES | Utilities Sector | 43.1 | 43.52 | 0.009744779582366636 | 8 |
| US_DOLLAR | US Dollar | 27.76 | 28.03 | 0.009726224783861648 | 9 |
| INDUSTRIALS | Industrials Sector | 172.4 | 173.63 | 0.007134570765661152 | 10 |
| DIVIDEND | US Dividend Equities | 32.18 | 32.29 | 0.003418272218769447 | 11 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.4 | 91.46 | 0.0006564551422318932 | 12 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 13 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.94 | 106.94 | 0.0 | 13 |
| LARGE_VALUE | US Large-Cap Value | 237.46 | 237.27 | -0.00080013475953844 | 15 |
| OIL | Crude Oil | 135.5 | 135.15 | -0.0025830258302582676 | 16 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.11 | 47.95 | -0.0033257119102056976 | 17 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.84 | 79.54 | -0.0037575150300600546 | 18 |
| YEN | Japanese Yen | 57.51 | 57.28 | -0.003999304468787934 | 19 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.68 | 98.17 | -0.005168220510741839 | 20 |
| UNITED_KINGDOM | United Kingdom Equities | 46.69 | 46.43 | -0.005568644249303922 | 21 |
| MID_CAP | US Mid-Cap Stocks | 74.54 | 74.11 | -0.005768714784008644 | 22 |
| MOMENTUM | US Momentum Equities | 316.93 | 315.08 | -0.005837251128009369 | 23 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.32 | 93.7 | -0.0065733672603900395 | 24 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.17 | 93.52 | -0.006902410534140424 | 25 |
| SMALL_VALUE | US Small-Cap Value | 212.74 | 211.25 | -0.00700385447024543 | 26 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.01 | 95.28 | -0.007603374648474159 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 209.21 | 207.61 | -0.007647817981932037 | 28 |
| TIPS | Treasury Inflation-Protected Securities | 109.98 | 109.13 | -0.00772867794144394 | 29 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.93 | 108.06 | -0.007986780501239354 | 30 |
| EURO | Euro | 107.33 | 106.42 | -0.008478524177769509 | 31 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.47 | 84.62 | -0.009945009945009908 | 32 |
| JAPAN | Japan Equities | 92.93 | 91.95 | -0.010545571935865694 | 33 |
| CANADA | Canada Equities | 58.71 | 58.06 | -0.011071367739737714 | 34 |
| EUROPE | Europe Equities | 88.52 | 87.52 | -0.011296882060551239 | 35 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 229.91 | 227.26 | -0.011526249401939914 | 36 |
| BROAD_COMMODITIES | Broad Commodities | 17.87 | 17.62 | -0.013989927252378243 | 37 |
| SEMICONDUCTORS | Semiconductors | 607.81 | 598.16 | -0.015876671986311486 | 38 |
| INDIA | India Equities | 47.99 | 47.21 | -0.016253386122108804 | 39 |
| SMALL_CAP | US Small-Cap Stocks | 288.98 | 284.11 | -0.016852377327150725 | 40 |
| MATERIALS | Materials Sector | 50.92 | 49.96 | -0.01885310290652009 | 41 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.19 | 115.39 | -0.023690667569168267 | 42 |
| TOTAL_US_MARKET | Total US Stock Market | 373.4 | 364.47 | -0.023915372254954326 | 43 |
| SP500 | S&P 500 | 758.54 | 739.22 | -0.02546998180715576 | 44 |
| CHINA | China Equities | 55.4 | 53.93 | -0.0265342960288808 | 45 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.87 | 69.86 | -0.027967162933073664 | 46 |
| AGRICULTURE | Agriculture Commodities | 27.24 | 26.33 | -0.03340675477239352 | 47 |
| GOLD | Gold | 84.27 | 81.38 | -0.03429452948854872 | 48 |
| EMERGING_MARKETS | Emerging Markets | 60.42 | 58.33 | -0.03459119496855356 | 49 |
| COPPER | Copper | 39.96 | 38.55 | -0.035285285285285406 | 50 |
| NASDAQ100 | Nasdaq 100 | 742.74 | 716.07 | -0.03590758542693262 | 51 |
| AUSTRALIA | Australia Equities | 29.13 | 28.07 | -0.036388602814967363 | 52 |
| MEXICO | Mexico Equities | 77.87 | 74.9 | -0.03814049056119173 | 53 |
| BIOTECH | Biotechnology | 133.62 | 128.43 | -0.038841490794791156 | 54 |
| COMMUNICATIONS | Communication Services Sector | 115.61 | 111.09 | -0.03909696393045581 | 55 |
| SOUTH_AFRICA | South Africa Equities | 67.62 | 64.83 | -0.041259982253771144 | 56 |
| LARGE_GROWTH | US Large-Cap Growth | 128.77 | 122.98 | -0.04496388910460514 | 57 |
| BRAZIL | Brazil Equities | 35.67 | 33.69 | -0.05550883095037862 | 58 |
| TAIWAN | Taiwan Equities | 106.42 | 100.43 | -0.056286412328509616 | 59 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 139.89 | 131.68 | -0.058688969904925115 | 60 |
| TECHNOLOGY | Technology Sector | 195.76 | 184.18 | -0.05915406620351438 | 61 |
| METALS_MINING | Metals and Mining | 127.46 | 118.59 | -0.069590459752079 | 62 |
| BROAD_AI_TECH | Broad AI Technology | 69.44 | 64.44 | -0.07200460829493083 | 63 |
| CYBERSECURITY | Cybersecurity | 94.15 | 86.13 | -0.08518321826872022 | 64 |
| SILVER | Silver | 67.67 | 61.58 | -0.08999556672085118 | 65 |
| SOLAR | Solar Energy | 71.13 | 63.58 | -0.10614368058484458 | 66 |
| SOFTWARE | Software | 107.7 | 95.65 | -0.11188486536675946 | 67 |
| BITCOIN_ETF | Bitcoin ETF | 40.49 | 35.89 | -0.11360829834527042 | 68 |
| SOUTH_KOREA | South Korea Equities | 216.7 | 185.64 | -0.14333179510844485 | 69 |
| ETHEREUM_ETF | Ethereum ETF | 15.11 | 12.72 | -0.158173395102581 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.015876671986311486 | -0.004763001595893446 | Strong momentum, ISM new orders accelerating, AI capex tailwind. |
| anthropic-claude-opus-4-7 | TECHNOLOGY | 25.0 | -0.05915406620351438 | -0.014788516550878594 | Tech leadership with strong trailing momentum and AI spend forecast. |
| anthropic-claude-opus-4-7 | SOFTWARE | 20.0 | -0.11188486536675946 | -0.022376973073351892 | Recent breakout, software PCE surge, momentum favorable. |
| anthropic-claude-opus-4-7 | TAIWAN | 15.0 | -0.056286412328509616 | -0.008442961849276441 | Semiconductor supply chain leverage with strong momentum. |
| anthropic-claude-opus-4-7 | GOLD | 10.0 | -0.03429452948854872 | -0.003429452948854872 | Hedge against sticky inflation prints and rising YoY CPI/PCE. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.015876671986311486 | -0.004763001595893446 | Strong momentum, robust semiconductor sales up 25% QoQ, AI capex tailwind, leading trailing returns. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 25.0 | -0.05915406620351438 | -0.014788516550878594 | Tech sector leading with broad AI infrastructure spending growth and strong recent momentum. |
| anthropic-claude-opus-4-8 | TAIWAN | 15.0 | -0.056286412328509616 | -0.008442961849276441 | Semiconductor supply-chain leverage with very strong recent momentum into the window. |
| anthropic-claude-opus-4-8 | MOMENTUM | 15.0 | -0.005837251128009369 | -0.0008755876692014053 | Momentum factor outperforming broadly; favorable risk appetite with low VIX and tight credit spreads. |
| anthropic-claude-opus-4-8 | SP500 | 15.0 | -0.02546998180715576 | -0.0038204972710733642 | Benchmark-relative core holding to maintain market exposure with positive trend. |
| google-gemini-3-1-pro | SOUTH_KOREA | 40.0 | -0.14333179510844485 | -0.057332718043377945 | South Korea has shown exceptional recent momentum, with a 19.05% 7-day return and 144.57% 6-month return, likely driven by strong semiconductor exports and AI-related demand. |
| google-gemini-3-1-pro | SOFTWARE | 30.0 | -0.11188486536675946 | -0.03356545961002783 | Software has demonstrated strong recent performance with a 14.56% 7-day return and 24.32% 30-day return, indicating positive sector momentum. |
| google-gemini-3-1-pro | CYBERSECURITY | 30.0 | -0.08518321826872022 | -0.025554965480616063 | Cybersecurity shows robust short-term momentum with an 11.71% 7-day return and 36.93% 30-day return, supported by strong AI-related spending forecasts. |
| openai-gpt-5-5 | SOFTWARE | 30.0 | -0.11188486536675946 | -0.03356545961002783 | Strongest short-term price momentum in the universe with 14.56% 7-day and 24.32% 30-day returns; AI/software spending datapoints support continued near-term risk appetite. |
| openai-gpt-5-5 | CYBERSECURITY | 25.0 | -0.08518321826872022 | -0.021295804567180054 | Cybersecurity has very strong 7-day and 30-day momentum and a supportive AI-security spending forecast, while being somewhat more diversified than single high-beta technology subsectors. |
| openai-gpt-5-5 | BROAD_AI_TECH | 20.0 | -0.07200460829493083 | -0.014400921658986167 | Broad AI technology exposure benefits from persistent AI capex and spending narratives, with strong recent momentum and less single-industry concentration than semiconductors alone. |
| openai-gpt-5-5 | SEMICONDUCTORS | 15.0 | -0.015876671986311486 | -0.002381500797946723 | Semiconductor sales growth and AI infrastructure capex remain supportive, and the group has continued positive momentum over 7-day, 30-day, 6-month, and 1-year windows. |
| openai-gpt-5-5 | SOUTH_KOREA | 10.0 | -0.14333179510844485 | -0.014333179510844486 | Extreme recent country momentum and semiconductor/export sensitivity provide high upside if the global AI and chip trade continues through the one-week window. |
| xai-grok-4-3 | TECHNOLOGY | 25.0 | -0.05915406620351438 | -0.014788516550878594 | Strongest 7-day trailing return at 8.52% with continued AI-driven momentum into the one-week window. |
| xai-grok-4-3 | SEMICONDUCTORS | 25.0 | -0.015876671986311486 | -0.0039691679965778714 | 5.46% 7-day return and semiconductor sales growth of 25% QoQ support near-term outperformance. |
| xai-grok-4-3 | SOFTWARE | 20.0 | -0.11188486536675946 | -0.022376973073351892 | 14.56% 7-day return and elevated software spending trends favor continued short-term gains. |
| xai-grok-4-3 | BROAD_AI_TECH | 15.0 | -0.07200460829493083 | -0.010800691244239624 | 10.56% 7-day return aligns with broad AI spending forecasts and sector momentum. |
| xai-grok-4-3 | MOMENTUM | 15.0 | -0.005837251128009369 | -0.0008755876692014053 | 4.39% 7-day return captures factor persistence likely to extend over the scoring horizon. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.015876671986311486 | -0.03269056493632325 | -0.007220583129167492 | 0.06522573809649632 |  | False | False |
| xai-grok-4-3 | TECHNOLOGY | 5 | 0.6 | -0.05915406620351438 | -0.052810936534249384 | -0.027340954727093622 | 0.08534610969442245 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.015876671986311486 | -0.05380090601825524 | -0.02833092421109948 | 0.08633607917842831 |  | False | False |
| openai-gpt-5-5 | SOFTWARE | 5 | 0.33 | -0.11188486536675946 | -0.08597686614498526 | -0.0605068843378295 | 0.11851203930515833 |  | False | False |
| google-gemini-3-1-pro | SOUTH_KOREA | 3 | 0.65 | -0.14333179510844485 | -0.11645314313402183 | -0.09098316132686607 | 0.1489883162941949 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | bfdcf917304fa7bc7ca0f4d4ac4a4b9b5de72e37ea6d5dec819fb7d7187d8c41 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 008220e22465445099de1977cb4d78a273377e5f259cbb9cefbde693e903d133 |
| manifest.yaml | 8852b2fb499d1c593b36073e7cf9801cad18ac0274e836d78e38aa046f30ecbe |
| market_data/universe_trailing_returns.csv | 71df7a03d263b99739fe3a0801d1298b5df12311f0ba83b10396f7e67f16d9fd |
| market_data/universe_trailing_returns.md | 2d8045022a85ce50d3dd78131aae3d6facc45dc80e7c693b0071003c7cf16dad |
| market_data/universe_trailing_returns.json | f2c37dc35a77f688e70c2db53dd46e05dc5d77fb0943fc54c1175ea814d41fdc |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 7a6f0e5604843432d585f11fdc744eddcbd2d6ae0c3f000a8d11d8279d2032a9 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 553d04a2fa1de707f2e8624f0b24dcd3f2a7098a8c9ac6990aa4c17b923fa8ed | yes |
| Final briefing | research/final_briefing.md | model-facing | bfdcf917304fa7bc7ca0f4d4ac4a4b9b5de72e37ea6d5dec819fb7d7187d8c41 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
