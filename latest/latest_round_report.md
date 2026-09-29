# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-09-21-1W
- Decision deadline: 2026-09-21T13:25:00Z
- Horizon: one week
- Official run ID: official-v3-20260921-weekly
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | JAPAN | 3 | 0.5633 | Narrow leadership with SPY near flat weekly, positive asset share low, 10y at 5%, and mixed industrial data favor selective quality pullbacks and limited shock reversals over pure momentum continuation into the one-week window. | 10-year yield at 5% can extend pressure on rate-sensitive and duration-adjacent assets; Low positive-asset share and negative RSP-SPY spread signal fragile breadth that can reverse any bounce; High-vol slate names (crypto, Korea, solar, metals) can gap on macro data releases Tue-Fri; Scheduled labor and sentiment data mid-week may reprice growth expectations abruptly |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Mixed signals with crypto outperformance offset by weak equity breadth, elevated rates, and low positive asset share. | Crypto volatility exceeding 50%; Rate sensitivity in defensives; Low positive asset share indicating narrow breadth |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is near a 52-week high with low 21-session vol while equal-weight and most assets lag; 10-year yield at 5.00% and flat industrial production favor a narrow, rate-sensitive week rather than a broad reversal or high-beta continuation. | A sharp equity selloff from 5% yields or weak Sep 24-25 data could let high-beta reversals (Korea, metals, aerospace) outperform SPY.; Crypto and oil remain high-vol two-sided risks if risk appetite or crude prices gap on the one-week window.; Utilities and yen can keep lagging if Treasury yields stay at or above 5%.; Volume spikes in ITA and MUB may be noise rather than mean-reversion catalysts. |
| anthropic-claude-opus-5 | anthropic | portfolio | JAPAN | 3 | 0.56 | Narrow tape: SPY flat while equal-weight lags badly (RSP-SPY -3.7% over 21 sessions) and only ~32-35% of assets are positive. 10-year yield at 5.00% is pressuring rate-sensitives, small caps and breadth, while mega-cap tech and crypto carry the index. With a heavy macro calendar only partly inside the window and no clear reversal catalyst, most mean-reversion candidates lack independent in-window support. I treat a small number of high-quality relative pullbacks (Japan, Mexico) as modest overreactions and default the rest toward SPY. | 10-year yield at 5.00% could break higher and pressure non-US and rate-sensitive equities; Mega-cap tech leadership could extend, causing SPY to outrun diversified pullback candidates; Dollar strength (UUP +1.83% over 21 sessions) mechanically hurts unhedged Japan and Mexico exposure; Dense macro calendar (jobless claims, durable goods, sentiment) inside the window can drive sharp single-day rotations |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SOUTH_KOREA | 3 | 0.555 | Narrow mega-cap-led tape: SPY flat over 5 sessions while equal-weight lags by 1.1% and only 35% of assets are positive; 10-year yield at 5% and dollar strength pressure rate-sensitive and cyclical assets. Crypto and semis show strength but stretched vol. Few clean edges; only a handful of pulled-back names with intact medium-term trends (Korea, Japan, Mexico) offer a modest reversal case. | 10-year yield above 5% triggering broader equity de-risking that hits high-beta Korea (beta 3.3) hardest; Dollar strength continuing, penalizing unhedged Japan, Korea and Mexico exposure; Semiconductor rebound reversing, dragging Korea and Taiwan; Narrow mega-cap leadership persisting so SPY outperforms diversified alternatives |
| openai-gpt-6-astra | openai | portfolio | JAPAN | 3 | 0.5567 | Weak breadth, a 5.00% Treasury yield and stagnant industrial production constrain broad risk-taking. Cross-sectional dispersion leaves room for selective reversals, but persistent weakness in rate-sensitive and industrial exposures has macroeconomic support. Favor modest pullbacks within stronger prior relative trends over either indiscriminate loser buying or unsupported crypto momentum. Conviction is limited because the briefing supplies few asset-specific catalysts within the scoring window. | Further dollar appreciation could depress both unhedged international equities and agricultural commodities.; Treasury yields rising above 5% could deepen risk-asset weakness, particularly in high-beta South Korea.; September 22–25 activity, labor and sentiment releases could invalidate the selective-reversal thesis before exit.; Moves before the September 21 entry close could absorb the anticipated rebound; no supplied evidence establishes an asset-specific catalyst afterward. |
| google-gemini-3-1-pro | google | portfolio | METALS_MINING | 3 | 0.58 | The market is showing mixed signals with the S&P 500 slightly up while the Dow and Russell 2000 are down. Industrial production is flat, and the 10-year Treasury yield is at 5.00%. | Interest rates remaining high could pressure equities.; Industrial production weakness could signal broader economic slowing. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| HEALTHCARE | Healthcare Sector | 169.01 | 171.26 | 0.013312821726525037 | 1 |
| OIL | Crude Oil | 148.16 | 150.00999450683594 | 0.012486464004022313 | 2 |
| US_DOLLAR | US Dollar | 28.48 | 28.700000762939453 | 0.007724745889728046 | 3 |
| SEMICONDUCTORS | Semiconductors | 596.03 | 600.01 | 0.0066775162324044235 | 4 |
| CONSUMER_STAPLES | Consumer Staples Sector | 81.92 | 82.28 | 0.00439453125 | 5 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.57 | 91.63 | 0.0006552364311456227 | 6 |
| YEN | Japanese Yen | 58.2 | 58.220001220703125 | 0.0003436635859643822 | 7 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 8 |
| TECHNOLOGY | Technology Sector | 194.85 | 194.53 | -0.0016422889402103458 | 9 |
| MOMENTUM | US Momentum Equities | 316.25 | 315.59 | -0.0020869565217391806 | 10 |
| BROAD_COMMODITIES | Broad Commodities | 19.44 | 19.37 | -0.0036008230452675427 | 11 |
| MATERIALS | Materials Sector | 49.71 | 49.47 | -0.004828002414001276 | 12 |
| ENERGY | Energy Sector | 62.46 | 62.1 | -0.0057636887608069065 | 13 |
| NASDAQ100 | Nasdaq 100 | 741.47 | 736.53 | -0.006662440827005844 | 14 |
| INDUSTRIALS | Industrials Sector | 169.98 | 168.78 | -0.007059654076950195 | 15 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.21 | 46.84000015258789 | -0.007837319369034312 | 16 |
| LARGE_GROWTH | US Large-Cap Growth | 126.25 | 125.2 | -0.008316831683168324 | 17 |
| EURO | Euro | 105.8 | 104.90499877929688 | -0.008459368815719515 | 18 |
| UNITED_KINGDOM | United Kingdom Equities | 47.69 | 47.27 | -0.008806877752149167 | 19 |
| EUROPE | Europe Equities | 89.24 | 88.38 | -0.00963693411026445 | 20 |
| SP500 | S&P 500 | 773.5 | 765.61 | -0.010200387847446701 | 21 |
| BIOTECH | Biotechnology | 158.23 | 156.61 | -0.010238260759653506 | 22 |
| MID_CAP | US Mid-Cap Stocks | 73.25 | 72.44 | -0.011058020477815678 | 23 |
| JAPAN | Japan Equities | 97.96 | 96.83 | -0.01153532053899542 | 24 |
| TAIWAN | Taiwan Equities | 115.64 | 114.16999816894531 | -0.012711880240874107 | 25 |
| LARGE_VALUE | US Large-Cap Value | 253.45 | 250.05 | -0.013414874728743253 | 26 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.3 | 71.31 | -0.013692946058091238 | 27 |
| CYBERSECURITY | Cybersecurity | 103.09 | 101.67 | -0.013774371908041538 | 28 |
| TOTAL_US_MARKET | Total US Stock Market | 381.1 | 375.84 | -0.013802151666229445 | 29 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.68 | 209.74 | -0.013823584728230198 | 30 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.68 | 77.54 | -0.014489069649212039 | 31 |
| LOW_VOL | US Low Volatility Equities | 72.18 | 71.12 | -0.014685508451094509 | 32 |
| AGRICULTURE | Agriculture Commodities | 28.68 | 28.25 | -0.014993026499302675 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 105.68 | 104.09 | -0.015045420136260423 | 34 |
| SOFTWARE | Software | 107.13 | 105.43 | -0.015868570895174017 | 35 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.21 | 94.65 | -0.01621453071406287 | 36 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 91.15 | 89.53 | -0.017772901810202968 | 37 |
| MEXICO | Mexico Equities | 73.7 | 72.37000274658203 | -0.018046095704450038 | 38 |
| AUSTRALIA | Australia Equities | 29.04 | 28.5 | -0.018595041322314043 | 39 |
| SMALL_VALUE | US Small-Cap Value | 215.95 | 211.8 | -0.019217411437832732 | 40 |
| SMALL_CAP | US Small-Cap Stocks | 285.58 | 280.02 | -0.019469150500735388 | 41 |
| REGIONAL_BANKS | Regional Banks | 71.99 | 70.55 | -0.020002778163633828 | 42 |
| DIVIDEND | US Dividend Equities | 33.72 | 33.01 | -0.021055753262159027 | 43 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.59 | 89.66000366210938 | -0.021072129467088474 | 44 |
| MUNICIPAL_BONDS | Municipal Bonds | 102.86 | 100.61000061035156 | -0.021874386444180827 | 45 |
| CANADA | Canada Equities | 60.43 | 59.07 | -0.02250537812344866 | 46 |
| EMERGING_MARKETS | Emerging Markets | 61.14 | 59.69 | -0.023716061498200935 | 47 |
| BROAD_AI_TECH | Broad AI Technology | 66.31 | 64.71 | -0.024129090634896877 | 48 |
| COPPER | Copper | 40.67 | 39.68000030517578 | -0.024342259523585486 | 49 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.09 | 102.47 | -0.024931011513940504 | 50 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.78 | 91.33999633789062 | -0.026018379847615458 | 51 |
| CHINA | China Equities | 54.0 | 52.54 | -0.02703703703703708 | 52 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.23 | 109.0 | -0.02878018355163503 | 53 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 125.49 | 121.87 | -0.028846920073312576 | 54 |
| INDIA | India Equities | 48.5 | 47.09 | -0.02907216494845355 | 55 |
| REAL_ESTATE | Real Estate Sector | 42.59 | 41.35 | -0.02911481568443297 | 56 |
| SOUTH_KOREA | South Korea Equities | 189.16 | 183.5800018310547 | -0.029498827283491846 | 57 |
| FINANCIALS | Financials Sector | 55.9 | 54.19 | -0.030590339892665463 | 58 |
| COMMUNICATIONS | Communication Services Sector | 114.75 | 111.18 | -0.03111111111111109 | 59 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 216.14 | 209.26 | -0.03183122050522802 | 60 |
| METALS_MINING | Metals and Mining | 109.0 | 105.42 | -0.03284403669724767 | 61 |
| ETHEREUM_ETF | Ethereum ETF | 20.85 | 20.149999618530273 | -0.033573159782720796 | 62 |
| UTILITIES | Utilities Sector | 40.66 | 39.25 | -0.03467781603541553 | 63 |
| BITCOIN_ETF | Bitcoin ETF | 49.01 | 47.209999084472656 | -0.03672721721133121 | 64 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.8 | 78.62 | -0.038875305623471745 | 65 |
| BRAZIL | Brazil Equities | 38.07 | 36.209999084472656 | -0.048857392054829085 | 66 |
| GOLD | Gold | 81.67 | 77.5 | -0.05105914044324722 | 67 |
| SOUTH_AFRICA | South Africa Equities | 68.23 | 64.47000122070312 | -0.0551077059841254 | 68 |
| SILVER | Silver | 59.63 | 54.95000076293945 | -0.07848397177696709 | 69 |
| SOLAR | Solar Energy | 46.71 | 43.0 | -0.07942624705630486 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | portfolio | JAPAN | 3 | 0.5633 | -0.01153532053899542 | -0.008414987883351665 | 0.0017853999640950365 | 0.021727809609876702 |  | True | False |
| xai-grok-4-3 | portfolio | SP500 | 1 | 0.5 | -0.010200387847446701 | -0.010200387847446701 | 0.0 | 0.02351320957397174 |  | False | False |
| xai-grok-4-6 | portfolio | SP500 | 1 | 0.5 | -0.010200387847446701 | -0.010200387847446701 | 0.0 | 0.02351320957397174 |  | False | False |
| anthropic-claude-opus-5 | portfolio | JAPAN | 3 | 0.56 | -0.01153532053899542 | -0.01341361203943992 | -0.003213224191993219 | 0.02672643376596496 |  | False | False |
| anthropic-claude-fable-5-1 | portfolio | SOUTH_KOREA | 3 | 0.555 | -0.029498827283491846 | -0.017422068092104552 | -0.007221680244657851 | 0.03073488981862959 |  | False | False |
| openai-gpt-6-astra | portfolio | JAPAN | 3 | 0.5567 | -0.01153532053899542 | -0.018859859687661344 | -0.008659471840214643 | 0.03217268141418638 |  | False | False |
| google-gemini-3-1-pro | portfolio | METALS_MINING | 3 | 0.58 | -0.03284403669724767 | -0.02904647716776713 | -0.01884608932032043 | 0.04235929889429217 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1W has no scored official run.
- Round CB-2026-09-28-1W has no scored official run.
