# CapitalBench Report: CB-2026-08-11-1M / official-v2-2-all-monthly-20260811

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260811
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench Monthly Allocation — August 11, 2026
- Description: Pre-entry one-month portfolio allocation round using a newly researched August 11 briefing and market data through the August 10 close.
- Decision date: 2026-08-11
- Decision deadline: 2026-08-11T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-11
- Exit date: 2026-09-11
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | OIL | 4 | 0.58 | One-month alpha is sought via oil/energy continuation plus selective growth and defensive equity sleeves that clear the SPY base hurdle under the supplied macro and price context. | Rapid de-escalation on Strait of Hormuz could reverse oil and energy gains; Higher-than-expected July/August inflation or hawkish FOMC minutes could pressure equities and duration-sensitive growth; High volatility in oil and software could produce large adverse swings inside the scoring window; Cluster concentration in energy leaves portfolio exposed to commodity-specific shocks |
| google-gemini-3-1-pro | google | portfolio | GOLD | 3 | 0.65 | Defensive positioning with commodities and healthcare to navigate geopolitical and inflation risks. | A sudden resolution to geopolitical conflicts could lead to a sharp drop in oil and gold prices.; A stronger-than-expected US dollar could pressure commodity prices.; A broad market rally driven by technology could cause this defensive portfolio to underperform the S&P 500. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | SPY has solid earnings and activity support but sits near a 52-week high, so selected active positions need stronger one-month catalysts or cross-sectional evidence. Semiconductors, cybersecurity, oil, biotech, and metals/mining clear that hurdle on a base-case basis. | A softer July or August CPI and rapid easing of energy-supply concerns could reverse oil and commodity-linked holdings.; Hot inflation, hawkish FOMC minutes, or weak labor data could trigger broad equity risk-off and hit high-beta technology and biotech positions.; Recent winners such as oil, metals/mining, and cybersecurity may mean-revert sharply because several have elevated volatility or extended short-term moves.; Semiconductor exposure has very high beta, large drawdown, and could underperform if the recent pullback reflects deteriorating fundamentals rather than a temporary reset. |
| xai-grok-4-3 | xai | portfolio | SP500 | 3 | 0.55 | Energy and Japan bases exceed SPY forecast; allocations respect 50% cluster limit and 5% increments. | Oil supply resolution reverses energy gains; Higher-than-expected CPI triggers rate volatility; Labor market data weakens growth outlook |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 4 | 0.6 | Overweight energy equities and gold on the Hormuz-driven oil spike and elevated inflation, with a value tilt suited to 4.70% ten-year yields and a SPY core. | Rapid Strait of Hormuz reopening collapses crude and reverses energy/gold gains; Cool CPI prints and dovish Fed minutes lift growth stocks over value, hurting the tilts; Higher yields from inflation pressure could drag all equities including holdings; Gold's steep prior-year drawdown (-27% prior active) signals reversal fragility |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.53 | 40% SPY core plus energy, healthcare and Canada tilts backed by supplied crude, active-return and volatility data; expected alpha is modest and deliberately low-variance. | Rapid Hormuz reopening collapses crude and energy equities; Hot July/August CPI lifts the 10-year above 5% and compresses equity multiples; Weak August payrolls trigger a broad risk-off that hits cyclical tilts more than SPY; Healthcare policy headlines reverse the sector's recent relative strength |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 4 | 0.55 | Overweight defensive-quality equity sectors with strong relative trends and low drawdown while keeping SPY as core, aiming for modest alpha with reduced volatility. | Sharp risk-on rotation into mega-cap tech leaving defensives behind; CPI/PPI reacceleration lifting yields and pressuring equities; Labor market deterioration triggering broad equity drawdown |
| openai-gpt-5-6-sol | openai | portfolio | CYBERSECURITY | 2 | 0.56 | Cybersecurity and biotechnology have stronger one-month base cases than SPY based on supplied relative-trend and quality evidence. Their equal weighting respects the cluster cap and produces a 2.30% portfolio base forecast. | Hot CPI or PPI data could lift already-high Treasury yields and compress growth-equity valuations.; A sharp momentum-factor reversal could disproportionately hurt both selected holdings.; Weak employment or activity data could trigger broad risk aversion despite potentially lower rates.; The concentrated two-holding portfolio has substantially higher volatility than SPY. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.18 | 19.15999984741211 | 0.3511988608894294 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 35.94 | 43.77000045776367 | 0.21786311791217794 | 2 |
| OIL | Crude Oil | 127.61 | 154.9 | 0.2138547135804405 | 3 |
| SOUTH_KOREA | South Korea Equities | 167.24 | 188.72 | 0.12843817268596025 | 4 |
| BRAZIL | Brazil Equities | 33.98 | 38.19 | 0.12389640965273685 | 5 |
| BROAD_COMMODITIES | Broad Commodities | 17.91 | 19.79 | 0.10496929089893903 | 6 |
| ENERGY | Energy Sector | 60.93 | 65.14 | 0.06909568357131146 | 7 |
| TAIWAN | Taiwan Equities | 103.94 | 110.91 | 0.06705791802963246 | 8 |
| AGRICULTURE | Agriculture Commodities | 27.59 | 28.93 | 0.04856832185574489 | 9 |
| YEN | Japanese Yen | 57.63 | 59.68000030517578 | 0.03557175611965602 | 10 |
| JAPAN | Japan Equities | 96.28 | 98.56 | 0.023680930619027762 | 11 |
| SOUTH_AFRICA | South Africa Equities | 68.59 | 70.1 | 0.02201487097244481 | 12 |
| BROAD_AI_TECH | Broad AI Technology | 63.2 | 63.98 | 0.012341772151898578 | 13 |
| COMMUNICATIONS | Communication Services Sector | 111.27 | 112.6 | 0.011952907342500207 | 14 |
| TECHNOLOGY | Technology Sector | 186.09 | 187.67 | 0.008490515342038707 | 15 |
| EURO | Euro | 106.52 | 107.01000213623047 | 0.00460009515800297 | 16 |
| EMERGING_MARKETS | Emerging Markets | 60.12 | 60.35 | 0.003825681969394701 | 17 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.49 | 91.5 | 0.00010930156301247607 | 18 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 19 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.69 | 72.69 | 0.0 | 19 |
| US_DOLLAR | US Dollar | 28.14 | 28.06999969482422 | -0.0024875730339651847 | 21 |
| MOMENTUM | US Momentum Equities | 308.34 | 307.04 | -0.004216125056755393 | 22 |
| DIVIDEND | US Dividend Equities | 34.27 | 34.12 | -0.00437700612780878 | 23 |
| NASDAQ100 | Nasdaq 100 | 718.45 | 714.88 | -0.004969030551882581 | 24 |
| GOLD | Gold | 82.18 | 81.71 | -0.005719153078608041 | 25 |
| SILVER | Silver | 58.55 | 58.12 | -0.0073441502988897955 | 26 |
| UNITED_KINGDOM | United Kingdom Equities | 48.3 | 47.94 | -0.007453416149068359 | 27 |
| SEMICONDUCTORS | Semiconductors | 572.93 | 568.53 | -0.007679821269614084 | 28 |
| SP500 | S&P 500 | 770.56 | 764.29 | -0.00813693936877069 | 29 |
| LARGE_VALUE | US Large-Cap Value | 257.92 | 255.58 | -0.009072580645161255 | 30 |
| FINANCIALS | Financials Sector | 57.8 | 57.25 | -0.009515570934256035 | 31 |
| TIPS | Treasury Inflation-Protected Securities | 106.89 | 105.84 | -0.00982318271119842 | 32 |
| LARGE_GROWTH | US Large-Cap Growth | 123.6 | 122.27 | -0.01076051779935272 | 33 |
| MEXICO | Mexico Equities | 76.24 | 75.38 | -0.01128016789087094 | 34 |
| TOTAL_US_MARKET | Total US Stock Market | 380.65 | 376.31 | -0.011401549980296743 | 35 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.51 | 78.6 | -0.011445101245126543 | 36 |
| BIOTECH | Biotechnology | 158.07 | 156.2 | -0.011830201809325036 | 37 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.32 | 95.98 | -0.01376900945334969 | 38 |
| REAL_ESTATE | Real Estate Sector | 44.08 | 43.42 | -0.014972776769509921 | 39 |
| CANADA | Canada Equities | 61.51 | 60.58 | -0.01511949276540403 | 40 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.69 | 83.38 | -0.015468178061164295 | 41 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.83 | 93.34 | -0.015712327322577213 | 42 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.99 | 104.32 | -0.015756203415416614 | 43 |
| HEALTHCARE | Healthcare Sector | 168.01 | 165.36 | -0.01577287066246047 | 44 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.19 | 80.87 | -0.01606034797420608 | 45 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.82 | 46.99 | -0.017356754496026694 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.03 | 91.38 | -0.017736214124476013 | 47 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.87 | 91.01 | -0.02002799612361361 | 48 |
| AUSTRALIA | Australia Equities | 29.95 | 29.27 | -0.022704507512520844 | 49 |
| SOFTWARE | Software | 103.92 | 101.52 | -0.023094688221709014 | 50 |
| SMALL_VALUE | US Small-Cap Value | 224.97 | 219.69 | -0.023469795972796414 | 51 |
| LOW_VOL | US Low Volatility Equities | 75.65 | 73.79 | -0.024586913417052214 | 52 |
| EUROPE | Europe Equities | 92.3 | 90.02 | -0.02470205850487539 | 53 |
| COPPER | Copper | 40.22 | 39.18 | -0.02585778219791146 | 54 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.93 | 103.17 | -0.026054941942792453 | 55 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.69 | 214.87 | -0.026371833794009647 | 56 |
| UTILITIES | Utilities Sector | 43.63 | 42.39 | -0.02842081136832464 | 57 |
| INDIA | India Equities | 50.09 | 48.57 | -0.03034537831902584 | 58 |
| METALS_MINING | Metals and Mining | 117.83 | 113.63 | -0.03564457268946786 | 59 |
| REGIONAL_BANKS | Regional Banks | 76.81 | 73.9 | -0.037885691967191715 | 60 |
| SMALL_CAP | US Small-Cap Stocks | 300.99 | 288.89 | -0.040200671118641895 | 61 |
| MID_CAP | US Mid-Cap Stocks | 77.77 | 74.44 | -0.042818567571042854 | 62 |
| MATERIALS | Materials Sector | 53.24 | 50.95 | -0.04301277235161527 | 63 |
| CHINA | China Equities | 55.62 | 52.96 | -0.047824523552678855 | 64 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 119.24 | 112.96 | -0.05266689030526672 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 128.3 | 121.36 | -0.05409197194076387 | 66 |
| CYBERSECURITY | Cybersecurity | 99.92 | 94.4 | -0.055244195356285 | 67 |
| INDUSTRIALS | Industrials Sector | 185.7 | 172.37 | -0.07178244480344631 | 68 |
| SOLAR | Solar Energy | 52.7 | 47.15 | -0.10531309297912717 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 251.9 | 219.01 | -0.1305676855895197 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | 0.06909568357131146 | 0.020728705071393436 | Brent rose 5% Aug 10 to $87.72 and continued higher pre-cutoff with Strait of Hormuz reopening uncertain; energy equities lag the crude move (+6.86% active 21s vs USO +13.45%) and offer catch-up with negative SPY beta hedging value. |
| anthropic-claude-fable-5 | GOLD | 25.0 | -0.005719153078608041 | -0.0014297882696520103 | Gold at $4,425 with strong recent momentum (+8.3% 5s), sticky inflation (CPI 3.5% y/y, PPI 5.5% y/y) and rising geopolitical risk support safe-haven and inflation-hedge demand. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | -0.009072580645161255 | -0.001814516129032251 | Value at 52-week high with positive active return (+2.25% 21s), low volatility and shallow drawdown; energy/financial tilt benefits from higher oil and 4.70% 10-year yields while growth faces rate pressure. |
| anthropic-claude-fable-5 | SP500 | 25.0 | -0.00813693936877069 | -0.0020342348421926726 | Benchmark anchor: ~50% y/y Q2 earnings growth and solid ISM data support equities, but rising oil, 4.70% yields and hawkish FOMC dissent cap upside. |
| anthropic-claude-opus-4-8 | SP500 | 40.0 | -0.00813693936877069 | -0.0032547757475082763 | Core broad US large-cap exposure with strong Q2 earnings growth (~50% YoY) and cooling inflation supporting the tape. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | -0.01577287066246047 | -0.0039432176656151174 | Defensive sector with positive active return, low beta, shallow drawdown, and strong recent 5-day momentum (3.82%). |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | -0.009515570934256035 | -0.001903114186851207 | Positive active return, very shallow drawdown, low volatility, and stable credit backdrop with solid economy per Fed. |
| anthropic-claude-opus-4-8 | DIVIDEND | 15.0 | -0.00437700612780878 | -0.000656550919171317 | Best recent active return (3.13%) with low volatility and defensive profile suited to a mixed macro backdrop. |
| anthropic-claude-opus-5 | SP500 | 40.0 | -0.00813693936877069 | -0.0032547757475082763 | Core benchmark exposure with ~50% y/y Q2 earnings growth backdrop and low relative volatility. |
| anthropic-claude-opus-5 | ENERGY | 20.0 | 0.06909568357131146 | 0.013819136714262293 | Brent near $89 with Strait of Hormuz reopening uncertain; energy shows strong recent active return and negative SPY beta as a hedge. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | -0.01577287066246047 | -0.003154574132492094 | Positive 21-session active return, at 52-week high, low beta and shallow drawdown; defensive ballast if growth data soften. |
| anthropic-claude-opus-5 | CANADA | 20.0 | -0.01511949276540403 | -0.003023898553080806 | Energy/materials-levered developed market with low volatility (12.1%) and positive active return at 52-week high. |
| google-gemini-3-1-pro | GOLD | 40.0 | -0.005719153078608041 | -0.0022876612314432164 | Gold has shown strong recent momentum and acts as a hedge against geopolitical uncertainty and potential equity volatility. |
| google-gemini-3-1-pro | OIL | 30.0 | 0.2138547135804405 | 0.06415641407413215 | Oil prices are supported by supply concerns and recent price strength. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | -0.01577287066246047 | -0.004731861198738141 | Healthcare offers defensive growth characteristics and has shown positive recent returns. |
| openai-gpt-5-5 | SEMICONDUCTORS | 30.0 | -0.007679821269614084 | -0.002303946380884225 | Highest prior active rank and quality evidence among thematic growth candidates, with a large recent relative pullback that creates room for a one-month rebound if risk appetite persists. |
| openai-gpt-5-5 | CYBERSECURITY | 20.0 | -0.055244195356285 | -0.011048839071257 | Combines strong prior active return and recent positive active return with a new 52-week high, offering technology exposure with less extreme drawdown than semiconductors. |
| openai-gpt-5-5 | OIL | 20.0 | 0.2138547135804405 | 0.042770942716088105 | Supplied briefing identifies a sharp Brent/WTI rise and uncertainty around the Strait of Hormuz, matching very strong oil price momentum into the window. |
| openai-gpt-5-5 | BIOTECH | 15.0 | -0.011830201809325036 | -0.0017745302713987553 | High quality evidence score, strong prior active trend, and a recent pullback give an asymmetric rebound setup in a distinct healthcare/biotech cluster. |
| openai-gpt-5-5 | METALS_MINING | 15.0 | -0.03564457268946786 | -0.005346685903420178 | Recent 5-day and 21-day active strength is strong and can continue if commodity/inflation concern persists, but allocation is limited due to weak quality evidence and high volatility. |
| openai-gpt-5-6-sol | CYBERSECURITY | 50.0 | -0.055244195356285 | -0.0276220976781425 | Strong intermediate and recent benchmark-relative momentum provides the clearest continuation signal, although the position is capped for concentration control. |
| openai-gpt-5-6-sol | BIOTECH | 50.0 | -0.011830201809325036 | -0.005915100904662518 | High quality evidence, strong prior active performance, and a recent rebound support a one-month recovery trade distinct from the technology exposure. |
| xai-grok-4-3 | SP500 | 60.0 | -0.00813693936877069 | -0.004882163621262414 | Broad US equity exposure with solid earnings backdrop and neutral recent momentum. |
| xai-grok-4-3 | ENERGY | 25.0 | 0.06909568357131146 | 0.017273920892827865 | Oil price surge from supply disruption risk supports near-term outperformance. |
| xai-grok-4-3 | JAPAN | 15.0 | 0.023680930619027762 | 0.0035521395928541644 | Relative strength in recent returns and export exposure to global growth. |
| xai-grok-4-5 | OIL | 40.0 | 0.2138547135804405 | 0.08554188543217621 | Geopolitical supply risk and strong recent crude momentum support higher base return than SPY over the one-month window. |
| xai-grok-4-5 | ENERGY | 10.0 | 0.06909568357131146 | 0.006909568357131146 | Equity energy exposure captures oil upside with somewhat lower pure-commodity beta while still clearing the SPY base hurdle. |
| xai-grok-4-5 | SOFTWARE | 30.0 | -0.023094688221709014 | -0.006928406466512704 | Strong 5-session relative strength and solid earnings backdrop support a base case above SPY without exceeding the tech cluster cap. |
| xai-grok-4-5 | HEALTHCARE | 20.0 | -0.01577287066246047 | -0.003154574132492094 | Defensive sector near 52-week high with positive active 21s return offers diversification and base above SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | OIL | 4 | 0.58 | 0.2138547135804405 | 0.08236847319030256 | 0.09050541255907325 | 0.26883038769912687 |  | True | True |
| google-gemini-3-1-pro | GOLD | 3 | 0.65 | -0.005719153078608041 | 0.0571368916439508 | 0.0652738310127215 | 0.2940619692454786 |  | True | True |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | -0.007679821269614084 | 0.022296941089127945 | 0.030433880457898636 | 0.3289019198003015 |  | True | True |
| xai-grok-4-3 | SP500 | 3 | 0.55 | -0.00813693936877069 | 0.015943896864419615 | 0.024080836233190305 | 0.3352549640250098 |  | True | True |
| anthropic-claude-fable-5 | ENERGY | 4 | 0.6 | 0.06909568357131146 | 0.015450165830516501 | 0.02358710519928719 | 0.3357486950589129 |  | True | True |
| anthropic-claude-opus-5 | SP500 | 4 | 0.53 | -0.00813693936877069 | 0.004385888281181116 | 0.012522827649951806 | 0.3468129726082483 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 4 | 0.55 | -0.00813693936877069 | -0.009757658519145918 | -0.0016207191503752275 | 0.3609565194085753 |  | False | False |
| openai-gpt-5-6-sol | CYBERSECURITY | 2 | 0.56 | -0.055244195356285 | -0.03353719858280502 | -0.025400259214034326 | 0.38473605947223444 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | SP500 | 0.012522827649951806 | 0.21663499999999997 | 0.05780611466268982 |
| anthropic-claude-fable-5 | ENERGY | 0.02358710519928719 | 0.45962 | 0.05131870936705799 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 846e446b282f2abc8094e627708bdcdec7452b6fddb1cba831c91746c45f53d5 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | ab28a54578c553e8b02901314a2a4173bfeaf847d07d0d9943d370ce7b7eeb98 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 1de169e00ff9d8826c2920757dc8c9efb7135c4e0c979b369f578183b8febcbd |
| market_data/universe_decision_context.md | 2f7dd6244dd3c38dacb6b261117f3e5458857f0147f279bb5881fa98215b399d |
| market_data/universe_decision_context.json | 12464e5b4a3d1ac903eacfbcd42d613dad469ee59c294e7e8d26c8de9909f1a6 |
| market_data/decision_context_source_history.json | 14a32d7fd16a190c5f9e2f77927b353c0337279deb1894c03ba0a5dcc8df2a82 |
| market_data/universe_quality_evidence.md | e8931ebaf97f706c02129566a3b06c38d174ebb8f93bb3d07c4c565c4b1795e4 |
| market_data/universe_quality_evidence.json | ce34db8d534744bf7a0c42916d5127975ef28b633430177c0e3c626c1166d61b |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 0d736bd1ab3bcfd86ea4300104bf85241765c91a84e7d176f95aba4b11bebcea | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 99a469d3e5384abdb60d51ede0dc216d0f9dd2ae4ad895ea45d350c3894ddf5a | yes |
| Final briefing | research/final_briefing.md | model-facing | 846e446b282f2abc8094e627708bdcdec7452b6fddb1cba831c91746c45f53d5 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
