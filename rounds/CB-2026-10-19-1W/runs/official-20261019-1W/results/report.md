# CapitalBench Report: CB-2026-10-19-1W / official-20261019-1W

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20261019-1W
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-19-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-10-19
- Decision deadline: 2026-10-19T13:25:00Z
- Horizon: one week
- Entry date: 2026-10-19
- Exit date: 2026-10-26
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-6-astra | openai | portfolio | SP500 | 2 | 0.56 | Five-session active-return dispersion of 4.27% and equal-weight outperformance of 2.46 points indicate substantial rotation rather than uniform liquidation. Inflation and the September rate increase provide a substantive reason for growth-stock repricing, limiting blanket reversal bets. Cybersecurity offers the strongest selective dislocation case, while energy and defensive exposures have independent macro support. Major scheduled national releases and the FOMC decision occur after the exit; anticipation can still affect prices. | Persistent inflation or higher yields could extend technology repricing and invalidate the cybersecurity reversal.; High-volume cybersecurity selling could reflect information absent from the briefing rather than temporary liquidation.; Any rebound before the October 19 entry close is unavailable to the scored holding period.; Oil and defensive sectors could unwind sharply if risk appetite recovers.; Positioning ahead of the post-exit FOMC meeting could dominate the limited scheduled information within the holding window. |
| anthropic-claude-opus-5-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.555 | The past week saw a sharp tech-led selloff: SPY fell 1.97% while RSP rose 0.49%, and 68 of 75 tech constituents fell on Oct 16. The 10-year yield sits near 5.09%, CPI ran hot at 0.6% m/m, and PPI rose 1.3% m/m. Active-return dispersion of 4.27% is high. The FOMC falls after the exit and few major catalysts land inside the window. Prior-trend tech leaders that pulled back hard offer a modest reversal case, but the rate and inflation backdrop limits conviction. | Further rise in yields above 5.1% compresses growth multiples; Continued tech de-rating or a factor rotation into value; High-beta semiconductor exposure amplifies any market drawdown; Event surprises inside the window (earnings, data) ahead of the FOMC |
| anthropic-claude-fable-5-1 | anthropic | portfolio | CYBERSECURITY | 3 | 0.5633 | Hot inflation prints (CPI 3.7% y/y, PPI 6.3% y/y), a 10-year near 5.09%, and a hiking Fed drove a sharp one-week rotation out of mega-cap tech and momentum into defensives, value and equal weight (RSP beat SPY by 2.46% in 5 sessions). Active-return dispersion of 4.27% is elevated. Tech-heavy groups with strong prior 16-session trends (semis, cyber, software) took 8%+ hits in one week with no in-briefing fundamental catalyst, which looks like a factor-crowding unwind rather than earnings deterioration; a partial mean reversion over one week is plausible but rates remain a headwind. Oil and staples strength lacks fresh catalysts inside the window. | Continued rate pressure after hot CPI/PPI keeps long-duration tech under pressure, extending the unwind into another week; Mega-cap tech earnings or AI-capex news inside the window could reprice semis and cyber sharply in either direction; High beta (1.5-2.3) of top picks means a further broad market decline would widen underperformance versus SPY; Defensive rotation into staples/value could persist, making the reversal call early |
| xai-grok-4-5 | xai | portfolio | CYBERSECURITY | 3 | 0.5633 | Recent tech/growth shock after hot CPI/PPI and higher rates; equal-weight outperforming cap-weight; defensive and oil strength; high-vol laggards may bounce but macro data risk remains inside the week. | October 20-21 employment/earnings data could extend growth selloff; Hot September CPI/PPI and 5.09% 10y yield keep duration/growth pressure; High-beta semis/cyber/Korea remain vulnerable to further risk-off; Oil/staples continuation could keep outperforming if inflation narrative persists |
| xai-grok-4-6 | xai | portfolio | CYBERSECURITY | 3 | 0.5633 | Hot September CPI/PPI and a 5.09% 10-year coexist with a concentrated growth/tech shock while equal-weight and defensives outperformed; one-week path is mixed mean-reversion in high-quality pullbacks versus continuation in oil/staples, not a clean trend. | Further inflation follow-through from 0.6% CPI and 1.3% PPI can extend the growth selloff into the October 26 close; State employment and weekly earnings releases October 20–21 can reprice rates before exit; Oil and staples already sit near 52-week highs, so continuation names can reverse if energy prices fade; Korea/semiconductor betas above 2 can dominate weekly tracking error if Asia risk persists |
| google-gemini-4-argon | google | portfolio | CYBERSECURITY | 3 | 0.6 | Cross-sectional active return dispersion is high at 4.27% following a sharp rotation out of technology and growth equities (68 of 75 S&P 500 tech constituents fell on Oct 16) triggered by hot September CPI (+0.6% MoM) and PPI (+1.3% MoM) prints and a 10-year Treasury yield near 5.09%. With major macro catalysts (FOMC, Q3 GDP, PCE) falling after the October 26 weekly exit and Treasury yields stabilizing on Friday, high-quality secular leaders experiencing volume-dislocated pullbacks are positioned for short-term mean reversion. | Renewed upward pressure on the 10-year Treasury yield above 5.10% following hot September CPI (+0.6% MoM) and PPI (+1.3% MoM) prints could extend valuation compression in high-beta growth and tech.; Pre-FOMC positioning ahead of the October 27-28 policy meeting could sustain defensive rotation into low-beta and energy assets through the October 26 exit.; Correlated factor exposure across CIBR, SMH, and IWF increases portfolio sensitivity to broad technology sentiment and mega-cap earnings announcements. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| CYBERSECURITY | Cybersecurity | 99.92 | 108.43 | 0.08516813450760607 | 1 |
| SOFTWARE | Software | 105.99 | 111.39 | 0.050948202660628494 | 2 |
| REGIONAL_BANKS | Regional Banks | 69.26 | 72.73 | 0.050101068437770735 | 3 |
| OIL | Crude Oil | 160.80999755859375 | 166.22999572753906 | 0.033704360743929795 | 4 |
| DIVIDEND | US Dividend Equities | 34.24 | 35.3 | 0.030957943925233433 | 5 |
| UTILITIES | Utilities Sector | 41.36 | 42.55 | 0.028771760154738812 | 6 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 79.46 | 81.68 | 0.027938585451799725 | 7 |
| SMALL_VALUE | US Small-Cap Value | 207.85 | 213.52 | 0.027279287948039466 | 8 |
| ENERGY | Energy Sector | 67.8 | 69.64 | 0.027138643067846635 | 9 |
| REAL_ESTATE | Real Estate Sector | 41.67 | 42.8 | 0.02711783057355399 | 10 |
| LOW_VOL | US Low Volatility Equities | 73.57 | 75.52 | 0.02650536903629197 | 11 |
| SMALL_CAP | US Small-Cap Stocks | 271.28 | 276.99 | 0.021048363314656537 | 12 |
| HEALTHCARE | Healthcare Sector | 175.65 | 179.28 | 0.020666097352689983 | 13 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.4 | 217.29 | 0.018228678537956844 | 14 |
| BIOTECH | Biotechnology | 147.86 | 150.47 | 0.01765183281482474 | 15 |
| FINANCIALS | Financials Sector | 55.06 | 56.02 | 0.017435524881946884 | 16 |
| MUNICIPAL_BONDS | Municipal Bonds | 102.33999633789062 | 103.81999969482422 | 0.01446163191219152 | 17 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 90.22000122070312 | 91.5199966430664 | 0.014409170968454399 | 18 |
| AUSTRALIA | Australia Equities | 28.829999923706055 | 29.170000076293945 | 0.011793276222256122 | 19 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 90.08 | 91.12 | 0.011545293072824148 | 20 |
| LARGE_VALUE | US Large-Cap Value | 255.43 | 258.35 | 0.011431703402106308 | 21 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 102.88 | 104.02 | 0.011080870917573815 | 22 |
| TIPS | Treasury Inflation-Protected Securities | 105.26 | 106.31 | 0.009975299258977666 | 23 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.11 | 96.05 | 0.009883293029124163 | 24 |
| CANADA | Canada Equities | 60.28 | 60.86 | 0.009621765096217594 | 25 |
| CONSUMER_STAPLES | Consumer Staples Sector | 87.21 | 87.96 | 0.00859993120055047 | 26 |
| MATERIALS | Materials Sector | 50.95 | 51.38 | 0.008439646712463222 | 27 |
| YEN | Japanese Yen | 57.790000915527344 | 58.2400016784668 | 0.007786827406305541 | 28 |
| MID_CAP | US Mid-Cap Stocks | 72.38 | 72.91 | 0.00732246476927334 | 29 |
| UNITED_KINGDOM | United Kingdom Equities | 47.34 | 47.61 | 0.005703422053231932 | 30 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 76.83 | 77.2 | 0.004815827150852492 | 31 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 91.08999633789062 | 91.5 | 0.004501083308736886 | 32 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.029998779296875 | 47.2400016784668 | 0.004465296717429901 | 33 |
| BROAD_COMMODITIES | Broad Commodities | 20.07 | 20.15 | 0.003986048829098143 | 34 |
| TECHNOLOGY | Technology Sector | 185.96 | 186.32 | 0.0019359001935899123 | 35 |
| INDUSTRIALS | Industrials Sector | 166.68 | 166.96 | 0.0016798656107510634 | 36 |
| EUROPE | Europe Equities | 86.43 | 86.55 | 0.0013884068031932983 | 37 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 113.51 | 113.63 | 0.0010571755792441184 | 38 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.57 | 91.64 | 0.0007644425030033375 | 39 |
| US_DOLLAR | US Dollar | 29.0 | 29.010000228881836 | 0.0003448354786839136 | 40 |
| TOTAL_US_MARKET | Total US Stock Market | 375.54 | 375.59 | 0.00013314160941568787 | 41 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 42 |
| BROAD_AI_TECH | Broad AI Technology | 62.96 | 62.94 | -0.00031766200762395336 | 43 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.36 | 69.33 | -0.0004325259515570723 | 44 |
| MEXICO | Mexico Equities | 75.36000061035156 | 75.30000305175781 | -0.0007961459409211447 | 45 |
| SP500 | S&P 500 | 766.48 | 765.37 | -0.001448178686984658 | 46 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.46 | 114.26 | -0.0017473353136465697 | 47 |
| EURO | Euro | 103.4800033569336 | 103.19000244140625 | -0.002802482664472361 | 48 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 207.755 | 207.16 | -0.0028639503261053134 | 49 |
| MOMENTUM | US Momentum Equities | 295.71 | 294.56 | -0.0038889452504141664 | 50 |
| COPPER | Copper | 39.56999969482422 | 39.38999938964844 | -0.004548908429719445 | 51 |
| JAPAN | Japan Equities | 94.99 | 94.28 | -0.00747447099694698 | 52 |
| NASDAQ100 | Nasdaq 100 | 718.36 | 712.2 | -0.008575087699760564 | 53 |
| SEMICONDUCTORS | Semiconductors | 548.46 | 541.62 | -0.01247128322940605 | 54 |
| SOLAR | Solar Energy | 41.31 | 40.76 | -0.013313967562333717 | 55 |
| LARGE_GROWTH | US Large-Cap Growth | 122.61 | 120.89 | -0.014028219557947974 | 56 |
| TAIWAN | Taiwan Equities | 107.26000213623047 | 105.61000061035156 | -0.015383194974984638 | 57 |
| INDIA | India Equities | 47.4 | 46.59 | -0.017088607594936578 | 58 |
| SOUTH_AFRICA | South Africa Equities | 64.61000061035156 | 63.4900016784668 | -0.017334761202669302 | 59 |
| AGRICULTURE | Agriculture Commodities | 28.200000762939453 | 27.600000381469727 | -0.021276608696346178 | 60 |
| BITCOIN_ETF | Bitcoin ETF | 46.29999923706055 | 45.220001220703125 | -0.023326091450406428 | 61 |
| SOUTH_KOREA | South Korea Equities | 156.5800018310547 | 152.72000122070312 | -0.0246519387227776 | 62 |
| EMERGING_MARKETS | Emerging Markets | 58.03 | 56.5 | -0.026365672927796013 | 63 |
| GOLD | Gold | 77.85 | 75.42 | -0.03121387283236987 | 64 |
| ETHEREUM_ETF | Ethereum ETF | 54.11000061035156 | 52.34000015258789 | -0.0327111520568909 | 65 |
| CHINA | China Equities | 50.87 | 49.12 | -0.034401415372518174 | 66 |
| METALS_MINING | Metals and Mining | 101.37 | 96.01 | -0.052875604222156425 | 67 |
| SILVER | Silver | 51.540000915527344 | 48.65999984741211 | -0.055878948718597776 | 68 |
| COMMUNICATIONS | Communication Services Sector | 110.09 | 103.85 | -0.05668089744754301 | 69 |
| BRAZIL | Brazil Equities | 41.93000030517578 | 34.150001525878906 | -0.1855473103427696 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | CYBERSECURITY | 35.0 | 0.08516813450760607 | 0.029808847077662123 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 35.0 | -0.01247128322940605 | -0.004364949130292117 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | MOMENTUM | 30.0 | -0.0038889452504141664 | -0.0011666835751242498 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | CYBERSECURITY | 35.0 | 0.08516813450760607 | 0.029808847077662123 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SEMICONDUCTORS | 35.0 | -0.01247128322940605 | -0.004364949130292117 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 30.0 | -0.001448178686984658 | -0.0004344536060953974 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-4-argon | CYBERSECURITY | 35.0 | 0.08516813450760607 | 0.029808847077662123 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| google-gemini-4-argon | SEMICONDUCTORS | 35.0 | -0.01247128322940605 | -0.004364949130292117 | V3 selected model rank 2: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-4-argon | LARGE_GROWTH | 30.0 | -0.014028219557947974 | -0.004208465867384392 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-6-astra | CYBERSECURITY | 35.0 | 0.08516813450760607 | 0.029808847077662123 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 65.0 | -0.001448178686984658 | -0.0009413161465400277 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | 0.08516813450760607 | 0.029808847077662123 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SEMICONDUCTORS | 35.0 | -0.01247128322940605 | -0.004364949130292117 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-5 | MOMENTUM | 30.0 | -0.0038889452504141664 | -0.0011666835751242498 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | 0.08516813450760607 | 0.029808847077662123 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | SEMICONDUCTORS | 35.0 | -0.01247128322940605 | -0.004364949130292117 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | MOMENTUM | 30.0 | -0.0038889452504141664 | -0.0011666835751242498 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-6-astra | SP500 | 2 | 0.56 | -0.001448178686984658 | 0.028867530931122095 | 0.030315709618106753 | 0.056300603576483976 |  | True | True |
| anthropic-claude-opus-5-5 | CYBERSECURITY | 3 | 0.555 | 0.08516813450760607 | 0.025009444341274608 | 0.026457623028259266 | 0.06015869016633146 |  | True | True |
| anthropic-claude-fable-5-1 | CYBERSECURITY | 3 | 0.5633 | 0.08516813450760607 | 0.024277214372245757 | 0.025725393059230415 | 0.06089092013536032 |  | True | True |
| xai-grok-4-5 | CYBERSECURITY | 3 | 0.5633 | 0.08516813450760607 | 0.024277214372245757 | 0.025725393059230415 | 0.06089092013536032 |  | True | True |
| xai-grok-4-6 | CYBERSECURITY | 3 | 0.5633 | 0.08516813450760607 | 0.024277214372245757 | 0.025725393059230415 | 0.06089092013536032 |  | True | True |
| google-gemini-4-argon | CYBERSECURITY | 3 | 0.6 | 0.08516813450760607 | 0.021235432079985614 | 0.022683610766970272 | 0.06393270242762046 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | df536fd4144e3ce2b63e5b81f1b8c554764bcab03afe9532c3c13b31a33d9bd1 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 4fbc2566f9a18731bd47264ad404fa2e9d45f72aa63c0818df76a155b814f8cc |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 7ab2277359f7a101a9cdeab193708f8e4b67be2e74b662fadda0a8b0ee813b57 |
| market_data/universe_decision_context.md | 65daecf1fb3b2f7729591ff1bc38dcd5022893dba2fd23a7f360d8c05459f49e |
| market_data/universe_decision_context.json | 0f769aaffe49b5d7028a815a0255a56fcb9ec0022ad4eb637b44af3cd42f6c64 |
| market_data/decision_context_source_history.json | c2a0b9871f7d43fc310a3450c395bd408d8dc0de99f9baf851b9ec0fb0d7df92 |
| market_data/universe_quality_evidence.md | e6546634aaf030978f6abf533f41b8a8ebad8bf10c478ac61e91e02cb7313c53 |
| market_data/universe_quality_evidence.json | a34f5ac6b83946c9026bdf00189d3ea052cc8f082effa945833a5ca79c9f2014 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 3bfc868f4f4c590332c038354383f7c9ae28cadc5a8127b7920f5c74f43dafa9 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 1050489e659d549c0f9255a4a9a3edd263cbf6414244f78aeb34615ddcd16188 | yes |
| Final briefing | research/final_briefing.md | model-facing | df536fd4144e3ce2b63e5b81f1b8c554764bcab03afe9532c3c13b31a33d9bd1 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
