# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-23
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.67% |
| spy_return_21s | 0.63% |
| rsp_return_5s | -1.46% |
| rsp_return_21s | 1.45% |
| hyg_return_5s | -0.71% |
| hyg_return_21s | -0.34% |
| tlt_return_5s | -1.24% |
| tlt_return_21s | -3.16% |
| uup_return_5s | 0.78% |
| uup_return_21s | 0.39% |
| uso_return_5s | 16.92% |
| uso_return_21s | 25.37% |
| iau_return_5s | 1.80% |
| iau_return_21s | -1.53% |
| rsp_minus_spy_5s | 0.21% |
| rsp_minus_spy_21s | 0.82% |
| positive_asset_share_5s | 30.43% |
| positive_asset_share_21s | 49.28% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.63% | -7.60% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -0.33% | -6.11% | 0.21% | -0.01% | -0.182 | -0.109 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.67% | 0.00% | 0.00% | 13.07% | -4.49% | -0.956 | 1.000 | 1.000 | -2.57% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.59% | -0.07% | -0.00% | 13.01% | -4.36% | -0.847 | 0.995 | 1.013 | -2.30% |
| NASDAQ100 | QQQ | technology_and_growth | -1.98% | -3.67% | 8.47% | 24.54% | -7.16% | -0.940 | 0.933 | 1.389 | -7.16% |
| LARGE_GROWTH | IWF | technology_and_growth | -2.15% | -1.65% | -3.78% | 18.94% | -8.21% | -0.600 | 0.937 | 1.261 | -7.82% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.31% | 1.54% | 3.13% | 11.80% | -2.40% | -0.106 | 0.809 | 0.719 | -1.31% |
| MID_CAP | IJH | diversified_us_equity | -0.71% | -0.43% | -0.03% | 14.53% | -4.25% | -0.994 | 0.800 | 0.990 | -2.15% |
| SMALL_CAP | IWM | diversified_us_equity | -1.18% | -1.72% | 3.14% | 18.37% | -4.81% | -1.148 | 0.815 | 1.244 | -2.78% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.61% | 0.77% | 3.19% | 15.34% | -4.01% | -0.580 | 0.734 | 1.010 | -1.61% |
| DIVIDEND | SCHD | diversified_us_equity | -0.73% | 2.62% | 3.18% | 11.92% | -2.95% | -0.469 | 0.317 | 0.274 | -0.73% |
| LOW_VOL | SPLV | diversified_us_equity | -0.57% | 2.46% | -4.97% | 13.22% | -4.09% | -0.820 | 0.042 | 0.035 | -0.57% |
| MOMENTUM | MTUM | diversified_us_equity | 3.48% | -5.41% | 21.78% | 36.23% | -12.49% | 1.458 | 0.784 | 1.503 | -9.05% |
| TECHNOLOGY | XLK | technology_and_growth | 0.52% | -3.74% | 20.79% | 33.27% | -11.31% | -0.961 | 0.863 | 1.679 | -9.86% |
| COMMUNICATIONS | XLC | technology_and_growth | -6.45% | -2.39% | -13.48% | 16.62% | -10.37% | 0.060 | 0.630 | 0.711 | -11.73% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -7.31% | -5.02% | -13.52% | 20.56% | -10.72% | -0.332 | 0.795 | 1.204 | -12.31% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -3.03% | -1.24% | -4.77% | 16.65% | -4.95% | -0.892 | -0.046 | -0.050 | -6.39% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.22% | 5.46% | -10.62% | 18.17% | -3.74% | -0.482 | 0.260 | 0.323 | -1.82% |
| FINANCIALS | XLF | financials | -1.62% | 2.99% | -5.94% | 13.09% | -2.57% | -0.767 | 0.559 | 0.644 | -1.62% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.99% | 1.50% | 0.05% | 19.37% | -4.60% | -1.063 | 0.713 | 0.938 | -1.95% |
| ENERGY | XLE | energy | 4.14% | 8.41% | 5.66% | 24.04% | -13.21% | -0.963 | -0.122 | -0.202 | -4.40% |
| MATERIALS | XLB | materials_and_mining | -1.18% | -1.77% | -3.44% | 19.37% | -6.43% | -0.682 | 0.550 | 0.761 | -5.44% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.58% | 1.86% | -1.43% | 17.77% | -8.00% | -0.798 | 0.129 | 0.152 | -1.93% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.12% | 0.07% | 1.51% | 15.77% | -3.38% | -0.813 | 0.254 | 0.285 | -1.12% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.93% | -1.65% | -7.76% | 4.96% | -2.24% | -0.885 | 0.215 | 0.080 | -3.70% |
| LONG_TREASURY | TLT | rates_and_duration | -1.24% | -3.79% | -7.00% | 8.78% | -4.54% | -0.883 | 0.171 | 0.126 | -6.70% |
| TIPS | TIP | rates_and_duration | -0.44% | -0.96% | -7.05% | 3.56% | -1.44% | -0.567 | 0.236 | 0.065 | -1.44% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.15% | -2.72% | -7.21% | 5.28% | -2.80% | -0.428 | 0.418 | 0.174 | -3.09% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.71% | -0.97% | -6.65% | 3.65% | -1.01% | -0.766 | 0.769 | 0.232 | -0.80% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.81% | -1.68% | -7.25% | 4.10% | -1.71% | -0.231 | 0.324 | 0.097 | -2.40% |
| DEVELOPED_EX_US | VEA | international_equity | -0.36% | -1.18% | 1.09% | 20.74% | -4.85% | -0.636 | 0.799 | 1.078 | -3.61% |
| EMERGING_MARKETS | VWO | international_equity | -1.26% | -2.75% | -1.68% | 20.59% | -5.67% | -0.490 | 0.801 | 1.096 | -5.13% |
| EUROPE | VGK | international_equity | -1.08% | 0.14% | -4.16% | 18.05% | -3.86% | -1.029 | 0.741 | 0.934 | -2.38% |
| JAPAN | EWJ | international_equity | -0.88% | -2.41% | 2.40% | 22.13% | -6.74% | -0.768 | 0.709 | 1.174 | -6.05% |
| CHINA | MCHI | international_equity | -1.46% | 2.35% | -24.14% | 21.01% | -15.01% | -0.174 | 0.575 | 0.929 | -18.85% |
| INDIA | INDA | international_equity | -2.18% | -3.56% | -12.41% | 15.36% | -5.64% | -0.712 | 0.518 | 0.613 | -13.85% |
| GOLD | IAU | precious_metals | 1.80% | -2.15% | -22.50% | 23.94% | -16.13% | -0.582 | 0.305 | 0.671 | -25.03% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 6.49% | 10.99% | 7.32% | 20.91% | -16.55% | 0.117 | -0.123 | -0.184 | -4.49% |
| SEMICONDUCTORS | SMH | technology_and_growth | 1.98% | -7.36% | 47.17% | 52.76% | -16.80% | 0.461 | 0.783 | 2.294 | -13.27% |
| SOFTWARE | IGV | technology_and_growth | -7.04% | -0.88% | -16.05% | 34.99% | -21.29% | -0.644 | 0.513 | 1.167 | -26.04% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.03% | -6.97% | 14.46% | 39.42% | -16.31% | -0.051 | 0.849 | 1.866 | -15.41% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.09% | -8.15% | -10.48% | 38.40% | -19.25% | -1.046 | 0.794 | 2.151 | -18.75% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.54% | 3.63% | 12.79% | 33.15% | -11.74% | 0.075 | 0.532 | 1.085 | -7.40% |
| SOLAR | TAN | clean_energy | -2.45% | -10.38% | 4.48% | 44.85% | -28.73% | -0.964 | 0.587 | 1.780 | -28.51% |
| METALS_MINING | XME | materials_and_mining | 4.22% | -7.60% | -20.72% | 40.26% | -26.37% | -0.540 | 0.587 | 1.686 | -22.28% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.46% | 0.82% | -1.98% | 10.75% | -2.04% | -0.794 | 0.780 | 0.719 | -1.46% |
| BIOTECH | XBI | healthcare_and_biotech | 0.15% | 2.91% | 7.22% | 30.68% | -8.12% | -0.037 | 0.479 | 1.007 | -7.34% |
| REGIONAL_BANKS | KRE | financials | -3.55% | 2.15% | -2.04% | 20.59% | -5.29% | -0.608 | 0.446 | 0.805 | -3.55% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 3.18% | 0.35% | -9.27% | 25.01% | -8.58% | -0.484 | 0.559 | 0.979 | -5.00% |
| CANADA | EWC | international_equity | -0.96% | 1.37% | -2.29% | 13.10% | -3.20% | -0.651 | 0.679 | 0.765 | -1.13% |
| UNITED_KINGDOM | EWU | international_equity | -0.57% | 1.85% | -5.24% | 16.89% | -3.94% | -0.473 | 0.611 | 0.719 | -2.69% |
| AUSTRALIA | EWA | international_equity | -0.49% | 1.05% | -1.18% | 18.29% | -6.84% | -0.825 | 0.675 | 0.921 | -4.53% |
| SOUTH_KOREA | EWY | international_equity | 6.43% | -10.17% | 58.58% | 77.36% | -25.85% | 0.302 | 0.644 | 2.631 | -20.68% |
| TAIWAN | EWT | international_equity | -0.32% | -5.76% | 48.43% | 42.24% | -13.98% | 0.128 | 0.747 | 1.738 | -10.48% |
| BRAZIL | EWZ | international_equity | 2.38% | 5.29% | -9.15% | 23.76% | -17.00% | -1.072 | 0.507 | 1.000 | -12.50% |
| MEXICO | EWW | international_equity | -0.29% | -0.27% | -6.97% | 20.61% | -7.30% | -0.751 | 0.533 | 0.928 | -6.31% |
| SOUTH_AFRICA | EZA | international_equity | -3.99% | -6.10% | -18.74% | 33.26% | -14.17% | -0.479 | 0.625 | 1.595 | -24.32% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.94% | -1.82% | -7.02% | 4.80% | -1.97% | -0.559 | 0.321 | 0.112 | -2.46% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -1.28% | -2.23% | -6.49% | 2.96% | -2.15% | -0.234 | 0.323 | 0.075 | -2.15% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.11% | -2.02% | -5.65% | 5.83% | -2.10% | -0.709 | 0.662 | 0.294 | -1.96% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.52% | -1.79% | -6.56% | 4.19% | -1.44% | -0.416 | 0.409 | 0.113 | -1.92% |
| SILVER | SLV | precious_metals | 3.31% | -7.21% | -41.22% | 50.50% | -36.50% | -0.686 | 0.353 | 1.703 | -50.70% |
| COPPER | CPER | non_energy_commodities | 0.47% | 1.84% | -3.00% | 29.36% | -10.57% | -0.688 | 0.464 | 1.251 | -5.81% |
| AGRICULTURE | DBA | non_energy_commodities | 2.36% | 5.54% | -3.49% | 13.49% | -8.67% | -0.307 | 0.079 | 0.067 | -1.71% |
| OIL | USO | energy | 16.92% | 24.75% | 44.11% | 51.65% | -32.49% | -0.559 | -0.298 | -1.066 | -8.81% |
| US_DOLLAR | UUP | currencies | 0.78% | -0.24% | -3.27% | 4.91% | -0.98% | -0.231 | -0.280 | -0.131 | 0.00% |
| EURO | FXE | currencies | -0.51% | -0.56% | -9.95% | 4.65% | -3.57% | -0.811 | 0.261 | 0.126 | -5.11% |
| YEN | FXY | currencies | -0.78% | -2.02% | -9.79% | 6.51% | -4.57% | -0.197 | 0.111 | 0.069 | -10.88% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.71% | 3.17% | -38.51% | 36.89% | -28.36% | -0.422 | 0.513 | 1.791 | -48.59% |
| ETHEREUM_ETF | ETHA | crypto_assets | -0.14% | 12.07% | -52.88% | 52.48% | -35.25% | -0.400 | 0.550 | 2.926 | -61.44% |
