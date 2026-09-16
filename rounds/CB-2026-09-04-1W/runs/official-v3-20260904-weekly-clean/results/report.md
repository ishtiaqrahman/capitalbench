# CapitalBench Report: CB-2026-09-04-1W / official-v3-20260904-weekly-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260904-weekly-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-04-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-04
- Decision deadline: 2026-09-08T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-08
- Exit date: 2026-09-15
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | SOFTWARE | 3 | 0.59 | Modest SPY strength with low cross-sectional dispersion; mixed labor/inflation data and rate-hike odds favor selective quality pullbacks over pure continuation or deep losers with fundamental drag. High-vol tech pullbacks and commodity strength compete with defensive quality. | September CPI/PPI and ECB decision inside window could reprice rates and growth equities; 58% implied odds of Fed hike and elevated yields pressure duration and high-beta tech; Oil/geopolitical supply shocks and trade-threat rhetoric raise commodity and EM volatility; High horizon vol in software/cyber/crypto can reverse any bounce before Sept 15 close |
| xai-grok-4-6 | xai | portfolio | SOFTWARE | 3 | 0.56 | SPY is near a 52-week high with low 5-session dispersion while software and cyber show large relative pullbacks after strong prior active returns; CPI/PPI land inside the week and a 58% hike probability plus hawkish Fed dissent raise rate-sensitive risk, so the week is mixed rather than a clean continuation or reversal tape. | August CPI and PPI on Sept 10-11 can reprice the 58% hike odds and hit high-beta software/cyber.; Software and cyber horizon vol near 41% can dominate a one-week excess even if the pullback was overdone.; Oil continuation can reverse if diesel/refinery headlines fade while SPY holds near highs.; Trade-threat rhetoric and euro-area energy inflation can widen EM and cyclical dispersion versus SPY. |
| google-gemini-3-1-pro | google | portfolio | SOFTWARE | 3 | 0.61 | The market is experiencing a slight pullback with mixed economic data, presenting opportunities in high-quality assets that have recently underperformed. | Continued weakness in the software sector could lead to further underperformance.; Agricultural commodities may face unexpected supply shocks or demand shifts. |
| anthropic-claude-opus-5 | anthropic | portfolio | SOFTWARE | 3 | 0.56 | Macro backdrop is stagflationary at the margin: PCE 3.7% y/y headline, euro-area inflation re-accelerating to 3.3%, diesel sharply higher, and FedWatch pricing 58% odds of a September hike. Cross-sectional dispersion (2.03% 5-session active) is normal; positive asset share near 54% shows no clean regime. CPI and PPI land inside the scoring week, and the FOMC decision falls just after the exit, so rate-sensitive and high-beta names carry event risk without event resolution. I see mostly mixed signals: a few quality pullbacks (SOFTWARE, MATERIALS, AGRICULTURE) look like temporary relative overreactions with strong prior trends, while oil and Brazil strength looks like supported commodity continuation rather than a repeatable one-week edge. | August CPI on September 11 and PPI on September 10 could reprice rate-hike odds and hit high-beta software hardest; Hike probability at 58% before the September 16 FOMC creates a hawkish drift risk for all equity exposures inside the window; SOFTWARE has 41% annualized volatility, so the reversal thesis can invert quickly within one week; Trade-halt rhetoric from September 4 could escalate and pressure materials and commodity-linked exposures; Agriculture's elevated volume z-score may signal distribution rather than accumulation |
| openai-gpt-6-astra | openai | portfolio | SP500 | 2 | 0.55 | Five-session active dispersion of 2.03% and oil's sharp divergence from equities indicate substantial cross-sectional risk. Energy disruptions support oil independently of momentum, while elevated inflation and hike expectations limit confidence in growth-stock reversals. Producer and consumer prices fall inside the scoring window; the Fed decision does not. Reversal evidence is strongest where prior relative strength survives a shallow pullback, but the supplied quality scores are technical composites, not evidence of business fundamentals. | September 10 producer prices and September 11 consumer prices could sharply reprice rates and reverse cross-asset leadership.; Refinery restoration or weaker crude demand could unwind oil's already substantial advance.; Agriculture's elevated volume could reflect informed selling; crop, weather, and inventory evidence is absent.; Trade threats could become concrete during the window, changing commodity demand and equity risk premiums.; Moves before the September 8 entry close are not captured, and the September 16 Fed decision occurs after exit. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SOFTWARE | 3 | 0.555 | Macro backdrop is stagflationary: core PCE 3.3% y/y, oil up 19% over 21 sessions with diesel at $5.85, 10y at 4.78%, and a 58% market-implied probability of a September hike with a hawkish dissent already on record. Weekly window contains PPI (Sep 10), ECB (Sep 10), and CPI (Sep 11) but the FOMC decision falls after the exit. Active dispersion is moderate (2.03%), breadth is weak (RSP -0.87% vs SPY over 5 sessions). Cross-section shows high-beta tech/crypto strength alongside a sharp software/cyber pullback; energy continuation is supply-driven. With rate-hike risk unresolved and CPI in-window, edges are modest and reversal candidates need a defensible pullback plus a prior trend. | August CPI on September 11 prints hot and lifts September hike odds above 58%, hitting high-duration software and cyber names hardest; Oil supply disruption extends, pushing yields and inflation expectations up and rotating capital away from growth toward energy; Trade-halt threat against surplus countries escalates, hitting risk assets and cyclicals such as materials; Software pullback reflects sector-specific earnings or AI-displacement concerns not captured in the briefing, so selling continues |
| xai-grok-4-3 | xai | portfolio | AGRICULTURE | 3 | 0.5833 | Mixed signals with commodity and value pullbacks showing reversal potential amid stable labor data and scheduled inflation releases. | August CPI and PPI releases on September 10-11; ECB monetary policy decision; Trade policy statements |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 141.9600067138672 | 161.86 | 0.14018027856425097 | 1 |
| CYBERSECURITY | Cybersecurity | 94.58999633789062 | 101.0 | 0.06776618998072292 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 19.010000228881836 | 20.1 | 0.057338230299552206 | 3 |
| ENERGY | Energy Sector | 64.05999755859375 | 65.93 | 0.02919142230212901 | 4 |
| COMMUNICATIONS | Communication Services Sector | 112.02999877929688 | 114.03 | 0.017852372065478628 | 5 |
| SOFTWARE | Software | 104.56999969482422 | 105.55 | 0.009371715674053815 | 6 |
| YEN | Japanese Yen | 58.66999816894531 | 59.13 | 0.007840495064105335 | 7 |
| US_DOLLAR | US Dollar | 28.079999923706055 | 28.22 | 0.004985757716322148 | 8 |
| AGRICULTURE | Agriculture Commodities | 28.850000381469727 | 28.88 | 0.0010398481155493577 | 9 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.44999694824219 | 91.51 | 0.0006561296201221811 | 10 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 11 |
| BRAZIL | Brazil Equities | 37.86000061035156 | 37.78 | -0.0021130641590557664 | 12 |
| EURO | Euro | 107.1500015258789 | 106.49 | -0.006159603513580025 | 13 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.16000366210938 | 78.38 | -0.009853507150388574 | 14 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.58000183105469 | 83.73 | -0.010049678560571929 | 15 |
| TIPS | Treasury Inflation-Protected Securities | 106.97000122070312 | 105.79 | -0.011031141509183606 | 16 |
| MUNICIPAL_BONDS | Municipal Bonds | 104.02999877929688 | 102.87 | -0.011150618022767178 | 17 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.4800033569336 | 104.28 | -0.011376595740833495 | 18 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.0 | 95.85 | -0.011855670103092852 | 19 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.45000076293945 | 46.87 | -0.012223408927581336 | 20 |
| DIVIDEND | US Dividend Equities | 34.79999923706055 | 34.33 | -0.013505725498982768 | 21 |
| JAPAN | Japan Equities | 98.27999877929688 | 96.92 | -0.013838001589224325 | 22 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.25 | 90.82 | -0.015501355013550211 | 23 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.47000122070312 | 92.99 | -0.015666361824697272 | 24 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.72000122070312 | 91.24 | -0.015962049193466443 | 25 |
| LARGE_VALUE | US Large-Cap Value | 257.6300048828125 | 253.49 | -0.016069575765041977 | 26 |
| REGIONAL_BANKS | Regional Banks | 75.2699966430664 | 74.05 | -0.01620827285075732 | 27 |
| UNITED_KINGDOM | United Kingdom Equities | 48.59000015258789 | 47.8 | -0.01625849249036926 | 28 |
| SP500 | S&P 500 | 770.1900024414062 | 757.39 | -0.016619278880317667 | 29 |
| ETHEREUM_ETF | Ethereum ETF | 18.520000457763672 | 18.2 | -0.017278642000763345 | 30 |
| MOMENTUM | US Momentum Equities | 304.8599853515625 | 299.51 | -0.01754899169660773 | 31 |
| LOW_VOL | US Low Volatility Equities | 74.73999786376953 | 73.42 | -0.017661197504655002 | 32 |
| TOTAL_US_MARKET | Total US Stock Market | 379.7300109863281 | 372.84 | -0.01814449947854191 | 33 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.20999908447266 | 80.71 | -0.01824594454661632 | 34 |
| TECHNOLOGY | Technology Sector | 187.27999877929688 | 183.74 | -0.018902172161313624 | 35 |
| REAL_ESTATE | Real Estate Sector | 43.93000030517578 | 43.07 | -0.01957660594585653 | 36 |
| NASDAQ100 | Nasdaq 100 | 718.9600219726562 | 704.54 | -0.02005677858567312 | 37 |
| BROAD_AI_TECH | Broad AI Technology | 64.31999969482422 | 62.96 | -0.02114427396263896 | 38 |
| FINANCIALS | Financials Sector | 58.099998474121094 | 56.85 | -0.021514604250426395 | 39 |
| HEALTHCARE | Healthcare Sector | 171.4499969482422 | 167.66 | -0.022105552730842692 | 40 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 219.0 | 213.96 | -0.023013698630136914 | 41 |
| LARGE_GROWTH | US Large-Cap Growth | 123.41000366210938 | 120.45 | -0.023985119311832448 | 42 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.25 | 118.95 | -0.026993865030674802 | 43 |
| CANADA | Canada Equities | 62.040000915527344 | 60.29 | -0.028207622335630123 | 44 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.76000213623047 | 71.53 | -0.03023321680647162 | 45 |
| EUROPE | Europe Equities | 91.73999786376953 | 88.96 | -0.030303007722953357 | 46 |
| SMALL_VALUE | US Small-Cap Value | 224.6199951171875 | 217.68 | -0.03089660434533803 | 47 |
| GOLD | Gold | 83.38999938964844 | 80.78 | -0.03129870978236782 | 48 |
| COPPER | Copper | 39.95000076293945 | 38.67 | -0.03204006854805552 | 49 |
| MATERIALS | Materials Sector | 52.439998626708984 | 50.73 | -0.03260867031827197 | 50 |
| MEXICO | Mexico Equities | 76.62999725341797 | 74.03 | -0.0339292358946548 | 51 |
| MID_CAP | US Mid-Cap Stocks | 75.8499984741211 | 73.23 | -0.03454183950992429 | 52 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.91000366210938 | 110.88 | -0.035070955823476635 | 53 |
| EMERGING_MARKETS | Emerging Markets | 61.439998626708984 | 59.22 | -0.03613279095588906 | 54 |
| CHINA | China Equities | 54.90999984741211 | 52.91 | -0.036423235348203575 | 55 |
| INDUSTRIALS | Industrials Sector | 175.27000427246094 | 168.85 | -0.0366292241453986 | 56 |
| SMALL_CAP | US Small-Cap Stocks | 296.010009765625 | 285.14 | -0.03672176415328543 | 57 |
| SOUTH_AFRICA | South Africa Equities | 71.63999938964844 | 68.92 | -0.03796760766083229 | 58 |
| SILVER | Silver | 59.81999969482422 | 57.53 | -0.038281506293995404 | 59 |
| UTILITIES | Utilities Sector | 43.08000183105469 | 41.32 | -0.04085426546537352 | 60 |
| SEMICONDUCTORS | Semiconductors | 567.010009765625 | 542.11 | -0.04391458587462582 | 61 |
| AUSTRALIA | Australia Equities | 30.229999542236328 | 28.89 | -0.04432681318317999 | 62 |
| INDIA | India Equities | 49.90999984741211 | 47.59 | -0.046483667691944563 | 63 |
| BITCOIN_ETF | Bitcoin ETF | 45.22999954223633 | 43.11 | -0.04687153578802594 | 64 |
| TAIWAN | Taiwan Equities | 112.18000030517578 | 106.67 | -0.049117492335410184 | 65 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 225.61000061035156 | 214.0 | -0.05146048747370491 | 66 |
| BIOTECH | Biotechnology | 163.80999755859375 | 154.03 | -0.05970330080186659 | 67 |
| SOLAR | Solar Energy | 48.040000915527344 | 45.09 | -0.06140717858674827 | 68 |
| SOUTH_KOREA | South Korea Equities | 188.8699951171875 | 176.49 | -0.06554770708553315 | 69 |
| METALS_MINING | Metals and Mining | 118.62000274658203 | 109.44 | -0.07739000618802927 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SOFTWARE | 35.0 | 0.009371715674053815 | 0.0032801004859188353 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | MATERIALS | 35.0 | -0.03260867031827197 | -0.011413034611395189 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 30.0 | -0.016619278880317667 | -0.0049857836640953 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | SOFTWARE | 35.0 | 0.009371715674053815 | 0.0032801004859188353 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | MATERIALS | 35.0 | -0.03260867031827197 | -0.011413034611395189 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | AGRICULTURE | 30.0 | 0.0010398481155493577 | 0.0003119544346648073 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOFTWARE | 35.0 | 0.009371715674053815 | 0.0032801004859188353 | V3 selected model rank 1: overreaction with 65% estimated probability of beating SPY. |
| google-gemini-3-1-pro | AGRICULTURE | 35.0 | 0.0010398481155493577 | 0.0003639468404422752 | V3 selected model rank 2: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | DIVIDEND | 30.0 | -0.013505725498982768 | -0.00405171764969483 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-6-astra | AGRICULTURE | 35.0 | 0.0010398481155493577 | 0.0003639468404422752 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 65.0 | -0.016619278880317667 | -0.010802531272206484 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | AGRICULTURE | 35.0 | 0.0010398481155493577 | 0.0003639468404422752 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | DIVIDEND | 35.0 | -0.013505725498982768 | -0.004727003924643969 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | MATERIALS | 30.0 | -0.03260867031827197 | -0.009782601095481592 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | SOFTWARE | 35.0 | 0.009371715674053815 | 0.0032801004859188353 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | 0.06776618998072292 | 0.02371816649325302 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | AGRICULTURE | 30.0 | 0.0010398481155493577 | 0.0003119544346648073 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SOFTWARE | 35.0 | 0.009371715674053815 | 0.0032801004859188353 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | 0.06776618998072292 | 0.02371816649325302 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 30.0 | -0.016619278880317667 | -0.0049857836640953 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | SOFTWARE | 3 | 0.59 | 0.009371715674053815 | 0.027310221413836662 | 0.04392950029415433 | 0.11287005715041432 |  | True | True |
| xai-grok-4-6 | SOFTWARE | 3 | 0.56 | 0.009371715674053815 | 0.022012483315076554 | 0.03863176219539422 | 0.11816779524917442 |  | True | True |
| google-gemini-3-1-pro | SOFTWARE | 3 | 0.61 | 0.009371715674053815 | -0.00040767032333371934 | 0.016211608556983947 | 0.1405879488875847 |  | True | False |
| anthropic-claude-opus-5 | SOFTWARE | 3 | 0.56 | 0.009371715674053815 | -0.007820979690811546 | 0.008798299189506122 | 0.14800125825506252 |  | True | False |
| openai-gpt-6-astra | SP500 | 2 | 0.55 | -0.016619278880317667 | -0.010438584431764208 | 0.006180694448553459 | 0.15061886299601518 |  | True | False |
| anthropic-claude-fable-5-1 | SOFTWARE | 3 | 0.555 | 0.009371715674053815 | -0.013118717789571653 | 0.003500561090746014 | 0.15329899635382263 |  | True | False |
| xai-grok-4-3 | AGRICULTURE | 3 | 0.5833 | 0.0010398481155493577 | -0.014145658179683284 | 0.002473620700634383 | 0.15432593674393424 |  | True | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | SOFTWARE | 0.008798299189506122 | 0.226215 | 0.03889352690805703 |
| openai-gpt-6-astra | SP500 | 0.006180694448553459 | 0.30922 | 0.019988016456094233 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | befe1aa32232427435a399cf0e93d11b5531eb01b342bd2607a3f3af7348ca10 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | d508c24e2cc904c5341cfc07dacc8aec2cbce83c4ee24ed76b11f26e785e5861 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 4c56af0f82cb66748ef2c5d312625e05d3ee828de6a2c113e0d6ad790792acd7 |
| market_data/universe_decision_context.md | bbd67102e68df4954cd0e620264168b4cf692b1563191f38a1803f2a32924e48 |
| market_data/universe_decision_context.json | 4fb2fcdeb80aafde1ec85cebecabdf98272ea901bac4b9c36ba2a942ef24602b |
| market_data/decision_context_source_history.json | 23250589a77632258bfbd680757c4d9a8f78e5568c2dca6350a4cbbf3c1ec257 |
| market_data/universe_quality_evidence.md | afbc88ae149852edf67256afef980fefd5d14a438993a62b0394e3d95326692d |
| market_data/universe_quality_evidence.json | 744b1b7a1916b02eaf81b0e7776af383543056a1ac936db35546a57c22c6c13c |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 82676ab576a6ffbd319bf6aa3d67ac360f8609d6eb42f12f1d1fc6a159566cd4 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 4a5ed88b2faa7ba6b5704b5569774b124b28f15ab4381431b811e8c76d42a6ef | yes |
| Final briefing | research/final_briefing.md | model-facing | befe1aa32232427435a399cf0e93d11b5531eb01b342bd2607a3f3af7348ca10 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
