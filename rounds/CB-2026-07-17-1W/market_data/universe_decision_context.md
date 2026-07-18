# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-17
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.54% |
| spy_return_21s | -0.68% |
| rsp_return_5s | -0.43% |
| rsp_return_21s | 0.96% |
| hyg_return_5s | -0.08% |
| hyg_return_21s | -0.01% |
| tlt_return_5s | 0.06% |
| tlt_return_21s | -1.58% |
| uup_return_5s | -0.21% |
| uup_return_21s | 1.43% |
| uso_return_5s | 14.04% |
| uso_return_21s | 7.35% |
| iau_return_5s | -2.28% |
| iau_return_21s | -7.36% |
| rsp_minus_spy_5s | 1.11% |
| rsp_minus_spy_21s | 1.64% |
| positive_asset_share_5s | 43.48% |
| positive_asset_share_21s | 37.68% |
| active_return_dispersion_5s | 3.49% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.54% | -0.87% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 1.60% | -0.60% | 0.25% | -0.01% | -0.151 | -0.178 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.14% | 0.00% | 0.00% | 12.73% | -2.59% | -0.512 | 1.000 | 1.000 | -1.89% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.12% | 0.02% | 0.04% | 12.00% | -1.92% | -0.430 | 0.992 | 0.991 | -1.68% |
| NASDAQ100 | QQQ | technology_and_growth | -3.38% | -2.62% | -1.36% | 25.77% | -6.01% | -0.425 | 0.917 | 1.695 | -6.71% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.12% | -2.14% | -0.39% | 22.32% | -4.26% | 0.116 | 0.890 | 1.279 | -7.21% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.67% | 2.03% | 0.72% | 11.32% | -1.06% | -0.482 | 0.720 | 0.651 | -0.57% |
| MID_CAP | IJH | diversified_us_equity | -0.04% | 1.37% | -1.22% | 12.49% | -3.09% | -0.587 | 0.772 | 0.876 | -2.04% |
| SMALL_CAP | IWM | diversified_us_equity | -0.16% | 0.89% | 0.46% | 12.68% | -2.32% | -0.765 | 0.788 | 1.117 | -2.13% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.25% | 2.62% | 0.87% | 11.33% | -1.83% | -0.891 | 0.679 | 0.816 | -0.82% |
| DIVIDEND | SCHD | diversified_us_equity | 2.20% | 3.12% | -0.48% | 14.28% | -2.06% | 0.311 | 0.110 | 0.100 | -0.39% |
| LOW_VOL | SPLV | diversified_us_equity | 0.87% | 2.51% | 1.12% | 15.92% | -1.89% | -0.153 | -0.265 | -0.271 | -0.48% |
| MOMENTUM | MTUM | diversified_us_equity | -5.53% | -4.57% | -2.19% | 42.17% | -12.49% | 1.532 | 0.765 | 2.080 | -12.49% |
| TECHNOLOGY | XLK | technology_and_growth | -4.37% | -3.94% | -1.11% | 33.08% | -8.62% | -0.897 | 0.840 | 2.116 | -11.31% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.72% | 0.66% | -1.22% | 20.79% | -5.76% | 0.044 | 0.463 | 0.541 | -7.32% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.40% | 0.01% | -1.71% | 20.70% | -4.12% | -0.194 | 0.750 | 1.086 | -6.92% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 2.12% | 2.82% | -1.91% | 20.65% | -3.32% | -0.662 | -0.273 | -0.343 | -4.16% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.77% | 1.70% | 4.75% | 22.41% | -3.74% | -0.129 | -0.071 | -0.099 | -2.04% |
| FINANCIALS | XLF | financials | 0.14% | 2.53% | 1.99% | 14.21% | -2.08% | 0.524 | 0.189 | 0.189 | -0.86% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.58% | 0.16% | 0.52% | 17.23% | -3.31% | -0.732 | 0.656 | 0.980 | -3.31% |
| ENERGY | XLE | energy | 1.28% | 6.26% | -0.66% | 21.41% | -3.92% | -0.342 | -0.409 | -0.772 | -7.14% |
| MATERIALS | XLB | materials_and_mining | -0.22% | 0.84% | -3.99% | 17.34% | -4.50% | -0.673 | 0.540 | 0.784 | -4.99% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.14% | 1.02% | 0.55% | 15.59% | -3.10% | -0.734 | -0.052 | -0.070 | -4.09% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 2.11% | 3.73% | -1.45% | 18.81% | -2.75% | -0.630 | -0.059 | -0.074 | -0.09% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.31% | 1.77% | -1.49% | 5.07% | -1.54% | -0.298 | 0.562 | 0.217 | -2.68% |
| LONG_TREASURY | TLT | rates_and_duration | 0.52% | 1.60% | -2.51% | 8.84% | -3.62% | -0.548 | 0.432 | 0.292 | -5.19% |
| TIPS | TIP | rates_and_duration | 0.24% | 1.67% | -1.40% | 4.29% | -0.85% | -0.483 | 0.567 | 0.153 | -0.72% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.33% | 1.64% | -2.05% | 4.87% | -2.16% | 0.352 | 0.595 | 0.242 | -1.90% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.04% | 1.47% | -0.81% | 2.77% | -0.44% | -0.491 | 0.786 | 0.221 | -0.28% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.20% | 1.67% | -1.44% | 3.98% | -1.34% | -0.098 | 0.598 | 0.189 | -1.54% |
| DEVELOPED_EX_US | VEA | international_equity | -1.27% | -0.27% | -2.20% | 18.24% | -3.72% | -0.382 | 0.841 | 1.347 | -3.72% |
| EMERGING_MARKETS | VWO | international_equity | -2.10% | -1.88% | -1.21% | 20.06% | -5.55% | 0.215 | 0.875 | 1.382 | -5.55% |
| EUROPE | VGK | international_equity | 0.33% | 1.57% | -1.13% | 13.30% | -2.35% | -1.575 | 0.728 | 1.018 | -1.53% |
| JAPAN | EWJ | international_equity | -3.62% | -2.75% | -0.42% | 24.60% | -6.68% | -0.451 | 0.791 | 1.334 | -6.68% |
| CHINA | MCHI | international_equity | -0.53% | 1.21% | -2.72% | 20.80% | -6.74% | -0.404 | 0.549 | 0.875 | -19.46% |
| INDIA | INDA | international_equity | 0.37% | 0.75% | -1.10% | 13.10% | -2.54% | -0.674 | 0.599 | 0.745 | -11.54% |
| GOLD | IAU | precious_metals | -1.01% | -0.73% | -6.08% | 22.95% | -8.22% | -0.482 | 0.701 | 1.286 | -25.67% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.00% | 6.47% | -2.25% | 21.87% | -5.34% | 3.747 | -0.172 | -0.286 | -8.78% |
| SEMICONDUCTORS | SMH | technology_and_growth | -7.29% | -7.37% | -1.68% | 56.68% | -16.80% | 0.433 | 0.786 | 3.133 | -16.80% |
| SOFTWARE | IGV | technology_and_growth | -0.89% | 1.97% | 0.26% | 26.63% | -7.23% | -1.368 | 0.346 | 0.909 | -21.20% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -5.26% | -5.93% | -2.73% | 38.59% | -12.51% | -0.152 | 0.827 | 2.459 | -16.31% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -5.02% | -4.79% | -7.19% | 32.43% | -12.79% | -0.969 | 0.850 | 2.461 | -19.25% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.50% | 2.07% | 7.21% | 27.07% | -3.00% | -0.610 | 0.424 | 1.048 | -2.50% |
| SOLAR | TAN | clean_energy | -2.23% | -0.38% | -10.15% | 40.36% | -13.07% | -1.347 | 0.735 | 2.541 | -27.09% |
| METALS_MINING | XME | materials_and_mining | -5.81% | -3.61% | -13.92% | 28.31% | -17.53% | -0.618 | 0.701 | 2.151 | -25.91% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.04% | 1.11% | 0.52% | 11.20% | -1.50% | -0.417 | 0.723 | 0.606 | -0.79% |
| BIOTECH | XBI | healthcare_and_biotech | -0.77% | -1.45% | 16.74% | 29.25% | -7.48% | 0.160 | 0.372 | 0.857 | -6.10% |
| REGIONAL_BANKS | KRE | financials | 2.25% | 3.77% | 3.22% | 21.12% | -3.73% | -0.067 | 0.184 | 0.294 | -1.58% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.93% | -1.94% | -1.07% | 20.19% | -8.00% | -0.930 | 0.493 | 0.970 | -8.00% |
| CANADA | EWC | international_equity | 0.46% | 2.91% | -1.65% | 9.19% | -3.08% | -0.417 | 0.612 | 0.613 | -0.07% |
| UNITED_KINGDOM | EWU | international_equity | 1.36% | 2.27% | -0.68% | 13.95% | -2.28% | -0.514 | 0.500 | 0.651 | -2.19% |
| AUSTRALIA | EWA | international_equity | 0.14% | 2.60% | -2.70% | 12.98% | -4.42% | -0.451 | 0.613 | 0.863 | -3.65% |
| SOUTH_KOREA | EWY | international_equity | -8.16% | -9.89% | -11.75% | 77.47% | -25.85% | 1.519 | 0.755 | 4.467 | -25.85% |
| TAIWAN | EWT | international_equity | -4.47% | -6.80% | 1.44% | 43.46% | -12.73% | 0.705 | 0.795 | 2.511 | -12.73% |
| BRAZIL | EWZ | international_equity | -2.22% | -0.40% | 3.54% | 19.83% | -2.22% | -0.459 | 0.428 | 0.747 | -14.77% |
| MEXICO | EWW | international_equity | -0.31% | 1.88% | -4.88% | 17.77% | -5.37% | -0.542 | 0.626 | 0.978 | -6.17% |
| SOUTH_AFRICA | EZA | international_equity | -1.72% | -0.74% | -7.08% | 22.45% | -8.61% | -0.513 | 0.778 | 1.994 | -21.90% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.12% | 1.61% | -1.56% | 4.62% | -1.45% | -0.221 | 0.600 | 0.221 | -1.52% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.35% | 1.14% | -0.76% | 2.48% | -0.92% | -0.281 | 0.615 | 0.128 | -0.92% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.04% | 1.07% | -1.16% | 4.53% | -1.08% | -0.556 | 0.752 | 0.341 | -0.92% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.06% | 1.23% | -1.16% | 3.39% | -1.20% | -0.546 | 0.574 | 0.190 | -1.47% |
| SILVER | SLV | precious_metals | -4.50% | -4.33% | -15.77% | 44.20% | -20.51% | -0.639 | 0.669 | 2.601 | -51.91% |
| COPPER | CPER | non_energy_commodities | -1.61% | 1.36% | -4.82% | 24.61% | -8.19% | -0.841 | 0.719 | 1.584 | -6.60% |
| AGRICULTURE | DBA | non_energy_commodities | 0.76% | 1.80% | 3.29% | 15.12% | -1.52% | -0.667 | -0.021 | -0.021 | -3.10% |
| OIL | USO | energy | 3.15% | 15.58% | -6.74% | 48.38% | -10.57% | -0.190 | -0.353 | -1.457 | -18.96% |
| US_DOLLAR | UUP | currencies | -0.21% | 1.33% | 0.77% | 5.48% | -0.98% | 0.422 | -0.544 | -0.205 | -0.70% |
| EURO | FXE | currencies | 0.21% | 1.84% | -2.51% | 5.47% | -2.19% | -0.584 | 0.556 | 0.200 | -4.58% |
| YEN | FXY | currencies | -0.11% | 1.14% | -1.66% | 5.29% | -1.33% | -0.126 | 0.239 | 0.119 | -10.09% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.63% | 1.88% | -3.40% | 37.36% | -10.44% | -0.288 | 0.498 | 1.464 | -49.01% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.90% | 4.35% | -0.95% | 51.56% | -13.29% | 0.415 | 0.597 | 2.441 | -61.98% |
