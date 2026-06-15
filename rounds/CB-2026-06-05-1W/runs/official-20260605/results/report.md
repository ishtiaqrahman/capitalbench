# CapitalBench Report: CB-2026-06-05-1W / official-20260605

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260605
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 5 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round scored from the June 5, 2026 adjusted close to the June 12, 2026 adjusted close.
- Decision date: 2026-06-05
- Decision deadline: 2026-06-05T20:35:00Z
- Horizon: one week
- Entry date: 2026-06-05
- Exit date: 2026-06-12
- Entry rule: Use adjusted close on Friday, June 5, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Friday, June 12, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Defensive posture with inflation hedge ahead of CPI/PPI catalysts and Treasury auctions in a high-vol, weakening-sentiment tape. | Cool CPI/PPI prints trigger sharp risk-on rotation into growth/tech, leaving defensive tilt behind SPY; Oil reverses on demand concerns or OPEC surprise, hurting energy overweight; Healthcare-specific drug pricing headlines weigh on XLV; Long-end auction tails spike yields and pressure rate-sensitive defensives |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Tilt defensive and toward inflation winners ahead of in-window CPI/PPI, favoring sectors showing positive recent relative strength versus a falling S&P 500. | A cool CPI/PPI surprise sparks a risk-on rally that lifts growth/tech and leaves defensive tilt underperforming SPY.; Oil reverses sharply on supply news, hurting the energy allocation.; Yields fall, pressuring financials and removing inflation tailwind to energy. |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.55 | Energy, financials, and healthcare positioned for one-week window given high oil, rate backdrop, and upcoming data releases. | Hotter-than-expected CPI on June 10 could pressure equities broadly; PPI release on June 11 may increase volatility in rate-sensitive sectors; Recent equity weakness may extend if risk appetite deteriorates |
| google-gemini-3-1-pro | google | portfolio | SHORT_TREASURY | 3 | 0.65 | A defensive allocation favoring short-term Treasuries, Healthcare, and Energy to navigate potential volatility from upcoming inflation data. | A hotter-than-expected CPI or PPI print could trigger a broad market sell-off, negatively impacting the equity portions of the portfolio.; A sudden drop in oil prices could negatively impact the Energy sector allocation.; Unexpected regulatory news in the Healthcare sector could cause underperformance. |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.58 | Recent data show sticky inflation, elevated rates, and strong oil prices, with CPI, PPI, Treasury auctions, and EIA reports all inside the scoring window. This allocation seeks relative outperformance through oil/energy strength and defensive positioning rather than broad equity beta. | A cooler-than-expected CPI or PPI release could trigger a sharp growth-equity rebound, causing this defensive and energy-heavy portfolio to lag SPY.; Oil could fall on bearish EIA inventory data, demand concerns, or easing supply-risk premium during the week.; The U.S. dollar could weaken if markets price a more dovish Fed path after inflation data or if the ECB decision supports the euro.; Healthcare and low-volatility equities could underperform if the market rally is led by high-beta technology and small caps. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 175.19000244140625 | 197.4499969482 | 0.12706201379407367 | 1 |
| SEMICONDUCTORS | Semiconductors | 569.6900024414062 | 619.9600219727 | 0.08824100706675853 | 2 |
| ETHEREUM_ETF | Ethereum ETF | 11.869999885559082 | 12.5699996948 | 0.058972183318428684 | 3 |
| MOMENTUM | US Momentum Equities | 306.4700012207031 | 324.3999938965 | 0.058504886626357555 | 4 |
| BITCOIN_ETF | Bitcoin ETF | 34.13999938964844 | 36.0400009155 | 0.05565323842471015 | 5 |
| TAIWAN | Taiwan Equities | 98.08000183105469 | 102.6200027466 | 0.046288752353059515 | 6 |
| REGIONAL_BANKS | Regional Banks | 70.16999816894531 | 73.4100036621 | 0.04617365794073214 | 7 |
| MEXICO | Mexico Equities | 75.0999984741211 | 78.4700012207 | 0.04487353948136463 | 8 |
| SMALL_VALUE | US Small-Cap Value | 209.44000244140625 | 218.3300018311 | 0.04244652065538834 | 9 |
| AUSTRALIA | Australia Equities | 28.059999465942383 | 29.2199993134 | 0.041339981095350975 | 10 |
| SMALL_CAP | US Small-Cap Stocks | 281.6499938964844 | 292.950012207 | 0.04012078308323597 | 11 |
| BIOTECH | Biotechnology | 128.6699981689453 | 133.7899932861 | 0.03979167785820659 | 12 |
| SOUTH_AFRICA | South Africa Equities | 64.37000274658203 | 66.8700027466 | 0.038837966340629304 | 13 |
| COPPER | Copper | 38.08000183105469 | 39.5499992371 | 0.03860287120171613 | 14 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.16999816894531 | 71.5500030518 | 0.03440805184122775 | 15 |
| BRAZIL | Brazil Equities | 34.0099983215332 | 35.0999984741 | 0.0320494033037535 | 16 |
| MATERIALS | Materials Sector | 50.630001068115234 | 52.1800003052 | 0.03061424460567297 | 17 |
| EUROPE | Europe Equities | 87.12999725341797 | 89.6200027466 | 0.028578050862779536 | 18 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.44000244140625 | 85.8199996948 | 0.02852345618116492 | 19 |
| MID_CAP | US Mid-Cap Stocks | 73.94999694824219 | 76.0400009155 | 0.028262394232694943 | 20 |
| EMERGING_MARKETS | Emerging Markets | 58.029998779296875 | 59.5499992371 | 0.026193356708210214 | 21 |
| TECHNOLOGY | Technology Sector | 180.3000030517578 | 184.8000030518 | 0.024958402240017552 | 22 |
| LARGE_VALUE | US Large-Cap Value | 236.4199981689453 | 242.1300048828 | 0.024151961585645143 | 23 |
| BROAD_AI_TECH | Broad AI Technology | 62.52000045776367 | 64.0 | 0.023672417328854056 | 24 |
| NASDAQ100 | Nasdaq 100 | 705.0599975585938 | 721.3400268555 | 0.023090275087622292 | 25 |
| JAPAN | Japan Equities | 90.72000122070312 | 92.7099990845 | 0.02193560225992086 | 26 |
| INDIA | India Equities | 47.34000015258789 | 48.3300018311 | 0.02091258291764042 | 27 |
| FINANCIALS | Financials Sector | 52.29999923706055 | 53.3400001526 | 0.0198852950422701 | 28 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 229.4499969482422 | 233.7899932861 | 0.01891478054295548 | 29 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 207.8300018310547 | 211.6499938965 | 0.018380368723427187 | 30 |
| UNITED_KINGDOM | United Kingdom Equities | 46.380001068115234 | 47.1599998474 | 0.016817567083261542 | 31 |
| DIVIDEND | US Dividend Equities | 32.29999923706055 | 32.8199996948 | 0.016099085759197607 | 32 |
| METALS_MINING | Metals and Mining | 118.5999984741211 | 120.4400024414 | 0.015514367545969243 | 33 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.86000061035156 | 116.5999984741 | 0.015148858214367955 | 34 |
| REAL_ESTATE | Real Estate Sector | 44.70000076293945 | 45.3600006104 | 0.014765097006614658 | 35 |
| LOW_VOL | US Low Volatility Equities | 73.47000122070312 | 74.4700012207 | 0.01361099745994121 | 36 |
| CANADA | Canada Equities | 58.029998779296875 | 58.7599983215 | 0.012579692530745978 | 37 |
| INDUSTRIALS | Industrials Sector | 174.17999267578125 | 176.1799926758 | 0.011482375037996206 | 38 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.4000015258789 | 96.3600006104 | 0.010062883324594818 | 39 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.05999755859375 | 85.7699966431 | 0.008347038618442992 | 40 |
| TOTAL_US_MARKET | Total US Stock Market | 363.3800048828125 | 366.3599853516 | 0.008200727692071474 | 41 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.16999816894531 | 109.0100021362 | 0.007765591027770302 | 42 |
| CHINA | China Equities | 54.439998626708984 | 54.8300018311 | 0.007163909151894687 | 43 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.73999786376953 | 94.3799972534 | 0.006827388566410741 | 44 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.43000030517578 | 79.9400024414 | 0.006420774698032927 | 45 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.16999816894531 | 98.7600021362 | 0.006010023207287052 | 46 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.62000274658203 | 94.1800003052 | 0.0059816016042406606 | 47 |
| SP500 | S&P 500 | 737.5499877929688 | 741.75 | 0.005694545829495912 | 48 |
| HEALTHCARE | Healthcare Sector | 153.00999450683594 | 153.8099975586 | 0.0052284365759409646 | 49 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.0099983215332 | 48.2599983215 | 0.005207248671255771 | 50 |
| EURO | Euro | 106.29000091552734 | 106.8300018311 | 0.0050804488749776056 | 51 |
| UTILITIES | Utilities Sector | 44.349998474121094 | 44.5299987793 | 0.00405863159801334 | 52 |
| TIPS | Treasury Inflation-Protected Securities | 109.25 | 109.6100006104 | 0.0032952000951944616 | 53 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.97000122070312 | 107.0500030518 | 0.000747890344806379 | 54 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.44999694824219 | 91.5100021362 | 0.0006561529793354115 | 55 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 56 |
| COMMUNICATIONS | Communication Services Sector | 111.66999816894531 | 111.6500015259 | -0.00017906907292197793 | 57 |
| YEN | Japanese Yen | 57.310001373291016 | 57.2599983215 | -0.0008725013190161723 | 58 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 129.60000610351562 | 129.4100036621 | -0.0014660681517550955 | 59 |
| ENERGY | Energy Sector | 57.66999816894531 | 57.5499992371 | -0.002080786121993139 | 60 |
| US_DOLLAR | US Dollar | 28.020000457763672 | 27.9500007629 | -0.0024982046295533022 | 61 |
| SILVER | Silver | 61.56999969482422 | 61.2900009155 | -0.004547649516193797 | 62 |
| AGRICULTURE | Agriculture Commodities | 26.399999618530273 | 26.2399997711 | -0.006060600369023117 | 63 |
| LARGE_GROWTH | US Large-Cap Growth | 122.69000244140625 | 121.6100006104 | -0.008802688153193516 | 64 |
| CYBERSECURITY | Cybersecurity | 86.69999694824219 | 85.3300018311 | -0.015801559000746424 | 65 |
| SOLAR | Solar Energy | 64.05000305175781 | 63.0299987793 | -0.01592512449427308 | 66 |
| BROAD_COMMODITIES | Broad Commodities | 17.459999084472656 | 17.0599994659 | -0.022909486801083512 | 67 |
| GOLD | Gold | 81.22000122070312 | 79.1900024414 | -0.024993828475659785 | 68 |
| SOFTWARE | Software | 95.8499984741211 | 90.6999969482 | -0.053729802899387336 | 69 |
| OIL | Crude Oil | 133.02000427246094 | 125.4300003052 | -0.057059116850684766 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.0052284365759409646 | 0.0015685309727822892 | Defensive leadership with positive recent momentum amid risk-off tape; low beta into CPI/PPI week. |
| anthropic-claude-opus-4-7 | LOW_VOL | 25.0 | 0.01361099745994121 | 0.0034027493649853024 | Outperforming defensively (+1.7% 7d) amid elevated VIX 21.5 and soft sentiment. |
| anthropic-claude-opus-4-7 | CONSUMER_STAPLES | 15.0 | 0.02852345618116492 | 0.004278518427174738 | Defensive ballast; hot CPI/PPI risk favors staples over discretionary. |
| anthropic-claude-opus-4-7 | ENERGY | 15.0 | -0.002080786121993139 | -0.0003121179182989708 | WTI $90, EIA forecasting inventory draws; sector showing relative strength. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.0006561529793354115 | 9.842294690031173e-05 | Carry with no duration risk ahead of hot CPI/PPI prints and 3/10/30Y auctions. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.0052284365759409646 | 0.0015685309727822892 | Defensive sector with strong recent relative strength (+2.37% 7d while market fell); low beta into hot CPI/PPI prints during the week. |
| anthropic-claude-opus-4-8 | ENERGY | 20.0 | -0.002080786121993139 | -0.00041615722439862783 | Energy leading on firm oil ($90 WTI) and EIA inventory draw forecasts; positive momentum and inflation tailwind ahead of CPI/PPI. |
| anthropic-claude-opus-4-8 | CONSUMER_STAPLES | 15.0 | 0.02852345618116492 | 0.004278518427174738 | Defensive positioning with positive 7d return; cushions against equity drawdown risk into inflation data. |
| anthropic-claude-opus-4-8 | FINANCIALS | 15.0 | 0.0198852950422701 | 0.002982794256340515 | Outperformed broad market recently (+1.40% 7d), supported by strong FDIC bank profits and rising yields/steeper curve. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 20.0 | 0.0006561529793354115 | 0.0001312305958670823 | Cash-like ballast yielding positive carry; protects against hot CPI/PPI selloff and elevated VIX while keeping flexibility. |
| google-gemini-3-1-pro | SHORT_TREASURY | 40.0 | 0.0006561529793354115 | 0.0002624611917341646 | Provides a stable, low-risk yield while avoiding equity market volatility ahead of key inflation data. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.0052284365759409646 | 0.0015685309727822892 | A defensive sector that has shown recent positive momentum and is less sensitive to immediate macroeconomic shocks. |
| google-gemini-3-1-pro | ENERGY | 30.0 | -0.002080786121993139 | -0.0006242358365979416 | Offers exposure to a sector with strong recent performance and potential upside from tight global oil inventories. |
| openai-gpt-5-5 | OIL | 35.0 | -0.057059116850684766 | -0.019970690897739667 | Crude has positive short-term momentum, WTI is elevated, and upcoming EIA reports plus a forecast inventory draw create a near-term catalyst for continued energy commodity strength. |
| openai-gpt-5-5 | ENERGY | 25.0 | -0.002080786121993139 | -0.0005201965304982847 | Energy equities can benefit from high oil prices and inflation persistence while offering better equity-market beta than broad growth sectors if rates stay pressured. |
| openai-gpt-5-5 | US_DOLLAR | 15.0 | -0.0024982046295533022 | -0.0003747306944329953 | Hot inflation data, high Treasury yields, and risk-off conditions around CPI/PPI could support the dollar over the one-week window. |
| openai-gpt-5-5 | HEALTHCARE | 15.0 | 0.0052284365759409646 | 0.0007842654863911446 | Healthcare has recent relative strength and defensive characteristics that may outperform the S&P 500 if inflation data pressures broad equities. |
| openai-gpt-5-5 | LOW_VOL | 10.0 | 0.01361099745994121 | 0.001361099745994121 | Low-volatility equities provide defensive equity exposure and have shown recent resilience during the prior week’s broad market weakness. |
| xai-grok-4-3 | ENERGY | 40.0 | -0.002080786121993139 | -0.0008323144487972557 | Oil at $90+ and positive recent sector returns amid sticky inflation data. |
| xai-grok-4-3 | FINANCIALS | 30.0 | 0.0198852950422701 | 0.00596558851268103 | Resilient to rate environment with recent positive performance and stable labor data. |
| xai-grok-4-3 | HEALTHCARE | 30.0 | 0.0052284365759409646 | 0.0015685309727822892 | Defensive qualities ahead of CPI and PPI releases within the scoring window. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.0052284365759409646 | 0.00903610379354367 | 0.0033415579640477585 | 0.11802591000053 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.0052284365759409646 | 0.008544917027765997 | 0.0028503711982700852 | 0.11851709676630767 |  | True | True |
| xai-grok-4-3 | ENERGY | 3 | 0.55 | -0.002080786121993139 | 0.006701805036666064 | 0.0010072592071701525 | 0.1203602087574076 |  | True | True |
| google-gemini-3-1-pro | SHORT_TREASURY | 3 | 0.65 | 0.0006561529793354115 | 0.0012067563279185122 | -0.004487789501577399 | 0.12585525746615517 |  | False | True |
| openai-gpt-5-5 | OIL | 5 | 0.58 | -0.057059116850684766 | -0.018720252890285678 | -0.02441479871978159 | 0.14578226668435934 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | f8d9bb05eab91cb0136381882864d6eb302ac26bf20d7c95392c40894b806c27 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 03b5e9792d4c6bade89526a62f43cbdf51184fe03753997a0637de246e708b81 |
| manifest.yaml | e6723ee12d24d4583d30b84583c1ff925e89490ef938f3ab7bded36d95dc6ec4 |
| market_data/universe_trailing_returns.csv | 30efc20118b973b5a836953a08852bad01096fd828eed623d3d196aa04324b6a |
| market_data/universe_trailing_returns.md | f3580ea3bf260aa7c674328c329f4602535148cf7de1f0acfb51de3ee610e8c9 |
| market_data/universe_trailing_returns.json | e308b733de0aa6e291b26f72cdd2ffd14a6f4552d59deb8dafb6c3e678751f4b |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a9220eceafde6b728ac0179196d915eaf25b425a7acc9753f4ce25436319b6ef | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c3c1ac7dda4f498830d979eb8dc630e093abb98bc4b179045f67addc0660570e | yes |
| Final briefing | research/final_briefing.md | model-facing | f8d9bb05eab91cb0136381882864d6eb302ac26bf20d7c95392c40894b806c27 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
