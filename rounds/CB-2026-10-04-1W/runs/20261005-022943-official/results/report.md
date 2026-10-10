# CapitalBench Report: CB-2026-10-04-1W / 20261005-022943-official

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: 20261005-022943-official
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-04-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-10-04
- Decision deadline: 2026-10-05T13:25:00Z
- Horizon: one week
- Entry date: 2026-10-02
- Exit date: 2026-10-09
- Entry rule: Use the October 2, 2026 official adjusted close supplied in prices/entry_prices.csv; CASH is fixed at 1.0.
- Exit rule: Use the October 9, 2026 official adjusted close supplied in prices/exit_prices.csv; CASH is fixed at 1.0.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-6-astra | openai | portfolio | COPPER | 3 | 0.555 | Weak payrolls and downward revisions favor selective pullback recovery, but manufacturing expansion, elevated input prices and recent policy tightening argue against a broad reversal. Only 26.09% of assets rose over five sessions, while active-return dispersion was 1.81 percentage points. Copper and healthcare offer modest reversal edges; neither recent technology leadership nor extreme precious-metal losses alone establishes a reliable one-week advantage. Services and trade releases can change the balance before October 9. | October 5 services data could strengthen inflation and rate concerns or reveal a sharper demand slowdown, undermining the selected reversal theses.; Persistent dollar appreciation and high real-rate pressure could overwhelm copper's manufacturing support.; Healthcare has no supplied sector-specific catalyst; its pullback may persist despite defensive macro characteristics.; Renewed concentrated technology leadership could cause both eligible candidates to lag SPY. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | HEALTHCARE | 3 | 0.555 | Macro mix is stagflationary-leaning: payrolls weak (29k, prior months revised down 60k) but inflation elevated (PCE 3.4%, ISM prices 77.9), Fed hiked to 3.75-4.00% and 10y at 5.28%. SPY sits within 1% of its 52-week high while breadth is narrow (RSP -4.5% vs SPY over 21 sessions, only 26% of assets positive over 5 sessions). Leadership is concentrated in semis/tech; defensives, duration, credit and precious metals have been sold. With yields easing slightly after the soft payroll print and only second-tier data (ISM services, trade, wholesale) before exit, a modest mean-reversion in oversold low-beta pockets is plausible, but the regime offers limited high-conviction edge versus SPY. | ISM services on Oct 5 prints hot on prices, pushing yields and the dollar higher and hurting gold, healthcare rotation, and credit; Semiconductor/mega-cap leadership extends further, leaving defensive and reversal names lagging SPY; Risk-off shock from weak labor data widens credit spreads, hurting HYG and high-beta EM candidates; Dollar strength continues (UUP +2.56% over 21 sessions), pressuring precious metals and EM equities |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 2 | 0.55 | Active-return dispersion is moderate at 1.81%, and only 26% of assets rose over the week. Long yields sit above 5%, the dollar is strong, and gold and TLT are weak. The Fed hiked into elevated PCE inflation while payrolls softened. Breadth is narrow, with RSP 4.5% behind SPY over 21 sessions and tech leading. No dominant reversal or continuation signal is clear before the ISM services release on Oct 5. | A strong ISM services print could lift high-beta tech, leaving low-beta Healthcare behind; A further rise in yields could hurt defensive sectors; Narrow market leadership could keep favoring mega-cap tech |
| xai-grok-4-5 | xai | portfolio | HEALTHCARE | 3 | 0.57 | Low cross-sectional dispersion with weak breadth, sticky inflation and soft payrolls after a 25bp hike, mixed manufacturing strength vs price pressures; tech/semi continuation coexists with precious-metal and select EM pullbacks that may reverse over one week. | Sticky PCE inflation and manufacturing prices index at 77.9 could extend rate pressure and hurt duration-sensitive reversals; Soft payrolls with downward revisions may trigger risk-off that hits EM and metals harder than expected; High-beta continuation names (semis, crypto) could reverse sharply if ISM services disappoints; Volume dislocations in HYG/XLU may reflect liquidity stress rather than clean mean-reversion |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Mixed signals from weak payrolls offset by manufacturing expansion and rate hike; limited one-week edge outside select continuation and pullback names. | weakening labor data may pressure equities; elevated manufacturing input prices could limit upside; upcoming CPI and FOMC events add volatility |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | Five-session active dispersion is only 1.81% with 26% of assets positive; SPY is 0.81% from a 52-week high after a 0.71% bounce while equal-weight lagged. Policy rates were just hiked, long yields remain above 5%, and the dollar was firm, so mega-cap/tech continuation coexists with commodity and EM shock-reversal candidates rather than a clean one-week trend. | ISM services Oct 5 and trade/energy data Oct 6-7 can reverse one-week factor leadership.; Elevated manufacturing input prices (77.9) and PCE 3.4% y/y keep rates and the dollar bid against metals and EM.; Semiconductor beta 2.38 and crypto/metal vols above 38% can produce large negative excess even if the directional call is right.; HYG and utilities volume spikes may reflect stress rather than a durable bid. |
| google-gemini-3-1-pro | google | portfolio | SILVER | 3 | 0.58 | The market is digesting mixed economic signals, with slower payroll growth and downward revisions contrasting with ongoing manufacturing expansion and positive real consumption growth. Long-term Treasury yields remain elevated above 5%. | Continued upward pressure on long-term Treasury yields could negatively impact non-yielding assets like precious metals.; Upcoming economic data releases (ISM services, CPI, PPI) could introduce volatility and alter the current market narrative. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 20.110000610351562 | 55.9900016784668 | 1.784186970618296 | 1 |
| BRAZIL | Brazil Equities | 38.189998626708984 | 43.540000915527344 | 0.1400890935114285 | 2 |
| CYBERSECURITY | Cybersecurity | 104.7 | 110.0 | 0.050620821394460336 | 3 |
| UTILITIES | Utilities Sector | 39.83 | 41.41 | 0.03966859151393409 | 4 |
| SOFTWARE | Software | 108.43 | 112.67 | 0.039103569122936443 | 5 |
| CONSUMER_STAPLES | Consumer Staples Sector | 80.53 | 83.43 | 0.03601142431392024 | 6 |
| ENERGY | Energy Sector | 62.82 | 65.08 | 0.035975803884113366 | 7 |
| HEALTHCARE | Healthcare Sector | 166.18 | 170.81 | 0.027861355157058565 | 8 |
| CHINA | China Equities | 51.24 | 52.55 | 0.025565964090554116 | 9 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 110.04 | 112.85 | 0.02553616866593944 | 10 |
| FINANCIALS | Financials Sector | 53.49 | 54.73 | 0.023181903159468886 | 11 |
| COPPER | Copper | 39.52000045776367 | 40.310001373291016 | 0.01998990147714297 | 12 |
| REAL_ESTATE | Real Estate Sector | 40.81 | 41.61 | 0.019603038470962897 | 13 |
| LOW_VOL | US Low Volatility Equities | 70.89 | 72.14 | 0.01763295246156016 | 14 |
| LARGE_VALUE | US Large-Cap Value | 249.38 | 253.54 | 0.01668136979709689 | 15 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 209.73 | 213.04 | 0.015782196156963746 | 16 |
| MEXICO | Mexico Equities | 71.08999633789062 | 71.94999694824219 | 0.01209735060702477 | 17 |
| GOLD | Gold | 77.95 | 78.87 | 0.011802437459910164 | 18 |
| MATERIALS | Materials Sector | 48.86 | 49.43 | 0.01166598444535416 | 19 |
| SP500 | S&P 500 | 769.64 | 778.57 | 0.011602827295878582 | 20 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 90.13999938964844 | 91.16999816894531 | 0.011426656160097082 | 21 |
| BROAD_COMMODITIES | Broad Commodities | 19.44 | 19.66 | 0.011316872427983515 | 22 |
| AUSTRALIA | Australia Equities | 28.31999969482422 | 28.6200008392334 | 0.010593260863064557 | 23 |
| TOTAL_US_MARKET | Total US Stock Market | 377.99 | 381.94 | 0.010450011905076773 | 24 |
| DIVIDEND | US Dividend Equities | 32.72 | 33.04 | 0.009779951100244544 | 25 |
| SOUTH_AFRICA | South Africa Equities | 63.189998626708984 | 63.79999923706055 | 0.009653436043812968 | 26 |
| UNITED_KINGDOM | United Kingdom Equities | 46.18 | 46.52 | 0.007362494586401036 | 27 |
| LARGE_GROWTH | US Large-Cap Growth | 127.07 | 127.91 | 0.006610529629338169 | 28 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 77.48 | 77.98 | 0.006453278265358797 | 29 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 89.22000122070312 | 89.79000091552734 | 0.006388698576838214 | 30 |
| METALS_MINING | Metals and Mining | 105.74 | 106.35 | 0.005768867032343472 | 31 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 101.83 | 102.41 | 0.0056957674555631055 | 32 |
| OIL | Crude Oil | 147.3699951171875 | 148.1999969482422 | 0.0056320951248907125 | 33 |
| BROAD_AI_TECH | Broad AI Technology | 66.23 | 66.6 | 0.005586592178770777 | 34 |
| CANADA | Canada Equities | 58.72 | 59.03 | 0.005279291553133447 | 35 |
| US_DOLLAR | US Dollar | 28.889999389648438 | 29.020000457763672 | 0.004499863996598519 | 36 |
| AGRICULTURE | Agriculture Commodities | 28.209999084472656 | 28.329999923706055 | 0.004253840592977953 | 37 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 76.91 | 77.23 | 0.004160707320244539 | 38 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 89.05 | 89.4 | 0.003930376193149954 | 39 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 94.25 | 94.59 | 0.0036074270557029386 | 40 |
| EMERGING_MARKETS | Emerging Markets | 59.56 | 59.76 | 0.003357958361316138 | 41 |
| TIPS | Treasury Inflation-Protected Securities | 104.11 | 104.42 | 0.002977619825184963 | 42 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.86000061035156 | 46.97999954223633 | 0.0025607966351210987 | 43 |
| NASDAQ100 | Nasdaq 100 | 749.58 | 751.27 | 0.002254595907041246 | 44 |
| MUNICIPAL_BONDS | Municipal Bonds | 100.95999908447266 | 101.08000183105469 | 0.0011886167558463612 | 45 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.43 | 91.51 | 0.0008749863283386006 | 46 |
| SILVER | Silver | 54.7400016784668 | 54.779998779296875 | 0.0007306740884849283 | 47 |
| MID_CAP | US Mid-Cap Stocks | 73.39 | 73.43 | 0.0005450333832948129 | 48 |
| COMMUNICATIONS | Communication Services Sector | 110.32 | 110.38 | 0.0005438723712836158 | 49 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 50 |
| YEN | Japanese Yen | 58.06999969482422 | 57.900001525878906 | -0.002927469775076741 | 51 |
| EUROPE | Europe Equities | 86.38 | 86.03 | -0.004051863857374327 | 52 |
| INDUSTRIALS | Industrials Sector | 169.95 | 169.25 | -0.004118858487790478 | 53 |
| BIOTECH | Biotechnology | 154.43 | 153.77 | -0.004273781001100763 | 54 |
| EURO | Euro | 103.81999969482422 | 103.37000274658203 | -0.004334395584328021 | 55 |
| TECHNOLOGY | Technology Sector | 199.81 | 198.78 | -0.0051548971522946685 | 56 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 207.79 | 206.65 | -0.005486308292025566 | 57 |
| SOLAR | Solar Energy | 44.05 | 43.75 | -0.006810442678774065 | 58 |
| SMALL_VALUE | US Small-Cap Value | 212.34 | 210.87 | -0.006922859564848838 | 59 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.48 | 123.51 | -0.007792416452442108 | 60 |
| MOMENTUM | US Momentum Equities | 322.88 | 320.0 | -0.008919722497522264 | 61 |
| SMALL_CAP | US Small-Cap Stocks | 281.52 | 278.94 | -0.009164535379369121 | 62 |
| INDIA | India Equities | 46.52 | 46.03 | -0.010533104041272612 | 63 |
| JAPAN | Japan Equities | 98.92 | 97.86 | -0.010715729882733505 | 64 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.13 | 70.35 | -0.010965837199493955 | 65 |
| TAIWAN | Taiwan Equities | 116.33000183105469 | 114.30999755859375 | -0.01736443084901329 | 66 |
| BITCOIN_ETF | Bitcoin ETF | 47.72999954223633 | 46.54999923706055 | -0.02472240344631882 | 67 |
| REGIONAL_BANKS | Regional Banks | 70.78 | 69.01 | -0.02500706414241305 | 68 |
| SEMICONDUCTORS | Semiconductors | 630.6 | 603.33 | -0.04324452901998099 | 69 |
| SOUTH_KOREA | South Korea Equities | 191.8800048828125 | 177.24000549316406 | -0.07629768093131728 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | HEALTHCARE | 35.0 | 0.027861355157058565 | 0.009751474304970496 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | GOLD | 35.0 | 0.011802437459910164 | 0.0041308531109685576 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 30.0 | 0.011602827295878582 | 0.0034808481887635746 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5-5 | HEALTHCARE | 35.0 | 0.027861355157058565 | 0.009751474304970496 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 65.0 | 0.011602827295878582 | 0.007541837742321078 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | SILVER | 35.0 | 0.0007306740884849283 | 0.0002557359309697249 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOUTH_AFRICA | 35.0 | 0.009653436043812968 | 0.003378702615334539 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | GOLD | 30.0 | 0.011802437459910164 | 0.0035407312379730493 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | COPPER | 35.0 | 0.01998990147714297 | 0.006996465517000039 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | HEALTHCARE | 35.0 | 0.027861355157058565 | 0.009751474304970496 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | 0.011602827295878582 | 0.0034808481887635746 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | SP500 | 100.0 | 0.011602827295878582 | 0.011602827295878582 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | HEALTHCARE | 35.0 | 0.027861355157058565 | 0.009751474304970496 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | GOLD | 35.0 | 0.011802437459910164 | 0.0041308531109685576 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-5 | HIGH_YIELD_CREDIT | 30.0 | 0.004160707320244539 | 0.0012482121960733616 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.011602827295878582 | 0.011602827295878582 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-6-astra | COPPER | 3 | 0.555 | 0.01998990147714297 | 0.020228788010734113 | 0.008625960714855531 | 1.7639581826075619 |  | True | True |
| anthropic-claude-fable-5-1 | HEALTHCARE | 3 | 0.555 | 0.027861355157058565 | 0.01736317560470263 | 0.005760348308824048 | 1.7668237950135934 |  | True | True |
| anthropic-claude-opus-5-5 | SP500 | 2 | 0.55 | 0.011602827295878582 | 0.017293312047291575 | 0.0056904847514129935 | 1.7668936585710044 |  | True | True |
| xai-grok-4-5 | HEALTHCARE | 3 | 0.57 | 0.027861355157058565 | 0.015130539612012415 | 0.003527712316133833 | 1.7690564310062835 |  | True | True |
| xai-grok-4-3 | SP500 | 1 | 0.5 | 0.011602827295878582 | 0.011602827295878582 | 0.0 | 1.7725841433224174 |  | False | True |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.011602827295878582 | 0.011602827295878582 | 0.0 | 1.7725841433224174 |  | False | True |
| google-gemini-3-1-pro | SILVER | 3 | 0.58 | 0.0007306740884849283 | 0.007175169784277314 | -0.004427657511601268 | 1.7770118008340188 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 2be55e79cbacdf50251358420f8851ed8ebd9700ede2c515652ef8f68466e8c5 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 993c872945daffea70b0b5cd12fdf096342df574277bf36d674628fe8f6035c6 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | b4e2ef36c58f15a24d5af1e0b1cb1686363900ec8c9a88a6eb1627f5b9599e14 |
| market_data/universe_decision_context.md | 79658091bf1cbc400f50e2e7deb8cd778b8ebefe4525a1308c8ea5a82a104d39 |
| market_data/universe_decision_context.json | 0b341d73559c1e959f7c4a724d2977e84718ecc5303b1e7c27cf3edcd67a86cd |
| market_data/decision_context_source_history.json | 2564e1ab0296d6800f7ac0fecbaf983a6e10db406a09a96f3ad9a368895140b2 |
| market_data/universe_quality_evidence.md | d831c88555000415e9432ed678fea3b915aedc734db17eccca1847336929f6c7 |
| market_data/universe_quality_evidence.json | 1ce57a15f7c1202a53ed46b59d5f46b0994d28e750c874136f5c9495d9eb7c10 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 909160d5d547fd1eed9d1b8c91c2165f665c76315399da1b1c9e3a6ef1d98f85 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | ca1df3e34fb65c139c4d56c1790794b673de5173335602e2e5998b8fabb76f85 | yes |
| Final briefing | research/final_briefing.md | model-facing | 2be55e79cbacdf50251358420f8851ed8ebd9700ede2c515652ef8f68466e8c5 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
