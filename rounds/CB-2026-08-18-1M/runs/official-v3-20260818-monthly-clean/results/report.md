# CapitalBench Report: CB-2026-08-18-1M / official-v3-20260818-monthly-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260818-monthly-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-18-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-18
- Decision deadline: 2026-08-18T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-18
- Exit date: 2026-09-18
- Entry rule: Use the Tuesday, August 18, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Friday, September 18, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 1 | 0.5 | Macro is soft-landing-with-friction: weak payrolls (-23k, downward revisions), cooling core PCE 3.3% but sticky, hawkish Fed dividing 9-3, and consumer sentiment falling to 51.0. SPY up 13% YTD near highs. Dispersion is high with tech/semis, precious metals momentum, and defensive rate-sensitives all diverging. No compelling single-name overreaction warrants overriding SPY; edges are thin and mostly no_edge, so SPY default is preferred. | September FOMC (Sep 16) surprises with hawkish hold given 9-3 split and sticky core inflation; High-beta semis/oil could see sharp drawdowns given very high volatility if growth data weakens further; Consumer sentiment falling to 51.0 and negative payrolls raise recession/risk-off tail |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is within 1% of its 52-week high after a modest 21-session gain while inflation is still above target, the FOMC is on hold with three dissenters preferring a hike, and September FOMC/CPI land inside the scoring window. Cross-section is mixed: energy and semis retain medium-horizon strength, several rate-sensitive and EM names show deep active drawdowns, and equal-weight versus cap-weight is not decisive. | September 16 FOMC statement, SEP, and press conference can reprice duration, growth, and high-beta tech inside the exit window.; August CPI/PPI and the September 4 employment report can reverse the recent disinflation/soft-labor narrative.; Oil and semiconductor 50%+ horizon volatility can dominate one-month excess even if the directional thesis is right.; China PMI contraction and euro-area energy-price uncertainty can hit EM, metals, and cyclical risk assets. |
| xai-grok-4-3 | xai | portfolio | LONG_TREASURY | 3 | 0.6 | July employment decline, downward revisions, and weak consumer sentiment point to growth slowdown favoring rate-sensitive reversals over growth continuation. | Further labor market deterioration; FOMC policy response; Commodity price volatility; Equity valuation compression |
| xai-grok-4-5 | xai | portfolio | REGIONAL_BANKS | 3 | 0.5633 | Soft July payrolls, sticky but cooling CPI/PCE mix, and held funds rate leave a one-month window of modest equity drift with selective mean-reversion in rate-sensitive and EM laggards; oil strength and high ISM prices keep cyclical/commodity dispersion elevated versus pure growth continuation. | September FOMC and August CPI/PPI could reprice rates higher and reverse TLT/financials bounce; Sticky services inflation and ISM prices >70 keep real-rate pressure on duration and rate-sensitive equities; Oil near $91 and energy volatility can rotate risk away from banks and into commodities; Payroll revisions and weak retail sales raise recession-scare risk that hits small/regional banks harder than SPY |
| anthropic-claude-opus-5 | anthropic | portfolio | REGIONAL_BANKS | 3 | 0.57 | Late-cycle mix: inflation still above target (core PCE 3.3%, PPI 4.7%), FOMC on hold with three hawkish dissents, but labor data deteriorating (payrolls -23k, downward revisions, sentiment 51.0). Equity breadth positive (72% of assets up over 21 sessions) yet leadership is narrow and concentrated in semis, Korea/Taiwan, metals and oil. Long duration has been punished as the long end steepened (20y 5.30%, 30y 5.31%), so bond reversal is not clearly supported. With a September FOMC and August CPI inside the window, and dispersion high, most single-sleeve bets carry wide ranges relative to SPY. Highest-quality relative-pullback candidates are financials/regional banks, where prior trend is positive, volatility and drawdown low, and recent underperformance looks like rotation rather than deterioration. | September 16 FOMC and August CPI on September 11 could shift rate expectations sharply against financials and small caps; Continued payroll deterioration and 51.0 consumer sentiment could trigger a credit-quality repricing in regional banks; Narrow mega-cap/semiconductor leadership could extend, causing SPY to outrun value-tilted sleeves; Long-end yields above 5.3% could pressure bank securities portfolios and rate-sensitive equity; Brent volatility ($72-$102 July range) can drive fast cross-asset factor rotations before the September 18 exit |
| openai-gpt-5-6-sol | openai | portfolio | LONG_TREASURY | 3 | 0.57 | Cooling inflation and weakening labor and retail data favor selective reversals in duration and defensives, but elevated producer inflation, a divided Fed, and strong activity surveys limit conviction. Extreme commodity and thematic moves face substantial reversal risk. | August inflation data or the September FOMC could reinforce higher-for-longer rates and hurt duration-sensitive selections.; Strong activity data or an upside GDP revision could reverse the bond rally thesis and favor high-beta cyclicals.; Further labor and consumer deterioration could widen bank credit concerns despite regional banks' quality signal.; Oil or geopolitical shocks could revive inflation and cause commodity momentum to outperform reversal candidates. |
| google-gemini-3-1-pro | google | portfolio | UTILITIES | 3 | 0.58 | The market is digesting mixed economic signals, with inflation moderating but labor market softening. The Fed held rates steady but acknowledged elevated inflation. This environment favors a balanced approach, with potential for defensive sectors and select growth areas to outperform. | Inflation could re-accelerate, negatively impacting long-duration assets like Long-Term Treasuries and Utilities.; A sharper-than-expected economic slowdown could hurt Regional Banks despite their recent pullback. |
| anthropic-claude-fable-5 | anthropic | portfolio | REGIONAL_BANKS | 3 | 0.5633 | Macro data show softening labor (payrolls -23k, downward revisions) and weak retail sales alongside moderating CPI (0.1% m/m), raising odds the September 16 FOMC tilts dovish. Cross-sectional dispersion is elevated, with rate-sensitive and quality pullback names offering the cleanest reversal setups; high-vol momentum names (semis, Korea, oil) carry large give-back risk. | Sticky inflation (CPI 3.4%, PPI 4.7%) leads to a hawkish September FOMC, hurting rate-sensitive picks; Labor deterioration accelerates into a credit-quality concern, hitting regional banks and financials; August CPI/payrolls surprises within the window drive sharp rate volatility; Continued mega-cap tech leadership makes SPY hard to beat with value/defensive tilts |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.44 | 19.920000076293945 | 0.37950139032506547 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 36.6 | 46.02000045776367 | 0.25737706168753194 | 2 |
| OIL | Crude Oil | 130.66000366210938 | 153.82000732421875 | 0.17725396458737164 | 3 |
| BRAZIL | Brazil Equities | 33.70000076293945 | 37.52 | 0.11335309052163223 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 18.2 | 19.66 | 0.08021978021978038 | 5 |
| TAIWAN | Taiwan Equities | 104.39 | 111.64 | 0.06945109684835704 | 6 |
| SOUTH_KOREA | South Korea Equities | 170.05 | 181.31 | 0.06621581887680095 | 7 |
| SILVER | Silver | 57.44 | 59.93000030517578 | 0.043349587485650876 | 8 |
| COPPER | Copper | 39.18 | 40.22999954223633 | 0.02679937575896707 | 9 |
| BROAD_AI_TECH | Broad AI Technology | 62.529998779296875 | 64.13 | 0.02558773791681035 | 10 |
| CYBERSECURITY | Cybersecurity | 97.44 | 99.87 | 0.024938423645320285 | 11 |
| SOFTWARE | Software | 101.95999908447266 | 104.35 | 0.02344057411718148 | 12 |
| TECHNOLOGY | Technology Sector | 185.6199951171875 | 189.6 | 0.021441681863528794 | 13 |
| SOUTH_AFRICA | South Africa Equities | 67.1 | 68.49 | 0.02071535022354687 | 14 |
| YEN | Japanese Yen | 57.48 | 58.47999954223633 | 0.017397347638071103 | 15 |
| JAPAN | Japan Equities | 95.37000274658203 | 97.0 | 0.017091299218572997 | 16 |
| ENERGY | Energy Sector | 63.68000030517578 | 64.31 | 0.00989321124065734 | 17 |
| US_DOLLAR | US Dollar | 28.14 | 28.389999389648438 | 0.008884128985374495 | 18 |
| GOLD | Gold | 81.70999908447266 | 82.23 | 0.006363981414193365 | 19 |
| EMERGING_MARKETS | Emerging Markets | 59.63999938964844 | 60.01 | 0.006203900304126764 | 20 |
| SEMICONDUCTORS | Semiconductors | 569.77 | 573.0 | 0.005668954139389504 | 21 |
| NASDAQ100 | Nasdaq 100 | 717.510009765625 | 721.45 | 0.005491198980850598 | 22 |
| AGRICULTURE | Agriculture Commodities | 28.030000686645508 | 28.149999618530273 | 0.004281089152521345 | 23 |
| COMMUNICATIONS | Communication Services Sector | 110.4800033569336 | 110.81 | 0.002986935490943754 | 24 |
| LARGE_GROWTH | US Large-Cap Growth | 123.07 | 123.25 | 0.0014625822702527547 | 25 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 26 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.56 | 91.55 | -0.00010921799912633201 | 27 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.66 | 81.25 | -0.005020818025961216 | 28 |
| MOMENTUM | US Momentum Equities | 311.80999755859375 | 309.62 | -0.007023500130659555 | 29 |
| SP500 | S&P 500 | 767.45 | 761.69 | -0.007505374942992971 | 30 |
| HEALTHCARE | Healthcare Sector | 169.73 | 168.39 | -0.007894891887114897 | 31 |
| EURO | Euro | 106.84 | 105.98999786376953 | -0.00795584178426123 | 32 |
| TOTAL_US_MARKET | Total US Stock Market | 379.04 | 375.43 | -0.009524060785141453 | 33 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.83999633789062 | 104.7 | -0.010770940828939812 | 34 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.59 | 47.04999923706055 | -0.01134693765369732 | 35 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.53 | 78.53 | -0.012573871495033306 | 36 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.64 | 93.37999725341797 | -0.013313638488821167 | 37 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.38999938964844 | 71.38 | -0.013952195029205527 | 38 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.35 | 95.96 | -0.01427837699024137 | 39 |
| MEXICO | Mexico Equities | 74.46 | 73.34 | -0.015041633091592677 | 40 |
| TIPS | Treasury Inflation-Protected Securities | 107.0199966430664 | 105.27 | -0.01635205286824115 | 41 |
| UNITED_KINGDOM | United Kingdom Equities | 48.16 | 47.27 | -0.01848006644518263 | 42 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.08 | 91.29 | -0.019230769230769162 | 43 |
| LARGE_VALUE | US Large-Cap Value | 256.7300109863281 | 251.7 | -0.019592610022503343 | 44 |
| BIOTECH | Biotechnology | 160.11 | 156.72 | -0.021172943601274197 | 45 |
| CANADA | Canada Equities | 61.58 | 60.22 | -0.022085092562520336 | 46 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.93 | 90.8 | -0.022920477778973547 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.37000274658203 | 102.88 | -0.023631039970365864 | 48 |
| DIVIDEND | US Dividend Equities | 34.51 | 33.68 | -0.024050999710228838 | 49 |
| INDIA | India Equities | 49.38 | 48.02 | -0.027541514783313015 | 50 |
| AUSTRALIA | Australia Equities | 29.610000610351562 | 28.75 | -0.02904426182453068 | 51 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.58 | 82.8 | -0.03248422528628181 | 52 |
| CHINA | China Equities | 54.9 | 53.07 | -0.033333333333333326 | 53 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 219.7899932861328 | 212.29 | -0.034123452000696775 | 54 |
| FINANCIALS | Financials Sector | 57.84000015258789 | 55.86 | -0.03423236769302296 | 55 |
| MATERIALS | Materials Sector | 51.779998779296875 | 49.99 | -0.034569309028500084 | 56 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 126.80000305175781 | 122.2 | -0.0362776257180385 | 57 |
| EUROPE | Europe Equities | 91.55000305175781 | 88.21 | -0.036482828404380774 | 58 |
| SMALL_VALUE | US Small-Cap Value | 224.45 | 215.58 | -0.03951882379149019 | 59 |
| METALS_MINING | Metals and Mining | 113.63 | 108.68 | -0.04356243949661176 | 60 |
| LOW_VOL | US Low Volatility Equities | 76.03 | 72.58 | -0.04537682493752471 | 61 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.36 | 111.03 | -0.04580611894121689 | 62 |
| REAL_ESTATE | Real Estate Sector | 44.630001068115234 | 42.53 | -0.047053574229365736 | 63 |
| REGIONAL_BANKS | Regional Banks | 76.85 | 72.75 | -0.053350683148991496 | 64 |
| SMALL_CAP | US Small-Cap Stocks | 300.23 | 284.1 | -0.053725477134197064 | 65 |
| MID_CAP | US Mid-Cap Stocks | 77.23999786376953 | 72.98 | -0.055152744453502045 | 66 |
| UTILITIES | Utilities Sector | 44.02 | 41.1 | -0.06633348477964562 | 67 |
| INDUSTRIALS | Industrials Sector | 183.57 | 169.75 | -0.07528463256523399 | 68 |
| SOLAR | Solar Energy | 49.87 | 45.66 | -0.08441949067575694 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 252.16 | 213.84 | -0.15196700507614214 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | REGIONAL_BANKS | 35.0 | -0.053350683148991496 | -0.01867273910214702 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | FINANCIALS | 35.0 | -0.03423236769302296 | -0.011981328692558035 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | UTILITIES | 30.0 | -0.06633348477964562 | -0.019900045433893686 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-4-8 | SP500 | 100.0 | -0.007505374942992971 | -0.007505374942992971 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 35.0 | -0.053350683148991496 | -0.01867273910214702 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | FINANCIALS | 35.0 | -0.03423236769302296 | -0.011981328692558035 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 30.0 | -0.007505374942992971 | -0.002251612482897891 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | UTILITIES | 35.0 | -0.06633348477964562 | -0.023216719672875967 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | LONG_TREASURY | 35.0 | -0.005020818025961216 | -0.0017572863090864253 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 30.0 | -0.053350683148991496 | -0.016005204944697447 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | LONG_TREASURY | 35.0 | -0.005020818025961216 | -0.0017572863090864253 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 35.0 | -0.053350683148991496 | -0.01867273910214702 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | UTILITIES | 30.0 | -0.06633348477964562 | -0.019900045433893686 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | LONG_TREASURY | 35.0 | -0.005020818025961216 | -0.0017572863090864253 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | UTILITIES | 35.0 | -0.06633348477964562 | -0.023216719672875967 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 30.0 | -0.007505374942992971 | -0.002251612482897891 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | REGIONAL_BANKS | 35.0 | -0.053350683148991496 | -0.01867273910214702 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | LONG_TREASURY | 35.0 | -0.005020818025961216 | -0.0017572863090864253 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-5 | FINANCIALS | 30.0 | -0.03423236769302296 | -0.010269710307906887 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | -0.007505374942992971 | -0.007505374942992971 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SP500 | 1 | 0.5 | -0.007505374942992971 | -0.007505374942992971 | 0.0 | 0.38700676526805844 |  | False | False |
| xai-grok-4-6 | SP500 | 1 | 0.5 | -0.007505374942992971 | -0.007505374942992971 | 0.0 | 0.38700676526805844 |  | False | False |
| xai-grok-4-3 | LONG_TREASURY | 3 | 0.6 | -0.005020818025961216 | -0.027225618464860286 | -0.019720243521867315 | 0.40672700878992574 |  | False | False |
| xai-grok-4-5 | REGIONAL_BANKS | 3 | 0.5633 | -0.053350683148991496 | -0.030699735719140336 | -0.023194360776147366 | 0.4102011260442058 |  | False | False |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 3 | 0.57 | -0.053350683148991496 | -0.03290568027760295 | -0.025400305334609977 | 0.4124070706026684 |  | False | False |
| openai-gpt-5-6-sol | LONG_TREASURY | 3 | 0.57 | -0.005020818025961216 | -0.04033007084512713 | -0.03282469590213416 | 0.4198314611701926 |  | False | False |
| google-gemini-3-1-pro | UTILITIES | 3 | 0.58 | -0.06633348477964562 | -0.04097921092665984 | -0.03347383598366687 | 0.4204806012517253 |  | False | False |
| anthropic-claude-fable-5 | REGIONAL_BANKS | 3 | 0.5633 | -0.053350683148991496 | -0.05055411322859874 | -0.04304873828560577 | 0.43005550355366423 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 4edaec8125fd868a585c3e4ab4b55a21329c158c817874b629b01f774a82ef11 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 225b669bc866adfff14184f30e015eb38168c0364246ca396bf09c3ea3c786bc |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 248a3672444d2268da726eb036f70e6ac38851f02732bb43f418157fcba5ab0c |
| market_data/universe_decision_context.md | 27d0479a4a6cbb6103af6d6c1a06b150c8a42e2dd04f96572f818d58e478da12 |
| market_data/universe_decision_context.json | c7e2e7a71df8620e6db80a8a7d37f28c02d923c69f6ce0f72f6b878ddad43eab |
| market_data/decision_context_source_history.json | e63ed76c87773237b316607a84bc46ac67471f9837aeccfe0f22a33a388edd1f |
| market_data/universe_quality_evidence.md | a4d8f53178aee2dac55da5885b00caa23f9b25a355d8a489b1e8bdcec3670a22 |
| market_data/universe_quality_evidence.json | 19861164c66dabdf0eb2c68cbabbfdfec585caad2504bab405b3db9caf21e917 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 6788836986cb7b98745a9e08bae1a791f604743898fcc2aa46b2e713c7b121a3 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 5de76b6c7e4253d05aa56f7e0deff657907b7bcdd05d446ec22d16d4cbde86ad | yes |
| Final briefing | research/final_briefing.md | model-facing | 4edaec8125fd868a585c3e4ab4b55a21329c158c817874b629b01f774a82ef11 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
