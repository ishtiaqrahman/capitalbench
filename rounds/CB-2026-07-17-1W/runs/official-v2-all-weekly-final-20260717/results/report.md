# CapitalBench Report: CB-2026-07-17-1W / official-v2-all-weekly-final-20260717

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-all-weekly-final-20260717
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-17-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-17
- Decision deadline: 2026-07-18T09:30:00Z
- Horizon: one week
- Entry date: 2026-07-17
- Exit date: 2026-07-24
- Entry rule: Use adjusted close prices on Friday, July 17, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, July 24, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | OIL | 4 | 0.65 | Overweight energy and oil for momentum, balanced with regional banks and consumer staples for relative strength. | A sudden reversal in oil prices could negatively impact the 50% allocation to energy and oil.; A strong broad market rally could lead to underperformance of the defensive consumer staples allocation.; Unexpected negative news in the banking sector could hurt the regional banks position. |
| xai-grok-4-3 | xai | portfolio | ENERGY | 4 | 0.62 | Selected holdings have base forecasts exceeding SPY; energy cluster at cap; four clusters represented. | Weak payrolls and downward revisions pressure growth outlook; Tech and growth drawdowns may spill into broader market; Oil volatility from EIA inventory data |
| anthropic-claude-opus-4-8 | anthropic | portfolio | ENERGY | 4 | 0.56 | Overweight energy on oil strength, dividends and financials on defensive rotation, retain SPY core. | Oil reverses if EIA report shows large inventory build; Defensive rotation unwinds and growth rebounds sharply |
| xai-grok-4-5 | xai | portfolio | ENERGY | 5 | 0.58 | SPY base is modest after weekly decline; selected holdings show stronger recent active returns and cluster diversification within the 50% cap. One-week horizon favors continuation of defensive/value and oil strength over reversal into mega-cap growth. | Sudden risk-on rebound in Nasdaq/tech reverses value and energy leadership; EIA report or oil supply news triggers sharp energy pullback; Unexpectedly strong data lifts yields and pressures rate-sensitive names; Broad equity follow-through selling from the prior week |
| openai-gpt-5-5 | openai | portfolio | REGIONAL_BANKS | 5 | 0.57 | SPY has weak short-term breadth and negative 5-day/21-day returns, while several value, defensive, financial, real-estate, and energy exposures have stronger active trends. Selected holdings all have base forecasts above SPY and no non-benchmark cluster exceeds 50%. | A sharp rebound in mega-cap growth and technology could make SPY outperform the diversified active tilts.; Treasury yields could rise despite softer CPI/PPI, hurting real estate and other rate-sensitive holdings.; Oil could reverse after a 14% five-session move or the EIA petroleum report could be bearish for energy.; Recent relative-strength signals may mean-revert over the one-week horizon. |
| anthropic-claude-fable-5 | anthropic | portfolio | LARGE_VALUE | 5 | 0.62 | Underweight mega-cap growth, overweight value/defensive/financials/energy to capture continued breadth rotation over the one-week window with reduced beta to a falling index. | Sharp mega-cap tech rebound would leave the low-beta portfolio lagging SPY; Crude oil spike reverses, hurting the energy sleeve; Defensive/value crowding unwinds in a broad risk-on move; Bank earnings disappointments hit financials |
| anthropic-claude-opus-4-7 | anthropic | portfolio | ENERGY | 4 | 0.55 | SPY weak (-1.6% wk) led by tech drawdown; rotation into energy, defensives, financials evident. Portfolio tilts to these leaders while keeping SPY core. | Oil reversal if EIA shows large build; Tech snap-back rally lifts SPY faster than defensives; Bank earnings disappointment |
| openai-gpt-5-6-sol | openai | portfolio | DIVIDEND | 4 | 0.59 | Dividend equities, healthcare, financials, and intermediate Treasuries each have base forecasts above SPY. The allocation spans four capped exposure clusters and has a weighted base return of 0.52%. | A sharp rebound in mega-cap growth could cause the defensive equity holdings to lag SPY.; A rise in Treasury yields driven by persistent import or PCE inflation could hurt IEF.; Weak July 21 labor data could raise financial-sector credit concerns even while supporting Treasuries.; Recent dividend and healthcare relative strength could reverse after crowded defensive positioning. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 123.95999908447266 | 136.69 | 0.1026944256981841 | 1 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 230.72999572753906 | 240.14 | 0.04078361915098738 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 17.25 | 17.95 | 0.04057971014492745 | 3 |
| SILVER | Silver | 50.779998779296875 | 52.59 | 0.0356439792086225 | 4 |
| METALS_MINING | Metals and Mining | 98.3499984741211 | 101.74 | 0.03446875016242035 | 5 |
| ENERGY | Energy Sector | 57.68000030517578 | 59.62 | 0.03363383641747553 | 6 |
| UTILITIES | Utilities Sector | 45.16999816894531 | 46.29 | 0.024795259607176545 | 7 |
| INDUSTRIALS | Industrials Sector | 179.41000366210938 | 182.66000366210938 | 0.01811493190826119 | 8 |
| MATERIALS | Materials Sector | 50.529998779296875 | 51.26 | 0.01444688775655023 | 9 |
| AGRICULTURE | Agriculture Commodities | 27.84000015258789 | 28.24 | 0.014367810532318837 | 10 |
| MOMENTUM | US Momentum Equities | 302.0899963378906 | 306.3900146484375 | 0.014234229410686083 | 11 |
| BRAZIL | Brazil Equities | 35.22999954223633 | 35.73 | 0.01419246279479025 | 12 |
| REAL_ESTATE | Real Estate Sector | 45.41999816894531 | 45.95 | 0.011668909124198601 | 13 |
| DIVIDEND | US Dividend Equities | 32.90999984741211 | 33.290000915527344 | 0.011546674867126017 | 14 |
| COPPER | Copper | 37.91999816894531 | 38.35 | 0.01133971128212874 | 15 |
| LOW_VOL | US Low Volatility Equities | 76.42900085449219 | 77.19000244140625 | 0.009956974164334387 | 16 |
| GOLD | Gold | 75.5 | 76.23 | 0.009668874172185538 | 17 |
| ETHEREUM_ETF | Ethereum ETF | 13.90999984741211 | 14.04 | 0.009345805464697765 | 18 |
| HEALTHCARE | Healthcare Sector | 161.08999633789062 | 162.57000732421875 | 0.009187479172969581 | 19 |
| US_DOLLAR | US Dollar | 28.329999923706055 | 28.58 | 0.008824570312996993 | 20 |
| SEMICONDUCTORS | Semiconductors | 556.530029296875 | 561.19 | 0.008373260125805748 | 21 |
| JAPAN | Japan Equities | 90.48999786376953 | 91.21 | 0.007956704091367284 | 22 |
| CHINA | China Equities | 52.95000076293945 | 53.33 | 0.007176567168748926 | 23 |
| TAIWAN | Taiwan Equities | 97.33000183105469 | 98.01 | 0.006986521690667047 | 24 |
| UNITED_KINGDOM | United Kingdom Equities | 46.939998626708984 | 47.23 | 0.006178129138802335 | 25 |
| MEXICO | Mexico Equities | 75.11000061035156 | 75.45 | 0.004526686018979875 | 26 |
| MID_CAP | US Mid-Cap Stocks | 75.54000091552734 | 75.7699966430664 | 0.0030446879103993574 | 27 |
| SOUTH_KOREA | South Korea Equities | 162.5399932861328 | 162.96 | 0.002584020740838966 | 28 |
| TECHNOLOGY | Technology Sector | 175.58999633789062 | 175.8800048828125 | 0.001651623389545609 | 29 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.3699951171875 | 213.57 | 0.0009373618005785733 | 30 |
| FINANCIALS | Financials Sector | 56.2599983215332 | 56.310001373291016 | 0.0008887851626309118 | 31 |
| LARGE_VALUE | US Large-Cap Value | 248.02999877929688 | 248.24000549316406 | 0.0008466988465134495 | 32 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.55000305175781 | 91.61000061035156 | 0.0006553528846944268 | 33 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.69999694824219 | 69.71 | 0.00014351581342575415 | 34 |
| BITCOIN_ETF | Bitcoin ETF | 36.349998474121094 | 36.35 | 4.1977413323124324e-08 | 35 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 36 |
| EMERGING_MARKETS | Emerging Markets | 57.84000015258789 | 57.8 | -0.0006915655685056921 | 37 |
| AUSTRALIA | Australia Equities | 28.75 | 28.72 | -0.0010434782608695903 | 38 |
| EUROPE | Europe Equities | 88.58999633789062 | 88.41 | -0.0020317907814795255 | 39 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.93000030517578 | 47.8 | -0.002712295104278284 | 40 |
| SMALL_VALUE | US Small-Cap Value | 222.33999633789062 | 221.4199981689453 | -0.00413779879508136 | 41 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.6500015258789 | 79.23 | -0.005273088736130638 | 42 |
| SP500 | S&P 500 | 743.2899780273438 | 738.9299926757812 | -0.005865793271064512 | 43 |
| TOTAL_US_MARKET | Total US Stock Market | 367.010009765625 | 364.79998779296875 | -0.006021693997031785 | 44 |
| EURO | Euro | 105.61000061035156 | 104.947 | -0.006277820343905671 | 45 |
| CANADA | Canada Equities | 59.45000076293945 | 59.07 | -0.0063919387394918425 | 46 |
| TIPS | Treasury Inflation-Protected Securities | 108.2699966430664 | 107.5 | -0.0071118192199161046 | 47 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.77999877929688 | 93.11 | -0.007144367541245811 | 48 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.19999694824219 | 97.46 | -0.007535610705082019 | 49 |
| YEN | Japanese Yen | 56.5099983215332 | 56.04 | -0.008317082560487576 | 50 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.83999633789062 | 93.03 | -0.008631674866802608 | 51 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.52999877929688 | 94.64 | -0.009316432436611288 | 52 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.58000183105469 | 105.55 | -0.009664119097008483 | 53 |
| SMALL_CAP | US Small-Cap Stocks | 294.0400085449219 | 291.1700134277344 | -0.009760559902680876 | 54 |
| BROAD_AI_TECH | Broad AI Technology | 58.70000076293945 | 57.98 | -0.012265770929836717 | 55 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.55999755859375 | 106.23 | -0.01236516910359009 | 56 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.19000244140625 | 84.12999725341797 | -0.012442835516026096 | 57 |
| REGIONAL_BANKS | Regional Banks | 76.69000244140625 | 75.73 | -0.012517960762091773 | 58 |
| LARGE_GROWTH | US Large-Cap Growth | 119.37999725341797 | 117.6500015258789 | -0.014491504166034286 | 59 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.5199966430664 | 83.25 | -0.015025990221339991 | 60 |
| NASDAQ100 | Nasdaq 100 | 695.3300170898438 | 684.22998046875 | -0.01596369543709708 | 61 |
| INDIA | India Equities | 48.90999984741211 | 48.02 | -0.018196684730907742 | 62 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 116.13999938964844 | 114.015 | -0.018296877913001275 | 63 |
| SOUTH_AFRICA | South Africa Equities | 62.36000061035156 | 61.07 | -0.020686346980847037 | 64 |
| BIOTECH | Biotechnology | 154.25999450683594 | 150.48 | -0.024504049276810047 | 65 |
| COMMUNICATIONS | Communication Services Sector | 110.6500015258789 | 106.30000305175781 | -0.039313135238445596 | 66 |
| CYBERSECURITY | Cybersecurity | 92.36000061035156 | 88.4 | -0.04287571009292224 | 67 |
| SOLAR | Solar Energy | 53.900001525878906 | 51.28 | -0.048608561256180516 | 68 |
| SOFTWARE | Software | 92.80000305175781 | 87.98 | -0.05193968634968171 | 69 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.44000244140625 | 109.41000366210938 | -0.05223491555587512 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.0008466988465134495 | 0.00021167471162836238 | Value showing positive absolute returns amid tech-led selloff; near 52w high with low drawdown; benefits from breadth rotation (RSP-SPY +1.64% 21s). |
| anthropic-claude-fable-5 | LOW_VOL | 20.0 | 0.009956974164334387 | 0.0019913948328668775 | Defensive factor with negative SPY beta (-0.27) and positive 3s return; hedges continued index weakness. |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | 0.009187479172969581 | 0.0022968697932423954 | Positive prior-window active return (+4.75%) plus recent strength (+1.77% 3s); near-zero SPY beta cushions further drawdown. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.0008887851626309118 | 0.00017775703252618236 | Positive active return both windows (+2.53% 5s, +1.99% prior), positive volume z-score, steep curve (2s10s +37bp) supportive. |
| anthropic-claude-fable-5 | ENERGY | 10.0 | 0.03363383641747553 | 0.003363383641747553 | Brent +4.6% July 17, oil momentum strong (USO +15.6% active 5s); XLE +6.26% active with negative SPY beta. |
| anthropic-claude-opus-4-7 | ENERGY | 35.0 | 0.03363383641747553 | 0.011771842746116434 | Brent +4.6% on 7/17 and XLE +6.26% active 5s; oil momentum with EIA inventory catalyst. |
| anthropic-claude-opus-4-7 | REGIONAL_BANKS | 15.0 | -0.012517960762091773 | -0.001877694114313766 | KRE +3.77% active 5s with steep curve (30y 5.06%, 2y 4.18%) supportive. |
| anthropic-claude-opus-4-7 | CONSUMER_STAPLES | 15.0 | -0.012442835516026096 | -0.0018664253274039144 | Defensive with +2.82% active 5s amid broad market weakness. |
| anthropic-claude-opus-4-7 | SP500 | 35.0 | -0.005865793271064512 | -0.002053027644872579 | Core benchmark exposure; oversold bounce potential after -1.6% week. |
| anthropic-claude-opus-4-8 | ENERGY | 30.0 | 0.03363383641747553 | 0.010090150925242658 | Brent up 4.6% in July 17 session, strong 6.26% 5s active return, oil supply catalyst via EIA report supports energy continuation. |
| anthropic-claude-opus-4-8 | DIVIDEND | 25.0 | 0.011546674867126017 | 0.002886668716781504 | SCHD low beta 0.10, defensive tilt with +2.20% 3s return during broad market decline, low correlation cushions risk. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | 0.0008887851626309118 | 0.00017775703252618236 | XLF positive 2.53% active 5s, strong prior-window active return 1.99%, low beta and steady momentum. |
| anthropic-claude-opus-4-8 | SP500 | 25.0 | -0.005865793271064512 | -0.001466448317766128 | Core benchmark exposure to limit tracking error while active tilts express views. |
| google-gemini-3-1-pro | OIL | 25.0 | 0.1026944256981841 | 0.025673606424546025 | Strong recent momentum and a 4.6% jump in Brent crude support a short-term continuation. |
| google-gemini-3-1-pro | ENERGY | 25.0 | 0.03363383641747553 | 0.008408459104368882 | Energy equities are well-positioned to benefit from the recent surge in oil prices. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 25.0 | -0.012517960762091773 | -0.0031294901905229433 | Recent outperformance suggests a rotation into financials that may persist over the short horizon. |
| google-gemini-3-1-pro | CONSUMER_STAPLES | 25.0 | -0.012442835516026096 | -0.003110708879006524 | Provides defensive exposure amid broader market weakness, supported by recent positive active returns. |
| openai-gpt-5-5 | REGIONAL_BANKS | 25.0 | -0.012517960762091773 | -0.0031294901905229433 | Financials and regional banks showed positive short-window and prior-window active strength, with low SPY beta and potential benefit from a less inflationary CPI/PPI mix. |
| openai-gpt-5-5 | REAL_ESTATE | 25.0 | 0.011668909124198601 | 0.0029172272810496502 | Real estate combines strong recent active return, near-52-week-high positioning, and sensitivity to lower inflation and yields after soft CPI/PPI data. |
| openai-gpt-5-5 | DIVIDEND | 20.0 | 0.011546674867126017 | 0.0023093349734252034 | Dividend equities outperformed SPY in the latest week and offer a defensive/value tilt amid broad market weakness and weak breadth. |
| openai-gpt-5-5 | ENERGY | 15.0 | 0.03363383641747553 | 0.005045075462621329 | Energy has a direct near-term catalyst from the scheduled EIA petroleum report and was supported by a sharp oil move, while allocation is limited due to reversal risk. |
| openai-gpt-5-5 | HEALTHCARE | 15.0 | 0.009187479172969581 | 0.0013781218759454372 | Healthcare has positive recent and prior active strength with low correlation to SPY, offering a diversifying defensive equity exposure. |
| openai-gpt-5-6-sol | DIVIDEND | 30.0 | 0.011546674867126017 | 0.003464002460137805 | Defensive dividend exposure has materially outperformed SPY recently, although the preceding trend offers limited confirmation. |
| openai-gpt-5-6-sol | HEALTHCARE | 30.0 | 0.009187479172969581 | 0.0027562437518908744 | Healthcare combines recent relative strength with positive prior-window active performance and low measured SPY correlation. |
| openai-gpt-5-6-sol | FINANCIALS | 20.0 | 0.0008887851626309118 | 0.00017775703252618236 | Financials have positive recent and prior-window active returns, providing stronger trend confirmation than most equity finalists. |
| openai-gpt-5-6-sol | INTERMEDIATE_TREASURY | 20.0 | -0.008631674866802608 | -0.0017263349733605217 | Weak payroll growth and benign June core CPI support a modest duration bid, with lower equity sensitivity than the other holdings. |
| xai-grok-4-3 | ENERGY | 50.0 | 0.03363383641747553 | 0.016816918208737763 | Strong recent active returns and oil price momentum within scoring window |
| xai-grok-4-3 | CONSUMER_STAPLES | 20.0 | -0.012442835516026096 | -0.0024885671032052192 | Defensive sector with positive active returns amid weak growth data |
| xai-grok-4-3 | FINANCIALS | 15.0 | 0.0008887851626309118 | 0.00013331777439463675 | Positive active returns and regional bank strength in supplied data |
| xai-grok-4-3 | SP500 | 15.0 | -0.005865793271064512 | -0.0008798689906596768 | Benchmark exposure with base forecast cleared by selected actives |
| xai-grok-4-5 | ENERGY | 25.0 | 0.03363383641747553 | 0.008408459104368882 | Recent oil strength and session gains support short-term continuation over soft equity tape. |
| xai-grok-4-5 | DIVIDEND | 25.0 | 0.011546674867126017 | 0.002886668716781504 | Relative strength versus SPY and defensive tilt favored under soft inflation and payroll data. |
| xai-grok-4-5 | REGIONAL_BANKS | 20.0 | -0.012517960762091773 | -0.0025035921524183546 | Strong active returns and financials resilience amid stable yields and soft landing signals. |
| xai-grok-4-5 | HEALTHCARE | 15.0 | 0.009187479172969581 | 0.0013781218759454372 | Positive prior active trend and defensive characteristics under mixed growth data. |
| xai-grok-4-5 | SMALL_VALUE | 15.0 | -0.00413779879508136 | -0.000620669819262204 | Outperformance versus SPY and value tilt supported by equal-weight relative strength. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | OIL | 4 | 0.65 | 0.1026944256981841 | 0.02784186645938544 | 0.03370765973044995 | 0.07485255923879866 |  | True | True |
| xai-grok-4-3 | ENERGY | 4 | 0.62 | 0.03363383641747553 | 0.013581799889267504 | 0.019447593160332018 | 0.0891126258089166 |  | True | True |
| anthropic-claude-opus-4-8 | ENERGY | 4 | 0.56 | 0.03363383641747553 | 0.011688128356784216 | 0.017553921627848728 | 0.09100629734139988 |  | True | True |
| xai-grok-4-5 | ENERGY | 5 | 0.58 | 0.03363383641747553 | 0.009548987725415264 | 0.015414780996479777 | 0.09314543797276884 |  | True | True |
| openai-gpt-5-5 | REGIONAL_BANKS | 5 | 0.57 | -0.012517960762091773 | 0.008520269402518677 | 0.014386062673583189 | 0.09417415629566542 |  | True | True |
| anthropic-claude-fable-5 | LARGE_VALUE | 5 | 0.62 | 0.0008466988465134495 | 0.00804108001201137 | 0.013906873283075882 | 0.09465334568617273 |  | True | True |
| anthropic-claude-opus-4-7 | ENERGY | 4 | 0.55 | 0.03363383641747553 | 0.005974695659526174 | 0.011840488930590686 | 0.09671973003865793 |  | True | True |
| openai-gpt-5-6-sol | DIVIDEND | 4 | 0.59 | 0.011546674867126017 | 0.00467166827119434 | 0.010537461542258852 | 0.09802275742698977 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | b7fe222181e4b7ea56480587c8ff7bda4cd9d6143f221e3d9c6431d76ff0755d |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 56aa11e0208b796cee9a8e71d7b8779c5c87c37c286a14d00a17ab57e5215ccd |
| manifest.yaml | 3814d64377f27aee9528331d4647384be47cc8893b56a486d11397cc1afc8d76 |
| submission_schema.json | f74e11a346ede06b8dd5aabf1008dc1d51b36b7920a525a9f7c592f84031ce88 |
| market_data/universe_decision_context.csv | 91781bd2587bb36420a8ea315db530c40527dcdb1d446ae93b2e9a8fe29f274a |
| market_data/universe_decision_context.md | b89739f1ed5849fa019394f65f74f2a873930e57da6c5046e5ae973a823ce88e |
| market_data/universe_decision_context.json | 823b7fb14c1430c7a1f160cac62f129e02a2c52d2d91e6a6016d787eb457c5ab |
| market_data/decision_context_source_history.json | 6c33e0bcacb095062b807b9ebff08d2166c379681d4700bac10a6ffc42d9db7d |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 37ca2302e07b9b06dc825e402faa47a42d4cc4546ac255a5979a733f253d109b | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | d013682fcfbac9ced1105c0e9c266563ca966782bd2b1665ee0c5c02088672ce | yes |
| Final briefing | research/final_briefing.md | model-facing | b7fe222181e4b7ea56480587c8ff7bda4cd9d6143f221e3d9c6431d76ff0755d | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
