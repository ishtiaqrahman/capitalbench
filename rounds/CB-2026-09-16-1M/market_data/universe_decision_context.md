# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-16
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.10% |
| spy_return_21s | -2.41% |
| rsp_return_5s | -1.10% |
| rsp_return_21s | -3.85% |
| hyg_return_5s | -0.71% |
| hyg_return_21s | -0.95% |
| tlt_return_5s | -1.04% |
| tlt_return_21s | -0.20% |
| uup_return_5s | 1.50% |
| uup_return_21s | 1.07% |
| uso_return_5s | 4.13% |
| uso_return_21s | 19.86% |
| iau_return_5s | -2.87% |
| iau_return_21s | -3.36% |
| rsp_minus_spy_5s | -0.00% |
| rsp_minus_spy_21s | -1.44% |
| positive_asset_share_5s | 14.49% |
| positive_asset_share_21s | 21.74% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 2.41% | -15.80% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 2.67% | -14.29% | 0.20% | -0.01% | -0.440 | -0.082 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.10% | 0.00% | 0.00% | 11.72% | -3.38% | -0.903 | 1.000 | 1.000 | -3.06% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.14% | -0.43% | 0.50% | 11.58% | -3.39% | -0.655 | 0.995 | 1.012 | -3.39% |
| NASDAQ100 | QQQ | technology_and_growth | -1.62% | -1.04% | 5.46% | 21.25% | -10.55% | -1.008 | 0.929 | 1.420 | -5.45% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.48% | -1.13% | -2.95% | 19.33% | -8.15% | -0.640 | 0.934 | 1.286 | -6.23% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.78% | 0.64% | 2.91% | 9.86% | -2.81% | -0.482 | 0.804 | 0.703 | -2.81% |
| MID_CAP | IJH | diversified_us_equity | -2.06% | -4.54% | 0.20% | 12.46% | -7.18% | -0.632 | 0.815 | 0.978 | -7.18% |
| SMALL_CAP | IWM | diversified_us_equity | -2.06% | -3.97% | 6.08% | 13.57% | -6.69% | -0.808 | 0.821 | 1.198 | -6.69% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.70% | -1.88% | 4.75% | 11.02% | -4.70% | -0.775 | 0.739 | 0.938 | -4.70% |
| DIVIDEND | SCHD | diversified_us_equity | -0.73% | 1.10% | -3.19% | 12.16% | -3.89% | 0.139 | 0.292 | 0.254 | -3.89% |
| LOW_VOL | SPLV | diversified_us_equity | -1.49% | -1.13% | -13.97% | 11.71% | -6.30% | -0.662 | 0.024 | 0.020 | -6.30% |
| MOMENTUM | MTUM | diversified_us_equity | -2.86% | -4.31% | 14.08% | 33.68% | -17.99% | -0.589 | 0.763 | 1.565 | -12.97% |
| TECHNOLOGY | XLK | technology_and_growth | -2.10% | -0.95% | 20.92% | 29.28% | -13.31% | -1.179 | 0.851 | 1.744 | -7.09% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.96% | 4.38% | -19.19% | 20.44% | -7.06% | -0.907 | 0.557 | 0.664 | -5.35% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.03% | -3.22% | -12.24% | 20.75% | -8.08% | -0.853 | 0.768 | 1.162 | -11.16% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.34% | 0.82% | -14.56% | 16.95% | -5.03% | -0.644 | -0.056 | -0.063 | -6.25% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.71% | 2.84% | -3.22% | 19.37% | -5.87% | -0.828 | 0.224 | 0.281 | -4.50% |
| FINANCIALS | XLF | financials | -1.98% | -0.46% | 1.38% | 12.96% | -4.49% | -0.612 | 0.543 | 0.617 | -4.49% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.79% | -7.04% | -3.31% | 16.33% | -9.54% | -0.487 | 0.713 | 0.957 | -9.54% |
| ENERGY | XLE | energy | -1.96% | 4.73% | -7.39% | 21.58% | -3.93% | -0.607 | -0.176 | -0.301 | -2.88% |
| MATERIALS | XLB | materials_and_mining | -2.00% | -1.19% | -9.45% | 17.26% | -6.17% | -0.318 | 0.538 | 0.744 | -6.17% |
| UTILITIES | XLU | rate_sensitive_defensive | -3.77% | -4.06% | -20.81% | 14.52% | -10.74% | -0.198 | 0.121 | 0.143 | -12.28% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.38% | -2.10% | -9.25% | 14.60% | -6.96% | -0.480 | 0.250 | 0.273 | -6.96% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.27% | 0.49% | -17.66% | 4.72% | -3.57% | -0.191 | 0.287 | 0.103 | -5.23% |
| LONG_TREASURY | TLT | rates_and_duration | -1.04% | 2.21% | -20.96% | 9.39% | -6.63% | 0.157 | 0.236 | 0.168 | -8.55% |
| TIPS | TIP | rates_and_duration | -1.32% | 1.12% | -16.72% | 3.66% | -2.45% | -0.277 | 0.252 | 0.065 | -2.65% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.82% | 1.64% | -17.18% | 5.21% | -3.79% | -0.435 | 0.470 | 0.191 | -3.92% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.71% | 1.46% | -13.57% | 2.80% | -1.39% | -0.371 | 0.773 | 0.228 | -1.34% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.90% | 1.27% | -16.70% | 3.94% | -2.58% | -0.189 | 0.395 | 0.115 | -3.27% |
| DEVELOPED_EX_US | VEA | international_equity | -2.14% | -0.89% | -2.36% | 16.03% | -4.75% | -0.601 | 0.802 | 1.088 | -3.43% |
| EMERGING_MARKETS | VWO | international_equity | -2.78% | 0.41% | -6.39% | 15.83% | -7.05% | -0.755 | 0.814 | 1.114 | -3.68% |
| EUROPE | VGK | international_equity | -1.75% | -1.36% | -4.00% | 12.10% | -4.89% | -0.856 | 0.749 | 0.915 | -4.89% |
| JAPAN | EWJ | international_equity | 0.01% | 1.23% | 0.20% | 21.69% | -7.86% | -0.740 | 0.727 | 1.188 | -1.57% |
| CHINA | MCHI | international_equity | -1.93% | -2.58% | -20.97% | 16.76% | -8.12% | -0.932 | 0.561 | 0.860 | -20.43% |
| INDIA | INDA | international_equity | -2.49% | -1.87% | -13.62% | 12.77% | -6.08% | -0.724 | 0.562 | 0.669 | -14.16% |
| GOLD | IAU | precious_metals | -2.87% | -0.95% | -27.45% | 24.55% | -8.48% | -0.257 | 0.333 | 0.753 | -20.92% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.02% | 11.14% | -9.74% | 22.08% | -6.42% | -0.419 | -0.185 | -0.295 | -1.49% |
| SEMICONDUCTORS | SMH | technology_and_growth | -5.00% | -5.76% | 33.88% | 45.99% | -24.62% | -0.868 | 0.770 | 2.379 | -18.44% |
| SOFTWARE | IGV | technology_and_growth | 3.07% | 5.32% | 3.46% | 34.18% | -8.27% | -1.103 | 0.496 | 1.228 | -10.88% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.72% | 0.86% | 13.28% | 31.24% | -16.56% | -0.845 | 0.849 | 1.923 | -10.16% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.16% | -6.08% | -8.73% | 31.44% | -17.73% | -1.172 | 0.804 | 2.192 | -16.99% |
| CYBERSECURITY | CIBR | technology_and_growth | 6.16% | 4.98% | 35.11% | 32.98% | -9.53% | 0.099 | 0.504 | 1.129 | -1.86% |
| SOLAR | TAN | clean_energy | -6.54% | -9.96% | -27.61% | 36.10% | -26.98% | -0.562 | 0.640 | 1.904 | -39.65% |
| METALS_MINING | XME | materials_and_mining | -8.74% | -5.49% | -9.05% | 36.48% | -18.17% | -0.407 | 0.597 | 1.775 | -18.06% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.10% | -1.44% | -2.27% | 10.57% | -4.71% | -0.939 | 0.778 | 0.704 | -4.71% |
| BIOTECH | XBI | healthcare_and_biotech | -3.26% | -0.94% | 12.78% | 29.26% | -10.51% | -0.131 | 0.484 | 1.053 | -9.07% |
| REGIONAL_BANKS | KRE | financials | -0.97% | -3.60% | 7.57% | 17.15% | -6.81% | -0.348 | 0.418 | 0.722 | -6.66% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.79% | -11.79% | -7.87% | 21.31% | -15.39% | -0.254 | 0.571 | 1.034 | -14.89% |
| CANADA | EWC | international_equity | -1.85% | -1.32% | -4.05% | 11.42% | -4.44% | -0.367 | 0.678 | 0.763 | -4.44% |
| UNITED_KINGDOM | EWU | international_equity | -0.77% | 0.96% | -10.28% | 11.70% | -3.91% | -0.606 | 0.604 | 0.702 | -3.91% |
| AUSTRALIA | EWA | international_equity | -3.81% | -1.18% | -11.38% | 15.18% | -6.38% | -0.076 | 0.676 | 0.939 | -6.38% |
| SOUTH_KOREA | EWY | international_equity | -7.99% | -2.75% | 21.89% | 66.97% | -34.21% | -0.923 | 0.633 | 2.788 | -19.92% |
| TAIWAN | EWT | international_equity | -3.01% | 2.97% | 31.87% | 37.26% | -19.83% | -1.102 | 0.750 | 1.842 | -3.37% |
| BRAZIL | EWZ | international_equity | -1.55% | 12.74% | -22.38% | 21.88% | -8.05% | -0.104 | 0.478 | 0.938 | -9.33% |
| MEXICO | EWW | international_equity | -4.72% | -0.29% | -12.22% | 16.57% | -6.53% | -0.694 | 0.551 | 0.942 | -8.95% |
| SOUTH_AFRICA | EZA | international_equity | -5.27% | 1.47% | -15.15% | 26.92% | -11.18% | -0.470 | 0.633 | 1.631 | -15.47% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.08% | 0.81% | -16.62% | 4.68% | -2.89% | 0.377 | 0.390 | 0.134 | -3.49% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.64% | 0.08% | -16.03% | 3.50% | -3.98% | 3.312 | 0.392 | 0.092 | -3.89% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.18% | 1.11% | -14.02% | 4.91% | -2.71% | -0.298 | 0.685 | 0.302 | -2.64% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.55% | 1.23% | -15.98% | 3.61% | -2.69% | -0.173 | 0.466 | 0.132 | -2.95% |
| SILVER | SLV | precious_metals | -6.04% | -1.82% | -32.67% | 41.22% | -20.51% | -0.541 | 0.368 | 1.789 | -45.98% |
| COPPER | CPER | non_energy_commodities | -5.99% | -1.43% | -1.83% | 24.20% | -8.19% | -0.296 | 0.553 | 1.243 | -5.99% |
| AGRICULTURE | DBA | non_energy_commodities | -0.62% | 4.83% | -10.09% | 13.36% | -2.87% | 0.418 | 0.043 | 0.037 | -2.27% |
| OIL | USO | energy | 4.13% | 22.27% | -6.17% | 51.52% | -17.64% | -0.595 | -0.345 | -1.315 | -3.52% |
| US_DOLLAR | UUP | currencies | 1.50% | 3.48% | -14.28% | 5.42% | -2.52% | -0.969 | -0.296 | -0.130 | -0.70% |
| EURO | FXE | currencies | -1.37% | 1.54% | -15.07% | 4.93% | -2.19% | -0.593 | 0.277 | 0.119 | -4.21% |
| YEN | FXY | currencies | -1.64% | 4.48% | -16.17% | 9.83% | -2.22% | 0.334 | 0.182 | 0.121 | -6.53% |
| BITCOIN_ETF | IBIT | crypto_assets | -2.82% | 20.59% | -29.64% | 37.60% | -10.44% | 1.088 | 0.489 | 1.723 | -39.63% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.31% | 28.45% | -33.70% | 49.14% | -13.29% | 2.028 | 0.510 | 2.564 | -49.29% |
