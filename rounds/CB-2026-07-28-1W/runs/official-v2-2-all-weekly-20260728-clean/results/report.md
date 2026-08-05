# CapitalBench Report: CB-2026-07-28-1W / official-v2-2-all-weekly-20260728-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260728-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-28-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-28
- Decision deadline: 2026-07-29T12:30:00Z
- Horizon: one week
- Entry date: 2026-07-28
- Exit date: 2026-08-04
- Entry rule: Use the Tuesday, July 28, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Tuesday, August 4, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.62 | Portfolio tilts toward large value, healthcare, and financials for one-week alpha while retaining core SPY exposure. | FOMC outcome surprises rate expectations; Tech earnings after July 29 close pressure broader market; Oil price volatility affects energy-related holdings indirectly |
| openai-gpt-5-6-sol | openai | portfolio | FINANCIALS | 4 | 0.61 | Breadth favored non-mega-cap exposures while SPY faced a dense Fed, inflation, growth, and mega-cap earnings calendar. Diversification across four capped clusters improves the chance of beating a modest SPY base case. | A dovish Fed and strong mega-cap earnings could drive a sharp SPY and growth-stock rebound.; Hot PCE or hawkish FOMC communication could pressure financials, China equities, and credit simultaneously.; Commodity-specific weather or supply news could reverse agriculture's prior relative trend.; Risk-off conditions could widen high-yield spreads and weaken international equities. |
| anthropic-claude-opus-5 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Tilt to financials, healthcare, equal-weight breadth and UK, with a benchmark anchor; avoid semis/AI where volatility and drawdowns are extreme. | Hawkish FOMC (31.5% hike-implied probability) hits all equity exposure; Strong mega-cap earnings spark tech-led rebound, causing defensives to lag SPY; Financials reverse on weak Senior Loan Officer Survey or credit deterioration; Defensive sectors already at 52-week highs and vulnerable to profit-taking; Oil weakness and Hormuz escalation risk creating cross-asset volatility |
| xai-grok-4-5 | xai | portfolio | EQUAL_WEIGHT_SP500 | 4 | 0.58 | SPY base is modest given mixed tech weakness and event risk; selected holdings show superior recent active returns, quality scores or defensive characteristics that support higher one-week expected returns. | FOMC hawkish surprise drives rates higher and compresses equity multiples; Mega-cap earnings miss triggers broad risk-off that hits cyclicals harder; Oil price collapse from de-escalation or demand data reverses energy; GDP/PCE surprise shifts growth narrative against value/equal-weight |
| anthropic-claude-fable-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 4 | 0.6 | Overweight the breadth rotation: equal-weight, value, financials, and healthcare, all with positive recent active returns, low beta, and shallow drawdowns, versus a SPY dragged by weak mega-cap tech into an FOMC and earnings-heavy week. | Blowout Microsoft/Meta/Apple/Amazon earnings reignite mega-cap leadership, causing SPY to beat this low-beta basket; Hawkish FOMC hike hits financials and rate-sensitive value; Rotation into defensives is already extended and could mean-revert within the week; Oil/geopolitical shock (Strait of Hormuz) drives a broad risk-off that favors bonds over any equity tilt |
| openai-gpt-5-5 | openai | portfolio | HEALTHCARE | 4 | 0.56 | Selected holdings all have base forecasts above SPY and span diversified U.S. equity, healthcare, financials, and international equity clusters. No non-benchmark cluster exceeds the 50% cap. | FOMC communication or inflation data could tighten financial conditions and pressure equities broadly.; Mega-cap technology earnings from Microsoft, Meta, Apple, or Amazon could revive SPY leadership and reduce relative alpha.; Recent sector and breadth outperformance could reverse quickly after strong short-term moves.; International exposure could underperform if the U.S. dollar strengthens or global risk appetite deteriorates. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 3 | 0.55 | Tilt toward broadening breadth and defensive strength while avoiding the tech/semiconductor drawdown; all holdings beat SPY base forecast. | FOMC July 29 surprise hawkish shift lifts yields and hits financials; Megacap tech earnings (MSFT, META, AAPL, AMZN) spark risk-on reversal favoring SPY/Nasdaq over defensives; Sharp broad equity selloff drags all holdings |
| google-gemini-3-1-pro | google | portfolio | CONSUMER_STAPLES | 2 | 0.65 | Defensive allocation to Consumer Staples and Healthcare to navigate potential volatility from FOMC and tech earnings. | A dovish FOMC and strong tech earnings could lead to a risk-on rally, causing defensive sectors to underperform.; Sector-specific negative news in Healthcare or Consumer Staples could drag down the portfolio. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 151.45 | 171.13999938964844 | 0.13000990022877823 | 1 |
| SOFTWARE | Software | 91.78 | 102.0 | 0.11135323599912827 | 2 |
| BROAD_AI_TECH | Broad AI Technology | 57.24 | 63.130001068115234 | 0.10290008854149613 | 3 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 113.59 | 124.83000183105469 | 0.09895238868786582 | 4 |
| CYBERSECURITY | Cybersecurity | 89.28 | 97.94000244140625 | 0.09699823523080475 | 5 |
| TECHNOLOGY | Technology Sector | 171.09 | 186.89999389648438 | 0.09240746914772568 | 6 |
| TAIWAN | Taiwan Equities | 93.95 | 102.20999908447266 | 0.08791909616256155 | 7 |
| SEMICONDUCTORS | Semiconductors | 529.6 | 575.7100219726562 | 0.08706575145894302 | 8 |
| SOLAR | Solar Energy | 49.1 | 53.369998931884766 | 0.08696535502820302 | 9 |
| MOMENTUM | US Momentum Equities | 292.32 | 313.3500061035156 | 0.07194172859713888 | 10 |
| NASDAQ100 | Nasdaq 100 | 675.49 | 723.8499755859375 | 0.07159243746900401 | 11 |
| LARGE_GROWTH | US Large-Cap Growth | 116.48 | 124.30000305175781 | 0.0671360152108329 | 12 |
| SOUTH_AFRICA | South Africa Equities | 61.98 | 65.95999908447266 | 0.06421424789404107 | 13 |
| METALS_MINING | Metals and Mining | 101.44 | 107.86000061035156 | 0.0632886495499958 | 14 |
| JAPAN | Japan Equities | 89.83 | 94.61000061035156 | 0.053211628747095174 | 15 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.48 | 118.29000091552734 | 0.05165363545098978 | 16 |
| COPPER | Copper | 38.33 | 40.13999938964844 | 0.047221481597924386 | 17 |
| SILVER | Silver | 51.7 | 53.84000015258789 | 0.04139265285469795 | 18 |
| SP500 | S&P 500 | 740.86 | 771.3300170898438 | 0.0411279014791508 | 19 |
| TOTAL_US_MARKET | Total US Stock Market | 365.99 | 380.82000732421875 | 0.04052025280531901 | 20 |
| EMERGING_MARKETS | Emerging Markets | 57.74 | 60.04999923706055 | 0.04000691439315118 | 21 |
| YEN | Japanese Yen | 56.0 | 58.150001525878906 | 0.03839288439069466 | 22 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.6 | 72.22000122070312 | 0.03764369569975767 | 23 |
| CHINA | China Equities | 54.41 | 56.09000015258789 | 0.030876679885827762 | 24 |
| EUROPE | Europe Equities | 89.23 | 91.83999633789062 | 0.02925021111611148 | 25 |
| SMALL_CAP | US Small-Cap Stocks | 293.37 | 301.7099914550781 | 0.028428235521962497 | 26 |
| AUSTRALIA | Australia Equities | 29.32 | 30.1200008392334 | 0.027285158227605688 | 27 |
| INDIA | India Equities | 49.38 | 50.529998779296875 | 0.023288756162350488 | 28 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 244.98 | 250.64999389648438 | 0.02314472159557668 | 29 |
| COMMUNICATIONS | Communication Services Sector | 109.67 | 112.04000091552734 | 0.021610293749679377 | 30 |
| INDUSTRIALS | Industrials Sector | 182.49 | 186.39999389648438 | 0.0214257981066599 | 31 |
| MID_CAP | US Mid-Cap Stocks | 76.03 | 77.4800033569336 | 0.019071463329390914 | 32 |
| LARGE_VALUE | US Large-Cap Value | 252.04 | 256.6300048828125 | 0.018211414389829095 | 33 |
| ENERGY | Energy Sector | 57.57 | 58.52000045776367 | 0.016501658116443885 | 34 |
| BIOTECH | Biotechnology | 149.78 | 151.8800048828125 | 0.014020596093019755 | 35 |
| REGIONAL_BANKS | Regional Banks | 76.79 | 77.83999633789062 | 0.013673607733957871 | 36 |
| GOLD | Gold | 75.7 | 76.69000244140625 | 0.013077971484890982 | 37 |
| EURO | Euro | 105.028076171875 | 106.37000274658203 | 0.012776836667092839 | 38 |
| SMALL_VALUE | US Small-Cap Value | 224.11 | 226.97000122070312 | 0.012761595737375009 | 39 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 217.69 | 220.22999572753906 | 0.011667948585323495 | 40 |
| UNITED_KINGDOM | United Kingdom Equities | 47.82 | 48.34000015258789 | 0.010874114441403071 | 41 |
| BITCOIN_ETF | Bitcoin ETF | 36.13999938964844 | 36.38999938964844 | 0.0069175430055929965 | 42 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.0370336324 | 79.55000305175781 | 0.006490241293007459 | 43 |
| FINANCIALS | Financials Sector | 57.6 | 57.880001068115234 | 0.004861129654778251 | 44 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.7762972115 | 95.22000122070312 | 0.00468159257385814 | 45 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.3713002078 | 106.76000213623047 | 0.0036541992781053967 | 46 |
| MEXICO | Mexico Equities | 76.78 | 77.05999755859375 | 0.003646751218985944 | 47 |
| CANADA | Canada Equities | 59.84 | 60.0 | 0.002673796791443861 | 48 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.8714221671 | 47.970001220703125 | 0.002059246396712844 | 49 |
| TIPS | Treasury Inflation-Protected Securities | 106.8755022092 | 107.05000305175781 | 0.001632748749252677 | 50 |
| BRAZIL | Brazil Equities | 36.05 | 36.09000015258789 | 0.0011095742742828207 | 51 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.5813167804 | 97.66000366210938 | 0.0008063724112932213 | 52 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3572363921 | 91.41999816894531 | 0.0006869929446633449 | 53 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.7129879845 | 105.76000213623047 | 0.0004447339217898971 | 54 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.2410106691 | 93.25 | 9.640962528711938e-05 | 55 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 56 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.3264315053 | 93.29499816894531 | -0.0003368106531844717 | 57 |
| DIVIDEND | US Dividend Equities | 33.89 | 33.849998474121094 | -0.0011803341953056101 | 58 |
| AGRICULTURE | Agriculture Commodities | 27.84 | 27.65999984741211 | -0.006465522722266193 | 59 |
| MATERIALS | Materials Sector | 52.34 | 52.0 | -0.006495987772258349 | 60 |
| BROAD_COMMODITIES | Broad Commodities | 17.06 | 16.899999618530273 | -0.009378685900921724 | 61 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.9026600605 | 82.81999969482422 | -0.012903766875747458 | 62 |
| US_DOLLAR | US Dollar | 28.579999923706055 | 28.15999984741211 | -0.014695594031320147 | 63 |
| REAL_ESTATE | Real Estate Sector | 46.01 | 45.16999816894531 | -0.01825694047065174 | 64 |
| CONSUMER_STAPLES | Consumer Staples Sector | 87.06 | 85.37000274658203 | -0.019411868291040357 | 65 |
| LOW_VOL | US Low Volatility Equities | 77.97 | 76.38999938964844 | -0.020264212009126092 | 66 |
| ETHEREUM_ETF | Ethereum ETF | 14.489999771118164 | 14.149999618530273 | -0.02346446914827338 | 67 |
| HEALTHCARE | Healthcare Sector | 167.26 | 162.10000610351562 | -0.030850136891572233 | 68 |
| UTILITIES | Utilities Sector | 45.52 | 44.11000061035156 | -0.030975382022153775 | 69 |
| OIL | Crude Oil | 120.48999786376953 | 115.77999877929688 | -0.0390903740391626 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.011667948585323495 | 0.002916987146330874 | Broad rotation from mega-cap tech into the average stock; RSP beat SPY by 3.31% over 5 sessions with breadth improving and at 52-week high. |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.018211414389829095 | 0.004552853597457274 | Value at 52-week high with low 9.09% volatility, +2.85% 5-session active return, benefits from tech drawdown rotation. |
| anthropic-claude-fable-5 | FINANCIALS | 25.0 | 0.004861129654778251 | 0.0012152824136945628 | Only sector with both positive prior trend (+2.10%) and strong recent active return (+3.65%), at 52-week high, low beta cushions FOMC risk. |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | -0.030850136891572233 | -0.007712534222893058 | Defensive sector with +5.37% 5-session active return, at 52-week high, near-zero SPY beta provides ballast into event-heavy week. |
| anthropic-claude-opus-4-8 | FINANCIALS | 35.0 | 0.004861129654778251 | 0.0017013953791723878 | Strong prior active rank, positive recent trend, low drawdown, defensive to tech selloff, Chevron/Exxon earnings and broadening breadth support financials. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 35.0 | 0.011667948585323495 | 0.004083782004863223 | RSP has strongly outperformed SPY (rsp_minus_spy 3.31% over 5s) as breadth broadens away from megacap tech; low volatility and shallow drawdown. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | -0.030850136891572233 | -0.00925504106747167 | Healthcare posted +5.37% active return with low beta and defensive characteristics, benefiting during tech drawdown. |
| anthropic-claude-opus-5 | FINANCIALS | 25.0 | 0.004861129654778251 | 0.0012152824136945628 | Positive prior active trend (+2.10%), at 52w high, low beta and low drawdown; benefits from steep-curve/loan-survey week. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | -0.030850136891572233 | -0.006170027378314447 | Defensive sector at 52-week high with strong recent relative strength and near-zero SPY beta; hedges mega-cap earnings risk. |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.011667948585323495 | 0.002916987146330874 | Breadth is broadening (RSP +3.31% vs SPY over 5 sessions, low vol, shallow drawdown) while mega-cap tech corrects. |
| anthropic-claude-opus-5 | UNITED_KINGDOM | 15.0 | 0.010874114441403071 | 0.0016311171662104606 | Positive prior active trend, near 52w high, low volatility, defensive/dividend tilt; diversifies away from US tech risk. |
| anthropic-claude-opus-5 | SP500 | 15.0 | 0.0411279014791508 | 0.006169185221872619 | Benchmark anchor to limit tracking error in a heavy event week. |
| google-gemini-3-1-pro | CONSUMER_STAPLES | 50.0 | -0.019411868291040357 | -0.009705934145520179 | Defensive positioning ahead of FOMC and tech earnings, supported by strong recent relative performance. |
| google-gemini-3-1-pro | HEALTHCARE | 50.0 | -0.030850136891572233 | -0.015425068445786116 | Defensive sector with strong recent active return, providing stability during a potentially volatile week. |
| openai-gpt-5-5 | HEALTHCARE | 30.0 | -0.030850136891572233 | -0.00925504106747167 | Healthcare showed strong short-term relative strength, a new 52-week high, and low market correlation, making it a plausible one-week defensive leadership holding around heavy macro and earnings events. |
| openai-gpt-5-5 | FINANCIALS | 25.0 | 0.004861129654778251 | 0.0012152824136945628 | Financials combine positive prior active return, recent active strength, and a 52-week high, with scheduled macro and credit data that can reinforce the rotation if rates and growth data are not adverse. |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.011667948585323495 | 0.002916987146330874 | Equal-weight S&P 500 benefits from the supplied breadth evidence: most U.S. stocks rose and RSP outperformed SPY over both 5-day and 21-day windows. |
| openai-gpt-5-5 | UNITED_KINGDOM | 20.0 | 0.010874114441403071 | 0.0021748228882806143 | UK equities have recent active strength, near-high price positioning, and less dependence on U.S. mega-cap technology earnings than SPY. |
| openai-gpt-5-6-sol | FINANCIALS | 30.0 | 0.004861129654778251 | 0.0014583388964334754 | Positive prior and recent active returns, a high prior-active rank, and upcoming Fed and lending data support continued relative strength. |
| openai-gpt-5-6-sol | CHINA | 25.0 | 0.030876679885827762 | 0.007719169971456941 | Positive prior and recent active returns plus reported GDP growth provide independent support for continuation outside U.S. event concentration. |
| openai-gpt-5-6-sol | AGRICULTURE | 25.0 | -0.006465522722266193 | -0.0016163806805665482 | Positive prior active trend, low equity correlation, and a high quality score offer differentiated one-week return potential. |
| openai-gpt-5-6-sol | HIGH_YIELD_CREDIT | 20.0 | 0.006490241293007459 | 0.001298048258601492 | Very low volatility and shallow drawdown provide a steadier expression of benign credit conditions around a dense macro calendar. |
| xai-grok-4-3 | SP500 | 40.0 | 0.0411279014791508 | 0.01645116059166032 | Broad market exposure with stable recent breadth and FOMC clarity expected. |
| xai-grok-4-3 | LARGE_VALUE | 20.0 | 0.018211414389829095 | 0.003642282877965819 | Strong recent active return and high quality evidence score support outperformance. |
| xai-grok-4-3 | HEALTHCARE | 20.0 | -0.030850136891572233 | -0.006170027378314447 | Positive active return and defensive characteristics amid policy events. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.004861129654778251 | 0.0009722259309556503 | Highest prior active rank and positive recent performance in value tilt. |
| xai-grok-4-5 | EQUAL_WEIGHT_SP500 | 30.0 | 0.011667948585323495 | 0.0035003845755970484 | Recent breadth and equal-weight outperformance versus cap-weighted SPY supports higher base return into data and earnings week. |
| xai-grok-4-5 | FINANCIALS | 25.0 | 0.004861129654778251 | 0.0012152824136945628 | Strong prior active trend, shallow drawdown, and quality score support continuation if rates stabilize post-FOMC. |
| xai-grok-4-5 | HEALTHCARE | 20.0 | -0.030850136891572233 | -0.006170027378314447 | Defensive relative strength, zero distance to 52w high, and positive active returns favor outperformance in uncertain macro week. |
| xai-grok-4-5 | ENERGY | 25.0 | 0.016501658116443885 | 0.004125414529110971 | Highest quality evidence score among cyclicals plus prior active strength; oil volatility creates asymmetric upside if geopolitics stabilize. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 4 | 0.62 | 0.0411279014791508 | 0.014895642022267341 | -0.026232259456883456 | 0.11511425820651089 |  | False | True |
| openai-gpt-5-6-sol | FINANCIALS | 4 | 0.61 | 0.004861129654778251 | 0.00885917644592536 | -0.032268725033225434 | 0.12115072378285287 |  | False | True |
| anthropic-claude-opus-5 | FINANCIALS | 5 | 0.55 | 0.004861129654778251 | 0.005762544569794069 | -0.03536535690935673 | 0.12424735565898416 |  | False | True |
| xai-grok-4-5 | EQUAL_WEIGHT_SP500 | 4 | 0.58 | 0.011667948585323495 | 0.0026710541400881346 | -0.03845684733906266 | 0.1273388460886901 |  | False | True |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 4 | 0.6 | 0.011667948585323495 | 0.0009725889345896521 | -0.040155312544561145 | 0.12903731129418858 |  | False | True |
| openai-gpt-5-5 | HEALTHCARE | 4 | 0.56 | -0.030850136891572233 | -0.0029479486191656182 | -0.04407585009831642 | 0.13295784884794384 |  | False | False |
| anthropic-claude-opus-4-8 | FINANCIALS | 3 | 0.55 | 0.004861129654778251 | -0.0034698636834360587 | -0.04459776516258686 | 0.13347976391221428 |  | False | False |
| google-gemini-3-1-pro | CONSUMER_STAPLES | 2 | 0.65 | -0.019411868291040357 | -0.025131002591306295 | -0.06625890407045709 | 0.15514090282008453 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | b01a48d5cd37b282bf3e1dcef75b6e9c7043fe7db85c1b2ccd4540072ea9c3ba |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | fa8192f0bc0e493ef24cb90e403b5ff2cdb716e1a66c58c727a485a15cac2fa6 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 4af2e30e221b7c4c0184353a22fd61d9f1206853423010eae4b93037457945a5 |
| market_data/universe_decision_context.md | c4b8f5b846ac27e8231c9c067e5159a2d94277d72ddae73330bd1037de7f1b0e |
| market_data/universe_decision_context.json | 0a71127b239120d3beb40ae828a64c5d76f0ce87610e87599ef229f6d1f0a8f9 |
| market_data/decision_context_source_history.json | 609c57e3cb31240686967a91daaedef0223ecef60c44c692f4e9559bd7339517 |
| market_data/universe_quality_evidence.md | d93e1db53f3595444fc5cdca67d1a2247c8689dadec1a931b8003d687a965eec |
| market_data/universe_quality_evidence.json | 16a5dbc24fe5a847a14a0b106afe322fd23f3689772e0bacda368d7a9bcc01a0 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | ed6ea0b7ff799e1cff045040a07a94413758164538ddbe7131eb04a772a62384 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 78ce9ddd530ed361bdb23c7569868b56b7a48552ba783111fec7053a9939e7d2 | yes |
| Final briefing | research/final_briefing.md | model-facing | b01a48d5cd37b282bf3e1dcef75b6e9c7043fe7db85c1b2ccd4540072ea9c3ba | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
