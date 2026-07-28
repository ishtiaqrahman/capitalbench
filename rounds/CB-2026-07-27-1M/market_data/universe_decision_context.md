# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume; yahoo_chart_history_with_tiingo_eod_frozen_entry_close
- As-of date requested: 2026-07-27
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.40% |
| spy_return_21s | 0.65% |
| rsp_return_5s | 1.30% |
| rsp_return_21s | 1.62% |
| hyg_return_5s | -0.51% |
| hyg_return_21s | -0.30% |
| tlt_return_5s | -0.17% |
| tlt_return_21s | -3.77% |
| uup_return_5s | 0.74% |
| uup_return_21s | 0.42% |
| uso_return_5s | -0.60% |
| uso_return_21s | 14.13% |
| iau_return_5s | 1.90% |
| iau_return_21s | 1.41% |
| rsp_minus_spy_5s | 1.70% |
| rsp_minus_spy_21s | 0.97% |
| positive_asset_share_5s | 53.62% |
| positive_asset_share_21s | 50.72% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.65% | -7.11% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -0.34% | -5.64% | 0.21% | -0.01% | -0.175 | -0.108 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.40% | 0.00% | 0.00% | 12.96% | -4.49% | -1.018 | 1.000 | 1.000 | -2.45% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.29% | -0.03% | 0.11% | 12.93% | -4.36% | -0.830 | 0.995 | 1.013 | -2.17% |
| NASDAQ100 | QQQ | technology_and_growth | -2.00% | -5.43% | 8.21% | 24.36% | -8.48% | -0.968 | 0.931 | 1.393 | -8.48% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.96% | -1.47% | -6.04% | 18.68% | -8.96% | -0.682 | 0.935 | 1.261 | -8.96% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.13% | 1.53% | 5.54% | 11.90% | -2.40% | -0.445 | 0.807 | 0.718 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 1.43% | -1.25% | 3.22% | 14.55% | -4.25% | -1.019 | 0.801 | 0.990 | -1.44% |
| SMALL_CAP | IWM | diversified_us_equity | 0.21% | -2.66% | 6.24% | 18.38% | -4.81% | -1.250 | 0.816 | 1.241 | -2.51% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.59% | 0.28% | 6.13% | 15.36% | -4.01% | -0.687 | 0.736 | 1.008 | -0.90% |
| DIVIDEND | SCHD | diversified_us_equity | 2.08% | 3.95% | 4.38% | 11.90% | -2.95% | -0.421 | 0.313 | 0.274 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 1.49% | 2.64% | -3.16% | 12.98% | -4.09% | -0.914 | 0.043 | 0.036 | 0.00% |
| MOMENTUM | MTUM | diversified_us_equity | -0.10% | -11.55% | 25.96% | 36.58% | -12.49% | 1.324 | 0.778 | 1.504 | -12.42% |
| TECHNOLOGY | XLK | technology_and_growth | -0.80% | -6.22% | 20.42% | 32.93% | -11.96% | -1.041 | 0.861 | 1.683 | -11.96% |
| COMMUNICATIONS | XLC | technology_and_growth | -2.83% | 1.32% | -16.31% | 16.73% | -9.99% | 0.006 | 0.626 | 0.711 | -9.82% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -3.29% | -2.87% | -14.68% | 20.65% | -10.72% | -0.341 | 0.795 | 1.205 | -10.63% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.59% | 1.04% | -4.59% | 16.70% | -4.95% | -0.910 | -0.046 | -0.051 | -3.97% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.61% | 4.34% | -7.44% | 17.92% | -3.74% | -0.633 | 0.255 | 0.315 | -0.63% |
| FINANCIALS | XLF | financials | 1.50% | 5.76% | -5.52% | 13.03% | -2.42% | -0.756 | 0.556 | 0.642 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | 2.85% | -1.15% | 5.60% | 18.98% | -4.60% | -1.141 | 0.712 | 0.933 | -1.27% |
| ENERGY | XLE | energy | 0.72% | 7.24% | 4.37% | 24.41% | -13.21% | -0.914 | -0.126 | -0.208 | -6.04% |
| MATERIALS | XLB | materials_and_mining | 2.72% | -1.52% | -2.51% | 19.76% | -6.43% | -0.660 | 0.548 | 0.762 | -3.37% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.65% | -1.02% | 2.07% | 17.14% | -8.00% | -0.856 | 0.132 | 0.156 | -3.01% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.17% | 1.97% | 2.67% | 16.22% | -3.38% | -0.832 | 0.251 | 0.285 | -0.41% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.28% | -1.92% | -6.71% | 4.99% | -2.24% | -0.903 | 0.220 | 0.082 | -3.26% |
| LONG_TREASURY | TLT | rates_and_duration | -0.17% | -4.42% | -5.89% | 8.86% | -4.54% | -0.904 | 0.175 | 0.129 | -6.05% |
| TIPS | TIP | rates_and_duration | -0.61% | -1.62% | -6.10% | 3.51% | -1.53% | -0.706 | 0.246 | 0.067 | -1.53% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.60% | -3.04% | -6.43% | 5.28% | -2.82% | -0.433 | 0.420 | 0.175 | -2.86% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.51% | -0.96% | -6.17% | 3.63% | -1.01% | -0.739 | 0.770 | 0.233 | -0.75% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.27% | -1.89% | -6.32% | 4.12% | -1.71% | -0.296 | 0.328 | 0.098 | -2.05% |
| DEVELOPED_EX_US | VEA | international_equity | 1.11% | -2.28% | 1.83% | 20.61% | -4.85% | -0.675 | 0.799 | 1.072 | -3.30% |
| EMERGING_MARKETS | VWO | international_equity | 0.52% | -1.62% | -3.41% | 20.11% | -5.67% | -0.496 | 0.799 | 1.096 | -4.92% |
| EUROPE | VGK | international_equity | 1.31% | 0.50% | -4.21% | 18.00% | -3.86% | -1.006 | 0.742 | 0.928 | -1.26% |
| JAPAN | EWJ | international_equity | 1.19% | -2.67% | 3.94% | 22.06% | -6.74% | -0.796 | 0.714 | 1.156 | -5.63% |
| CHINA | MCHI | international_equity | 0.33% | 6.20% | -25.63% | 20.97% | -15.01% | -0.280 | 0.571 | 0.927 | -17.47% |
| INDIA | INDA | international_equity | 0.70% | -1.74% | -10.64% | 15.74% | -5.64% | -0.677 | 0.514 | 0.614 | -11.58% |
| GOLD | IAU | precious_metals | 1.90% | 0.76% | -26.38% | 23.94% | -16.01% | -0.601 | 0.309 | 0.679 | -24.41% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.23% | 6.98% | 5.24% | 21.85% | -16.55% | 0.128 | -0.119 | -0.182 | -8.30% |
| SEMICONDUCTORS | SMH | technology_and_growth | -1.84% | -14.52% | 52.08% | 52.57% | -17.99% | 0.855 | 0.779 | 2.303 | -17.99% |
| SOFTWARE | IGV | technology_and_growth | -2.23% | 6.60% | -20.34% | 33.41% | -21.29% | -0.651 | 0.509 | 1.166 | -22.81% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.42% | -9.81% | 15.12% | 38.89% | -17.34% | -0.261 | 0.845 | 1.866 | -16.88% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.51% | -7.90% | -12.02% | 38.57% | -20.72% | -1.022 | 0.792 | 2.144 | -20.13% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.93% | 5.85% | 11.35% | 32.25% | -11.74% | -0.206 | 0.532 | 1.087 | -5.94% |
| SOLAR | TAN | clean_energy | -2.14% | -11.56% | -2.33% | 44.86% | -30.64% | -0.920 | 0.590 | 1.797 | -30.26% |
| METALS_MINING | XME | materials_and_mining | 5.49% | -5.83% | -24.27% | 39.92% | -26.37% | -0.493 | 0.587 | 1.690 | -22.32% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.30% | 0.97% | 0.30% | 10.90% | -2.04% | -0.920 | 0.777 | 0.718 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | -0.23% | -1.31% | 11.40% | 30.38% | -8.40% | -0.170 | 0.477 | 1.003 | -8.33% |
| REGIONAL_BANKS | KRE | financials | -0.49% | 0.35% | 4.78% | 20.26% | -5.29% | -0.627 | 0.448 | 0.808 | -3.08% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 6.39% | 2.10% | -5.99% | 24.97% | -8.58% | -0.451 | 0.555 | 0.971 | -2.74% |
| CANADA | EWC | international_equity | 1.31% | 2.42% | -3.30% | 13.14% | -3.20% |  | 0.680 | 0.767 | -0.17% |
| UNITED_KINGDOM | EWU | international_equity | 2.11% | 2.60% | -4.98% | 16.95% | -3.94% | -0.436 | 0.608 | 0.717 | -1.30% |
| AUSTRALIA | EWA | international_equity | 1.26% | 2.75% | -3.66% | 18.35% | -6.84% | -0.918 | 0.674 | 0.919 | -3.22% |
| SOUTH_KOREA | EWY | international_equity | -1.02% | -22.02% | 66.67% | 78.03% | -26.46% | 0.296 | 0.638 | 2.635 | -26.46% |
| TAIWAN | EWT | international_equity | 1.95% | -7.42% | 43.39% | 41.24% | -13.98% | 0.005 | 0.744 | 1.736 | -12.30% |
| BRAZIL | EWZ | international_equity | 1.10% | 4.29% | -12.80% | 23.78% | -15.65% | -1.119 | 0.505 | 0.995 | -13.22% |
| MEXICO | EWW | international_equity | 1.93% | 0.68% | -6.37% | 20.66% | -7.30% | -0.759 | 0.530 | 0.920 | -4.39% |
| SOUTH_AFRICA | EZA | international_equity | 0.50% | -2.60% | -22.54% | 32.93% | -14.17% | -0.573 | 0.625 | 1.597 | -22.43% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.21% | -1.93% | -6.01% | 4.83% | -1.93% | -0.619 | 0.327 | 0.115 | -1.95% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.56% | -2.04% | -5.80% | 3.06% | -2.15% | 0.127 | 0.324 | 0.076 | -1.65% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.43% | -1.90% | -5.07% | 5.77% | -2.10% | -0.674 | 0.662 | 0.294 | -1.51% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.21% | -1.60% | -5.88% | 4.21% | -1.44% | -0.540 | 0.417 | 0.115 | -1.49% |
| SILVER | SLV | precious_metals | 3.83% | 0.44% | -50.75% | 50.34% | -36.50% | -0.679 | 0.354 | 1.711 | -49.88% |
| COPPER | CPER | non_energy_commodities | 0.91% | 4.19% | -5.85% | 29.22% | -10.57% | -0.709 | 0.462 | 1.248 | -4.51% |
| AGRICULTURE | DBA | non_energy_commodities | -1.43% | 1.95% | -2.52% | 14.09% | -8.67% | -0.332 | 0.073 | 0.064 | -3.86% |
| OIL | USO | energy | -0.60% | 13.48% | 40.71% | 54.04% | -32.49% | -0.558 | -0.291 | -1.066 | -18.44% |
| US_DOLLAR | UUP | currencies | 0.74% | -0.23% | -1.27% | 4.88% | -0.98% | -0.290 | -0.279 | -0.131 | 0.00% |
| EURO | FXE | currencies | -0.40% | -0.58% | -10.66% | 4.59% | -3.57% | -0.812 | 0.260 | 0.125 | -5.18% |
| YEN | FXY | currencies | -0.80% | -1.85% | -11.05% | 6.50% | -4.57% | -0.087 | 0.111 | 0.069 | -10.84% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.33% | 9.04% | -40.99% | 36.93% | -28.36% | -0.547 | 0.515 | 1.800 | -48.42% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.65% | 24.65% | -54.22% | 53.05% | -34.41% | -0.408 | 0.553 | 2.947 | -59.80% |
