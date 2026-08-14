# CapitalBench Report: CB-2026-07-13-1M / official-20260713

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260713
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-13-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-13
- Decision deadline: 2026-07-14T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-13
- Exit date: 2026-08-13
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | OIL | 4 | 0.85 | Overweight oil, energy, defense, and gold to profit from the US-Iran conflict and Strait of Hormuz blockade. | A sudden diplomatic de-escalation or lifting of the blockade could cause a sharp reversal in oil prices.; A broader macroeconomic shock or aggressive Fed tightening could drag down all equity sectors, including energy and defense.; Rising real interest rates could pressure gold prices despite its safe-haven appeal. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 5 | 0.58 | Geopolitical oil risk is the dominant near-term price driver; pair with relative-strength sectors less exposed to growth/tech drawdowns ahead of FOMC and CPI prints. | Rapid de-escalation or free transit restoration in Hormuz could reverse oil/energy gains; Higher-than-expected June/July CPI or hawkish FOMC could pressure equities and rates-sensitive holdings; Weak bank earnings or further soft labor data could undermine financials allocation; Broad risk-off from Asia equity weakness or tech spillover could drag even value/energy names |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.65 | Energy positioned for continued Hormuz-driven gains; financials and healthcare provide relative stability ahead of FOMC and CPI releases. | Rapid de-escalation in Hormuz reducing oil prices before exit date; Weaker-than-expected Q2 GDP or July employment data pressuring cyclicals; FOMC signaling tighter policy on persistent inflation |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.46 | Over the July 13 to August 13 window, the highest-conviction relative opportunity is an energy/geopolitical shock trade rather than broad equity beta. The allocation emphasizes crude and energy producers, with commodity, dollar, and defense complements. | A rapid diplomatic de-escalation or uninterrupted Strait of Hormuz transit could reverse the oil spike and hurt OIL, ENERGY, and BROAD_COMMODITIES.; A weak global growth signal from payrolls, GDP, or earnings could pressure oil demand expectations and energy equities despite supply risk.; Hot CPI or hawkish FOMC communication could tighten financial conditions enough to weigh on equities, including energy and defense stocks.; Oil futures curve dynamics and ETF roll costs could cause OIL to underperform spot crude over the month.; If mega-cap technology rebounds sharply after earnings, this defensive commodity-heavy portfolio could lag the S&P 500. |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 5 | 0.61 | Geopolitical supply disruption, persistent inflation, and high Treasury yields favor energy and the dollar over duration-sensitive growth. Financials and healthcare add earnings catalysts and broader sector diversification. | A rapid ceasefire, restored Hormuz transit, or reversal of the blockade could sharply unwind oil and energy gains.; June or July inflation could undershoot expectations, lowering yields and rotating leadership back toward long-duration technology.; Weak bank earnings, deposit pressure, or deteriorating credit quality could outweigh benefits from higher rates.; A sharper labor-market slowdown could reduce oil demand expectations and pressure cyclical equities.; Oil's recent 12.9% weekly surge raises substantial short-term reversal and futures-curve risk. |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.5 | Overweight energy and value for the oil supply shock and inflation backdrop, with low-vol and T-bill ballast against geopolitically driven equity weakness; underweight rate-sensitive growth. | Rapid de-escalation or negotiated Hormuz resolution could crater crude prices and reverse energy gains; A soft June/July CPI print could rally growth/tech and QQQ, causing this value/energy tilt to lag SPY; Demand destruction from an oil shock could hit energy equities alongside broad markets; USO futures roll and volatility can erode returns even if spot crude stays elevated |
| anthropic-claude-opus-4-7 | anthropic | portfolio | ENERGY | 5 | 0.55 | Barbell: energy upside from Strait of Hormuz escalation plus defensive low-beta sectors (healthcare, low-vol) and financials into earnings, with short T-bills as ballast against rate and geopolitical volatility. | Hormuz de-escalation collapses oil premium and XLE; Hot June/July CPI triggers hawkish Fed repricing hurting all equities; Bank earnings disappoint on credit or NIM, hitting XLF; Healthcare policy or drug-pricing headline reverses recent XLV strength |
| anthropic-claude-opus-4-8 | anthropic | portfolio | ENERGY | 5 | 0.55 | Defensive rotation into energy, healthcare, financials, low-vol equity plus short-duration Treasuries to capture geopolitical/oil upside while limiting exposure to the fading tech/growth leadership. | Strait of Hormuz de-escalates quickly, reversing the oil/energy trade; Tech/semiconductor rebound drives SPY higher, causing defensive tilt to underperform the benchmark; Bank Q2 earnings disappoint, pressuring the financials allocation; A dovish FOMC on July 29 sparks a growth/tech rally that low-vol and cash miss |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOFTWARE | Software | 92.7 | 106.28 | 0.1464940668824164 | 1 |
| METALS_MINING | Metals and Mining | 102.09 | 115.27 | 0.12910177294544023 | 2 |
| SILVER | Silver | 52.16 | 58.16 | 0.11503067484662588 | 3 |
| CYBERSECURITY | Cybersecurity | 91.84 | 102.2 | 0.11280487804878048 | 4 |
| GOLD | Gold | 75.25 | 81.78 | 0.08677740863787387 | 5 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 120.7 | 130.1 | 0.07787903893951942 | 6 |
| ENERGY | Energy Sector | 56.74 | 61.06 | 0.07613676418752213 | 7 |
| SOUTH_AFRICA | South Africa Equities | 62.76 | 67.33 | 0.07281708094327599 | 8 |
| ETHEREUM_ETF | Ethereum ETF | 13.37 | 14.23 | 0.06432311144353031 | 9 |
| SOUTH_KOREA | South Korea Equities | 168.02 | 178.62 | 0.06308772765147008 | 10 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.05 | 249.69 | 0.06228462029355453 | 11 |
| JAPAN | Japan Equities | 92.72 | 98.47 | 0.062014667817083646 | 12 |
| OIL | Crude Oil | 117.79 | 125.03 | 0.06146531963664148 | 13 |
| DIVIDEND | US Dividend Equities | 32.56 | 34.43 | 0.057432432432432456 | 14 |
| CANADA | Canada Equities | 58.73 | 62.1 | 0.05738123616550328 | 15 |
| TAIWAN | Taiwan Equities | 101.88 | 107.5 | 0.05516293678837858 | 16 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.76 | 73.54 | 0.054185779816513735 | 17 |
| BROAD_AI_TECH | Broad AI Technology | 61.3 | 64.62 | 0.054159869494290414 | 18 |
| TECHNOLOGY | Technology Sector | 181.28 | 190.77 | 0.05234995586937341 | 19 |
| BROAD_COMMODITIES | Broad Commodities | 16.9 | 17.77 | 0.05147928994082851 | 20 |
| EUROPE | Europe Equities | 87.86 | 92.38 | 0.051445481447757846 | 21 |
| COPPER | Copper | 37.94 | 39.85 | 0.05034264628360585 | 22 |
| AUSTRALIA | Australia Equities | 28.35 | 29.74 | 0.04902998236331557 | 23 |
| LARGE_VALUE | US Large-Cap Value | 247.62 | 258.7 | 0.044745981746223906 | 24 |
| HEALTHCARE | Healthcare Sector | 161.41 | 168.38 | 0.043181958986431956 | 25 |
| MID_CAP | US Mid-Cap Stocks | 75.24 | 78.42 | 0.04226475279106867 | 26 |
| UNITED_KINGDOM | United Kingdom Equities | 46.36 | 48.26 | 0.040983606557376984 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.23 | 222.73 | 0.03967698268216413 | 28 |
| TOTAL_US_MARKET | Total US Stock Market | 369.78 | 384.3 | 0.03926659094596796 | 29 |
| FINANCIALS | Financials Sector | 56.07 | 58.26 | 0.03905831995719633 | 30 |
| SP500 | S&P 500 | 749.17 | 777.88 | 0.03832241013388149 | 31 |
| CHINA | China Equities | 52.53 | 54.42 | 0.03597944031981726 | 32 |
| REGIONAL_BANKS | Regional Banks | 75.12 | 77.75 | 0.03501064962726308 | 33 |
| MATERIALS | Materials Sector | 50.58 | 52.31 | 0.03420324238829586 | 34 |
| SMALL_CAP | US Small-Cap Stocks | 293.48 | 303.5 | 0.03414201989914134 | 35 |
| LARGE_GROWTH | US Large-Cap Growth | 121.59 | 125.66 | 0.033473147462784736 | 36 |
| SMALL_VALUE | US Small-Cap Value | 219.78 | 226.77 | 0.03180453180453191 | 37 |
| INDUSTRIALS | Industrials Sector | 180.37 | 185.79 | 0.030049343017131358 | 38 |
| NASDAQ100 | Nasdaq 100 | 711.74 | 732.07 | 0.028563801388147514 | 39 |
| EMERGING_MARKETS | Emerging Markets | 58.79 | 60.34 | 0.02636502806599772 | 40 |
| INDIA | India Equities | 48.79 | 49.98 | 0.024390243902439046 | 41 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.04 | 118.45 | 0.020768700448121402 | 42 |
| YEN | Japanese Yen | 56.46 | 57.53 | 0.018951470067304355 | 43 |
| BITCOIN_ETF | Bitcoin ETF | 35.22 | 35.88 | 0.01873935264054527 | 44 |
| MEXICO | Mexico Equities | 74.15 | 75.45 | 0.017532029669588667 | 45 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.59 | 86.0 | 0.01666863695472265 | 46 |
| EURO | Euro | 104.9281838815 | 106.3994 | 0.014021172044314634 | 47 |
| BIOTECH | Biotechnology | 155.34 | 156.86 | 0.009784987768765463 | 48 |
| REAL_ESTATE | Real Estate Sector | 44.7 | 45.12 | 0.009395973154362247 | 49 |
| COMMUNICATIONS | Communication Services Sector | 111.59 | 112.55 | 0.008602921408728426 | 50 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.1365514284 | 79.79 | 0.008257228294705543 | 51 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.9179353282 | 93.49 | 0.006156665769416536 | 52 |
| SEMICONDUCTORS | Semiconductors | 585.62 | 589.12 | 0.005976571838393507 | 53 |
| MOMENTUM | US Momentum Equities | 314.63 | 316.03 | 0.004449671042176417 | 54 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.9654714574 | 95.36 | 0.004154441993972302 | 55 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.971931224 | 93.3 | 0.0035286862570336197 | 56 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.372043123 | 97.69 | 0.003265381590056071 | 57 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.2276233753 | 91.51 | 0.0030952973918694227 | 58 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.7716692557 | 47.91 | 0.0028956648669649088 | 59 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.5007420222 | 106.55 | 0.00046251300098676396 | 60 |
| TIPS | Treasury Inflation-Protected Securities | 107.1236805071 | 107.16 | 0.00033904261623640686 | 61 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 62 |
| LOW_VOL | US Low Volatility Equities | 76.2683187429 | 76.23 | -0.0005024201861477673 | 63 |
| AGRICULTURE | Agriculture Commodities | 27.72 | 27.62 | -0.003607503607503504 | 64 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.61055109 | 106.16 | -0.004226139771284498 | 65 |
| US_DOLLAR | US Dollar | 28.5 | 28.18 | -0.011228070175438587 | 66 |
| SOLAR | Solar Energy | 53.12 | 52.47 | -0.012236445783132543 | 67 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.6337412783 | 82.59 | -0.01247990658252185 | 68 |
| UTILITIES | Utilities Sector | 45.72 | 44.04 | -0.03674540682414695 | 69 |
| BRAZIL | Brazil Equities | 35.39 | 33.77 | -0.04577564283695956 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | 0.07613676418752213 | 0.02284102925625664 | Direct beneficiary of Hormuz blockade escalation and Brent at $83; equities lag spot crude and offer upside with less curve decay than USO. |
| anthropic-claude-fable-5 | OIL | 10.0 | 0.06146531963664148 | 0.006146531963664149 | Highest-torque exposure to supply disruption from the July 14 blockade; negative beta to SPY hedges equity drawdown. |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.044745981746223906 | 0.011186495436555977 | Value with energy/financials tilt outperforms growth when 10y yields rise to 4.61% and inflation runs 4.2%. |
| anthropic-claude-fable-5 | LOW_VOL | 20.0 | -0.0005024201861477673 | -0.00010048403722955346 | Defensive equity holding up well (+2.8% 30d vs SPY) amid geopolitical stress and rate pressure; near-zero beta cushions selloff. |
| anthropic-claude-fable-5 | SHORT_TREASURY | 15.0 | 0.0030952973918694227 | 0.00046429460878041337 | Cash-like yield with no duration risk while yields rise and rate-cut odds fade on hot CPI. |
| anthropic-claude-opus-4-7 | ENERGY | 30.0 | 0.07613676418752213 | 0.02284102925625664 | Hormuz blockade escalation and 20% cargo toll announcement; Brent +9.6%, oil supply risk into exit window with XLE lagging spot. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 20.0 | 0.043181958986431956 | 0.008636391797286392 | Defensive with strong recent momentum (+5.4% 30d, +4.14% vs SPY); low beta hedge amid tech drawdown and geopolitical risk. |
| anthropic-claude-opus-4-7 | LOW_VOL | 15.0 | -0.0005024201861477673 | -7.536302792216509e-05 | Defensive factor outperforming; near-zero beta helps hedge rate/geopolitical shock into FOMC and CPI prints. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.0030952973918694227 | 0.00046429460878041337 | Dry powder given 10Y yield rising to 4.61%, sticky CPI (4.2%), and unresolved Hormuz situation. |
| anthropic-claude-opus-4-7 | FINANCIALS | 20.0 | 0.03905831995719633 | 0.0078116639914392666 | Steepening curve, big-bank Q2 earnings catalyst next week, strong recent relative strength (+4.23% vs SPY 30d). |
| anthropic-claude-opus-4-8 | ENERGY | 25.0 | 0.07613676418752213 | 0.019034191046880533 | Strait of Hormuz blockade set to resume July 14, oil up sharply, Brent up 9.6%; energy equities have negative beta to broad market and direct catalyst upside if disruption persists. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | 0.043181958986431956 | 0.008636391797286392 | Defensive sector with strong 30d relative outperformance (+4.14%), low beta 0.35, benefits from rotation amid rising rates and tech weakness. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | 0.03905831995719633 | 0.0078116639914392666 | Strong recent momentum (+5.49% 30d, +4.23% vs SPY), Q2 bank earnings July 14-17 as near-term catalyst, benefits from higher yields. |
| anthropic-claude-opus-4-8 | LOW_VOL | 20.0 | -0.0005024201861477673 | -0.00010048403722955346 | Defensive tilt with near-zero beta, positive relative performance; hedges against tech-led drawdown and geopolitical volatility. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.0030952973918694227 | 0.00046429460878041337 | Cash-like ballast amid rising 10yr yields (4.61%), sticky inflation (core 2.9%), and unresolved Hormuz shock; preserves capital with positive carry. |
| google-gemini-3-1-pro | OIL | 30.0 | 0.06146531963664148 | 0.018439595890992443 | Directly benefits from the announced US blockade of Iranian shipping and conflict in the Strait of Hormuz, which threatens global oil supply. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.07613676418752213 | 0.02284102925625664 | Provides equity exposure to rising crude prices while offering some diversification compared to direct commodity holdings. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 20.0 | 0.06228462029355453 | 0.012456924058710905 | Positioned to benefit from the direct military engagement between the US and Iran and the enforcement of the naval blockade. |
| google-gemini-3-1-pro | GOLD | 20.0 | 0.08677740863787387 | 0.017355481727574774 | Acts as a safe-haven asset amid severe geopolitical escalation and rising inflation concerns. |
| openai-gpt-5-5 | OIL | 45.0 | 0.06146531963664148 | 0.027659393836488667 | Direct exposure to crude prices, with unresolved Strait of Hormuz blockade and transit-risk headlines creating a plausible near-term upside catalyst before the exit date. |
| openai-gpt-5-5 | ENERGY | 25.0 | 0.07613676418752213 | 0.019034191046880533 | Energy equities should benefit from sustained higher oil prices while offering somewhat less futures-curve and daily volatility risk than pure crude exposure. |
| openai-gpt-5-5 | BROAD_COMMODITIES | 15.0 | 0.05147928994082851 | 0.007721893491124276 | Diversified commodity exposure adds participation in energy-led inflation and supply-risk repricing without relying solely on crude oil. |
| openai-gpt-5-5 | US_DOLLAR | 10.0 | -0.011228070175438587 | -0.0011228070175438587 | Higher Treasury yields, geopolitical stress, and potentially sticky inflation support dollar strength as a partial hedge against equity weakness. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 5.0 | 0.06228462029355453 | 0.0031142310146777263 | Geopolitical escalation and defense-spending attention may support a rebound after the recent pullback. |
| openai-gpt-5-6-sol | ENERGY | 35.0 | 0.07613676418752213 | 0.026647867465632746 | Hormuz disruption and the renewed blockade create a near-term earnings and cash-flow tailwind for energy producers, with less futures-curve risk than direct oil exposure. |
| openai-gpt-5-6-sol | OIL | 25.0 | 0.06146531963664148 | 0.01536632990916037 | Unresolved control of Hormuz and imminent resumption of the blockade provide the strongest explicit one-month supply catalyst despite high volatility. |
| openai-gpt-5-6-sol | FINANCIALS | 15.0 | 0.03905831995719633 | 0.00585874799357945 | Major-bank earnings are immediate catalysts, while a 4.61% 10-year yield and recent relative strength support the sector, subject to credit risk. |
| openai-gpt-5-6-sol | HEALTHCARE | 15.0 | 0.043181958986431956 | 0.006477293847964793 | Recent broad participation and defensive characteristics offer diversification against weakening labor data and growth-stock pressure. |
| openai-gpt-5-6-sol | US_DOLLAR | 10.0 | -0.011228070175438587 | -0.0011228070175438587 | Elevated US yields, geopolitical stress, and risk aversion can sustain safe-haven and rate-differential demand for the dollar. |
| xai-grok-4-3 | ENERGY | 50.0 | 0.07613676418752213 | 0.038068382093761066 | Unresolved Strait of Hormuz blockade and Brent surge to $83.30 support sustained energy price premium through August. |
| xai-grok-4-3 | FINANCIALS | 30.0 | 0.03905831995719633 | 0.0117174959871589 | Recent 5.49% 30-day outperformance and sensitivity to any steepening yield curve from inflation data. |
| xai-grok-4-3 | HEALTHCARE | 20.0 | 0.043181958986431956 | 0.008636391797286392 | Defensive characteristics with 5.40% 30-day gain amid weak payrolls and policy uncertainty. |
| xai-grok-4-5 | ENERGY | 35.0 | 0.07613676418752213 | 0.026647867465632746 | Hormuz blockade restart and dual control claims create near-term upside for energy equities via oil price support before August exit. |
| xai-grok-4-5 | OIL | 25.0 | 0.06146531963664148 | 0.01536632990916037 | Direct crude exposure benefits from unresolved Strait transit risks and announced US Iranian shipping blockade starting July 14. |
| xai-grok-4-5 | FINANCIALS | 20.0 | 0.03905831995719633 | 0.0078116639914392666 | Upcoming major-bank Q2 results and relative 30d strength position financials for potential outperformance amid rate and growth data. |
| xai-grok-4-5 | HEALTHCARE | 15.0 | 0.043181958986431956 | 0.006477293847964793 | Defensive sector with strong recent relative returns and lower beta offers ballast if oil-driven inflation or risk-off hits broader market. |
| xai-grok-4-5 | LARGE_VALUE | 5.0 | 0.044745981746223906 | 0.0022372990873111955 | Value tilt captures energy/financials exposure with lower growth sensitivity while rates remain elevated. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | OIL | 4 | 0.85 | 0.06146531963664148 | 0.07109303093353476 | 0.032770620799653274 | 0.07540103594888163 |  | True | True |
| xai-grok-4-5 | ENERGY | 5 | 0.58 | 0.07613676418752213 | 0.05854045430150837 | 0.020218044167626882 | 0.08795361258090803 |  | True | True |
| xai-grok-4-3 | ENERGY | 3 | 0.65 | 0.07613676418752213 | 0.058422269878206354 | 0.020099859744324863 | 0.08807179700421004 |  | True | True |
| openai-gpt-5-5 | OIL | 5 | 0.46 | 0.06146531963664148 | 0.05640690237162734 | 0.01808449223774585 | 0.09008716451078905 |  | True | True |
| openai-gpt-5-6-sol | ENERGY | 5 | 0.61 | 0.07613676418752213 | 0.0532274321987935 | 0.01490502206491201 | 0.0932666346836229 |  | True | True |
| anthropic-claude-fable-5 | ENERGY | 5 | 0.5 | 0.07613676418752213 | 0.04053786722802762 | 0.0022154570941461324 | 0.10595619965438877 |  | True | True |
| anthropic-claude-opus-4-7 | ENERGY | 5 | 0.55 | 0.07613676418752213 | 0.03967801662584054 | 0.0013556064919590521 | 0.10681605025657585 |  | True | True |
| anthropic-claude-opus-4-8 | ENERGY | 5 | 0.55 | 0.07613676418752213 | 0.03584605740715705 | -0.0024763527267244387 | 0.11064800947525935 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 9919ea62d295c08bfbfb3ef2ab267ab1d7de1e196a7bb5028344dc8b8ed77176 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | 9d93c78d0833b5711328c0d018abb144bff4d4576a06cdd760a85a9a15319270 |
| market_data/universe_trailing_returns.csv | 3143d3d3a51ee7eb219e7c8bf7e4908568aa4e1d3375a0660c359488744cd8b2 |
| market_data/universe_trailing_returns.md | 36556b4c86167e1ef6c6b0fca3e489889d2705afe148df8ba4a39bf8df092961 |
| market_data/universe_trailing_returns.json | f81b44add4dc75e5716f1a4606a6b70d9c3306deb10d643a7fc5d3d0bf94fc65 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 598d82b383370521b5dbca23c09c84e32c38ae951df3a93a77090b6794af9c22 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 414198418f63d1ba4bd6ad23fbd17d8e01b213627c359bbdc73555b9fa64ea3e | yes |
| Final briefing | research/final_briefing.md | model-facing | 9919ea62d295c08bfbfb3ef2ab267ab1d7de1e196a7bb5028344dc8b8ed77176 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
