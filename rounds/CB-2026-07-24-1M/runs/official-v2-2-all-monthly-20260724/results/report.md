# CapitalBench Report: CB-2026-07-24-1M / official-v2-2-all-monthly-20260724

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260724
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-24-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-24
- Decision deadline: 2026-07-25T23:30:00Z
- Horizon: one month
- Entry date: 2026-07-24
- Exit date: 2026-08-24
- Entry rule: Use adjusted close prices on Friday, July 24, 2026 as the one-month entry snapshot, calculated after regular trading ends and supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Monday, August 24, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | A balanced approach utilizing SP500 for core exposure, Energy for momentum, and Healthcare for defense. | Hawkish surprise from the upcoming FOMC meeting.; Disappointing earnings from major tech companies.; A sudden drop in oil prices impacting the Energy allocation. |
| anthropic-claude-fable-5 | anthropic | portfolio | LARGE_VALUE | 5 | 0.62 | Energy-shock plus hawkish-Fed regime favors low-beta value/defensive equity and commodity exposure over the growth-heavy S&P 500 for this one-month window. | Oil price collapse on Iran de-escalation would hurt energy and commodity sleeves; A dovish FOMC and soft July CPI could spark a growth rally that the portfolio underweights; A Fed hike triggering a broad equity selloff would drag all equity sleeves despite defensive tilt; Tariff-driven earnings warnings during Aug reporting could hit value cyclicals |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.55 | Sticky 3.5% CPI, a live 38% July hike probability, tariff risk and negative tech breadth argue for lower-beta defensive and real-asset tilts around an SPY core. | Dovish FOMC sparks a mega-cap tech melt-up that leaves defensive tilts behind; Sharp oil reversal hits energy allocation; Tariff pass-through crushes consumer and broad equity sentiment; Hot July CPI on Aug 12 raises rates and pressures all equity clusters |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 4 | 0.55 | Tilt toward defensively resilient sectors with positive active momentum while keeping broad SPY core; hedges tariff and rate risk during a heavy earnings and data window. | FOMC surprise hike July 28-29 with 38% implied probability hurts rate-sensitive holdings; Mega-cap earnings disappointment drags broad market and correlates holdings; Tariff round announced July 24 raises inflation pass-through risk |
| openai-gpt-5-5 | openai | portfolio | DIVIDEND | 5 | 0.56 | SPY has decent earnings support but faces tariff, rate, and growth-data risks. Selected holdings have base forecasts above SPY and diversify across four non-benchmark clusters with catalysts inside the scoring window. | A dovish risk-on rally led by mega-cap technology could cause SPY to outperform the defensive/value tilt.; Oil and energy equities could reverse if crude prices fall after the geopolitical shock premium fades.; A hotter July CPI/PPI or hawkish FOMC message could pressure utilities and dividend/value equities through higher yields.; Earnings disappointments in selected defensive, value, or energy sectors could overwhelm recent relative-strength signals. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 5 | 0.62 | Energy complex leads on supplied price and macro facts; value and healthcare add breadth across clusters with superior recent active returns and quality metrics versus growth-heavy benchmarks. | Rapid oil price reversal if geopolitical premium fades; FOMC hawkish surprise or tariff-driven risk-off hitting cyclicals; High volatility in OIL and ENERGY amplifying drawdowns; Commodity correlation breakdown if dollar strengthens sharply |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 4 | 0.57 | Strong aggregate earnings and semiconductor pullback potential support upside, while broader participation and elevated energy prices favor dividend and energy exposure. Defensive healthcare reduces dependence on a single continuation regime. | A hawkish FOMC decision or renewed rise in Treasury yields could deepen the technology selloff.; Tariff pass-through could lift inflation while weakening corporate margins and consumer demand.; Crude oil could continue its July 24 reversal, sharply reducing energy-sector returns.; Mega-cap technology earnings could disappoint after the semiconductor group's extreme prior advance. |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.55 | Three holdings selected with bases exceeding SPY; energy cluster at 40% under 50% cap. | Tariff implementation raises consumer prices faster than expected; FOMC signals tighter policy than futures imply; Energy reversal if geopolitical tensions ease |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.04 | 18.66 | 0.3290598290598292 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 36.35 | 44.64 | 0.22806052269601107 | 2 |
| SILVER | Silver | 52.59 | 62.2 | 0.18273436014451416 | 3 |
| SOUTH_AFRICA | South Africa Equities | 61.07 | 71.33 | 0.16800392991648927 | 4 |
| SOFTWARE | Software | 87.98 | 102.45 | 0.16446919754489664 | 5 |
| METALS_MINING | Metals and Mining | 101.74 | 117.87 | 0.1585413799882054 | 6 |
| GOLD | Gold | 76.23 | 87.47 | 0.14744851108487467 | 7 |
| BIOTECH | Biotechnology | 150.48 | 164.17 | 0.09097554492291327 | 8 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 109.41 | 118.3 | 0.0812539987204095 | 9 |
| HEALTHCARE | Healthcare Sector | 162.57 | 174.7 | 0.07461401242541665 | 10 |
| BROAD_AI_TECH | Broad AI Technology | 57.98 | 62.3 | 0.07450845119006555 | 11 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 114.015 | 121.83 | 0.06854361268254183 | 12 |
| SOUTH_KOREA | South Korea Equities | 162.96 | 173.64 | 0.06553755522827664 | 13 |
| ENERGY | Energy Sector | 59.62 | 63.11 | 0.058537403555853684 | 14 |
| DIVIDEND | US Dividend Equities | 33.29 | 35.21 | 0.05767497747071193 | 15 |
| COMMUNICATIONS | Communication Services Sector | 106.3 | 112.32 | 0.056632173095014116 | 16 |
| CYBERSECURITY | Cybersecurity | 88.4 | 93.23 | 0.054638009049773784 | 17 |
| TAIWAN | Taiwan Equities | 98.01 | 103.33 | 0.05428017549229658 | 18 |
| CANADA | Canada Equities | 59.07 | 62.12 | 0.05163365498561023 | 19 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.71 | 73.06 | 0.0480562329651415 | 20 |
| EUROPE | Europe Equities | 88.41 | 92.61 | 0.04750593824228022 | 21 |
| AUSTRALIA | Australia Equities | 28.72 | 30.06 | 0.04665738161559885 | 22 |
| MATERIALS | Materials Sector | 51.26 | 53.58 | 0.04525946156847449 | 23 |
| COPPER | Copper | 38.35 | 40.07 | 0.044850065189048216 | 24 |
| LARGE_VALUE | US Large-Cap Value | 248.24 | 258.32 | 0.04060586529165322 | 25 |
| JAPAN | Japan Equities | 91.21 | 94.84 | 0.03979826773380113 | 26 |
| UNITED_KINGDOM | United Kingdom Equities | 47.23 | 49.1 | 0.03959347872115182 | 27 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.13 | 87.45 | 0.03946273624153096 | 28 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.57 | 221.93 | 0.03914407454230462 | 29 |
| EMERGING_MARKETS | Emerging Markets | 57.8 | 59.97 | 0.037543252595155785 | 30 |
| FINANCIALS | Financials Sector | 56.31 | 58.22 | 0.0339193748890072 | 31 |
| TOTAL_US_MARKET | Total US Stock Market | 364.8 | 377.07 | 0.033634868421052566 | 32 |
| SP500 | S&P 500 | 738.93 | 763.47 | 0.03321018229060946 | 33 |
| NASDAQ100 | Nasdaq 100 | 684.23 | 706.32 | 0.03228446574982091 | 34 |
| CHINA | China Equities | 53.33 | 54.93 | 0.030001875117194876 | 35 |
| BROAD_COMMODITIES | Broad Commodities | 17.95 | 18.47 | 0.028969359331476374 | 36 |
| LARGE_GROWTH | US Large-Cap Growth | 117.65 | 121.04 | 0.028814279643008867 | 37 |
| YEN | Japanese Yen | 56.04 | 57.64 | 0.028551034975017764 | 38 |
| INDIA | India Equities | 48.02 | 49.35 | 0.0276967930029155 | 39 |
| EURO | Euro | 104.947 | 107.645 | 0.025708214622619074 | 40 |
| TECHNOLOGY | Technology Sector | 175.88 | 180.05 | 0.023709347282238058 | 41 |
| SMALL_CAP | US Small-Cap Stocks | 291.17 | 297.97 | 0.02335405433252058 | 42 |
| MEXICO | Mexico Equities | 75.45 | 77.15 | 0.022531477799867528 | 43 |
| SMALL_VALUE | US Small-Cap Value | 221.42 | 224.06 | 0.01192304218227802 | 44 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.23 | 79.7 | 0.005932096428120648 | 45 |
| MID_CAP | US Mid-Cap Stocks | 75.77 | 76.2 | 0.005675069288636703 | 46 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.64 | 94.85 | 0.002218934911242476 | 47 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.11 | 93.31 | 0.002147996992804213 | 48 |
| AGRICULTURE | Agriculture Commodities | 28.24 | 28.3 | 0.0021246458923513956 | 49 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.46 | 97.55 | 0.0009234557767290319 | 50 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 51 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.61 | 91.61 | 0.0 | 51 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.03 | 93.01 | -0.00021498441362999277 | 53 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.23 | 106.18 | -0.0004706768332862765 | 54 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.55 | 105.41 | -0.0013263855992420304 | 55 |
| TIPS | Treasury Inflation-Protected Securities | 107.5 | 107.25 | -0.0023255813953488857 | 56 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.8 | 47.68 | -0.002510460251045954 | 57 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.25 | 82.56 | -0.008288288288288315 | 58 |
| REGIONAL_BANKS | Regional Banks | 75.73 | 74.76 | -0.012808662353096523 | 59 |
| REAL_ESTATE | Real Estate Sector | 45.95 | 45.33 | -0.013492927094668206 | 60 |
| LOW_VOL | US Low Volatility Equities | 77.19 | 76.01 | -0.015286954268687536 | 61 |
| BRAZIL | Brazil Equities | 35.73 | 35.17 | -0.01567310383431275 | 62 |
| MOMENTUM | US Momentum Equities | 306.39 | 300.59 | -0.01893012174026576 | 63 |
| INDUSTRIALS | Industrials Sector | 182.66 | 179.0 | -0.020037227636045096 | 64 |
| US_DOLLAR | US Dollar | 28.58 | 27.96 | -0.021693491952414212 | 65 |
| SEMICONDUCTORS | Semiconductors | 561.19 | 546.8 | -0.025641939450097295 | 66 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 240.14 | 233.4 | -0.028066960939451935 | 67 |
| OIL | Crude Oil | 136.69 | 132.21 | -0.03277489209159401 | 68 |
| SOLAR | Solar Energy | 51.28 | 48.32 | -0.057722308892355745 | 69 |
| UTILITIES | Utilities Sector | 46.29 | 43.22 | -0.06632101965867354 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | LARGE_VALUE | 30.0 | 0.04060586529165322 | 0.012181759587495965 | Value leads in a rising-rate, energy-shock regime; +2.23% 21d active return, only -0.49% from 52w high, low vol. |
| anthropic-claude-fable-5 | DIVIDEND | 20.0 | 0.05767497747071193 | 0.011534995494142386 | Defensive dividend equity at 52w high with +4.17% 21d active return and very low beta (0.27) into hike risk. |
| anthropic-claude-fable-5 | ENERGY | 20.0 | 0.058537403555853684 | 0.011707480711170738 | Brent ~$97 amid Iran war supply shock; XLE +10.5% 21d active, negative SPY beta gives hedge value. |
| anthropic-claude-fable-5 | BROAD_COMMODITIES | 15.0 | 0.028969359331476374 | 0.004345403899721456 | Broad inflation hedge: +12.98% 21d active, tariffs and energy shock support commodity prices; negative equity beta. |
| anthropic-claude-fable-5 | HEALTHCARE | 15.0 | 0.07461401242541665 | 0.011192101863812498 | Defensive sector turning: +5.24% 21d active after prolonged underperformance, low beta 0.32, near 52w high. |
| anthropic-claude-opus-4-8 | SP500 | 40.0 | 0.03321018229060946 | 0.013284072916243783 | Core broad equity exposure with strong Q2 earnings tracking +26.5% YoY supporting large-cap resilience. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | 0.07461401242541665 | 0.018653503106354163 | Defensive leadership with +5.24% active 21s return, low drawdown -3.74%, and shallow pullback offering value after prior underperformance. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | 0.0339193748890072 | 0.006783874977801441 | Positive +4.05% active 21s return, low vol 13% and shallow drawdown -2.42%; strong earnings backdrop. |
| anthropic-claude-opus-4-8 | DIVIDEND | 15.0 | 0.05767497747071193 | 0.00865124662060679 | Strong +4.17% active 21s return, recent +1.15% strength, low beta 0.27, at 52w high with low drawdown. |
| anthropic-claude-opus-5 | SP500 | 35.0 | 0.03321018229060946 | 0.01162356380171331 | Core benchmark exposure with Q2 earnings tracking +26.5% y/y. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | 0.07461401242541665 | 0.014922802485083332 | Defensive sector with positive relative momentum, low drawdown and tariff/rate insulation. |
| anthropic-claude-opus-5 | DIVIDEND | 20.0 | 0.05767497747071193 | 0.011534995494142386 | Strong relative trend, at 52-week high, low beta cushions mega-cap tech drawdown risk. |
| anthropic-claude-opus-5 | ENERGY | 15.0 | 0.058537403555853684 | 0.008780610533378053 | Oil near $97 on Iran-war supply shock supports energy cash flows; low correlation to SPY. |
| anthropic-claude-opus-5 | FINANCIALS | 10.0 | 0.0339193748890072 | 0.0033919374889007205 | Positive 21-day active return, shallow drawdown, benefits from higher-for-longer rates. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.03321018229060946 | 0.013284072916243783 | Core holding providing broad market exposure amid mixed economic signals and upcoming earnings. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.058537403555853684 | 0.017561221066756106 | Strong recent momentum and high quality evidence score, supported by elevated oil prices. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.07461401242541665 | 0.022384203727624997 | Defensive sector with positive recent active return and upcoming earnings reports. |
| openai-gpt-5-5 | DIVIDEND | 30.0 | 0.05767497747071193 | 0.01730249324121358 | Dividend equities show strong recent relative performance, low beta, shallow drawdown, and exposure to profitable mature companies ahead of a heavy earnings window. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | 0.07461401242541665 | 0.014922802485083332 | Healthcare combines strong 21-day active return and moderate beta with defensive characteristics if macro or tariff uncertainty weighs on broad risk appetite. |
| openai-gpt-5-5 | ENERGY | 20.0 | 0.058537403555853684 | 0.011707480711170738 | Energy has direct support from elevated crude prices after the Iran-war shock, strong recent active return, and possible earnings/geopolitical catalysts, while using sector equity rather than the more volatile oil ETP. |
| openai-gpt-5-5 | LARGE_VALUE | 15.0 | 0.04060586529165322 | 0.006090879793747983 | Large value has positive prior and recent active performance, lower volatility, low drawdown, and is near its 52-week high, fitting a one-month broadening and earnings-quality thesis. |
| openai-gpt-5-5 | UTILITIES | 15.0 | -0.06632101965867354 | -0.00994815294880103 | Utilities provide rate-sensitive defensive exposure with positive recent and prior active returns, useful if labor or tariff uncertainty pressures cyclicals. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 45.0 | -0.025641939450097295 | -0.011538872752543783 | Exceptional prior relative strength and a deep recent pullback create the strongest rebound setup, supported by the imminent mega-cap earnings cycle, though volatility warrants staying below the cluster cap. |
| openai-gpt-5-6-sol | DIVIDEND | 30.0 | 0.05767497747071193 | 0.01730249324121358 | Positive short- and medium-term relative performance, lower volatility, and a defensive profile provide exposure to broadening market participation. |
| openai-gpt-5-6-sol | ENERGY | 15.0 | 0.058537403555853684 | 0.008780610533378053 | Energy equities retain support from elevated crude prices and strong relative performance, while the smaller allocation accounts for oil's sharp extension and reversal risk. |
| openai-gpt-5-6-sol | HEALTHCARE | 10.0 | 0.07461401242541665 | 0.007461401242541666 | Recent benchmark-relative strength and defensive demand may persist if tariffs, softer employment, or policy uncertainty pressure cyclical equities. |
| xai-grok-4-3 | ENERGY | 40.0 | 0.058537403555853684 | 0.023414961422341476 | Recent 5s and 21s outperformance plus oil price stability support base case above SPY. |
| xai-grok-4-3 | INDUSTRIALS | 30.0 | -0.020037227636045096 | -0.0060111682908135285 | Positive 5s return and earnings tracking support modest outperformance. |
| xai-grok-4-3 | UTILITIES | 30.0 | -0.06632101965867354 | -0.01989630589760206 | Defensive characteristics and positive 5s return provide stability. |
| xai-grok-4-5 | ENERGY | 30.0 | 0.058537403555853684 | 0.017561221066756106 | Oil price persistence and energy sector momentum from geopolitical premium support outperformance versus broad equities over the one-month window. |
| xai-grok-4-5 | OIL | 20.0 | -0.03277489209159401 | -0.006554978418318803 | Direct crude exposure captures the largest recent active returns and geopolitical premium more efficiently than equities for the short horizon. |
| xai-grok-4-5 | BROAD_COMMODITIES | 20.0 | 0.028969359331476374 | 0.005793871866295275 | Diversified commodity basket benefits from energy spillover and inflation residual while offering lower single-name oil volatility. |
| xai-grok-4-5 | LARGE_VALUE | 15.0 | 0.04060586529165322 | 0.006090879793747983 | Value tilt shows positive active return and lower drawdown versus growth/tech, aligning with equal-weight outperformance and defensive rotation. |
| xai-grok-4-5 | HEALTHCARE | 15.0 | 0.07461401242541665 | 0.011192101863812498 | Strong recent active return, defensive characteristics, and shallow drawdown provide ballast with base case above SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SP500 | 3 | 0.65 | 0.03321018229060946 | 0.053229497710624886 | 0.020019315420015428 | 0.2758303313492043 |  | True | True |
| anthropic-claude-fable-5 | LARGE_VALUE | 5 | 0.62 | 0.04060586529165322 | 0.05096174155634304 | 0.01775155926573358 | 0.2780980875034862 |  | True | True |
| anthropic-claude-opus-5 | SP500 | 5 | 0.55 | 0.03321018229060946 | 0.050253909803217804 | 0.017043727512608346 | 0.2788059192566114 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 4 | 0.55 | 0.03321018229060946 | 0.047372697621006175 | 0.014162515330396717 | 0.28168713143882307 |  | True | True |
| openai-gpt-5-5 | DIVIDEND | 5 | 0.56 | 0.05767497747071193 | 0.040075503282414604 | 0.006865320991805146 | 0.2889843257774146 |  | True | True |
| xai-grok-4-5 | ENERGY | 5 | 0.62 | 0.058537403555853684 | 0.034083096172293055 | 0.0008729138816835971 | 0.2949767328875362 |  | True | True |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 4 | 0.57 | -0.025641939450097295 | 0.022005632264589514 | -0.011204550026019944 | 0.3070541967952397 |  | False | True |
| xai-grok-4-3 | ENERGY | 3 | 0.55 | 0.058537403555853684 | -0.0024925127660741127 | -0.03570269505668357 | 0.3315523418259033 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | SP500 | 0.017043727512608346 | 0.21178 | 0.08047845647657166 |
| anthropic-claude-fable-5 | LARGE_VALUE | 0.01775155926573358 | 0.46416 | 0.038244483078536666 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 016707fe54a92a820ba5cb2c560e626a47bbbc30b710a1a9d35d156e13685123 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | 9ca38f88d9f0339ddaaef13f31e82e9635b968bf8c6467680ed52b285a3ca40e |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 9210d3e9a412d6e041ac8a954c0758259cb8fe7e239eb4acd10a646b7036bbd3 |
| market_data/universe_decision_context.md | 3c027e726e5d0120375352a529da590b547b947ecd059dad8c48ed45a91b36fa |
| market_data/universe_decision_context.json | 12c4f592509ddf0bb649d2bb3e0a76673f8ad66972f5bb70928ea5bce2c3bdfb |
| market_data/decision_context_source_history.json | ebd65f39ea9fde61dfc4e669b64a26b19fb79d71c77d8282cecc90482ded1743 |
| market_data/universe_quality_evidence.md | 40986d7de45369cbba7a9c4efc481d7127d331e8f39db8e5bc9ee157b3419096 |
| market_data/universe_quality_evidence.json | 069fb142aa635230c3019724e14830ed5e8fb989f8e9fa68af1f3a5947b2ae76 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 8c0ecd265368f14faa1b51e514cbddc9894c887549e0cee332687deda61c9ffd | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 0908a232f37a1d2658e273efd857369e78dfd4143a83fda7c8d422eeb77d1167 | yes |
| Final briefing | research/final_briefing.md | model-facing | 016707fe54a92a820ba5cb2c560e626a47bbbc30b710a1a9d35d156e13685123 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
