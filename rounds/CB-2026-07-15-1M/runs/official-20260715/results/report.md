# CapitalBench Report: CB-2026-07-15-1M / official-20260715

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260715
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-15-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-15
- Decision deadline: 2026-07-16T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-15
- Exit date: 2026-08-14
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | ENERGY | 4 | 0.75 | Allocations focus on the immediate impact of the Middle East conflict on oil prices and defense spending, with gold as a safe-haven hedge. | A rapid de-escalation or diplomatic resolution in the Middle East could cause oil prices and defense stocks to reverse sharply.; The energy sector's recent strong performance could face profit-taking if the geopolitical premium fades.; Broader market sell-offs due to inflation fears or economic weakness could drag down the entire portfolio despite the specific catalysts. |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.6 | Geopolitical energy supply risk dominates the one-month window; allocations prioritize direct beneficiaries with 5% increments summing to 100%. | Rapid de-escalation or negotiated resolution of Hormuz blockade reduces oil price support; FOMC July 29 decision or July CPI release produces unexpected hawkish outcome; Weaker-than-expected Q2 GDP or retail sales data weighs on cyclical financials |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 5 | 0.61 | A concentrated geopolitical-supply portfolio offers greater one-month alpha potential than broad equities, while financials add a fundamentally supported cyclical sleeve. Allocations favor beneficiaries with catalysts likely to remain price-relevant through August 14. | A ceasefire, successful negotiations, or rapid normalization of Hormuz transit could sharply reverse oil and energy gains.; Oil demand concerns could intensify if weak U.S. labor data or China's slowing growth dominates the supply shock.; The FOMC or July inflation releases could drive yields lower and pressure financial-sector earnings expectations.; Cybersecurity's recent outperformance could reverse on crowded positioning or disappointing technology earnings.; Escalation could trigger a broad risk-off selloff that overwhelms the expected benefit to defense and energy equities. |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.58 | Soft June inflation supports risk assets, but the new blockade and Iranian threats create a more immediate supply-shock catalyst for oil-linked assets. The allocation intentionally accepts high volatility to exploit a near-term event risk that is less directly captured by the S&P 500 benchmark. | A rapid diplomatic de-escalation or restoration of normal Strait of Hormuz transit could erase the oil geopolitical risk premium and hurt OIL, ENERGY, and BROAD_COMMODITIES.; Weak U.S. or China growth data could reduce demand expectations for energy and commodities despite supply risks.; Oil futures curve effects and ETF roll costs could cause OIL to lag spot crude moves over the scoring window.; A broad equity rally led by mega-cap technology after earnings could make the S&P 500 outperform this commodity-heavy portfolio.; Energy-price increases could revive inflation concerns, lift yields, and pressure both energy equities and defense stocks through broader risk-off conditions. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 5 | 0.48 | Geopolitical energy disruption is the dominant near-term catalyst, paired with macro data that could ease policy expectations and favor cyclicals over extended growth names. The mix targets alpha from oil-linked assets and rate-sensitive financials before the August 14 exit. | Rapid de-escalation or reopening of the Strait of Hormuz would reverse oil and energy gains; Hawkish FOMC surprise on July 29 despite soft data could pressure equities and financials; High volatility in OIL and BIOTECH could produce sharp drawdowns if risk appetite fades; Further energy-price spikes could re-accelerate inflation readings and reverse the soft-data narrative |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.5 | Geopolitical energy supply disruption plus strong financial-sector earnings favor an energy/value/financials tilt over mega-cap growth, which faces earnings and rate-path risk during the window. | Rapid Hormuz de-escalation or negotiated resolution could unwind the oil risk premium and hurt energy and commodity positions; Strong mega-cap tech earnings (Alphabet, Microsoft, Meta, TSMC) could drive SPY higher via growth, causing this value/energy tilt to lag the benchmark; Hawkish FOMC surprise on July 29 amid sticky 3.5% YoY CPI could pressure financials and cyclical value; Oil demand destruction or Chinese growth slowdown (Q2 GDP 4.3%) could cap energy gains despite supply risk |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Overweight financials on earnings momentum, energy on Hormuz supply risk, and value/equal-weight on rotation, balanced by defensive healthcare. | Rapid de-escalation in the Strait of Hormuz could reverse oil and energy gains sharply; Disappointing bank or mega-cap earnings (Alphabet, Microsoft, Meta) could pressure financials and broad market; Hawkish FOMC July 28-29 or hot July CPI/PPI could lift rates and hurt cyclicals and value; Value/financials rotation could reverse if growth leadership resumes |
| anthropic-claude-opus-4-7 | anthropic | portfolio | FINANCIALS | 5 | 0.6 | Barbell of cyclical value (financials, energy) with defensive healthcare/biotech and short-duration cash, positioned for earnings-driven rotation away from crowded mega-cap tech which shows negative 30d returns and elevated drawdowns. | Hormuz de-escalation would reverse energy premium and hurt XLE overweight; Hawkish FOMC on July 29 could pressure financials and value cyclicals; Biotech recent strength may reverse without briefing-supported catalysts (momentum reversal risk); Mega-cap tech earnings (Alphabet, Microsoft, Meta) surprise could drive SPY higher while portfolio underweights QQQ; Oil spike passthrough could re-accelerate CPI and pressure duration-sensitive equity sectors |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| METALS_MINING | Metals and Mining | 103.2 | 117.14 | 0.13507751937984502 | 1 |
| SILVER | Silver | 52.21 | 58.48 | 0.12009193641064919 | 2 |
| SOFTWARE | Software | 93.94 | 104.08 | 0.10794123908878017 | 3 |
| ENERGY | Energy Sector | 56.5 | 61.91 | 0.09575221238938036 | 4 |
| GOLD | Gold | 76.28 | 82.28 | 0.07865757734661782 | 5 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 121.52 | 130.39 | 0.07299210006583268 | 6 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.42 | 253.215 | 0.07103882920226723 | 7 |
| CYBERSECURITY | Cybersecurity | 93.09 | 99.6 | 0.06993232355784706 | 8 |
| DIVIDEND | US Dividend Equities | 32.34 | 34.52 | 0.06740878169449593 | 9 |
| SOUTH_AFRICA | South Africa Equities | 63.74 | 67.53 | 0.05946030749921549 | 10 |
| HEALTHCARE | Healthcare Sector | 158.29 | 167.37 | 0.05736306778697342 | 11 |
| BROAD_AI_TECH | Broad AI Technology | 61.12 | 64.2 | 0.050392670157068054 | 12 |
| JAPAN | Japan Equities | 93.5 | 98.21 | 0.050374331550802065 | 13 |
| SOUTH_KOREA | South Korea Equities | 171.64 | 179.74 | 0.047191796783966566 | 14 |
| TECHNOLOGY | Technology Sector | 181.58 | 190.01 | 0.046425817821345916 | 15 |
| CANADA | Canada Equities | 59.49 | 62.23 | 0.046058161035468004 | 16 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.97 | 222.77 | 0.046015870779922086 | 17 |
| LARGE_VALUE | US Large-Cap Value | 247.28 | 258.57 | 0.045656745389841547 | 18 |
| TAIWAN | Taiwan Equities | 102.49 | 107.07 | 0.044687286564542905 | 19 |
| BROAD_COMMODITIES | Broad Commodities | 17.17 | 17.91 | 0.043098427489807634 | 20 |
| OIL | Crude Oil | 121.38 | 126.6 | 0.043005437469105345 | 21 |
| MATERIALS | Materials Sector | 50.5 | 52.54 | 0.04039603960396043 | 22 |
| MID_CAP | US Mid-Cap Stocks | 75.63 | 78.67 | 0.04019568954118746 | 23 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.82 | 73.58 | 0.03897204179610281 | 24 |
| EUROPE | Europe Equities | 89.12 | 92.37 | 0.03646768402154388 | 25 |
| INDUSTRIALS | Industrials Sector | 180.06 | 186.51 | 0.03582139286904362 | 26 |
| COPPER | Copper | 38.63 | 40.01 | 0.03572353093450675 | 27 |
| UNITED_KINGDOM | United Kingdom Equities | 46.77 | 48.26 | 0.03185802865084453 | 28 |
| SMALL_CAP | US Small-Cap Stocks | 295.77 | 305.09 | 0.03151097136288339 | 29 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.47 | 86.09 | 0.031388522822570986 | 30 |
| TOTAL_US_MARKET | Total US Stock Market | 372.42 | 383.85 | 0.030691155147414273 | 31 |
| AUSTRALIA | Australia Equities | 28.8 | 29.65 | 0.02951388888888884 | 32 |
| SP500 | S&P 500 | 754.81 | 776.34 | 0.02852373444972911 | 33 |
| REGIONAL_BANKS | Regional Banks | 75.78 | 77.93 | 0.028371602005806462 | 34 |
| FINANCIALS | Financials Sector | 56.56 | 58.16 | 0.028288543140028155 | 35 |
| SMALL_VALUE | US Small-Cap Value | 221.29 | 227.43 | 0.027746396131772766 | 36 |
| INDIA | India Equities | 48.72 | 49.78 | 0.021756978653530323 | 37 |
| YEN | Japanese Yen | 56.53 | 57.58 | 0.018574208384928292 | 38 |
| NASDAQ100 | Nasdaq 100 | 717.74 | 731.07 | 0.018572184913757228 | 39 |
| REAL_ESTATE | Real Estate Sector | 44.56 | 45.27 | 0.015933572710951527 | 40 |
| MOMENTUM | US Momentum Equities | 312.67 | 317.21 | 0.014520101065020441 | 41 |
| LARGE_GROWTH | US Large-Cap Growth | 123.58 | 125.29 | 0.0138371904838972 | 42 |
| LOW_VOL | US Low Volatility Equities | 75.3300617135 | 76.36 | 0.013672340936306648 | 43 |
| EMERGING_MARKETS | Emerging Markets | 59.48 | 60.11 | 0.010591795561533335 | 44 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.0 | 118.2 | 0.01025641025641022 | 45 |
| EURO | Euro | 105.7275605799 | 106.79 | 0.010048840758953403 | 46 |
| CHINA | China Equities | 54.15 | 54.63 | 0.008864265927977844 | 47 |
| BIOTECH | Biotechnology | 156.22 | 157.41 | 0.007617462552810039 | 48 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.425153037 | 79.71 | 0.003586357118724015 | 49 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.2475638394 | 91.53 | 0.0030952734376239466 | 50 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 51 |
| TIPS | Treasury Inflation-Protected Securities | 107.2825146178 | 106.99 | -0.0027265824150571882 | 52 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.3139503315 | 95.05 | -0.0027692728145458645 | 53 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.4858446477 | 93.2 | -0.0030576249139878664 | 54 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.8005558499 | 97.48 | -0.0032776485482552964 | 55 |
| COMMUNICATIONS | Communication Services Sector | 113.38 | 112.95 | -0.0037925560063503116 | 56 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.9113233316 | 47.72 | -0.003993280049391035 | 57 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.4602605873 | 93.04 | -0.004496676819207401 | 58 |
| US_DOLLAR | US Dollar | 28.25 | 28.11 | -0.004955752212389419 | 59 |
| SEMICONDUCTORS | Semiconductors | 590.77 | 587.82 | -0.004993483081402128 | 60 |
| MEXICO | Mexico Equities | 75.39 | 75.01 | -0.0050404562939381226 | 61 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.4709301625 | 105.86 | -0.005737999673409155 | 62 |
| AGRICULTURE | Agriculture Commodities | 27.98 | 27.77 | -0.007505360972122954 | 63 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.118079906 | 106.12 | -0.009317567182644204 | 64 |
| UTILITIES | Utilities Sector | 45.22 | 44.31 | -0.020123839009287825 | 65 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.9026600605 | 82.04 | -0.022200250375338237 | 66 |
| ETHEREUM_ETF | Ethereum ETF | 14.52 | 14.18 | -0.023415977961432466 | 67 |
| BITCOIN_ETF | Bitcoin ETF | 36.81 | 35.63 | -0.03205650638413471 | 68 |
| BRAZIL | Brazil Equities | 35.88 | 33.93 | -0.05434782608695665 | 69 |
| SOLAR | Solar Energy | 55.8 | 51.97 | -0.06863799283154115 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | 0.09575221238938036 | 0.028725663716814107 | Active Strait of Hormuz blockade, missile alerts, and Iran export threats support elevated oil prices; energy equities benefit directly while remaining less volatile than crude futures. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.028288543140028155 | 0.005657708628005631 | Strong Q2 bank/asset-manager earnings (BlackRock, BNY Mellon beats), sector at 52-week high, and continued earnings season catalysts through the window. |
| anthropic-claude-fable-5 | BROAD_COMMODITIES | 15.0 | 0.043098427489807634 | 0.006464764123471145 | Diversified hedge against Middle East supply disruption and elevated headline inflation; negative beta to equities offers protection if conflict escalates. |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.045656745389841547 | 0.011414186347460387 | Value tilt (energy, financials, defensives) outperforming with lower beta; cooling CPI/PPI supports a dovish-leaning FOMC July 29 without relying on rate-sensitive mega-cap growth. |
| anthropic-claude-fable-5 | SHORT_TREASURY | 10.0 | 0.0030952734376239466 | 0.00030952734376239467 | Low-risk ballast given geopolitical uncertainty and stretched tech valuations into mega-cap earnings. |
| anthropic-claude-opus-4-7 | FINANCIALS | 30.0 | 0.028288543140028155 | 0.008486562942008447 | Strong earnings momentum (BlackRock, BNY Mellon beats), best 30d sector performance +5.97%, benefiting from steep yield curve and stable credit quality per Beige Book. |
| anthropic-claude-opus-4-7 | ENERGY | 20.0 | 0.09575221238938036 | 0.019150442477876076 | Strait of Hormuz blockade and CENTCOM strikes create tangible supply risk; Brent at $85, oil +8% weekly. Hedge against geopolitical escalation over the window. |
| anthropic-claude-opus-4-7 | BIOTECH | 15.0 | 0.007617462552810039 | 0.0011426193829215058 | Strong 30d momentum +14.6% with 70% up-day share suggests factor rotation; healthcare sector also +4% on month with defensive characteristics. |
| anthropic-claude-opus-4-7 | LARGE_VALUE | 20.0 | 0.045656745389841547 | 0.00913134907796831 | Value outperforming growth with lower volatility (11%) and beta 0.73; benefits from financials/energy tilt and defensive positioning into FOMC. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.0030952734376239466 | 0.000464291015643592 | Dry powder ahead of FOMC July 29, July CPI Aug 12, and geopolitical tail risk; yields ~4.5% annualized with minimal duration risk. |
| anthropic-claude-opus-4-8 | FINANCIALS | 30.0 | 0.028288543140028155 | 0.008486562942008447 | Strong earnings momentum (BlackRock +6.6%, BNY +5.1%), broadening sector at 52w high, favorable disinflation and stable credit quality per Beige Book, with heavy July bank earnings season as catalyst. |
| anthropic-claude-opus-4-8 | ENERGY | 20.0 | 0.09575221238938036 | 0.019150442477876076 | Strait of Hormuz blockade, Iran export threats, and renewed US military strikes create near-term oil supply risk; Brent above $84 and XLE has negative beta providing geopolitical hedge into the window. |
| anthropic-claude-opus-4-8 | LARGE_VALUE | 20.0 | 0.045656745389841547 | 0.00913134907796831 | Value leadership with low volatility and near 52w highs; benefits from disinflation, cyclical/financial tilt, and rotation away from stretched mega-cap tech showing recent 30d weakness. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 15.0 | 0.046015870779922086 | 0.0069023806169883125 | Diversified broad-market exposure with reduced mega-cap tech concentration risk amid soft QQQ/SMH 30d returns; supported by broadening leadership across sectors. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 15.0 | 0.05736306778697342 | 0.008604460168046012 | Defensive low-beta sector with recent 30d outperformance (+3.99%), supported by disinflation backdrop and biotech strength; positive relative return vs SPX with downside protection. |
| google-gemini-3-1-pro | ENERGY | 40.0 | 0.09575221238938036 | 0.03830088495575215 | The reimposed blockade on Iranian ports and threats to halt Middle East energy exports create a strong near-term catalyst for energy prices, supporting the energy sector. |
| google-gemini-3-1-pro | OIL | 30.0 | 0.043005437469105345 | 0.012901631240731603 | Direct exposure to crude oil prices, which are likely to rise due to the Strait of Hormuz blockade and military strikes. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 15.0 | 0.07103882920226723 | 0.010655824380340084 | Increased military activity in the Middle East and missile alerts in Bahrain and Kuwait provide a catalyst for defense equities. |
| google-gemini-3-1-pro | GOLD | 15.0 | 0.07865757734661782 | 0.011798636601992674 | Geopolitical uncertainty and military conflict in the Middle East typically drive safe-haven demand for gold. |
| openai-gpt-5-5 | OIL | 45.0 | 0.043005437469105345 | 0.019352446861097407 | Direct exposure to crude prices amid the renewed U.S. blockade of Iranian ports, additional strikes, and unresolved Strait of Hormuz transit and energy-flow risks before the exit date. |
| openai-gpt-5-5 | ENERGY | 25.0 | 0.09575221238938036 | 0.02393805309734509 | Energy equities should benefit if elevated crude prices persist, while recent sector strength is supported by the supplied geopolitical supply shock rather than price history alone. |
| openai-gpt-5-5 | BROAD_COMMODITIES | 15.0 | 0.043098427489807634 | 0.006464764123471145 | Diversified commodity exposure adds participation in an inflation and supply-risk repricing while reducing reliance on a single futures product. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 10.0 | 0.07103882920226723 | 0.0071038829202267235 | Defense equities have a plausible near-term catalyst from ongoing Middle East military activity and policy focus, despite limited recent momentum support in the price table. |
| openai-gpt-5-5 | US_DOLLAR | 5.0 | -0.004955752212389419 | -0.00024778761061947097 | Small diversifier that may benefit from geopolitical risk aversion and relative-rate support if the oil shock pressures global risk assets. |
| openai-gpt-5-6-sol | ENERGY | 35.0 | 0.09575221238938036 | 0.03351327433628312 | The renewed Hormuz blockade and threats to regional exports create a direct near-term earnings and risk-premium catalyst, while energy equities remain well below their 52-week high. |
| openai-gpt-5-6-sol | OIL | 25.0 | 0.043005437469105345 | 0.010751359367276336 | Unresolved shipping conditions and military escalation threaten a major supply route, giving crude the portfolio's most immediate one-month catalyst despite substantial volatility. |
| openai-gpt-5-6-sol | FINANCIALS | 20.0 | 0.028288543140028155 | 0.005657708628005631 | Recent asset-manager and custody-bank earnings were strong, while moderate economic growth, stable commercial-loan quality, and a still-high 10-year yield support sector earnings. |
| openai-gpt-5-6-sol | CYBERSECURITY | 10.0 | 0.06993232355784706 | 0.006993232355784707 | Heightened geopolitical conflict can accelerate security demand, while the theme's recent relative strength has an identifiable operational catalyst rather than price momentum alone. |
| openai-gpt-5-6-sol | AEROSPACE_DEFENSE | 10.0 | 0.07103882920226723 | 0.0071038829202267235 | Ongoing U.S. strikes and regional missile activity can raise expectations for replenishment and defense demand; recent weakness limits the degree of crowded momentum exposure. |
| xai-grok-4-3 | ENERGY | 50.0 | 0.09575221238938036 | 0.04787610619469018 | US military blockade and Iranian threats to halt Middle East energy exports create unresolved supply risk through the scoring window, supporting oil prices and energy equities. |
| xai-grok-4-3 | OIL | 30.0 | 0.043005437469105345 | 0.012901631240731603 | Direct crude exposure benefits from Brent trading above $86 and ongoing Hormuz military activity that can affect flows before August 14 close. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.028288543140028155 | 0.005657708628005631 | BlackRock and other financial names reported strong results with asset inflows; sector showed recent outperformance amid stable loan quality in Beige Book. |
| xai-grok-4-5 | ENERGY | 35.0 | 0.09575221238938036 | 0.03351327433628312 | Strait of Hormuz blockade, Iranian threats to halt Middle East energy exports, and renewed US strikes create near-term upside for energy equities via higher oil prices and supply risk before the August 14 close. |
| xai-grok-4-5 | OIL | 25.0 | 0.043005437469105345 | 0.010751359367276336 | Direct crude exposure benefits from the same Hormuz military escalation and shipping disruptions that already lifted Brent above $86; unresolved transit conditions can drive further price gains in the scoring window. |
| xai-grok-4-5 | FINANCIALS | 20.0 | 0.028288543140028155 | 0.005657708628005631 | Soft June CPI/PPI and modest payrolls raise odds of a dovish FOMC outcome on July 29, supporting bank and capital-markets valuations; recent relative strength aligns with stable commercial loan quality noted in the Beige Book. |
| xai-grok-4-5 | BIOTECH | 10.0 | 0.007617462552810039 | 0.000761746255281004 | Strong 30-day relative performance coincides with risk-on potential from cooler inflation data and upcoming earnings catalysts; healthcare sector resilience provides independent support beyond pure price momentum. |
| xai-grok-4-5 | LARGE_VALUE | 10.0 | 0.045656745389841547 | 0.004565674538984155 | Value tilt captures financials/energy cyclical exposure while offering lower beta than pure growth amid geopolitical uncertainty and potential rate-path shifts after soft labor and inflation prints. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | ENERGY | 4 | 0.75 | 0.09575221238938036 | 0.07365697717881652 | 0.045133242729087406 | 0.06142054220102851 |  | True | True |
| xai-grok-4-3 | ENERGY | 3 | 0.6 | 0.09575221238938036 | 0.06643544606342741 | 0.0379117116136983 | 0.06864207331641761 |  | True | True |
| openai-gpt-5-6-sol | ENERGY | 5 | 0.61 | 0.09575221238938036 | 0.06401945760757652 | 0.03549572315784741 | 0.0710580617722685 |  | True | True |
| openai-gpt-5-5 | OIL | 5 | 0.58 | 0.043005437469105345 | 0.0566113593915209 | 0.02808762494179179 | 0.07846615998832412 |  | True | True |
| xai-grok-4-5 | ENERGY | 5 | 0.48 | 0.09575221238938036 | 0.05524976312583025 | 0.02672602867610114 | 0.07982775625401478 |  | True | True |
| anthropic-claude-fable-5 | ENERGY | 5 | 0.5 | 0.09575221238938036 | 0.05257185015951367 | 0.02404811570978456 | 0.08250566922033135 |  | True | True |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.55 | 0.028288543140028155 | 0.052275195282887155 | 0.023751460833158045 | 0.08280232409695787 |  | True | True |
| anthropic-claude-opus-4-7 | FINANCIALS | 5 | 0.6 | 0.028288543140028155 | 0.038375264896417925 | 0.009851530446688815 | 0.09670225448342709 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 130ef09ad868dca29018495a4daf32bb30e7f47a5873f810467f0dc58dcb3ad2 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | c73683bc9fa820808708505bc28db84aeb8dccf21e56f8658bdec17cb0e5b086 |
| market_data/universe_trailing_returns.csv | c45d51366ea39e3dace3fbbaa72081356693ad996f8dec2a85e6ace48d9aad42 |
| market_data/universe_trailing_returns.md | 750726f4a01e525469b385a5bfaee106c6b10786ed245b27ef197ef99d772531 |
| market_data/universe_trailing_returns.json | a0bd466bf6639146447fe816d00a96742237b71fb244061419ede84c1a8b5d9a |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | ad0121f75e3b1e62c7db063d83eceb9ae8621e09073917b678ae5fc47986bc29 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 2e61d9e43cee520dc284192780592a786e8a31c4d4ff667b9686f43ef4d84867 | yes |
| Final briefing | research/final_briefing.md | model-facing | 130ef09ad868dca29018495a4daf32bb30e7f47a5873f810467f0dc58dcb3ad2 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
