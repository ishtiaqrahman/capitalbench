# CapitalBench Report: CB-2026-08-11-1W / official-v2-2-all-weekly-20260811

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260811
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench Weekly Allocation — August 11, 2026
- Description: Pre-entry one-week portfolio allocation round using a newly researched August 11 briefing and market data through the August 10 close.
- Decision date: 2026-08-11
- Decision deadline: 2026-08-11T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-11
- Exit date: 2026-08-18
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 2 | 0.6 | Energy has direct support from elevated crude prices and supply uncertainty, while healthcare has recent breadth-independent strength and defensive appeal. This barbell is expected to outperform SPY during a macro-event-heavy week. | A rapid reopening of the Strait of Hormuz could unwind the oil risk premium and pressure energy equities.; Softer-than-expected inflation could trigger a growth-stock rally that leaves both holdings behind SPY.; Hot CPI or PPI could lift yields and produce a broad equity selloff.; Recent healthcare strength could reverse without a sector-specific catalyst. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 3 | 0.58 | One-week edge is concentrated in energy continuation plus healthcare relative strength; SPY base is modest positive so only higher-base actives are sized, with cluster discipline. | Crude mean-reversion after the Aug 10-11 spike removes ENERGY premium; Hotter-than-expected CPI/PPI triggers broad equity drawdown; Defensive underperformance if risk appetite expands sharply; Geopolitical headline volatility amplifies oil and equity swings inside the week |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 4 | 0.6 | Overweight energy and gold on the geopolitical crude spike and inflation-print week, plus defensive healthcare, against a 25% SPY core. | Rapid Hormuz reopening triggers a sharp oil and energy-sector reversal; Cool CPI print sparks a growth/tech rally that this defensive tilt underperforms; Gold pullback from record levels if real yields rise; High oil volatility (USO 70% vol) spills into energy equities |
| openai-gpt-5-5 | openai | portfolio | OIL | 4 | 0.58 | Selected holdings have stronger base forecasts than SPY for the August 11 to August 18 window. The allocation balances a high-conviction energy catalyst with healthcare and cybersecurity diversifiers while respecting the 50% cluster cap. | A rapid Strait of Hormuz reopening or geopolitical de-escalation could reverse oil and energy gains sharply.; July CPI or PPI could surprise in a way that lifts yields and pressures risk assets, especially cybersecurity.; Retail sales, housing starts, or industrial production could weaken risk appetite before the exit close.; Recent winners such as oil, energy, healthcare, and cybersecurity may mean-revert after strong short-term moves. |
| anthropic-claude-opus-5 | anthropic | portfolio | ENERGY | 5 | 0.53 | Modest SPY base case; diversified tilt to energy, gold, healthcare and UK equities with independent macro support, capped per cluster. | Rapid Hormuz reopening collapses crude and hits energy allocation; Cool July CPI sparks a mega-cap tech-led SPY melt-up that low-beta holdings lag; Gold gives back its 8% five-day gain on higher real yields; Healthcare at 52-week high vulnerable to policy or reversal risk |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 4 | 0.55 | Tilt toward defensives and real assets given elevated inflation prints scheduled and geopolitical energy risk, while retaining SPY core. | Cooler CPI could spark growth-stock rotation hurting defensives and gold; Hormuz reopening could crush energy and oil prices; Gold pullback if dollar/real yields rise |
| google-gemini-3-1-pro | google | portfolio | OIL | 2 | 0.65 | Defensive positioning with commodities. | Geopolitical de-escalation leading to a drop in oil prices.; Stronger-than-expected economic data boosting equities and the US dollar, hurting gold. |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.58 | Energy and select defensives show higher one-week base forecasts than SPY amid oil and inflation data; 50/25/15/10 mix balances exposure. | Oil reversal if Hormuz uncertainty resolves quickly; Weaker than expected July CPI triggering broad equity rally; Higher Treasury yields pressuring rate-sensitive sectors |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ENERGY | Energy Sector | 60.93 | 63.68000030517578 | 0.04513376506114852 | 1 |
| OIL | Crude Oil | 127.61 | 130.66000366210938 | 0.02390097689921933 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 35.94 | 36.6 | 0.018363939899833204 | 3 |
| ETHEREUM_ETF | Ethereum ETF | 14.18 | 14.44 | 0.01833568406205921 | 4 |
| SOUTH_KOREA | South Korea Equities | 167.24 | 170.05 | 0.016802200430519054 | 5 |
| BROAD_COMMODITIES | Broad Commodities | 17.91 | 18.2 | 0.016192071468453362 | 6 |
| AGRICULTURE | Agriculture Commodities | 27.59 | 28.030000686645508 | 0.015947832063990974 | 7 |
| BIOTECH | Biotechnology | 158.07 | 160.11 | 0.012905674701081837 | 8 |
| REAL_ESTATE | Real Estate Sector | 44.08 | 44.630001068115234 | 0.012477338205880928 | 9 |
| MOMENTUM | US Momentum Equities | 308.34 | 311.80999755859375 | 0.01125380281051358 | 10 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.69 | 85.58 | 0.010508914865981822 | 11 |
| HEALTHCARE | Healthcare Sector | 168.01 | 169.73 | 0.01023748586393669 | 12 |
| UTILITIES | Utilities Sector | 43.63 | 44.02 | 0.008938803575521348 | 13 |
| DIVIDEND | US Dividend Equities | 34.27 | 34.51 | 0.007003209804493649 | 14 |
| LOW_VOL | US Low Volatility Equities | 75.65 | 76.03 | 0.005023132848644973 | 15 |
| TAIWAN | Taiwan Equities | 103.94 | 104.39 | 0.004329420819703778 | 16 |
| EURO | Euro | 106.52 | 106.84 | 0.0030041306796846357 | 17 |
| TIPS | Treasury Inflation-Protected Securities | 106.89 | 107.0199966430664 | 0.001216172168270191 | 18 |
| CANADA | Canada Equities | 61.51 | 61.58 | 0.001138026337180964 | 19 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 251.9 | 252.16 | 0.0010321556173085167 | 20 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.49 | 91.56 | 0.0007651109410864443 | 21 |
| FINANCIALS | Financials Sector | 57.8 | 57.84000015258789 | 0.0006920441624203022 | 22 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.87 | 92.93 | 0.0006460643910843888 | 23 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.03 | 93.08 | 0.0005374610340749264 | 24 |
| REGIONAL_BANKS | Regional Banks | 76.81 | 76.85 | 0.0005207655253220977 | 25 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.32 | 97.35 | 0.00030826140567197235 | 26 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.51 | 79.53 | 0.00025154068670607543 | 27 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 28 |
| US_DOLLAR | US Dollar | 28.14 | 28.14 | 0.0 | 28 |
| NASDAQ100 | Nasdaq 100 | 718.45 | 717.510009765625 | -0.0013083585975016687 | 30 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.99 | 105.83999633789062 | -0.0014152624031452676 | 31 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.83 | 94.64 | -0.0020035853632816014 | 32 |
| SMALL_VALUE | US Small-Cap Value | 224.97 | 224.45 | -0.0023114193003511696 | 33 |
| SMALL_CAP | US Small-Cap Stocks | 300.99 | 300.23 | -0.002525000830592372 | 34 |
| TECHNOLOGY | Technology Sector | 186.09 | 185.6199951171875 | -0.002525685866046068 | 35 |
| YEN | Japanese Yen | 57.63 | 57.48 | -0.0026028110359188616 | 36 |
| UNITED_KINGDOM | United Kingdom Equities | 48.3 | 48.16 | -0.0028985507246377384 | 37 |
| SP500 | S&P 500 | 770.56 | 767.45 | -0.004036025747508165 | 38 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.69 | 219.7899932861328 | -0.004078149050102842 | 39 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.69 | 72.38999938964844 | -0.004127123543149813 | 40 |
| TOTAL_US_MARKET | Total US Stock Market | 380.65 | 379.04 | -0.004229607250755163 | 41 |
| LARGE_GROWTH | US Large-Cap Growth | 123.6 | 123.07 | -0.004288025889967684 | 42 |
| LARGE_VALUE | US Large-Cap Value | 257.92 | 256.7300109863281 | -0.004613791151023117 | 43 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.82 | 47.59 | -0.004809703053115788 | 44 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.93 | 105.37000274658203 | -0.00528648403113352 | 45 |
| SEMICONDUCTORS | Semiconductors | 572.93 | 569.77 | -0.005515508002722824 | 46 |
| GOLD | Gold | 82.18 | 81.70999908447266 | -0.005719164219120887 | 47 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.19 | 81.66 | -0.006448473050249426 | 48 |
| MID_CAP | US Mid-Cap Stocks | 77.77 | 77.23999786376953 | -0.006814994679573916 | 49 |
| COMMUNICATIONS | Communication Services Sector | 111.27 | 110.4800033569336 | -0.00709981704921725 | 50 |
| EMERGING_MARKETS | Emerging Markets | 60.12 | 59.63999938964844 | -0.007984042088349352 | 51 |
| EUROPE | Europe Equities | 92.3 | 91.55000305175781 | -0.008125644076296679 | 52 |
| BRAZIL | Brazil Equities | 33.98 | 33.70000076293945 | -0.008240118806961294 | 53 |
| JAPAN | Japan Equities | 96.28 | 95.37000274658203 | -0.009451570974428392 | 54 |
| BROAD_AI_TECH | Broad AI Technology | 63.2 | 62.529998779296875 | -0.01060128513770775 | 55 |
| AUSTRALIA | Australia Equities | 29.95 | 29.610000610351562 | -0.011352233377243337 | 56 |
| INDUSTRIALS | Industrials Sector | 185.7 | 183.57 | -0.011470113085621958 | 57 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 128.3 | 126.80000305175781 | -0.011691324616073251 | 58 |
| CHINA | China Equities | 55.62 | 54.9 | -0.012944983818770184 | 59 |
| INDIA | India Equities | 50.09 | 49.38 | -0.014174485925334435 | 60 |
| SOFTWARE | Software | 103.92 | 101.95999908447266 | -0.018860670857653417 | 61 |
| SILVER | Silver | 58.55 | 57.44 | -0.018958155422715617 | 62 |
| SOUTH_AFRICA | South Africa Equities | 68.59 | 67.1 | -0.02172328327744577 | 63 |
| MEXICO | Mexico Equities | 76.24 | 74.46 | -0.02334732423924446 | 64 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 119.24 | 116.36 | -0.024152968802415242 | 65 |
| CYBERSECURITY | Cybersecurity | 99.92 | 97.44 | -0.02481985588470781 | 66 |
| COPPER | Copper | 40.22 | 39.18 | -0.02585778219791146 | 67 |
| MATERIALS | Materials Sector | 53.24 | 51.779998779296875 | -0.02742301316121576 | 68 |
| METALS_MINING | Metals and Mining | 117.83 | 113.63 | -0.03564457268946786 | 69 |
| SOLAR | Solar Energy | 52.7 | 49.87 | -0.053700189753320804 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | 0.04513376506114852 | 0.013540129518344556 | Brent up 5% Aug 10 and another 1.5% pre-cutoff with Strait of Hormuz reopening uncertain; energy sector has strong prior trend (0.985 prior active rank) and low SPY beta hedges an equity pullback. |
| anthropic-claude-fable-5 | GOLD | 25.0 | -0.005719164219120887 | -0.0014297910547802217 | Gold at $4,425 with safe-haven demand amid geopolitical supply shock and elevated inflation; hedges hot CPI/PPI prints during the window. |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | 0.01023748586393669 | 0.0020474971727873384 | Defensive sector with recent relative strength (+2.61% 3-session, +1.79% active) and negative SPY beta, cushioning against energy-shock equity weakness. |
| anthropic-claude-fable-5 | SP500 | 25.0 | -0.004036025747508165 | -0.0010090064368770413 | Benchmark anchor; ~50% Q2 earnings growth supports equities but oil shock and 4.70% 10-year yield cap upside. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.01023748586393669 | 0.003071245759181007 | Defensive sector with positive recent active return, low beta, near 52w high, and rising healthcare employment; resilient into CPI/PPI week. |
| anthropic-claude-opus-4-8 | GOLD | 25.0 | -0.005719164219120887 | -0.0014297910547802217 | Strong recent momentum (+8.3% 21s, +6.27% active 5s), safe-haven demand amid elevated inflation and geopolitical oil risk. |
| anthropic-claude-opus-4-8 | SP500 | 25.0 | -0.004036025747508165 | -0.0010090064368770413 | Broad benchmark exposure with strong Q2 earnings growth (~50% YoY) and solid ISM data. |
| anthropic-claude-opus-4-8 | ENERGY | 20.0 | 0.04513376506114852 | 0.009026753012229705 | Highest prior active rank, Brent up on Hormuz uncertainty, strong 3s (+5.01%) with low drawdown vs energy peers. |
| anthropic-claude-opus-5 | ENERGY | 25.0 | 0.04513376506114852 | 0.01128344126528713 | Brent up to $89 with Hormuz reopening uncertain; energy has strongest prior active trend and low SPY correlation. |
| anthropic-claude-opus-5 | HEALTHCARE | 25.0 | 0.01023748586393669 | 0.0025593714659841726 | Defensive sector at 52-week high with positive volume and negative beta to SPY; hedges CPI-driven equity drawdown. |
| anthropic-claude-opus-5 | GOLD | 20.0 | -0.005719164219120887 | -0.0011438328438241774 | Elevated inflation (headline 3.5% y/y, PPI 5.5%) and geopolitical energy risk support gold; strong recent bid. |
| anthropic-claude-opus-5 | UNITED_KINGDOM | 15.0 | -0.0028985507246377384 | -0.00043478260869566076 | Top quality-evidence score: strong prior relative trend, low volatility, shallow drawdown, energy/financial tilt. |
| anthropic-claude-opus-5 | SP500 | 15.0 | -0.004036025747508165 | -0.0006054038621262247 | Benchmark anchor to limit tracking error given a heavy data week. |
| google-gemini-3-1-pro | OIL | 50.0 | 0.02390097689921933 | 0.011950488449609664 | Oil prices are rising amid geopolitical uncertainty and supply concerns. |
| google-gemini-3-1-pro | GOLD | 50.0 | -0.005719164219120887 | -0.0028595821095604435 | Gold provides a safe haven amid equity volatility and geopolitical risks. |
| openai-gpt-5-5 | OIL | 30.0 | 0.02390097689921933 | 0.0071702930697657985 | Crude has the clearest one-week catalyst from early August 11 strength and unresolved Strait of Hormuz reopening uncertainty, with strong prior active momentum despite high reversal risk. |
| openai-gpt-5-5 | ENERGY | 20.0 | 0.04513376506114852 | 0.009026753012229705 | Energy equities offer leveraged but less futures-specific participation in the oil shock, supported by strong prior active return and high quality prior trend rank. |
| openai-gpt-5-5 | HEALTHCARE | 25.0 | 0.01023748586393669 | 0.0025593714659841726 | Healthcare combines recent relative strength with lower beta to SPY, providing a diversifier if macro data unsettle broad equities. |
| openai-gpt-5-5 | CYBERSECURITY | 25.0 | -0.02481985588470781 | -0.006204963971176952 | Cybersecurity has strong recent and prior active performance with a 52-week-high position, giving a focused continuation candidate within the technology-and-growth cluster. |
| openai-gpt-5-6-sol | ENERGY | 50.0 | 0.04513376506114852 | 0.02256688253057426 | Energy equities offer moderated exposure to the oil-supply shock, supported by strong prior relative performance and continued crude strength. |
| openai-gpt-5-6-sol | HEALTHCARE | 50.0 | 0.01023748586393669 | 0.005118742931968345 | Healthcare combines recent relative strength with defensive characteristics that may help during inflation and growth uncertainty. |
| xai-grok-4-3 | SP500 | 50.0 | -0.004036025747508165 | -0.0020180128737540826 | Broad equity exposure with neutral base case amid mixed macro data. |
| xai-grok-4-3 | ENERGY | 25.0 | 0.04513376506114852 | 0.01128344126528713 | Oil price surge and supply disruption signals support near-term outperformance. |
| xai-grok-4-3 | HEALTHCARE | 15.0 | 0.01023748586393669 | 0.0015356228795905035 | Defensive sector with positive recent relative return and earnings visibility. |
| xai-grok-4-3 | MATERIALS | 10.0 | -0.02742301316121576 | -0.002742301316121576 | Commodity-linked sector showing recent strength consistent with energy move. |
| xai-grok-4-5 | ENERGY | 35.0 | 0.04513376506114852 | 0.01579681777140198 | Oil price surge and Hormuz uncertainty support near-term energy equity continuation into the scoring window. |
| xai-grok-4-5 | HEALTHCARE | 30.0 | 0.01023748586393669 | 0.003071245759181007 | Recent relative strength, lower beta, and defensive characteristics with quality evidence support outperformance vs SPY base. |
| xai-grok-4-5 | SP500 | 35.0 | -0.004036025747508165 | -0.0014126090116278577 | Core benchmark ballast given mixed macro calendar and to keep non-benchmark cluster exposure inside caps. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | ENERGY | 2 | 0.6 | 0.04513376506114852 | 0.027685625462542607 | 0.03172165121005077 | 0.017448139598605916 |  | True | True |
| xai-grok-4-5 | ENERGY | 3 | 0.58 | 0.04513376506114852 | 0.01745545451895513 | 0.021491480266463296 | 0.027678310542193392 |  | True | True |
| anthropic-claude-fable-5 | ENERGY | 4 | 0.6 | 0.04513376506114852 | 0.013148829199474632 | 0.017184854946982797 | 0.03198493586167389 |  | True | True |
| openai-gpt-5-5 | OIL | 4 | 0.58 | 0.02390097689921933 | 0.012551453576802724 | 0.01658747932431089 | 0.0325823114843458 |  | True | True |
| anthropic-claude-opus-5 | ENERGY | 5 | 0.53 | 0.04513376506114852 | 0.011658793416625238 | 0.015694819164133404 | 0.03347497164452329 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 4 | 0.55 | 0.01023748586393669 | 0.009659201279753449 | 0.013695227027261614 | 0.035474563781395074 |  | True | True |
| google-gemini-3-1-pro | OIL | 2 | 0.65 | 0.02390097689921933 | 0.00909090634004922 | 0.013126932087557386 | 0.0360428587210993 |  | True | True |
| xai-grok-4-3 | SP500 | 4 | 0.58 | -0.004036025747508165 | 0.008058749955001976 | 0.01209477570251014 | 0.037075015106146546 |  | True | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | ENERGY | 0.015694819164133404 | 0.22418 | 0.07000989902816221 |
| anthropic-claude-fable-5 | ENERGY | 0.017184854946982797 | 0.44676000000000005 | 0.03846551828047004 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 846e446b282f2abc8094e627708bdcdec7452b6fddb1cba831c91746c45f53d5 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 44cd9835b6f4d7138f57d0bbb95ae9fce7b70e952c3aa04a8f7bd84258999c64 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 7f1269fa161b48e92103804a3a4990e3983bff57fd51dfc5808d3186bee35d2c |
| market_data/universe_decision_context.md | 98c5321d267cc9cc25a682d227243a56d5de6b601052e17ac2f2c34bb51fd632 |
| market_data/universe_decision_context.json | 83f6d2fce83a46651091c5fd32919c1230f9993e67d8b754f5c01a0029280001 |
| market_data/decision_context_source_history.json | 1c1717633977f347a599583dce6dd1d518a5d6d645a5173d2c2f4309a5793c40 |
| market_data/universe_quality_evidence.md | 58c3dab03e1823bfebcffa3486f21551cf4e10c22223512fb6fc58290ae1d8b5 |
| market_data/universe_quality_evidence.json | ef75e6301ecab531d5e9c67504e6ffbb4d6cc90311714e0b0719ffc5f41a8ff0 |

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
