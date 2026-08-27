# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume; yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-26
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.39% |
| spy_return_21s | 3.40% |
| rsp_return_5s | 0.02% |
| rsp_return_21s | 2.03% |
| hyg_return_5s | 0.24% |
| hyg_return_21s | 1.09% |
| tlt_return_5s | 0.34% |
| tlt_return_21s | -0.72% |
| uup_return_5s | 0.50% |
| uup_return_21s | -1.96% |
| uso_return_5s | -2.72% |
| uso_return_21s | 5.69% |
| iau_return_5s | 1.80% |
| iau_return_21s | 14.10% |
| rsp_minus_spy_5s | 0.41% |
| rsp_minus_spy_21s | -1.37% |
| positive_asset_share_5s | 52.17% |
| positive_asset_share_21s | 81.16% |
| active_return_dispersion_5s | 3.07% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.39% | -3.81% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | 0.45% | -3.57% | 0.17% | 0.00% | -0.892 | -0.122 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.05% | 0.00% | 0.00% | 12.96% | -1.96% | -1.146 | 1.000 | 1.000 | -1.52% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.00% | -0.08% | 0.02% | 13.20% | -2.01% | -0.630 | 0.993 | 0.987 | -1.58% |
| NASDAQ100 | QQQ | technology_and_growth | -0.29% | -0.27% | 2.20% | 21.91% | -3.52% | -0.914 | 0.920 | 1.718 | -4.56% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.52% | -0.36% | 1.51% | 20.49% | -3.68% | -0.489 | 0.904 | 1.393 | -5.37% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.45% | 0.27% | -1.14% | 8.76% | -1.00% | -0.171 | 0.697 | 0.567 | -0.12% |
| MID_CAP | IJH | diversified_us_equity | -0.20% | -0.16% | -2.48% | 14.04% | -3.22% | 0.148 | 0.791 | 0.783 | -2.61% |
| SMALL_CAP | IWM | diversified_us_equity | -0.34% | -0.54% | -0.96% | 15.47% | -2.43% | -0.987 | 0.787 | 0.951 | -2.02% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.21% | -0.18% | -3.14% | 10.84% | -1.59% | -0.869 | 0.651 | 0.630 | -1.36% |
| DIVIDEND | SCHD | diversified_us_equity | -0.17% | 0.27% | -0.27% | 10.53% | -1.42% | 0.226 | 0.107 | 0.092 | -0.45% |
| LOW_VOL | SPLV | diversified_us_equity | 0.94% | 0.44% | -6.36% | 8.67% | -3.41% | -0.555 | -0.297 | -0.283 | -2.50% |
| MOMENTUM | MTUM | diversified_us_equity | -0.38% | -0.23% | 0.83% | 31.90% | -6.67% | -0.947 | 0.699 | 1.948 | -11.94% |
| TECHNOLOGY | XLK | technology_and_growth | -0.26% | -0.05% | 3.53% | 31.82% | -5.62% | -1.162 | 0.829 | 2.114 | -7.64% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.09% | 1.55% | -2.30% | 19.84% | -2.82% | -1.122 | 0.404 | 0.580 | -5.67% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.73% | -0.82% | 1.63% | 18.93% | -2.92% | -1.248 | 0.675 | 1.067 | -5.54% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.33% | 0.08% | -4.40% | 15.39% | -3.07% | -0.644 | -0.282 | -0.361 | -2.94% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.62% | -0.83% | 1.23% | 19.25% | -3.09% | -1.000 | -0.125 | -0.182 | -1.22% |
| FINANCIALS | XLF | financials | 1.36% | 1.74% | -4.01% | 11.22% | -2.25% | -0.893 | 0.286 | 0.275 | -0.09% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.05% | -0.50% | -4.10% | 18.08% | -4.35% | -0.380 | 0.647 | 0.872 | -3.31% |
| ENERGY | XLE | energy | -1.90% | -1.42% | 6.63% | 23.69% | -3.76% | -0.771 | -0.315 | -0.522 | -2.07% |
| MATERIALS | XLB | materials_and_mining | 0.24% | 2.58% | -3.46% | 18.03% | -3.65% | -0.365 | 0.421 | 0.594 | 0.00% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.73% | -0.77% | -7.10% | 13.37% | -6.04% | -0.681 | -0.129 | -0.151 | -7.63% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.02% | 0.61% | -6.02% | 11.65% | -4.19% | -0.971 | -0.173 | -0.200 | -2.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.54% | 0.32% | -3.66% | 5.03% | -0.65% | -0.194 | 0.442 | 0.156 | -2.88% |
| LONG_TREASURY | TLT | rates_and_duration | 1.52% | 0.72% | -4.86% | 12.25% | -3.04% | 0.194 | 0.323 | 0.229 | -6.18% |
| TIPS | TIP | rates_and_duration | 0.35% | 0.39% | -3.21% | 3.19% | -0.36% | -0.144 | 0.396 | 0.102 | -0.69% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.81% | 0.58% | -3.62% | 6.17% | -0.99% | -0.488 | 0.518 | 0.202 | -2.19% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.36% | 0.63% | -2.95% | 2.74% | -0.33% | 0.019 | 0.816 | 0.181 | -0.03% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.52% | 0.43% | -3.56% | 4.41% | -0.56% | -1.031 | 0.485 | 0.142 | -1.54% |
| DEVELOPED_EX_US | VEA | international_equity | 0.04% | 1.24% | 0.83% | 16.13% | -1.76% | -0.249 | 0.809 | 1.112 | -0.46% |
| EMERGING_MARKETS | VWO | international_equity | 0.35% | 1.42% | 0.18% | 14.07% | -1.42% | -1.325 | 0.844 | 1.169 | -0.95% |
| EUROPE | VGK | international_equity | -0.02% | 0.90% | -0.44% | 11.07% | -1.13% | -0.766 | 0.733 | 0.760 | -0.53% |
| JAPAN | EWJ | international_equity | 0.26% | 1.07% | 1.70% | 22.63% | -4.27% | -1.288 | 0.751 | 1.300 | -3.09% |
| CHINA | MCHI | international_equity | -1.01% | -0.14% | -2.01% | 14.02% | -4.41% | -1.141 | 0.410 | 0.559 | -16.19% |
| INDIA | INDA | international_equity | 0.22% | 0.81% | -3.48% | 10.25% | -2.34% | -0.676 | 0.572 | 0.565 | -10.02% |
| GOLD | IAU | precious_metals | -0.48% | 2.19% | 8.27% | 24.92% | -1.68% | -0.027 | 0.478 | 0.915 | -14.97% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -2.52% | -0.43% | 3.64% | 22.14% | -3.81% | -0.292 | -0.172 | -0.274 | -3.86% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.83% | -0.53% | 2.11% | 42.77% | -7.96% | -0.829 | 0.747 | 2.895 | -16.91% |
| SOFTWARE | IGV | technology_and_growth | -0.95% | -0.02% | 8.21% | 30.28% | -4.17% | -1.259 | 0.475 | 1.225 | -13.06% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -0.57% | 0.51% | 6.24% | 29.90% | -3.59% | -0.564 | 0.828 | 2.355 | -10.08% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.59% | -2.53% | 7.13% | 36.72% | -6.62% | -1.135 | 0.858 | 2.375 | -14.94% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.25% | -1.58% | 3.21% | 29.76% | -9.53% | 0.107 | 0.559 | 1.332 | -8.36% |
| SOLAR | TAN | clean_energy | -1.09% | -2.96% | -1.02% | 37.42% | -9.46% | 0.172 | 0.772 | 2.435 | -34.02% |
| METALS_MINING | XME | materials_and_mining | 0.81% | 3.16% | 11.60% | 43.17% | -3.81% | 0.486 | 0.647 | 1.950 | -9.36% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.20% | 0.41% | -1.79% | 10.22% | -1.34% | -1.242 | 0.698 | 0.559 | -0.30% |
| BIOTECH | XBI | healthcare_and_biotech | 1.61% | -0.30% | 9.39% | 33.51% | -3.64% | 0.608 | 0.310 | 0.722 | -0.68% |
| REGIONAL_BANKS | KRE | financials | -0.37% | -0.17% | -6.14% | 13.42% | -4.62% | -0.705 | 0.153 | 0.210 | -4.30% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.40% | -3.58% | -3.33% | 25.15% | -7.83% | -0.355 | 0.431 | 0.797 | -6.65% |
| CANADA | EWC | international_equity | -0.21% | 1.03% | -0.48% | 10.28% | -1.04% | -0.715 | 0.595 | 0.509 | -0.65% |
| UNITED_KINGDOM | EWU | international_equity | -0.16% | 0.98% | -2.24% | 9.29% | -1.07% | -0.731 | 0.393 | 0.370 | -1.07% |
| AUSTRALIA | EWA | international_equity | 0.03% | 0.99% | -1.59% | 17.25% | -2.83% | -0.109 | 0.584 | 0.719 | -0.92% |
| SOUTH_KOREA | EWY | international_equity | 0.47% | 3.11% | 11.37% | 67.37% | -8.13% | -1.196 | 0.675 | 3.844 | -18.26% |
| TAIWAN | EWT | international_equity | 2.00% | 2.00% | 7.64% | 35.18% | -4.83% | -1.071 | 0.786 | 2.393 | -4.61% |
| BRAZIL | EWZ | international_equity | 1.88% | 4.65% | -8.77% | 23.23% | -8.05% | 0.590 | 0.391 | 0.617 | -13.58% |
| MEXICO | EWW | international_equity | 0.22% | 3.59% | -5.94% | 16.32% | -3.95% | -0.043 | 0.579 | 0.810 | -3.13% |
| SOUTH_AFRICA | EZA | international_equity | -1.14% | 2.37% | 9.60% | 30.45% | -3.77% | -0.709 | 0.673 | 1.526 | -10.30% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.49% | 0.40% | -3.55% | 5.18% | -0.80% | 0.450 | 0.490 | 0.167 | -1.36% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.10% | 0.17% | -3.84% | 2.91% | -0.77% | 0.112 | 0.539 | 0.114 | -1.70% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.62% | 0.60% | -3.45% | 5.73% | -0.76% | -0.935 | 0.731 | 0.289 | -0.72% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.27% | 0.47% | -4.08% | 4.04% | -0.83% | -0.281 | 0.485 | 0.127 | -1.53% |
| SILVER | SLV | precious_metals | -1.80% | 3.02% | 12.27% | 35.24% | -3.58% | 0.102 | 0.556 | 1.778 | -41.68% |
| COPPER | CPER | non_energy_commodities | 0.18% | 2.09% | -1.04% | 19.74% | -4.09% | -0.020 | 0.628 | 1.169 | -1.93% |
| AGRICULTURE | DBA | non_energy_commodities | 0.95% | 1.45% | -2.19% | 11.56% | -1.47% | 0.418 | 0.146 | 0.140 | -0.49% |
| OIL | USO | energy | -5.41% | -2.33% | 4.84% | 52.48% | -11.16% | -0.878 | -0.322 | -1.232 | -16.74% |
| US_DOLLAR | UUP | currencies | 0.43% | 0.89% | -6.26% | 5.81% | -2.45% | -1.625 | -0.389 | -0.147 | -2.03% |
| EURO | FXE | currencies | -0.19% | 0.22% | -1.19% | 4.92% | -0.32% | -0.490 | 0.402 | 0.145 | -2.71% |
| YEN | FXY | currencies | -0.26% | -0.42% | -0.20% | 12.25% | -1.74% | 0.046 | 0.260 | 0.150 | -8.39% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.79% | 15.03% | 3.50% | 38.83% | -3.18% | 1.903 | 0.333 | 1.005 | -37.64% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.25% | 17.83% | 5.79% | 53.56% | -3.03% | 2.195 | 0.416 | 1.799 | -47.89% |
