# CapitalBench Report: CB-2026-07-23-1M / official-v2-2-20260723-1m

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-20260723-1m
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-23-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-23
- Decision deadline: 2026-07-24T09:30:00Z
- Horizon: one month
- Entry date: 2026-07-23
- Exit date: 2026-08-21
- Entry rule: Use adjusted close prices on Thursday, July 23, 2026 as the one-month entry snapshot, calculated after regular trading ends and supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, August 21, 2026 as the one-month exit snapshot, the closest prior trading close to Sunday, August 23, and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.6 | Overweight energy on the oil price shock, pair with defensive value, healthcare, dividend equities, and gold to outperform SPY in a risk-off, high-rate, high-oil month. | Rapid geopolitical de-escalation collapses oil and reverses energy/gold gains; Dovish FOMC surprise Jul 29 sparks growth rally that value/defensives lag; Oil-driven inflation forces yields higher, hitting all equities including holdings; Soft July CPI (Aug 12) reignites mega-cap growth leadership |
| openai-gpt-5-5 | openai | portfolio | ENERGY | 4 | 0.57 | SPY faces near-term pressure from weak breadth, mega-cap earnings declines, and a scheduled FOMC/macro-heavy month. Selected holdings have base forecasts above SPY and combine oil-driven continuation with defensive rotation potential. | Oil-price spike reverses quickly as inventories build or geopolitical risk premium fades.; FOMC communication or July CPI/PPI triggers a broad equity selloff that overwhelms defensive sector selection.; Mega-cap technology rebounds sharply after Microsoft, Qualcomm, AMD, or Amazon-related earnings updates, causing SPY to outperform.; Commodity inflation pressures rates higher, hurting dividend and healthcare equity valuations. |
| google-gemini-3-1-pro | google | portfolio | ENERGY | 4 | 0.65 | Overweight energy and oil due to tight supplies and rising prices. Include gold as an inflation hedge and maintain a core S&P 500 position. | A sudden drop in energy prices due to increased supply or weakening demand.; A stronger-than-expected US dollar, which could weigh on commodity prices.; A broader market sell-off driven by disappointing corporate earnings or economic data. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 4 | 0.55 | Healthcare and financials show positive active returns with shallow drawdowns; energy rides oil strength; SPY anchors the portfolio. | FOMC July 29 hawkish surprise pressures rate-sensitive and equity broadly; Oil price reversal undercuts energy overweight; Mega-cap tech earnings volatility spills into broad market |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | Energy and oil offer the clearest positive base-case edge from the supplied price and briefing facts; healthcare adds a second cluster with better recent active return. Remaining weight stays in SPY. | Sharp reversal in crude oil prices from elevated levels; FOMC or inflation data triggering broad equity risk-off; High volatility in oil and energy products amplifying drawdowns; Concentration risk within the energy economic-exposure cluster |
| xai-grok-4-3 | xai | portfolio | SP500 | 3 | 0.62 | Portfolio tilts toward energy strength and Japan policy catalyst while retaining core SP500 exposure. | Oil price reversal on inventory builds; FOMC outcome surprises rates markets; Geopolitical escalation affecting energy |
| openai-gpt-5-6-sol | openai | portfolio | AEROSPACE_DEFENSE | 4 | 0.58 | Direct corporate evidence and near-term scheduled catalysts favor a diversified active allocation over SPY. The principal trade-off is exposure to volatile technology and energy reversals. | A geopolitical de-escalation could sharply reverse oil and defense-sector gains.; Technology earnings or guidance could disappoint after elevated prior relative performance.; A hawkish FOMC response to energy-driven inflation could pressure equity valuations.; Weak breadth and the July 23 surge in new lows could develop into a broader risk-off correction. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.109999656677246 | 18.239999771118164 | 0.29270022784773686 | 1 |
| SILVER | Silver | 52.060001373291016 | 62.720001220703125 | 0.20476372582043645 | 2 |
| SOUTH_AFRICA | South Africa Equities | 60.43000030517578 | 72.51000213623047 | 0.19990074085801468 | 3 |
| BITCOIN_ETF | Bitcoin ETF | 36.650001525878906 | 43.68000030517578 | 0.19181441982568348 | 4 |
| SOFTWARE | Software | 87.0999984741211 | 103.37000274658203 | 0.18679683762905053 | 5 |
| METALS_MINING | Metals and Mining | 103.16999816894531 | 119.33999633789062 | 0.15673159305931406 | 6 |
| GOLD | Gold | 76.1500015258789 | 86.79000091552734 | 0.13972421768149967 | 7 |
| BIOTECH | Biotechnology | 152.22999572753906 | 165.72999572753906 | 0.08868160269913083 | 8 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 108.76000213623047 | 118.0199966430664 | 0.0851415439955312 | 9 |
| HEALTHCARE | Healthcare Sector | 161.44000244140625 | 174.6199951171875 | 0.08164019125659294 | 10 |
| CYBERSECURITY | Cybersecurity | 87.72000122070312 | 94.8499984741211 | 0.08128131730731436 | 11 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 116.8499984741211 | 125.58000183105469 | 0.07471119786849667 | 12 |
| ENERGY | Energy Sector | 59.380001068115234 | 63.63999938964844 | 0.0717412974891416 | 13 |
| DIVIDEND | US Dividend Equities | 32.79999923706055 | 35.11000061035156 | 0.07042687277507476 | 14 |
| BROAD_AI_TECH | Broad AI Technology | 59.33000183105469 | 63.43000030517578 | 0.06910497804797067 | 15 |
| MATERIALS | Materials Sector | 50.290000915527344 | 53.540000915527344 | 0.06462517281435454 | 16 |
| CANADA | Canada Equities | 58.81999969482422 | 62.36000061035156 | 0.060183626893810516 | 17 |
| AUSTRALIA | Australia Equities | 28.489999771118164 | 30.139999389648438 | 0.057915044990732634 | 18 |
| COMMUNICATIONS | Communication Services Sector | 105.37999725341797 | 111.4000015258789 | 0.05712663151797237 | 19 |
| EUROPE | Europe Equities | 87.83000183105469 | 92.72000122070312 | 0.05567572910967922 | 20 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.77999877929688 | 73.41999816894531 | 0.0521639359891819 | 21 |
| UNITED_KINGDOM | United Kingdom Equities | 46.70000076293945 | 48.939998626708984 | 0.04796569223071967 | 22 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.9199981689453 | 221.6699981689453 | 0.04600792791734154 | 23 |
| COPPER | Copper | 38.2400016784668 | 39.9900016784668 | 0.04576359631766014 | 24 |
| LARGE_VALUE | US Large-Cap Value | 246.17999267578125 | 257.2900085449219 | 0.04512964578633527 | 25 |
| JAPAN | Japan Equities | 91.0999984741211 | 95.18000030517578 | 0.04478597035557241 | 26 |
| TAIWAN | Taiwan Equities | 99.83999633789062 | 104.30000305175781 | 0.04467154324378275 | 27 |
| CHINA | China Equities | 53.349998474121094 | 55.65999984741211 | 0.043298996051734484 | 28 |
| INDIA | India Equities | 47.630001068115234 | 49.63999938964844 | 0.04220025774634606 | 29 |
| EMERGING_MARKETS | Emerging Markets | 58.099998474121094 | 60.45000076293945 | 0.040447544759662835 | 30 |
| SP500 | S&P 500 | 738.1799926757812 | 765.719970703125 | 0.03730794426914197 | 31 |
| TOTAL_US_MARKET | Total US Stock Market | 364.69000244140625 | 378.239990234375 | 0.0371548101188921 | 32 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.20999908447266 | 85.98999786376953 | 0.03340943167749222 | 33 |
| BROAD_COMMODITIES | Broad Commodities | 18.059999465942383 | 18.649999618530273 | 0.03266889092109415 | 34 |
| LARGE_GROWTH | US Large-Cap Growth | 118.58999633789062 | 122.38999938964844 | 0.03204320068389843 | 35 |
| MEXICO | Mexico Equities | 75.0 | 77.37999725341797 | 0.03173329671223968 | 36 |
| NASDAQ100 | Nasdaq 100 | 691.9600219726562 | 713.4400024414062 | 0.031042227566145053 | 37 |
| YEN | Japanese Yen | 56.0099983215332 | 57.70000076293945 | 0.030173227853079965 | 38 |
| FINANCIALS | Financials Sector | 55.83000183105469 | 57.47999954223633 | 0.02955396125858356 | 39 |
| TECHNOLOGY | Technology Sector | 178.4499969482422 | 183.30999755859375 | 0.027234523359286777 | 40 |
| SMALL_CAP | US Small-Cap Stocks | 292.0899963378906 | 299.9599914550781 | 0.026943733834976946 | 41 |
| EURO | Euro | 105.02999877929688 | 107.80000305175781 | 0.026373458103923664 | 42 |
| SOUTH_KOREA | South Korea Equities | 173.86000061035156 | 178.33999633789062 | 0.02576783453244924 | 43 |
| SMALL_VALUE | US Small-Cap Value | 220.5800018310547 | 224.80999755859375 | 0.019176696402327886 | 44 |
| MID_CAP | US Mid-Cap Stocks | 75.44999694824219 | 76.7699966430664 | 0.017495026483960174 | 45 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.2300033569336 | 79.61000061035156 | 0.004796128200399874 | 46 |
| REAL_ESTATE | Real Estate Sector | 44.95000076293945 | 45.08000183105469 | 0.0028921260491372447 | 47 |
| AGRICULTURE | Agriculture Commodities | 28.239999771118164 | 28.31999969482422 | 0.002832858511134795 | 48 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.87999725341797 | 93.12000274658203 | 0.0025840385471720406 | 49 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.52999877929688 | 94.72000122070312 | 0.00200996978588619 | 50 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.26000213623047 | 105.33999633789062 | 0.0007599676993794713 | 51 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.58000183105469 | 91.5999984741211 | 0.0002183516342715297 | 52 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.33999633789062 | 97.3499984741211 | 0.00010275463947784225 | 53 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 54 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.8499984741211 | 92.81999969482422 | -0.0003230886353243756 | 55 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.709999084472656 | 47.650001525878906 | -0.0012575468401816448 | 56 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.26000213623047 | 105.91999816894531 | -0.0031997361231863586 | 57 |
| TIPS | Treasury Inflation-Protected Securities | 107.48999786376953 | 107.12999725341797 | -0.003349154502801488 | 58 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 238.22999572753906 | 237.33999633789062 | -0.00373588299378691 | 59 |
| REGIONAL_BANKS | Regional Banks | 75.1500015258789 | 74.86000061035156 | -0.003858960873440287 | 60 |
| INDUSTRIALS | Industrials Sector | 181.94000244140625 | 180.25 | -0.009288789813831744 | 61 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.16999816894531 | 82.05000305175781 | -0.013466335720152656 | 62 |
| LOW_VOL | US Low Volatility Equities | 76.36000061035156 | 75.30999755859375 | -0.013750694648573258 | 63 |
| US_DOLLAR | US Dollar | 28.559999465942383 | 27.899999618530273 | -0.023109238786896857 | 64 |
| MOMENTUM | US Momentum Equities | 313.9800109863281 | 305.1700134277344 | -0.028059103287875753 | 65 |
| BRAZIL | Brazil Equities | 36.16999816894531 | 35.060001373291016 | -0.03068832877650829 | 66 |
| SEMICONDUCTORS | Semiconductors | 580.1699829101562 | 560.4199829101562 | -0.03404174738743493 | 67 |
| OIL | Crude Oil | 139.49000549316406 | 134.63999938964844 | -0.03476955991483788 | 68 |
| SOLAR | Solar Energy | 52.849998474121094 | 49.31999969482422 | -0.06679278867009619 | 69 |
| UTILITIES | Utilities Sector | 46.189998626708984 | 42.77000045776367 | -0.07404196299256283 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | 0.0717412974891416 | 0.02152238924674248 | Brent at $100.69 (from sub-$72 early July) amid war shock; energy sector has strong 21-session active return (+8.41%) and low SPY beta, benefiting from sustained high crude through the window. |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.04512964578633527 | 0.011282411446583818 | Value leading (+1.54% 21s active), shallow drawdown, benefits from energy/financials tilt while growth de-rates on 4.69% 10-year yield. |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | 0.08164019125659294 | 0.01632803825131859 | Best 21-session active return (+5.46%), low beta (0.32) defensive exposure amid war/oil shock and equity weakness; low prior-window active return argues room to run. |
| anthropic-claude-fable-5 | DIVIDEND | 15.0 | 0.07042687277507476 | 0.010564030916261213 | +2.62% 21s active, very low beta (0.27), shallow drawdown; suits an environment of elevated yields, energy shock, and negative market breadth. |
| anthropic-claude-fable-5 | GOLD | 10.0 | 0.13972421768149967 | 0.013972421768149968 | Safe-haven hedge on war escalation and inflation pass-through; +1.80% over 5 sessions despite dollar strength, deep prior pullback offers entry. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.08164019125659294 | 0.02449205737697788 | Defensive sector with strong recent active outperformance (+5.46% 21s), shallow drawdown, low beta; attractive after prior underperformance. |
| anthropic-claude-opus-4-8 | ENERGY | 25.0 | 0.0717412974891416 | 0.0179353243722854 | Strongest active return (+8.41% 21s) amid Brent surging 7% to $100.69; oil momentum supports energy equities. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | 0.02955396125858356 | 0.005910792251716712 | Positive active return (+2.99% 21s), shallow drawdown, low volatility; benefits from steady rates and strong labor market. |
| anthropic-claude-opus-4-8 | SP500 | 25.0 | 0.03730794426914197 | 0.009326986067285492 | Core benchmark exposure to reduce tracking risk while active tilts seek alpha. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.0717412974891416 | 0.02152238924674248 | Energy sector shows strong recent momentum and benefits from rising crude prices and tight inventories. |
| google-gemini-3-1-pro | OIL | 20.0 | -0.03476955991483788 | -0.0069539119829675755 | Direct exposure to crude oil, which has surged recently amid tight supplies and strong demand proxies. |
| google-gemini-3-1-pro | GOLD | 25.0 | 0.13972421768149967 | 0.03493105442037492 | Gold provides a hedge against inflation and geopolitical uncertainty, with recent positive momentum. |
| google-gemini-3-1-pro | SP500 | 25.0 | 0.03730794426914197 | 0.009326986067285492 | Core equity exposure to balance the portfolio, despite recent weakness, supported by ongoing economic growth. |
| openai-gpt-5-5 | ENERGY | 30.0 | 0.0717412974891416 | 0.02152238924674248 | Energy equities have direct support from the supplied oil shock, positive recent active performance, and a still-reasonable distance from highs versus crude itself. |
| openai-gpt-5-5 | BROAD_COMMODITIES | 25.0 | 0.03266889092109415 | 0.008167222730273538 | Broad commodities provide diversified exposure to the energy-led inflation impulse while avoiding single-contract oil concentration. |
| openai-gpt-5-5 | DIVIDEND | 25.0 | 0.07042687277507476 | 0.01760671819376869 | Dividend equities show strong recent active return, low drawdown, and lower beta, offering a defensive equity tilt if mega-cap growth remains under pressure. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | 0.08164019125659294 | 0.01632803825131859 | Healthcare has a strong 21-day active return, shallow drawdown, and low market beta, fitting a defensive sector rotation case over the one-month window. |
| openai-gpt-5-6-sol | AEROSPACE_DEFENSE | 35.0 | -0.00373588299378691 | -0.0013075590478254183 | RTX's strong sales, earnings, and cash-flow growth provide direct fundamental support, while geopolitical conditions may sustain defense demand. |
| openai-gpt-5-6-sol | TECHNOLOGY | 25.0 | 0.027234523359286777 | 0.006808630839821694 | Strong prior relative performance and a recent relative pullback create a favorable setup around major technology earnings. |
| openai-gpt-5-6-sol | ENERGY | 20.0 | 0.0717412974891416 | 0.01434825949782832 | Elevated crude prices and strong sector-relative momentum support near-term earnings expectations, with sizing limited by reversal risk. |
| openai-gpt-5-6-sol | DIVIDEND | 20.0 | 0.07042687277507476 | 0.014085374555014952 | Positive short- and prior-window relative performance, moderate volatility, and mature-company exposure offer defensive participation during macro uncertainty. |
| xai-grok-4-3 | SP500 | 50.0 | 0.03730794426914197 | 0.018653972134570984 | Broad US equity exposure with base forecast supported by recent stabilization and upcoming data releases. |
| xai-grok-4-3 | ENERGY | 30.0 | 0.0717412974891416 | 0.02152238924674248 | Strong oil price momentum and inventory data support outperformance versus SPY. |
| xai-grok-4-3 | JAPAN | 20.0 | 0.04478597035557241 | 0.008957194071114482 | Relative strength in prior active returns and Bank of Japan policy meeting provide catalyst. |
| xai-grok-4-5 | ENERGY | 35.0 | 0.0717412974891416 | 0.025109454121199557 | Oil price spike and inventory tightness support energy equities outperformance versus broad market over the one-month window. |
| xai-grok-4-5 | OIL | 15.0 | -0.03476955991483788 | -0.005215433987225682 | Direct crude exposure captures the sharp recent price move and elevated levels after the session surge. |
| xai-grok-4-5 | HEALTHCARE | 25.0 | 0.08164019125659294 | 0.020410047814148236 | Defensive relative strength and positive active return provide diversification with higher base case than SPY. |
| xai-grok-4-5 | SP500 | 25.0 | 0.03730794426914197 | 0.009326986067285492 | Core benchmark holding while concentrating active risk in higher-base energy and healthcare. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 5 | 0.6 | 0.0717412974891416 | 0.07366929162905607 | 0.0363613473599141 | 0.2190309362186808 |  | True | True |
| openai-gpt-5-5 | ENERGY | 4 | 0.57 | 0.0717412974891416 | 0.0636243684221033 | 0.02631642415296133 | 0.22907585942563358 |  | True | True |
| google-gemini-3-1-pro | ENERGY | 4 | 0.65 | 0.0717412974891416 | 0.05882651775143531 | 0.021518573482293343 | 0.23387371009630153 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 4 | 0.55 | 0.08164019125659294 | 0.057665160068265484 | 0.020357215799123515 | 0.23503506777947136 |  | True | True |
| xai-grok-4-5 | ENERGY | 4 | 0.58 | 0.0717412974891416 | 0.0496310540154076 | 0.012323109746265631 | 0.24306917383232926 |  | True | True |
| xai-grok-4-3 | SP500 | 3 | 0.62 | 0.03730794426914197 | 0.049133555452427945 | 0.011825611183285976 | 0.2435666723953089 |  | True | True |
| openai-gpt-5-6-sol | AEROSPACE_DEFENSE | 4 | 0.58 | -0.00373588299378691 | 0.03393470584483955 | -0.00337323842430242 | 0.2587655220028973 |  | False | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 0.0363613473599141 | 0.47733000000000003 | 0.0761765389979974 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 35719b1e1aed21a35150d8f2f577abb191a027721c728526b6a206f5634efe48 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | 595021ad891d72d904d3d5506d262e4f2c109f038eb91b24c45793d59fa56f32 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | d263fa53ccb0b7f09a8c639491bd44ea37957575064b13c7d7a62be40c99b0d2 |
| market_data/universe_decision_context.md | 3b25a34c5332d21e7694e4a5206e4a55df141da106d21154cebef012fa7570f5 |
| market_data/universe_decision_context.json | f0de03a7eba67d80bc7804b65ab5d2a36b0e8f797a54ffdf66e6ee6b41e4350a |
| market_data/decision_context_source_history.json | d8a52935923966c85a0ea7c39c196d6210e7ac82541ac67913bdf309040270e8 |
| market_data/universe_quality_evidence.md | d20fa212025928bf700a78f1bf0eb9f4037cbbf81a45c9cd07b9f77d93ed0b4e |
| market_data/universe_quality_evidence.json | 25afcb60643308cda4e1b09f74971e174f47a2fa3a657a035311a4542d780bcf |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 27d0418fae50529e59d35ed261eabed009bc5862e1baaf622e230bb5fc925c45 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c3734f1f0a8a4f49e610c11199ec52d8c72a482fdac355c53365889bb75c68a4 | yes |
| Final briefing | research/final_briefing.md | model-facing | 35719b1e1aed21a35150d8f2f577abb191a027721c728526b6a206f5634efe48 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
