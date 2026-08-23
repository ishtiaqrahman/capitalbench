# CapitalBench Report: CB-2026-07-22-1M / official-v2-2-20260722-1m

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-20260722-1m
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-22-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-22
- Decision deadline: 2026-07-23T09:30:00Z
- Horizon: one month
- Entry date: 2026-07-22
- Exit date: 2026-08-21
- Entry rule: Use adjusted close prices on Wednesday, July 22, 2026 as the one-month entry snapshot, calculated after regular trading ends and supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, August 21, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | ENERGY | 2 | 0.65 | Balanced approach using Energy for growth and Dividend for defense. | A sudden drop in oil prices could negatively impact the Energy allocation.; A broad market downturn could drag down Dividend equities despite their defensive nature. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | SPY base is modest given mixed payrolls, cooling CPI, and recent 5-session weakness. Energy/OIL clear the hurdle on price and inventory evidence; healthcare and dividend clear on relative performance and defensive characteristics into the FOMC and data window. | Sudden oil price reversal on inventory builds or de-escalation; FOMC hawkish surprise lifting real yields and pressuring all risk assets; Growth re-acceleration favoring mega-cap tech over value/energy/defensives; Cluster concentration risk if energy mean-reverts hard |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 4 | 0.55 | Defensive/value rotation with recent momentum and low drawdown provides modest alpha over SPY into a busy macro window. | Hawkish FOMC on July 29 triggers broad equity selloff hurting all holdings; Sharp mega-cap tech rally lifts SPY faster than defensive tilts; Oil spike reignites inflation and pressures rate-sensitive names |
| openai-gpt-5-5 | openai | portfolio | OIL | 4 | 0.56 | Base forecasts for all selected holdings exceed the SPY base forecast. The weighted base return is 1.54%, implying 0.74 percentage points of expected alpha versus SPY over the one-month window. | Oil's recent surge reverses if inventory builds and weaker product supplied outweigh geopolitical supply risk.; A dovish growth rally or mega-cap technology rebound causes SPY to outperform defensive and international tilts.; July FOMC, CPI/PPI, GDP, or payrolls surprise markets and trigger broad risk-off selling.; Currency or policy surprises around the Bank of England decision hurt UK equities. |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.55 | Energy and select defensive sectors show stronger base-case returns than SPY over the one-month horizon based on recent price action and macro data. | FOMC policy surprise on July 29; Oil price reversal below $90; Weaker than expected Q2 GDP print |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.58 | Pullback-in-uptrend AI/semis exposure plus energy hedge and defensive dividend sleeve, anchored with 15% SPY, targeting ~1% alpha over the month. | Hawkish FOMC on July 29 with sticky 3.5% CPI could hit high-beta tech; Oil above $95 could squeeze margins and consumer demand, hurting equities broadly; Semiconductor pullback could continue rather than revert (52.9% volatility); Taiwan geopolitical or currency shock; Energy positions vulnerable to a rapid oil retracement |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | Selected holdings all exceed SPY's 1.0% base forecast. The weighted base return is 2.08%, implying 1.08 percentage points of expected alpha. | Semiconductor and growth-stock pullbacks deepen as elevated yields compress valuations.; Alphabet, Microsoft, or Qualcomm results fail to meet embedded market expectations despite strong reported growth.; The Bank of Japan delivers a policy surprise that pressures Japanese equities.; Oil reverses sharply as rising inventories and weak product demand outweigh geopolitical supply concerns. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.520000457763672 | 18.239999771118164 | 0.25619829174078657 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 37.34000015258789 | 43.68000030517578 | 0.16979111212318765 | 2 |
| SILVER | Silver | 53.91999816894531 | 62.720001220703125 | 0.16320480991459085 | 3 |
| SOFTWARE | Software | 89.0199966430664 | 103.37000274658203 | 0.1611998050399086 | 4 |
| METALS_MINING | Metals and Mining | 103.5 | 119.33999633789062 | 0.1530434428781704 | 5 |
| SOUTH_AFRICA | South Africa Equities | 62.97999954223633 | 72.51000213623047 | 0.15131792097907248 | 6 |
| GOLD | Gold | 77.69000244140625 | 86.79000091552734 | 0.11713216872382404 | 7 |
| HEALTHCARE | Healthcare Sector | 159.42999267578125 | 174.6199951171875 | 0.09527694373226758 | 8 |
| BIOTECH | Biotechnology | 152.11000061035156 | 165.72999572753906 | 0.08954043167797221 | 9 |
| ENERGY | Energy Sector | 59.20000076293945 | 63.63999938964844 | 0.07499997583595519 | 10 |
| DIVIDEND | US Dividend Equities | 32.900001525878906 | 35.11000061035156 | 0.06717322133660963 | 11 |
| CYBERSECURITY | Cybersecurity | 89.33000183105469 | 94.8499984741211 | 0.061793311652518446 | 12 |
| BROAD_AI_TECH | Broad AI Technology | 60.13999938964844 | 63.43000030517578 | 0.054705702509428855 | 13 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 119.13999938964844 | 125.58000183105469 | 0.0540540748228826 | 14 |
| MATERIALS | Materials Sector | 50.81999969482422 | 53.540000915527344 | 0.053522259681952455 | 15 |
| CANADA | Canada Equities | 59.279998779296875 | 62.36000061035156 | 0.05195684707285042 | 16 |
| BROAD_COMMODITIES | Broad Commodities | 17.809999465942383 | 18.649999618530273 | 0.047164524299633026 | 17 |
| SOUTH_KOREA | South Korea Equities | 170.42999267578125 | 178.33999633789062 | 0.04641204014575662 | 18 |
| AUSTRALIA | Australia Equities | 28.860000610351562 | 30.139999389648438 | 0.044352001116651385 | 19 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.6999969482422 | 221.6699981689453 | 0.04217207968689274 | 20 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.48999786376953 | 73.41999816894531 | 0.04156618518897326 | 21 |
| EUROPE | Europe Equities | 89.08999633789062 | 92.72000122070312 | 0.04074537021019764 | 22 |
| LARGE_VALUE | US Large-Cap Value | 247.52000427246094 | 257.2900085449219 | 0.03947157443366267 | 23 |
| CHINA | China Equities | 53.56999969482422 | 55.65999984741211 | 0.03901437678727149 | 24 |
| UNITED_KINGDOM | United Kingdom Equities | 47.2400016784668 | 48.939998626708984 | 0.03598638627942918 | 25 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.0199966430664 | 118.0199966430664 | 0.03508156567064091 | 26 |
| JAPAN | Japan Equities | 92.19000244140625 | 95.18000030517578 | 0.032432994734650444 | 27 |
| INDIA | India Equities | 48.220001220703125 | 49.63999938964844 | 0.029448322957230433 | 28 |
| EMERGING_MARKETS | Emerging Markets | 58.810001373291016 | 60.45000076293945 | 0.027886402845643365 | 29 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 231.11000061035156 | 237.33999633789062 | 0.026956841811630383 | 30 |
| YEN | Japanese Yen | 56.22999954223633 | 57.70000076293945 | 0.02614265041206254 | 31 |
| TAIWAN | Taiwan Equities | 101.68000030517578 | 104.30000305175781 | 0.025767139444517362 | 32 |
| FINANCIALS | Financials Sector | 56.04999923706055 | 57.47999954223633 | 0.025512940671554185 | 33 |
| TOTAL_US_MARKET | Total US Stock Market | 368.8699951171875 | 378.239990234375 | 0.02540189020852912 | 34 |
| SP500 | S&P 500 | 747.4099731445312 | 765.719970703125 | 0.024497930475237295 | 35 |
| EURO | Euro | 105.33000183105469 | 107.80000305175781 | 0.023450120362334292 | 36 |
| OIL | Crude Oil | 131.67999267578125 | 134.63999938964844 | 0.022478788567031893 | 37 |
| SMALL_CAP | US Small-Cap Stocks | 293.7900085449219 | 299.9599914550781 | 0.02100133677355065 | 38 |
| COMMUNICATIONS | Communication Services Sector | 109.19999694824219 | 111.4000015258789 | 0.02014656262929626 | 39 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.37999725341797 | 85.98999786376953 | 0.019080358648463358 | 40 |
| COPPER | Copper | 39.25 | 39.9900016784668 | 0.018853545948198658 | 41 |
| TECHNOLOGY | Technology Sector | 180.27000427246094 | 183.30999755859375 | 0.016863555855571866 | 42 |
| MID_CAP | US Mid-Cap Stocks | 75.69000244140625 | 76.7699966430664 | 0.01426865063845395 | 43 |
| SMALL_VALUE | US Small-Cap Value | 222.0500030517578 | 224.80999755859375 | 0.01242960805631066 | 44 |
| LARGE_GROWTH | US Large-Cap Growth | 120.91999816894531 | 122.38999938964844 | 0.012156808162114618 | 45 |
| NASDAQ100 | Nasdaq 100 | 705.3499755859375 | 713.4400024414062 | 0.011469521706225727 | 46 |
| MEXICO | Mexico Equities | 76.70999908447266 | 77.37999725341797 | 0.008734169951006177 | 47 |
| INDUSTRIALS | Industrials Sector | 178.85000610351562 | 180.25 | 0.007827754256122699 | 48 |
| AGRICULTURE | Agriculture Commodities | 28.229999542236328 | 28.31999969482422 | 0.003188103225196137 | 49 |
| REAL_ESTATE | Real Estate Sector | 45.0099983215332 | 45.08000183105469 | 0.001555287983381115 | 50 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.5199966430664 | 79.61000061035156 | 0.0011318406826543725 | 51 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.58000183105469 | 91.5999984741211 | 0.0002183516342715297 | 52 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 53 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.1500015258789 | 93.12000274658203 | -0.0003220480816475968 | 54 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.58000183105469 | 97.3499984741211 | -0.002357074734757769 | 55 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.0999984741211 | 92.81999969482422 | -0.0030075057345431144 | 56 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.79999923706055 | 47.650001525878906 | -0.003138027480664607 | 57 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.08999633789062 | 94.72000122070312 | -0.003890999384128402 | 58 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.87999725341797 | 105.33999633789062 | -0.005100122114991001 | 59 |
| TIPS | Treasury Inflation-Protected Securities | 107.7699966430664 | 107.12999725341797 | -0.0059385674082195195 | 60 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.66999816894531 | 105.91999816894531 | -0.007031030400995619 | 61 |
| REGIONAL_BANKS | Regional Banks | 75.5999984741211 | 74.86000061035156 | -0.009788331728906585 | 62 |
| LOW_VOL | US Low Volatility Equities | 76.19999694824219 | 75.30999755859375 | -0.011679782484151024 | 63 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.44000244140625 | 82.05000305175781 | -0.01665866909129743 | 64 |
| US_DOLLAR | US Dollar | 28.450000762939453 | 27.899999618530273 | -0.019332201394020365 | 65 |
| MOMENTUM | US Momentum Equities | 314.239990234375 | 305.1700134277344 | -0.028863216294895522 | 66 |
| BRAZIL | Brazil Equities | 36.619998931884766 | 35.060001373291016 | -0.04259960688408082 | 67 |
| SEMICONDUCTORS | Semiconductors | 586.9099731445312 | 560.4199829101562 | -0.045134673879279275 | 68 |
| UTILITIES | Utilities Sector | 45.93000030517578 | 42.77000045776367 | -0.0688003445768759 | 69 |
| SOLAR | Solar Energy | 53.720001220703125 | 49.31999969482422 | -0.08190620673670412 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 30.0 | -0.045134673879279275 | -0.013540402163783782 | Strongest prior relative trend (+60.9% prior active) with deepest recent pullback; AI capex signals (Alphabet Cloud +82%, SMCI +19.8%) support mean reversion upward into Nvidia-adjacent earnings season. |
| anthropic-claude-fable-5 | TAIWAN | 20.0 | 0.025767139444517362 | 0.005153427888903473 | Semiconductor supply-chain proxy with strong prior trend (+57% prior active) and sharp recent pullback; benefits from same AI demand evidence with lower drawdown than Korea. |
| anthropic-claude-fable-5 | ENERGY | 15.0 | 0.07499997583595519 | 0.011249996375393279 | Brent above $94 with Middle East supply risk cited by the Fed; XLE +9.1% active over 21 sessions with negative SPY beta offers hedge against oil-driven equity weakness. |
| anthropic-claude-fable-5 | DIVIDEND | 20.0 | 0.06717322133660963 | 0.013434644267321928 | Low-beta (0.27) quality equity outperforming recently (+3.58% active 21s), near 52-week high; ballast against FOMC/CPI event risk with sticky 3.5% CPI. |
| anthropic-claude-fable-5 | SP500 | 15.0 | 0.024497930475237295 | 0.003674689571285594 | Benchmark anchor to control tracking error around heavy event calendar. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.09527694373226758 | 0.028583083119680275 | Strong recent active return (+5.84% 21s), low drawdown, deep prior pullback offering mean-reversion with defensive characteristics. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.025512940671554185 | 0.006378235167888546 | Positive active return (+3.97% 21s), low volatility and drawdown, supported by steepening yield curve context. |
| anthropic-claude-opus-4-8 | DIVIDEND | 25.0 | 0.06717322133660963 | 0.01679330533415241 | Strong +3.58% active return, shallow drawdown, low beta defensive equity with recent strength. |
| anthropic-claude-opus-4-8 | SP500 | 20.0 | 0.024497930475237295 | 0.0048995860950474595 | Core benchmark exposure to anchor portfolio. |
| google-gemini-3-1-pro | ENERGY | 50.0 | 0.07499997583595519 | 0.037499987917977595 | Energy sector shows strong recent momentum and benefits from rising crude prices. |
| google-gemini-3-1-pro | DIVIDEND | 50.0 | 0.06717322133660963 | 0.03358661066830482 | Dividend equities offer defensive characteristics and have shown positive recent returns. |
| openai-gpt-5-5 | OIL | 40.0 | 0.022478788567031893 | 0.008991515426812757 | Crude has the clearest one-month momentum and macro catalyst set, with Brent up sharply and energy-supply uncertainty noted, while keeping energy exposure below the 50% cap. |
| openai-gpt-5-5 | DIVIDEND | 25.0 | 0.06717322133660963 | 0.01679330533415241 | Dividend equities show positive 5-day and 21-day active strength, low drawdown, and lower beta than SPY, giving a defensive equity path to outperform if breadth remains stronger than cap-weighted growth. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | 0.09527694373226758 | 0.019055388746453517 | Healthcare has strong recent active return, a shallow drawdown, and low correlation/beta versus SPY, offering non-tech defensive equity exposure during a data-heavy month. |
| openai-gpt-5-5 | UNITED_KINGDOM | 15.0 | 0.03598638627942918 | 0.005397957941914377 | UK equities provide international diversification with positive recent returns and active strength, plus a Bank of England decision inside the scoring window. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 30.0 | -0.045134673879279275 | -0.013540402163783782 | The strongest prior relative trend is paired with a deep recent pullback, while rapid cloud growth and upcoming technology earnings provide fundamental and event support for a rebound. |
| openai-gpt-5-6-sol | NASDAQ100 | 20.0 | 0.011469521706225727 | 0.0022939043412451457 | High-quality pullback evidence and strong Alphabet operating results support recovery potential without using the full technology-cluster allowance in the higher-volatility semiconductor sleeve. |
| openai-gpt-5-6-sol | DIVIDEND | 20.0 | 0.06717322133660963 | 0.013434644267321928 | Positive short- and medium-term relative performance, low beta, and cooling labor and core-inflation data favor profitable defensive equities during a macro-heavy month. |
| openai-gpt-5-6-sol | JAPAN | 15.0 | 0.032432994734650444 | 0.004864949210197566 | A strong prior relative trend and deep pullback create rebound potential around the scheduled Bank of Japan decision. |
| openai-gpt-5-6-sol | ENERGY | 15.0 | 0.07499997583595519 | 0.011249996375393279 | Higher crude prices and Middle East supply uncertainty support sector earnings, while the modest weight limits exposure to an overextended and inventory-sensitive trade. |
| xai-grok-4-3 | SP500 | 60.0 | 0.024497930475237295 | 0.014698758285142376 | Broad diversified US equity exposure with neutral base case for the one-month window. |
| xai-grok-4-3 | ENERGY | 20.0 | 0.07499997583595519 | 0.01499999516719104 | Recent oil price strength and inventory data support relative outperformance. |
| xai-grok-4-3 | HEALTHCARE | 10.0 | 0.09527694373226758 | 0.009527694373226758 | Defensive characteristics and recent relative performance versus SPY. |
| xai-grok-4-3 | FINANCIALS | 10.0 | 0.025512940671554185 | 0.0025512940671554188 | Yield curve and rate environment supportive for sector. |
| xai-grok-4-5 | ENERGY | 30.0 | 0.07499997583595519 | 0.022499992750786558 | Oil price strength and inventory/build data support near-term energy equity continuation into FOMC and summer demand window. |
| xai-grok-4-5 | OIL | 20.0 | 0.022478788567031893 | 0.004495757713406379 | Direct crude exposure captures the recent supply-shock premium and product-supplied trends better than equities alone. |
| xai-grok-4-5 | HEALTHCARE | 25.0 | 0.09527694373226758 | 0.023819235933066896 | Defensive relative strength and lower beta provide ballast while recent active outperformance can persist on soft macro data. |
| xai-grok-4-5 | DIVIDEND | 25.0 | 0.06717322133660963 | 0.01679330533415241 | Quality dividend tilt benefits from elevated yields environment and recent relative resilience versus growth. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | ENERGY | 2 | 0.65 | 0.07499997583595519 | 0.07108659858628241 | 0.04658866811104512 | 0.18511169315450415 |  | True | True |
| xai-grok-4-5 | ENERGY | 4 | 0.58 | 0.07499997583595519 | 0.06760829173141224 | 0.04311036125617494 | 0.18859000000937431 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 4 | 0.55 | 0.09527694373226758 | 0.05665420971676869 | 0.032156279241531395 | 0.19954408202401788 |  | True | True |
| openai-gpt-5-5 | OIL | 4 | 0.56 | 0.022478788567031893 | 0.05023816744933306 | 0.025740236974095762 | 0.2059601242914535 |  | True | True |
| xai-grok-4-3 | SP500 | 4 | 0.55 | 0.024497930475237295 | 0.04177774189271559 | 0.017279811417478294 | 0.21442054984807096 |  | True | True |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 5 | 0.58 | -0.045134673879279275 | 0.01997235593912049 | -0.004525574536116805 | 0.23622593580166606 |  | False | True |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 5 | 0.58 | -0.045134673879279275 | 0.018303092030374137 | -0.006194838444863158 | 0.23789519971041242 |  | False | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | -0.004525574536116805 | 0.46826 | -0.009664661803521131 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | cb55d4f2bd27e6e6aa8e4b54096b80c92f156c975fa794fe4f628217de1709dc |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | 2d5e658cbebfeefa44652c4d94d5cdd5c716daefc0e4af9290ec368cb6731665 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | ad896ddffbd083aded4bde4f839d13b6970f67386b470cb8000a1e245a769c8d |
| market_data/universe_decision_context.md | 4f92d022627cac76ad3d705e1ace9cbd56aed71cb1031f150b981b558e9a5a0a |
| market_data/universe_decision_context.json | a879f382f94328929f2100068fe018b79c2372f70d3cf907c16bf4c1b7b93da2 |
| market_data/decision_context_source_history.json | d8899b0772c1c9fe295d971fc0ee95353d211003db593e96f9761ced71b49cac |
| market_data/universe_quality_evidence.md | 75cd3c01e1648802031e1bc3f4238d1eac758efd138ac4f97d24c673d3a3e4f4 |
| market_data/universe_quality_evidence.json | 78be4e540a94a67a40231c12b51524cbcc7f3aa6a99e1f55ea60f9a69f7040d5 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 7fb9ac9a4b425eb97ea8a28ffd7ad984a86dda5523fef6d179f6bd012c1d59a2 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 75203e137c74b00b27ca12143c55a95bc5ef73c0bd302848818844031c99a196 | yes |
| Final briefing | research/final_briefing.md | model-facing | cb55d4f2bd27e6e6aa8e4b54096b80c92f156c975fa794fe4f628217de1709dc | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
