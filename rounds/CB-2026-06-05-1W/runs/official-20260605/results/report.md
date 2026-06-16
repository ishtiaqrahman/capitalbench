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
| SOUTH_KOREA | South Korea Equities | 175.19 | 197.45 | 0.12706204692048617 | 1 |
| SEMICONDUCTORS | Semiconductors | 569.69 | 619.96 | 0.08824097316084178 | 2 |
| ETHEREUM_ETF | Ethereum ETF | 11.87 | 12.57 | 0.05897219882055604 | 3 |
| MOMENTUM | US Momentum Equities | 306.1414469034 | 324.0522249338 | 0.058504910757972706 | 4 |
| BITCOIN_ETF | Bitcoin ETF | 34.14 | 36.04 | 0.05565319273579372 | 5 |
| TAIWAN | Taiwan Equities | 98.08 | 102.62 | 0.046288743882545 | 6 |
| REGIONAL_BANKS | Regional Banks | 70.17 | 73.41 | 0.046173578452330055 | 7 |
| MEXICO | Mexico Equities | 74.0169687875 | 77.3383693842 | 0.04487350199703011 | 8 |
| SMALL_VALUE | US Small-Cap Value | 208.6861177981 | 217.5441181191 | 0.04244652406428839 | 9 |
| AUSTRALIA | Australia Equities | 27.6682905302 | 28.8120972663 | 0.0413399857447474 | 10 |
| SMALL_CAP | US Small-Cap Stocks | 280.9871092193 | 292.2605135658 | 0.040120717202373646 | 11 |
| BIOTECH | Biotechnology | 128.67 | 133.79 | 0.03979171524053782 | 12 |
| SOUTH_AFRICA | South Africa Equities | 63.035508056 | 65.4836791006 | 0.038837967997736644 | 13 |
| COPPER | Copper | 38.08 | 39.55 | 0.03860294117647056 | 14 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.17 | 71.55 | 0.03440798033829684 | 15 |
| BRAZIL | Brazil Equities | 33.6883848479 | 34.7680772761 | 0.03204939723512168 | 16 |
| MATERIALS | Materials Sector | 50.63 | 52.18 | 0.03061426031996839 | 17 |
| EUROPE | Europe Equities | 87.13 | 89.62 | 0.02857798691610247 | 18 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.44 | 85.82 | 0.028523489932885893 | 19 |
| MID_CAP | US Mid-Cap Stocks | 73.766455576 | 75.8512681812 | 0.028262339418654303 | 20 |
| EMERGING_MARKETS | Emerging Markets | 58.03 | 59.55 | 0.02619334826813713 | 21 |
| TECHNOLOGY | Technology Sector | 180.3 | 184.8 | 0.024958402662229595 | 22 |
| LARGE_VALUE | US Large-Cap Value | 235.6837902769 | 241.376009389 | 0.024151933000620573 | 23 |
| BROAD_AI_TECH | Broad AI Technology | 62.52 | 64.0 | 0.023672424824056293 | 24 |
| NASDAQ100 | Nasdaq 100 | 705.06 | 721.34 | 0.023090233455308917 | 25 |
| JAPAN | Japan Equities | 90.2393502607 | 92.2188069077 | 0.021935626101932115 | 26 |
| INDIA | India Equities | 47.34 | 48.33 | 0.02091254752851701 | 27 |
| FINANCIALS | Financials Sector | 52.3 | 53.34 | 0.01988527724665401 | 28 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 229.2920067967 | 233.6290183874 | 0.018914796251686905 | 29 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 207.83 | 211.65 | 0.01838040706346522 | 30 |
| UNITED_KINGDOM | United Kingdom Equities | 45.7207544111 | 46.4896674866 | 0.01681759379091341 | 31 |
| DIVIDEND | US Dividend Equities | 32.3 | 32.82 | 0.016099071207430482 | 32 |
| METALS_MINING | Metals and Mining | 118.6 | 120.44 | 0.015514333895446875 | 33 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.86 | 116.6 | 0.015148876893609664 | 34 |
| REAL_ESTATE | Real Estate Sector | 44.7 | 45.36 | 0.014765100671140896 | 35 |
| LOW_VOL | US Low Volatility Equities | 73.47 | 74.47 | 0.0136109976861305 | 36 |
| CANADA | Canada Equities | 57.7599699352 | 58.486573038 | 0.012579700155924023 | 37 |
| INDUSTRIALS | Industrials Sector | 174.18 | 176.18 | 0.011482374555058072 | 38 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.4 | 96.36 | 0.010062893081761004 | 39 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.06 | 85.77 | 0.008347049141782303 | 40 |
| TOTAL_US_MARKET | Total US Stock Market | 363.38 | 366.36 | 0.008200781550993463 | 41 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.17 | 109.01 | 0.007765554220208859 | 42 |
| CHINA | China Equities | 54.0842676953 | 54.4717192824 | 0.0071638501104023256 | 43 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.74 | 94.38 | 0.006827394922125141 | 44 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.43 | 79.94 | 0.006420747828276285 | 45 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.17 | 98.76 | 0.006009982683100823 | 46 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.62 | 94.18 | 0.005981627857295502 | 47 |
| SP500 | S&P 500 | 737.55 | 741.75 | 0.005694529184462116 | 48 |
| HEALTHCARE | Healthcare Sector | 153.01 | 153.81 | 0.005228416443369799 | 49 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.01 | 48.26 | 0.005207248489897953 | 50 |
| EURO | Euro | 106.29 | 106.83 | 0.00508044030482635 | 51 |
| UTILITIES | Utilities Sector | 44.35 | 44.53 | 0.0040586245772264995 | 52 |
| TIPS | Treasury Inflation-Protected Securities | 109.25 | 109.61 | 0.0032951945080090805 | 53 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.97 | 107.05 | 0.0007478732354866402 | 54 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.45 | 91.51 | 0.0006560962274466675 | 55 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 56 |
| COMMUNICATIONS | Communication Services Sector | 111.67 | 111.65 | -0.00017909913136915367 | 57 |
| YEN | Japanese Yen | 57.31 | 57.26 | -0.0008724480893387287 | 58 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 129.6 | 129.41 | -0.0014660493827159948 | 59 |
| ENERGY | Energy Sector | 57.67 | 57.55 | -0.0020808045777701567 | 60 |
| US_DOLLAR | US Dollar | 28.02 | 27.95 | -0.0024982155603140432 | 61 |
| SILVER | Silver | 61.57 | 61.29 | -0.004547669319473813 | 62 |
| AGRICULTURE | Agriculture Commodities | 26.4 | 26.24 | -0.0060606060606061 | 63 |
| LARGE_GROWTH | US Large-Cap Growth | 122.5847246013 | 121.5056513062 | -0.008802673404942007 | 64 |
| CYBERSECURITY | Cybersecurity | 86.7 | 85.33 | -0.015801614763552574 | 65 |
| SOLAR | Solar Energy | 64.05 | 63.03 | -0.015925058548009297 | 66 |
| BROAD_COMMODITIES | Broad Commodities | 17.46 | 17.06 | -0.02290950744559006 | 67 |
| GOLD | Gold | 81.22 | 79.19 | -0.0249938438808176 | 68 |
| SOFTWARE | Software | 95.832595444 | 90.6835305871 | -0.053729786123854706 | 69 |
| OIL | Crude Oil | 133.02 | 125.43 | -0.057059088858818274 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.005228416443369799 | 0.0015685249330109395 | Defensive leadership with positive recent momentum amid risk-off tape; low beta into CPI/PPI week. |
| anthropic-claude-opus-4-7 | LOW_VOL | 25.0 | 0.0136109976861305 | 0.003402749421532625 | Outperforming defensively (+1.7% 7d) amid elevated VIX 21.5 and soft sentiment. |
| anthropic-claude-opus-4-7 | CONSUMER_STAPLES | 15.0 | 0.028523489932885893 | 0.0042785234899328835 | Defensive ballast; hot CPI/PPI risk favors staples over discretionary. |
| anthropic-claude-opus-4-7 | ENERGY | 15.0 | -0.0020808045777701567 | -0.0003121206866655235 | WTI $90, EIA forecasting inventory draws; sector showing relative strength. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.0006560962274466675 | 9.841443411700013e-05 | Carry with no duration risk ahead of hot CPI/PPI prints and 3/10/30Y auctions. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.005228416443369799 | 0.0015685249330109395 | Defensive sector with strong recent relative strength (+2.37% 7d while market fell); low beta into hot CPI/PPI prints during the week. |
| anthropic-claude-opus-4-8 | ENERGY | 20.0 | -0.0020808045777701567 | -0.00041616091555403135 | Energy leading on firm oil ($90 WTI) and EIA inventory draw forecasts; positive momentum and inflation tailwind ahead of CPI/PPI. |
| anthropic-claude-opus-4-8 | CONSUMER_STAPLES | 15.0 | 0.028523489932885893 | 0.0042785234899328835 | Defensive positioning with positive 7d return; cushions against equity drawdown risk into inflation data. |
| anthropic-claude-opus-4-8 | FINANCIALS | 15.0 | 0.01988527724665401 | 0.0029827915869981014 | Outperformed broad market recently (+1.40% 7d), supported by strong FDIC bank profits and rising yields/steeper curve. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 20.0 | 0.0006560962274466675 | 0.0001312192454893335 | Cash-like ballast yielding positive carry; protects against hot CPI/PPI selloff and elevated VIX while keeping flexibility. |
| google-gemini-3-1-pro | SHORT_TREASURY | 40.0 | 0.0006560962274466675 | 0.000262438490978667 | Provides a stable, low-risk yield while avoiding equity market volatility ahead of key inflation data. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.005228416443369799 | 0.0015685249330109395 | A defensive sector that has shown recent positive momentum and is less sensitive to immediate macroeconomic shocks. |
| google-gemini-3-1-pro | ENERGY | 30.0 | -0.0020808045777701567 | -0.000624241373331047 | Offers exposure to a sector with strong recent performance and potential upside from tight global oil inventories. |
| openai-gpt-5-5 | OIL | 35.0 | -0.057059088858818274 | -0.019970681100586394 | Crude has positive short-term momentum, WTI is elevated, and upcoming EIA reports plus a forecast inventory draw create a near-term catalyst for continued energy commodity strength. |
| openai-gpt-5-5 | ENERGY | 25.0 | -0.0020808045777701567 | -0.0005202011444425392 | Energy equities can benefit from high oil prices and inflation persistence while offering better equity-market beta than broad growth sectors if rates stay pressured. |
| openai-gpt-5-5 | US_DOLLAR | 15.0 | -0.0024982155603140432 | -0.00037473233404710645 | Hot inflation data, high Treasury yields, and risk-off conditions around CPI/PPI could support the dollar over the one-week window. |
| openai-gpt-5-5 | HEALTHCARE | 15.0 | 0.005228416443369799 | 0.0007842624665054698 | Healthcare has recent relative strength and defensive characteristics that may outperform the S&P 500 if inflation data pressures broad equities. |
| openai-gpt-5-5 | LOW_VOL | 10.0 | 0.0136109976861305 | 0.00136109976861305 | Low-volatility equities provide defensive equity exposure and have shown recent resilience during the prior week’s broad market weakness. |
| xai-grok-4-3 | ENERGY | 40.0 | -0.0020808045777701567 | -0.0008323218311080627 | Oil at $90+ and positive recent sector returns amid sticky inflation data. |
| xai-grok-4-3 | FINANCIALS | 30.0 | 0.01988527724665401 | 0.005965583173996203 | Resilient to rate environment with recent positive performance and stable labor data. |
| xai-grok-4-3 | HEALTHCARE | 30.0 | 0.005228416443369799 | 0.0015685249330109395 | Defensive qualities ahead of CPI and PPI releases within the scoring window. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.005228416443369799 | 0.009036091591927925 | 0.0033415624074658087 | 0.11802595532855825 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.005228416443369799 | 0.008544898339877227 | 0.0028503691554151115 | 0.11851714858060894 |  | True | True |
| xai-grok-4-3 | ENERGY | 3 | 0.55 | -0.0020808045777701567 | 0.006701786275899079 | 0.0010072570914369632 | 0.12036026064458709 |  | True | True |
| google-gemini-3-1-pro | SHORT_TREASURY | 3 | 0.65 | 0.0006560962274466675 | 0.0012067220506585597 | -0.004487807133803557 | 0.12585532486982762 |  | False | True |
| openai-gpt-5-5 | OIL | 5 | 0.58 | -0.057059088858818274 | -0.01872025234395752 | -0.024414781528419634 | 0.1457822992644437 |  | False | False |

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
