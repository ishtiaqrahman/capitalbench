# CapitalBench Report: CB-2026-08-04-1M / official-v2-2-all-monthly-20260804-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260804-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-04-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-04
- Decision deadline: 2026-08-05T12:30:00Z
- Horizon: one month
- Entry date: 2026-08-04
- Exit date: 2026-09-04
- Entry rule: Use the Tuesday, August 4, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Friday, September 4, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | TECHNOLOGY | 3 | 0.65 | Overweight technology for growth, with energy and gold as geopolitical hedges. | Escalation of Middle East conflict disrupting oil supplies.; Higher-than-expected inflation delaying Fed rate cuts.; A sudden reversal in technology sector momentum. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.56 | SPY is at a record close with positive breadth, but selected active holdings show stronger supplied quality evidence or event sensitivity. The allocation seeks one-month alpha from risk-on continuation, semiconductor-linked rebound, biotech mean reversion, and energy geopolitical optionality. | High-beta technology and Taiwan exposures could underperform if CPI, PPI, or employment data revive rate concerns.; Semiconductors and Taiwan have large drawdowns and high volatility, so recent strength could reverse quickly.; Strait of Hormuz negotiations could de-escalate energy risk and pressure oil exposure.; A broad equity reversal from record S&P 500 levels would likely hurt most selected active holdings more than SPY. |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 4 | 0.58 | Barbell of AI-chip supply chain (SMH/EWT) on pullback entries and energy as a geopolitical hedge over a 40% SPY core; clusters stay within the 50% cap. | Hot July CPI (Aug 12) with Fed dissenters favoring hikes could hit high-beta tech; Hormuz resolution would deflate energy quickly (Brent already -5.3% on Aug 4); Semis/Taiwan volatility (56%/45%) can produce large drawdowns in one month; Weak Aug 7 or Sep 4 payrolls could sour risk appetite broadly |
| xai-grok-4-5 | xai | portfolio | SOFTWARE | 4 | 0.58 | Selected higher-base active options in tech and energy clusters while respecting 50% cluster cap and using SPY as ballast. Forecasts prioritize one-month catalysts from briefing data releases and Hormuz status. | Sticky inflation and FOMC hawkish dissent could reverse growth/tech leadership; Resolution of Strait of Hormuz talks could pressure energy; High volatility in selected tech names amplifies drawdown risk into September employment; Broad market concentration at records leaves limited cushion if data disappoints |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.5 | Diversified, near-benchmark portfolio with small alpha tilts; equity backdrop is supportive (records, ISM 55.6, high positive-asset breadth) but inflation is sticky and the Fed has hawkish dissenters, so risk budget is limited. | July CPI on Aug 12 surprises higher, pressuring long duration and equity multiples; Hormuz escalation spikes oil and hits risk assets; Momentum/tech unwind after a 4.1% five-day SPY surge; Weak Aug 7 or Sep 4 payrolls signal a growth downturn; Biotech and cybersecurity are high-volatility sleeves that can underperform sharply |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.62 | Selected holdings show base-case outperformance supported by recent relative strength and scheduled data releases within the window. | Elevated inflation readings could pressure growth stocks; Geopolitical developments in Strait of Hormuz; Weaker than expected Q2 GDP revision on August 26 |
| openai-gpt-5-6-sol | openai | portfolio | CYBERSECURITY | 4 | 0.58 | Cross-sectional quality and near-term macro catalysts favor selective active risk over SPY, but elevated rates and event risk warrant diversification rather than concentration in the highest-beta winners. | Hot CPI or PPI could lift Treasury yields and compress equity valuations.; Weak employment or consumer data could reverse cyclical and risk-asset momentum.; Technology and biotech pullbacks may continue despite strong quality ranks.; Yen volatility or geopolitical stress could hurt Japanese equities.; Record US index levels increase broad-market reversal risk. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.55 | Balanced tilt around record-high SPY, adding CYBERSECURITY and INDUSTRIALS which clear the SPY base hurdle on fundamental and quality evidence. | Hot July CPI (Aug 12) or PPI reaccelerates hawkish Fed expectations given 9-3 FOMC vote; Tech/growth pullback hits cybersecurity given elevated volatility; Weak Sept 4 payrolls signals sharper growth slowdown after Q2 GDP 1.5% |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.149999618530273 | 18.52 | 0.30883395754632725 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 36.38999938964844 | 45.23 | 0.24292390103381534 | 2 |
| OIL | Crude Oil | 115.77999877929688 | 141.96 | 0.2261185135319288 | 3 |
| BROAD_COMMODITIES | Broad Commodities | 16.899999618530273 | 19.01 | 0.12485209639627359 | 4 |
| SILVER | Silver | 53.84000015258789 | 59.82 | 0.11106983340386689 | 5 |
| SOUTH_KOREA | South Korea Equities | 171.13999938964844 | 188.87 | 0.10359939624625225 | 6 |
| METALS_MINING | Metals and Mining | 107.86000061035156 | 118.62 | 0.0997589405596182 | 7 |
| TAIWAN | Taiwan Equities | 102.20999908447266 | 112.18 | 0.09754428142874283 | 8 |
| ENERGY | Energy Sector | 58.52000045776367 | 64.06 | 0.09466848084245627 | 9 |
| GOLD | Gold | 76.69000244140625 | 83.39 | 0.0873646804707402 | 10 |
| SOUTH_AFRICA | South Africa Equities | 65.95999908447266 | 71.64 | 0.086112810709005 | 11 |
| BIOTECH | Biotechnology | 151.8800048828125 | 163.81 | 0.0785488196842794 | 12 |
| HEALTHCARE | Healthcare Sector | 162.10000610351562 | 171.45 | 0.0576804043456578 | 13 |
| BRAZIL | Brazil Equities | 36.09000015258789 | 37.86 | 0.04904405209001328 | 14 |
| AGRICULTURE | Agriculture Commodities | 27.65999984741211 | 28.85 | 0.04302242079365848 | 15 |
| JAPAN | Japan Equities | 94.61000061035156 | 98.28 | 0.038790818792647785 | 16 |
| CANADA | Canada Equities | 60.0 | 62.04 | 0.03400000000000003 | 17 |
| DIVIDEND | US Dividend Equities | 33.849998474121094 | 34.8 | 0.028065038957245436 | 18 |
| SOFTWARE | Software | 102.0 | 104.57 | 0.025196078431372504 | 19 |
| EMERGING_MARKETS | Emerging Markets | 60.04999923706055 | 61.44 | 0.0231473901848378 | 20 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.22000122070312 | 73.76 | 0.021323715774950847 | 21 |
| BROAD_AI_TECH | Broad AI Technology | 63.130001068115234 | 64.32 | 0.01884997484160955 | 22 |
| YEN | Japanese Yen | 58.150001525878906 | 58.67 | 0.008942363894688388 | 23 |
| MATERIALS | Materials Sector | 52.0 | 52.44 | 0.00846153846153852 | 24 |
| EURO | Euro | 106.37000274658203 | 107.15 | 0.007332868602779374 | 25 |
| UNITED_KINGDOM | United Kingdom Equities | 48.34000015258789 | 48.59 | 0.005171697282229548 | 26 |
| LARGE_VALUE | US Large-Cap Value | 256.6300048828125 | 257.63 | 0.0038966414610954736 | 27 |
| FINANCIALS | Financials Sector | 57.880001068115234 | 58.1 | 0.0038009489949017983 | 28 |
| AUSTRALIA | Australia Equities | 30.1200008392334 | 30.23 | 0.0036520304681837423 | 29 |
| TECHNOLOGY | Technology Sector | 186.89999389648438 | 187.28 | 0.0020332055426717233 | 30 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.41999816894531 | 91.45 | 0.00032817580021426984 | 31 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 32 |
| COMMUNICATIONS | Communication Services Sector | 112.04000091552734 | 112.03 | -8.926200861858469e-05 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 107.05000305175781 | 106.97 | -0.0007473428255684311 | 34 |
| EUROPE | Europe Equities | 91.83999633789062 | 91.74 | -0.0010888103427479923 | 35 |
| SP500 | S&P 500 | 771.3300170898438 | 770.19 | -0.001477988752654591 | 36 |
| US_DOLLAR | US Dollar | 28.15999984741211 | 28.08 | -0.002840903687698848 | 37 |
| TOTAL_US_MARKET | Total US Stock Market | 380.82000732421875 | 379.73 | -0.002862263807717258 | 38 |
| COPPER | Copper | 40.13999938964844 | 39.95 | -0.00473341785095871 | 39 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.55000305175781 | 79.16 | -0.0049026151702856735 | 40 |
| MEXICO | Mexico Equities | 77.05999755859375 | 76.63 | -0.005580035974784403 | 41 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.22999572753906 | 219.0 | -0.005585050862284779 | 42 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.29499816894531 | 92.715 | -0.006216819554409669 | 43 |
| NASDAQ100 | Nasdaq 100 | 723.8499755859375 | 718.96 | -0.006755509775322133 | 44 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.66000366210938 | 97.0 | -0.006758177732543391 | 45 |
| LARGE_GROWTH | US Large-Cap Growth | 124.30000305175781 | 123.41 | -0.007160120916386625 | 46 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.81999969482422 | 82.21 | -0.007365367025742087 | 47 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.22000122070312 | 94.47 | -0.007876509253184727 | 48 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.37000274658203 | 84.58 | -0.009253868117201858 | 49 |
| SMALL_VALUE | US Small-Cap Value | 226.97000122070312 | 224.62 | -0.010353796572517115 | 50 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.25 | 92.25 | -0.01072386058981234 | 51 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.970001220703125 | 47.45 | -0.010840133572452282 | 52 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.76000213623047 | 105.48 | -0.01198952894921379 | 53 |
| INDIA | India Equities | 50.529998779296875 | 49.91 | -0.012269914788735403 | 54 |
| SEMICONDUCTORS | Semiconductors | 575.7100219726562 | 567.01 | -0.01511181261504857 | 55 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.76000213623047 | 104.03 | -0.01635781109385792 | 56 |
| SMALL_CAP | US Small-Cap Stocks | 301.7099914550781 | 296.01 | -0.018892286024696725 | 57 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.83000183105469 | 122.25 | -0.020668122992952176 | 58 |
| CHINA | China Equities | 56.09000015258789 | 54.91 | -0.021037620776926502 | 59 |
| MID_CAP | US Mid-Cap Stocks | 77.4800033569336 | 75.85 | -0.021037729560032803 | 60 |
| LOW_VOL | US Low Volatility Equities | 76.38999938964844 | 74.74 | -0.02159967800539131 | 61 |
| UTILITIES | Utilities Sector | 44.11000061035156 | 43.08 | -0.02335072763771051 | 62 |
| MOMENTUM | US Momentum Equities | 313.3500061035156 | 304.86 | -0.02709432244501353 | 63 |
| REAL_ESTATE | Real Estate Sector | 45.16999816894531 | 43.93 | -0.027451809147909567 | 64 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.29000091552734 | 114.91 | -0.028573851461384803 | 65 |
| REGIONAL_BANKS | Regional Banks | 77.83999633789062 | 75.27 | -0.03301639849435112 | 66 |
| CYBERSECURITY | Cybersecurity | 97.94000244140625 | 94.59 | -0.03420463914538319 | 67 |
| INDUSTRIALS | Industrials Sector | 186.39999389648438 | 175.27 | -0.0597102696401659 | 68 |
| SOLAR | Solar Energy | 53.369998931884766 | 48.04 | -0.09986882215769488 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 250.64999389648438 | 225.61 | -0.0999002374076482 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SP500 | 40.0 | -0.001477988752654591 | -0.0005911955010618364 | Record-high close with strong ISM (55.6) and cooling core inflation; solid benchmark core. |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 25.0 | -0.01511181261504857 | -0.0037779531537621425 | Strongest prior active trend (+39.5% prior 105s) with deep recent pullback (-7.4% active 21s), top-decile quality evidence; AI capex cycle intact per broad tech strength. |
| anthropic-claude-fable-5 | TAIWAN | 20.0 | 0.09754428142874283 | 0.01950885628574857 | Very strong prior active trend (+47%) with meaningful recent pullback (-7.4% active), leveraged to same semiconductor demand; weaker dollar (UUP -1.5% 5s) is a tailwind. |
| anthropic-claude-fable-5 | ENERGY | 15.0 | 0.09466848084245627 | 0.01420027212636844 | Gulf exports still 16.1 vs 24 mbd prewar, Hormuz status unresolved; sector +7.5% active 21s with negative SPY beta provides hedge against oil-shock scenarios. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | -0.001477988752654591 | -0.0007389943763272955 | Record close with broad breadth (79.7% positive assets over 5 days); solid ISM manufacturing and resilient consumer. |
| anthropic-claude-opus-4-8 | CYBERSECURITY | 25.0 | -0.03420463914538319 | -0.008551159786345797 | Strong prior active trend with recent pullback (positive pullback rank), robust quality score, secular demand independent of rate path. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 25.0 | -0.0597102696401659 | -0.014927567410041476 | ISM Manufacturing PMI jumped to 55.6 with new orders 56.7, production 58.5, supporting cyclical industrials. |
| anthropic-claude-opus-5 | SP500 | 40.0 | -0.001477988752654591 | -0.0005911955010618364 | Core benchmark exposure at record highs with broad participation. |
| anthropic-claude-opus-5 | BIOTECH | 20.0 | 0.0785488196842794 | 0.015709763936855883 | Strong prior relative trend plus deep recent relative pullback; top quality evidence score. |
| anthropic-claude-opus-5 | CYBERSECURITY | 15.0 | -0.03420463914538319 | -0.005130695871807478 | Positive prior and recent active return with no drawdown from 52-week high; lower volatility than other tech sleeves. |
| anthropic-claude-opus-5 | LARGE_VALUE | 15.0 | 0.0038966414610954736 | 0.000584496219164321 | Positive 21-day active return, low volatility, shallow drawdown, at 52-week high. |
| anthropic-claude-opus-5 | FINANCIALS | 10.0 | 0.0038009489949017983 | 0.00038009489949017986 | Steep curve (30y 5.18% vs 1y 4.04%), positive active return, smallest drawdown among sectors. |
| google-gemini-3-1-pro | TECHNOLOGY | 40.0 | 0.0020332055426717233 | 0.0008132822170686893 | Strong momentum and high quality evidence score support continued outperformance. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.09466848084245627 | 0.02840054425273688 | Geopolitical tensions in the Middle East and tight supply support energy prices. |
| google-gemini-3-1-pro | GOLD | 30.0 | 0.0873646804707402 | 0.026209404141222057 | Safe-haven demand amid geopolitical uncertainty and potential rate cuts. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.01511181261504857 | -0.005289134415266999 | Strongest supplied trend-plus-pullback setup among technology candidates, with very high prior active return and high quality evidence, despite high volatility. |
| openai-gpt-5-5 | CYBERSECURITY | 15.0 | -0.03420463914538319 | -0.005130695871807478 | Selected as a technology-and-growth holding with positive recent and prior active returns, at a 52-week high, but lower beta than the highest-volatility AI/semiconductor choices. |
| openai-gpt-5-5 | TAIWAN | 25.0 | 0.09754428142874283 | 0.024386070357185707 | International semiconductor-linked exposure with very high prior active rank and recent pullback rank, offering non-US participation in the same electronics cycle. |
| openai-gpt-5-5 | BIOTECH | 15.0 | 0.0785488196842794 | 0.01178232295264191 | High quality evidence score and strong prior active return after a deep recent active pullback create a mean-reversion plus trend setup outside technology. |
| openai-gpt-5-5 | OIL | 10.0 | 0.2261185135319288 | 0.02261185135319288 | Small diversifying energy allocation tied to unresolved Strait of Hormuz risk and strong prior active return, balanced against the sharp one-day crude decline. |
| openai-gpt-5-6-sol | CYBERSECURITY | 30.0 | -0.03420463914538319 | -0.010261391743614956 | Positive 21-session active return and strong prior active trend provide independent support for recent strength, while its volatility is below the most aggressive technology alternatives. |
| openai-gpt-5-6-sol | BIOTECH | 25.0 | 0.0785488196842794 | 0.01963720492106985 | The highest quality score combines a strong prior trend with an unusually deep relative pullback, creating a favorable one-month rebound setup. |
| openai-gpt-5-6-sol | JAPAN | 25.0 | 0.038790818792647785 | 0.009697704698161946 | Strong prior trend, deep pullback rank, and recent absolute strength support a diversified rebound candidate outside US equities. |
| openai-gpt-5-6-sol | INDUSTRIALS | 20.0 | -0.0597102696401659 | -0.011942053928033181 | Improving manufacturing data and a solid quality score support cyclical exposure with substantially less volatility than thematic technology. |
| xai-grok-4-3 | SP500 | 40.0 | -0.001477988752654591 | -0.0005911955010618364 | Broad US equity exposure with record closes and stable macro backdrop. |
| xai-grok-4-3 | TECHNOLOGY | 30.0 | 0.0020332055426717233 | 0.0006099616628015169 | Strong recent relative performance and ISM manufacturing strength support outperformance. |
| xai-grok-4-3 | JAPAN | 20.0 | 0.038790818792647785 | 0.007758163758529557 | High quality evidence score and positive 5-day return versus SPY. |
| xai-grok-4-3 | LARGE_VALUE | 10.0 | 0.0038966414610954736 | 0.0003896641461095474 | Positive 21-day active return and lower volatility profile. |
| xai-grok-4-5 | SOFTWARE | 35.0 | 0.025196078431372504 | 0.008818627450980375 | Strong recent absolute performance and positive active return support higher base case than SPY amid growth leadership persistence into data releases. |
| xai-grok-4-5 | CYBERSECURITY | 15.0 | -0.03420463914538319 | -0.005130695871807478 | Positive active return and at 52w high with quality score support outperformance vs broad market over one-month window. |
| xai-grok-4-5 | ENERGY | 20.0 | 0.09466848084245627 | 0.018933696168491256 | Strong 21s active return and oil volatility create asymmetric upside if Hormuz risks reprice before exit. |
| xai-grok-4-5 | SP500 | 30.0 | -0.001477988752654591 | -0.00044339662579637726 | Benchmark core holding given record close and broad positive asset share; anchors portfolio while active sleeves seek alpha. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | TECHNOLOGY | 3 | 0.65 | 0.0020332055426717233 | 0.05542323061102762 | 0.05690121936368221 | 0.25341072693529965 |  | True | True |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.56 | -0.01511181261504857 | 0.04836041437594602 | 0.04983840312860061 | 0.26047354317038124 |  | True | True |
| anthropic-claude-fable-5 | SP500 | 4 | 0.58 | -0.001477988752654591 | 0.02933997975729303 | 0.03081796850994762 | 0.27949397778903423 |  | True | True |
| xai-grok-4-5 | SOFTWARE | 4 | 0.58 | 0.025196078431372504 | 0.022178231121867772 | 0.023656219874522363 | 0.28665572642445947 |  | True | True |
| anthropic-claude-opus-5 | SP500 | 5 | 0.5 | -0.001477988752654591 | 0.010952463682641068 | 0.012430452435295659 | 0.2978814938636862 |  | True | True |
| xai-grok-4-3 | SP500 | 4 | 0.62 | -0.001477988752654591 | 0.008166594066378785 | 0.009644582819033376 | 0.3006673634799485 |  | True | True |
| openai-gpt-5-6-sol | CYBERSECURITY | 4 | 0.58 | -0.03420463914538319 | 0.00713146394758366 | 0.008609452700238251 | 0.30170249359874357 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.55 | -0.001477988752654591 | -0.024217721572714568 | -0.022739732820059977 | 0.3330516791190418 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 8867d2beab94d6e43833c054c911d08bbab8cceafee0184e7c5b94953efd25bc |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | fc00696229a62ba5abc12c83e12154fe67d73ad64f1b4f58942e25b7340b6a11 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | d629d140f8fb97591536a62dce13df9fc868a866874c88690bb28669f5041a17 |
| market_data/universe_decision_context.md | e61d4585419c2ace7b412fec75941a8a0bc324b245d48585e27eef02207cab50 |
| market_data/universe_decision_context.json | 401e99955ca25da3939e9f88fe86f20f69dac72392b1c19960faad8d59f53af5 |
| market_data/decision_context_source_history.json | 073a73508e18b3f6d945ada4780eb5c180b5b450ba9fdf02c08018c2c595bc88 |
| market_data/universe_quality_evidence.md | 18e36c777c256251c051428ff93eab4627ff2fccc3deb6bb0dd1d5f22d7ac764 |
| market_data/universe_quality_evidence.json | f43fcf423201ddb1447b913ac2c6b8cda6fa80fb5df6a36caac9f42f9b7a9970 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | e9288f14cea5acfdee6d969ab4b469a710fa7c4b6f260b55988bf7169a17ca51 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 191f38bebe6dd1623e871a317f42bcb3491ba0865c486a6a0ec2d8ba493b1902 | yes |
| Final briefing | research/final_briefing.md | model-facing | 8867d2beab94d6e43833c054c911d08bbab8cceafee0184e7c5b94953efd25bc | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
