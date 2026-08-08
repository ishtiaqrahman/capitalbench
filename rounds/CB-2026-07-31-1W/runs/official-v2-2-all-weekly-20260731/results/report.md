# CapitalBench Report: CB-2026-07-31-1W / official-v2-2-all-weekly-20260731

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260731
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-31-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-31
- Decision deadline: 2026-08-03T12:30:00Z
- Horizon: one week
- Entry date: 2026-07-31
- Exit date: 2026-08-07
- Entry rule: Use the Friday, July 31, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Friday, August 7, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.52 | SPY base forecast of 0.6% used as hurdle; portfolio expected return equals benchmark with zero alpha. | July employment data surprise on August 7; Continued 10-year yield rise above 4.8%; Geopolitical developments around Strait of Hormuz |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.5 | Balanced SPY core with two international tilts showing recent positive relative strength. | Weak August 7 payrolls could trigger broad equity drawdown; China rebound may reverse quickly given high volatility; Rising 10-year yields pressure equities |
| xai-grok-4-5 | xai | portfolio | SOFTWARE | 4 | 0.58 | Selected holdings clear the SPY base hurdle on supplied relative trends and briefing catalysts; equal-weight style avoided due to weaker recent breadth. Expected alpha driven by non-benchmark exposures under 50% per cluster. | July employment report August 7 could trigger broad risk-off if weak; Hormuz de-escalation statements reverse energy and commodity gains; Tech earnings follow-through fails after AMD; Rising Treasury yields pressure growth and EM simultaneously |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.5 | Modest tilt away from crowded mega-cap tech into energy, healthcare, and Europe while holding 40% SPY, targeting small positive alpha with contained tracking error. | A confirmed Iran agreement and Hormuz reopening could sharply cut oil and energy equities; Hot payrolls or higher yields could hit defensives and Europe more than SPY; Mega-cap tech continuation would leave SPY ahead of this diversified mix; Eli Lilly earnings disappointment drags healthcare |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | A balanced approach combining core equities with commodities for potential upside and diversification. | Geopolitical tensions de-escalating, leading to a drop in oil and gold prices.; A stronger-than-expected employment report causing a spike in interest rates and a broad market sell-off.; Unexpected shifts in OPEC+ production policy impacting oil prices. |
| anthropic-claude-fable-5 | anthropic | portfolio | CONSUMER_DISCRETIONARY | 4 | 0.55 | Tilt toward earnings momentum (XLY), supply-driven energy strength, and China relative momentum, funded away from expensive mega-cap growth after mixed reactions (Apple -7.4%, Meta margin compression). | An Iran/Hormuz agreement could collapse oil prices and energy equities; Hot July payrolls or inflation could push 10y yields above 4.8%, pressuring all equities; Amazon-driven XLY gains may mean-revert after the 15% pop; China policy or geopolitical headlines can reverse momentum quickly |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 4 | 0.59 | Energy supply disruption, resilient UK and China relative trends, and agriculture's high-quality pullback setup offer better one-week base cases than SPY. Diversification reduces dependence on a single macro outcome. | A credible Hormuz reopening agreement could sharply reverse oil and energy exposure.; The August 7 employment report could lift yields and favor US mega-cap equities over the portfolio.; China policy or geopolitical disappointment could reverse recent relative strength.; Commodity pullbacks may persist despite strong prior trends. |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.57 | Base case expects commodity-linked and value/international exposures to outperform SPY over the one-week window. The main edge is near-term event risk in oil supply plus cross-sectional quality in agriculture and large value. | A confirmed Strait of Hormuz reopening or Middle East de-escalation could reverse oil and energy exposure quickly.; August 7 employment data or other U.S. macro releases could trigger broad risk-off and hurt equities and commodities together.; A mega-cap technology rebound could lift SPY more than the selected value, China, and commodity exposures.; Commodity positions may be volatile and can reverse despite favorable prior trend and pullback evidence. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| METALS_MINING | Metals and Mining | 100.65 | 115.74 | 0.1499254843517137 | 1 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 115.07 | 127.85 | 0.11106283132006611 | 2 |
| SILVER | Silver | 52.36 | 57.5 | 0.09816653934301 | 3 |
| SOUTH_AFRICA | South Africa Equities | 63.62 | 69.6500015258789 | 0.09478153923104227 | 4 |
| SOFTWARE | Software | 94.58 | 102.69 | 0.08574751533093683 | 5 |
| SEMICONDUCTORS | Semiconductors | 540.53 | 582.7 | 0.0780160213124157 | 6 |
| BROAD_AI_TECH | Broad AI Technology | 58.89 | 63.35 | 0.07573442010528098 | 7 |
| GOLD | Gold | 76.17 | 81.68 | 0.07233819088880145 | 8 |
| TECHNOLOGY | Technology Sector | 175.35 | 187.97 | 0.07197034502423727 | 9 |
| BIOTECH | Biotechnology | 147.01 | 157.37 | 0.0704713965036392 | 10 |
| SOLAR | Solar Energy | 49.33 | 52.75 | 0.06932900871680525 | 11 |
| TAIWAN | Taiwan Equities | 96.55 | 103.08999633789062 | 0.06773688594397331 | 12 |
| CYBERSECURITY | Cybersecurity | 91.83 | 97.85 | 0.06555591854513776 | 13 |
| SOUTH_KOREA | South Korea Equities | 157.1 | 166.08999633789062 | 0.05722467433412248 | 14 |
| LARGE_GROWTH | US Large-Cap Growth | 118.32 | 124.6 | 0.05307640297498306 | 15 |
| NASDAQ100 | Nasdaq 100 | 687.99 | 723.03 | 0.05093097283390735 | 16 |
| JAPAN | Japan Equities | 92.39 | 96.9 | 0.04881480679727246 | 17 |
| MATERIALS | Materials Sector | 50.43 | 52.86 | 0.04818560380725767 | 18 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.66 | 250.75 | 0.046273888008011355 | 19 |
| TOTAL_US_MARKET | Total US Stock Market | 368.21 | 381.78 | 0.036853969202357284 | 20 |
| AUSTRALIA | Australia Equities | 29.34 | 30.40999984741211 | 0.03646897912106706 | 21 |
| SMALL_CAP | US Small-Cap Stocks | 291.2 | 301.56 | 0.03557692307692317 | 22 |
| SP500 | S&P 500 | 747.03 | 773.26 | 0.03511237835160563 | 23 |
| MID_CAP | US Mid-Cap Stocks | 75.27 | 77.79 | 0.03347947389398187 | 24 |
| BITCOIN_ETF | Bitcoin ETF | 35.64 | 36.79999923706055 | 0.03254767780753487 | 25 |
| MOMENTUM | US Momentum Equities | 299.59 | 309.32 | 0.03247771955005185 | 26 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.09 | 119.86 | 0.03247480403135494 | 27 |
| CANADA | Canada Equities | 59.39 | 61.29999923706055 | 0.03216028349992506 | 28 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.62 | 72.89 | 0.03214386859246665 | 29 |
| INDUSTRIALS | Industrials Sector | 179.84 | 185.18 | 0.029693060498220625 | 30 |
| EMERGING_MARKETS | Emerging Markets | 58.75 | 60.47 | 0.029276595744680778 | 31 |
| ETHEREUM_ETF | Ethereum ETF | 14.07 | 14.470000267028809 | 0.02842930113921871 | 32 |
| COMMUNICATIONS | Communication Services Sector | 108.24 | 111.25 | 0.02780857354028088 | 33 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.01 | 220.09 | 0.023626808055439374 | 34 |
| LARGE_VALUE | US Large-Cap Value | 251.82 | 257.56 | 0.02279405924866973 | 35 |
| EUROPE | Europe Equities | 90.59 | 92.6 | 0.02218787945689349 | 36 |
| SMALL_VALUE | US Small-Cap Value | 221.24 | 225.52 | 0.0193455071415658 | 37 |
| HEALTHCARE | Healthcare Sector | 162.55 | 165.68 | 0.01925561365733608 | 38 |
| CHINA | China Equities | 55.8 | 56.57 | 0.013799283154121822 | 39 |
| DIVIDEND | US Dividend Equities | 33.47 | 33.9 | 0.012847325963549538 | 40 |
| FINANCIALS | Financials Sector | 56.94 | 57.6 | 0.011591148577450028 | 41 |
| INDIA | India Equities | 49.8 | 50.365 | 0.011345381526104426 | 42 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.2486006307 | 95.23999786376953 | 0.010518959713303078 | 43 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.9206290358 | 82.76 | 0.010246148913641617 | 44 |
| YEN | Japanese Yen | 57.66 | 58.2400016784668 | 0.010058995464217846 | 45 |
| MEXICO | Mexico Equities | 76.81 | 77.5199966430664 | 0.009243544370087342 | 46 |
| COPPER | Copper | 39.56 | 39.900001525878906 | 0.00859457851058898 | 47 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.5791824007 | 93.2699966430664 | 0.007461874521384582 | 48 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.7937905745 | 106.55 | 0.007147956618186235 | 49 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.09674431 | 79.61 | 0.006488961011952954 | 50 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.6519657621 | 47.95000076293945 | 0.0062544114617932856 | 51 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.0332191064 | 97.6 | 0.005841101622924727 | 52 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.6330904413 | 93.17 | 0.005796088159665036 | 53 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.3539627423 | 105.94000244140625 | 0.005562578605037727 | 54 |
| UNITED_KINGDOM | United Kingdom Equities | 48.41 | 48.63999938964844 | 0.004751071878711821 | 55 |
| AGRICULTURE | Agriculture Commodities | 27.51 | 27.6200008392334 | 0.00399857648976365 | 56 |
| EURO | Euro | 106.4070307736 | 106.68000030517578 | 0.0025653336024060724 | 57 |
| TIPS | Treasury Inflation-Protected Securities | 106.8457208135 | 107.08 | 0.002192686658073484 | 58 |
| REGIONAL_BANKS | Regional Banks | 76.06 | 76.20999908447266 | 0.0019721152310367973 | 59 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.05 | 85.12 | 0.0008230452674897748 | 60 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.4070875525 | 91.48 | 0.0007976673303164983 | 61 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 62 |
| LOW_VOL | US Low Volatility Equities | 76.23 | 76.21 | -0.00026236389872769106 | 63 |
| REAL_ESTATE | Real Estate Sector | 45.07 | 44.98 | -0.001996893720878745 | 64 |
| US_DOLLAR | US Dollar | 28.17 | 28.06999969482422 | -0.0035498865877097163 | 65 |
| UTILITIES | Utilities Sector | 44.35 | 43.61 | -0.01668545659526499 | 66 |
| BROAD_COMMODITIES | Broad Commodities | 17.56 | 17.25 | -0.01765375854214113 | 67 |
| ENERGY | Energy Sector | 59.55 | 57.5 | -0.034424853064651484 | 68 |
| BRAZIL | Brazil Equities | 36.65 | 35.34000015258789 | -0.03574351561833855 | 69 |
| OIL | Crude Oil | 129.17 | 117.9800033569336 | -0.08662999646254077 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | CONSUMER_DISCRETIONARY | 30.0 | 0.03247480403135494 | 0.009742441209406483 | Amazon +15.3% on strong results (sales +20%, AWS +37%) anchors the sector with post-earnings drift potential. |
| anthropic-claude-fable-5 | CHINA | 25.0 | 0.013799283154121822 | 0.0034498207885304555 | Positive relative momentum (+3.5% 5-day active, +4.4% prior active), Q2 GDP 4.3% y/y, modest drawdown and 15% below 52w high. |
| anthropic-claude-fable-5 | ENERGY | 25.0 | -0.034424853064651484 | -0.008606213266162871 | Brent $87.93 with 9.4 mb/d supply shortfall from war; XLE equities lag the oil move with lower volatility than USO. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | 0.02279405924866973 | 0.004558811849733946 | Steady prior active trend (+2.7%), near 52w high, low volatility ballast in an elevated-rate environment. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | 0.03511237835160563 | 0.017556189175802817 | Broad large-cap exposure with positive weekly momentum and strong mega-cap earnings from Amazon, Microsoft, Meta. |
| anthropic-claude-opus-4-8 | CHINA | 25.0 | 0.013799283154121822 | 0.0034498207885304555 | Strongest recent active return (+3.54% 5s) with deep 52w drawdown, GDP growth 4.3% supports rebound. |
| anthropic-claude-opus-4-8 | EUROPE | 25.0 | 0.02218787945689349 | 0.005546969864223372 | Positive active return (+1.37% 5s), low drawdown, near 52w high, stable ECB policy. |
| anthropic-claude-opus-5 | SP500 | 40.0 | 0.03511237835160563 | 0.014044951340642254 | Benchmark core given elevated macro uncertainty and a heavy data week. |
| anthropic-claude-opus-5 | ENERGY | 20.0 | -0.034424853064651484 | -0.0068849706129302975 | Strong prior relative trend with supply still 9.4 mb/d below pre-war levels and unresolved Hormuz situation; negative SPY beta diversifies. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | 0.01925561365733608 | 0.003851122731467216 | Defensive sector with positive prior active return, low drawdown, and a major catalyst in Eli Lilly results. |
| anthropic-claude-opus-5 | EUROPE | 20.0 | 0.02218787945689349 | 0.004437575891378698 | Positive 5-day active return, low volatility, near 52-week high, ECB on hold with contained core inflation. |
| google-gemini-3-1-pro | SP500 | 50.0 | 0.03511237835160563 | 0.017556189175802817 | Core equity exposure with solid recent performance and broad diversification. |
| google-gemini-3-1-pro | OIL | 25.0 | -0.08662999646254077 | -0.021657499115635193 | Strong recent momentum and geopolitical tensions supporting prices. |
| google-gemini-3-1-pro | GOLD | 25.0 | 0.07233819088880145 | 0.01808454772220036 | Safe-haven asset amid geopolitical uncertainty and potential for rate cuts. |
| openai-gpt-5-5 | OIL | 25.0 | -0.08662999646254077 | -0.021657499115635193 | Crude has the clearest one-week event risk: large supply disruption remains unresolved despite reported U.S. de-escalation comments, while the quality table shows top prior trend and pullback ranks. |
| openai-gpt-5-5 | ENERGY | 25.0 | -0.034424853064651484 | -0.008606213266162871 | Energy equities provide related but less direct exposure to tight oil conditions, supported by strong prior active return and high quality evidence while respecting the 50% energy cluster cap. |
| openai-gpt-5-5 | AGRICULTURE | 20.0 | 0.00399857648976365 | 0.0007997152979527301 | Agriculture has the highest quality evidence score in the supplied table, low SPY beta, and a meaningful prior active trend with recent pullback, giving diversifying alpha potential. |
| openai-gpt-5-5 | CHINA | 15.0 | 0.013799283154121822 | 0.002069892473118273 | China combines positive prior and recent active returns with modest SPY beta, giving international equity upside that is less directly tied to U.S. large-cap positioning. |
| openai-gpt-5-5 | LARGE_VALUE | 15.0 | 0.02279405924866973 | 0.0034191088873004594 | Large value offers a lower-volatility U.S. equity tilt with strong prior active return and shallow drawdown, useful if the week favors breadth and defensives over mega-cap growth. |
| openai-gpt-5-6-sol | ENERGY | 30.0 | -0.034424853064651484 | -0.010327455919395444 | Strong prior relative trend and constrained global supply support energy equities, while the smaller allocation reflects acute geopolitical reversal risk. |
| openai-gpt-5-6-sol | CHINA | 25.0 | 0.013799283154121822 | 0.0034498207885304555 | Positive short- and prior-window relative performance provides a continuation setup, tempered by weak recent-pullback evidence and policy risk. |
| openai-gpt-5-6-sol | UNITED_KINGDOM | 25.0 | 0.004751071878711821 | 0.0011877679696779553 | Positive recent and prior relative returns, moderate volatility, and shallow drawdown offer a comparatively stable international-equity trend. |
| openai-gpt-5-6-sol | AGRICULTURE | 20.0 | 0.00399857648976365 | 0.0007997152979527301 | The highest quality score and strong prior trend create a pullback-rebound setup with low SPY correlation. |
| xai-grok-4-3 | SP500 | 100.0 | 0.03511237835160563 | 0.03511237835160563 | No active holding clears the base-forecast hurdle above SPY; SPY is the benchmark proxy with neutral-to-positive near-term momentum from recent breadth data. |
| xai-grok-4-5 | SOFTWARE | 30.0 | 0.08574751533093683 | 0.025724254599281047 | Strong recent relative performance and software exposure supported by large-cap tech earnings momentum into the short window. |
| xai-grok-4-5 | CHINA | 25.0 | 0.013799283154121822 | 0.0034498207885304555 | Positive prior active trend and recent outperformance versus SPY with China GDP data already released. |
| xai-grok-4-5 | ENERGY | 25.0 | -0.034424853064651484 | -0.008606213266162871 | Elevated oil prices from supply disruption and strong prior active return support energy equities over the week. |
| xai-grok-4-5 | COPPER | 20.0 | 0.00859457851058898 | 0.0017189157021177959 | Positive active returns and industrial demand linkage with China growth backdrop. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 1 | 0.52 | 0.03511237835160563 | 0.03511237835160563 | 0.0 | 0.11481310600010808 |  | False | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.5 | 0.03511237835160563 | 0.026552979828556644 | -0.008559398523048989 | 0.12337250452315707 |  | False | True |
| xai-grok-4-5 | SOFTWARE | 4 | 0.58 | 0.08574751533093683 | 0.022286777823766427 | -0.012825600527839206 | 0.1276387065279473 |  | False | True |
| anthropic-claude-opus-5 | SP500 | 4 | 0.5 | 0.03511237835160563 | 0.01544867935055787 | -0.019663699001047762 | 0.13447680500115583 |  | False | True |
| google-gemini-3-1-pro | SP500 | 3 | 0.65 | 0.03511237835160563 | 0.013983237782367985 | -0.021129140569237648 | 0.13594224656934573 |  | False | True |
| anthropic-claude-fable-5 | CONSUMER_DISCRETIONARY | 4 | 0.55 | 0.03247480403135494 | 0.009144860581508013 | -0.02596751777009762 | 0.1407806237702057 |  | False | True |
| openai-gpt-5-6-sol | ENERGY | 4 | 0.59 | -0.034424853064651484 | -0.004890151863234304 | -0.04000253021483994 | 0.154815636214948 |  | False | False |
| openai-gpt-5-5 | OIL | 5 | 0.57 | -0.08662999646254077 | -0.0239749957234266 | -0.05908737407503223 | 0.1739004800751403 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 2266cf2a241a540af510065b6d6dd359e82ea50c57521d82007d6fd87f4da197 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 296569157edb01824029dfaeb1df82b756a157bf48bdb0081cb2024d6cefd476 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 3fc072dfc8635ac5f743433db1f8bbfb56ba65fde78604fe5be5c329b66985e1 |
| market_data/universe_decision_context.md | cb90fa9b59ded50ab5775c7b3fc51705702d9f201896cd4978de9f5071a2ba4e |
| market_data/universe_decision_context.json | 9c90d67fa3be6561463b91a8b921654ba73f287ba1510db887d1c84e30a3b2a3 |
| market_data/decision_context_source_history.json | e496a6c0e751078d730b4b2fdedf768e27a8fd4529bf826667a3fb4bb7b27745 |
| market_data/universe_quality_evidence.md | 5e3ceeccf920ee99581b5aa30f7b9961dea1bbeaf0e83f59951e24d135835be8 |
| market_data/universe_quality_evidence.json | ba988c2ff5d290710000695c99c305f5272d8827b4847c14921a9415fad61e44 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 6c3be88f44053a8538070524627e12862f0afddaae0b0dc3cbfdb18817d7de44 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 4303ade3d2e1bf0e4f8425180050ec0d993c77fa72ad9cd5b9c1ea64691ea9f3 | yes |
| Final briefing | research/final_briefing.md | model-facing | 2266cf2a241a540af510065b6d6dd359e82ea50c57521d82007d6fd87f4da197 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
