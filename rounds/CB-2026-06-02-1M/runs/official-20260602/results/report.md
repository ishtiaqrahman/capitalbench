# CapitalBench Report: CB-2026-06-02-1M / official-20260602

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260602
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 2 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round scored from the June 1, 2026 adjusted close to the July 1, 2026 adjusted close.
- Decision date: 2026-06-02
- Decision deadline: 2026-06-02T08:00:00Z
- Horizon: one month
- Entry date: 2026-06-01
- Exit date: 2026-07-01
- Entry rule: Use adjusted close on Monday, June 1, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Wednesday, July 1, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | TECHNOLOGY | 3 | 0.55 | Tech and momentum factors show the strongest recent performance and forward catalysts within the scoring window amid mixed macro data. | Hotter-than-expected CPI or PPI releases on June 10-11 pressuring rate-sensitive growth stocks; FOMC June 16-17 outcome or guidance shifting rate expectations; Weak May employment report on June 5 amplifying growth concerns |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.75 | Overweighting technology and semiconductors against a core S&P 500 holding to capture AI-driven growth and momentum. | A sudden rotation out of high-valuation technology stocks could cause the portfolio to underperform the broader market.; Sticky inflation data in the upcoming CPI release could lead to higher rate expectations, disproportionately impacting growth equities.; Any delays or reductions in anticipated AI capital expenditures by major tech companies could negatively impact the semiconductor allocation. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Overweight AI/semis/tech where earnings momentum and capex cycles dominate, with gold and defense as inflation/geopolitical hedges into June FOMC. | Hawkish June FOMC surprise given CPI reacceleration to 3.8% YoY could compress growth multiples; Oil at $92 and PPI +6% YoY may spark stagflation fears hurting high-multiple tech; Semis/tech have run hard (SMH +19% 30d); profit-taking risk into month-end; Consumer sentiment at 44.8 signals demand deterioration risk; Dollar weakness or yen intervention could disrupt cross-asset positioning |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Lean into the dominant AI/semiconductor trend with diversification across chips, Taiwan supply chain, broad AI, tech sector, and cybersecurity to maximize one-month alpha. | Crowded mega-cap tech/semi trade vulnerable to sharp factor rotation or profit-taking before July 1 exit; Elevated forward P/E (25.9) and high inflation prints (CPI 3.8% YoY, PPI 6%) could pressure rate-sensitive growth names; Taiwan/semi concentration exposes portfolio to geopolitical or supply-chain headline shock; June 16-17 FOMC and June CPI/PPI releases could trigger hawkish repricing hitting high-beta growth |
| openai-gpt-5-5 | openai | portfolio | CYBERSECURITY | 5 | 0.33 | Near-term market leadership is concentrated in AI-adjacent technology and select semiconductor-linked exposures. The allocation prioritizes trend persistence through July 1 while diversifying across related but distinct growth themes. | A hotter-than-expected CPI or PPI release could lift yields and trigger a sharp valuation reset in long-duration technology stocks.; Extreme recent gains in cybersecurity, software, and South Korea could reverse if momentum unwinds or investors rotate into value and defensives.; Any disappointment in AI infrastructure spending expectations or semiconductor demand could disproportionately hurt all selected holdings.; A broader risk-off shock around the June FOMC meeting or geopolitical headlines could compress high-beta thematic equity multiples. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 133.4936139646 | 156.55 | 0.1727152734176043 | 1 |
| REGIONAL_BANKS | Regional Banks | 67.9168473992 | 76.18 | 0.12166572680017151 | 2 |
| HEALTHCARE | Healthcare Sector | 147.1962718394 | 159.54 | 0.08385897282825039 | 3 |
| FINANCIALS | Financials Sector | 51.2514474016 | 54.78 | 0.06884786239792806 | 4 |
| INDUSTRIALS | Industrials Sector | 171.9798941742 | 183.36 | 0.06617114099554566 | 5 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 229.7516900528 | 243.86 | 0.061406773303638085 | 6 |
| LOW_VOL | US Low Volatility Equities | 71.1761802291 | 75.24 | 0.05709522143250001 | 7 |
| SMALL_VALUE | US Small-Cap Value | 211.9741995509 | 221.71 | 0.04592917661548812 | 8 |
| UTILITIES | Utilities Sector | 42.8276203568 | 44.77 | 0.04535343376582457 | 9 |
| SMALL_CAP | US Small-Cap Stocks | 288.2998290393 | 299.32 | 0.038224687809987445 | 10 |
| MOMENTUM | US Momentum Equities | 316.5902331944 | 328.1 | 0.03635540708083851 | 11 |
| LARGE_VALUE | US Large-Cap Value | 236.7205662467 | 243.88 | 0.030244240569443193 | 12 |
| REAL_ESTATE | Real Estate Sector | 42.8985619921 | 44.18 | 0.029871351122118917 | 13 |
| MID_CAP | US Mid-Cap Stocks | 74.355029173 | 76.44 | 0.02804075057450306 | 14 |
| US_DOLLAR | US Dollar | 27.76 | 28.49 | 0.026296829971181435 | 15 |
| INDIA | India Equities | 47.99 | 49.21 | 0.02542196290893939 | 16 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.404558785 | 213.41 | 0.024017906538041922 | 17 |
| CONSUMER_STAPLES | Consumer Staples Sector | 81.4608367615 | 83.3 | 0.022577269171499825 | 18 |
| SEMICONDUCTORS | Semiconductors | 607.81 | 620.46 | 0.020812424935424012 | 19 |
| JAPAN | Japan Equities | 92.4376657495 | 93.05 | 0.006624293739300846 | 20 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.6532642788 | 107.34 | 0.006438956424295039 | 21 |
| MATERIALS | Materials Sector | 50.7300884448 | 51.02 | 0.0057147851322092436 | 22 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.9994233297 | 48.27 | 0.005637081688283141 | 23 |
| EUROPE | Europe Equities | 87.3336202108 | 87.77 | 0.004996698730073135 | 24 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.1533335516 | 85.52 | 0.004305955305646592 | 25 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.6119983779 | 96.02 | 0.004267263826945644 | 26 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.1331593177 | 91.4 | 0.0029280306344889873 | 27 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.8595050115 | 94.03 | 0.0018164914515488295 | 28 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.3498162028 | 98.5 | 0.0015270368872912776 | 29 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.4717568954 | 79.59 | 0.0014878632261223768 | 30 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.9506711716 | 118.09 | 0.001181246592461438 | 31 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.9828333367 | 94.02 | 0.0003954622560360388 | 32 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 33 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.5481588825 | 108.46 | -0.0008121637751169475 | 34 |
| UNITED_KINGDOM | United Kingdom Equities | 46.026395199 | 45.94 | -0.0018770794155498205 | 35 |
| DIVIDEND | US Dividend Equities | 31.925861287 | 31.85 | -0.002376170413008971 | 36 |
| TIPS | Treasury Inflation-Protected Securities | 108.9146930729 | 108.17 | -0.006837397709063442 | 37 |
| TAIWAN | Taiwan Equities | 106.42 | 105.69 | -0.006859612854726582 | 38 |
| TOTAL_US_MARKET | Total US Stock Market | 372.3271771994 | 369.27 | -0.008210996635796941 | 39 |
| CANADA | Canada Equities | 58.4368086632 | 57.67 | -0.013122014715408081 | 40 |
| AGRICULTURE | Agriculture Commodities | 27.24 | 26.86 | -0.013950073421439058 | 41 |
| SP500 | S&P 500 | 756.6113210015 | 745.76 | -0.014342001897534984 | 42 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.4970407445 | 70.36 | -0.015903325965102466 | 43 |
| EMERGING_MARKETS | Emerging Markets | 60.349491297 | 59.22 | -0.018715837908912847 | 44 |
| YEN | Japanese Yen | 57.51 | 56.43 | -0.018779342723004633 | 45 |
| MEXICO | Mexico Equities | 76.7469899965 | 75.27 | -0.01924492408845435 | 46 |
| EURO | Euro | 107.2583581619 | 104.95 | -0.021521475822104952 | 47 |
| NASDAQ100 | Nasdaq 100 | 741.9221312629 | 725.17 | -0.02257936588895737 | 48 |
| CYBERSECURITY | Cybersecurity | 94.0689293592 | 91.11 | -0.03145490630494363 | 49 |
| BRAZIL | Brazil Equities | 35.3326830366 | 34.18 | -0.032623705236479617 | 50 |
| AUSTRALIA | Australia Equities | 28.7233962229 | 27.7 | -0.03562935994609473 | 51 |
| LARGE_GROWTH | US Large-Cap Growth | 128.6595324041 | 123.02 | -0.04383299316203859 | 52 |
| COMMUNICATIONS | Communication Services Sector | 115.3038330394 | 109.74 | -0.04825366939448417 | 53 |
| TECHNOLOGY | Technology Sector | 195.5280751089 | 185.62 | -0.05067341405259407 | 54 |
| SOUTH_AFRICA | South Africa Equities | 66.218153385 | 62.73 | -0.0526766937265597 | 55 |
| CHINA | China Equities | 55.0379946789 | 51.525 | -0.06382853698422963 | 56 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 139.89 | 130.44 | -0.06755307741797123 | 57 |
| COPPER | Copper | 39.96 | 37.21 | -0.0688188188188188 | 58 |
| ENERGY | Energy Sector | 56.8949408572 | 52.81 | -0.0717979629762292 | 59 |
| BROAD_AI_TECH | Broad AI Technology | 69.4395112635 | 63.63 | -0.08366290542361132 | 60 |
| GOLD | Gold | 84.27 | 75.96 | -0.09861160555357784 | 61 |
| BROAD_COMMODITIES | Broad Commodities | 17.87 | 15.78 | -0.11695579182988258 | 62 |
| SOFTWARE | Software | 107.6804437071 | 93.34 | -0.1331759343981459 | 63 |
| SOUTH_KOREA | South Korea Equities | 216.7 | 185.5 | -0.14397784956160586 | 64 |
| BITCOIN_ETF | Bitcoin ETF | 40.49 | 34.0 | -0.16028649049147947 | 65 |
| METALS_MINING | Metals and Mining | 127.3713806047 | 104.36 | -0.18066366632325626 | 66 |
| SOLAR | Solar Energy | 71.13 | 57.8 | -0.18740334598622244 | 67 |
| ETHEREUM_ETF | Ethereum ETF | 15.11 | 12.19 | -0.1932495036399735 | 68 |
| SILVER | Silver | 67.67 | 53.58 | -0.20821634402246203 | 69 |
| OIL | Crude Oil | 135.5 | 103.27 | -0.23785977859778595 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | 0.020812424935424012 | 0.006243727480627203 | Strong momentum, AI capex acceleration, ISM new orders rising, semiconductor sales +25% QoQ. |
| anthropic-claude-opus-4-7 | TECHNOLOGY | 25.0 | -0.05067341405259407 | -0.012668353513148517 | Tech leadership with strong earnings, AI spending forecast +47% YoY, ISM manufacturing reaccelerating. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | -0.09861160555357784 | -0.014791740833036676 | Hedge against rising inflation (CPI 3.8%, PPI 6.0% YoY) and elevated geopolitical/oil risk. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | 0.061406773303638085 | 0.009211015995545713 | $1.5T FY27 defense budget request, strong durable goods orders +7.9%, geopolitical tailwinds. |
| anthropic-claude-opus-4-7 | CYBERSECURITY | 15.0 | -0.03145490630494363 | -0.004718235945741544 | Strong sector momentum (+37% 30d), AI-driven cybersecurity spend forecast $86B in 2026. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | 0.020812424935424012 | 0.006243727480627203 | Strong momentum, +25% QoQ global semi sales, AI capex tailwind set to rise 75% in 2026; leadership trend intact. |
| anthropic-claude-opus-4-8 | TAIWAN | 20.0 | -0.006859612854726582 | -0.0013719225709453164 | Semiconductor supply-chain leverage with strong trailing momentum and Q1 global chip sales surge. |
| anthropic-claude-opus-4-8 | BROAD_AI_TECH | 20.0 | -0.08366290542361132 | -0.016732581084722264 | Gartner $2.59T AI spend forecast (+47% YoY); broad AI exposure with persistent strength. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 15.0 | -0.05067341405259407 | -0.00760101210788911 | Tech sector leadership, strongest 30d sector return; software/AI inflection supports continuation. |
| anthropic-claude-opus-4-8 | CYBERSECURITY | 15.0 | -0.03145490630494363 | -0.004718235945741544 | AI cybersecurity spend forecast to rise to ~$86B in 2026; strong 30d momentum. |
| google-gemini-3-1-pro | SP500 | 40.0 | -0.014342001897534984 | -0.005736800759013994 | Provides broad US equity exposure as a core holding to track the benchmark while allowing satellite tilts. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | -0.05067341405259407 | -0.01520202421577822 | Strong momentum and continued AI infrastructure spending provide a catalyst for outperformance. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | 0.020812424935424012 | 0.006243727480627203 | High growth in global semiconductor sales and AI capex forecasts support continued strength in the sector. |
| openai-gpt-5-5 | CYBERSECURITY | 30.0 | -0.03145490630494363 | -0.009436471891483089 | Strongest 30-day relative momentum in the universe, with a supportive near-term narrative from rising AI-related cybersecurity spending. |
| openai-gpt-5-5 | SOFTWARE | 25.0 | -0.1331759343981459 | -0.033293983599536475 | Recent price leadership is broadening beyond semiconductors, and the briefing cites unusually strong software-category pricing momentum. |
| openai-gpt-5-5 | BROAD_AI_TECH | 20.0 | -0.08366290542361132 | -0.016732581084722264 | Provides diversified exposure to the AI spending and infrastructure theme, supported by large 2026 AI spending forecasts and strong recent trend. |
| openai-gpt-5-5 | SEMICONDUCTORS | 15.0 | 0.020812424935424012 | 0.0031218637403136015 | Semiconductor sales growth and AI infrastructure capex remain key catalysts, while the group continues to show strong intermediate momentum. |
| openai-gpt-5-5 | SOUTH_KOREA | 10.0 | -0.14397784956160586 | -0.014397784956160587 | High-beta semiconductor/export exposure with exceptional recent momentum, included as a smaller satellite due to elevated reversal risk. |
| xai-grok-4-3 | TECHNOLOGY | 40.0 | -0.05067341405259407 | -0.02026936562103763 | Strong 30-day trailing return of 20.94% and ISM manufacturing strength support continued tech outperformance into July. |
| xai-grok-4-3 | SEMICONDUCTORS | 35.0 | 0.020812424935424012 | 0.007284348727398404 | Q1 semiconductor sales up 25% and high AI spending forecasts position the sector for near-term gains. |
| xai-grok-4-3 | MOMENTUM | 25.0 | 0.03635540708083851 | 0.009088851770209627 | Leading 30-day return of 11.17% and factor persistence likely to extend through the one-month window. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | TECHNOLOGY | 3 | 0.55 | -0.05067341405259407 | -0.0038961651234295964 | 0.010445836774105387 | 0.1766114385410339 |  | True | False |
| google-gemini-3-1-pro | SP500 | 3 | 0.75 | -0.014342001897534984 | -0.014695097494165012 | -0.0003530955966300278 | 0.1874103709117693 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | 0.020812424935424012 | -0.01672358681575382 | -0.002381584918218837 | 0.1894388602333581 |  | False | False |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | 0.020812424935424012 | -0.02418002422867103 | -0.009838022331136047 | 0.1968952976462753 |  | False | False |
| openai-gpt-5-5 | CYBERSECURITY | 5 | 0.33 | -0.03145490630494363 | -0.07073895779158881 | -0.05639695589405383 | 0.2434542312091931 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 48c18e1b10207b4f0438ad302f4da26e48e673336876cf9924befb1d090fca5e |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 8eb0483e2ff6a07db9b46bad7176cfbe2ebbd28eef2df6e0c31196f680d27ad3 |
| manifest.yaml | 1a651fd4bcbbb6198b95d8ab6623961654d1d7b956b87703dd9fb3d2aa7843a7 |
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
| Market fact report | research/market_fact_report.md | audit-only | 1d42b985b60fc8a208c88daecf3f3e843bbc854ae84ab6089d7d952e159794ee | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 836783c9ed1528c72cc70c57dade2061cef0252b9df8d3e061542bb850a317d7 | yes |
| Final briefing | research/final_briefing.md | model-facing | 48c18e1b10207b4f0438ad302f4da26e48e673336876cf9924befb1d090fca5e | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
