# CapitalBench Report: CB-2026-08-15-1W / official-v3-20260815-weekly-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260815-weekly-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-15-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-15
- Decision deadline: 2026-08-17T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-17
- Exit date: 2026-08-24
- Entry rule: Use the Monday, August 17, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Monday, August 24, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | anthropic | portfolio | AUSTRALIA | 3 | 0.56 | SPY sits near an all-time high with modest weekly gains, breadth positive (RSP beat SPY by 0.82% over 5 sessions), credit stable, and a mild rise in long yields. Cross-sectional active dispersion of 2.17% is unremarkable. The week's calendar (FOMC minutes, big-box retail earnings, industrial production) is informational rather than regime-changing. Recent laggards are mostly emerging-market/currency-driven pullbacks with intact medium-term trends, which supports modest mean-reversion in quality pullback names rather than aggressive positioning. | Currency-driven EM pullbacks can extend if the dollar firms further, hurting Australia, Mexico and South Africa simultaneously; FOMC minutes on August 19 could reveal hawkish dissent momentum and lift yields, pressuring high-beta international equities; Big-box retail earnings could shift US consumer sentiment and drive an index-level move that swamps small relative edges; South Africa's 28.5% volatility means the position can lose several points versus SPY in a single week; Correlated EM exposure across all three selections limits diversification if global risk appetite deteriorates |
| xai-grok-4-3 | xai | portfolio | AUSTRALIA | 3 | 0.5633 | Weak labor revisions and mixed retail data limit directional conviction; cross-sectional quality and pullback signals favor selective reversals over continuation in the one-week window. | Labor market revisions may extend defensive flows; One-week volatility in commodity-linked names; FOMC minutes could shift rate expectations |
| anthropic-claude-fable-5 | anthropic | portfolio | SOUTH_AFRICA | 3 | 0.5833 | SPY near all-time highs with modest weekly gains, equal-weight outperforming, and dispersion around 2.2%. Weak payrolls and mixed CPI/PPI keep policy uncertainty elevated. Best setups are quality pullbacks in international equities with strong prior relative trends (South Africa, China, Mexico) that lagged sharply last week without new fundamental deterioration, while short-term momentum names (Korea, Energy) look extended and high-vol. | EM/international reversal fails if dollar strengthens on hawkish FOMC minutes Aug 19; South Africa's 28.5% vol and 1.64 beta amplify any risk-off move; China-specific policy or geopolitical headlines could extend rather than reverse the pullback; Weak US retail earnings (HD/TGT/WMT) could trigger broad risk-off hitting high-beta EM |
| openai-gpt-5-6-sol | openai | portfolio | AUSTRALIA | 3 | 0.5767 | Breadth is positive but macro signals conflict: weak labor and retail data favor pullback reversals, while elevated inflation and rising yields constrain risk assets. High-quality international pullbacks offer the clearest one-week relative setups. | FOMC minutes could reinforce a hawkish stance and pressure global risk assets.; Housing, industrial-production, or retail earnings surprises could reverse the pullback thesis.; Elevated inflation and rising long yields could keep SPY leadership intact.; Currency and commodity moves could dominate the international-equity candidates over the short window. |
| xai-grok-4-5 | xai | portfolio | SOUTH_AFRICA | 3 | 0.59 | SPY near highs with low-to-normal cross-sectional dispersion; soft labor and sticky inflation mixed with solid ISM and energy strength create room for selective mean-reversion in high-quality international pullbacks alongside limited continuation in energy, rather than broad trend dominance. | Sticky CPI/PPI and hawkish FOMC minority could lift yields and pressure EM/risk assets into Aug 24; Soft July payrolls and retail sales may trigger growth-scare selling that hits cyclical internationals; Energy and metals continuation could reverse if oil fails to hold recent gains; High-vol names (Korea, silver, metals) can gap against mean-reversion thesis on any risk-off day |
| google-gemini-3-1-pro | google | portfolio | SOUTH_AFRICA | 3 | 0.555 | The market is showing mixed signals with the S&P 500 near all-time highs but some underlying weakness in specific sectors and international markets. Inflation data is relatively benign, but retail sales and housing starts show some softness. | A sudden reversal in recent momentum trends could negatively impact South Korea and Energy.; Broader market weakness could drag down all equity positions, including the S&P 500. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 1 | 0.5 | SPY near all-time highs with modest weekly gains; breadth positive (RSP slightly outperforming). Macro mixed: soft labor data, cooling core inflation, but yields drifting up. No high-conviction overreaction with strong reversal setup among the slate. Retailer earnings (HD, WMT, TGT, LOW) and FOMC minutes create idiosyncratic risk. Defaulting toward SPY given weak edge. | FOMC minutes and retailer earnings could drive sharp idiosyncratic moves during window; Rising Treasury yields pressuring rate-sensitive and high-beta EM equities; Oil pullback would reverse the energy continuation thesis |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is near a fresh high with only 2.17% 5-session active-return dispersion, mixed labor/inflation prints, and a data-and-FOMC-minutes week. Quality international pullbacks look cleaner than high-vol continuations or EM/crypto shocks, but none have a clear one-week catalyst edge versus the benchmark. | July 28-29 FOMC minutes on August 19 can reprice the 3.50%-3.75% hold and the three dissenters favoring a hike.; Retail and housing prints on August 18-20 plus Home Depot, Target, Lowe's, and Walmart can hit discretionary and cyclicals.; Energy and metals remain sensitive to the already-large oil move and 39%+ mining/silver vol.; EM and Korea beta (up to ~4) can dominate if risk appetite fades after the August 13 high. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.4 | 18.66 | 0.2958333333333334 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 36.42 | 44.64 | 0.22570016474464571 | 2 |
| GOLD | Gold | 83.11 | 87.47 | 0.05246059439297324 | 3 |
| SOUTH_AFRICA | South Africa Equities | 68.19 | 71.33 | 0.046047807596421686 | 4 |
| HEALTHCARE | Healthcare Sector | 167.05 | 174.7 | 0.04579467225381606 | 5 |
| SILVER | Silver | 59.57 | 62.2 | 0.04414973980191372 | 6 |
| BRAZIL | Brazil Equities | 33.97 | 35.17 | 0.03532528701795701 | 7 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.68 | 87.45 | 0.032711384034010305 | 8 |
| MEXICO | Mexico Equities | 74.91 | 77.15 | 0.029902549726338323 | 9 |
| BIOTECH | Biotechnology | 159.53 | 164.17 | 0.029085438475521697 | 10 |
| DIVIDEND | US Dividend Equities | 34.29 | 35.21 | 0.026829979585885066 | 11 |
| MATERIALS | Materials Sector | 52.24 | 53.58 | 0.025650842266462304 | 12 |
| UNITED_KINGDOM | United Kingdom Equities | 48.16 | 49.1 | 0.019518272425249172 | 13 |
| AUSTRALIA | Australia Equities | 29.55 | 30.06 | 0.017258883248730816 | 14 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.35 | 82.56 | 0.014874001229256306 | 15 |
| OIL | Crude Oil | 130.29 | 132.21 | 0.014736357356666119 | 16 |
| BROAD_COMMODITIES | Broad Commodities | 18.21 | 18.47 | 0.014277869302580903 | 17 |
| COMMUNICATIONS | Communication Services Sector | 110.82 | 112.32 | 0.013535462912831697 | 18 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.75 | 118.3 | 0.013276231263383176 | 19 |
| REAL_ESTATE | Real Estate Sector | 44.83 | 45.33 | 0.011153245594468064 | 20 |
| FINANCIALS | Financials Sector | 57.58 | 58.22 | 0.011114970475859742 | 21 |
| ENERGY | Energy Sector | 62.58 | 63.11 | 0.008469159475871013 | 22 |
| EURO | Euro | 106.86 | 107.645 | 0.007346060265768228 | 23 |
| LARGE_VALUE | US Large-Cap Value | 256.62 | 258.32 | 0.006624581092666171 | 24 |
| AGRICULTURE | Agriculture Commodities | 28.14 | 28.3 | 0.005685856432125158 | 25 |
| EUROPE | Europe Equities | 92.1 | 92.61 | 0.005537459283387669 | 26 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.79 | 221.93 | 0.005163277322342674 | 27 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.7 | 106.18 | 0.004541154210028431 | 28 |
| SOFTWARE | Software | 101.99 | 102.45 | 0.004510246102559234 | 29 |
| TIPS | Treasury Inflation-Protected Securities | 106.77 | 107.25 | 0.0044956448440574 | 30 |
| LOW_VOL | US Low Volatility Equities | 75.74 | 76.01 | 0.003564827039873375 | 31 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.25 | 97.55 | 0.0030848329048842604 | 32 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.05 | 93.31 | 0.0027941966684579267 | 33 |
| YEN | Japanese Yen | 57.53 | 57.64 | 0.0019120458891013214 | 34 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.84 | 93.01 | 0.0018311072813441687 | 35 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.7 | 94.85 | 0.0015839493136218241 | 36 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.61 | 79.7 | 0.0011305112423063424 | 37 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.55 | 91.61 | 0.0006553795740034118 | 38 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.65 | 47.68 | 0.0006295907660021083 | 39 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 40 |
| CANADA | Canada Equities | 62.18 | 62.12 | -0.0009649404953361307 | 41 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.56 | 105.41 | -0.0014209928003031669 | 42 |
| COPPER | Copper | 40.13 | 40.07 | -0.0014951407924246318 | 43 |
| METALS_MINING | Metals and Mining | 118.1 | 117.87 | -0.0019475021168500195 | 44 |
| CHINA | China Equities | 55.06 | 54.93 | -0.002361060661096981 | 45 |
| INDIA | India Equities | 49.58 | 49.35 | -0.004638967325534482 | 46 |
| US_DOLLAR | US Dollar | 28.1 | 27.96 | -0.004982206405694023 | 47 |
| EMERGING_MARKETS | Emerging Markets | 60.39 | 59.97 | -0.006954793840039719 | 48 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.69 | 73.06 | -0.00854932826706467 | 49 |
| SMALL_VALUE | US Small-Cap Value | 226.46 | 224.06 | -0.01059789808354683 | 50 |
| SP500 | S&P 500 | 772.67 | 763.47 | -0.011906764854336171 | 51 |
| TOTAL_US_MARKET | Total US Stock Market | 382.13 | 377.07 | -0.013241567005992771 | 52 |
| SMALL_CAP | US Small-Cap Stocks | 304.06 | 297.97 | -0.02002894165625202 | 53 |
| UTILITIES | Utilities Sector | 44.18 | 43.22 | -0.021729289271163466 | 54 |
| BROAD_AI_TECH | Broad AI Technology | 64.0 | 62.3 | -0.026562500000000044 | 55 |
| MID_CAP | US Mid-Cap Stocks | 78.48 | 76.2 | -0.02905198776758411 | 56 |
| NASDAQ100 | Nasdaq 100 | 729.87 | 706.32 | -0.032266019976160076 | 57 |
| LARGE_GROWTH | US Large-Cap Growth | 125.08 | 121.04 | -0.032299328429804874 | 58 |
| JAPAN | Japan Equities | 98.17 | 94.84 | -0.03392074971987369 | 59 |
| REGIONAL_BANKS | Regional Banks | 77.39 | 74.76 | -0.03398371882672169 | 60 |
| INDUSTRIALS | Industrials Sector | 186.32 | 179.0 | -0.0392872477458136 | 61 |
| TAIWAN | Taiwan Equities | 107.8 | 103.33 | -0.041465677179962857 | 62 |
| CYBERSECURITY | Cybersecurity | 97.79 | 93.23 | -0.04663053481951118 | 63 |
| SOLAR | Solar Energy | 50.92 | 48.32 | -0.05106048703849175 | 64 |
| TECHNOLOGY | Technology Sector | 190.32 | 180.05 | -0.0539617486338797 | 65 |
| SOUTH_KOREA | South Korea Equities | 185.1 | 173.64 | -0.061912479740680704 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.47 | 121.83 | -0.06622212002759253 | 67 |
| MOMENTUM | US Momentum Equities | 322.07 | 300.59 | -0.06669357593069836 | 68 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 251.2 | 233.4 | -0.07085987261146487 | 69 |
| SEMICONDUCTORS | Semiconductors | 594.07 | 546.8 | -0.07956974767283331 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SOUTH_AFRICA | 35.0 | 0.046047807596421686 | 0.01611673265874759 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | CHINA | 35.0 | -0.002361060661096981 | -0.0008263712313839433 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | MEXICO | 30.0 | 0.029902549726338323 | 0.008970764917901497 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-4-8 | SP500 | 100.0 | -0.011906764854336171 | -0.011906764854336171 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | AUSTRALIA | 35.0 | 0.017258883248730816 | 0.006040609137055786 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | MEXICO | 35.0 | 0.029902549726338323 | 0.010465892404218413 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SOUTH_AFRICA | 30.0 | 0.046047807596421686 | 0.013814342278926505 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOUTH_AFRICA | 35.0 | 0.046047807596421686 | 0.01611673265874759 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| google-gemini-3-1-pro | AUSTRALIA | 35.0 | 0.017258883248730816 | 0.006040609137055786 | V3 selected model rank 6: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SP500 | 30.0 | -0.011906764854336171 | -0.0035720294563008513 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| openai-gpt-5-6-sol | AUSTRALIA | 35.0 | 0.017258883248730816 | 0.006040609137055786 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SOUTH_AFRICA | 35.0 | 0.046047807596421686 | 0.01611673265874759 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | CHINA | 30.0 | -0.002361060661096981 | -0.0007083181983290942 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | AUSTRALIA | 35.0 | 0.017258883248730816 | 0.006040609137055786 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | UNITED_KINGDOM | 35.0 | 0.019518272425249172 | 0.00683139534883721 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | SOUTH_AFRICA | 30.0 | 0.046047807596421686 | 0.013814342278926505 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | SOUTH_AFRICA | 35.0 | 0.046047807596421686 | 0.01611673265874759 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | CHINA | 35.0 | -0.002361060661096981 | -0.0008263712313839433 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | AUSTRALIA | 30.0 | 0.017258883248730816 | 0.005177664974619245 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | -0.011906764854336171 | -0.011906764854336171 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | AUSTRALIA | 3 | 0.56 | 0.017258883248730816 | 0.030320843820200706 | 0.04222760867453688 | 0.26551248951313267 |  | True | True |
| xai-grok-4-3 | AUSTRALIA | 3 | 0.5633 | 0.017258883248730816 | 0.0266863467648195 | 0.03859311161915567 | 0.2691469865685139 |  | True | True |
| anthropic-claude-fable-5 | SOUTH_AFRICA | 3 | 0.5833 | 0.046047807596421686 | 0.024261126345265144 | 0.036167891199601315 | 0.2715722069880683 |  | True | True |
| openai-gpt-5-6-sol | AUSTRALIA | 3 | 0.5767 | 0.017258883248730816 | 0.02144902359747428 | 0.03335578845181045 | 0.2743843097358591 |  | True | True |
| xai-grok-4-5 | SOUTH_AFRICA | 3 | 0.59 | 0.046047807596421686 | 0.02046802640198289 | 0.03237479125631906 | 0.27536530693135053 |  | True | True |
| google-gemini-3-1-pro | SOUTH_AFRICA | 3 | 0.555 | 0.046047807596421686 | 0.018585312339502523 | 0.030492077193838694 | 0.2772480209938309 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 1 | 0.5 | -0.011906764854336171 | -0.011906764854336171 | 0.0 | 0.30774009818766956 |  | False | False |
| xai-grok-4-6 | SP500 | 1 | 0.5 | -0.011906764854336171 | -0.011906764854336171 | 0.0 | 0.30774009818766956 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | AUSTRALIA | 0.04222760867453688 | 0.23669500000000002 | 0.17840515716232652 |
| anthropic-claude-fable-5 | SOUTH_AFRICA | 0.036167891199601315 | 0.45874000000000004 | 0.07884180843092234 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | ca24953369416a48cfced71a2553b0a47fed5ce8f1f2437280952dc20699d9d3 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | baae37f01f065069195c9deba954dbfabe8db19cb7083de9c93bbef0dbc8732f |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 0675b6d99529ee610b2ac0f7bf61fc6e46bfde8864dbdea1323e7af502aa175a |
| market_data/universe_decision_context.md | dca47afa16d34ccf30d7a8bf374b0f1d0ed7588d41eece76be6187ef39bd1a61 |
| market_data/universe_decision_context.json | 22455f946ba533f17ed3bc7a6c28fb31891e3f097e8e628af3aaf48313e137aa |
| market_data/decision_context_source_history.json | 4b59aad49799ce1393bdfc3f70e7f59d45df01fc7b82bae9241d85aa7817f4b7 |
| market_data/universe_quality_evidence.md | ebfe7db8cd46151df5d52d98abb70504dcd690fb77feec23f468eac54a8e629a |
| market_data/universe_quality_evidence.json | 49ce675f2646c5f3a7eeec693302eb5a5444d6c5d0725c821137df5f16680fae |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | cc00ca8bf34f9e4df0900b306e6cd668d67a5f7723b69d23ba63fbf9fa43a7a7 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | ce87aa06282dbd4593df41e7903037dc0b2b7a240370519fa36fd8edd4efbe9f | yes |
| Final briefing | research/final_briefing.md | model-facing | ca24953369416a48cfced71a2553b0a47fed5ce8f1f2437280952dc20699d9d3 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
