# CapitalBench Report: CB-2026-10-27-1W / official-20261027-1W

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20261027-1W
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-27-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-10-28
- Decision deadline: 2026-10-28T13:25:00Z
- Horizon: one week
- Entry date: 2026-10-28
- Exit date: 2026-11-04
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-4-argon | google | portfolio | CONSUMER_DISCRETIONARY | 3 | 0.57 | Cross-sectional dispersion is moderate (5-session active dispersion at 3.22%) with broad breadth outperforming cap-weighted benchmarks (RSP beating SPY by 3.18% over 21 sessions). Macro data shows sticky inflation alongside rebounding consumer confidence (91.7) and retail sales (+0.8% monthly). With the October FOMC conclusion at entry and Q3 GDP, PCE, ECI, and the US general election inside the scoring window, high-quality value and consumer pullbacks with strong prior relative trends offer superior risk-adjusted setups over volatile idiosyncratic shocks. | Advance Q3 GDP, September PCE, and Q3 Employment Cost Index releases on October 29-30 could surprise to the upside on inflation, pressuring equities.; The November 3 US general election and November 3 JOLTS release introduce event and policy uncertainty right before the November 4 exit close.; Post-FOMC market repricing on the October 28 entry day could alter sector leadership and rate sensitivity across value and defensive equities. |
| openai-gpt-6-astra | openai | portfolio | SP500 | 2 | 0.56 | Active-return dispersion of 3.22% and Brazil's exceptional dislocation indicate substantial cross-sectional risk. Energy has independent inflation and refinery-demand support, while selected defensive pullbacks merit reversal consideration. Strong nominal consumption conflicts with weak employment and housing, limiting confidence in broad cyclical continuation. GDP, income/outlays, ECI and the election fall inside the holding window; the initial FOMC announcement precedes the entry close. | The unknown FOMC outcome occurs before entry and could materially reset prices and relative opportunities.; GDP, personal income/outlays and ECI could reveal either renewed inflation pressure or weaker demand, reversing sector preferences.; November 3 election developments can cause abrupt sector and broad-market repricing before the exit close.; Staples' decline may reflect persistent margin pressure rather than temporary selling; elevated producer prices challenge the reversal thesis.; Brazil's unexplained dislocation could reflect either lasting impairment or a rapid rebound far larger than the central forecast. |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 2 | 0.55 | SPY is flat over 5 sessions while equal-weight outperformed and bonds rallied. The FOMC concludes on entry day with inflation still hot (CPI 3.7%, PPI 6.3%). GDP, ECI, the election and JOLTS all fall inside the window. Active dispersion of 3.22% is moderate, and Brazil's shock is the outlier. | A hawkish FOMC outcome on entry day; Election-week volatility; Further policy or currency shock in Brazil; A risk-on rally that leaves defensives lagging |
| xai-grok-4-5 | xai | portfolio | BRAZIL | 3 | 0.5867 | Elevated cross-sectional dispersion with extreme EM shock in Brazil, mixed sector moves, pending FOMC outcome on entry day, and data releases inside the week favor selective reversal over pure continuation; SPY remains competitive amid policy uncertainty. | FOMC decision unknown at cutoff can reverse risk assets on entry close; Brazil idiosyncratic political/commodity shock may not mean-revert in one week; High horizon vol in EM/crypto/energy can dominate excess ranges; November 3 election and mid-week data (GDP/ECI/JOLTS) add event risk |
| xai-grok-4-6 | xai | portfolio | BRAZIL | 3 | 0.5633 | Five-session active-return dispersion is 3.22% with 70% of assets positive, equal-weight beating SPY, and a hot September CPI/PPI plus an in-progress FOMC and in-window election/GDP prints. Breadth and energy strength coexist with a Brazil shock and communications/staples pullbacks, so the week is mixed rather than a clean continuation or reversal tape. | FOMC decision on entry day can reprice rates, growth, and high-beta EM simultaneously.; Brazil 86% horizon vol can extend the -18% shock rather than mean-revert in one week.; November 3 election plus Oct 29-30 GDP/ECI and Nov 3 JOLTS can dominate the Nov 4 close.; Hot September CPI/PPI (0.6%/1.3% m/m) can keep duration and defensives unstable if the Fed stays hawkish. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | BRAZIL | 3 | 0.565 | Macro backdrop is stagflationary: hot CPI/PPI, a Fed hiking cycle with the FOMC decision landing on entry day, weak payrolls and housing, yet rising confidence and retail sales. SPY is near highs with narrow breadth (most constituents fell on Oct 27, RSP outperforming over 21 sessions). Week contains FOMC aftermath, GDP, ECI, the Nov 3 election and JOLTS, so event risk is elevated. Cross-sectional dispersion is moderate; a single idiosyncratic shock (Brazil -18%) dominates the slate. Most slate moves are either small or trend-supported, leaving few true overreaction setups. | FOMC decision on entry day could trigger a repricing in rates and dollar that extends EM and Brazil weakness; Brazil's -18% drop may reflect unreported country-specific fiscal or political news that continues, with 86% vol amplifying downside; Nov 3 US election and GDP/ECI data could spark a volatility spike that hurts beta-exposed Communications; Hot CPI/PPI with a hiking Fed raises risk of broad equity de-rating where overreaction picks fail to bounce |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOLAR | Solar Energy | 40.98 | 45.79 | 0.11737432894094679 | 1 |
| REAL_ESTATE | Real Estate Sector | 42.13 | 45.12 | 0.07097080465226657 | 2 |
| INDIA | India Equities | 46.79 | 50.03 | 0.06924556529172898 | 3 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.33 | 122.33 | 0.06069539582068839 | 4 |
| CONSUMER_STAPLES | Consumer Staples Sector | 86.84 | 91.94 | 0.05872869645324719 | 5 |
| HEALTHCARE | Healthcare Sector | 179.72 | 189.66 | 0.05530825728911637 | 6 |
| FINANCIALS | Financials Sector | 56.13 | 59.2 | 0.05469445929093175 | 7 |
| CHINA | China Equities | 49.04 | 51.56 | 0.0513866231647635 | 8 |
| LOW_VOL | US Low Volatility Equities | 75.07 | 78.51 | 0.04582389769548434 | 9 |
| MATERIALS | Materials Sector | 51.86 | 53.9 | 0.039336675665252674 | 10 |
| UNITED_KINGDOM | United Kingdom Equities | 47.29 | 48.93 | 0.03467963628674142 | 11 |
| EUROPE | Europe Equities | 87.31 | 90.24 | 0.033558584354598464 | 12 |
| DIVIDEND | US Dividend Equities | 35.09 | 36.21 | 0.03191792533485316 | 13 |
| REGIONAL_BANKS | Regional Banks | 72.11 | 74.13 | 0.028012758285951955 | 14 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 217.43 | 223.33 | 0.027135169939750847 | 15 |
| UTILITIES | Utilities Sector | 42.49 | 43.61 | 0.02635914332784184 | 16 |
| LARGE_VALUE | US Large-Cap Value | 258.72 | 265.3 | 0.025432900432900363 | 17 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 207.74 | 212.84 | 0.02454991816693952 | 18 |
| MEXICO | Mexico Equities | 74.62999725341797 | 76.3499984741211 | 0.02304704922958245 | 19 |
| ETHEREUM_ETF | Ethereum ETF | 53.599998474121094 | 54.7400016784668 | 0.021268717104462542 | 20 |
| SOUTH_AFRICA | South Africa Equities | 64.36000061035156 | 65.55999755859375 | 0.01864507359947387 | 21 |
| SMALL_VALUE | US Small-Cap Value | 214.81 | 218.65 | 0.017876262743820037 | 22 |
| COMMUNICATIONS | Communication Services Sector | 103.14 | 104.96 | 0.01764591816947836 | 23 |
| MID_CAP | US Mid-Cap Stocks | 73.35 | 74.59 | 0.016905248807089324 | 24 |
| BIOTECH | Biotechnology | 157.51 | 159.1 | 0.010094597168433861 | 25 |
| SMALL_CAP | US Small-Cap Stocks | 281.29 | 284.02 | 0.009705286359273257 | 26 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 80.99 | 81.76 | 0.0095073465859985 | 27 |
| AUSTRALIA | Australia Equities | 29.59000015258789 | 29.860000610351562 | 0.009124719715152052 | 28 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 90.85 | 91.66 | 0.008915795266923432 | 29 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 91.79000091552734 | 92.44000244140625 | 0.007081397967051872 | 30 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.34 | 70.82 | 0.00682399772533393 | 31 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.41000366210938 | 91.97000122070312 | 0.006126217439655024 | 32 |
| MUNICIPAL_BONDS | Municipal Bonds | 103.76000213623047 | 104.36000061035156 | 0.005782560348575716 | 33 |
| INDUSTRIALS | Industrials Sector | 168.49 | 169.46 | 0.005757018220665877 | 34 |
| EURO | Euro | 103.02999877929688 | 103.61000061035156 | 0.005629446160599461 | 35 |
| CANADA | Canada Equities | 61.51 | 61.84 | 0.005364981303853211 | 36 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.89 | 96.38 | 0.0051100219000939084 | 37 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.279998779296875 | 47.4900016784668 | 0.004441685799321027 | 38 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 104.07 | 104.5 | 0.0041318343422696024 | 39 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 40 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 77.59 | 77.52 | -0.0009021781157366737 | 41 |
| TIPS | Treasury Inflation-Protected Securities | 106.26 | 106.1 | -0.0015057406361754788 | 42 |
| GOLD | Gold | 76.57 | 76.37 | -0.002611989029645878 | 43 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.66 | 91.42 | -0.0026183722452541858 | 44 |
| YEN | Japanese Yen | 58.08000183105469 | 57.81999969482422 | -0.004476620661734376 | 45 |
| US_DOLLAR | US Dollar | 29.059999465942383 | 28.899999618530273 | -0.005505844815985816 | 46 |
| TOTAL_US_MARKET | Total US Stock Market | 379.17 | 376.92 | -0.005934013766911939 | 47 |
| SP500 | S&P 500 | 772.31 | 766.81 | -0.007121492664862505 | 48 |
| JAPAN | Japan Equities | 94.99 | 93.86 | -0.011895989051479039 | 49 |
| EMERGING_MARKETS | Emerging Markets | 57.02 | 56.28 | -0.012977902490354243 | 50 |
| BITCOIN_ETF | Bitcoin ETF | 46.13999938964844 | 45.33000183105469 | -0.01755521389918946 | 51 |
| AGRICULTURE | Agriculture Commodities | 27.110000610351562 | 26.450000762939453 | -0.02434525387506259 | 52 |
| SILVER | Silver | 49.060001373291016 | 47.15999984741211 | -0.0387281180736635 | 53 |
| BRAZIL | Brazil Equities | 33.619998931884766 | 32.25 | -0.040749523361390594 | 54 |
| LARGE_GROWTH | US Large-Cap Growth | 123.01 | 117.9 | -0.041541338102593306 | 55 |
| COPPER | Copper | 40.33000183105469 | 38.59000015258789 | -0.043144101152184144 | 56 |
| NASDAQ100 | Nasdaq 100 | 725.61 | 691.95 | -0.0463885558357795 | 57 |
| METALS_MINING | Metals and Mining | 101.31 | 95.78 | -0.05458493732109371 | 58 |
| BROAD_AI_TECH | Broad AI Technology | 64.4 | 59.87 | -0.07034161490683244 | 59 |
| ENERGY | Energy Sector | 68.45 | 63.52 | -0.07202337472607745 | 60 |
| SOFTWARE | Software | 111.91 | 103.56 | -0.0746135287284424 | 61 |
| BROAD_COMMODITIES | Broad Commodities | 20.14 | 18.63 | -0.07497517378351548 | 62 |
| TECHNOLOGY | Technology Sector | 191.0 | 176.5 | -0.0759162303664922 | 63 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 116.66 | 107.74 | -0.07646151208640495 | 64 |
| SOUTH_KOREA | South Korea Equities | 165.91000366210938 | 152.1199951171875 | -0.08311740245034571 | 65 |
| CYBERSECURITY | Cybersecurity | 107.92 | 97.36 | -0.09785025945144554 | 66 |
| MOMENTUM | US Momentum Equities | 303.5 | 272.86 | -0.10095551894563426 | 67 |
| TAIWAN | Taiwan Equities | 108.94000244140625 | 97.08000183105469 | -0.1088672695480295 | 68 |
| SEMICONDUCTORS | Semiconductors | 567.67 | 504.27 | -0.11168460549262771 | 69 |
| OIL | Crude Oil | 166.57000732421875 | 145.41000366210938 | -0.12703369593376235 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | BRAZIL | 35.0 | -0.040749523361390594 | -0.014262333176486707 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | COMMUNICATIONS | 35.0 | 0.01764591816947836 | 0.006176071359317425 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 30.0 | -0.007121492664862505 | -0.0021364477994587515 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5-5 | CONSUMER_STAPLES | 35.0 | 0.05872869645324719 | 0.020555043758636513 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 65.0 | -0.007121492664862505 | -0.004628970232160629 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-4-argon | CONSUMER_DISCRETIONARY | 35.0 | 0.06069539582068839 | 0.021243388537240934 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-4-argon | CONSUMER_STAPLES | 35.0 | 0.05872869645324719 | 0.020555043758636513 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| google-gemini-4-argon | LARGE_VALUE | 30.0 | 0.025432900432900363 | 0.007629870129870108 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | CONSUMER_STAPLES | 35.0 | 0.05872869645324719 | 0.020555043758636513 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 65.0 | -0.007121492664862505 | -0.004628970232160629 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | BRAZIL | 35.0 | -0.040749523361390594 | -0.014262333176486707 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | COMMUNICATIONS | 35.0 | 0.01764591816947836 | 0.006176071359317425 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | CONSUMER_STAPLES | 30.0 | 0.05872869645324719 | 0.017618608935974157 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | BRAZIL | 35.0 | -0.040749523361390594 | -0.014262333176486707 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | COMMUNICATIONS | 35.0 | 0.01764591816947836 | 0.006176071359317425 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | CONSUMER_STAPLES | 30.0 | 0.05872869645324719 | 0.017618608935974157 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-4-argon | CONSUMER_DISCRETIONARY | 3 | 0.57 | 0.06069539582068839 | 0.049428302425747556 | 0.05654979509061006 | 0.06794602651519924 |  | True | True |
| openai-gpt-6-astra | SP500 | 2 | 0.56 | -0.007121492664862505 | 0.015926073526475883 | 0.023047566191338388 | 0.10144825541447092 |  | True | True |
| anthropic-claude-opus-5-5 | SP500 | 2 | 0.55 | -0.007121492664862505 | 0.015926073526475883 | 0.023047566191338388 | 0.10144825541447092 |  | True | True |
| xai-grok-4-5 | BRAZIL | 3 | 0.5867 | -0.040749523361390594 | 0.009532347118804874 | 0.016653839783667378 | 0.10784198182214191 |  | True | True |
| xai-grok-4-6 | BRAZIL | 3 | 0.5633 | -0.040749523361390594 | 0.009532347118804874 | 0.016653839783667378 | 0.10784198182214191 |  | True | True |
| anthropic-claude-fable-5-1 | BRAZIL | 3 | 0.565 | -0.040749523361390594 | -0.010222709616628033 | -0.003101216951765528 | 0.12759703855757482 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 339b0a702a7a3a9afe4d0dbfd6b903112b069467d01f55204345d1184bcdcc4c |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | f129402e78b42bc664276e0952d4500c91facbf2be5b2c79e66bc70db672245f |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 040c84d48a05c4f7e7180a4f01786156fc00f14068585b2cadf90b2e5741ebd0 |
| market_data/universe_decision_context.md | 59548a20d7f2685d2bda0c3ea9debf2144b629a101dbbb0185a2ff6e4eff395e |
| market_data/universe_decision_context.json | 70f4ad5c978b0d8348c2d44516f4874adff1f8d821da277975de91f563b90463 |
| market_data/decision_context_source_history.json | fb5ab8adc818282c49cb189b6e69606f4b8511c2a66fe8160ec8c60922c10264 |
| market_data/universe_quality_evidence.md | 402964c5202a69a217445d6467dcc7bb4fa4593f44ddcf4d0927e264dd1c4b66 |
| market_data/universe_quality_evidence.json | 766da6eff01a321842a9da7c7027f32e6f2c8f1de8c1c6f8d323d5e0e2168ee5 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | bc8baeae24f840e6eafbed0960625486865bd415a749e8a40686e79d6ea56674 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 7c81186260dddac1d67f1f2f621be2641603c5026c976bb587a858e6fa642303 | yes |
| Final briefing | research/final_briefing.md | model-facing | 339b0a702a7a3a9afe4d0dbfd6b903112b069467d01f55204345d1184bcdcc4c | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
