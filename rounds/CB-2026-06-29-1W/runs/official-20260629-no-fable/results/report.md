# CapitalBench Report: CB-2026-06-29-1W / official-20260629-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260629-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-29-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-29
- Decision deadline: 2026-06-30T03:30:00Z
- Horizon: one week
- Entry date: 2026-06-29
- Exit date: 2026-07-06
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Overweight healthcare/biotech momentum with fundamental sector breadth, add semis on Micron catalyst and industrials on PMI strength, balanced by low-vol defensiveness ahead of key labor data. | July 2 jobs report or ISM/JOLTS surprises could trigger a broad risk-off move hurting cyclicals and semis before exit close; Semiconductor and biotech high volatility and recent SMH 7d pullback (-5.5%) raise reversal risk if AI sentiment fades; Healthcare/biotech at 52-week highs are vulnerable to mean reversion after sharp run-up; Holiday-shortened week (July 3 closed) thins liquidity and can amplify gaps |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.6 | Mix sector leadership (XLV), broadening (RSP, IJH), a Micron-driven semi catalyst (SMH), and Treasury hedge (TLT) to capture upside while limiting concentration in volatile mega-cap tech ahead of payrolls. | Hot June payrolls or JOLTS could spike yields and hurt duration plus rate-sensitive equities; Semiconductor reversal continues after recent -5.5% week despite Micron catalyst; Healthcare/biotech momentum reverses after sharp 7-8% 30d gains; Geopolitical re-escalation (Iran) disrupts risk appetite over holiday-shortened week |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.65 | Overweighting semiconductors and communications based on strong corporate earnings and index inclusion catalysts, balanced with broad market exposure. | Semiconductor reversal if the recent AI-linked stock rebound fails to hold.; Broader market selloff due to elevated inflation data and lengthening supplier delivery times.; Tech sector volatility ahead of the July 4th holiday shortened week and upcoming employment data. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.57 | Semiconductors offer the clearest near-term catalyst, while biotech, regional banks, Nasdaq exposure, and healthcare add complementary upside if macro data support continued risk appetite. The main bet is that June 29's rebound persists through the July 6 close rather than reversing after large year-to-date gains. | Semiconductor and AI-linked stocks have very high beta and large prior gains, so profit-taking or a factor reversal could overwhelm Micron-related optimism.; This week's JOLTS, consumer confidence, ISM, ADP, and employment reports could reprice growth, inflation, or Fed expectations and pressure cyclicals and high-duration equities.; Treasury yields were already inching higher with inflation still elevated; a further rate backup could hurt Nasdaq, biotech, and other growth-oriented holdings.; Regional banks could underperform if labor or credit data revive concerns about loan quality, deposits, commercial real estate, or net interest margins.; The holiday-shortened week may amplify liquidity-driven moves and make recent momentum signals less reliable. |
| xai-grok-4-3 | xai | portfolio | NASDAQ100 | 3 | 0.65 | Micron-driven semiconductor strength and Nasdaq rebound combined with positive PMI and income data favor concentrated equity tilt in high-conviction areas for the short scoring horizon. | Weaker-than-expected June employment data on July 2 could pressure risk assets; Profit-taking after the June 29 rebound may limit follow-through gains in tech; Holiday-shortened week reduces liquidity and amplifies any negative surprises |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 12.239999771118164 | 13.55 | 0.10702616449168145 | 1 |
| SILVER | Silver | 52.68000030517578 | 56.11 | 0.0651100925389938 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 34.18000030517578 | 36.12 | 0.056758328774223266 | 3 |
| SOFTWARE | Software | 89.88999938964844 | 94.79000091552734 | 0.05451108642952307 | 4 |
| CYBERSECURITY | Cybersecurity | 88.5 | 92.91000366210938 | 0.04983054985434321 | 5 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.1300048828125 | 250.78 | 0.0487182489830027 | 6 |
| FINANCIALS | Financials Sector | 53.720001220703125 | 56.13999938964844 | 0.04504836399766621 | 7 |
| AGRICULTURE | Agriculture Commodities | 26.510000228881836 | 27.54 | 0.038853253950409616 | 8 |
| GOLD | Gold | 75.52999877929688 | 78.30000305175781 | 0.036674226363422324 | 9 |
| MATERIALS | Materials Sector | 50.65999984741211 | 51.97999954223633 | 0.026056054062377765 | 10 |
| CHINA | China Equities | 50.790000915527344 | 52.02000045776367 | 0.024217356173748206 | 11 |
| UNITED_KINGDOM | United Kingdom Equities | 46.150001525878906 | 47.22 | 0.023185231608737533 | 12 |
| JAPAN | Japan Equities | 93.20999908447266 | 95.2699966430664 | 0.022100607003834982 | 13 |
| COMMUNICATIONS | Communication Services Sector | 107.87999725341797 | 110.20999908447266 | 0.021598089454723857 | 14 |
| EUROPE | Europe Equities | 88.06999969482422 | 89.97000122070312 | 0.02157376555538426 | 15 |
| SOUTH_AFRICA | South Africa Equities | 63.41999816894531 | 64.63 | 0.01907918426347699 | 16 |
| LARGE_VALUE | US Large-Cap Value | 242.75 | 247.24000549316406 | 0.01849641809748337 | 17 |
| BROAD_COMMODITIES | Broad Commodities | 15.84000015258789 | 16.100000381469727 | 0.016414155705633426 | 18 |
| COPPER | Copper | 37.22999954223633 | 37.84 | 0.016384648543217084 | 19 |
| BIOTECH | Biotechnology | 158.30999755859375 | 160.80999755859375 | 0.015791801140510486 | 20 |
| INDUSTRIALS | Industrials Sector | 182.75999450683594 | 185.55999755859375 | 0.015320656248176245 | 21 |
| EMERGING_MARKETS | Emerging Markets | 59.18000030517578 | 60.06999969482422 | 0.015038854090215326 | 22 |
| INDIA | India Equities | 49.18000030517578 | 49.880001068115234 | 0.01423344364773782 | 23 |
| TAIWAN | Taiwan Equities | 105.79000091552734 | 107.27 | 0.013989971374084975 | 24 |
| SP500 | S&P 500 | 741.0 | 751.280029296875 | 0.013873183936403466 | 25 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.91999816894531 | 71.88999938964844 | 0.013677400532250417 | 26 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 128.38999938964844 | 130.11000061035156 | 0.013396691556038842 | 27 |
| TOTAL_US_MARKET | Total US Stock Market | 367.1199951171875 | 371.6700134277344 | 0.012393817746414237 | 28 |
| REGIONAL_BANKS | Regional Banks | 74.75 | 75.56 | 0.010836120401337856 | 29 |
| BRAZIL | Brazil Equities | 34.54999923706055 | 34.92 | 0.010709139540083346 | 30 |
| CANADA | Canada Equities | 57.4900016784668 | 58.06 | 0.009914738300428771 | 31 |
| DIVIDEND | US Dividend Equities | 31.93000030517578 | 32.2400016784668 | 0.009708780780711912 | 32 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.0500030517578 | 215.0 | 0.00915276658207076 | 33 |
| LARGE_GROWTH | US Large-Cap Growth | 121.9800033569336 | 123.0 | 0.008361998811245552 | 34 |
| AUSTRALIA | Australia Equities | 28.110000610351562 | 28.33 | 0.007826374417345905 | 35 |
| LOW_VOL | US Low Volatility Equities | 75.58999633789062 | 76.16999816894531 | 0.007672997210663279 | 36 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.12000274658203 | 118.01000213623047 | 0.007599038326306928 | 37 |
| HEALTHCARE | Healthcare Sector | 160.74000549316406 | 161.9600067138672 | 0.007589904062526687 | 38 |
| MEXICO | Mexico Equities | 76.12000274658203 | 76.43 | 0.004072480849087956 | 39 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.64081573486328 | 79.87000274658203 | 0.0028777582148549197 | 40 |
| SMALL_VALUE | US Small-Cap Value | 221.27999877929688 | 221.74000549316406 | 0.0020788445246060494 | 41 |
| EURO | Euro | 105.37998962402344 | 105.57 | 0.0018030973114959714 | 42 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.42076110839844 | 107.57 | 0.0013892928151100215 | 43 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.37200164794922 | 91.43000030517578 | 0.0006347530554275949 | 44 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 45 |
| SMALL_CAP | US Small-Cap Stocks | 298.9700012207031 | 298.8999938964844 | -0.00023416170161860705 | 46 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.41842651367188 | 96.35 | -0.0007096829532079463 | 47 |
| SOLAR | Solar Energy | 57.599998474121094 | 57.540000915527344 | -0.0010416243087351118 | 48 |
| YEN | Japanese Yen | 56.65999984741211 | 56.59 | -0.0012354367737490435 | 49 |
| MID_CAP | US Mid-Cap Stocks | 76.52999877929688 | 76.41999816894531 | -0.001437352830342964 | 50 |
| NASDAQ100 | Nasdaq 100 | 724.0800170898438 | 722.8200073242188 | -0.0017401526570075543 | 51 |
| US_DOLLAR | US Dollar | 28.3700008392334 | 28.32 | -0.0017624546265170293 | 52 |
| TIPS | Treasury Inflation-Protected Securities | 108.83745574951172 | 108.48999786376953 | -0.0031924477042338806 | 53 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.37000274658203 | 84.0999984741211 | -0.0032002401762618593 | 54 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.63140106201172 | 94.28 | -0.0037133663674856487 | 55 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 99.0376968383789 | 98.66000366210938 | -0.0038136304490793416 | 56 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.40879440307617 | 48.22 | -0.003900002167047889 | 57 |
| METALS_MINING | Metals and Mining | 106.5199966430664 | 106.08000183105469 | -0.00413063111038281 | 58 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.3157958984375 | 108.66999816894531 | -0.005907634154648456 | 59 |
| BROAD_AI_TECH | Broad AI Technology | 64.22000122070312 | 63.84000015258789 | -0.005917176282966619 | 60 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.74738311767578 | 94.18000030517578 | -0.00598837449468459 | 61 |
| ENERGY | Energy Sector | 53.58000183105469 | 53.130001068115234 | -0.008398670167245825 | 62 |
| TECHNOLOGY | Technology Sector | 185.41000366210938 | 183.57000732421875 | -0.0099239323744571 | 63 |
| REAL_ESTATE | Real Estate Sector | 44.91999816894531 | 44.290000915527344 | -0.014024872642437125 | 64 |
| UTILITIES | Utilities Sector | 46.02000045776367 | 45.29999923706055 | -0.01564539794744091 | 65 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 87.12820434570312 | 85.44999694824219 | -0.019261356412238473 | 66 |
| OIL | Crude Oil | 107.08000183105469 | 104.35 | -0.02549497370537912 | 67 |
| SOUTH_KOREA | South Korea Equities | 197.5 | 189.85 | -0.0387341772151899 | 68 |
| MOMENTUM | US Momentum Equities | 336.0 | 321.7099914550781 | -0.04252978733607704 | 69 |
| SEMICONDUCTORS | Semiconductors | 631.97998046875 | 604.2999877929688 | -0.04379884415840285 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.007589904062526687 | 0.002276971218758006 | Strong recent leadership with defensive characteristics; XBI biotech strength and sector breadth ahead of holiday-shortened week. |
| anthropic-claude-opus-4-7 | MID_CAP | 20.0 | -0.001437352830342964 | -0.0002874705660685928 | Mid-caps near 52w highs with solid macro (Q1 GDP revised up, claims falling, PMIs expanding) and lower vol than small caps. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 20.0 | 0.00915276658207076 | 0.001830553316414152 | Broad participation play after mega-cap AI volatility; benefits from broadening rally with lower concentration risk. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 15.0 | -0.04379884415840285 | -0.006569826623760427 | Micron blowout guide ($50B Q4, 86% GM) signals memory cycle still accelerating; HBM demand outpacing supply through 2027. |
| anthropic-claude-opus-4-7 | LONG_TREASURY | 15.0 | -0.019261356412238473 | -0.002889203461835771 | Hedge against equity reversal; benefits if payrolls/JOLTS soften and yields drift lower into July FOMC. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.007589904062526687 | 0.002276971218758006 | Strong recent breadth and leadership (+7.1% 7d, +9.8% vs SPX 30d), low beta defensive sector at 52w high with positive momentum into a busy macro data week. |
| anthropic-claude-opus-4-8 | BIOTECH | 20.0 | 0.015791801140510486 | 0.0031583602281020974 | Best recent performer (+8.5% 7d, +17.7% vs SPX 30d) with high up-day share; healthcare/biotech rotation supported by independent sector strength, not price alone. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 15.0 | 0.015320656248176245 | 0.0022980984372264366 | Solid breadth (+5.8% 30d), supported by improving flash PMI manufacturing output at 59-month high; cyclical participation with moderate beta. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 15.0 | -0.04379884415840285 | -0.006569826623760427 | Micron blowout guidance ($50B revenue, ~86% GM) signals memory demand exceeding supply; near-term AI chip catalyst despite high volatility. |
| anthropic-claude-opus-4-8 | LOW_VOL | 20.0 | 0.007672997210663279 | 0.001534599442132656 | Defensive ballast (+3.2% 7d, beta 0.07) ahead of JOLTS, ISM, and the July 2 jobs report which fall inside the scoring window. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 50.0 | -0.04379884415840285 | -0.021899422079201425 | Micron's strong earnings, positive guidance, and commentary on memory demand exceeding supply provide a clear near-term catalyst for the semiconductor sector. |
| google-gemini-3-1-pro | COMMUNICATIONS | 25.0 | 0.021598089454723857 | 0.005399522363680964 | Alphabet's inclusion in the Dow and the sector's reported strength during the June 29 session offer positive near-term sentiment. |
| google-gemini-3-1-pro | SP500 | 25.0 | 0.013873183936403466 | 0.0034682959841008665 | Provides diversified baseline exposure to the broader market while targeted sector bets play out. |
| openai-gpt-5-5 | SEMICONDUCTORS | 45.0 | -0.04379884415840285 | -0.01970947987128128 | Micron's exceptionally strong reported results, guidance, and comments that memory demand is running ahead of supply provide a near-term fundamental catalyst for AI-linked semiconductor sentiment, despite very high volatility and reversal risk after large prior gains. |
| openai-gpt-5-5 | BIOTECH | 20.0 | 0.015791801140510486 | 0.0031583602281020974 | Biotech has shown strong recent relative strength and healthcare is at a 52-week high in the supplied data; independent near-term support is limited, but the group can benefit from risk appetite while being less directly tied to rates than long-duration tech. |
| openai-gpt-5-5 | REGIONAL_BANKS | 15.0 | 0.010836120401337856 | 0.0016254180602006784 | Regional banks have recent relative strength with high up-day participation, and the solid macro and claims backdrop may support domestic cyclicals if this week's labor data avoid a growth scare. |
| openai-gpt-5-5 | NASDAQ100 | 10.0 | -0.0017401526570075543 | -0.00017401526570075544 | Nasdaq and AI-linked stocks rebounded on June 29 after a five-day losing streak, and large growth exposure should benefit if the risk-on bounce continues into the holiday-shortened week. |
| openai-gpt-5-5 | HEALTHCARE | 10.0 | 0.007589904062526687 | 0.0007589904062526687 | Healthcare has strong recent performance, lower beta than the S&P 500, and a 52-week-high position, offering participation in sector momentum with some ballast against a reversal in high-beta technology. |
| xai-grok-4-3 | NASDAQ100 | 40.0 | -0.0017401526570075543 | -0.0006960610628030218 | Rebound in AI-linked stocks and Nasdaq on June 29 after prior weakness, supported by strong Micron earnings and guidance indicating sustained memory demand. |
| xai-grok-4-3 | SEMICONDUCTORS | 35.0 | -0.04379884415840285 | -0.015329595455440997 | Micron fiscal Q3 results and Q4 guidance highlight demand exceeding supply through 2027, with HBM4 in high-volume production. |
| xai-grok-4-3 | SMALL_VALUE | 25.0 | 0.0020788445246060494 | 0.0005197111311515124 | Positive 7-day return amid solid macro data including upward GDP revision and strong flash PMI readings. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.007589904062526687 | 0.0026982027024587693 | -0.011174981233944697 | 0.10432796178922268 |  | False | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.6 | 0.007589904062526687 | -0.005638976116492633 | -0.019512160052896098 | 0.11266514060817409 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.65 | -0.04379884415840285 | -0.013031603731419594 | -0.02690478766782306 | 0.12005776822310105 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.57 | -0.04379884415840285 | -0.014340726442426593 | -0.02821391037883006 | 0.12136689093410805 |  | False | False |
| xai-grok-4-3 | NASDAQ100 | 3 | 0.65 | -0.0017401526570075543 | -0.015505945387092507 | -0.029379129323495973 | 0.12253210987877396 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 73765871e99df8b3698748a0947e5d669444b0b9ccaa2c481d82ab979927242e |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | a2801398a3d1e92f2c2887aa498452789a4885d075fbe8ad2acfed94fdc687ea |
| market_data/universe_trailing_returns.csv | c0937e790244709e8e76b1ac70bf45e07da98eef8d36b4849f6ddd7fda1cef3d |
| market_data/universe_trailing_returns.md | ecc7c68b2d5f32fdd96dc2de8c4c7c8c4528b2232c02ba17d9ea0117ad289d08 |
| market_data/universe_trailing_returns.json | 7da1345fbf9dd088b0d276a9211e6ee827a7f2f5456080c0e163254cfc297187 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 68ea14f7cdf7ce35eb687d4ec9be8a27bbecd2dc2b1155c78d0e438cff3e84ab | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 4707ce1223ffd1865d3864f299dfbe7baefaaff92c12f892dcf64bfa3945a86b | yes |
| Final briefing | research/final_briefing.md | model-facing | 73765871e99df8b3698748a0947e5d669444b0b9ccaa2c481d82ab979927242e | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
