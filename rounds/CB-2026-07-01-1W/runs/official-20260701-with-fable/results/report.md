# CapitalBench Report: CB-2026-07-01-1W / official-20260701-with-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260701-with-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-01-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-01
- Decision deadline: 2026-07-02T07:30:00Z
- Horizon: one week
- Entry date: 2026-07-01
- Exit date: 2026-07-08
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | HEALTHCARE | 3 | 0.65 | Allocations target sectors with positive trailing returns and resilience to scheduled data releases within the one-week scoring period. | Adverse June employment report surprise increasing volatility in rate-sensitive holdings; Post-holiday reversal in recent sector leaders; FOMC minutes on July 8 introducing unexpected policy signals |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.45 | Overweight healthcare/biotech, financials, and value/equal-weight to ride the ongoing breadth rotation while limiting exposure to faltering AI/tech leadership over the short window. | A strong jobs report or benign FOMC minutes could reignite mega-cap tech leadership, causing this rotation-tilted portfolio to lag SPY.; Recent 30-day strength in healthcare, biotech, and financials could mean-revert; independent catalyst support beyond price action is limited.; Hot wage or inflation data could push yields higher, hurting biotech and value equities alike.; Biotech's very high idiosyncratic risk (clinical/regulatory news) could drag returns in a short window. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Overweight sectors showing durable breadth and defensive tilt into a holiday-shortened week with payrolls catalyst; underweight mega-cap tech given recent AI-name weakness and elevated volatility. | Weak June payrolls or hot wage print could trigger rate/risk repricing across cyclicals; Reversal in healthcare/biotech after strong 30d run (momentum reversal risk); Mega-cap tech rebound would cause equal-weight and non-tech tilt to lag SPY benchmark; FOMC minutes July 8 could surprise hawkish given sticky 3.4% core PCE |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.6 | A balanced approach utilizing broad US equities, defensive healthcare, and short-term Treasuries to navigate potential short-term volatility. | Unexpected negative economic data releases, such as the upcoming employment report, could trigger a broad market sell-off.; A sudden shift in interest rate expectations could negatively impact both equities and fixed-income assets.; Sector-specific risks in healthcare, such as regulatory changes or disappointing clinical trial results, could lead to underperformance. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Overweight healthcare/financials/industrials for continued relative strength backed by macro data, buffered by low-vol and core SPX to limit tracking error. | A hot or very weak June payrolls print on July 2 could sharply rotate sector leadership against defensives/financials.; Holiday-shortened, thin-liquidity week amplifies single-day gap risk around the jobs data and FOMC minutes.; Recent sector strength (healthcare, financials, industrials) could mean-revert given elevated positioning and limited independent catalysts in-window. |
| openai-gpt-5-5 | openai | portfolio | REGIONAL_BANKS | 5 | 0.55 | Favor regional banks, biotech/healthcare, industrials, and small value over cap-weighted tech concentration. Recent relative strength is used only alongside breadth, macro data, and sector context, with explicit reversal risk acknowledged. | A rebound in mega-cap technology or AI-related stocks would likely make SPY outperform this underweight-tech portfolio.; A weak payrolls or ISM services report could hurt regional banks, industrials, and small value through growth and credit-quality concerns.; Hawkish FOMC minutes or hotter wage data could raise rate expectations and pressure biotech and small-cap valuations.; Recent strength in biotech and regional banks may reverse quickly because some continuation support is price-based and positioning may be extended. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 103.27 | 112.20999908447266 | 0.08656917870119751 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 12.19 | 13.109999656677246 | 0.07547166994891286 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 15.78 | 16.62 | 0.05323193916349811 | 3 |
| ENERGY | Energy Sector | 52.81 | 55.6 | 0.052830903238022975 | 4 |
| BIOTECH | Biotechnology | 156.55 | 162.97 | 0.04100926221654411 | 5 |
| BITCOIN_ETF | Bitcoin ETF | 34.0 | 35.22999954223633 | 0.03617645712459794 | 6 |
| AGRICULTURE | Agriculture Commodities | 26.86 | 27.6200008392334 | 0.028294893493425066 | 7 |
| CHINA | China Equities | 51.525 | 52.85 | 0.025715672003881584 | 8 |
| HEALTHCARE | Healthcare Sector | 159.54 | 162.3 | 0.017299736743136673 | 9 |
| DIVIDEND | US Dividend Equities | 31.85 | 32.34 | 0.015384615384615552 | 10 |
| AUSTRALIA | Australia Equities | 27.7 | 28.12 | 0.015162454873646203 | 11 |
| UTILITIES | Utilities Sector | 44.77 | 45.36 | 0.013178467723922171 | 12 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.3 | 84.39 | 0.013085234093637599 | 13 |
| UNITED_KINGDOM | United Kingdom Equities | 45.94 | 46.49 | 0.011972137570744446 | 14 |
| GOLD | Gold | 75.96 | 76.74 | 0.010268562401263948 | 15 |
| LOW_VOL | US Low Volatility Equities | 75.24 | 75.86 | 0.008240297713981937 | 16 |
| BRAZIL | Brazil Equities | 34.18 | 34.41 | 0.006729081334113429 | 17 |
| CYBERSECURITY | Cybersecurity | 91.11 | 91.66 | 0.006036658983646026 | 18 |
| LARGE_VALUE | US Large-Cap Value | 243.88 | 245.2 | 0.005412497949811357 | 19 |
| CANADA | Canada Equities | 57.67 | 57.97 | 0.005202011444425114 | 20 |
| EURO | Euro | 104.95 | 105.44999694824219 | 0.004764144337705334 | 21 |
| EUROPE | Europe Equities | 87.77 | 88.18 | 0.004671299988606714 | 22 |
| FINANCIALS | Financials Sector | 54.78 | 54.97 | 0.0034684191310696555 | 23 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.59 | 79.66 | 0.0008795074758134458 | 24 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.4 | 91.45 | 0.000547045951859948 | 25 |
| YEN | Japanese Yen | 56.43 | 56.459999084472656 | 0.0005316158864550058 | 26 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 27 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.36 | 70.34 | -0.0002842524161454918 | 28 |
| SP500 | S&P 500 | 745.76 | 745.4 | -0.000482729028105533 | 29 |
| SOUTH_AFRICA | South Africa Equities | 62.73 | 62.69 | -0.0006376534353578212 | 30 |
| REAL_ESTATE | Real Estate Sector | 44.18 | 44.15 | -0.0006790402897238756 | 31 |
| EMERGING_MARKETS | Emerging Markets | 59.22 | 59.17 | -0.0008443093549476144 | 32 |
| TIPS | Treasury Inflation-Protected Securities | 108.17 | 108.05 | -0.0011093648886013607 | 33 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.02 | 95.79000091552734 | -0.00239532477059623 | 34 |
| COMMUNICATIONS | Communication Services Sector | 109.74 | 109.46 | -0.0025514853289593242 | 35 |
| TOTAL_US_MARKET | Total US Stock Market | 369.27 | 368.25 | -0.002762206515557697 | 36 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.02 | 93.69000244140625 | -0.0035098655455620964 | 37 |
| COPPER | Copper | 37.21 | 37.06999969482422 | -0.003762437655893125 | 38 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.34 | 106.91000366210938 | -0.0040059282456738066 | 39 |
| US_DOLLAR | US Dollar | 28.49 | 28.360000610351562 | -0.004562983139643206 | 40 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.5 | 98.04 | -0.0046700507614212405 | 41 |
| JAPAN | Japan Equities | 93.05 | 92.54 | -0.0054809242342825915 | 42 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.03 | 93.51 | -0.005530149952142849 | 43 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.41 | 212.2 | -0.005669837402183631 | 44 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.46 | 107.67 | -0.007283791259450445 | 45 |
| MEXICO | Mexico Equities | 75.27 | 74.71 | -0.007439883087551502 | 46 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.27 | 47.83000183105469 | -0.009115354649788965 | 47 |
| SOFTWARE | Software | 93.34 | 92.48 | -0.009213627598028684 | 48 |
| LARGE_GROWTH | US Large-Cap Growth | 123.02 | 121.8 | -0.009917086652576845 | 49 |
| INDIA | India Equities | 49.21 | 48.65 | -0.011379800853485111 | 50 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.52 | 84.36 | -0.013564078578110372 | 51 |
| SILVER | Silver | 53.58 | 52.83000183105469 | -0.013997726184122983 | 52 |
| SOUTH_KOREA | South Korea Equities | 185.5 | 182.72 | -0.014986522911051181 | 53 |
| INDUSTRIALS | Industrials Sector | 183.36 | 180.42 | -0.016034031413612704 | 54 |
| BROAD_AI_TECH | Broad AI Technology | 63.63 | 62.57 | -0.016658808738016728 | 55 |
| MATERIALS | Materials Sector | 51.02 | 50.16 | -0.016856134849078885 | 56 |
| TAIWAN | Taiwan Equities | 105.69 | 103.9 | -0.016936323209385873 | 57 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 243.86 | 239.63 | -0.01734601820716808 | 58 |
| SMALL_VALUE | US Small-Cap Value | 221.71 | 217.68 | -0.018176897749312193 | 59 |
| NASDAQ100 | Nasdaq 100 | 725.17 | 711.44 | -0.018933491457175378 | 60 |
| SMALL_CAP | US Small-Cap Stocks | 299.32 | 293.48 | -0.01951089135373507 | 61 |
| MID_CAP | US Mid-Cap Stocks | 76.44 | 74.73 | -0.022370486656200894 | 62 |
| TECHNOLOGY | Technology Sector | 185.62 | 181.4 | -0.02273461911431962 | 63 |
| METALS_MINING | Metals and Mining | 104.36 | 101.94 | -0.023188961287849752 | 64 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.09 | 115.3 | -0.02362604792954537 | 65 |
| REGIONAL_BANKS | Regional Banks | 76.18 | 73.34 | -0.03728012601732744 | 66 |
| MOMENTUM | US Momentum Equities | 328.1 | 314.85 | -0.04038402925937212 | 67 |
| SEMICONDUCTORS | Semiconductors | 620.46 | 593.0 | -0.044257486381072186 | 68 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.44 | 123.81 | -0.05082796688132474 | 69 |
| SOLAR | Solar Energy | 57.8 | 54.14 | -0.06332179930795845 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | 0.017299736743136673 | 0.004324934185784168 | Broad 30-day strength with low beta (0.37) and defensive character supports continuation into a data-heavy week; sector rotation toward defensives amid sticky 4.1% PCE inflation. |
| anthropic-claude-fable-5 | BIOTECH | 20.0 | 0.04100926221654411 | 0.008201852443308821 | Strong recent breadth (66.7% up days, near 52w high) with healthcare sector rotation support; higher beta captures upside if risk appetite holds. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.0034684191310696555 | 0.0006936838262139311 | Value/financials rotation evident (+6.9% 30d, 61.9% up days) with upcoming bank earnings anticipation and moderate beta; sticky inflation and 4.48% 10y support net interest margins. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | 0.005412497949811357 | 0.0010824995899622713 | Value outperforming growth amid sticky inflation; lower volatility and near 52w highs, benefits from broadening market breadth. |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 15.0 | -0.005669837402183631 | -0.0008504756103275445 | Most stocks rising while mega-cap tech lags; equal-weight captures breadth broadening at new highs with low drawdown. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.017299736743136673 | 0.005189921022941002 | Strong recent leadership (+8.4% 30d, +9.8% vs SPY) with defensive characteristics ahead of jobs data and holiday-shortened week; low beta cushions downside. |
| anthropic-claude-opus-4-7 | FINANCIALS | 20.0 | 0.0034684191310696555 | 0.0006936838262139311 | Broadening rally beneficiary with steady momentum (+6.9% 30d); benefits from firm rates and upcoming bank earnings positioning. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | -0.016034031413612704 | -0.003206806282722541 | ISM manufacturing still expansionary at 53.3 with new orders 56.0; industrials showing consistent breadth (+6.6% 30d). |
| anthropic-claude-opus-4-7 | BIOTECH | 15.0 | 0.04100926221654411 | 0.006151389332481616 | Strongest 30d momentum (+17.3%) with catalyst-rich window; supported by broader healthcare leadership. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 15.0 | -0.005669837402183631 | -0.0008504756103275445 | Diversified market breadth exposure that has outperformed cap-weighted SPY, hedging against mega-cap tech weakness noted in briefing. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.017299736743136673 | 0.005189921022941002 | Strongest broad-sector momentum with defensive character; +8.4% 30d, +4% 7d, low beta (0.37), near 52w high with limited drawdown, resilient to a soft payrolls print on July 2. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.0034684191310696555 | 0.0008671047827674139 | Steady uptrend (+6.9% 30d, 61.9% up-day share) with Q2 bank earnings approaching mid-July; low drawdown and moderate beta support continuation into the window. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | -0.016034031413612704 | -0.003206806282722541 | Broad cyclical strength (+6.6% 30d, +1.75% 7d) supported by ISM manufacturing still expansionary at 53.3 and firm new orders; consistent up-day share. |
| anthropic-claude-opus-4-8 | LOW_VOL | 15.0 | 0.008240297713981937 | 0.0012360446570972904 | Defensive ballast; +5.7% 30d, +7.1% vs SPY, very low beta (0.07) and smallest drawdown cushion the portfolio against a weak jobs report and holiday-thinned liquidity. |
| anthropic-claude-opus-4-8 | SP500 | 10.0 | -0.000482729028105533 | -4.82729028105533e-05 | Core benchmark exposure to limit tracking error against the SPY scoring benchmark while the sleaders carry relative alpha. |
| google-gemini-3-1-pro | SP500 | 40.0 | -0.000482729028105533 | -0.0001930916112422132 | Broad US equity exposure provides a baseline for the portfolio, balancing potential gains with market risk. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.017299736743136673 | 0.005189921022941002 | Healthcare has shown recent strength and offers defensive characteristics in a potentially volatile market. |
| google-gemini-3-1-pro | SHORT_TREASURY | 30.0 | 0.000547045951859948 | 0.00016411378555798438 | Short-term Treasuries provide a safe haven and liquidity, reducing overall portfolio volatility. |
| openai-gpt-5-5 | REGIONAL_BANKS | 30.0 | -0.03728012601732744 | -0.011184037805198232 | Strong recent relative performance, broad up-day participation, and new 52-week-high proximity suggest near-term demand for domestic financial cyclicals; stable growth data and still-high rates can support bank earnings, though positioning is extended. |
| openai-gpt-5-5 | BIOTECH | 25.0 | 0.04100926221654411 | 0.010252315554136027 | Healthcare-linked risk appetite has been strong, with biotech outperforming over the past month and retaining high beta without direct exposure to the AI names that weakened into the entry close; continuation support is mainly price-based, so reversal risk is material. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | 0.017299736743136673 | 0.003459947348627335 | Healthcare showed strong one-month and one-week relative strength with lower beta than the S&P 500, offering a defensive growth tilt if payrolls or FOMC minutes pressure broader equities. |
| openai-gpt-5-5 | INDUSTRIALS | 15.0 | -0.016034031413612704 | -0.0024051047120419054 | Industrials have had broad recent participation and may benefit from still-expanding manufacturing data, including June ISM readings above 50 with solid new orders. |
| openai-gpt-5-5 | SMALL_VALUE | 10.0 | -0.018176897749312193 | -0.0018176897749312194 | Small value combines recent breadth and domestic cyclical exposure with less mega-cap technology concentration than SPY; it could benefit if the market continues to broaden beyond AI leaders. |
| xai-grok-4-3 | HEALTHCARE | 50.0 | 0.017299736743136673 | 0.008649868371568337 | Strong 7d return of 4.04% alongside stable PCE and consumer data supporting defensive healthcare positioning into jobs report. |
| xai-grok-4-3 | BIOTECH | 30.0 | 0.04100926221654411 | 0.012302778664963232 | 4.57% 7d return with positive labor market trends and low drawdown supporting sector momentum through holiday-shortened week. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.0034684191310696555 | 0.0006936838262139311 | 1.97% 7d return and 6.88% 30d return with steady ADP employment gains favoring financials ahead of FOMC minutes. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | HEALTHCARE | 3 | 0.65 | 0.017299736743136673 | 0.0216463308627455 | 0.02212905989085103 | 0.06492284783845201 |  | True | True |
| anthropic-claude-fable-5 | HEALTHCARE | 5 | 0.45 | 0.017299736743136673 | 0.013452494434941646 | 0.013935223463047179 | 0.07311668426625587 |  | True | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.017299736743136673 | 0.007977712288586462 | 0.008460441316691995 | 0.07859146641261106 |  | True | True |
| google-gemini-3-1-pro | SP500 | 3 | 0.6 | -0.000482729028105533 | 0.005160943197256773 | 0.005643672225362306 | 0.08140823550394075 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.017299736743136673 | 0.0040379912772726114 | 0.004520720305378144 | 0.0825311874239249 |  | True | True |
| openai-gpt-5-5 | REGIONAL_BANKS | 5 | 0.55 | -0.03728012601732744 | -0.001694569389407995 | -0.001211840361302462 | 0.08826374809060551 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 0.013935223463047179 | 0.26746 | 0.05210208428567704 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 3738d4f6be5fc14989131b7bd65d5822ada04471f07d71b8ceef5d9a56553477 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | d77692ebf82162635d9a1308643e467198bb1c1faa683508170f83b575d2585f |
| market_data/universe_trailing_returns.csv | fb5dc17daf1e0f939405696981e26a2673dbc70b63fb830608f857a9f5566763 |
| market_data/universe_trailing_returns.md | a18f671af37c4e4d52095bdc6102c07e11bff2764f37450504d357722aebe9a9 |
| market_data/universe_trailing_returns.json | 3ba5033579de0dc0c723f050ac717d42f50508fcccb52ebe37a0a0bd879243f2 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 3199804d98151c4131093adf80706680a72376b94ef7269cc4aa32f6f5f95a06 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 8709ac7c84a704dbb0f1c7472daf09c478fd3e410b70eb23fc66ce5c2356d605 | yes |
| Final briefing | research/final_briefing.md | model-facing | 3738d4f6be5fc14989131b7bd65d5822ada04471f07d71b8ceef5d9a56553477 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
