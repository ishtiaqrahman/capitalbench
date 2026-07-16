# CapitalBench Report: CB-2026-06-15-1M / official-20260615-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260615-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-15-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-15
- Decision deadline: 2026-06-16T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-15
- Exit date: 2026-07-15
- Entry rule: Use adjusted close prices on Monday, June 15, 2026 as the post-close entry snapshot.
- Exit rule: Use adjusted close prices on Wednesday, July 15, 2026 as the one-month exit snapshot, calculated after regular trading ends.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | NASDAQ100 | 4 | 0.75 | Overweight US tech and semiconductors for momentum and growth, balanced with broad market exposure and a small gold hedge. | A sudden reversal in tech and AI sentiment could disproportionately impact the portfolio's heavy growth allocation.; Unexpectedly hawkish signals from the upcoming FOMC meeting could drive interest rates higher, pressuring growth stock valuations.; Geopolitical shocks or a resurgence in inflation could trigger a broader market sell-off, negatively affecting the equity-heavy portfolio. |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 4 | 0.55 | Tilt to high-momentum tech and growth factors expected to outperform SP500 over the scoring window given observed market moves and scheduled data releases. | FOMC June 16-17 outcome surprises markets on rates or guidance; June CPI release on July 14 exceeds expectations and pressures growth stocks; Reversal in semiconductor and AI leadership after extended 30d gains |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.6 | Overweight the AI/tech and momentum complex showing the strongest trend and breadth, with a gold hedge against policy or geopolitical surprises within the one-month window. | Hawkish FOMC on June 17 amid sticky 4.2% headline CPI could compress high-multiple growth/semis; Semiconductor and Taiwan concentration amplifies single-theme drawdown risk if AI sentiment reverses; Geopolitical reversal (Hormuz deal collapse) would spike oil and pressure growth equities; July 14 CPI print could reignite inflation/rate fears before exit close |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Pro-risk growth/semis tilt with momentum and Korea leverage to chip cycle; gold hedges inflation/geopolitical reversal. | Hawkish FOMC surprise hitting growth/semis duration; Iran deal unravels, oil spikes, risk-off rotation; Semiconductor momentum unwinds after parabolic run; June CPI reaccelerates on energy base effects |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | Allocate aggressively to semiconductors, Korea, Taiwan, broad AI tech, and momentum to maximize upside if the current risk-on growth trend continues. The construction intentionally accepts high volatility to outperform the S&P 500 over the short scoring window. | A hawkish FOMC message or upside inflation data could raise yields and trigger a sharp reversal in high-valuation growth and semiconductor equities.; Semiconductor and AI trades are crowded after very large trailing gains, increasing drawdown risk from profit-taking or positioning unwind.; South Korea and Taiwan exposures add currency, export-cycle, and regional geopolitical risks that could overwhelm sector momentum.; The reported U.S.-Iran peace progress could reverse or broader geopolitical tensions could flare, hurting global risk appetite.; A disappointing June retail sales, PCE, or CPI print could shift the market toward defensives and away from high-beta momentum. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 136.2709844692 | 156.22000122070312 | 0.14639225532279054 | 1 |
| CYBERSECURITY | Cybersecurity | 86.1957146662 | 93.08999633789062 | 0.07998404211148191 | 2 |
| AGRICULTURE | Agriculture Commodities | 26.38 | 27.979999542236328 | 0.06065199174512248 | 3 |
| FINANCIALS | Financials Sector | 53.3740525536 | 56.560001373291016 | 0.059690967188440025 | 4 |
| ETHEREUM_ETF | Ethereum ETF | 13.76 | 14.520000457763672 | 0.05523259140724357 | 5 |
| REGIONAL_BANKS | Regional Banks | 71.8142861608 | 75.77999877929688 | 0.0552217787087268 | 6 |
| HEALTHCARE | Healthcare Sector | 152.2242830189 | 158.2899932861328 | 0.039847192228060546 | 7 |
| BRAZIL | Brazil Equities | 34.64 | 35.880001068115234 | 0.03579679757838439 | 8 |
| ENERGY | Energy Sector | 55.1573117735 | 56.5 | 0.0243428873403706 | 9 |
| LOW_VOL | US Low Volatility Equities | 74.0607568785 | 75.47000122070312 | 0.019028219553778758 | 10 |
| SMALL_VALUE | US Small-Cap Value | 217.3 | 221.2899932861328 | 0.018361681022240228 | 11 |
| UTILITIES | Utilities Sector | 44.457256027 | 45.220001220703125 | 0.017156821222611862 | 12 |
| BROAD_COMMODITIES | Broad Commodities | 16.89 | 17.170000076293945 | 0.016577861237060176 | 13 |
| LARGE_VALUE | US Large-Cap Value | 243.78 | 247.27999877929688 | 0.014357202310677053 | 14 |
| SOFTWARE | Software | 92.68 | 93.94000244140625 | 0.013595192505462261 | 15 |
| COMMUNICATIONS | Communication Services Sector | 111.8928901366 | 113.37999725341797 | 0.013290452279876686 | 16 |
| UNITED_KINGDOM | United Kingdom Equities | 46.21 | 46.77000045776367 | 0.01211859895614964 | 17 |
| INDUSTRIALS | Industrials Sector | 178.2445910154 | 180.05999755859375 | 0.010184917998644405 | 18 |
| US_DOLLAR | US Dollar | 27.97 | 28.25 | 0.010010725777618967 | 19 |
| CANADA | Canada Equities | 58.93 | 59.4900016784668 | 0.009502828414505338 | 20 |
| AUSTRALIA | Australia Equities | 28.6 | 28.799999237060547 | 0.006992980316802289 | 21 |
| EUROPE | Europe Equities | 88.6655269808 | 89.12000274658203 | 0.005125732415490525 | 22 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.0604295882 | 212.97000122070312 | 0.004289209610059741 | 23 |
| SMALL_CAP | US Small-Cap Stocks | 294.64 | 295.7699890136719 | 0.00383515141756674 | 24 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.2428381746 | 91.52 | 0.003037628277954507 | 25 |
| TOTAL_US_MARKET | Total US Stock Market | 371.4596768133 | 372.42 | 0.0025852689986123334 | 26 |
| SP500 | S&P 500 | 752.9107541219 | 754.81 | 0.002522537854190876 | 27 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.6708344427 | 79.80999755859375 | 0.001746725974030472 | 28 |
| OIL | Crude Oil | 121.21 | 121.37999725341797 | 0.001402501884481211 | 29 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 30 |
| REAL_ESTATE | Real Estate Sector | 44.6037971811 | 44.560001373291016 | -0.0009818851886346236 | 31 |
| DIVIDEND | US Dividend Equities | 32.3723074517 | 32.34000015258789 | -0.0009979918533862264 | 32 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.8826475852 | 106.76000213623047 | -0.0011474776471248616 | 33 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.9691423222 | 93.77999877929688 | -0.002012826106836174 | 34 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.1590555836 | 48.029998779296875 | -0.0026798034707946616 | 35 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.1821183947 | 93.83000183105469 | -0.0037386774649690313 | 36 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.5192473819 | 98.13999938964844 | -0.0038494812164109327 | 37 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 237.4 | 236.4199981689453 | -0.004128061630390478 | 38 |
| TIPS | Treasury Inflation-Protected Securities | 108.6968240742 | 108.06999969482422 | -0.005766722116442802 | 39 |
| JAPAN | Japan Equities | 94.06 | 93.5 | -0.005953646608547802 | 40 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.3090606263 | 95.7300033569336 | -0.006012490056499176 | 41 |
| LARGE_GROWTH | US Large-Cap Growth | 124.36 | 123.58 | -0.006272113219684794 | 42 |
| MID_CAP | US Mid-Cap Stocks | 76.16 | 75.62999725341797 | -0.006959069676759855 | 43 |
| EURO | Euro | 106.8186518581 | 105.80999755859375 | -0.009442679550441868 | 44 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.6079485596 | 107.58000183105469 | -0.009464746753606312 | 45 |
| INDIA | India Equities | 49.26 | 48.720001220703125 | -0.010962216388487045 | 46 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.3299016907 | 117.0 | -0.011238931763639881 | 47 |
| YEN | Japanese Yen | 57.24 | 56.529998779296875 | -0.012403934673359984 | 48 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.4024073013 | 84.23999786376953 | -0.013610968054208139 | 49 |
| CHINA | China Equities | 54.93 | 54.150001525878906 | -0.014199862991463585 | 50 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.0143422776 | 70.81999969482422 | -0.016584787765912545 | 51 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.8868990171 | 83.47000122070312 | -0.016691595673808957 | 52 |
| EMERGING_MARKETS | Emerging Markets | 60.769001167 | 59.47999954223633 | -0.021211499284336632 | 53 |
| BITCOIN_ETF | Bitcoin ETF | 37.74 | 36.810001373291016 | -0.024642252959962585 | 54 |
| COPPER | Copper | 39.65 | 38.630001068115234 | -0.025725067638959986 | 55 |
| MEXICO | Mexico Equities | 77.76 | 75.38999938964844 | -0.03047840291089976 | 56 |
| NASDAQ100 | Nasdaq 100 | 743.1807438129 | 717.74 | -0.034232242997007556 | 57 |
| MATERIALS | Materials Sector | 52.3041956667 | 50.5 | -0.034494281839203556 | 58 |
| TAIWAN | Taiwan Equities | 106.37 | 102.48999786376953 | -0.036476470209932055 | 59 |
| TECHNOLOGY | Technology Sector | 191.5627785305 | 181.5800018310547 | -0.05211229851657162 | 60 |
| SOUTH_AFRICA | South Africa Equities | 67.75 | 63.7400016784668 | -0.05918816710750119 | 61 |
| GOLD | Gold | 81.26 | 76.27999877929688 | -0.06128477997419557 | 62 |
| MOMENTUM | US Momentum Equities | 333.63 | 312.6700134277344 | -0.06282404631557603 | 63 |
| BROAD_AI_TECH | Broad AI Technology | 66.549531604 | 61.119998931884766 | -0.08158633939639759 | 64 |
| SEMICONDUCTORS | Semiconductors | 647.1 | 590.77001953125 | -0.0870498848226704 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 134.69 | 121.5199966430664 | -0.09778011253198893 | 66 |
| SOLAR | Solar Energy | 62.7 | 55.79999923706055 | -0.1100478590580456 | 67 |
| METALS_MINING | Metals and Mining | 120.5461293139 | 103.19999694824219 | -0.14389622018048198 | 68 |
| SILVER | Silver | 63.47 | 52.209999084472656 | -0.17740666323502985 | 69 |
| SOUTH_KOREA | South Korea Equities | 211.45 | 171.63999938964844 | -0.188271461860258 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | -0.0870498848226704 | -0.03046745968793464 | Strong momentum, AI capex cycle, Iran de-escalation lowers tail risk for risk assets. |
| anthropic-claude-opus-4-7 | MOMENTUM | 20.0 | -0.06282404631557603 | -0.012564809263115206 | Momentum factor leadership continues with risk-on tape post-oil drop. |
| anthropic-claude-opus-4-7 | SOUTH_KOREA | 15.0 | -0.188271461860258 | -0.0282407192790387 | Semis-heavy export market with strong trend; benefits from chip cycle. |
| anthropic-claude-opus-4-7 | NASDAQ100 | 20.0 | -0.034232242997007556 | -0.006846448599401512 | Dovish FOMC potential and falling oil support large-cap growth into July. |
| anthropic-claude-opus-4-7 | GOLD | 10.0 | -0.06128477997419557 | -0.006128477997419557 | Hedge versus sticky CPI surprise and geopolitical reversal risk. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.0870498848226704 | -0.026114965446801117 | Strong AI-led momentum and broad participation in the June 15 tech rally; semis leading the leadership cohort with structural demand. |
| anthropic-claude-opus-4-8 | NASDAQ100 | 25.0 | -0.034232242997007556 | -0.008558060749251889 | Mega-cap growth strength with falling VIX and Iran de-escalation easing energy/geopolitical risk; benefits from any dovish FOMC tone. |
| anthropic-claude-opus-4-8 | MOMENTUM | 20.0 | -0.06282404631557603 | -0.012564809263115206 | Momentum factor showing best risk-adjusted trend persistence; captures the rotation into winners with diversification across the leadership cohort. |
| anthropic-claude-opus-4-8 | TAIWAN | 15.0 | -0.036476470209932055 | -0.005471470531489808 | Direct semiconductor supply-chain leverage with strong trailing performance; benefits from same AI demand cycle as SMH. |
| anthropic-claude-opus-4-8 | GOLD | 10.0 | -0.06128477997419557 | -0.006128477997419557 | Hedge against FOMC surprise or renewed geopolitical risk; gold has pulled back, offering a diversifying ballast against the high-beta sleeve. |
| google-gemini-3-1-pro | NASDAQ100 | 40.0 | -0.034232242997007556 | -0.013692897198803023 | Strong momentum in tech and growth sectors, supported by solid economic data and potential for continued AI-driven gains. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | -0.0870498848226704 | -0.026114965446801117 | High beta play on the AI and tech theme, showing exceptional recent performance and strong structural tailwinds. |
| google-gemini-3-1-pro | SP500 | 20.0 | 0.002522537854190876 | 0.0005045075708381752 | Core broad market exposure to capture general equity upside while providing some diversification from pure tech. |
| google-gemini-3-1-pro | GOLD | 10.0 | -0.06128477997419557 | -0.006128477997419557 | Defensive allocation to hedge against potential volatility spikes or unexpected macro shocks during the one-month window. |
| openai-gpt-5-5 | SEMICONDUCTORS | 40.0 | -0.0870498848226704 | -0.03481995392906816 | Strongest AI-linked leadership with exceptional 7-day, 30-day, 6-month, and 1-year momentum; should benefit most if risk appetite and growth leadership persist through the one-month window. |
| openai-gpt-5-5 | SOUTH_KOREA | 25.0 | -0.188271461860258 | -0.0470678654650645 | Extreme recent and longer-term momentum with meaningful semiconductor and export sensitivity, offering high beta to the same global tech cycle that has been leading markets. |
| openai-gpt-5-5 | TAIWAN | 15.0 | -0.036476470209932055 | -0.005471470531489808 | Direct exposure to semiconductor supply-chain leadership and strong recent momentum, while diversifying geographically from US chip equities. |
| openai-gpt-5-5 | BROAD_AI_TECH | 10.0 | -0.08158633939639759 | -0.008158633939639759 | Broader AI technology exposure captures continued AI infrastructure and application enthusiasm with less single-industry concentration than semiconductors alone. |
| openai-gpt-5-5 | MOMENTUM | 10.0 | -0.06282404631557603 | -0.006282404631557603 | US momentum factor has strong 7-day and 30-day performance and can benefit from trend persistence in a low-volatility, risk-on tape. |
| xai-grok-4-3 | SEMICONDUCTORS | 40.0 | -0.0870498848226704 | -0.03481995392906816 | Strong recent 30d return of 16.31% and positioning for continued AI-driven demand into July exit. |
| xai-grok-4-3 | NASDAQ100 | 30.0 | -0.034232242997007556 | -0.010269672899102267 | Captured +3.06% daily move on 6/15 with heavy tech weighting likely to benefit from post-deal risk-on sentiment. |
| xai-grok-4-3 | MOMENTUM | 20.0 | -0.06282404631557603 | -0.012564809263115206 | Leading 30d factor return of 11.86% aligns with trend persistence over the one-month window. |
| xai-grok-4-3 | SMALL_CAP | 10.0 | 0.00383515141756674 | 0.000383515141756674 | 6.14% 30d return and domestic growth sensitivity ahead of FOMC and retail sales data. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | NASDAQ100 | 4 | 0.75 | -0.034232242997007556 | -0.04543183307218552 | -0.047954370926376395 | 0.19182408839497606 |  | False | False |
| xai-grok-4-3 | SEMICONDUCTORS | 4 | 0.55 | -0.0870498848226704 | -0.05727092094952896 | -0.059793458803719834 | 0.2036631762723195 |  | False | False |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.6 | -0.0870498848226704 | -0.058837783988077576 | -0.06136032184226845 | 0.2052300393108681 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.0870498848226704 | -0.0842479148269096 | -0.08677045268110048 | 0.23064017014970015 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | -0.0870498848226704 | -0.10180032849681983 | -0.1043228663510107 | 0.24819258381961037 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 93a5aa93d8d62b80d6a0d1855ed79696cc721ae43680478ba28dbe7e6049efe8 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | 8291de828cbc7d49975cf10094febc458839eddbcb969e528c858d4cd1864a3e |
| market_data/universe_trailing_returns.csv | f07d9d798e3ee06b916cffb63ade54874774ad1ffa41957cda015e109e391b72 |
| market_data/universe_trailing_returns.md | e129c1d066abf520b5d93ef0ac0f83fe0e0d639aed716e712e951831896ab93b |
| market_data/universe_trailing_returns.json | 4e18d9f8438451c7dffd47ae4f347dc3b9e41f6dd1ee7e723634fee0714e1166 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 57818ce9fe8994ce0a1da380125449530c6bbb7b17179982bd2e5b796557831f | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | d277a43be79df78637f5ad94136cec3a0e8a67b62ca86f33bb3b5b29fa43b8c8 | yes |
| Final briefing | research/final_briefing.md | model-facing | 93a5aa93d8d62b80d6a0d1855ed79696cc721ae43680478ba28dbe7e6049efe8 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
