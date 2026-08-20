# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-19
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.44% |
| spy_return_21s | 2.78% |
| rsp_return_5s | 0.45% |
| rsp_return_21s | 4.38% |
| hyg_return_5s | 0.13% |
| hyg_return_21s | 0.56% |
| tlt_return_5s | 1.11% |
| tlt_return_21s | -0.37% |
| uup_return_5s | -1.13% |
| uup_return_21s | -2.11% |
| uso_return_5s | 2.84% |
| uso_return_21s | 1.60% |
| iau_return_5s | 2.24% |
| iau_return_21s | 10.44% |
| rsp_minus_spy_5s | 0.89% |
| rsp_minus_spy_21s | 1.60% |
| positive_asset_share_5s | 53.62% |
| positive_asset_share_21s | 75.36% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.78% | -9.61% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -2.47% | -8.13% | 0.21% | -0.01% | -0.355 | -0.108 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.44% | 0.00% | 0.00% | 13.72% | -4.49% | -0.809 | 1.000 | 1.000 | -1.13% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.48% | 0.08% | 0.08% | 13.67% | -4.36% | -0.693 | 0.995 | 1.012 | -1.12% |
| NASDAQ100 | QQQ | technology_and_growth | -1.05% | -1.77% | 7.70% | 25.85% | -11.22% | -0.685 | 0.930 | 1.420 | -3.93% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.41% | -1.56% | -1.44% | 21.02% | -11.35% | -0.860 | 0.933 | 1.280 | -4.65% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.39% | 1.55% | 2.03% | 11.31% | -2.40% | -0.725 | 0.804 | 0.706 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | -1.31% | -0.79% | -3.06% | 14.24% | -3.09% | -0.860 | 0.806 | 0.981 | -2.07% |
| SMALL_CAP | IWM | diversified_us_equity | -0.33% | -1.03% | 3.19% | 17.38% | -3.95% | -1.088 | 0.819 | 1.214 | -1.10% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.14% | -2.14% | 4.81% | 14.50% | -2.75% | -0.545 | 0.730 | 0.959 | -0.80% |
| DIVIDEND | SCHD | diversified_us_equity | 2.42% | 4.14% | -3.90% | 12.14% | -2.95% | 0.309 | 0.283 | 0.244 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 0.21% | -3.84% | -6.33% | 13.19% | -3.75% | -0.697 | 0.020 | 0.017 | -2.55% |
| MOMENTUM | MTUM | diversified_us_equity | -2.81% | -1.96% | 11.90% | 39.44% | -17.99% | 0.447 | 0.750 | 1.529 | -11.40% |
| TECHNOLOGY | XLK | technology_and_growth | -2.76% | -1.19% | 19.00% | 35.35% | -15.86% | -0.975 | 0.856 | 1.735 | -7.24% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.95% | -2.17% | -12.48% | 20.70% | -9.68% | -0.540 | 0.576 | 0.693 | -6.76% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.59% | -0.05% | -9.85% | 23.94% | -10.72% | -0.850 | 0.769 | 1.195 | -4.38% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.72% | 0.17% | -12.93% | 17.31% | -4.95% | -0.706 | -0.067 | -0.074 | -2.64% |
| HEALTHCARE | XLV | healthcare_and_biotech | 4.30% | 6.85% | -7.11% | 19.32% | -3.74% | -0.597 | 0.218 | 0.268 | 0.00% |
| FINANCIALS | XLF | financials | -0.76% | -0.34% | -1.99% | 13.01% | -2.08% | -0.868 | 0.542 | 0.613 | -1.34% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.11% | -1.78% | -4.78% | 19.51% | -4.80% | -1.033 | 0.713 | 0.959 | -2.44% |
| ENERGY | XLE | energy | 4.18% | 5.91% | -1.35% | 23.96% | -13.21% | -0.897 | -0.163 | -0.276 | -0.16% |
| MATERIALS | XLB | materials_and_mining | -0.11% | 2.05% | -14.34% | 19.25% | -4.75% | -0.475 | 0.535 | 0.739 | -1.35% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.41% | -4.78% | -9.80% | 15.47% | -6.83% | -0.458 | 0.125 | 0.145 | -6.54% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.12% | -3.72% | -3.58% | 16.17% | -4.19% | -0.427 | 0.249 | 0.276 | -2.22% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.45% | -2.36% | -11.85% | 4.83% | -2.00% | -0.137 | 0.292 | 0.105 | -2.82% |
| LONG_TREASURY | TLT | rates_and_duration | 1.11% | -3.14% | -14.41% | 9.61% | -6.26% | 0.318 | 0.240 | 0.176 | -6.50% |
| TIPS | TIP | rates_and_duration | 0.55% | -3.20% | -9.97% | 4.05% | -1.97% | -0.453 | 0.257 | 0.070 | -1.42% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.42% | -3.64% | -11.13% | 5.79% | -3.31% | -0.370 | 0.481 | 0.202 | -2.81% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.13% | -2.22% | -8.63% | 3.42% | -0.80% | -0.628 | 0.784 | 0.237 | -0.10% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.40% | -3.09% | -10.51% | 4.41% | -1.82% | -0.256 | 0.398 | 0.118 | -1.92% |
| DEVELOPED_EX_US | VEA | international_equity | -0.64% | 0.57% | -6.49% | 19.33% | -4.85% | -0.851 | 0.803 | 1.083 | -1.17% |
| EMERGING_MARKETS | VWO | international_equity | -0.61% | -0.77% | -7.92% | 19.37% | -7.05% | -0.689 | 0.813 | 1.112 | -1.96% |
| EUROPE | VGK | international_equity | -0.02% | 1.10% | -7.73% | 15.19% | -3.12% | -0.784 | 0.739 | 0.904 | -0.40% |
| JAPAN | EWJ | international_equity | -3.08% | -0.58% | -7.57% | 23.78% | -7.86% | -0.945 | 0.720 | 1.182 | -3.75% |
| CHINA | MCHI | international_equity | 0.56% | -0.47% | -19.65% | 19.70% | -12.54% | -0.541 | 0.547 | 0.872 | -15.75% |
| INDIA | INDA | international_equity | -0.82% | -1.22% | -18.13% | 13.27% | -4.59% | -0.634 | 0.551 | 0.644 | -10.40% |
| GOLD | IAU | precious_metals | 2.24% | 7.66% | -27.76% | 25.95% | -12.55% | -0.455 | 0.312 | 0.692 | -16.47% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.00% | 2.69% | 14.27% | 22.64% | -16.24% | -0.367 | -0.180 | -0.283 | -3.07% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.09% | -6.74% | 31.97% | 54.10% | -24.62% | 0.332 | 0.783 | 2.379 | -16.14% |
| SOFTWARE | IGV | technology_and_growth | -0.26% | 9.19% | 2.38% | 35.38% | -21.29% | -0.900 | 0.510 | 1.191 | -12.70% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.22% | 4.53% | 9.09% | 40.05% | -20.19% | -0.550 | 0.853 | 1.934 | -10.19% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.26% | 3.88% | -11.66% | 38.77% | -23.82% | -0.700 | 0.795 | 2.177 | -12.38% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.83% | 2.70% | 28.13% | 32.82% | -11.74% | -0.447 | 0.537 | 1.107 | -6.52% |
| SOLAR | TAN | clean_energy | -3.55% | -8.86% | -20.68% | 45.63% | -35.51% | -0.116 | 0.632 | 1.906 | -31.73% |
| METALS_MINING | XME | materials_and_mining | 0.24% | 12.45% | -22.73% | 41.51% | -26.49% | -0.237 | 0.597 | 1.748 | -11.80% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.45% | 1.60% | -4.24% | 11.08% | -2.04% | -0.811 | 0.771 | 0.701 | -0.31% |
| BIOTECH | XBI | healthcare_and_biotech | 6.37% | 6.96% | 13.52% | 31.08% | -10.51% | -0.486 | 0.468 | 1.004 | 0.00% |
| REGIONAL_BANKS | KRE | financials | -3.08% | -3.95% | -2.28% | 19.54% | -3.76% | -0.838 | 0.428 | 0.753 | -3.76% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.17% | 3.83% | -10.18% | 26.43% | -8.58% | -0.394 | 0.559 | 1.005 | -2.79% |
| CANADA | EWC | international_equity | 0.10% | 1.93% | -4.53% | 11.77% | -3.20% | -0.393 | 0.674 | 0.746 | -0.64% |
| UNITED_KINGDOM | EWU | international_equity | 0.41% | 0.63% | -8.27% | 14.45% | -3.40% | -0.554 | 0.592 | 0.687 | -0.23% |
| AUSTRALIA | EWA | international_equity | 0.27% | 1.72% | -10.39% | 16.56% | -4.78% | -0.777 | 0.672 | 0.924 | -1.45% |
| SOUTH_KOREA | EWY | international_equity | -0.82% | -1.89% | 20.46% | 80.71% | -34.21% | 0.139 | 0.640 | 2.774 | -20.42% |
| TAIWAN | EWT | international_equity | -1.39% | 6.35% | 22.01% | 44.17% | -19.83% | -0.767 | 0.763 | 1.870 | -6.12% |
| BRAZIL | EWZ | international_equity | 1.18% | -6.22% | -14.71% | 22.11% | -8.97% | -0.750 | 0.504 | 0.988 | -17.12% |
| MEXICO | EWW | international_equity | -1.73% | -2.88% | -14.11% | 18.76% | -6.47% | -0.449 | 0.537 | 0.917 | -6.14% |
| SOUTH_AFRICA | EZA | international_equity | 2.87% | 8.90% | -22.87% | 32.18% | -12.38% | -0.566 | 0.618 | 1.582 | -11.97% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.41% | -2.98% | -10.36% | 5.28% | -2.02% | -0.063 | 0.392 | 0.138 | -1.74% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.28% | -2.97% | -10.27% | 3.06% | -2.15% | 1.259 | 0.388 | 0.091 | -1.49% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.18% | -3.28% | -9.17% | 5.88% | -1.96% | -0.693 | 0.683 | 0.307 | -1.36% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.17% | -2.72% | -10.68% | 3.74% | -1.45% | -0.617 | 0.466 | 0.129 | -1.61% |
| SILVER | SLV | precious_metals | 1.61% | 10.28% | -33.88% | 44.29% | -27.73% | -0.512 | 0.356 | 1.715 | -43.17% |
| COPPER | CPER | non_energy_commodities | -1.57% | -3.13% | 1.49% | 25.48% | -10.57% | -0.388 | 0.547 | 1.198 | -3.57% |
| AGRICULTURE | DBA | non_energy_commodities | 1.62% | -0.24% | -3.05% | 14.02% | -7.21% | -0.580 | 0.069 | 0.061 | -1.53% |
| OIL | USO | energy | 2.84% | -1.18% | 52.67% | 53.37% | -32.49% | -0.573 | -0.336 | -1.252 | -14.42% |
| US_DOLLAR | UUP | currencies | -1.13% | -4.88% | -4.44% | 5.14% | -2.52% | -0.463 | -0.308 | -0.139 | -2.52% |
| EURO | FXE | currencies | 1.35% | -0.68% | -12.91% | 5.10% | -2.66% | -0.795 | 0.288 | 0.130 | -2.62% |
| YEN | FXY | currencies | 0.87% | -0.01% | -15.48% | 7.81% | -3.11% | 1.541 | 0.185 | 0.118 | -7.64% |
| BITCOIN_ETF | IBIT | crypto_assets | 8.05% | 0.17% | -9.27% | 37.59% | -24.34% | -0.469 | 0.501 | 1.732 | -45.60% |
| ETHEREUM_ETF | ETHA | crypto_assets | 12.15% | 6.51% | -10.30% | 55.29% | -27.31% | -0.286 | 0.525 | 2.716 | -56.60% |
