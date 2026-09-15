# CapitalBench Report: CB-2026-08-13-1M / official-v2-2-all-monthly-20260813

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260813
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-13-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-13
- Decision deadline: 2026-08-13T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-13
- Exit date: 2026-09-14
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | Select active sleeves only where base exceeds SPY; energy leads on oil/geopolitics, healthcare on relative strength, software on recent active gains. Remainder in SPY for diversification under the 50% cluster cap. | Geopolitical de-escalation or oil supply surprise reverses energy; Rates reprice higher on sticky inflation data hurting growth/software; Labor or GDP revisions trigger broad equity drawdown; Concentration in correlated risk assets if risk appetite fades |
| xai-grok-4-6 | xai | portfolio | ENERGY | 4 | 0.56 | SPY is near a record with only a modest expected one-month gain. Energy, healthcare, cybersecurity, and Japan have stronger supplied continuation setups and higher bases, producing positive expected alpha versus SPY. | A broad equity reversal from the August 7 S&P high would drag high-beta cybersecurity and Japan; Oil geopolitics can fade quickly, reversing the energy overweight; Hotter August CPI or a hawkish FOMC-minutes read can compress risk assets before September 14; Labor-market deterioration beyond the July softness can hit cyclicals and international equities together |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | A balanced approach combining core US equities with defensive healthcare and inflation-hedging energy. | Geopolitical tensions easing, leading to a drop in energy prices.; A sudden shift in market sentiment away from defensive sectors like healthcare.; Unexpectedly weak economic data impacting broad equity markets. |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.62 | Selected holdings show base forecasts exceeding SPY while respecting cluster caps and allocation rules. | Labor market revisions could pressure equities; Oil volatility from geopolitical events; Rate-sensitive sector reactions to CPI |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 5 | 0.58 | Breadth is broadening (RSP outperforming), value and healthcare show fresh relative strength with low drawdowns, and energy is supported by Iran-related crude supply risk, all offering modest expected alpha over SPY into mid-September. | Hot August CPI (Sep 11) reprices Fed expectations and hits all equity sleeves; Iran de-escalation drops crude prices, reversing the energy tilt; Mega-cap tech leadership resumes, causing value/equal-weight tilts to lag SPY; Sharp payroll deterioration on Sep 4 triggers broad risk-off despite defensive tilts |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.55 | Modest alpha construction: benchmark core plus low-beta healthcare, improving breadth, and a commodity-linked hedge into a data-heavy month ahead of the September FOMC. | Hot September CPI/PPI revives hike risk given three FOMC dissenters; Mega-cap tech leadership resumes and SPY outruns equal-weight and defensives; Crude reverses lower on Iran de-escalation, hitting the energy sleeve; Further payroll deterioration triggers a broad risk-off drawdown |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 4 | 0.55 | Core SPY with defensive quality and gold overweight to capture recent leadership while managing macro risk. | Hot Aug CPI/PPI reverses rate-cut hopes hurting gold and defensives; Risk-on growth rally leaves defensives lagging SPY; Gold pullback after strong run |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 4 | 0.59 | All selected holdings have base forecasts above SPY's 0.70% forecast. The mix targets positive alpha while diversifying the primary technology thesis across healthcare and equal-weight US equities. | Semiconductor volatility and a renewed growth-stock selloff could overwhelm the pullback thesis.; Hot producer or consumer inflation could lift yields and compress technology valuations.; Weak September labor data could turn the current soft-landing interpretation into recession concern.; Recent healthcare and market-breadth leadership could reverse as prior laggards lose momentum.; Geopolitical escalation involving Iran and crude flows could create an inflation shock before exit. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.23 | 19.17 | 0.3471539002108224 | 1 |
| OIL | Crude Oil | 125.03 | 156.66 | 0.2529792849716068 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 35.88 | 44.74 | 0.24693422519509478 | 3 |
| BRAZIL | Brazil Equities | 33.77 | 37.72 | 0.11696772283091494 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 17.77 | 19.78 | 0.11311198649409127 | 5 |
| ENERGY | Energy Sector | 61.06 | 64.53 | 0.056829348182115824 | 6 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 28.96 | 0.04851556842867488 | 7 |
| YEN | Japanese Yen | 57.53 | 59.43 | 0.033026247175386825 | 8 |
| COMMUNICATIONS | Communication Services Sector | 112.55 | 115.07 | 0.02239004886717022 | 9 |
| SOUTH_AFRICA | South Africa Equities | 67.33 | 68.49 | 0.01722857567206293 | 10 |
| BIOTECH | Biotechnology | 156.86 | 157.6 | 0.004717582557694611 | 11 |
| SOFTWARE | Software | 106.28 | 106.64 | 0.0033872788859616865 | 12 |
| EURO | Euro | 106.3994 | 106.55 | 0.0014154215155348648 | 13 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 14 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.51 | 91.5 | -0.0001092776745711399 | 15 |
| US_DOLLAR | US Dollar | 28.18 | 28.17 | -0.0003548616039743546 | 16 |
| DIVIDEND | US Dividend Equities | 34.43 | 34.34 | -0.0026139994191111127 | 17 |
| TAIWAN | Taiwan Equities | 107.5 | 107.21 | -0.0026976744186046897 | 18 |
| HEALTHCARE | Healthcare Sector | 168.38 | 167.75 | -0.0037415369996436354 | 19 |
| UNITED_KINGDOM | United Kingdom Equities | 48.26 | 47.91 | -0.007252382925818535 | 20 |
| MEXICO | Mexico Equities | 75.45 | 74.82 | -0.0083499005964216 | 21 |
| JAPAN | Japan Equities | 98.47 | 97.58 | -0.009038285772316468 | 22 |
| EMERGING_MARKETS | Emerging Markets | 60.34 | 59.61 | -0.01209811070599942 | 23 |
| TIPS | Treasury Inflation-Protected Securities | 107.16 | 105.82 | -0.012504665920119451 | 24 |
| LARGE_VALUE | US Large-Cap Value | 258.7 | 255.37 | -0.012872052570545023 | 25 |
| SOUTH_KOREA | South Korea Equities | 178.62 | 176.22 | -0.01343634531407456 | 26 |
| GOLD | Gold | 81.78 | 80.54 | -0.015162631450232222 | 27 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.79 | 78.53 | -0.01579145256297787 | 28 |
| BROAD_AI_TECH | Broad AI Technology | 64.62 | 63.47 | -0.017796347879913466 | 29 |
| CONSUMER_STAPLES | Consumer Staples Sector | 86.0 | 84.42 | -0.01837209302325582 | 30 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.69 | 95.89 | -0.018425632101545686 | 31 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.59 | 80.93 | -0.020099285627799945 | 32 |
| CHINA | China Equities | 54.42 | 53.32 | -0.020213156927600173 | 33 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.91 | 46.93 | -0.020455019828845677 | 34 |
| CYBERSECURITY | Cybersecurity | 102.2 | 100.05 | -0.021037181996086174 | 35 |
| FINANCIALS | Financials Sector | 58.26 | 57.03 | -0.021112255406797065 | 36 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.55 | 104.3 | -0.021116846550915058 | 37 |
| SP500 | S&P 500 | 777.88 | 760.88 | -0.021854270581580737 | 38 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.36 | 93.22 | -0.02244127516778527 | 39 |
| SILVER | Silver | 58.16 | 56.84 | -0.022696011004126437 | 40 |
| AUSTRALIA | Australia Equities | 29.74 | 29.06 | -0.02286482851378613 | 41 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.49 | 91.22 | -0.024280671729596692 | 42 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.54 | 71.72 | -0.024748436225183634 | 43 |
| TOTAL_US_MARKET | Total US Stock Market | 384.3 | 374.68 | -0.025032526671870947 | 44 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.3 | 90.93 | -0.02540192926045004 | 45 |
| CANADA | Canada Equities | 62.1 | 60.5 | -0.025764895330112725 | 46 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.16 | 103.11 | -0.028730218538055685 | 47 |
| INDIA | India Equities | 49.98 | 48.43 | -0.031012404961984763 | 48 |
| NASDAQ100 | Nasdaq 100 | 732.07 | 709.18 | -0.03126750174163684 | 49 |
| LOW_VOL | US Low Volatility Equities | 76.23 | 73.82 | -0.031614849796668065 | 50 |
| SMALL_VALUE | US Small-Cap Value | 226.77 | 219.45 | -0.032279402037306615 | 51 |
| TECHNOLOGY | Technology Sector | 190.77 | 184.28 | -0.034020024112806024 | 52 |
| EUROPE | Europe Equities | 92.38 | 89.23 | -0.034098289673089366 | 53 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 222.73 | 215.01 | -0.03466080007183581 | 54 |
| MATERIALS | Materials Sector | 52.31 | 50.49 | -0.03479258268017593 | 55 |
| LARGE_GROWTH | US Large-Cap Growth | 125.66 | 121.26 | -0.03501512016552599 | 56 |
| COPPER | Copper | 39.85 | 38.26 | -0.03989962358845678 | 57 |
| METALS_MINING | Metals and Mining | 115.27 | 110.17 | -0.044243948989329374 | 58 |
| REAL_ESTATE | Real Estate Sector | 45.12 | 43.12 | -0.04432624113475181 | 59 |
| REGIONAL_BANKS | Regional Banks | 77.75 | 74.11 | -0.04681672025723471 | 60 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.45 | 112.85 | -0.0472773322076826 | 61 |
| UTILITIES | Utilities Sector | 44.04 | 41.82 | -0.05040871934604907 | 62 |
| SMALL_CAP | US Small-Cap Stocks | 303.5 | 287.91 | -0.05136738056013168 | 63 |
| MOMENTUM | US Momentum Equities | 316.03 | 299.7 | -0.051672309590861554 | 64 |
| MID_CAP | US Mid-Cap Stocks | 78.42 | 73.79 | -0.05904106095383821 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.1 | 119.595 | -0.08074558032282853 | 66 |
| SEMICONDUCTORS | Semiconductors | 589.12 | 541.5 | -0.08083242802824553 | 67 |
| INDUSTRIALS | Industrials Sector | 185.79 | 169.93 | -0.08536519726573 | 68 |
| SOLAR | Solar Energy | 52.47 | 46.22 | -0.11911568515342097 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 249.69 | 216.77 | -0.1318434859225439 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SP500 | 30.0 | -0.021854270581580737 | -0.006556281174474221 | Core benchmark anchor; index near all-time high with cooling core CPI and strong ISM data supporting broad equity. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | -0.012872052570545023 | -0.0025744105141090046 | Positive 21s active return (+1.68%), low volatility and shallow drawdown; value benefits from elevated rates and firm ISM manufacturing. |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 15.0 | -0.03466080007183581 | -0.005199120010775371 | Broadening breadth: RSP beat SPY by 0.83% over 21s and 0.26% over 5s with lower volatility (11.06%) and shallow drawdown. |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | -0.0037415369996436354 | -0.0007483073999287271 | Strong recent turn (+3.66% active 21s) after deep prior underperformance; low beta (0.27), at 52-week high, health employment growing. |
| anthropic-claude-fable-5 | ENERGY | 15.0 | 0.056829348182115824 | 0.008524402227317374 | Brent at $88.98 with Iran conflict supply uncertainty; +4.42% active 21s, negative SPY beta adds diversification. |
| anthropic-claude-opus-4-8 | SP500 | 40.0 | -0.021854270581580737 | -0.008741708232632294 | Core broad exposure at all-time highs with solid economy and cooling inflation. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | -0.0037415369996436354 | -0.0009353842499109088 | Strong recent active return +3.66%, deep prior pullback, low beta defensive with momentum turning. |
| anthropic-claude-opus-4-8 | GOLD | 20.0 | -0.015162631450232222 | -0.0030325262900464446 | Strong recent momentum +6.05% active, safe-haven demand amid softening labor market and rate-cut odds. |
| anthropic-claude-opus-4-8 | DIVIDEND | 15.0 | -0.0026139994191111127 | -0.0003920999128666669 | Leading recent active return +3.65%, low volatility, defensive quality tilt. |
| anthropic-claude-opus-5 | SP500 | 40.0 | -0.021854270581580737 | -0.008741708232632294 | Core benchmark exposure with market at highs and solid ISM prints. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | -0.0037415369996436354 | -0.0007483073999287271 | Low beta, positive relative trend, at 52-week high with modest drawdown; defensive ballast that has been outperforming. |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 20.0 | -0.03466080007183581 | -0.006932160014367162 | Breadth improving (RSP beating SPY on 5d and 21d) with lowest volatility and shallow drawdown among broad US equity. |
| anthropic-claude-opus-5 | ENERGY | 10.0 | 0.056829348182115824 | 0.005682934818211582 | Brent near $89 with Iran-related supply uncertainty; XLE strongly positive relative return with negative SPY correlation as hedge. |
| anthropic-claude-opus-5 | JAPAN | 10.0 | -0.009038285772316468 | -0.0009038285772316468 | Positive relative trend at 52-week high with weak yen supporting exporter earnings. |
| google-gemini-3-1-pro | SP500 | 50.0 | -0.021854270581580737 | -0.010927135290790368 | Core holding providing broad US equity exposure amid solid economic expansion. |
| google-gemini-3-1-pro | HEALTHCARE | 25.0 | -0.0037415369996436354 | -0.0009353842499109088 | Defensive growth sector with strong recent momentum and positive employment trends. |
| google-gemini-3-1-pro | ENERGY | 25.0 | 0.056829348182115824 | 0.014207337045528956 | Benefiting from rising crude prices and geopolitical uncertainty. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 35.0 | -0.08083242802824553 | -0.028291349809885933 | Deep benchmark-relative pullback follows exceptionally strong prior leadership, while expanding manufacturing offers independent cyclical support. |
| openai-gpt-5-6-sol | CYBERSECURITY | 15.0 | -0.021037181996086174 | -0.003155577299412926 | Strong prior and recent relative performance near a 52-week high provides a cleaner continuation signal than most growth exposures. |
| openai-gpt-5-6-sol | HEALTHCARE | 25.0 | -0.0037415369996436354 | -0.0009353842499109088 | Recent leadership, a fresh 52-week high, and relatively low market beta provide diversification from the technology allocation. |
| openai-gpt-5-6-sol | EQUAL_WEIGHT_SP500 | 25.0 | -0.03466080007183581 | -0.008665200017958952 | Positive breadth, benchmark outperformance, low volatility, and a shallow drawdown support continued participation beyond mega-cap stocks. |
| xai-grok-4-3 | SP500 | 40.0 | -0.021854270581580737 | -0.008741708232632294 | Broad diversified US equity exposure with stable recent performance. |
| xai-grok-4-3 | ENERGY | 20.0 | 0.056829348182115824 | 0.011365869636423165 | Strong recent price gains and oil price stability amid supply uncertainty. |
| xai-grok-4-3 | HEALTHCARE | 20.0 | -0.0037415369996436354 | -0.0007483073999287271 | Outperformed in recent session with defensive characteristics. |
| xai-grok-4-3 | JAPAN | 20.0 | -0.009038285772316468 | -0.0018076571544632936 | Recent outperformance in international equity with positive momentum. |
| xai-grok-4-5 | ENERGY | 30.0 | 0.056829348182115824 | 0.017048804454634747 | Strong recent relative performance with oil price support and geopolitical uncertainty; base case exceeds SPY on energy momentum into the monthly window. |
| xai-grok-4-5 | HEALTHCARE | 25.0 | -0.0037415369996436354 | -0.0009353842499109088 | Recent outperformance, shallow drawdown, and defensive characteristics amid soft labor data support higher base return than SPY. |
| xai-grok-4-5 | SOFTWARE | 20.0 | 0.0033872788859616865 | 0.0006774557771923374 | Strong 21-session active return and quality pullback setup versus high-vol semis; growth exposure with better recent path than SPY. |
| xai-grok-4-5 | SP500 | 25.0 | -0.021854270581580737 | -0.005463567645395184 | Core benchmark ballast given solid but not exceptional macro backdrop and near all-time highs. |
| xai-grok-4-6 | ENERGY | 30.0 | 0.056829348182115824 | 0.017048804454634747 | Oil-linked energy has the strongest near-term supplied price impulse and a live geopolitical supply-risk catalyst versus a modest SPY base. |
| xai-grok-4-6 | HEALTHCARE | 25.0 | -0.0037415369996436354 | -0.0009353842499109088 | Healthcare is at a 52-week high with recent relative strength and the only major July payroll gain cited, supporting a higher one-month base than SPY. |
| xai-grok-4-6 | CYBERSECURITY | 25.0 | -0.021037181996086174 | -0.0052592954990215435 | High prior-active rank and near-high price with positive 21-session active return support a continuation base above SPY if risk appetite holds. |
| xai-grok-4-6 | JAPAN | 20.0 | -0.009038285772316468 | -0.0018076571544632936 | Japan sits at a 52-week high with a strong 5-session bounce and positive 21-session active return, offering international diversification above the SPY base. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | ENERGY | 4 | 0.58 | 0.056829348182115824 | 0.011327308336520993 | 0.03318157891810173 | 0.33582659187430136 |  | True | True |
| xai-grok-4-6 | ENERGY | 4 | 0.56 | 0.056829348182115824 | 0.009046467551239001 | 0.03090073813281974 | 0.3381074326595834 |  | True | True |
| google-gemini-3-1-pro | SP500 | 3 | 0.65 | -0.021854270581580737 | 0.0023448175048276787 | 0.024199088086408416 | 0.3448090827059947 |  | True | True |
| xai-grok-4-3 | SP500 | 4 | 0.62 | -0.021854270581580737 | 6.819684939884984e-05 | 0.021922467430979586 | 0.3470857033614235 |  | True | True |
| anthropic-claude-fable-5 | SP500 | 5 | 0.58 | -0.021854270581580737 | -0.0065537168719699505 | 0.015300553709610787 | 0.3537076170827923 |  | True | False |
| anthropic-claude-opus-5 | SP500 | 5 | 0.55 | -0.021854270581580737 | -0.011643069405948246 | 0.01021120117563249 | 0.3587969696167706 |  | True | False |
| anthropic-claude-opus-4-8 | SP500 | 4 | 0.55 | -0.021854270581580737 | -0.013101718685456315 | 0.008752551896124422 | 0.36025561889627866 |  | True | False |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 4 | 0.59 | -0.08083242802824553 | -0.04104751137716872 | -0.019193240795587985 | 0.3882014115879911 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | SP500 | 0.01021120117563249 | 0.219225 | 0.046578634624848854 |
| anthropic-claude-fable-5 | SP500 | 0.015300553709610787 | 0.47075 | 0.032502503897208254 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c1531f7bcf8287a24759f94353d040d86f7a53050f9bebdc160b451f9eecbb0b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | e158e16952b300bc936a2f9ea12ece438f3f9b55c30da686f00ef520c6e065f9 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | d6554ea3b84a0fd6254a04ced8bd5d3e681475fa96b81af30881017071197709 |
| market_data/universe_decision_context.md | 451e3b4799a355bc00cb6cffaee48c4bd48109dde8082c1043e03e2718982438 |
| market_data/universe_decision_context.json | 3731d865f98a46acc80b5ef08d4de1085a9c915f685ddfc11052b2b1fd306f87 |
| market_data/decision_context_source_history.json | bef3f0dc8789fcb7b1f9b0c1b19da6908ec4fd3fa5f54a5f0d6060c5e01ebead |
| market_data/universe_quality_evidence.md | b6b364f7c5e726dd65bc9cbfbb5e301dbd6803e3b5bf3bfc746d19e69f41eb98 |
| market_data/universe_quality_evidence.json | 4adda7aef5d4638b345d5a8d0520ad186db58f15e985ecab9399458b8389f3de |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | dd1b1aac2282a3e68c147c1f4c9f9b5c88b67cf5611299d1e66bd625fbe0b25b | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 5bfa3d1aab603b4f71ea80c14503d404e7b810a510ba23c06baa8bde298c3cd7 | yes |
| Final briefing | research/final_briefing.md | model-facing | c1531f7bcf8287a24759f94353d040d86f7a53050f9bebdc160b451f9eecbb0b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
