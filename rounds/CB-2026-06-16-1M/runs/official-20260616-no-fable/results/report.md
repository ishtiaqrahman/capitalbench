# CapitalBench Report: CB-2026-06-16-1M / official-20260616-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260616-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-16-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-16
- Decision deadline: 2026-06-17T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-16
- Exit date: 2026-07-16
- Entry rule: Use adjusted close prices on Tuesday, June 16, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Thursday, July 16, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 4 | 0.65 | Concentrated in high-momentum equity factors with positive near-term catalysts and limited bond or commodity exposure given hot inflation data. | Hawkish FOMC reaction to May CPI could pressure growth and momentum holdings; July 14 CPI release may trigger volatility if hotter than expected; Oil price weakness may weigh on broader risk sentiment |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrated in trending winners with a gold hedge given 4.2% CPI, soft sentiment, and pending FOMC. | Hawkish FOMC surprise hits growth/semis; Oil rebound or geopolitical shock pressures equities; Momentum factor reversal post-FOMC |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.62 | Momentum-led growth concentration in semis/AI with diversification into industrials and a gold inflation/event hedge. | Hawkish FOMC outcome on June 17 (after cutoff) could trigger growth/semis drawdown given 4.47% 10y yields; Semiconductor and South Korea positions are highly correlated, amplifying any tech-sentiment reversal; Hot June CPI on July 14 could pressure rate-sensitive growth before exit close; Crowded momentum trade vulnerable to sharp factor rotation |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 5 | 0.75 | Overweighting high-momentum sectors like semiconductors and technology, along with South Korea, to capture ongoing market trends and maximize one-month relative returns. | A hawkish surprise from the upcoming FOMC meeting could disproportionately hurt high-valuation technology and growth stocks.; A sudden reversal in the semiconductor and AI momentum trade would lead to significant underperformance.; Geopolitical tensions or trade disruptions in Asia could negatively impact the South Korean equity allocation. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.63 | For a one-month contest, trend persistence and high-beta leadership appear more compelling than defensive assets despite elevated inflation and FOMC risk. The allocation is intentionally concentrated in assets with recent relative strength most likely to produce benchmark alpha if risk appetite remains constructive. | A hawkish FOMC statement or upside June CPI could pressure high-duration growth and AI-related equities before the exit date.; Semiconductor, Korea, and Taiwan exposures are highly correlated, so an AI hardware or chip-cycle reversal could cause broad underperformance.; Very strong trailing returns in South Korea and Taiwan raise the risk of profit-taking or crowded-position unwind over the month.; Geopolitical tension in East Asia or trade restrictions affecting semiconductor supply chains could disproportionately hit the largest allocations.; A rotation into value, defensives, or cash-like assets could leave high-momentum technology themes lagging the S&P 500. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 135.2119870825 | 152.0 | 0.1241606848604091 | 1 |
| REGIONAL_BANKS | Regional Banks | 72.0727897521 | 77.92 | 0.08112923432008046 | 2 |
| CYBERSECURITY | Cybersecurity | 85.0067393509 | 91.89 | 0.08097311697472032 | 3 |
| HEALTHCARE | Healthcare Sector | 152.2740653078 | 161.8 | 0.06255782738146998 | 4 |
| FINANCIALS | Financials Sector | 54.1613098634 | 56.75 | 0.04779592929212617 | 5 |
| ETHEREUM_ETF | Ethereum ETF | 13.54 | 14.13 | 0.04357459379615958 | 6 |
| ENERGY | Energy Sector | 54.9686549015 | 57.02 | 0.037318451800864905 | 7 |
| SMALL_VALUE | US Small-Cap Value | 216.2 | 224.18 | 0.03691026827012034 | 8 |
| AGRICULTURE | Agriculture Commodities | 26.66 | 27.59 | 0.03488372093023262 | 9 |
| LOW_VOL | US Low Volatility Equities | 74.3601939009 | 76.94 | 0.034693375094450474 | 10 |
| OIL | Crude Oil | 115.47 | 119.3 | 0.033168788429895235 | 11 |
| LARGE_VALUE | US Large-Cap Value | 242.96 | 249.46 | 0.026753375041159044 | 12 |
| BRAZIL | Brazil Equities | 34.41 | 35.33 | 0.026736413833188033 | 13 |
| SOFTWARE | Software | 91.37 | 93.7 | 0.025500711393236175 | 14 |
| DIVIDEND | US Dividend Equities | 32.2730971929 | 33.04 | 0.02376291319411128 | 15 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.3531630296 | 215.06 | 0.01753859236012878 | 16 |
| BROAD_COMMODITIES | Broad Commodities | 16.67 | 16.96 | 0.01739652069586084 | 17 |
| REAL_ESTATE | Real Estate Sector | 44.7128529199 | 45.46 | 0.016709895059446644 | 18 |
| UTILITIES | Utilities Sector | 44.7752337187 | 45.47 | 0.015516753874806444 | 19 |
| US_DOLLAR | US Dollar | 27.93 | 28.34 | 0.014679556032939578 | 20 |
| SMALL_CAP | US Small-Cap Stocks | 292.08 | 295.59 | 0.01201725554642552 | 21 |
| UNITED_KINGDOM | United Kingdom Equities | 46.51 | 46.97 | 0.009890346162115593 | 22 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.9961357847 | 85.81 | 0.009575308427686169 | 23 |
| COMMUNICATIONS | Communication Services Sector | 112.022545861 | 112.65 | 0.0056011415753625116 | 24 |
| CANADA | Canada Equities | 59.11 | 59.39 | 0.004736931145322254 | 25 |
| INDUSTRIALS | Industrials Sector | 179.4117399492 | 180.15 | 0.004114892654232261 | 26 |
| TOTAL_US_MARKET | Total US Stock Market | 369.3058827513 | 370.58 | 0.0034500323666872834 | 27 |
| SP500 | S&P 500 | 748.422195912 | 750.72 | 0.003070197677929709 | 28 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.2528089798 | 91.53 | 0.00303761630243482 | 29 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.6608805653 | 79.8 | 0.0017463958936023705 | 30 |
| MID_CAP | US Mid-Cap Stocks | 75.93 | 75.99 | 0.000790201501382759 | 31 |
| CHINA | China Equities | 54.13 | 54.14 | 0.0001847404396821961 | 32 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 33 |
| EUROPE | Europe Equities | 88.8036506459 | 88.79 | -0.00015371717041712252 | 34 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.8826475852 | 106.62 | -0.002457345426353119 | 35 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.6388458613 | 98.13 | -0.005158676146875374 | 36 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.2083510002 | 93.72 | -0.005183733660713008 | 37 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.2189176788 | 47.96 | -0.005369628586952557 | 38 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.3564928204 | 93.76 | -0.006321693426390662 | 39 |
| TIPS | Treasury Inflation-Protected Securities | 108.6968240742 | 107.97 | -0.006686709389998713 | 40 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.269226458 | 95.59 | -0.007055488892874107 | 41 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.2201244352 | 117.34 | -0.007444793679627915 | 42 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.7374928601 | 107.5 | -0.011380553547359673 | 43 |
| AUSTRALIA | Australia Equities | 28.98 | 28.63 | -0.012077294685990392 | 44 |
| YEN | Japanese Yen | 57.19 | 56.45 | -0.012939325056828044 | 45 |
| EURO | Euro | 107.0484983351 | 105.57 | -0.013811481320100238 | 46 |
| INDIA | India Equities | 49.41 | 48.69 | -0.014571948998178486 | 47 |
| LARGE_GROWTH | US Large-Cap Growth | 123.35 | 121.2 | -0.01743007701661936 | 48 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.8706659507 | 84.21 | -0.019339153042709945 | 49 |
| EMERGING_MARKETS | Emerging Markets | 60.0897947108 | 58.84 | -0.020798784832183337 | 50 |
| BITCOIN_ETF | Bitcoin ETF | 37.17 | 36.39 | -0.02098466505246166 | 51 |
| JAPAN | Japan Equities | 94.12 | 91.91 | -0.02348066298342555 | 52 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.9447055327 | 70.03 | -0.02661357105464468 | 53 |
| MATERIALS | Materials Sector | 52.5233751533 | 50.89 | -0.03109806154940864 | 54 |
| NASDAQ100 | Nasdaq 100 | 729.056314085 | 705.94 | -0.03170717218739416 | 55 |
| TAIWAN | Taiwan Equities | 103.79 | 100.16 | -0.03497446767511325 | 56 |
| MEXICO | Mexico Equities | 77.98 | 75.22 | -0.0353936906899206 | 57 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.52 | 230.89 | -0.0360303941215766 | 58 |
| COPPER | Copper | 39.55 | 38.06 | -0.0376738305941845 | 59 |
| TECHNOLOGY | Technology Sector | 186.2191168947 | 177.52 | -0.046714413856978054 | 60 |
| MOMENTUM | US Momentum Equities | 326.05 | 303.41 | -0.06943720288299338 | 61 |
| SOUTH_AFRICA | South Africa Equities | 68.04 | 62.94 | -0.0749559082892417 | 62 |
| SEMICONDUCTORS | Semiconductors | 616.0 | 568.92 | -0.07642857142857151 | 63 |
| GOLD | Gold | 81.5 | 74.8 | -0.0822085889570553 | 64 |
| BROAD_AI_TECH | Broad AI Technology | 64.6395450471 | 59.31 | -0.08245022521765266 | 65 |
| SOLAR | Solar Energy | 60.58 | 54.18 | -0.10564542753383954 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 132.35 | 118.14 | -0.10736683037400829 | 67 |
| METALS_MINING | Metals and Mining | 119.2470331677 | 98.99 | -0.16987452542498094 | 68 |
| SILVER | Silver | 63.39 | 50.39 | -0.20507966556239154 | 69 |
| SOUTH_KOREA | South Korea Equities | 205.91 | 163.36 | -0.20664367927735405 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.07642857142857151 | -0.022928571428571454 | Strong momentum, AI capex cycle, semis leadership continues. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | -0.0360303941215766 | -0.007206078824315321 | Defense budgets and geopolitical risk supportive; strong trend. |
| anthropic-claude-opus-4-7 | MOMENTUM | 20.0 | -0.06943720288299338 | -0.013887440576598676 | Momentum factor leading; trend persistence into July. |
| anthropic-claude-opus-4-7 | FINANCIALS | 15.0 | 0.04779592929212617 | 0.007169389393818925 | Steep curve, strong recent breadth, supportive of banks. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | -0.0822085889570553 | -0.012331288343558294 | Hedge against sticky inflation, weaker dollar, FOMC dovish risk. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.07642857142857151 | -0.022928571428571454 | Strongest momentum across timeframes with AI capex tailwinds; semis leading the tech rally with broad supply-chain demand. |
| anthropic-claude-opus-4-8 | MOMENTUM | 25.0 | -0.06943720288299338 | -0.017359300720748344 | Persistent factor leadership (9.4% 30d) captures trending winners while diversifying single-sector risk. |
| anthropic-claude-opus-4-8 | SOUTH_KOREA | 15.0 | -0.20664367927735405 | -0.030996551891603108 | Semiconductor-driven export momentum extremely strong; benefits from same AI/chip cycle with country diversification. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 15.0 | 0.004114892654232261 | 0.0006172338981348391 | Solid cyclical breadth (ITA/defense strong), steady output, benefits from broad market participation outside mega-cap. |
| anthropic-claude-opus-4-8 | GOLD | 15.0 | -0.0822085889570553 | -0.012331288343558294 | Hedge against sticky CPI (4.2% YoY) and FOMC surprise risk; safe-haven ballast with positive 1y trend. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | -0.07642857142857151 | -0.022928571428571454 | Semiconductors have shown exceptional momentum and strength, making them a prime candidate for continued outperformance over a one-month horizon. |
| google-gemini-3-1-pro | SOUTH_KOREA | 20.0 | -0.20664367927735405 | -0.04132873585547081 | South Korean equities are exhibiting massive momentum, likely driven by semiconductor and export strength, which should persist in the short term. |
| google-gemini-3-1-pro | TECHNOLOGY | 20.0 | -0.046714413856978054 | -0.00934288277139561 | Broad technology exposure captures the ongoing AI and growth themes that are currently leading market returns. |
| google-gemini-3-1-pro | MOMENTUM | 20.0 | -0.06943720288299338 | -0.013887440576598676 | A momentum factor allocation systematically captures the current market leaders, providing diversified exposure to the strongest trends. |
| google-gemini-3-1-pro | SP500 | 10.0 | 0.003070197677929709 | 0.0003070197677929709 | A baseline allocation to the broad market provides stability and benchmark tracking while the rest of the portfolio seeks alpha. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.07642857142857151 | -0.026750000000000027 | Strongest AI-linked leadership with very high 30-day, 6-month, and 1-year momentum; likely to benefit if risk appetite and earnings optimism persist over the month. |
| openai-gpt-5-5 | SOUTH_KOREA | 25.0 | -0.20664367927735405 | -0.05166091981933851 | Exceptional recent and longer-term momentum with heavy semiconductor/export sensitivity, offering high beta to the same AI and global electronics cycle. |
| openai-gpt-5-5 | TAIWAN | 20.0 | -0.03497446767511325 | -0.006994893535022651 | Semiconductor supply-chain exposure with strong 30-day and 6-month performance, providing concentrated participation in AI hardware demand. |
| openai-gpt-5-5 | MOMENTUM | 10.0 | -0.06943720288299338 | -0.006943720288299338 | Captures cross-sector trend persistence in recent market leaders while diversifying beyond a single industry or country. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 10.0 | -0.0360303941215766 | -0.0036030394121576606 | Strong 30-day performance and potential support from defense spending and geopolitical demand, with somewhat different drivers than AI semiconductors. |
| xai-grok-4-3 | SEMICONDUCTORS | 35.0 | -0.07642857142857151 | -0.026750000000000027 | Strong 30-day momentum and AI supply-chain exposure likely to benefit from continued tech spending before July CPI. |
| xai-grok-4-3 | SMALL_CAP | 25.0 | 0.01201725554642552 | 0.00300431388660638 | Recent outperformance and domestic growth sensitivity position it well for post-FOMC risk appetite. |
| xai-grok-4-3 | MOMENTUM | 20.0 | -0.06943720288299338 | -0.013887440576598676 | Factor has shown persistence in the latest 30-day window and should capture near-term trend continuation. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 20.0 | -0.0360303941215766 | -0.007206078824315321 | Robust 30-day returns and stable defense spending provide defensive growth through the one-month window. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SEMICONDUCTORS | 4 | 0.65 | -0.07642857142857151 | -0.044839205514307645 | -0.047909403192237354 | 0.16899989037471674 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.07642857142857151 | -0.04918398977922482 | -0.05225418745715453 | 0.17334467463963393 |  | False | False |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.62 | -0.07642857142857151 | -0.08299847848634635 | -0.08606867616427606 | 0.20715916334675544 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 5 | 0.75 | -0.07642857142857151 | -0.08718061086424357 | -0.09025080854217328 | 0.21134129572465266 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.63 | -0.07642857142857151 | -0.09595257305481819 | -0.0990227707327479 | 0.2201132579152273 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 72d6c03ef8c005ec2f76ba6634b90d88f3f3dc44950d2166e588a13e100b1fcc |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | 08ec9b4e20928d36c42103a764324c2f10ff80ea9a8a2c945bf71d42d42c742d |
| market_data/universe_trailing_returns.csv | 16bc494a75b84d92ae46d22af32635d0fdf971c6a180a7e66af662f61ae629bb |
| market_data/universe_trailing_returns.md | 3d88959b88dfb7a5a84279b7432fe392eaab70ef4a324f4d2e8efbb113de392b |
| market_data/universe_trailing_returns.json | d5301071d940e891606b26fc563b881db024cec206cf91695331aee082cbc2da |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | f5e89f195d1c85b6e102b873449ae7d6bfc3ea49c2dd78a9fb14e658256a48e1 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 1b6868d216aa6785c406ee597853c1b6f6763c574484a288b4cdbba3c97fdd27 | yes |
| Final briefing | research/final_briefing.md | model-facing | 72d6c03ef8c005ec2f76ba6634b90d88f3f3dc44950d2166e588a13e100b1fcc | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
