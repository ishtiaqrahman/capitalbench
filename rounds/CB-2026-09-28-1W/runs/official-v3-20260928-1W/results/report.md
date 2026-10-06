# CapitalBench Report: CB-2026-09-28-1W / official-v3-20260928-1W

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260928-1W
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-28-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-28
- Decision deadline: 2026-09-28T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-28
- Exit date: 2026-10-05
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | ENERGY | 3 | 0.59 | Narrow leadership with SPY up while equal-weight and small/mid caps lagged; elevated yields after recent hike and dense data calendar (jobs, GDP, ISM) favor selective mean-reversion in high-quality pullbacks over pure momentum continuation in a one-week window. | September employment and ISM releases could reprice rates and risk appetite sharply; Further upside in Treasury yields pressures rate-sensitive and EM assets; Oil/commodity bounce fails if demand data disappoints or supply overhang persists; Narrow mega-cap leadership continues, leaving equal-weight and cyclicals lagging |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 2 | 0.55 | Cap-weighted SPY led by mega-cap tech while breadth deteriorated (RSP -5.5% vs SPY over 21d). Rising yields after the Fed hike pressure duration and rate-sensitives. Oil pulled back after a strong prior run. A heavy data week, including payrolls and ISM, adds event risk. Active dispersion of 1.87% is moderate. | Oil continues to slide and drags XLE; A hot payrolls or ISM print sparks a yield spike and a broad selloff; Mega-cap tech leadership widens SPY outperformance |
| openai-gpt-6-astra | openai | portfolio | ENERGY | 3 | 0.56 | Weak breadth, falling credit and duration assets, and a recent Fed hike make indiscriminate dip-buying unattractive. Inflation and expansionary manufacturing readings provide some independent support for commodity-related pullbacks, but not a strong oil-specific catalyst. The crowded release calendar makes modest, uncertain reversal edges more credible than extrapolating technology leadership. Mechanical three-session returns and five-session active returns are treated as distinct measurements. | September 30 inflation data and October 2 payrolls could push yields and the dollar higher, overwhelming reversal effects.; Weaker manufacturing or services releases could undermine commodity demand and deepen the energy pullback.; Energy and broad commodities share meaningful commodity exposure, so their qualifying edges are not independent.; Continued narrow technology leadership could leave both qualifying reversal candidates behind SPY.; Any rebound realized before the September 28 entry close is outside the scored holding window. |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | Cap-weighted US equities sit near 52-week highs after a 1.2% week while equal-weight and small/mid lagged; 5-session active-return dispersion is only 1.87% with 43% of assets positive. A fresh 25 bp hike, 10-year yield at 5.17%, and a dense labor/GDP/ISM calendar through Oct 5 favor mixed factor outcomes rather than a clean continuation or reversal week. | September 30 GDP/PCE and October 2 employment prints can reprice duration and growth in a single session.; 10-year yield at 5.17% can extend pressure on rate-sensitive sleeves (utilities, MBS) if yields rise further.; Oil/commodity mean-reversion can fail if the Brent dip below $98 persists into settlement.; High-beta tech/semis can reverse if breadth remains weak versus cap-weighted SPY. |
| xai-grok-4-3 | xai | portfolio | OIL | 3 | 0.6 | Mixed signals with commodity pullbacks offering reversal potential and tech showing supported continuation amid upcoming labor data releases. | Labor data releases could increase volatility; Commodity price swings from geopolitical factors; Rate sensitivity in defensive sectors |
| anthropic-claude-fable-5-1 | anthropic | portfolio | ENERGY | 3 | 0.5567 | SPY rose 1.27% over five sessions on narrow mega-cap tech leadership while equal-weight, small caps, bonds, gold, and defensives fell. Rates are rising (10y 5.17%, Fed hiked to 3.75-4.00% on Sep 16) with CPI 3.4% and PPI 5.4%, keeping duration and rate-sensitive assets under pressure. Oil remains in a strong medium-term uptrend (+16.5% over 21 sessions) with a modest recent pullback. The window is data-heavy (JOLTS, GDP, ISM, payrolls), so a hot print could extend the rates-up/commodities-up regime while tech breadth narrowness raises reversal risk in the leaders. | Oil pullback extends if Brent breaks below $98 on demand or supply news, dragging XLE and PDBC; Strong payrolls or ISM prints push yields higher and trigger a broad equity selloff where high-beta commodity assets underperform; Mega-cap tech leadership persists, keeping SPY ahead of negative-beta commodity exposures; Dollar strength (UUP +2.14% over 21s) continues to weigh on commodities |
| google-gemini-3-1-pro | google | portfolio | UTILITIES | 3 | 0.58 | The market is showing mixed signals with the S&P 500 up 1.2% but weaker breadth as equal-weight and small-cap indexes fell. The recent Fed rate hike to 3.75%-4.00% and upcoming economic data releases (JOLTS, GDP, ISM) suggest a cautious environment where defensive and quality assets might outperform. | Upcoming economic data (ISM, GDP, Jobs) could surprise to the upside, hurting defensive and reversal plays.; Continued weakness in market breadth could drag down all equities, including potential reversal candidates. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BRAZIL | Brazil Equities | 36.82 | 42.97999954223633 | 0.16730036779566348 | 1 |
| CYBERSECURITY | Cybersecurity | 100.95 | 106.01 | 0.05012382367508672 | 2 |
| SEMICONDUCTORS | Semiconductors | 606.56 | 633.9 | 0.04507385914006856 | 3 |
| SOFTWARE | Software | 106.01 | 109.72 | 0.034996698424676786 | 4 |
| TAIWAN | Taiwan Equities | 114.78 | 118.0 | 0.02805366788639141 | 5 |
| TECHNOLOGY | Technology Sector | 196.27 | 200.93 | 0.023742803281194158 | 6 |
| SOUTH_KOREA | South Korea Equities | 187.18 | 191.4600067138672 | 0.02286572664743658 | 7 |
| ENERGY | Energy Sector | 62.04 | 63.45 | 0.022727272727272707 | 8 |
| BITCOIN_ETF | Bitcoin ETF | 47.57 | 48.560001373291016 | 0.020811464647698452 | 9 |
| LARGE_GROWTH | US Large-Cap Growth | 126.25 | 128.35 | 0.01663366336633665 | 10 |
| NASDAQ100 | Nasdaq 100 | 744.5 | 756.2 | 0.015715245130960342 | 11 |
| MOMENTUM | US Momentum Equities | 318.5 | 323.14 | 0.014568288854003075 | 12 |
| JAPAN | Japan Equities | 97.93 | 99.3 | 0.01398958439701814 | 13 |
| BROAD_AI_TECH | Broad AI Technology | 65.97 | 66.85 | 0.013339396695467576 | 14 |
| US_DOLLAR | US Dollar | 28.62 | 28.989999771118164 | 0.01292801436471569 | 15 |
| UTILITIES | Utilities Sector | 39.51 | 39.97 | 0.011642622120981994 | 16 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.42 | 125.84 | 0.011412956116380046 | 17 |
| MID_CAP | US Mid-Cap Stocks | 72.99 | 73.68 | 0.009453349773941744 | 18 |
| BIOTECH | Biotechnology | 155.03 | 156.19 | 0.007482422756885709 | 19 |
| EMERGING_MARKETS | Emerging Markets | 60.16 | 60.61 | 0.007480053191489366 | 20 |
| ETHEREUM_ETF | Ethereum ETF | 20.31 | 20.43000030517578 | 0.005908434523672179 | 21 |
| SMALL_CAP | US Small-Cap Stocks | 281.97 | 283.38 | 0.005000531971486311 | 22 |
| SP500 | S&P 500 | 771.35 | 774.83 | 0.004511570622933947 | 23 |
| TOTAL_US_MARKET | Total US Stock Market | 379.77 | 380.6 | 0.002185533349132518 | 24 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.11 | 211.12 | 4.7368670361480625e-05 | 25 |
| AUSTRALIA | Australia Equities | 28.43 | 28.43000030517578 | 1.0734287014813049e-08 | 26 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 27 |
| MUNICIPAL_BONDS | Municipal Bonds | 101.17 | 101.12000274658203 | -0.0004941905052681106 | 28 |
| SMALL_VALUE | US Small-Cap Value | 213.49 | 213.27 | -0.0010304932315330362 | 29 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 110.56 | 110.42 | -0.0012662807525325448 | 30 |
| INDUSTRIALS | Industrials Sector | 170.43 | 170.1 | -0.0019362788241507056 | 31 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.62 | 91.44 | -0.0019646365422397727 | 32 |
| AGRICULTURE | Agriculture Commodities | 28.54 | 28.459999084472656 | -0.0028031154704745154 | 33 |
| LOW_VOL | US Low Volatility Equities | 71.3 | 71.09 | -0.0029453015427769458 | 34 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.94 | 46.790000915527344 | -0.003195549307044132 | 35 |
| YEN | Japanese Yen | 58.3 | 58.02000045776367 | -0.004802736573521926 | 36 |
| METALS_MINING | Metals and Mining | 108.33 | 107.76 | -0.005261700360011057 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 104.54 | 103.98 | -0.0053568012244117336 | 38 |
| MATERIALS | Materials Sector | 49.8 | 49.5 | -0.0060240963855421326 | 39 |
| LARGE_VALUE | US Large-Cap Value | 251.93 | 250.36 | -0.006231889810661695 | 40 |
| CHINA | China Equities | 52.62 | 52.28 | -0.006461421512732768 | 41 |
| SOLAR | Solar Energy | 44.06 | 43.67 | -0.008851566046300552 | 42 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.84 | 71.13 | -0.0098830734966594 | 43 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.12 | 94.13 | -0.01040790580319606 | 44 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 77.86 | 76.98 | -0.011302337528897977 | 45 |
| COMMUNICATIONS | Communication Services Sector | 112.96 | 111.61 | -0.011951133144475823 | 46 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 90.0 | 88.92 | -0.01200000000000001 | 47 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.06 | 81.04 | -0.012429929320009747 | 48 |
| BROAD_COMMODITIES | Broad Commodities | 19.5 | 19.25 | -0.012820512820512775 | 49 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 103.21 | 101.83 | -0.013370797403352341 | 50 |
| CANADA | Canada Equities | 59.59 | 58.78 | -0.013592884712200104 | 51 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 90.34 | 89.08999633789062 | -0.013836657760785687 | 52 |
| DIVIDEND | US Dividend Equities | 33.21 | 32.72 | -0.01475459199036444 | 53 |
| EURO | Euro | 105.15 | 103.58999633789062 | -0.014835983472271774 | 54 |
| REGIONAL_BANKS | Regional Banks | 71.55 | 70.39 | -0.016212438853948186 | 55 |
| FINANCIALS | Financials Sector | 54.84 | 53.88 | -0.01750547045951867 | 56 |
| COPPER | Copper | 40.61 | 39.86000061035156 | -0.018468342517814262 | 57 |
| HEALTHCARE | Healthcare Sector | 170.7 | 167.37 | -0.019507908611599234 | 58 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 92.18 | 90.33999633789062 | -0.019960985703074252 | 59 |
| MEXICO | Mexico Equities | 73.34 | 71.87000274658203 | -0.02004359494706809 | 60 |
| REAL_ESTATE | Real Estate Sector | 41.56 | 40.67 | -0.021414821944177098 | 61 |
| UNITED_KINGDOM | United Kingdom Equities | 47.32 | 46.19 | -0.02387996618765853 | 62 |
| EUROPE | Europe Equities | 88.63 | 86.28 | -0.026514724134040324 | 63 |
| INDIA | India Equities | 47.86 | 46.57 | -0.026953614709569584 | 64 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 79.32 | 77.11 | -0.027861825516893535 | 65 |
| OIL | Crude Oil | 148.33 | 143.99000549316406 | -0.029259047440409525 | 66 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 213.81 | 206.98 | -0.03194424956737296 | 67 |
| GOLD | Gold | 80.66 | 77.82 | -0.03520952144805356 | 68 |
| SOUTH_AFRICA | South Africa Equities | 66.48 | 63.16999816894531 | -0.0497894378919177 | 69 |
| SILVER | Silver | 58.14 | 55.130001068115234 | -0.0517715674558783 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | ENERGY | 35.0 | 0.022727272727272707 | 0.007954545454545447 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | OIL | 35.0 | -0.029259047440409525 | -0.010240666604143333 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | BROAD_COMMODITIES | 30.0 | -0.012820512820512775 | -0.0038461538461538325 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | ENERGY | 35.0 | 0.022727272727272707 | 0.007954545454545447 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 65.0 | 0.004511570622933947 | 0.0029325209049070656 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | UTILITIES | 35.0 | 0.011642622120981994 | 0.004074917742343698 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SILVER | 35.0 | -0.0517715674558783 | -0.018120048609557404 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOLAR | 30.0 | -0.008851566046300552 | -0.0026554698138901655 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | ENERGY | 35.0 | 0.022727272727272707 | 0.007954545454545447 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | BROAD_COMMODITIES | 35.0 | -0.012820512820512775 | -0.004487179487179471 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | 0.004511570622933947 | 0.001353471186880184 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | OIL | 35.0 | -0.029259047440409525 | -0.010240666604143333 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | ENERGY | 35.0 | 0.022727272727272707 | 0.007954545454545447 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 30.0 | 0.004511570622933947 | 0.001353471186880184 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | ENERGY | 35.0 | 0.022727272727272707 | 0.007954545454545447 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | OIL | 35.0 | -0.029259047440409525 | -0.010240666604143333 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | BRAZIL | 30.0 | 0.16730036779566348 | 0.050190110338699044 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.004511570622933947 | 0.004511570622933947 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | ENERGY | 3 | 0.59 | 0.022727272727272707 | 0.04790398918910116 | 0.04339241856616721 | 0.11939637860656233 |  | True | True |
| anthropic-claude-opus-5-5 | SP500 | 2 | 0.55 | 0.004511570622933947 | 0.010887066359452512 | 0.006375495736518565 | 0.15641330143621096 |  | True | True |
| openai-gpt-6-astra | ENERGY | 3 | 0.56 | 0.022727272727272707 | 0.00482083715424616 | 0.00030926653131221286 | 0.16247953064141732 |  | True | True |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.004511570622933947 | 0.004511570622933947 | 0.0 | 0.16278879717272954 |  | False | True |
| xai-grok-4-3 | OIL | 3 | 0.6 | -0.029259047440409525 | -0.0009326499627177025 | -0.005444220585651649 | 0.16823301775838118 |  | False | False |
| anthropic-claude-fable-5-1 | ENERGY | 3 | 0.5567 | 0.022727272727272707 | -0.006132274995751719 | -0.010643845618685666 | 0.1734326427914152 |  | False | False |
| google-gemini-3-1-pro | UTILITIES | 3 | 0.58 | 0.011642622120981994 | -0.01670060068110387 | -0.021212171304037818 | 0.18400096847676736 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 500e12d10bc1830688f05c252973afaeb17a8afd26692e3dec0c0c41079f12e9 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | afd177a8126f3edcf107990cf171e414ac8a6ad192b5732250ae2e8786a76111 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | d5995651400a1f8bf4a65ebda65a98b6b3ad34861c366fbaf8c9823c6aa7fb8d |
| market_data/universe_decision_context.md | ce77abd37f189a32ff26dd51fcb405593c082307abb4587d818b3b064c7f92b0 |
| market_data/universe_decision_context.json | cafe2df004f3ee711c62ce3d2f339f8b3a1c48c54db2af09d1dc090dc172bd76 |
| market_data/decision_context_source_history.json | 6c65083ea80e2aa06edd9178418f6908ccef900edd8198da0d80fcbd8f243f6c |
| market_data/universe_quality_evidence.md | 0656f60d50080ae8850d9a2ed48c16d8e66daa13dc92bcd152e318e98b3b5bbf |
| market_data/universe_quality_evidence.json | d69c631c9bc8162ccdcdf8e370d009fa468ceaeca2c1e6bb425331dc1eae4947 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 52d42df8e1fc8774d10cbbbf79b36966846384551aba684e84f82aebfca0da58 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 84b7adca0829ffc8209688ac1dc8ab506a5dcba8543547436734005ec1ab1457 | yes |
| Final briefing | research/final_briefing.md | model-facing | 500e12d10bc1830688f05c252973afaeb17a8afd26692e3dec0c0c41079f12e9 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
