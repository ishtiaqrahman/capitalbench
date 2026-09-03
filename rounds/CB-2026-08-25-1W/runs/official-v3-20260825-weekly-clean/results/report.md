# CapitalBench Report: CB-2026-08-25-1W / official-v3-20260825-weekly-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260825-weekly-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-25-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-25
- Decision deadline: 2026-08-26T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-26
- Exit date: 2026-09-02
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | CYBERSECURITY | 3 | 0.57 | Broad participation and falling Treasury yields support risk assets, but 5.10% cross-sectional dispersion, Nvidia earnings, Jackson Hole, and several macro releases create a highly event-driven week. Selective reversals in strong prior trends have better support than chasing recent commodity or crypto surges. | Nvidia results could trigger a broad technology selloff and invalidate the robotics and cybersecurity reversals.; Jackson Hole communication or inflation data could push yields higher despite their recent decline.; A further crude-price decline could overwhelm energy-equity relative strength.; High cross-sectional dispersion makes one-week rankings unusually sensitive to event surprises. |
| xai-grok-4-5 | xai | portfolio | CYBERSECURITY | 3 | 0.5867 | SPY near highs with modest weekly gain; soft labor/housing/confidence data and falling yields support selective quality pullbacks, while oil shock and crypto volume spikes create mixed continuation vs reversal setups into Nvidia and Jackson Hole. | Nvidia earnings Aug 26 can reverse tech/growth pullback theses including CIBR and ARKQ; Jackson Hole and soft macro prints may drive risk-off that hits high-beta names harder than SPY; Further crude weakness or inventory surprise can pressure ENERGY/OIL without mean reversion; Crypto volume spikes can unwind quickly, contaminating risk appetite for growth factors |
| xai-grok-4-3 | xai | portfolio | METALS_MINING | 3 | 0.5833 | Mixed signals from macro releases and sector-specific volatility favor selective reversal candidates over broad continuation. | Nvidia earnings volatility on Aug 26; GDP revision and Fed speakers; Oil inventory and energy price swings |
| anthropic-claude-fable-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.5833 | 5-session active dispersion of 5.1% is elevated with equal-weight beating SPY by 1.1% and yields falling (10y 4.63% from 4.74%), a setup favoring pullback reversals in previously strong high-beta tech ahead of Nvidia earnings on Aug 26 within the window. | Nvidia earnings miss on Aug 26 could hit all three tech-cluster picks simultaneously; Jackson Hole commentary could push yields back up, pressuring high-beta growth; Crypto and metals momentum could extend, making pullback tech picks lag; Weak labor data (payrolls -23k) may signal broader growth deterioration hurting cyclical tech demand |
| xai-grok-4-6 | xai | portfolio | CYBERSECURITY | 3 | 0.5633 | SPY is near a 52-week high with modest 5-session weakness while 5s active-return dispersion is 5.10% and equal-weight led cap-weight. The slate mixes shock pullbacks in quality growth/defense/energy against stretched crypto and metals continuation, with Jackson Hole, GDP/PCE, oil inventories, and Nvidia results inside the week. | Nvidia earnings after the Aug 26 close can dominate high-beta software, robotics, and cyber versus SPY.; Jackson Hole plus Aug 26 GDP/PCE can reverse rate-sensitive banks and duration-linked defensives.; Further crude weakness after Brent -3.6% and the petroleum status report can keep ENERGY/OIL lagging.; 5s dispersion of 5.10% and stretched crypto volume z-scores raise gap/whipsaw risk in any non-SPY sleeve. |
| anthropic-claude-opus-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.5633 | Broad market is near highs with breadth improving (RSP beat SPY by 1.1% over 5 sessions) while mega-cap tech lagged into the Nvidia print. Yields fell to 4.63%, gold and silver surged, oil dropped sharply on weak Brent. The week contains Nvidia earnings, Jackson Hole, payroll benchmark revisions, JOLTS and the Beige Book, so idiosyncratic dispersion is elevated but no single directional macro regime dominates. Quality-pullback names with strong prior relative trends and shallow recent underperformance offer the cleanest one-week reversal setups; crypto after a 22-29% active spike is stretched, not a fresh entry. | Nvidia's August 26 report could drive a sharp directional move in tech-heavy candidates including cybersecurity, software and robotics.; Jackson Hole commentary or the August 28 payroll benchmark revisions could reprice rates and reverse the recent yield decline.; Relative pullbacks in defense and cybersecurity may reflect information not present in the briefing and continue rather than revert.; Precious-metals and crypto momentum could persist, causing selected reversal names to underperform SPY on a relative basis.; One-week horizon leaves little time for mean reversion to complete, and high-volatility candidates can miss on noise alone. |
| google-gemini-3-1-pro | google | portfolio | CYBERSECURITY | 3 | 0.58 | The market is showing mixed signals with some sectors experiencing pullbacks while others continue to show strength. The upcoming Nvidia earnings and Jackson Hole symposium are key catalysts. | Nvidia earnings could cause volatility in the broader market, particularly in tech sectors.; Jackson Hole symposium could lead to unexpected shifts in interest rate expectations, impacting rate-sensitive sectors. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 127.3499984741211 | 141.15 | 0.10836279302102403 | 1 |
| BRAZIL | Brazil Equities | 35.720001220703125 | 38.09 | 0.06634934765688749 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 18.18000030517578 | 19.06 | 0.04840482288516168 | 3 |
| ENERGY | Energy Sector | 62.43000030517578 | 65.1 | 0.042767894950704655 | 4 |
| TAIWAN | Taiwan Equities | 106.38999938964844 | 109.43 | 0.02857412000932258 | 5 |
| AGRICULTURE | Agriculture Commodities | 28.59000015258789 | 29.27 | 0.02378453458492058 | 6 |
| SOFTWARE | Software | 102.38999938964844 | 103.42 | 0.010059582151493718 | 7 |
| JAPAN | Japan Equities | 95.43000030517578 | 96.04 | 0.006392116660101754 | 8 |
| US_DOLLAR | US Dollar | 28.020000457763672 | 28.17 | 0.005353302633325674 | 9 |
| INDIA | India Equities | 49.75 | 49.97 | 0.004422110552763758 | 10 |
| TECHNOLOGY | Technology Sector | 182.83999633789062 | 183.6 | 0.004156659797262652 | 11 |
| YEN | Japanese Yen | 57.54999923706055 | 57.72999954223633 | 0.003127720374666243 | 12 |
| EMERGING_MARKETS | Emerging Markets | 60.65999984741211 | 60.77 | 0.0018133886064060079 | 13 |
| LARGE_GROWTH | US Large-Cap Growth | 121.75 | 121.81 | 0.0004928131416837012 | 14 |
| BROAD_AI_TECH | Broad AI Technology | 63.06999969482422 | 63.08 | 0.00015855882708359914 | 15 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 16 |
| DIVIDEND | US Dividend Equities | 35.04999923706055 | 35.01 | -0.001141205076496954 | 17 |
| SP500 | S&P 500 | 766.0800170898438 | 765.16 | -0.001200941245457221 | 18 |
| CYBERSECURITY | Cybersecurity | 93.66000366210938 | 93.54 | -0.0012812690307199004 | 19 |
| COMMUNICATIONS | Communication Services Sector | 112.61000061035156 | 112.42 | -0.0016872445548508086 | 20 |
| SOUTH_KOREA | South Korea Equities | 179.17999267578125 | 178.86 | -0.0017858728031105997 | 21 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.62999725341797 | 91.4 | -0.0025100650476052033 | 22 |
| NASDAQ100 | Nasdaq 100 | 711.3699951171875 | 709.24 | -0.0029942155724976827 | 23 |
| HEALTHCARE | Healthcare Sector | 173.5399932861328 | 172.95 | -0.003399753998837851 | 24 |
| TOTAL_US_MARKET | Total US Stock Market | 378.2300109863281 | 376.88 | -0.0035692857444273862 | 25 |
| AUSTRALIA | Australia Equities | 30.149999618530273 | 30.03 | -0.0039800869004495976 | 26 |
| REGIONAL_BANKS | Regional Banks | 74.58000183105469 | 74.24 | -0.004558887405566092 | 27 |
| LARGE_VALUE | US Large-Cap Value | 258.4599914550781 | 257.08 | -0.005339284611552753 | 28 |
| SMALL_VALUE | US Small-Cap Value | 224.33999633789062 | 223.04 | -0.00579475955742037 | 29 |
| TIPS | Treasury Inflation-Protected Securities | 107.51000213623047 | 106.86 | -0.006045968963955817 | 30 |
| EURO | Euro | 107.5999984741211 | 106.9 | -0.00650556211940323 | 31 |
| METALS_MINING | Metals and Mining | 120.30999755859375 | 119.46 | -0.007065061722570376 | 32 |
| CONSUMER_STAPLES | Consumer Staples Sector | 86.2699966430664 | 85.53 | -0.008577682529977038 | 33 |
| SEMICONDUCTORS | Semiconductors | 555.77001953125 | 550.48 | -0.009518360734376619 | 34 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.9000015258789 | 79.11 | -0.009887378107533928 | 35 |
| CHINA | China Equities | 55.099998474121094 | 54.54 | -0.010163311971489564 | 36 |
| FINANCIALS | Financials Sector | 58.2599983215332 | 57.66 | -0.010298632660815654 | 37 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.86000061035156 | 96.84 | -0.010423059513486876 | 38 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.779998779296875 | 47.25 | -0.011092482060223952 | 39 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.58000183105469 | 92.51 | -0.011434086451359793 | 40 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.44999694824219 | 104.22 | -0.011664267272059825 | 41 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.44999694824219 | 72.59 | -0.011708604274663137 | 42 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.30999755859375 | 94.15 | -0.012170785734000433 | 43 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.31999969482422 | 92.18 | -0.012216027631292814 | 44 |
| UNITED_KINGDOM | United Kingdom Equities | 48.86000061035156 | 48.22 | -0.013098661530019928 | 45 |
| COPPER | Copper | 40.060001373291016 | 39.53 | -0.01323018859516012 | 46 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.77999877929688 | 105.35 | -0.013392009698862561 | 47 |
| MATERIALS | Materials Sector | 53.66999816894531 | 52.95 | -0.013415282159668807 | 48 |
| BITCOIN_ETF | Bitcoin ETF | 44.459999084472656 | 43.790000915527344 | -0.015069684722042731 | 49 |
| CANADA | Canada Equities | 62.22999954223633 | 61.27 | -0.015426635855665727 | 50 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 222.11000061035156 | 218.6 | -0.01580298320969875 | 51 |
| LOW_VOL | US Low Volatility Equities | 75.87999725341797 | 74.66 | -0.016077982308611904 | 52 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.30000305175781 | 81.95 | -0.016206518635047296 | 53 |
| SMALL_CAP | US Small-Cap Stocks | 298.92999267578125 | 294.01 | -0.016458678608129773 | 54 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.33000183105469 | 120.24 | -0.01708494890681944 | 55 |
| MEXICO | Mexico Equities | 77.55000305175781 | 76.22 | -0.01715026433809619 | 56 |
| BIOTECH | Biotechnology | 168.38999938964844 | 165.37 | -0.017934553124263952 | 57 |
| EUROPE | Europe Equities | 92.69999694824219 | 90.96 | -0.018770194234350335 | 58 |
| UTILITIES | Utilities Sector | 43.5099983215332 | 42.67 | -0.019305868856296482 | 59 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.16000366210938 | 114.86 | -0.01963130411588765 | 60 |
| MID_CAP | US Mid-Cap Stocks | 76.62000274658203 | 75.11 | -0.01970768327399197 | 61 |
| MOMENTUM | US Momentum Equities | 304.0 | 297.04 | -0.02289473684210519 | 62 |
| SOUTH_AFRICA | South Africa Equities | 71.68000030517578 | 69.99 | -0.02357701308566762 | 63 |
| REAL_ESTATE | Real Estate Sector | 45.09000015258789 | 43.73 | -0.030161901707375316 | 64 |
| SOLAR | Solar Energy | 48.779998779296875 | 47.27 | -0.030955285303076785 | 65 |
| ETHEREUM_ETF | Ethereum ETF | 18.649999618530273 | 18.049999237060547 | -0.032171602881620354 | 66 |
| SILVER | Silver | 61.59000015258789 | 59.07 | -0.04091573544966143 | 67 |
| INDUSTRIALS | Industrials Sector | 180.33999633789062 | 172.78 | -0.041920796780576475 | 68 |
| GOLD | Gold | 86.37000274658203 | 82.55 | -0.044228350412240824 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.3800048828125 | 223.37 | -0.055038516854512776 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | CYBERSECURITY | 35.0 | -0.0012812690307199004 | -0.0004484441607519651 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | AUTONOMOUS_ROBOTICS | 35.0 | -0.01708494890681944 | -0.005979732117386804 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SOFTWARE | 30.0 | 0.010059582151493718 | 0.0030178746454481153 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | CYBERSECURITY | 35.0 | -0.0012812690307199004 | -0.0004484441607519651 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SOFTWARE | 35.0 | 0.010059582151493718 | 0.003520853753022801 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | AEROSPACE_DEFENSE | 30.0 | -0.055038516854512776 | -0.016511555056353832 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | CYBERSECURITY | 35.0 | -0.0012812690307199004 | -0.0004484441607519651 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 35.0 | -0.055038516854512776 | -0.01926348089907947 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 30.0 | -0.004558887405566092 | -0.0013676662216698277 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | CYBERSECURITY | 35.0 | -0.0012812690307199004 | -0.0004484441607519651 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | ENERGY | 35.0 | 0.042767894950704655 | 0.014968763232746629 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | AUTONOMOUS_ROBOTICS | 30.0 | -0.01708494890681944 | -0.005125484672045833 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | METALS_MINING | 35.0 | -0.007065061722570376 | -0.0024727716028996316 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | BITCOIN_ETF | 35.0 | -0.015069684722042731 | -0.005274389652714956 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | ENERGY | 30.0 | 0.042767894950704655 | 0.012830368485211395 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | -0.0012812690307199004 | -0.0004484441607519651 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | AUTONOMOUS_ROBOTICS | 35.0 | -0.01708494890681944 | -0.005979732117386804 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | ENERGY | 30.0 | 0.042767894950704655 | 0.012830368485211395 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | -0.0012812690307199004 | -0.0004484441607519651 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 35.0 | -0.055038516854512776 | -0.01926348089907947 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | ENERGY | 30.0 | 0.042767894950704655 | 0.012830368485211395 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | CYBERSECURITY | 3 | 0.57 | -0.0012812690307199004 | 0.009394834399948832 | 0.010595775645406053 | 0.0989679586210752 |  | True | True |
| xai-grok-4-5 | CYBERSECURITY | 3 | 0.5867 | -0.0012812690307199004 | 0.0064021922070726265 | 0.0076031334525298476 | 0.1019606008139514 |  | True | True |
| xai-grok-4-3 | METALS_MINING | 3 | 0.5833 | -0.007065061722570376 | 0.005083207229596808 | 0.006284148475054029 | 0.10327958579142722 |  | True | True |
| anthropic-claude-fable-5 | CYBERSECURITY | 3 | 0.5833 | -0.0012812690307199004 | -0.0034103016326906535 | -0.0022093603872334324 | 0.11177309465371468 |  | False | False |
| xai-grok-4-6 | CYBERSECURITY | 3 | 0.5633 | -0.0012812690307199004 | -0.006881556574620041 | -0.00568061532916282 | 0.11524434959564407 |  | False | False |
| anthropic-claude-opus-5 | CYBERSECURITY | 3 | 0.5633 | -0.0012812690307199004 | -0.013439145464082997 | -0.012238204218625776 | 0.12180193848510702 |  | False | False |
| google-gemini-3-1-pro | CYBERSECURITY | 3 | 0.58 | -0.0012812690307199004 | -0.021079591281501265 | -0.019878650036044044 | 0.1294423843025253 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | f80b43cbb211635532aa200e6f0bb830f1cfa3c34b67c84311f51497a3a9f02b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 140724bc0078da540ce0a71ef740ea5069e4763a95fd4e3df8fb8619afeae84d |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 38e6fdc93972d9e01315c01cc2e12d3513b7bd2e994eef354ae0d201255411ab |
| market_data/universe_decision_context.md | 8f3af1e62ba266f13849e2fa6549a6acc0181e3f73a7868caa8941ebf227981f |
| market_data/universe_decision_context.json | ea965d37efe4d02b77bbc7663207df6678dfe0acd1d401ae57493f3b53d079ed |
| market_data/decision_context_source_history.json | 402aa9d6e62239df2eb914f135cc645c6b76c0257c8efb20419cc2c21b4c205c |
| market_data/universe_quality_evidence.md | 2e92dbecaaf0086a3e1746bc3fc76e620aaf30da2b14c05af4a067c91f5ecd31 |
| market_data/universe_quality_evidence.json | f38dbf37d9c2e194448012e9b067fdc48330cfd5623db865d1863f0c973bd558 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | fea2ce583f511a928c8ad143ddc49912f10b1f67f39127a844b526c2473ef697 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | b6e5821ef98a7fb55e227b36298f660dd1b55eb7f23bbae2731ca935e77c16c9 | yes |
| Final briefing | research/final_briefing.md | model-facing | f80b43cbb211635532aa200e6f0bb830f1cfa3c34b67c84311f51497a3a9f02b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
