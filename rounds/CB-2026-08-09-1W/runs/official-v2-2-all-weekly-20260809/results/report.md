# CapitalBench Report: CB-2026-08-09-1W / official-v2-2-all-weekly-20260809

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260809
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-09-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-09
- Decision deadline: 2026-08-10T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-10
- Exit date: 2026-08-17
- Entry rule: Use the Monday, August 10, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Monday, August 17, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 3 | 0.58 | ENERGY has the clearest near-term fundamental catalyst, while UNITED_KINGDOM and LOW_VOL provide strong quality evidence and potential defensive rotation. All selected holdings have base forecasts above SPY's 0.35% forecast. | A rapid reopening of oil transit routes could reverse the energy thesis.; Benign inflation and strong retail sales could extend the mega-cap-led risk rally and hurt defensive relative performance.; A stronger U.S. dollar could reduce returns on unhedged United Kingdom equities.; One-week outcomes may be dominated by volatile reactions to CPI and PPI rather than prior quality signals. |
| anthropic-claude-fable-5 | anthropic | portfolio | GOLD | 4 | 0.56 | Real-asset and value tilt (gold, energy, UK) funded from a partial SPY anchor, positioned for sticky-inflation prints and geopolitical supply risk during the Aug 10-17 window. | Soft July CPI could lift growth/tech and hurt gold and energy relative to SPY; Sudden Middle East de-escalation or Hormuz reopening would hit energy and gold; Hot CPI could trigger broad risk-off dragging all equity holdings; Dollar rebound would pressure gold and international equities |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.55 | One-week alpha is expected to come from unresolved oil-supply risk, precious-metals support, commodity/mining momentum, and selective defensive rotation around CPI, PPI, and retail-sales releases. The main tradeoff is higher idiosyncratic volatility versus the benchmark. | CPI or PPI comes in benign enough to lift broad U.S. growth equities and reduce demand for gold and defensive exposures.; A rapid de-escalation or reopening arrangement for the Strait of Hormuz reverses oil and energy-sensitive trades.; Recent commodity and metals strength proves overextended and mean-reverts during the scoring week.; SPY momentum persists after its record close, led by mega-cap technology not represented in the selected portfolio. |
| xai-grok-4-5 | xai | portfolio | SP500 | 4 | 0.58 | One-week window dominated by CPI/PPI/retail data and unresolved oil-flow risk. Portfolio mixes benchmark beta with higher-base gold, energy, and value while staying inside allocation and cluster rules. | Soft July payrolls and revisions raise recession-scare risk-off that hits equities and commodities together; Stronger-than-expected CPI could reverse rate-cut hopes and pressure gold and duration-sensitive value; Sudden Hormuz de-escalation would remove energy and gold tailwinds; High recent SPY momentum leaves room for mean-reversion after 3.5% weekly gain |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.5 | SPY sits at a record after a +3.6% week into a dense CPI/PPI/retail-sales calendar, so a barbell of core index, gold, healthcare, and tech is preferred to a concentrated bet. | Hot July CPI on Aug 12 hits both equities and gold via higher real yields; Mean reversion after SPY's +3.5% five-day run; Gold already up 7.2% in five sessions and vulnerable to profit-taking; Tech's high beta amplifies any macro-driven drawdown |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.55 | SP500 at 50% anchors the portfolio while GOLD, JAPAN and HEALTHCARE each exceed SP500 base forecast and stay within cluster caps. | CPI and PPI releases on August 12-13 could trigger volatility; Unresolved Strait of Hormuz issues may reverse commodity flows; Downward payroll revisions increase recession odds before exit |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.5 | Half SPY, quarter gold for momentum/safe-haven, quarter healthcare for defensive tilt given soft payrolls. | Hot July CPI/PPI on Aug 12-13 lifts yields and hurts gold and equities; Risk-on continuation leaves defensives and gold lagging SPY; Middle East/oil shock triggers broad risk-off |
| google-gemini-3-1-pro | google | portfolio | GOLD | 2 | 0.65 | Defensive positioning with Gold and Healthcare to navigate mixed economic signals and geopolitical uncertainty. | A sudden resolution to Middle East tensions could reduce safe-haven demand for Gold.; Stronger-than-expected retail sales could trigger a rotation back into cyclical sectors, underperforming Healthcare.; Hotter-than-expected CPI/PPI could drive yields higher, negatively impacting Gold. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 163.12 | 185.1 | 0.13474742520843552 | 1 |
| TAIWAN | Taiwan Equities | 102.18 | 107.8 | 0.055000978665100675 | 2 |
| MOMENTUM | US Momentum Equities | 307.32 | 322.07 | 0.04799557464532089 | 3 |
| SEMICONDUCTORS | Semiconductors | 569.41 | 594.07 | 0.04330798545863268 | 4 |
| ENERGY | Energy Sector | 60.18 | 62.58 | 0.039880358923230386 | 5 |
| OIL | Crude Oil | 125.92 | 130.29 | 0.03470457433290974 | 6 |
| UTILITIES | Utilities Sector | 43.13 | 44.18 | 0.02434500347785762 | 7 |
| JAPAN | Japan Equities | 96.05 | 98.17 | 0.022071837584591414 | 8 |
| TECHNOLOGY | Technology Sector | 186.32 | 190.32 | 0.021468441391155002 | 9 |
| BROAD_COMMODITIES | Broad Commodities | 17.83 | 18.21 | 0.021312394840157234 | 10 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.89 | 130.47 | 0.020173586676049737 | 11 |
| ETHEREUM_ETF | Ethereum ETF | 14.14 | 14.4 | 0.018387553041018467 | 12 |
| REGIONAL_BANKS | Regional Banks | 76.03 | 77.39 | 0.017887675917400925 | 13 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.5 | 73.69 | 0.01641379310344826 | 14 |
| SMALL_CAP | US Small-Cap Stocks | 299.98 | 304.06 | 0.013600906727115003 | 15 |
| NASDAQ100 | Nasdaq 100 | 720.87 | 729.87 | 0.012484914062174779 | 16 |
| MID_CAP | US Mid-Cap Stocks | 77.54 | 78.48 | 0.012122775341758985 | 17 |
| AGRICULTURE | Agriculture Commodities | 27.82 | 28.14 | 0.011502516175413424 | 18 |
| CANADA | Canada Equities | 61.5 | 62.18 | 0.011056910569105627 | 19 |
| REAL_ESTATE | Real Estate Sector | 44.4 | 44.83 | 0.009684684684684752 | 20 |
| SMALL_VALUE | US Small-Cap Value | 224.29 | 226.46 | 0.009674974363547362 | 21 |
| BIOTECH | Biotechnology | 158.03 | 159.53 | 0.009491868632538036 | 22 |
| INDUSTRIALS | Industrials Sector | 184.6 | 186.32 | 0.00931744312026006 | 23 |
| BROAD_AI_TECH | Broad AI Technology | 63.51 | 64.0 | 0.007715320421980865 | 24 |
| LARGE_GROWTH | US Large-Cap Growth | 124.17 | 125.08 | 0.007328662317790169 | 25 |
| GOLD | Gold | 82.51 | 83.11 | 0.007271845836868129 | 26 |
| BITCOIN_ETF | Bitcoin ETF | 36.23 | 36.42 | 0.005244272702180641 | 27 |
| METALS_MINING | Metals and Mining | 117.54 | 118.1 | 0.0047643355453461655 | 28 |
| EURO | Euro | 106.51 | 106.86 | 0.003286076424748874 | 29 |
| DIVIDEND | US Dividend Equities | 34.19 | 34.29 | 0.002924831822170182 | 30 |
| SILVER | Silver | 59.41 | 59.57 | 0.0026931493014643593 | 31 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.22 | 220.79 | 0.00258832077013893 | 32 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.48 | 79.61 | 0.0016356316054353393 | 33 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.92 | 93.05 | 0.0013990529487730718 | 34 |
| TOTAL_US_MARKET | Total US Stock Market | 381.63 | 382.13 | 0.0013101695359378773 | 35 |
| EMERGING_MARKETS | Emerging Markets | 60.33 | 60.39 | 0.0009945300845350946 | 36 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.76 | 92.84 | 0.0008624407072013174 | 37 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.48 | 91.55 | 0.0007651945780497993 | 38 |
| LOW_VOL | US Low Volatility Equities | 75.7 | 75.74 | 0.0005284015852047297 | 39 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 251.13 | 251.2 | 0.00027874009477169004 | 40 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.24 | 97.25 | 0.00010283833813251597 | 41 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 42 |
| SP500 | S&P 500 | 773.03 | 772.67 | -0.00046569990815359397 | 43 |
| TIPS | Treasury Inflation-Protected Securities | 106.86 | 106.77 | -0.0008422234699607678 | 44 |
| COPPER | Copper | 40.18 | 40.13 | -0.00124440019910399 | 45 |
| US_DOLLAR | US Dollar | 28.14 | 28.1 | -0.001421464108031234 | 46 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.84 | 94.7 | -0.001476170392239573 | 47 |
| YEN | Japanese Yen | 57.62 | 57.53 | -0.0015619576535924606 | 48 |
| EUROPE | Europe Equities | 92.26 | 92.1 | -0.001734229351831873 | 49 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.96 | 105.7 | -0.0024537561343902503 | 50 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.85 | 105.56 | -0.002739726027397138 | 51 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.79 | 47.65 | -0.0029294831554718126 | 52 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.95 | 84.68 | -0.0031783402001176464 | 53 |
| FINANCIALS | Financials Sector | 57.81 | 57.58 | -0.00397855042380213 | 54 |
| LARGE_VALUE | US Large-Cap Value | 258.31 | 256.62 | -0.006542526421741357 | 55 |
| UNITED_KINGDOM | United Kingdom Equities | 48.49 | 48.16 | -0.0068055269127655915 | 56 |
| HEALTHCARE | Healthcare Sector | 168.44 | 167.05 | -0.008252196627879238 | 57 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.06 | 81.35 | -0.008652205703144178 | 58 |
| COMMUNICATIONS | Communication Services Sector | 111.83 | 110.82 | -0.009031565769471617 | 59 |
| INDIA | India Equities | 50.14 | 49.58 | -0.011168727562824166 | 60 |
| AUSTRALIA | Australia Equities | 30.05 | 29.55 | -0.016638935108153063 | 61 |
| MATERIALS | Materials Sector | 53.18 | 52.24 | -0.01767581797668294 | 62 |
| SOLAR | Solar Energy | 51.86 | 50.92 | -0.018125723100655522 | 63 |
| SOUTH_AFRICA | South Africa Equities | 69.73 | 68.19 | -0.022085185716334554 | 64 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 119.67 | 116.75 | -0.024400434528286108 | 65 |
| MEXICO | Mexico Equities | 76.93 | 74.91 | -0.026257636812687002 | 66 |
| CYBERSECURITY | Cybersecurity | 100.6 | 97.79 | -0.02793240556660026 | 67 |
| SOFTWARE | Software | 105.01 | 101.99 | -0.028759165793734054 | 68 |
| CHINA | China Equities | 56.93 | 55.06 | -0.032847356402599615 | 69 |
| BRAZIL | Brazil Equities | 35.19 | 33.97 | -0.034668940039784046 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | GOLD | 30.0 | 0.007271845836868129 | 0.002181553751060439 | Elevated inflation (CPI 3.5% y/y), Fed on hold, unresolved Middle East conflict, and strong recent gold momentum (+7.2% 5-session) support safe-haven and real-asset demand into the CPI print. |
| anthropic-claude-fable-5 | ENERGY | 25.0 | 0.039880358923230386 | 0.009970089730807596 | Brent at $83.55 with Hormuz flows restricted; energy equities pulled back ~7% vs SPY last week despite strong prior trend (top quality-evidence score 0.834), offering a rebound setup with geopolitical support. |
| anthropic-claude-fable-5 | UNITED_KINGDOM | 20.0 | -0.0068055269127655915 | -0.0013611053825531183 | Strong prior relative trend with a recent pullback (quality score 0.838, highest ex-cash), value/dividend tilt benefits from sticky inflation and weakening dollar (UUP -1.0% over 21 sessions). |
| anthropic-claude-fable-5 | SP500 | 25.0 | -0.00046569990815359397 | -0.00011642497703839849 | Benchmark ballast at record highs with solid final private demand growth (3.9%); anchors the portfolio against hot-CPI equity risk. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | -0.00046569990815359397 | -0.00023284995407679698 | Broad US large-cap at record highs with strong week momentum; core position with lower single-cluster risk. |
| anthropic-claude-opus-4-8 | GOLD | 25.0 | 0.007271845836868129 | 0.0018179614592170323 | Gold surged 6.5% recently with weak payrolls and rate-cut hopes supporting real-rate declines; safe-haven amid Middle East conflict. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | -0.008252196627879238 | -0.0020630491569698095 | Defensive sector with strong recent 3-session return (+2.21%), negative SPY beta, low drawdown; hedge on soft labor backdrop. |
| anthropic-claude-opus-5 | SP500 | 40.0 | -0.00046569990815359397 | -0.0001862799632614376 | Core benchmark exposure at record highs with broad participation. |
| anthropic-claude-opus-5 | GOLD | 20.0 | 0.007271845836868129 | 0.0014543691673736259 | Safe-haven bid amid unresolved Hormuz conflict, elevated 3.3% core PCE, and softening payrolls; low correlation hedge. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | -0.008252196627879238 | -0.0016504393255758476 | Defensive sector with mid-pack quality score, near 52-week high, negative SPY beta offers diversification with positive drift. |
| anthropic-claude-opus-5 | TECHNOLOGY | 20.0 | 0.021468441391155002 | 0.004293688278231 | Leadership re-established with +3.69% 5s active after a prior-window drawdown; participates if melt-up continues. |
| google-gemini-3-1-pro | GOLD | 50.0 | 0.007271845836868129 | 0.0036359229184340647 | Gold has strong recent momentum and acts as a safe haven amid Middle East tensions and mixed economic data. |
| google-gemini-3-1-pro | HEALTHCARE | 50.0 | -0.008252196627879238 | -0.004126098313939619 | Healthcare offers defensive characteristics with positive recent momentum and solid quality evidence. |
| openai-gpt-5-5 | OIL | 25.0 | 0.03470457433290974 | 0.008676143583227436 | Direct crude exposure has the strongest one-week event support from unresolved Hormuz restrictions and a deep recent pullback despite a very strong prior active trend. |
| openai-gpt-5-5 | GOLD | 25.0 | 0.007271845836868129 | 0.0018179614592170323 | Gold has recent strength and potential support from geopolitical uncertainty and inflation-event risk, with lower equity-market dependence than SPY. |
| openai-gpt-5-5 | METALS_MINING | 20.0 | 0.0047643355453461655 | 0.0009528671090692332 | Metals and mining shows the strongest recent active move in the ledger, supported by broad commodity sensitivity and potential continuation if cyclical commodity appetite persists. |
| openai-gpt-5-5 | UNITED_KINGDOM | 15.0 | -0.0068055269127655915 | -0.0010208290369148386 | UK equities combine high quality evidence, strong prior active trend, low drawdown, and a recent pullback that may mean-revert if global value/defensive exposures recover. |
| openai-gpt-5-5 | HEALTHCARE | 15.0 | -0.008252196627879238 | -0.0012378294941818857 | Healthcare offers a defensive equity diversifier with positive short-term absolute momentum and lower SPY beta, useful if weak labor data weighs on broad cyclicals. |
| openai-gpt-5-6-sol | ENERGY | 40.0 | 0.039880358923230386 | 0.015952143569292154 | Unresolved restrictions on oil flows provide direct fundamental support after a sharp relative pullback, while sector quality evidence is exceptionally strong. |
| openai-gpt-5-6-sol | UNITED_KINGDOM | 35.0 | -0.0068055269127655915 | -0.002381934419467957 | Strong prior relative performance, a recent pullback, low volatility, and the highest equity-market quality score offer a favorable rebound setup. |
| openai-gpt-5-6-sol | LOW_VOL | 25.0 | 0.0005284015852047297 | 0.00013210039630118242 | Weak labor data and major inflation releases favor defensive exposure, while the recent relative pullback creates room for mean reversion. |
| xai-grok-4-3 | SP500 | 50.0 | -0.00046569990815359397 | -0.00023284995407679698 | Broad US equity exposure with base forecast supported by recent session gains despite labor data weakness. |
| xai-grok-4-3 | GOLD | 20.0 | 0.007271845836868129 | 0.0014543691673736259 | Safe-haven demand from unresolved Middle East conflict and recent 5-day return of 7.23%. |
| xai-grok-4-3 | JAPAN | 15.0 | 0.022071837584591414 | 0.003310775637688712 | Strong 3-day return of 2.42% and developed-market equity exposure outside US. |
| xai-grok-4-3 | HEALTHCARE | 15.0 | -0.008252196627879238 | -0.0012378294941818857 | Defensive sector with 2.21% 3-day return amid employment weakness. |
| xai-grok-4-5 | SP500 | 40.0 | -0.00046569990815359397 | -0.0001862799632614376 | Benchmark core holding given record close and broad positive asset share; no stronger diversified active edge clears hurdle cleanly after labor softness. |
| xai-grok-4-5 | GOLD | 25.0 | 0.007271845836868129 | 0.0018179614592170323 | Geopolitical oil-flow uncertainty and recent relative strength support short-horizon safe-haven bid above SPY base. |
| xai-grok-4-5 | ENERGY | 20.0 | 0.039880358923230386 | 0.007976071784646077 | High quality-evidence score plus supply-restriction facts give base case above SPY despite recent pullback. |
| xai-grok-4-5 | LARGE_VALUE | 15.0 | -0.006542526421741357 | -0.0009813789632612034 | Strong prior active rank, low vol, and shallow drawdown support modest outperformance versus growth-heavy SPY on data week. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | ENERGY | 3 | 0.58 | 0.039880358923230386 | 0.013702309546125379 | 0.014168009454278973 | 0.12104511566231015 |  | True | True |
| anthropic-claude-fable-5 | GOLD | 4 | 0.56 | 0.007271845836868129 | 0.010674113122276518 | 0.011139813030430112 | 0.124073312086159 |  | True | True |
| openai-gpt-5-5 | OIL | 5 | 0.55 | 0.03470457433290974 | 0.009188313620416977 | 0.00965401352857057 | 0.12555911158801855 |  | True | True |
| xai-grok-4-5 | SP500 | 4 | 0.58 | -0.00046569990815359397 | 0.008626374317340469 | 0.009092074225494063 | 0.12612105089109504 |  | True | True |
| anthropic-claude-opus-5 | SP500 | 4 | 0.5 | -0.00046569990815359397 | 0.003911338156767341 | 0.004377038064920935 | 0.1308360870516682 |  | True | True |
| xai-grok-4-3 | SP500 | 4 | 0.55 | -0.00046569990815359397 | 0.003294465356803655 | 0.003760165264957249 | 0.13145295985163186 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.5 | -0.00046569990815359397 | -0.00047793765182957415 | -1.2237743675980184e-05 | 0.1352253628602651 |  | False | False |
| google-gemini-3-1-pro | GOLD | 2 | 0.65 | 0.007271845836868129 | -0.0004901753955055543 | -2.4475487351960368e-05 | 0.13523760060394108 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 08e33a271550b6d4ed825be9166c7c31cd2f3d423463f2099d715ddd2517e6f7 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 1426ed067381a75370f08ff821c270abe624f586660ca9394ef52d8fbf40e86b |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 2a8c66495be82da317ab5e80fc2842516d9dd57c66020472482043baa19399ac |
| market_data/universe_decision_context.md | 03175a2b62547b3ebf6c82685a61d915ab9e544e1243fa50a862bdb3453b2720 |
| market_data/universe_decision_context.json | 3f744f5f0bfc648fcad06cbee3b9aed246abdd08a38e85e5a0e8a6e2b8cc002e |
| market_data/decision_context_source_history.json | ba4ab086e5ee6a9d211b43feb61760bdcd3b524672e73db2745858fae9d35348 |
| market_data/universe_quality_evidence.md | 9d6ddad24d70a4923fef2c54f4017b89ad76eb66d64e1ceb771513e0596e933b |
| market_data/universe_quality_evidence.json | 8197b13ee6a5abc5a521ad748c3eea4ae59dfb141e129d4e80171bb0909726e1 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | ae06ddff3779869ca8e56f95dccb5fedec4c9cf4a535c906db7bfd15b26b02e2 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 0e96c84114b3e1c9cc168efa3898ea87c1ca86b7d2cfed5e9de6c3301f21c358 | yes |
| Final briefing | research/final_briefing.md | model-facing | 08e33a271550b6d4ed825be9166c7c31cd2f3d423463f2099d715ddd2517e6f7 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
