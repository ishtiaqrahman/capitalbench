# CapitalBench Report: CB-2026-06-18-1M / official-20260618-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260618-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-18-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-18
- Decision deadline: 2026-06-19T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-18
- Exit date: 2026-07-20
- Entry rule: Use adjusted close prices on Thursday, June 18, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Monday, July 20, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 5 | 0.62 | Tilt toward continuation in tech/semis and broad large-caps given strong momentum and solid macro, with modest diversification into industrials and gold. | Hot June CPI (Jul 14) or hawkish Fed repricing could hit high-duration growth and semis hardest.; Semiconductor momentum mean-reverts after a 21% 30-day run, dragging the concentrated tech tilt.; Soft June payrolls (Jul 2) or weaker retail sales (Jul 16) could undercut cyclical industrials exposure.; Gold drawdown if real yields rise further on hawkish dots. |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 5 | 0.62 | Recent price momentum in high-beta tech and factor names is expected to carry forward through July data releases; modest benchmark holding reduces tail risk. | Hotter-than-expected June CPI or employment data could trigger rate repricing; Profit-taking after extended semiconductor and momentum rallies; Geopolitical or supply-chain shocks affecting Taiwan and South Korea exposure indirectly |
| google-gemini-3-1-pro | google | portfolio | SP500 | 4 | 0.65 | Overweighting technology and semiconductors to capture ongoing momentum, anchored by a core S&P 500 position. | A sudden reversal in technology and semiconductor momentum could lead to significant underperformance.; Higher-than-expected inflation prints could trigger a hawkish repricing of Fed expectations, disproportionately hurting growth stocks.; Geopolitical tensions or supply chain disruptions could negatively impact the semiconductor industry and South Korean equities. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.6 | Overweight AI/semiconductor complex which has dominant momentum into a quiet macro window, with industrials for breadth and gold as hedge. | Semiconductor crowding and sharp factor reversal/mean-reversion after 21% 30d run; Hawkish Fed repricing if June CPI (July 14) surprises hot, hitting growth multiples; Korea/Taiwan geopolitical or FX shock; Oil/energy weakness signaling demand slowdown spilling into cyclicals |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.57 | A concentrated pro-momentum, pro-risk allocation is expected to outperform the S&P 500 if recent AI/semiconductor leadership persists through the July close. Diversification across SMH, Taiwan, South Korea, MTUM, and biotech reduces single-ETF dependence while keeping high upside beta. | A sharp rotation out of crowded AI and semiconductor winners after their very large trailing gains could drive severe underperformance versus the S&P 500.; Hot June CPI or PPI data could push yields higher and compress valuations for long-duration growth and high-beta equities.; Taiwan or Korea country exposure could be hurt by adverse currency moves, export disappointments, or regional geopolitical headlines.; A broad risk-off move before the July 20 exit would disproportionately hit semiconductors, biotech, and emerging Asia exposures. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 12.88 | 14.33 | 0.11257763975155277 | 1 |
| OIL | Crude Oil | 114.87 | 125.51 | 0.09262644728823899 | 2 |
| CYBERSECURITY | Cybersecurity | 84.4672043338 | 91.79000091552734 | 0.08669396175098809 | 3 |
| ENERGY | Energy Sector | 53.3898947625 | 57.94 | 0.0852240907711228 | 4 |
| BIOTECH | Biotechnology | 140.5868983468 | 150.94000244140625 | 0.07364202650710161 | 5 |
| HEALTHCARE | Healthcare Sector | 148.7494792532 | 159.25 | 0.0705919832426849 | 6 |
| REGIONAL_BANKS | Regional Banks | 71.3072214239 | 75.88999938964844 | 0.06426807655994882 | 7 |
| BROAD_COMMODITIES | Broad Commodities | 16.5 | 17.3799991607666 | 0.053333282470703125 | 8 |
| AGRICULTURE | Agriculture Commodities | 26.63 | 28.02 | 0.052196770559519434 | 9 |
| BRAZIL | Brazil Equities | 33.73 | 35.48 | 0.051882597094574656 | 10 |
| FINANCIALS | Financials Sector | 53.384017836 | 56.04 | 0.04975238417159589 | 11 |
| LOW_VOL | US Low Volatility Equities | 72.8175689877 | 76.09 | 0.04494012994106922 | 12 |
| SOFTWARE | Software | 89.09 | 92.9800033569336 | 0.04366374853444377 | 13 |
| REAL_ESTATE | Real Estate Sector | 43.4834973186 | 45.23 | 0.04016472429996876 | 14 |
| DIVIDEND | US Dividend Equities | 31.6083884588 | 32.75 | 0.036117359880211364 | 15 |
| BITCOIN_ETF | Bitcoin ETF | 35.62 | 36.89 | 0.0356541268950028 | 16 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.7220248962 | 84.86 | 0.025845294605429947 | 17 |
| CHINA | China Equities | 52.77 | 54.08000183105469 | 0.02482474570882487 | 18 |
| UNITED_KINGDOM | United Kingdom Equities | 45.46 | 46.39 | 0.020457545094588747 | 19 |
| LARGE_VALUE | US Large-Cap Value | 242.18 | 246.96 | 0.019737385415806497 | 20 |
| SMALL_VALUE | US Small-Cap Value | 216.87 | 220.85 | 0.018352008115460894 | 21 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 209.151671347 | 212.4199981689453 | 0.01562658715991283 | 22 |
| COMMUNICATIONS | Communication Services Sector | 109.1601464074 | 110.8 | 0.015022456881651935 | 23 |
| CANADA | Canada Equities | 57.87 | 58.62 | 0.012960082944530882 | 24 |
| UTILITIES | Utilities Sector | 44.4771296327 | 44.94 | 0.010406929833882472 | 25 |
| US_DOLLAR | US Dollar | 28.3 | 28.39 | 0.0031802120141342094 | 26 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3026630057 | 91.56 | 0.0028185048040048066 | 27 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.6409728106 | 79.68000030517578 | 0.0004900429163339215 | 28 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 29 |
| AUSTRALIA | Australia Equities | 28.56 | 28.52 | -0.0014005602240896309 | 30 |
| TIPS | Treasury Inflation-Protected Securities | 108.3304080309 | 108.05000305175781 | -0.0025884235482821483 | 31 |
| EURO | Euro | 105.6993994483 | 105.37 | -0.003116379563358973 | 32 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.0488785482 | 93.54 | -0.005410788050377313 | 33 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.0422185809 | 106.4 | -0.005999675543109317 | 34 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.1422613831 | 93.57 | -0.006078687453356046 | 35 |
| SP500 | S&P 500 | 746.74 | 742.09 | -0.006227066984492602 | 36 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.5690800817 | 97.94999694824219 | -0.006280703167206969 | 37 |
| EUROPE | Europe Equities | 88.27 | 87.69000244140625 | -0.0065707211803981425 | 38 |
| YEN | Japanese Yen | 56.85 | 56.46 | -0.0068601583113456766 | 39 |
| TOTAL_US_MARKET | Total US Stock Market | 368.9269745367 | 366.25 | -0.007256109532412958 | 40 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.2388717105 | 47.82 | -0.008683281669890852 | 41 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.3289777105 | 95.37 | -0.009955236038962645 | 42 |
| SMALL_CAP | US Small-Cap Stocks | 295.59 | 292.31 | -0.011096451165465537 | 43 |
| MID_CAP | US Mid-Cap Stocks | 75.78 | 74.93 | -0.011216679862760537 | 44 |
| COPPER | Copper | 38.86 | 38.42 | -0.011322696860524895 | 45 |
| INDUSTRIALS | Industrials Sector | 180.4691569319 | 178.12 | -0.013016944124066843 | 46 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.6876681292 | 107.1500015258789 | -0.014147571935145709 | 47 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.92275687 | 114.61 | -0.019780211585084584 | 48 |
| INDIA | India Equities | 49.58 | 48.54999923706055 | -0.020774521237181376 | 49 |
| MEXICO | Mexico Equities | 77.33 | 75.09 | -0.02896676580887103 | 50 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.4285911501 | 83.88999938964844 | -0.029372129369120592 | 51 |
| LARGE_GROWTH | US Large-Cap Growth | 123.19 | 119.47 | -0.030197256270801165 | 52 |
| MATERIALS | Materials Sector | 51.6167690951 | 50.03 | -0.03074134865311884 | 53 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 238.99 | 229.27000427246094 | -0.04067113991187532 | 54 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.31 | 69.2300033569336 | -0.04259433886138031 | 55 |
| EMERGING_MARKETS | Emerging Markets | 60.77 | 57.93000030517578 | -0.04673358062899824 | 56 |
| GOLD | Gold | 79.33 | 75.3499984741211 | -0.05017019445202198 | 57 |
| NASDAQ100 | Nasdaq 100 | 739.8044657025 | 696.06 | -0.05912976702696893 | 58 |
| JAPAN | Japan Equities | 96.26 | 90.43000030517578 | -0.06056513291942889 | 59 |
| SOUTH_AFRICA | South Africa Equities | 66.74 | 61.63 | -0.07656577764459083 | 60 |
| TECHNOLOGY | Technology Sector | 191.2131931899 | 175.71 | -0.08107805183977701 | 61 |
| MOMENTUM | US Momentum Equities | 338.52 | 302.64 | -0.10599078341013823 | 62 |
| BROAD_AI_TECH | Broad AI Technology | 66.7995298445 | 59.13999938964844 | -0.11466443660130365 | 63 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 133.17 | 116.62999725341797 | -0.12420216825547814 | 64 |
| TAIWAN | Taiwan Equities | 109.99 | 95.94 | -0.12773888535321387 | 65 |
| SOLAR | Solar Energy | 60.58 | 52.689998626708984 | -0.13024102630061096 | 66 |
| SILVER | Silver | 59.51 | 50.98 | -0.14333725424298438 | 67 |
| SEMICONDUCTORS | Semiconductors | 659.88 | 558.8300170898438 | -0.15313387723549166 | 68 |
| METALS_MINING | Metals and Mining | 116.9386392465 | 97.73999786376953 | -0.16417705479076794 | 69 |
| SOUTH_KOREA | South Korea Equities | 219.2 | 162.86 | -0.2570255474452554 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | -0.15313387723549166 | -0.05359685703242208 | Strong momentum, AI capex cycle, leading sector with broad earnings tailwind into July. |
| anthropic-claude-opus-4-7 | SOUTH_KOREA | 20.0 | -0.2570255474452554 | -0.05140510948905108 | Memory/semis exposure, powerful trend, benefiting from AI hardware demand. |
| anthropic-claude-opus-4-7 | NASDAQ100 | 25.0 | -0.05912976702696893 | -0.014782441756742232 | Mega-cap tech momentum with solid breadth; benchmark-beating tilt. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 10.0 | -0.013016944124066843 | -0.0013016944124066843 | Strong Philly Fed new orders, capex theme, broadening rally participation. |
| anthropic-claude-opus-4-7 | GOLD | 10.0 | -0.05017019445202198 | -0.005017019445202198 | Hedge against sticky inflation (CPI 4.2%) and risk-off; diversifies tech beta. |
| anthropic-claude-opus-4-8 | SP500 | 40.0 | -0.006227066984492602 | -0.002490826793797041 | Broad large-cap core with strong trend; benchmark-relative risk controlled while capturing continued melt-up. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 25.0 | -0.15313387723549166 | -0.038283469308872914 | Strongest momentum leader; AI capex cycle and chip demand driving outsized returns, with continuation likely into July earnings. |
| anthropic-claude-opus-4-8 | NASDAQ100 | 20.0 | -0.05912976702696893 | -0.011825953405393786 | Mega-cap growth strength confirmed by recent breadth and Nasdaq leadership into the window. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 10.0 | -0.013016944124066843 | -0.0013016944124066843 | Solid Philly Fed orders, resilient economy and defense/aerospace tailwinds; cyclically strong without crowding into a single theme. |
| anthropic-claude-opus-4-8 | GOLD | 5.0 | -0.05017019445202198 | -0.002508509722601099 | Hedge against sticky inflation (CPI 4.2% YoY, hawkish dots) and any risk-off shock during the window. |
| google-gemini-3-1-pro | SP500 | 40.0 | -0.006227066984492602 | -0.002490826793797041 | Core broad market exposure to capture general equity upside in a stable macro environment. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | -0.08107805183977701 | -0.0243234155519331 | Strong momentum and growth characteristics, supported by recent outperformance and AI trends. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 15.0 | -0.15313387723549166 | -0.022970081585323748 | High-beta play on technology and AI infrastructure build-out, showing exceptional recent returns. |
| google-gemini-3-1-pro | SOUTH_KOREA | 15.0 | -0.2570255474452554 | -0.03855383211678831 | Strong recent momentum and exposure to global semiconductor and electronics supply chains. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.15313387723549166 | -0.05359685703242208 | Strongest recent and medium-term momentum in the universe, with AI-linked chip leadership likely to remain a near-term market focus into the July window. |
| openai-gpt-5-5 | TAIWAN | 20.0 | -0.12773888535321387 | -0.025547777070642777 | High semiconductor supply-chain exposure with very strong trailing momentum, offering leveraged participation in the same AI hardware trend through country exposure. |
| openai-gpt-5-5 | SOUTH_KOREA | 20.0 | -0.2570255474452554 | -0.05140510948905108 | Exceptional momentum and export/semiconductor sensitivity support continuation if global risk appetite and AI hardware demand remain firm. |
| openai-gpt-5-5 | MOMENTUM | 15.0 | -0.10599078341013823 | -0.015898617511520736 | Captures broad trend persistence across recent market leaders while diversifying away from a single industry or country vehicle. |
| openai-gpt-5-5 | BIOTECH | 10.0 | 0.07364202650710161 | 0.007364202650710161 | Recent strength and high beta provide additional upside if risk appetite broadens beyond mega-cap technology during the scoring month. |
| xai-grok-4-3 | SEMICONDUCTORS | 30.0 | -0.15313387723549166 | -0.045940163170647495 | Strongest recent 30-day momentum and sector leadership likely to persist into July window |
| xai-grok-4-3 | MOMENTUM | 25.0 | -0.10599078341013823 | -0.02649769585253456 | Factor has delivered outsized gains and benefits from continuation of risk-on rotation |
| xai-grok-4-3 | NASDAQ100 | 20.0 | -0.05912976702696893 | -0.011825953405393786 | Heavy tech exposure aligns with observed growth and earnings momentum |
| xai-grok-4-3 | SMALL_CAP | 15.0 | -0.011096451165465537 | -0.0016644676748198306 | Domestic growth sensitivity and recent outperformance versus large caps |
| xai-grok-4-3 | SP500 | 10.0 | -0.006227066984492602 | -0.0006227066984492602 | Benchmark anchor to capture broad market beta while limiting active concentration |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SP500 | 5 | 0.62 | -0.006227066984492602 | -0.056410453643071526 | -0.050183386658578924 | 0.16898809339462428 |  | False | False |
| xai-grok-4-3 | SEMICONDUCTORS | 5 | 0.62 | -0.15313387723549166 | -0.08655098680184493 | -0.08032391981735233 | 0.1991286265533977 |  | False | False |
| google-gemini-3-1-pro | SP500 | 4 | 0.65 | -0.006227066984492602 | -0.0883381560478422 | -0.0821110890633496 | 0.20091579579939498 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.6 | -0.15313387723549166 | -0.12610312213582428 | -0.11987605515133168 | 0.23868076188737705 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.57 | -0.15313387723549166 | -0.13908415845292652 | -0.1328570914684339 | 0.2516617982044793 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | dda2ee5ee69295c60efc89f291aad2182afd5b498ee8c5f305989ec7f746d61a |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 15cfd72f631f247b0505ef997c6e93e6c8c27e052aad94143f8d9879a4a801b7 |
| manifest.yaml | ac810e656405d3ec5b5070a9191ceabc9cabfa9273fd9c5c8f2a2bdbeec992f5 |
| market_data/universe_trailing_returns.csv | fb88877ba6d0c6634f00dafe37ccd2085bdd8328a9eedc00a0f168d773b6b6df |
| market_data/universe_trailing_returns.md | a86a3bf5eaa7f64e8c8b534f433a1c510755ac647c99d5f88509a3b3e1222f26 |
| market_data/universe_trailing_returns.json | 979d2ec3ef630dd986852a84ef63172efe32da536aa01e4a17f03a82e9c5391a |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 71603cb8967d7bb6a1b16b28da99e3416b68a7669a41048290d29e00fcdd3a65 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 225b5b2a98fde058aef40e21ac16e7a994e4280be103e567b6fdf204f6c61aa7 | yes |
| Final briefing | research/final_briefing.md | model-facing | dda2ee5ee69295c60efc89f291aad2182afd5b498ee8c5f305989ec7f746d61a | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
