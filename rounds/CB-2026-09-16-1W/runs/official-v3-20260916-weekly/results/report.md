# CapitalBench Report: CB-2026-09-16-1W / official-v3-20260916-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260916-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-16-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-16
- Decision deadline: 2026-09-17T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-17
- Exit date: 2026-09-24
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | Hawkish unanimous 25bp hike with higher 2026 inflation and funds-rate medians, weak 5-session breadth (14.5% positive), and only 2.37% active-return dispersion favor the benchmark over high-beta shock names for a one-week window. | Further USD strength after the hike can keep high-beta EM, metals, and crypto lagging SPY; Brent's 2.7% drop can reverse USO's prior-window strength inside the scoring week; September 17-18 claims, housing, and industrial production prints can reprice rates and cyclicals before the September 24 exit |
| openai-gpt-6-astra | openai | portfolio | SOUTH_KOREA | 3 | 0.5633 | Only 14.49% of assets have positive five-session returns, with 2.37 percentage points of active-return dispersion. The Fed hike, higher inflation projections and stronger dollar provide substantive reasons for weakness, not a blanket reversal signal. Nevertheless, resilient spending and capital investment argue against treating the largest industrial-demand-sensitive pullbacks as evidence of collapsing demand. Selective reversals have a modest edge, with substantial uncertainty and no assumption that pre-entry rebounds remain available after September 17. | Further upward repricing of US rates and the dollar could overwhelm reversal demand across all three leading candidates.; Korea, copper and mining share global cyclical exposure, so their losses could be strongly correlated despite different instruments.; The September 17 entry close may already incorporate the Korean rebound and post-Fed stabilization, leaving less subsequent upside.; Industrial production on September 18 and new-home sales on September 24 could undermine the resilient-demand thesis; their results are unknown. |
| anthropic-claude-opus-5 | anthropic | portfolio | SOUTH_KOREA | 3 | 0.57 | The Fed hiked to 3.75-4.00% with elevated inflation and a higher projected year-end path, lifting the dollar and pressuring long-duration, precious metals and high-beta cyclicals. Breadth is weak (14% of assets positive over 5 sessions) and dispersion is moderate at 2.37%. The sharp one-week hits to metals/mining, silver, copper, South Korea and South Africa came after solid prior-window relative trends, which fits a policy-shock overreaction more than fundamental deterioration; a partial mean-reversion into a data-light week is plausible but far from certain, so only a few candidates clear the bar. | A further hawkish repricing strengthens the dollar and extends the selloff in metals and EM equities; High-beta selections (EWY beta 3.24) magnify losses if US equities keep falling into the Sept 24 close; Sept 17 jobless claims, housing starts and Philly Fed, plus Sept 24 new-home sales, could shift rate expectations mid-window; Commodity weakness (Brent -2.7%) may reflect demand deterioration rather than temporary overreaction |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SOUTH_KOREA | 3 | 0.56 | Hawkish surprise: Fed hiked 25bp to 3.75-4.00% with 10y at 5.01% and dollar up 1.5% over five sessions; SPY down 2.4% over 21 sessions with only 14% of assets positive. Strong-dollar, higher-rate regime pressured metals, EM, and crypto in the latest window, but the Kospi rose 1.4% on Sep 16 and Europe/Asia rose broadly, suggesting some of the sharp EM/metals selloff is positioning rather than fundamental. Oil remains supported by prior trend but Brent fell 2.7%. Edge is modest; most candidates near coin-flip versus SPY. | Continued dollar strength after the Fed hike extends EM and commodity underperformance; High-beta candidates (EWY beta 3.2, XME beta 1.6) amplify any further US equity drawdown; Jobless claims, housing, and industrial production releases could shift rate expectations mid-window; Copper and mining reversal fails if the prior window's selloff reflects genuine China-linked demand weakness |
| xai-grok-4-3 | xai | portfolio | YEN | 3 | 0.565 | Rate hike amid resilient demand favors defensive and commodity continuation while equity pullbacks show limited reversal support within one week. | Further equity weakness from rate hike; Commodity volatility from Brent decline; Limited reversal confirmation within one week |
| xai-grok-4-5 | xai | portfolio | COPPER | 3 | 0.6 | Post-hike risk-off with hawkish dots, resilient demand but elevated inflation; low positive-asset share and modest dispersion favor selective mean-reversion in high-quality pullbacks over pure continuation or broad beta. | Further upside in yields from hawkish 2026 dots could pressure cyclicals and EM; Oil/commodity mean-reversion if demand data softens on scheduled releases; High-beta names (Korea, crypto, solar) can extend losses on risk-off; Volume spikes in munis/Australia may reflect flow noise not durable edge |
| google-gemini-3-1-pro | google | portfolio | METALS_MINING | 3 | 0.58 | The FOMC raised rates by 25 bps to 3.75%-4.00%, citing solid economic expansion and elevated inflation. Retail sales and import/export prices showed strength. Equities have pulled back recently, while oil has rallied. The environment suggests a mix of rate-driven defensive positioning and potential reversals in oversold cyclical areas. | Continued hawkishness from the Fed could pressure cyclical and emerging market assets.; A stronger US dollar could negatively impact international equities and commodities. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BITCOIN_ETF | Bitcoin ETF | 43.3 | 47.81 | 0.10415704387990776 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 18.47 | 20.33 | 0.10070384407146715 | 2 |
| SEMICONDUCTORS | Semiconductors | 560.61 | 600.52 | 0.07119031055457437 | 3 |
| MOMENTUM | US Momentum Equities | 306.12 | 317.45 | 0.03701162942636871 | 4 |
| TECHNOLOGY | Technology Sector | 188.06 | 194.71 | 0.035361054982452345 | 5 |
| NASDAQ100 | Nasdaq 100 | 716.92 | 741.1 | 0.0337276125648609 | 6 |
| LARGE_GROWTH | US Large-Cap Growth | 122.53 | 125.62 | 0.025218313882314547 | 7 |
| BROAD_AI_TECH | Broad AI Technology | 64.37 | 65.98 | 0.025011651390399292 | 8 |
| COPPER | Copper | 39.66 | 40.65 | 0.024962178517397904 | 9 |
| TAIWAN | Taiwan Equities | 110.64 | 113.08 | 0.022053506869124995 | 10 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.52 | 124.88 | 0.019262161279790968 | 11 |
| CYBERSECURITY | Cybersecurity | 101.66 | 103.19 | 0.015050167224080369 | 12 |
| COMMUNICATIONS | Communication Services Sector | 112.35 | 113.99 | 0.014597240765465092 | 13 |
| SOFTWARE | Software | 105.78 | 107.15 | 0.012951408583853352 | 14 |
| US_DOLLAR | US Dollar | 28.38 | 28.69 | 0.010923185341790154 | 15 |
| TOTAL_US_MARKET | Total US Stock Market | 375.34 | 378.08 | 0.0073000479565195064 | 16 |
| HEALTHCARE | Healthcare Sector | 168.81 | 169.87 | 0.006279248859664799 | 17 |
| SP500 | S&P 500 | 762.6 | 767.18 | 0.006005769735116573 | 18 |
| AGRICULTURE | Agriculture Commodities | 28.42 | 28.55 | 0.004574243490499619 | 19 |
| BROAD_COMMODITIES | Broad Commodities | 19.71 | 19.8 | 0.004566210045662045 | 20 |
| CHINA | China Equities | 52.67 | 52.82 | 0.0028479210176570735 | 21 |
| SOUTH_KOREA | South Korea Equities | 182.39 | 182.53 | 0.0007675859422118236 | 22 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.53 | 91.58 | 0.0005462689828470424 | 23 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 24 |
| EMERGING_MARKETS | Emerging Markets | 59.91 | 59.87 | -0.0006676681689200548 | 25 |
| INDUSTRIALS | Industrials Sector | 169.01 | 168.83 | -0.0010650257381218386 | 26 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.11 | 46.895 | -0.004563786881765952 | 27 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 213.88 | 212.76 | -0.005236581260519957 | 28 |
| MID_CAP | US Mid-Cap Stocks | 73.21 | 72.73 | -0.006556481355005972 | 29 |
| LARGE_VALUE | US Large-Cap Value | 252.82 | 250.76 | -0.008148089549877446 | 30 |
| EURO | Euro | 105.91 | 104.9892 | -0.008694174298933044 | 31 |
| INDIA | India Equities | 48.01 | 47.56 | -0.009373047281816205 | 32 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 111.39 | 110.32 | -0.009605889218062713 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.72 | 77.89 | -0.010543699186991828 | 34 |
| SMALL_CAP | US Small-Cap Stocks | 285.43 | 281.66 | -0.013208142101390874 | 35 |
| TIPS | Treasury Inflation-Protected Securities | 105.71 | 104.3 | -0.013338378582915533 | 36 |
| BIOTECH | Biotechnology | 158.25 | 156.05 | -0.013902053712480211 | 37 |
| OIL | Crude Oil | 155.31 | 153.09 | -0.014293992659841548 | 38 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.31 | 210.26 | -0.014298438891753862 | 39 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.33 | 94.95 | -0.014325755216443414 | 40 |
| EUROPE | Europe Equities | 89.37 | 88.07 | -0.014546268322703448 | 41 |
| MUNICIPAL_BONDS | Municipal Bonds | 103.16 | 101.59 | -0.015219077161690464 | 42 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.15 | 71.05 | -0.015246015246015321 | 43 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.66 | 92.18 | -0.01580183642963906 | 44 |
| CANADA | Canada Equities | 60.41 | 59.44 | -0.016056944214533964 | 45 |
| UNITED_KINGDOM | United Kingdom Equities | 47.95 | 47.16 | -0.016475495307612276 | 46 |
| SMALL_VALUE | US Small-Cap Value | 216.73 | 213.12 | -0.01665666958888934 | 47 |
| GOLD | Gold | 81.69 | 80.3 | -0.01701554657852855 | 48 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 91.25 | 89.69 | -0.017095890410958936 | 49 |
| YEN | Japanese Yen | 58.76 | 57.68 | -0.018379850238257278 | 50 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.16 | 103.15 | -0.0191137314568276 | 51 |
| MATERIALS | Materials Sector | 50.71 | 49.68 | -0.0203115756261093 | 52 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.81 | 89.86 | -0.02123951639254984 | 53 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.49 | 81.7 | -0.02143969337645213 | 54 |
| JAPAN | Japan Equities | 97.91 | 95.81 | -0.02144826881830242 | 55 |
| BRAZIL | Brazil Equities | 37.74 | 36.91 | -0.02199258081611033 | 56 |
| SILVER | Silver | 58.97 | 57.62 | -0.02289299643886722 | 57 |
| DIVIDEND | US Dividend Equities | 33.89 | 33.1 | -0.023310711124225447 | 58 |
| MEXICO | Mexico Equities | 74.29 | 72.51 | -0.02396015614483782 | 59 |
| FINANCIALS | Financials Sector | 55.88 | 54.53 | -0.024158911954187623 | 60 |
| REGIONAL_BANKS | Regional Banks | 72.74 | 70.94 | -0.024745669507836077 | 61 |
| LOW_VOL | US Low Volatility Equities | 73.06 | 71.11 | -0.026690391459074814 | 62 |
| AUSTRALIA | Australia Equities | 29.13 | 28.31 | -0.02814967387572953 | 63 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.78 | 79.42 | -0.028857911469796993 | 64 |
| ENERGY | Energy Sector | 64.48 | 62.6 | -0.029156327543424343 | 65 |
| REAL_ESTATE | Real Estate Sector | 42.94 | 41.65 | -0.030041918956683733 | 66 |
| METALS_MINING | Metals and Mining | 111.32 | 107.96 | -0.030183255479698134 | 67 |
| SOUTH_AFRICA | South Africa Equities | 68.69 | 65.9 | -0.04061726597758031 | 68 |
| UTILITIES | Utilities Sector | 41.69 | 39.36 | -0.05588870232669696 | 69 |
| SOLAR | Solar Energy | 46.36 | 43.47 | -0.06233822260569455 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SOUTH_KOREA | 35.0 | 0.0007675859422118236 | 0.00026865507977413827 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | COPPER | 35.0 | 0.024962178517397904 | 0.008736762481089266 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SOUTH_AFRICA | 30.0 | -0.04061726597758031 | -0.012185179793274091 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SOUTH_KOREA | 35.0 | 0.0007675859422118236 | 0.00026865507977413827 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | COPPER | 35.0 | 0.024962178517397904 | 0.008736762481089266 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SOUTH_AFRICA | 30.0 | -0.04061726597758031 | -0.012185179793274091 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| google-gemini-3-1-pro | METALS_MINING | 35.0 | -0.030183255479698134 | -0.010564139417894346 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOUTH_KOREA | 35.0 | 0.0007675859422118236 | 0.00026865507977413827 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | YEN | 30.0 | -0.018379850238257278 | -0.005513955071477184 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | SOUTH_KOREA | 35.0 | 0.0007675859422118236 | 0.00026865507977413827 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | COPPER | 35.0 | 0.024962178517397904 | 0.008736762481089266 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | METALS_MINING | 30.0 | -0.030183255479698134 | -0.00905497664390944 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | YEN | 35.0 | -0.018379850238257278 | -0.006432947583390047 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | MUNICIPAL_BONDS | 35.0 | -0.015219077161690464 | -0.005326677006591662 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 30.0 | 0.006005769735116573 | 0.0018017309205349717 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | COPPER | 35.0 | 0.024962178517397904 | 0.008736762481089266 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | SOUTH_AFRICA | 35.0 | -0.04061726597758031 | -0.014216043092153107 | V3 selected model rank 2: overreaction with 60% estimated probability of beating SPY. |
| xai-grok-4-5 | METALS_MINING | 30.0 | -0.030183255479698134 | -0.00905497664390944 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.006005769735116573 | 0.006005769735116573 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.006005769735116573 | 0.006005769735116573 | 0.0 | 0.09815127414479119 |  | False | True |
| openai-gpt-6-astra | SOUTH_KOREA | 3 | 0.5633 | 0.0007675859422118236 | -4.955908304603643e-05 | -0.006055328818162609 | 0.1042066029629538 |  | False | False |
| anthropic-claude-opus-5 | SOUTH_KOREA | 3 | 0.57 | 0.0007675859422118236 | -0.003179762232410687 | -0.00918553196752726 | 0.10733680611231845 |  | False | False |
| anthropic-claude-fable-5-1 | SOUTH_KOREA | 3 | 0.56 | 0.0007675859422118236 | -0.003179762232410687 | -0.00918553196752726 | 0.10733680611231845 |  | False | False |
| xai-grok-4-3 | YEN | 3 | 0.565 | -0.018379850238257278 | -0.009957893669446737 | -0.01596366340456331 | 0.1141149375493545 |  | False | False |
| xai-grok-4-5 | COPPER | 3 | 0.6 | 0.024962178517397904 | -0.014534257254973282 | -0.020540026990089853 | 0.11869130113488105 |  | False | False |
| google-gemini-3-1-pro | METALS_MINING | 3 | 0.58 | -0.030183255479698134 | -0.015809439409597392 | -0.021815209144713965 | 0.11996648328950515 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 36bf2018cbdfa3960935b9d1d4b1831c4a248e534d9be22d4f667c8317fb4146 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 74868dfa9e19999c5bce3ccd50486b16b059263580668878a971c39f7c3cb62f |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | e4f28f02f6f778adab9b124b9c7e86cda940f96e85cd322f26bdfdc143c84741 |
| market_data/universe_decision_context.md | 6a4aa6a4c66111c8a3cf8383ec3c48a5fe36688101a37ecaba2f4e8cc6828062 |
| market_data/universe_decision_context.json | 8267dc9e881b7a5f1a97ba2cd1df4df9dd9ade43875cedd6ac7d3295dfe06bd5 |
| market_data/decision_context_source_history.json | 860c0e67622b3a15e721669054392274b002d932852b844d198ab026efe91bbd |
| market_data/universe_quality_evidence.md | b23bec140dc08f274b57c3ad10b202e5f3c65bef8d47f151e08376225c358e09 |
| market_data/universe_quality_evidence.json | 5d9844248025ed903e4b7dedc485c84bab005a647d60e1f78ed9818363f72f81 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a931712ea50a3787e2eae635b8d8a931b62d8e530c30d488de4e3dd98c985829 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 0c9f9d92f5a0710fd057177ab09ab78a27c26aedc5ee829046700f139617a9e7 | yes |
| Final briefing | research/final_briefing.md | model-facing | 36bf2018cbdfa3960935b9d1d4b1831c4a248e534d9be22d4f667c8317fb4146 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
