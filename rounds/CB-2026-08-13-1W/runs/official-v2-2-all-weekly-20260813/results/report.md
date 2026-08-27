# CapitalBench Report: CB-2026-08-13-1W / official-v2-2-all-weekly-20260813

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260813
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-13-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-13
- Decision deadline: 2026-08-13T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-13
- Exit date: 2026-08-20
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | ENERGY | 2 | 0.65 | A balanced approach utilizing energy momentum and healthcare defensiveness. | A sudden drop in oil prices could negatively impact the energy allocation.; A rapid shift in market sentiment towards high-growth sectors could lead to underperformance of healthcare.; Broader market volatility could affect both sectors. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | SPY base is modest near highs after a soft labor print and mixed inflation. Higher-base active holdings in energy, healthcare, gold, and copper are favored for one-week alpha with diversified economic exposures. | Geopolitical de-escalation could reverse energy and commodity gains; Hotter-than-expected PPI or retail sales could lift yields and pressure gold; Broad equity risk-off could compress active returns across cyclical holdings; FOMC minutes could reprice rate path and rotate leadership back to mega-cap growth |
| anthropic-claude-fable-5 | anthropic | portfolio | GOLD | 4 | 0.58 | Overweight healthcare, dividend/value equity, equal-weight breadth, and gold against SPY given broadening market leadership, weak labor data, elevated inflation, and Iran-related uncertainty. | A dovish read of FOMC minutes could reignite mega-cap growth leadership, hurting equal-weight and defensive tilts; Hot PPI or retail sales could push real yields and the dollar higher, pressuring gold; Geopolitical de-escalation could unwind safe-haven gold gains quickly |
| xai-grok-4-3 | xai | portfolio | LARGE_VALUE | 3 | 0.62 | Value, healthcare, and gold allocations target relative strength and defensive characteristics amid softening labor data. | Unexpectedly strong retail sales data lifting growth-sensitive equities; Resolution of Iran-related crude uncertainty reducing safe-haven flows; FOMC minutes on August 19 signaling less dovish stance than expected |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 3 | 0.55 | Healthcare and gold both show strong recent active returns with low SPY correlation, providing diversification while SPY anchors the core. | Hot PPI/CPI or retail sales sparking risk-on growth rally that leaves defensives behind; Gold pullback on USD strength or rising real yields; FOMC minutes signaling hawkish tilt hurting rate-sensitive positioning |
| openai-gpt-5-6-sol | openai | portfolio | HEALTHCARE | 4 | 0.59 | A mixed growth and inflation backdrop near an equity-market high favors selective relative-strength exposures rather than concentrated benchmark risk. The weighted base forecast is 0.49%, implying 0.34 percentage point of expected alpha. | Strong retail sales or hawkish FOMC minutes could lift yields and pressure software and gold.; A broad risk-on rally led by mega-cap equities could cause defensive dividend and healthcare holdings to lag SPY.; Recent strength in healthcare and gold could reverse through short-horizon profit taking.; Geopolitical de-escalation involving Iran could reduce safe-haven demand for gold. |
| xai-grok-4-6 | xai | portfolio | HEALTHCARE | 5 | 0.54 | SPY is treated as a modest positive but not the best weekly vehicle after an all-time high and a data-heavy week. Selected sleeves combine recent relative strength, quality ranks, and identifiable catalysts that can move prices before the August 20 close. | A hot PPI or retail print could extend the August 7 SPY high and leave cyclicals/gold lagging; Energy’s large 5-session gain can mean-revert if Iran-flow headlines fade; High-beta Japan and gold can reverse together if the dollar strengthens after FOMC minutes; Payroll revisions and 4.1% unemployment leave downside if growth data disappoints all risk assets |
| anthropic-claude-opus-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.53 | SPY base +0.35% for the week; portfolio tilts to higher quality-evidence, lower-volatility exposures with independent macro support rather than chasing the oil and semis spikes. | Mega-cap tech leadership resumes, causing cap-weighted SPY to outrun defensives; Hot July PPI on Aug 13 lifts yields and hurts gold and rate-sensitive equities; Hawkish FOMC minutes Aug 19 triggers a broad risk-off move; Dollar strength drags Europe and gold returns |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.23 | 17.55 | 0.23330990864371048 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 35.88 | 41.2 | 0.1482720178372352 | 2 |
| OIL | Crude Oil | 125.03 | 134.54 | 0.07606174518115649 | 3 |
| SILVER | Silver | 58.16 | 61.66 | 0.06017881705639616 | 4 |
| SOUTH_AFRICA | South Africa Equities | 67.33 | 70.47 | 0.04663597207782555 | 5 |
| ENERGY | Energy Sector | 61.06 | 63.75 | 0.04405502784146731 | 6 |
| BROAD_COMMODITIES | Broad Commodities | 17.77 | 18.55 | 0.043894203714125 | 7 |
| BIOTECH | Biotechnology | 156.86 | 163.38 | 0.04156572740022946 | 8 |
| GOLD | Gold | 81.78 | 85.13 | 0.04096356077280494 | 9 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 28.38 | 0.027516292541636345 | 10 |
| HEALTHCARE | Healthcare Sector | 168.38 | 172.39 | 0.02381517995011273 | 11 |
| CHINA | China Equities | 54.42 | 55.51 | 0.020029400955531074 | 12 |
| EURO | Euro | 106.3994 | 107.8 | 0.01316360806545891 | 13 |
| DIVIDEND | US Dividend Equities | 34.43 | 34.83 | 0.011617775196050006 | 14 |
| BRAZIL | Brazil Equities | 33.77 | 34.14 | 0.010956470239857685 | 15 |
| UNITED_KINGDOM | United Kingdom Equities | 48.26 | 48.54 | 0.0058019063406549165 | 16 |
| TIPS | Treasury Inflation-Protected Securities | 107.16 | 107.52 | 0.0033594624860022737 | 17 |
| YEN | Japanese Yen | 57.53 | 57.66 | 0.002259690596210673 | 18 |
| MATERIALS | Materials Sector | 52.31 | 52.42 | 0.0021028484037468598 | 19 |
| MEXICO | Mexico Equities | 75.45 | 75.5 | 0.000662690523525411 | 20 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.51 | 91.57 | 0.0006556660474263953 | 21 |
| AUSTRALIA | Australia Equities | 29.74 | 29.75 | 0.00033624747814386957 | 22 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 23 |
| REAL_ESTATE | Real Estate Sector | 45.12 | 45.08 | -0.0008865248226950229 | 24 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.49 | 93.3 | -0.002032302920098372 | 25 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.69 | 97.49 | -0.002047292455727323 | 26 |
| SOUTH_KOREA | South Korea Equities | 178.62 | 178.16 | -0.0025752995185309713 | 27 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.79 | 79.56 | -0.0028825667376864983 | 28 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.59 | 82.34 | -0.003027000847560246 | 29 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.3 | 93.0 | -0.003215434083601254 | 30 |
| EUROPE | Europe Equities | 92.38 | 92.01 | -0.004005195929854821 | 31 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.55 | 106.06 | -0.0045987799155325915 | 32 |
| METALS_MINING | Metals and Mining | 115.27 | 114.7 | -0.004944911945866215 | 33 |
| EMERGING_MARKETS | Emerging Markets | 60.34 | 60.02 | -0.00530328140536962 | 34 |
| CANADA | Canada Equities | 62.1 | 61.77 | -0.005314009661835706 | 35 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.91 | 47.65 | -0.005426841995407994 | 36 |
| UTILITIES | Utilities Sector | 44.04 | 43.77 | -0.006130790190735591 | 37 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.16 | 105.47 | -0.006499623210248662 | 38 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.36 | 94.67 | -0.007235738255033541 | 39 |
| LOW_VOL | US Low Volatility Equities | 76.23 | 75.66 | -0.00747737111373481 | 40 |
| CONSUMER_STAPLES | Consumer Staples Sector | 86.0 | 85.32 | -0.007906976744186167 | 41 |
| INDIA | India Equities | 49.98 | 49.55 | -0.008603441376550669 | 42 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.54 | 72.84 | -0.009518629317378346 | 43 |
| US_DOLLAR | US Dollar | 28.18 | 27.91 | -0.009581263307310128 | 44 |
| LARGE_VALUE | US Large-Cap Value | 258.7 | 256.17 | -0.00977966756861215 | 45 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 222.73 | 220.28 | -0.010999865307771639 | 46 |
| COPPER | Copper | 39.85 | 39.35 | -0.012547051442910906 | 47 |
| SMALL_VALUE | US Small-Cap Value | 226.77 | 223.81 | -0.01305287295497648 | 48 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.45 | 116.68 | -0.01494301392992825 | 49 |
| COMMUNICATIONS | Communication Services Sector | 112.55 | 110.68 | -0.01661483784984441 | 50 |
| SMALL_CAP | US Small-Cap Stocks | 303.5 | 297.67 | -0.0192092257001647 | 51 |
| SP500 | S&P 500 | 777.88 | 762.6 | -0.01964313261685602 | 52 |
| TOTAL_US_MARKET | Total US Stock Market | 384.3 | 376.58 | -0.020088472547489022 | 53 |
| FINANCIALS | Financials Sector | 58.26 | 56.95 | -0.02248541023000339 | 54 |
| BROAD_AI_TECH | Broad AI Technology | 64.62 | 63.03 | -0.02460538532961931 | 55 |
| MID_CAP | US Mid-Cap Stocks | 78.42 | 76.37 | -0.02614129048712055 | 56 |
| NASDAQ100 | Nasdaq 100 | 732.07 | 710.93 | -0.028877019957108008 | 57 |
| LARGE_GROWTH | US Large-Cap Growth | 125.66 | 121.82 | -0.030558650326277248 | 58 |
| TAIWAN | Taiwan Equities | 107.5 | 104.07 | -0.03190697674418608 | 59 |
| INDUSTRIALS | Industrials Sector | 185.79 | 179.77 | -0.03240217449808913 | 60 |
| MOMENTUM | US Momentum Equities | 316.03 | 305.11 | -0.03455368161250505 | 61 |
| REGIONAL_BANKS | Regional Banks | 77.75 | 74.71 | -0.03909967845659168 | 62 |
| TECHNOLOGY | Technology Sector | 190.77 | 183.1 | -0.04020548304240712 | 63 |
| SOFTWARE | Software | 106.28 | 101.91 | -0.04111780203236737 | 64 |
| JAPAN | Japan Equities | 98.47 | 94.27 | -0.04265258454351584 | 65 |
| SEMICONDUCTORS | Semiconductors | 589.12 | 562.65 | -0.04493142313959808 | 66 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 249.69 | 237.56 | -0.04858023949697621 | 67 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.1 | 123.68 | -0.049346656418139845 | 68 |
| SOLAR | Solar Energy | 52.47 | 49.73 | -0.05222031637125979 | 69 |
| CYBERSECURITY | Cybersecurity | 102.2 | 93.45 | -0.08561643835616439 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | GOLD | 25.0 | 0.04096356077280494 | 0.010240890193201235 | Strong prior and recent relative trend, elevated inflation (CPI 3.4%, energy +14.7% y/y) and Iran-related uncertainty support safe-haven demand. |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | 0.02381517995011273 | 0.005953794987528183 | Positive recent and prior active returns, low SPY beta (-0.22), at 52-week high, defensive earnings in a slowing labor market. |
| anthropic-claude-fable-5 | DIVIDEND | 25.0 | 0.011617775196050006 | 0.0029044437990125016 | Best combined prior (+2.08%) and recent (+1.49%) active return among diversified equity; near 52-week high with low volatility. |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 25.0 | -0.010999865307771639 | -0.0027499663269429098 | Market breadth improving: RSP beat SPY by 0.26% over 5 sessions and 0.83% over 21; positive asset share 72% over 21 sessions. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 35.0 | 0.02381517995011273 | 0.008335312982539455 | Strong recent active return (+2.26% 5s), low SPY beta/correlation, defensive quality with high prior rank. |
| anthropic-claude-opus-4-8 | GOLD | 30.0 | 0.04096356077280494 | 0.012289068231841482 | Strong momentum (+3.57% active 5s, +8.8% 21s IAU), safe-haven demand amid soft labor data and geopolitical crude uncertainty. |
| anthropic-claude-opus-4-8 | SP500 | 35.0 | -0.01964313261685602 | -0.006875096415899606 | Core benchmark exposure at all-time high area with positive breadth. |
| anthropic-claude-opus-5 | HEALTHCARE | 25.0 | 0.02381517995011273 | 0.005953794987528183 | Defensive sector with positive prior active trend, low beta and at 52-week high; diversifies from mega-cap tech risk. |
| anthropic-claude-opus-5 | FINANCIALS | 25.0 | -0.02248541023000339 | -0.005621352557500847 | High quality-evidence score, low volatility, steady positive prior active return, supported by solid PMI and steep curve. |
| anthropic-claude-opus-5 | EUROPE | 20.0 | -0.004005195929854821 | -0.0008010391859709642 | Strong prior relative trend with low volatility and minimal drawdown; diversifies US mega-cap concentration. |
| anthropic-claude-opus-5 | GOLD | 15.0 | 0.04096356077280494 | 0.006144534115920741 | Strong prior active trend with sticky 3.4% headline CPI and negative payrolls supporting safe-haven demand. |
| anthropic-claude-opus-5 | SP500 | 15.0 | -0.01964313261685602 | -0.0029464698925284025 | Benchmark anchor to limit tracking error in a trending tape. |
| google-gemini-3-1-pro | ENERGY | 50.0 | 0.04405502784146731 | 0.022027513920733655 | Strong recent momentum and high quality evidence score, supported by crude oil price stability. |
| google-gemini-3-1-pro | HEALTHCARE | 50.0 | 0.02381517995011273 | 0.011907589975056365 | Defensive sector with strong recent performance and positive employment data. |
| openai-gpt-5-6-sol | DIVIDEND | 25.0 | 0.011617775196050006 | 0.0029044437990125016 | Positive prior and recent benchmark-relative performance, moderate volatility, and a 0.650 quality score support continued defensive leadership. |
| openai-gpt-5-6-sol | HEALTHCARE | 30.0 | 0.02381517995011273 | 0.007144553985033819 | Healthcare combines strong recent and prior active returns with defensive exposure amid weak payroll data and event risk. |
| openai-gpt-5-6-sol | SOFTWARE | 20.0 | -0.04111780203236737 | -0.008223560406473474 | Software has the strongest prior active trend among the finalists and retained positive recent active momentum despite its elevated volatility. |
| openai-gpt-5-6-sol | GOLD | 25.0 | 0.04096356077280494 | 0.010240890193201235 | Gold has positive prior and recent relative momentum, with geopolitical uncertainty and soft labor data providing independent support. |
| xai-grok-4-3 | LARGE_VALUE | 40.0 | -0.00977966756861215 | -0.00391186702744486 | Value tilt with strong quality evidence and recent relative strength versus SPY. |
| xai-grok-4-3 | HEALTHCARE | 35.0 | 0.02381517995011273 | 0.008335312982539455 | Defensive sector with positive active return and employment resilience in July data. |
| xai-grok-4-3 | GOLD | 25.0 | 0.04096356077280494 | 0.010240890193201235 | Safe-haven demand supported by labor-market softening and geopolitical crude uncertainty. |
| xai-grok-4-5 | ENERGY | 35.0 | 0.04405502784146731 | 0.015419259744513558 | Strong recent absolute and active returns plus ongoing Iran-related crude uncertainty support continued outperformance versus SPY over the one-week window. |
| xai-grok-4-5 | HEALTHCARE | 30.0 | 0.02381517995011273 | 0.007144553985033819 | Positive active returns, new 52-week high proximity, and defensive characteristics amid soft labor data favor relative strength versus SPY. |
| xai-grok-4-5 | GOLD | 20.0 | 0.04096356077280494 | 0.008192712154560989 | Elevated prior active trend and recent strength with inflation still above target support further gains versus SPY. |
| xai-grok-4-5 | COPPER | 15.0 | -0.012547051442910906 | -0.0018820577164366358 | Top quality-evidence score, strong prior active return, and industrial demand backdrop support base-case outperformance. |
| xai-grok-4-6 | HEALTHCARE | 30.0 | 0.02381517995011273 | 0.007144553985033819 | Recent relative strength, new highs, and defensive earnings mix can outperform a near-ATH SPY if PPI/retail prints keep growth soft but not collapsing. |
| xai-grok-4-6 | ENERGY | 20.0 | 0.04405502784146731 | 0.008811005568293463 | Oil and energy already repriced higher on Iran-flow uncertainty; residual geopolitical premium can persist through the weekly window if crude stays bid. |
| xai-grok-4-6 | JAPAN | 20.0 | -0.04265258454351584 | -0.008530516908703168 | Japan showed the strongest developed-market 5-session active return and sits at a 52-week high with ISM expansion still supportive of global cyclicals. |
| xai-grok-4-6 | FINANCIALS | 15.0 | -0.02248541023000339 | -0.0033728115345005084 | High quality-evidence rank, shallow drawdown, and a still-steep long end of the Treasury curve support a modest weekly edge over cap-weighted SPY. |
| xai-grok-4-6 | GOLD | 15.0 | 0.04096356077280494 | 0.006144534115920741 | Gold’s 5- and 21-session strength can continue if softer labor/CPI path keeps real-rate upside limited after the July hold. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | ENERGY | 2 | 0.65 | 0.04405502784146731 | 0.03393510389579002 | 0.05357823651264604 | 0.19937480474792046 |  | True | True |
| xai-grok-4-5 | ENERGY | 4 | 0.58 | 0.04405502784146731 | 0.028874468167671728 | 0.04851760078452774 | 0.20443544047603876 |  | True | True |
| anthropic-claude-fable-5 | GOLD | 4 | 0.58 | 0.04096356077280494 | 0.01634916265279901 | 0.03599229526965503 | 0.21696074599091147 |  | True | True |
| xai-grok-4-3 | LARGE_VALUE | 3 | 0.62 | -0.00977966756861215 | 0.01466433614829583 | 0.03430746876515185 | 0.21864557249541466 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 3 | 0.55 | 0.02381517995011273 | 0.01374928479848133 | 0.03339241741533735 | 0.21956062384522915 |  | True | True |
| openai-gpt-5-6-sol | HEALTHCARE | 4 | 0.59 | 0.02381517995011273 | 0.012066327570774082 | 0.0317094601876301 | 0.2212435810729364 |  | True | True |
| xai-grok-4-6 | HEALTHCARE | 5 | 0.54 | 0.02381517995011273 | 0.010196765226044346 | 0.029839897842900365 | 0.22311314341766614 |  | True | True |
| anthropic-claude-opus-5 | HEALTHCARE | 5 | 0.53 | 0.02381517995011273 | 0.0027294674674487097 | 0.02237260008430473 | 0.23058044117626178 |  | True | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | HEALTHCARE | 0.02237260008430473 | 0.220995 | 0.10123577494651341 |
| anthropic-claude-fable-5 | GOLD | 0.03599229526965503 | 0.45684 | 0.07878534119090935 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c1531f7bcf8287a24759f94353d040d86f7a53050f9bebdc160b451f9eecbb0b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 919dfd9d5806523b9bf8aa5046b739226e39e8af7ee4ebe11911e26e18cec405 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 7e084bf9795a23e49f4917f7775baea8cb9df8ed857abe1cf7cb6ce7234372ad |
| market_data/universe_decision_context.md | d17a40f5388c9428beb191f21d0a6abdd5914c6fffc492459245fedb8e1d5b40 |
| market_data/universe_decision_context.json | a69b1f26261bb1b589b2f012fba5f8af048e34ba56b1bcae3f6e6d18f9a09d26 |
| market_data/decision_context_source_history.json | ab7826004db11708ae4aaff9428ac1662d2328b30d95d5aae25059b0be4dec99 |
| market_data/universe_quality_evidence.md | 567d17bff7928f7e724eaaf0a8f249cd213798b73b5b9d2a4905b2e82d8f3267 |
| market_data/universe_quality_evidence.json | 5b3342c41274c8a6f6944fd61ba7c5879b68251850f815f373625ec0199c3f43 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | dd1b1aac2282a3e68c147c1f4c9f9b5c88b67cf5611299d1e66bd625fbe0b25b | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 5bfa3d1aab603b4f71ea80c14503d404e7b810a510ba23c06baa8bde298c3cd7 | yes |
| Final briefing | research/final_briefing.md | model-facing | c1531f7bcf8287a24759f94353d040d86f7a53050f9bebdc160b451f9eecbb0b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
