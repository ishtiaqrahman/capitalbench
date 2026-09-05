# CapitalBench Report: CB-2026-08-05-1M / official-v2-2-all-monthly-20260805

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260805
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-05-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-05
- Decision deadline: 2026-08-06T12:30:00Z
- Horizon: one month
- Entry date: 2026-08-05
- Exit date: 2026-09-04
- Entry rule: Use the Wednesday, August 5, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Friday, September 4, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Overweight semiconductors/software on AI earnings strength and disinflation trajectory, add biotech and Taiwan with high quality-evidence scores, keep 10% SPY as ballast. | Hot July/August CPI (services prices at 70.3 ISM) triggers Fed hike pricing and growth-stock derating; High beta (~1.6 blended) means any broad selloff produces sizable negative alpha; Hormuz deal collapse spikes oil and inflation expectations; Semiconductor concentration: single-sector guidance disappointment hits three holdings simultaneously |
| xai-grok-4-5 | xai | portfolio | SEMICONDUCTORS | 4 | 0.58 | Selected holdings combine top quality-evidence scores, strong prior active trends, and recent pullbacks with one-month catalysts from data and earnings residual. Cluster limits and SPY inclusion control concentration while targeting positive alpha. | Sticky inflation and hawkish Fed residual from July FOMC could pressure growth equities; High volatility in semiconductors and Taiwan could reverse recent gains sharply; Geopolitical developments around energy or Asia trade disrupting international sleeves; Broad market concentration unwind if equal-weight or value factors rotate strongly |
| openai-gpt-5-5 | openai | portfolio | BIOTECH | 5 | 0.56 | SPY is forecast at a modest positive base return, but selected active candidates have stronger one-month base cases from quality ranks and relative trend/pullback evidence. The allocation balances upside from semiconductors, Taiwan, cybersecurity, and biotech with a smaller financials position. | A hotter July CPI/PPI or employment report could lift rate expectations and pressure high-beta growth, biotech, and semiconductor exposures.; Recent high-volatility winners such as semiconductors and Taiwan could mean-revert sharply over a one-month horizon.; Geopolitical or supply-chain stress could hurt Taiwan and semiconductor-linked holdings despite strong prior momentum.; If market leadership broadens defensively or rotates to cash-like assets, the portfolio may underperform SPY's large-cap benchmark composition. |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 2 | 0.56 | Semiconductors offer trend continuation backed by manufacturing and earnings evidence, while biotech offers a contrarian rebound setup. Both base forecasts exceed SPY's forecast for the one-month window. | Higher-than-expected CPI, PPI, or PCE data could lift yields and compress high-duration equity valuations.; Semiconductor gains could reverse after the 12.99% five-session advance and amid 55.95% annualized volatility.; Biotech's rebound thesis relies mainly on mechanical quality and pullback evidence rather than a supplied sector-specific catalyst.; Weak payroll, consumer, or GDP data could trigger a broad risk-off move before September 4. |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.5 | Hold SPY as the anchor and add healthcare, financials and equal-weight for mean-reversion of a very narrow five-session mega-cap advance, while capping any non-benchmark cluster at 40%. | Sticky inflation (core PCE 3.3%, PPI 5.5% y/y) with three FOMC hawkish dissents could lift yields and hit equities; Continued mega-cap/AI leadership would leave equal-weight and defensive tilts trailing SPY; Weak Sep 4 payrolls after 57k June and 44k ADP July could trigger a growth scare; Hormuz arrangement failure could re-spike oil and pressure margins; Heavy August Treasury refunding supply pressuring long-end yields and rate-sensitive equities |
| google-gemini-3-1-pro | google | portfolio | TECHNOLOGY | 4 | 0.65 | A balanced approach favoring technology and industrials for growth, with gold and healthcare for defense. | Higher-than-expected inflation data could trigger a sell-off in growth sectors like technology.; Geopolitical de-escalation could reduce the safe-haven appeal of gold.; A sudden deterioration in macroeconomic data could negatively impact industrials. |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Ledger spans four clusters with SP500 included; only SP500 selected as no superior base forecasts identified. | Higher than expected inflation from PCE and CPI data; Labor market softening in July Employment Situation; Geopolitical supply risks in energy markets |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.55 | Tilt toward US equity with tech and industrials overweights supported by strong ISM data and earnings momentum; SPY anchors the book. | Hot July CPI (Aug 12) or PPI (Aug 13) reviving rate-hike fears given 3 FOMC dissenters; Weak Sep 4 jobs report signaling labor deterioration; Tech high beta and elevated volatility amplifying drawdowns |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.48 | 18.52 | 0.27900552486187835 | 1 |
| OIL | Crude Oil | 114.88 | 141.96 | 0.235724233983287 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 36.74 | 45.23 | 0.23108328796951527 | 3 |
| BROAD_COMMODITIES | Broad Commodities | 16.98 | 19.01 | 0.1195524146054181 | 4 |
| ENERGY | Energy Sector | 57.31 | 64.06 | 0.11778049206072239 | 5 |
| SOUTH_KOREA | South Korea Equities | 169.14 | 188.87 | 0.1166489298805724 | 6 |
| TAIWAN | Taiwan Equities | 101.7 | 112.18 | 0.10304818092428714 | 7 |
| SOUTH_AFRICA | South Africa Equities | 66.85 | 71.64 | 0.07165295437546759 | 8 |
| BIOTECH | Biotechnology | 153.01 | 163.81 | 0.07058362198549117 | 9 |
| SILVER | Silver | 56.07 | 59.82 | 0.06688068485821286 | 10 |
| METALS_MINING | Metals and Mining | 111.92 | 118.62 | 0.05986418870621879 | 11 |
| BRAZIL | Brazil Equities | 36.11 | 37.86 | 0.04846302963168103 | 12 |
| HEALTHCARE | Healthcare Sector | 164.16 | 171.45 | 0.044407894736842035 | 13 |
| GOLD | Gold | 79.85 | 83.39 | 0.04433312460864136 | 14 |
| AGRICULTURE | Agriculture Commodities | 27.63 | 28.85 | 0.04415490408975753 | 15 |
| DIVIDEND | US Dividend Equities | 33.64 | 34.8 | 0.0344827586206895 | 16 |
| JAPAN | Japan Equities | 95.16 | 98.28 | 0.032786885245901676 | 17 |
| SOFTWARE | Software | 101.31 | 104.57 | 0.03217846214588871 | 18 |
| BROAD_AI_TECH | Broad AI Technology | 62.36 | 64.32 | 0.0314304041051956 | 19 |
| EMERGING_MARKETS | Emerging Markets | 60.01 | 61.44 | 0.02382936177303785 | 20 |
| CANADA | Canada Equities | 60.78 | 62.04 | 0.02073050345508398 | 21 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.35 | 73.76 | 0.019488597097443217 | 22 |
| COMMUNICATIONS | Communication Services Sector | 110.87 | 112.03 | 0.010462704067827122 | 23 |
| YEN | Japanese Yen | 58.15 | 58.67 | 0.008942390369733433 | 24 |
| TECHNOLOGY | Technology Sector | 185.91 | 187.28 | 0.007369157119036185 | 25 |
| LARGE_VALUE | US Large-Cap Value | 256.13 | 257.63 | 0.005856401046343551 | 26 |
| EURO | Euro | 106.585 | 107.15 | 0.005300933527231821 | 27 |
| UNITED_KINGDOM | United Kingdom Equities | 48.37 | 48.59 | 0.004548273723382401 | 28 |
| AUSTRALIA | Australia Equities | 30.14 | 30.23 | 0.0029860650298605407 | 29 |
| NASDAQ100 | Nasdaq 100 | 717.3 | 718.96 | 0.002314233932803722 | 30 |
| FINANCIALS | Financials Sector | 58.0 | 58.1 | 0.0017241379310344307 | 31 |
| SP500 | S&P 500 | 769.79 | 770.19 | 0.0005196222346355306 | 32 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.43 | 91.45 | 0.00021874658208465014 | 33 |
| TOTAL_US_MARKET | Total US Stock Market | 379.65 | 379.73 | 0.00021072040036895778 | 34 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 35 |
| TIPS | Treasury Inflation-Protected Securities | 107.0 | 106.97 | -0.0002803738317757043 | 36 |
| US_DOLLAR | US Dollar | 28.09 | 28.08 | -0.0003559985760057671 | 37 |
| MEXICO | Mexico Equities | 76.69 | 76.63 | -0.0007823705828661209 | 38 |
| EUROPE | Europe Equities | 91.85 | 91.74 | -0.0011976047904191933 | 39 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.4 | 122.25 | -0.001225490196078427 | 40 |
| SMALL_VALUE | US Small-Cap Value | 225.08 | 224.62 | -0.0020437177892305147 | 41 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 219.73 | 219.0 | -0.0033222591362125353 | 42 |
| MATERIALS | Materials Sector | 52.64 | 52.44 | -0.0037993920972645423 | 43 |
| LARGE_GROWTH | US Large-Cap Growth | 123.89 | 123.41 | -0.0038744047138591364 | 44 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.52 | 79.16 | -0.00452716297786715 | 45 |
| SEMICONDUCTORS | Semiconductors | 569.7 | 567.01 | -0.004721783394769252 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.34 | 92.715 | -0.006695950289265062 | 47 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.71 | 97.0 | -0.007266400573124443 | 48 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.17 | 94.47 | -0.007355259010192294 | 49 |
| INDIA | India Equities | 50.31 | 49.91 | -0.007950705625124344 | 50 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.33 | 84.58 | -0.008789405836165498 | 51 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.0 | 82.21 | -0.009518072289156687 | 52 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.99 | 47.45 | -0.01125234423838295 | 53 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.31 | 92.25 | -0.01135998285285611 | 54 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.74 | 105.48 | -0.011804384485666009 | 55 |
| SMALL_CAP | US Small-Cap Stocks | 299.77 | 296.01 | -0.012542949594689268 | 56 |
| UTILITIES | Utilities Sector | 43.66 | 43.08 | -0.013284470911589463 | 57 |
| MID_CAP | US Mid-Cap Stocks | 77.0 | 75.85 | -0.014935064935065023 | 58 |
| MOMENTUM | US Momentum Equities | 309.98 | 304.86 | -0.016517194657719836 | 59 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.82 | 104.03 | -0.01691551691551685 | 60 |
| CHINA | China Equities | 56.01 | 54.91 | -0.01963935011605078 | 61 |
| LOW_VOL | US Low Volatility Equities | 76.33 | 74.74 | -0.020830603956504712 | 62 |
| COPPER | Copper | 40.85 | 39.95 | -0.022031823745410017 | 63 |
| REGIONAL_BANKS | Regional Banks | 77.34 | 75.27 | -0.026764934057408984 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.2 | 43.93 | -0.028097345132743423 | 65 |
| CYBERSECURITY | Cybersecurity | 97.57 | 94.59 | -0.030542174848826376 | 66 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.64 | 114.91 | -0.031439649359406685 | 67 |
| INDUSTRIALS | Industrials Sector | 186.35 | 175.27 | -0.05945800912261867 | 68 |
| SOLAR | Solar Energy | 51.27 | 48.04 | -0.06299980495416435 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 252.28 | 225.61 | -0.10571587125416204 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 25.0 | -0.004721783394769252 | -0.001180445848692313 | Strongest prior trend (37% prior active return, top quality score 0.738) with AI earnings momentum (Nvidia +3.4% on earnings); reported 50% aggregate S&P profit growth supports the AI capex cycle. |
| anthropic-claude-fable-5 | SOFTWARE | 25.0 | 0.03217846214588871 | 0.008044615536472177 | Positive recent active return (+4.67% 21s) with deep prior pullback offering mean-reversion entry; benefits from same disinflation/rate path as growth. |
| anthropic-claude-fable-5 | TAIWAN | 20.0 | 0.10304818092428714 | 0.02060963618485743 | Top prior active rank (1.00) on semiconductor supply-chain strength; dollar weakness (UUP -1.09% 21s) supports non-US equity returns. |
| anthropic-claude-fable-5 | BIOTECH | 20.0 | 0.07058362198549117 | 0.014116724397098235 | Highest quality evidence score (0.785): strong prior trend (+19.5% prior active) with deep recent pullback (-9.58% 21s active), a favorable buy-the-dip setup; benefits from any rate relief. |
| anthropic-claude-fable-5 | SP500 | 10.0 | 0.0005196222346355306 | 5.196222346355306e-05 | Benchmark ballast near record levels with strong ISM (55.6) and record Dow close. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | 0.0005196222346355306 | 0.0002598111173177653 | Strong recent momentum, robust earnings season (~50% aggregate profit growth reported), and healthy ISM readings support broad large-cap equity. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 30.0 | 0.007369157119036185 | 0.002210747135710855 | Positive active return over 21 sessions, strong prior trend, and AI/semiconductor tailwinds; XLK has led with strong new-order manufacturing backdrop. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | -0.05945800912261867 | -0.011891601824523736 | ISM Manufacturing PMI at 55.6, highest since May 2022, with strong new orders and production supports industrials cyclicals. |
| anthropic-claude-opus-5 | SP500 | 40.0 | 0.0005196222346355306 | 0.00020784889385421225 | Core benchmark exposure with strong earnings season and record Dow. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | 0.044407894736842035 | 0.008881578947368407 | Defensive sector with high quality evidence score, recent underperformance, low beta and shallow drawdown. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | 0.0017241379310344307 | 0.00034482758620688617 | At 52-week high with low volatility and smallest drawdown; steep curve (5.17% 30y vs 3.50-3.75% funds) supports margins. |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 20.0 | -0.0033222591362125353 | -0.0006644518272425071 | Breadth catch-up after RSP lagged SPY by 3.67% in five sessions; lowest volatility broad equity sleeve. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | 0.007369157119036185 | 0.002210747135710855 | Strong recent momentum and high quality evidence score support continued outperformance. |
| google-gemini-3-1-pro | INDUSTRIALS | 30.0 | -0.05945800912261867 | -0.0178374027367856 | Supported by strong ISM Manufacturing PMI data and solid quality evidence. |
| google-gemini-3-1-pro | GOLD | 20.0 | 0.04433312460864136 | 0.008866624921728272 | Provides a hedge against geopolitical risks and potential inflation persistence. |
| google-gemini-3-1-pro | HEALTHCARE | 20.0 | 0.044407894736842035 | 0.008881578947368407 | Defensive characteristics with a strong quality evidence score and recent pullback. |
| openai-gpt-5-5 | BIOTECH | 30.0 | 0.07058362198549117 | 0.02117508659564735 | Highest quality evidence score among the assessed candidates, with a strong prior active trend and a deep recent relative pullback that can rebound if risk appetite remains firm. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | -0.004721783394769252 | -0.001180445848692313 | Very strong prior active return and high quality score support continuation, while the recent pullback provides potential rebound fuel into the one-month window. |
| openai-gpt-5-5 | TAIWAN | 20.0 | 0.10304818092428714 | 0.02060963618485743 | Taiwan has the top prior active rank in the quality table and strong semiconductor-linked momentum, offering differentiated international tech exposure within the cluster cap. |
| openai-gpt-5-5 | CYBERSECURITY | 15.0 | -0.030542174848826376 | -0.004581326227323956 | Cybersecurity combines positive 21-day active return, strong prior active return, and a shallow distance from its 52-week high relative to other growth options. |
| openai-gpt-5-5 | FINANCIALS | 10.0 | 0.0017241379310344307 | 0.00017241379310344309 | Financials provide non-technology cyclical exposure with positive recent active return, a new 52-week high, and lower volatility than most high-beta selections. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 50.0 | -0.004721783394769252 | -0.002360891697384626 | Strong prior benchmark-relative trend and a high quality-evidence score support continuation after a relative pullback, while manufacturing strength and aggregate earnings growth provide independent support. |
| openai-gpt-5-6-sol | BIOTECH | 50.0 | 0.07058362198549117 | 0.03529181099274559 | The highest quality-evidence score and a deep recent relative pullback create a rebound setup that complements semiconductor exposure, though sector-specific fundamental evidence is limited. |
| xai-grok-4-3 | SP500 | 100.0 | 0.0005196222346355306 | 0.0005196222346355306 | No active option base forecast exceeds SPY; broad diversified US equity exposure aligns with neutral data and scheduled releases. |
| xai-grok-4-5 | SEMICONDUCTORS | 30.0 | -0.004721783394769252 | -0.0014165350184307756 | Highest prior active trend and quality score with AI/earnings momentum support for outperformance vs broad market over one month. |
| xai-grok-4-5 | BIOTECH | 25.0 | 0.07058362198549117 | 0.017645905496372793 | Top quality evidence score with deep recent pullback rank supporting mean-reversion plus momentum continuation into the scoring window. |
| xai-grok-4-5 | TAIWAN | 20.0 | 0.10304818092428714 | 0.02060963618485743 | Strongest prior active return and high quality score tied to semiconductor supply chain exposure exceeding SPY base case. |
| xai-grok-4-5 | SP500 | 25.0 | 0.0005196222346355306 | 0.00012990555865888265 | Core benchmark holding for diversification while active sleeves target higher base forecasts. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 5 | 0.55 | -0.004721783394769252 | 0.04164249249319908 | 0.04112287025856355 | 0.23736303236867928 |  | True | True |
| xai-grok-4-5 | SEMICONDUCTORS | 4 | 0.58 | -0.004721783394769252 | 0.03696891222145833 | 0.0364492899868228 | 0.24203661264042003 |  | True | True |
| openai-gpt-5-5 | BIOTECH | 5 | 0.56 | 0.07058362198549117 | 0.036195364497591954 | 0.035675742262956424 | 0.2428101603642864 |  | True | True |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 2 | 0.56 | -0.004721783394769252 | 0.03293091929536096 | 0.03241129706072543 | 0.2460746055665174 |  | True | True |
| anthropic-claude-opus-5 | SP500 | 4 | 0.5 | 0.0005196222346355306 | 0.008769803600186999 | 0.008250181365551468 | 0.2702357212616914 |  | True | True |
| google-gemini-3-1-pro | TECHNOLOGY | 4 | 0.65 | 0.007369157119036185 | 0.0021215482680219337 | 0.001601926033386403 | 0.27688397659385644 |  | True | True |
| xai-grok-4-3 | SP500 | 1 | 0.5 | 0.0005196222346355306 | 0.0005196222346355306 | 0.0 | 0.2784859026272428 |  | False | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.55 | 0.0005196222346355306 | -0.009421043571495116 | -0.009940665806130646 | 0.28842656843337344 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 8a76c6e6ce6b3fe08a83e293601adca9ec61fd9fbab061267c7005b07e268e29 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | 1586a1cc8b0afc3f0f9310430337cd1577e3a694f47f41a21f5397f09f7e50e4 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | bfc6174602bee58d06d9581abcaa025a884baa2308476051bc3a5ceab13900ad |
| market_data/universe_decision_context.md | 02c1f007671722435bd04cb22964d6a2223d87ac67bfa4d98d1115f29e6bb082 |
| market_data/universe_decision_context.json | bac461e9c97912d2665dad37db2e2860acce0652a03c0d0e83add0a2f252dc95 |
| market_data/decision_context_source_history.json | ec5024c44ecd7a1636397bb1130b8dcbecd148a09c6841e8f6072af4fb7ff6d1 |
| market_data/universe_quality_evidence.md | fc3dc8d219b0a6b742acb9457dcd436106636d2468a9a33d9e49e8edbd2b1e5a |
| market_data/universe_quality_evidence.json | 5b5aacac97bc559adc22fdd04786d69ed3bf76bae1f348ca57d567a29c824e25 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 3c0b4c1cb23a494fcddf289ba5d11dbfb52f9a0549c507459224b5f1e8021a66 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 11e7d225e63bc14636dd954888b98832a223c0d38eee09db1f4f8083b60638cd | yes |
| Final briefing | research/final_briefing.md | model-facing | 8a76c6e6ce6b3fe08a83e293601adca9ec61fd9fbab061267c7005b07e268e29 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
