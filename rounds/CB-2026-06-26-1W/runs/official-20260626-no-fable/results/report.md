# CapitalBench Report: CB-2026-06-26-1W / official-20260626-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260626-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-26-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-26
- Decision deadline: 2026-06-27T03:30:00Z
- Horizon: one week
- Entry date: 2026-06-26
- Exit date: 2026-07-02
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | HEALTHCARE | 4 | 0.55 | Focus on sectors with positive June 26 momentum and lower sensitivity to tech/AI weakness and geopolitical oil moves over the one-week window. | Employment report surprise on July 2 could trigger broad equity volatility before close; Geopolitical escalation from Iran strike may increase risk-off flows; Reversal in recent healthcare and biotech gains if momentum fades; Tech sector stabilization could reduce relative outperformance of defensive holdings |
| google-gemini-3-1-pro | google | portfolio | HEALTHCARE | 3 | 0.65 | Overweighting healthcare and biotech based on positive regulatory news, while adding regional banks for diversification away from tech. | The positive momentum in healthcare and biotech from the EMA news may fade quickly or be overshadowed by broader market weakness.; Regional banks remain sensitive to interest rates and any unexpected shifts in Fed policy expectations could negatively impact the sector.; The portfolio is highly concentrated in just three sectors, increasing vulnerability to sector-specific shocks. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Overweight healthcare and biotech on EMA catalyst, regional banks on curve steepening, low-vol for stability, and long duration as hedge into NFP. | Hot June payrolls on exit day could spike yields and hurt rate-sensitive holdings; Healthcare/biotech reversal after sharp 30d rally; Geopolitical escalation from Iran strikes could shift risk appetite unpredictably; AI/tech rebound could leave defensive portfolio lagging SPY |
| openai-gpt-5-5 | openai | portfolio | BIOTECH | 5 | 0.57 | Positioning emphasizes one-week alpha versus SPY by favoring non-mega-cap leadership and healthcare-specific catalysts while avoiding recent AI-linked drag. The allocation remains equity-risk seeking but diversified across biotech, banks, small value, healthcare, and oil. | Biotech and healthcare may reverse after sharp recent gains if the EMA-related catalyst is fully priced or risk appetite weakens.; The July 2 Employment Situation release could surprise in a way that pressures small caps and regional banks through rate or credit-spread moves.; AI and mega-cap technology could rebound sharply after the recent selloff, causing this underweight to lag the S&P 500.; Oil could continue falling despite geopolitical tension if markets focus on demand concerns, refinery/product builds, or de-escalation in the Strait of Hormuz. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Favor catalyst-supported healthcare and breadth-positive non-mega-cap exposure over AI-heavy indexes, with defensive cushioning. | A sharp rebound in semiconductors/AI mega-caps could cause the S&P 500 benchmark to outrun this defensively tilted portfolio.; July 2 jobs report surprise could whipsaw regional banks and mid-caps on rate repricing.; Healthcare rally could mean-revert after sharp 7d/30d gains if EMA optimism fades.; Strait of Hormuz escalation could spike volatility and pressure cyclical holdings. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 11.890000343322754 | 12.86 | 0.08158112940862794 | 1 |
| CYBERSECURITY | Cybersecurity | 85.36000061035156 | 90.66999816894531 | 0.062207093728040785 | 2 |
| SOFTWARE | Software | 88.19999694824219 | 93.56999969482422 | 0.06088438698850829 | 3 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.77999877929688 | 248.19000244140625 | 0.048188207284960205 | 4 |
| FINANCIALS | Financials Sector | 53.56999969482422 | 55.619998931884766 | 0.03826767311440937 | 5 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.5999984741211 | 127.94000244140625 | 0.0351133011396747 | 6 |
| BIOTECH | Biotechnology | 155.3800048828125 | 160.4600067138672 | 0.03269405117399771 | 7 |
| SILVER | Silver | 53.279998779296875 | 55.02 | 0.03265768131697566 | 8 |
| COMMUNICATIONS | Communication Services Sector | 106.18000030517578 | 109.5999984741211 | 0.03220943830397216 | 9 |
| UNITED_KINGDOM | United Kingdom Equities | 45.7599983215332 | 47.16 | 0.030594443396384507 | 10 |
| BITCOIN_ETF | Bitcoin ETF | 33.849998474121094 | 34.87 | 0.030132985874688156 | 11 |
| EUROPE | Europe Equities | 87.12999725341797 | 89.3499984741211 | 0.025479183871040867 | 12 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.37000274658203 | 117.12000274658203 | 0.024044766406916773 | 13 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 210.30999755859375 | 214.91000366210938 | 0.021872503242429175 | 14 |
| SP500 | S&P 500 | 728.989990234375 | 744.780029296875 | 0.02166015895146023 | 15 |
| HEALTHCARE | Healthcare Sector | 160.33999633789062 | 163.74000549316406 | 0.02120499708699297 | 16 |
| TAIWAN | Taiwan Equities | 102.80999755859375 | 104.86 | 0.01993971880252121 | 17 |
| TOTAL_US_MARKET | Total US Stock Market | 362.2200012207031 | 368.760009765625 | 0.018055349022366718 | 18 |
| LARGE_GROWTH | US Large-Cap Growth | 119.04000091552734 | 121.16000366210938 | 0.017809162720743066 | 19 |
| LARGE_VALUE | US Large-Cap Value | 242.75999450683594 | 246.80999755859375 | 0.01668315679436949 | 20 |
| SOUTH_AFRICA | South Africa Equities | 63.0099983215332 | 64.0 | 0.015711818835717484 | 21 |
| INDUSTRIALS | Industrials Sector | 181.1999969482422 | 183.91000366210938 | 0.014955887193757844 | 22 |
| LOW_VOL | US Low Volatility Equities | 75.76000213623047 | 76.7300033569336 | 0.012803606036848825 | 23 |
| GOLD | Gold | 76.55999755859375 | 77.51000213623047 | 0.012408628630240726 | 24 |
| DIVIDEND | US Dividend Equities | 32.09000015258789 | 32.38999938964844 | 0.009348682942787567 | 25 |
| NASDAQ100 | Nasdaq 100 | 706.52001953125 | 712.5999755859375 | 0.00860549720688919 | 26 |
| CHINA | China Equities | 50.47999954223633 | 50.90999984741211 | 0.008518231162343959 | 27 |
| MATERIALS | Materials Sector | 51.599998474121094 | 52.0099983215332 | 0.007945733711944403 | 28 |
| EMERGING_MARKETS | Emerging Markets | 58.58000183105469 | 59.040000915527344 | 0.007852493514754366 | 29 |
| AUSTRALIA | Australia Equities | 27.969999313354492 | 28.09 | 0.004290335702232584 | 30 |
| EURO | Euro | 105.02023315429688 | 105.47 | 0.004282668512479049 | 31 |
| YEN | Japanese Yen | 56.709999084472656 | 56.95 | 0.004232074050465995 | 32 |
| JAPAN | Japan Equities | 92.80000305175781 | 93.13999938964844 | 0.003663753520579016 | 33 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.55999755859375 | 70.80999755859375 | 0.0035430840228189986 | 34 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.70999908447266 | 84.98999786376953 | 0.0033053805019838123 | 35 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.4616470336914 | 79.70999908447266 | 0.0031254329610856946 | 36 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.31105041503906 | 107.5 | 0.0017607654032847364 | 37 |
| MEXICO | Mexico Equities | 75.37000274658203 | 75.5 | 0.0017247876964401332 | 38 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.36202239990234 | 91.44000244140625 | 0.00085352796988869 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.13958740234375 | 96.2 | 0.0006283841993561801 | 40 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 41 |
| INDIA | India Equities | 49.560001373291016 | 49.560001373291016 | 0.0 | 41 |
| BROAD_COMMODITIES | Broad Commodities | 15.869999885559082 | 15.869999885559082 | 0.0 | 41 |
| SMALL_VALUE | US Small-Cap Value | 221.42999267578125 | 221.3300018310547 | -0.0004515686584199985 | 44 |
| CANADA | Canada Equities | 57.79999923706055 | 57.77 | -0.0005190179490748292 | 45 |
| COPPER | Copper | 37.33000183105469 | 37.29 | -0.0010715732411620271 | 46 |
| MID_CAP | US Mid-Cap Stocks | 76.22000122070312 | 76.08999633789062 | -0.0017056531190029478 | 47 |
| REGIONAL_BANKS | Regional Banks | 75.16999816894531 | 75.0199966430664 | -0.0019954972666326176 | 48 |
| AGRICULTURE | Agriculture Commodities | 26.799999237060547 | 26.74 | -0.0022387775659925557 | 49 |
| TIPS | Treasury Inflation-Protected Securities | 108.63938903808594 | 108.33000183105469 | -0.002847836404186621 | 50 |
| TECHNOLOGY | Technology Sector | 181.11000061035156 | 180.58999633789062 | -0.0028712068395366774 | 51 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.3988151550293 | 48.24 | -0.0032813851851658526 | 52 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 99.0077896118164 | 98.61000061035156 | -0.004017754593092837 | 53 |
| US_DOLLAR | US Dollar | 28.459999084472656 | 28.34 | -0.00421641209883683 | 54 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.11650085449219 | 108.63999938964844 | -0.004366905656910447 | 55 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.59153747558594 | 94.13 | -0.0048792681449444375 | 56 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.71748352050781 | 94.12000274658203 | -0.006308030489391325 | 57 |
| BRAZIL | Brazil Equities | 34.66999816894531 | 34.43 | -0.006922358858394317 | 58 |
| SMALL_CAP | US Small-Cap Stocks | 299.8299865722656 | 297.5799865722656 | -0.0075042527457729324 | 59 |
| SOLAR | Solar Energy | 56.849998474121094 | 56.31999969482422 | -0.009322758021499955 | 60 |
| UTILITIES | Utilities Sector | 46.20000076293945 | 45.7599983215332 | -0.00952386221082513 | 61 |
| ENERGY | Energy Sector | 53.84000015258789 | 53.220001220703125 | -0.01151558191173152 | 62 |
| REAL_ESTATE | Real Estate Sector | 45.2400016784668 | 44.68000030517578 | -0.012378456067952848 | 63 |
| OIL | Crude Oil | 105.4800033569336 | 103.98 | -0.0142207367197148 | 64 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 87.03854370117188 | 85.51000213623047 | -0.01756166291326433 | 65 |
| BROAD_AI_TECH | Broad AI Technology | 63.150001525878906 | 61.849998474121094 | -0.020585954399780504 | 66 |
| METALS_MINING | Metals and Mining | 108.01000213623047 | 105.12999725341797 | -0.02666424243914023 | 67 |
| MOMENTUM | US Momentum Equities | 325.739990234375 | 316.5299987792969 | -0.028274058240289723 | 68 |
| SEMICONDUCTORS | Semiconductors | 611.6099853515625 | 592.2899780273438 | -0.031588770273450195 | 69 |
| SOUTH_KOREA | South Korea Equities | 197.27999877929688 | 180.14 | -0.08688158396874246 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 35.0 | 0.02120499708699297 | 0.00742174898044754 | Strong recent catalyst with EMA approvals supporting sector; defensive with low beta and positive momentum into a week with payrolls risk. |
| anthropic-claude-opus-4-7 | REGIONAL_BANKS | 20.0 | -0.0019954972666326176 | -0.00039909945332652355 | Steepening curve, falling 10y yield, strong breadth; at 52w highs with solid recent momentum supported by rate backdrop. |
| anthropic-claude-opus-4-7 | LOW_VOL | 20.0 | 0.012803606036848825 | 0.002560721207369765 | Defensive tilt ahead of jobs report and holiday-shortened week with AI/tech weakness weighing on cap-weighted indexes. |
| anthropic-claude-opus-4-7 | BIOTECH | 15.0 | 0.03269405117399771 | 0.004904107676099656 | EMA approval catalyst plus strong 30d momentum; biotech leadership in healthcare rally. |
| anthropic-claude-opus-4-7 | LONG_TREASURY | 10.0 | -0.01756166291326433 | -0.0017561662913264332 | 10y yield declining, softening sentiment data and tech weakness support duration into payrolls. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.02120499708699297 | 0.006361499126097891 | Healthcare led the market on June 26 (+7.8% 7d) on EMA approval news; defensive low-beta with positive catalyst momentum and at 52w high, supported by the briefing's EMA committee recommendation fact. |
| anthropic-claude-opus-4-8 | REGIONAL_BANKS | 20.0 | -0.0019954972666326176 | -0.00039909945332652355 | KRE strong (+5.4% 7d, at 52w high) amid steepening curve and benign claims; positioning supported by improving macro and rate context, not price alone. |
| anthropic-claude-opus-4-8 | LOW_VOL | 20.0 | 0.012803606036848825 | 0.002560721207369765 | Defensive low-beta factor (+3.85% 7d) cushions against AI/tech-led index drawdown into the July 2 jobs report week. |
| anthropic-claude-opus-4-8 | MID_CAP | 15.0 | -0.0017056531190029478 | -0.00025584796785044217 | Mid caps showed broad-based strength (+0.58% 7d, near 52w high) with healthier breadth than mega-cap indexes; benefits from solid macro data. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.00085352796988869 | 0.0001280291954833035 | Cash-like buffer ahead of July 2 jobs report and holiday-shortened week to limit volatility exposure. |
| google-gemini-3-1-pro | HEALTHCARE | 40.0 | 0.02120499708699297 | 0.008481998834797189 | Healthcare stocks were among the strongest upward forces on the market after a European Medicines Agency committee recommended several medicines for approval or indication extensions, providing a near-term catalyst. |
| google-gemini-3-1-pro | BIOTECH | 30.0 | 0.03269405117399771 | 0.009808215352199312 | Biotech benefits from the same European Medicines Agency recommendations as the broader healthcare sector, and has shown strong recent momentum with a 10.53% 7-day return. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 30.0 | -0.0019954972666326176 | -0.0005986491799897853 | Regional banks have shown recent strength with a 5.42% 7-day return and 8.67% 30-day return, offering diversification away from tech and AI which are currently facing headwinds. |
| openai-gpt-5-5 | BIOTECH | 35.0 | 0.03269405117399771 | 0.011442917910899197 | Healthcare and biotech had strong recent relative performance, with independent support from reported healthcare strength after European Medicines Agency committee recommendations; high volatility is accepted for the one-week alpha objective. |
| openai-gpt-5-5 | REGIONAL_BANKS | 25.0 | -0.0019954972666326176 | -0.0004988743166581544 | Regional banks benefit from the current rotation toward smaller and value-oriented domestic equities, while firm claims, improved sentiment, and solid income/spending data support credit and growth expectations into the jobs release. |
| openai-gpt-5-5 | SMALL_VALUE | 20.0 | -0.0004515686584199985 | -9.03137316839997e-05 | Small value captures the broadening market breadth noted on June 26 and has less direct exposure to AI-linked mega-cap weakness that weighed on cap-weighted indexes. |
| openai-gpt-5-5 | HEALTHCARE | 10.0 | 0.02120499708699297 | 0.0021204997086992972 | Healthcare was among the strongest upward forces on the market with a near-term regulatory approval catalyst, offering defensive beta and sector-specific support. |
| openai-gpt-5-5 | OIL | 10.0 | -0.0142207367197148 | -0.00142207367197148 | Crude has a near-term geopolitical catalyst from U.S. strikes on Iran after a Strait of Hormuz cargo-ship drone attack, alongside low U.S. crude inventories, though recent price action has been weak. |
| xai-grok-4-3 | HEALTHCARE | 35.0 | 0.02120499708699297 | 0.00742174898044754 | Healthcare led market gains on June 26 with EMA approvals providing near-term catalyst support before exit close. |
| xai-grok-4-3 | BIOTECH | 25.0 | 0.03269405117399771 | 0.008173512793499427 | Biotech posted the strongest 7-day return in the data set amid favorable regulatory news flow. |
| xai-grok-4-3 | LOW_VOL | 25.0 | 0.012803606036848825 | 0.003200901509212206 | Low-volatility equities delivered positive recent performance with defensive characteristics ahead of employment data. |
| xai-grok-4-3 | SMALL_VALUE | 15.0 | -0.0004515686584199985 | -6.773529876299977e-05 | Small-value equities showed recent outperformance versus broad market with domestic growth sensitivity. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | HEALTHCARE | 4 | 0.55 | 0.02120499708699297 | 0.018728427984396175 | -0.0029317309670640543 | 0.06285270142423177 |  | False | True |
| google-gemini-3-1-pro | HEALTHCARE | 3 | 0.65 | 0.02120499708699297 | 0.017691565007006714 | -0.003968593944453515 | 0.06388956440162122 |  | False | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.02120499708699297 | 0.012731312119264005 | -0.008928846832196224 | 0.06884981728936393 |  | False | True |
| openai-gpt-5-5 | BIOTECH | 5 | 0.57 | 0.03269405117399771 | 0.01155215589928486 | -0.010108003052175369 | 0.07002897350934308 |  | False | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.02120499708699297 | 0.008395302107773993 | -0.013264856843686236 | 0.07318582730085395 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 1c9ea285a309fc37909ee033f834dd0ec72df267f2f661e2a332c29432fe5bb5 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | b14f6fc43eb97f71ba08d7904eff2288e3ac1de3218ed335f702fc37394220eb |
| market_data/universe_trailing_returns.csv | a2358b5038eabbc4632abf8ebfb758ea08dd3c6ee8321189d1eda3d73d4fdc95 |
| market_data/universe_trailing_returns.md | 95fb16347d221c8413bcfc8147edae69c474ee549438610e0bbdb0ecbc3185c8 |
| market_data/universe_trailing_returns.json | 18b95a3185c923fd10cd58f5cdd26a1a2a2762d4ab173f949fc23a6fae1e566b |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 323cf0a0134355cc5a58a844e8473570cc2375f1c4bb7a894c5997f403a6de79 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | d808f67f0f680bf0baec85b279dffa5d3884ddd51abea33252648f64f41c3a5a | yes |
| Final briefing | research/final_briefing.md | model-facing | 1c9ea285a309fc37909ee033f834dd0ec72df267f2f661e2a332c29432fe5bb5 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
