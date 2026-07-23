# CapitalBench Report: CB-2026-07-15-1W / official-20260715

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260715
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-15-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-15
- Decision deadline: 2026-07-16T07:30:00Z
- Horizon: one week
- Entry date: 2026-07-15
- Exit date: 2026-07-22
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | ENERGY | 2 | 0.65 | Geopolitical energy disruption outweighs mixed macro data and earnings timing for the short scoring window. | Rapid de-escalation or negotiated resolution of Hormuz blockade reduces oil upside; Oversupply response or inventory builds cap price gains within one week; Broader equity market rotation away from energy if risk appetite improves |
| xai-grok-4-5 | xai | portfolio | OIL | 5 | 0.62 | Prioritize oil and energy for the unresolved Strait of Hormuz military/energy-flow risk, add financials and SP500 for the disinflationary data backdrop, and use broad commodities for diversification. Allocation is sized for high expected return over the short scoring window while limiting pure single-name concentration. | Rapid de-escalation or reopening of Hormuz transit could reverse the oil premium and cause sharp underperformance in OIL and ENERGY; High volatility and contango/roll dynamics in oil futures products can produce large daily swings even if the geopolitical narrative persists; Further equity risk-off if military activity broadens or if retail sales/claims data disappoint, hurting the SP500 and FINANCIALS sleeves; Energy-price spike could re-ignite inflation concerns and pressure rates-sensitive financials despite the recent soft CPI/PPI prints |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.55 | A concentrated oil and energy overweight seeks to exploit unresolved Strait of Hormuz and Iran-related supply risks during the one-week window. Semiconductors and financials diversify into scheduled earnings and recent positive corporate signals that could outperform the S&P 500 if macro conditions remain supportive. | A diplomatic or military de-escalation in the Strait of Hormuz could quickly erase the crude-oil risk premium and hurt the largest portfolio exposures.; Oil futures and energy equities could decline if traders fade the recent 7-day oil rally, especially given high volatility and large recent drawdowns in oil-related instruments.; TSMC earnings or commentary could disappoint despite prior guidance, extending the semiconductor drawdown and weighing on high-beta technology exposure.; A weak retail sales, housing, or industrial production print could reduce risk appetite and pressure financials, regional banks, and semiconductors.; Further energy-price increases could revive inflation and rate concerns, hurting equities even if the oil allocation performs well. |
| google-gemini-3-1-pro | google | portfolio | OIL | 4 | 0.65 | Allocations focus on the acute geopolitical risks in the Middle East driving oil and defense, balanced with a tactical play on semiconductor earnings. | A rapid de-escalation or diplomatic resolution in the Middle East could cause a sharp reversal in oil and energy prices.; TSMC earnings could disappoint or offer weak forward guidance, negatively impacting the semiconductor allocation.; Broader market volatility could drag down equity allocations despite sector-specific catalysts. |
| openai-gpt-5-6-sol | openai | portfolio | OIL | 4 | 0.61 | Overweight oil and energy for acute supply-disruption risk, with smaller allocations to semiconductors and financials where fresh fundamental catalysts could drive near-term outperformance. | A ceasefire, restored Strait of Hormuz transit, or rapid policy reversal could sharply unwind oil and energy gains.; TSMC results or commentary could disappoint elevated expectations, extending the semiconductor sector's recent drawdown.; Weak retail sales or industrial production could pressure cyclical equities and reinforce concerns about slowing growth.; Oil's high recent volatility and sharp seven-day rise increase reversal and profit-taking risk.; A renewed rise in Treasury yields could weigh on semiconductor valuations and broader risk appetite. |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.5 | Geopolitical energy-supply catalyst plus financial-sector earnings strength drive a value/energy-tilted portfolio expected to outperform SPY over the week whether crude rises or markets wobble. | Rapid Hormuz de-escalation or negotiated resolution could reverse oil and energy gains sharply.; Strong TSMC/Netflix results could spark a tech-led rally that this portfolio underweights.; USO futures-curve structure and volatility can erode returns even if spot crude holds.; Financials/value recent outperformance could mean positioning is crowded and mean-reverts. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | ENERGY | 5 | 0.55 | Geopolitical oil catalyst plus strong financials earnings momentum with a broad-market core, balancing upside against a rapidly changing military situation. | Rapid de-escalation in the Strait of Hormuz reversing oil and energy gains; Bank/financials earnings disappointment or reversal of recent sharp KRE/XLF run-up; Broad equity pullback if retail sales or claims data surprise negatively during the window; Renewed rate volatility undermining rate-sensitive financials and regional banks |
| anthropic-claude-opus-4-7 | anthropic | portfolio | ENERGY | 5 | 0.55 | Tilt toward energy and financials with catalyst support from briefing (Hormuz military action, strong bank earnings), defensive tech via cyber and defense, and T-bills for risk control into a busy earnings/data week. | Rapid de-escalation in Hormuz collapses oil premium hurting XLE/ITA; Bank earnings disappointment or credit concerns reverse XLF rally; Tech mega-cap rebound (Netflix/TSMC beats) leaves portfolio underweight beta |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 121.38 | 131.67999267578125 | 0.08485741205949293 | 1 |
| ENERGY | Energy Sector | 56.5 | 59.2 | 0.04778761061946901 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 17.17 | 17.81 | 0.03727431566686068 | 3 |
| SILVER | Silver | 52.21 | 53.91999816894531 | 0.032752311222856045 | 4 |
| BRAZIL | Brazil Equities | 35.88 | 36.619998931884766 | 0.020624273463900833 | 5 |
| GOLD | Gold | 76.28 | 77.69 | 0.01848453067645517 | 6 |
| MEXICO | Mexico Equities | 75.39 | 76.70999908447266 | 0.017508941298218117 | 7 |
| DIVIDEND | US Dividend Equities | 32.34 | 32.9 | 0.017316017316017174 | 8 |
| COPPER | Copper | 38.63 | 39.25 | 0.016049702303908786 | 9 |
| UTILITIES | Utilities Sector | 45.22 | 45.93 | 0.015701017249004856 | 10 |
| BITCOIN_ETF | Bitcoin ETF | 36.81 | 37.34000015258789 | 0.014398265487310269 | 11 |
| LOW_VOL | US Low Volatility Equities | 75.3300617135 | 76.2 | 0.011548354889295176 | 12 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.47 | 84.38 | 0.010902120522343406 | 13 |
| REAL_ESTATE | Real Estate Sector | 44.56 | 45.01 | 0.010098743267504373 | 14 |
| UNITED_KINGDOM | United Kingdom Equities | 46.77 | 47.24 | 0.010049176822749528 | 15 |
| AGRICULTURE | Agriculture Commodities | 27.98 | 28.229999542236328 | 0.008934937177853097 | 16 |
| HEALTHCARE | Healthcare Sector | 158.29 | 159.43 | 0.007201971065765367 | 17 |
| US_DOLLAR | US Dollar | 28.25 | 28.450000762939453 | 0.007079673024405375 | 18 |
| MATERIALS | Materials Sector | 50.5 | 50.82 | 0.006336633663366342 | 19 |
| MOMENTUM | US Momentum Equities | 312.67 | 314.24 | 0.0050212684299739685 | 20 |
| SMALL_VALUE | US Small-Cap Value | 221.29 | 222.05 | 0.003434407338786194 | 21 |
| METALS_MINING | Metals and Mining | 103.2 | 103.5 | 0.0029069767441860517 | 22 |
| AUSTRALIA | Australia Equities | 28.8 | 28.86 | 0.002083333333333215 | 23 |
| LARGE_VALUE | US Large-Cap Value | 247.28 | 247.52 | 0.0009705596894209467 | 24 |
| MID_CAP | US Mid-Cap Stocks | 75.63 | 75.69 | 0.0007933359777865245 | 25 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.52 | 91.58 | 0.000655594405594373 | 26 |
| ETHEREUM_ETF | Ethereum ETF | 14.52 | 14.520000457763672 | 3.1526423693861716e-08 | 27 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 28 |
| EUROPE | Europe Equities | 89.12 | 89.09 | -0.0003366247755834939 | 29 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.97 | 212.7 | -0.0012677841949571 | 30 |
| REGIONAL_BANKS | Regional Banks | 75.78 | 75.6 | -0.002375296912114133 | 31 |
| TIPS | Treasury Inflation-Protected Securities | 108.07 | 107.77 | -0.0027759785324326103 | 32 |
| CANADA | Canada Equities | 59.49 | 59.28 | -0.0035300050428643814 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.81 | 79.52 | -0.003633629870943622 | 34 |
| EURO | Euro | 105.81 | 105.33000183105469 | -0.0045364159242540225 | 35 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.82 | 70.49 | -0.0046597006495340265 | 36 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.03 | 47.79999923706055 | -0.004788689630219722 | 37 |
| YEN | Japanese Yen | 56.53 | 56.22999954223633 | -0.0053069247791203145 | 38 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.14 | 97.58 | -0.005706134094151216 | 39 |
| SEMICONDUCTORS | Semiconductors | 590.77 | 586.91 | -0.006533845659055126 | 40 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.73 | 95.08999633789062 | -0.006685507804339075 | 41 |
| SMALL_CAP | US Small-Cap Stocks | 295.77 | 293.79 | -0.006694390911857084 | 42 |
| INDUSTRIALS | Industrials Sector | 180.06 | 178.85 | -0.006719982228146182 | 43 |
| SOUTH_KOREA | South Korea Equities | 171.64 | 170.43 | -0.007049638778839351 | 44 |
| TECHNOLOGY | Technology Sector | 181.58 | 180.27 | -0.007214450930719263 | 45 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.83 | 93.1500015258789 | -0.00724713283727052 | 46 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.78 | 93.1 | -0.007251013009170526 | 47 |
| TAIWAN | Taiwan Equities | 102.49 | 101.68000030517578 | -0.007903207091659814 | 48 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.76 | 105.87999725341797 | -0.00824281328757992 | 49 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.58 | 106.67 | -0.00845882134225684 | 50 |
| FINANCIALS | Financials Sector | 56.56 | 56.05 | -0.00901697312588412 | 51 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.24 | 83.44 | -0.009496676163342821 | 52 |
| TOTAL_US_MARKET | Total US Stock Market | 372.42 | 368.87 | -0.009532248536598509 | 53 |
| SP500 | S&P 500 | 754.81 | 747.41 | -0.00980379168267509 | 54 |
| INDIA | India Equities | 48.72 | 48.22 | -0.010262725779967119 | 55 |
| CHINA | China Equities | 54.15 | 53.57 | -0.010710987996306542 | 56 |
| EMERGING_MARKETS | Emerging Markets | 59.48 | 58.81 | -0.011264290517821074 | 57 |
| SOUTH_AFRICA | South Africa Equities | 63.74 | 62.97999954223633 | -0.011923446152552142 | 58 |
| JAPAN | Japan Equities | 93.5 | 92.19 | -0.0140106951871658 | 59 |
| BROAD_AI_TECH | Broad AI Technology | 61.12 | 60.14 | -0.016034031413612482 | 60 |
| NASDAQ100 | Nasdaq 100 | 717.74 | 705.35 | -0.017262518460723908 | 61 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 121.52 | 119.14 | -0.019585253456221197 | 62 |
| LARGE_GROWTH | US Large-Cap Growth | 123.58 | 120.92 | -0.02152451853050652 | 63 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.42 | 231.11 | -0.022460028762371964 | 64 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.0 | 114.02 | -0.025470085470085557 | 65 |
| BIOTECH | Biotechnology | 156.22 | 152.11 | -0.02630905133785677 | 66 |
| COMMUNICATIONS | Communication Services Sector | 113.38 | 109.2 | -0.036867172340800836 | 67 |
| SOLAR | Solar Energy | 55.8 | 53.72 | -0.037275985663082434 | 68 |
| CYBERSECURITY | Cybersecurity | 93.09 | 89.33 | -0.04039101944354928 | 69 |
| SOFTWARE | Software | 93.94 | 89.02 | -0.052373855652544155 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | 0.04778761061946901 | 0.014336283185840702 | Active Strait of Hormuz blockade, US strikes, and Iranian export threats create a live supply-disruption catalyst supporting energy equities within the window. |
| anthropic-claude-fable-5 | OIL | 15.0 | 0.08485741205949293 | 0.012728611808923939 | Direct crude exposure to unresolved Hormuz escalation; Brent settled near $85 with supply risk skewed higher; sized modestly given de-escalation reversal risk. |
| anthropic-claude-fable-5 | FINANCIALS | 25.0 | -0.00901697312588412 | -0.00225424328147103 | Strong bank/asset-manager earnings beats (BlackRock, BNY Mellon) mid-earnings season, low oil-shock sensitivity, and positive sector breadth; independent earnings support beyond recent price gains. |
| anthropic-claude-fable-5 | BROAD_COMMODITIES | 15.0 | 0.03727431566686068 | 0.0055911473500291015 | Diversified energy-heavy commodity exposure benefits from geopolitical supply risk with negative equity beta, hedging equity drawdown. |
| anthropic-claude-fable-5 | LARGE_VALUE | 15.0 | 0.0009705596894209467 | 0.000145583953413142 | Value tilt (financials, energy) benefits from soft CPI/PPI easing rate pressure while limiting mega-cap tech exposure ahead of geopolitically driven volatility. |
| anthropic-claude-opus-4-7 | ENERGY | 30.0 | 0.04778761061946901 | 0.014336283185840702 | Strait of Hormuz blockade reimposed with US strikes and Iran threats to halt ME energy exports; oil at $85 with upside risk. XLE benefits from higher crude with lower volatility than USO. |
| anthropic-claude-opus-4-7 | FINANCIALS | 25.0 | -0.00901697312588412 | -0.00225424328147103 | Strong earnings momentum (BlackRock +6.6%, BNY +5.1%), 30d outperformance +5.72% vs SPY, at 52w high, benefiting from steeper curve and solid Q2 results. |
| anthropic-claude-opus-4-7 | CYBERSECURITY | 15.0 | -0.04039101944354928 | -0.006058652916532392 | Defensive tech with strong catalysts, +8% 30d, uncorrelated to semi weakness, benefits from geopolitical tension backdrop. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | -0.022460028762371964 | -0.0033690043143557945 | Middle East military escalation with active US strikes supports defense names near-term; briefing catalyst-supported. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.000655594405594373 | 9.833916083915594e-05 | Dry powder given elevated geopolitical tail risk, Netflix/TSMC earnings volatility, and mega-cap tech weakness signals. |
| anthropic-claude-opus-4-8 | ENERGY | 30.0 | 0.04778761061946901 | 0.014336283185840702 | Strait of Hormuz blockade, Iranian export threats, and oil spiking (USO +8% 7d) create a near-term catalyst; XLE has negative beta to SPX offering asymmetric upside if conflict escalates before exit close. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | -0.00901697312588412 | -0.00225424328147103 | Strong bank earnings beats (BlackRock +6.6%, BNY +5.1%), lower 10y yield, and XLF leading with 65% up-day share and at 52w highs; earnings season tailwind continues into the window. |
| anthropic-claude-opus-4-8 | SP500 | 25.0 | -0.00980379168267509 | -0.0024509479206687723 | Broad market at highs with cooling monthly CPI/PPI and falling yields; core benchmark exposure to capture continued risk-on breadth. |
| anthropic-claude-opus-4-8 | REGIONAL_BANKS | 10.0 | -0.002375296912114133 | -0.00023752969121141332 | KRE strong recent breadth (70% up days, +5.5% 30d) supported by bank earnings momentum and falling short rates; limited independent fundamental support beyond sector earnings, reversal risk noted. |
| anthropic-claude-opus-4-8 | OIL | 10.0 | 0.08485741205949293 | 0.008485741205949294 | Direct geopolitical energy catalyst from Hormuz blockade; small tactical add given unresolved military duration and high volatility. |
| google-gemini-3-1-pro | OIL | 40.0 | 0.08485741205949293 | 0.033942964823797175 | The reimposed blockade on Iranian ports and threats to halt energy exports from the Middle East present a significant near-term catalyst for crude oil prices. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.04778761061946901 | 0.014336283185840702 | Energy equities are positioned to benefit from the immediate upward pressure on oil prices due to the Strait of Hormuz blockade and military activity. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 15.0 | -0.022460028762371964 | -0.0033690043143557945 | Renewed military strikes and blockades in the Middle East provide a catalyst for defense equities over the one-week horizon. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 15.0 | -0.006533845659055126 | -0.000980076848858269 | TSMC's upcoming earnings and strong Q2 guidance, alongside ASML's positive revenue forecast, offer a potential catalyst for semiconductor equities. |
| openai-gpt-5-5 | OIL | 45.0 | 0.08485741205949293 | 0.03818583542677182 | Direct exposure to crude oil, where renewed U.S. blockade activity, strikes, Iranian threats to halt Middle East energy exports, and unresolved Strait of Hormuz transit conditions create the strongest identifiable one-week catalyst; recent strength is supported by this geopolitical supply-risk catalyst but carries sharp de-escalation risk. |
| openai-gpt-5-5 | ENERGY | 20.0 | 0.04778761061946901 | 0.009557522123893804 | Energy equities should benefit if elevated oil prices persist or the Hormuz risk premium widens, while providing less futures-specific exposure than crude oil; recent gains have catalyst support from higher Brent and geopolitical supply uncertainty. |
| openai-gpt-5-5 | SEMICONDUCTORS | 15.0 | -0.006533845659055126 | -0.000980076848858269 | TSMC earnings are scheduled during the scoring window, ASML reported revenue growth above forecast and guided above expectations, and recent semiconductor weakness leaves room for a rebound if AI-chip fundamentals are reaffirmed. |
| openai-gpt-5-5 | FINANCIALS | 10.0 | -0.00901697312588412 | -0.0009016973125884121 | Financials have near-term support from strong reported results at BlackRock and Bank of New York Mellon, stable commercial loan quality in the Beige Book, and recent sector relative strength with moderate beta. |
| openai-gpt-5-5 | REGIONAL_BANKS | 10.0 | -0.002375296912114133 | -0.00023752969121141332 | Regional banks offer cyclical financial exposure that could benefit from stable credit-quality commentary and risk appetite if inflation data and yields remain supportive; recent strength is not used alone and could reverse if credit worries rise. |
| openai-gpt-5-6-sol | OIL | 40.0 | 0.08485741205949293 | 0.033942964823797175 | The renewed blockade, additional U.S. strikes, and Iranian threat to halt regional energy exports create the clearest immediate upside catalyst through the exit date. |
| openai-gpt-5-6-sol | ENERGY | 25.0 | 0.04778761061946901 | 0.011946902654867253 | Energy equities offer operational leverage to elevated crude prices while reducing some of the futures-specific volatility of direct oil exposure. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 20.0 | -0.006533845659055126 | -0.0013067691318110254 | TSMC earnings and ASML's stronger revenue outlook provide near-term fundamental catalysts after a sharp sector pullback, creating rebound potential despite high volatility. |
| openai-gpt-5-6-sol | FINANCIALS | 15.0 | -0.00901697312588412 | -0.001352545968882618 | Strong early financial-sector earnings and stable commercial loan quality support continued relative strength, while the sector's moderate beta diversifies commodity and chip exposure. |
| xai-grok-4-3 | ENERGY | 50.0 | 0.04778761061946901 | 0.023893805309734506 | US blockade and Iranian threats to halt Middle East energy exports create near-term upward pressure on oil prices before the July 22 close. |
| xai-grok-4-3 | OIL | 50.0 | 0.08485741205949293 | 0.042428706029746466 | Direct exposure to crude via USO benefits from Strait of Hormuz military escalation and unresolved transit risks over the one-week window. |
| xai-grok-4-5 | OIL | 40.0 | 0.08485741205949293 | 0.033942964823797175 | Strait of Hormuz blockade, Iranian threats to halt Middle East energy exports, and renewed US strikes create immediate supply-risk premium for crude; recent oil strength has independent geopolitical catalyst support beyond price history. |
| xai-grok-4-5 | ENERGY | 25.0 | 0.04778761061946901 | 0.011946902654867253 | Energy equities should benefit from elevated oil prices and Hormuz disruption risk; sector has positive 30d relative performance and direct leverage to the same unresolved military/energy-flow catalyst. |
| xai-grok-4-5 | FINANCIALS | 15.0 | -0.00901697312588412 | -0.001352545968882618 | Soft June CPI/PPI prints and falling 10y yields support risk assets and financials; BlackRock and BNY Mellon beat expectations, and the sector shows strong recent relative strength with lower beta. |
| xai-grok-4-5 | BROAD_COMMODITIES | 10.0 | 0.03727431566686068 | 0.003727431566686068 | Diversified commodity basket captures energy upside plus broader inflation/geopolitical hedge while reducing single-commodity concentration risk. |
| xai-grok-4-5 | SP500 | 10.0 | -0.00980379168267509 | -0.000980379168267509 | Cooling inflation data and modest growth backdrop favor continued equity risk appetite; provides liquid core exposure while the portfolio tilts to higher-conviction energy themes. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | ENERGY | 2 | 0.65 | 0.04778761061946901 | 0.06632251133948097 | 0.07612630302215606 | 0.01853490072001196 |  | True | True |
| xai-grok-4-5 | OIL | 5 | 0.62 | 0.08485741205949293 | 0.047284373908200374 | 0.05708816559087546 | 0.03757303815129256 |  | True | True |
| openai-gpt-5-5 | OIL | 5 | 0.55 | 0.08485741205949293 | 0.045624053698007525 | 0.055427845380682614 | 0.03923335836148541 |  | True | True |
| google-gemini-3-1-pro | OIL | 4 | 0.65 | 0.08485741205949293 | 0.04393016684642381 | 0.0537339585290989 | 0.04092724521306912 |  | True | True |
| openai-gpt-5-6-sol | OIL | 4 | 0.61 | 0.08485741205949293 | 0.043230552377970785 | 0.053034344060645874 | 0.041626859681522146 |  | True | True |
| anthropic-claude-fable-5 | ENERGY | 5 | 0.5 | 0.04778761061946901 | 0.030547383016735853 | 0.04035117469941094 | 0.05431002904275708 |  | True | True |
| anthropic-claude-opus-4-8 | ENERGY | 5 | 0.55 | 0.04778761061946901 | 0.017879303498438782 | 0.027683095181113872 | 0.06697810856105416 |  | True | True |
| anthropic-claude-opus-4-7 | ENERGY | 5 | 0.55 | 0.04778761061946901 | 0.0027527218343206417 | 0.012556513516995731 | 0.08210469022517229 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 06539d958e8cca084a69168dfad0c3ff41217e9171cd9f3e93b315d4f1d576a2 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | 2a334d00a7284504197285715affd77ad4c6ce6e4df5ada5b7acb66607a1d917 |
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
| Final briefing | research/final_briefing.md | model-facing | 06539d958e8cca084a69168dfad0c3ff41217e9171cd9f3e93b315d4f1d576a2 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
