# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-10-09_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-10-09
- As-of date requested: 2026-10-09
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.16% |
| spy_return_21s | 2.99% |
| rsp_return_5s | 1.58% |
| rsp_return_21s | 0.31% |
| hyg_return_5s | 0.42% |
| hyg_return_21s | -1.77% |
| tlt_return_5s | 0.65% |
| tlt_return_21s | -3.47% |
| uup_return_5s | 0.45% |
| uup_return_21s | 3.53% |
| uso_return_5s | 0.56% |
| uso_return_21s | -6.43% |
| iau_return_5s | 1.18% |
| iau_return_21s | -2.95% |
| rsp_minus_spy_5s | 0.42% |
| rsp_minus_spy_21s | -2.68% |
| positive_asset_share_5s | 71.01% |
| positive_asset_share_21s | 37.68% |
| active_return_dispersion_5s | 21.54% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -1.16% | -1.81% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -1.07% | -1.85% | 0.95% | -0.26% | -0.479 | 0.047 | 0.002 | -0.15% |
| SP500 | SPY | diversified_us_equity | -0.07% | 0.00% | 0.00% | 10.04% | -1.41% | -0.870 | 1.000 | 1.000 | -0.07% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.16% | -0.12% | -0.54% | 10.40% | -1.84% | -0.199 | 0.995 | 1.012 | -0.61% |
| NASDAQ100 | QQQ | technology_and_growth | -1.10% | -0.93% | 4.07% | 15.39% | -1.59% | -0.591 | 0.901 | 1.508 | -1.10% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.99% | -0.50% | 3.02% | 14.31% | -1.61% | 0.123 | 0.927 | 1.487 | -0.99% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.72% | 0.51% | -3.01% | 8.60% | -2.64% | -0.312 | 0.714 | 0.579 | -1.89% |
| MID_CAP | IJH | diversified_us_equity | -0.77% | -1.11% | -2.14% | 11.06% | -3.05% | 0.318 | 0.760 | 0.825 | -6.37% |
| SMALL_CAP | IWM | diversified_us_equity | -0.85% | -2.08% | -3.70% | 11.06% | -3.67% | 0.715 | 0.774 | 0.927 | -8.33% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.71% | -1.85% | -4.44% | 9.79% | -4.27% | 2.076 | 0.645 | 0.644 | -6.90% |
| DIVIDEND | SCHD | diversified_us_equity | 0.58% | -0.18% | -4.78% | 10.22% | -4.51% | -0.358 | 0.182 | 0.191 | -5.41% |
| LOW_VOL | SPLV | diversified_us_equity | 0.57% | 0.60% | -5.39% | 8.62% | -4.30% | -0.631 | 0.062 | 0.055 | -7.12% |
| MOMENTUM | MTUM | diversified_us_equity | -1.37% | -2.05% | 4.91% | 17.05% | -2.39% | -0.370 | 0.597 | 1.439 | -7.12% |
| TECHNOLOGY | XLK | technology_and_growth | -1.59% | -1.68% | 6.19% | 17.95% | -2.09% | -0.322 | 0.777 | 1.777 | -1.59% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.14% | -1.11% | -2.55% | 21.60% | -4.19% | 0.133 | 0.388 | 0.734 | -7.25% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.01% | 1.39% | -3.31% | 14.06% | -3.46% | -0.057 | 0.659 | 1.139 | -8.81% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.99% | 2.44% | -4.25% | 13.31% | -4.22% | 0.125 | -0.018 | -0.025 | -5.52% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.23% | 1.63% | -1.12% | 12.23% | -2.97% | -0.062 | 0.047 | 0.073 | -2.40% |
| FINANCIALS | XLF | financials | 1.33% | 1.16% | -7.42% | 12.62% | -6.40% | 0.114 | 0.557 | 0.618 | -6.21% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.36% | -1.57% | -1.90% | 13.97% | -2.87% | -0.085 | 0.591 | 0.804 | -9.01% |
| ENERGY | XLE | energy | 2.09% | 2.44% | -4.47% | 21.85% | -6.15% | 0.391 | -0.285 | -0.539 | -0.69% |
| MATERIALS | XLB | materials_and_mining | -0.60% | 0.01% | -5.11% | 13.90% | -4.29% | 0.072 | 0.378 | 0.559 | -7.48% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.61% | 2.81% | -7.44% | 17.21% | -7.01% | 1.248 | 0.169 | 0.231 | -11.44% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.24% | 0.80% | -6.22% | 13.54% | -5.79% | 1.936 | 0.241 | 0.287 | -8.81% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.31% | -0.77% | -4.15% | 5.91% | -2.55% | 0.255 | 0.483 | 0.226 | -6.62% |
| LONG_TREASURY | TLT | rates_and_duration | 0.91% | -0.51% | -5.90% | 10.36% | -5.73% | 0.213 | 0.432 | 0.394 | -11.83% |
| TIPS | TIP | rates_and_duration | 0.23% | -0.86% | -3.90% | 4.84% | -2.21% | 0.237 | 0.264 | 0.092 | -3.55% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.26% | -0.59% | -4.23% | 6.47% | -3.17% | 0.053 | 0.545 | 0.291 | -5.80% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.05% | -0.74% | -3.99% | 4.11% | -2.31% | 0.186 | 0.689 | 0.213 | -2.83% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.24% | -0.80% | -3.68% | 4.94% | -2.28% | 1.088 | 0.498 | 0.199 | -4.50% |
| DEVELOPED_EX_US | VEA | international_equity | -1.07% | -2.26% | -2.66% | 14.78% | -3.92% | 0.416 | 0.769 | 1.041 | -4.42% |
| EMERGING_MARKETS | VWO | international_equity | -1.42% | -0.82% | -2.26% | 15.89% | -3.45% | 0.178 | 0.804 | 1.066 | -2.55% |
| EUROPE | VGK | international_equity | -0.64% | -1.57% | -4.97% | 13.40% | -4.86% | 0.449 | 0.706 | 0.790 | -7.45% |
| JAPAN | EWJ | international_equity | -1.47% | -2.23% | 0.76% | 18.28% | -3.01% | -0.319 | 0.702 | 1.259 | -1.47% |
| CHINA | MCHI | international_equity | 0.63% | 1.40% | -4.76% | 18.06% | -5.55% | 0.044 | 0.329 | 0.500 | -18.36% |
| INDIA | INDA | international_equity | -1.50% | -2.21% | -5.12% | 13.91% | -6.20% | -0.079 | 0.595 | 0.683 | -16.75% |
| GOLD | IAU | precious_metals | 0.64% | 0.02% | -5.90% | 20.83% | -6.29% | -0.829 | 0.350 | 0.771 | -22.35% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.03% | -0.03% | -4.85% | 16.89% | -5.02% | -0.213 | -0.468 | -0.884 | -2.19% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.61% | -5.48% | 10.74% | 30.91% | -4.82% | -0.365 | 0.655 | 2.242 | -9.80% |
| SOFTWARE | IGV | technology_and_growth | 1.36% | 2.75% | 5.33% | 25.42% | -2.66% | -1.057 | 0.499 | 1.486 | -3.75% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -0.67% | -0.60% | 3.18% | 19.84% | -3.01% | -0.371 | 0.823 | 1.917 | -5.05% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.90% | -1.94% | 1.50% | 22.61% | -4.15% | 0.381 | 0.830 | 2.191 | -14.12% |
| CYBERSECURITY | CIBR | technology_and_growth | 1.73% | 3.90% | 9.39% | 30.04% | -2.94% | 0.927 | 0.434 | 1.308 | 0.00% |
| SOLAR | TAN | clean_energy | -1.46% | -1.84% | -8.17% | 32.13% | -8.80% | -0.474 | 0.675 | 2.130 | -40.82% |
| METALS_MINING | XME | materials_and_mining | -1.75% | -0.58% | -9.62% | 28.00% | -9.71% | -0.856 | 0.584 | 1.946 | -19.83% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.33% | 0.42% | -3.06% | 9.08% | -2.89% | 0.784 | 0.653 | 0.595 | -4.01% |
| BIOTECH | XBI | healthcare_and_biotech | 1.90% | -1.59% | -3.33% | 28.74% | -7.77% | 1.417 | 0.344 | 0.915 | -9.31% |
| REGIONAL_BANKS | KRE | financials | -1.51% | -3.66% | -5.37% | 14.17% | -6.51% | 0.398 | 0.329 | 0.471 | -10.94% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.77% | -1.71% | -6.52% | 14.65% | -6.93% | 0.451 | 0.451 | 0.830 | -18.29% |
| CANADA | EWC | international_equity | -0.25% | -0.63% | -4.41% | 13.58% | -4.64% | 0.042 | 0.620 | 0.726 | -5.76% |
| UNITED_KINGDOM | EWU | international_equity | 0.32% | -0.42% | -4.65% | 12.30% | -4.30% | -0.119 | 0.466 | 0.475 | -5.81% |
| AUSTRALIA | EWA | international_equity | 0.25% | -0.10% | -4.42% | 17.34% | -4.37% | -0.089 | 0.648 | 0.976 | -5.95% |
| SOUTH_KOREA | EWY | international_equity | -4.91% | -8.79% | 3.17% | 45.72% | -8.48% | -0.715 | 0.551 | 2.841 | -19.14% |
| TAIWAN | EWT | international_equity | -2.81% | -2.90% | 4.99% | 28.33% | -3.95% | -0.143 | 0.728 | 2.124 | -3.13% |
| BRAZIL | EWZ | international_equity | 1.26% | 12.85% | -2.77% | 48.39% | -6.09% | 6.507 | 0.296 | 0.909 | 0.00% |
| MEXICO | EWW | international_equity | -1.02% | 0.05% | -7.34% | 19.30% | -7.44% | 0.107 | 0.591 | 0.924 | -10.13% |
| SOUTH_AFRICA | EZA | international_equity | 0.22% | -0.19% | -10.94% | 25.64% | -11.14% | -0.369 | 0.563 | 1.412 | -20.16% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.48% | -0.52% | -4.28% | 6.92% | -2.96% | 0.144 | 0.486 | 0.251 | -5.01% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.06% | -1.04% | -3.52% | 6.03% | -2.80% | 2.016 | 0.411 | 0.172 | -5.52% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.24% | -0.02% | -5.31% | 7.24% | -3.88% | 0.977 | 0.664 | 0.360 | -4.61% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.28% | -0.90% | -2.03% | 3.53% | -0.99% | 1.196 | 0.601 | 0.201 | -2.93% |
| SILVER | SLV | precious_metals | -1.21% | -1.09% | -6.61% | 34.76% | -11.99% | -0.233 | 0.447 | 1.546 | -48.13% |
| COPPER | CPER | non_energy_commodities | 0.70% | 0.84% | -0.58% | 21.75% | -4.76% | -0.410 | 0.490 | 1.036 | -2.70% |
| AGRICULTURE | DBA | non_energy_commodities | -1.80% | -0.73% | -5.60% | 13.14% | -4.06% | -0.115 | 0.115 | 0.139 | -3.93% |
| OIL | USO | energy | 2.27% | -0.60% | -8.76% | 40.06% | -11.44% | -1.003 | -0.551 | -2.482 | -8.44% |
| US_DOLLAR | UUP | currencies | 0.42% | -0.71% | 1.26% | 4.59% | -0.31% | 0.092 | -0.282 | -0.137 | -0.07% |
| EURO | FXE | currencies | -0.53% | -1.59% | -4.90% | 4.65% | -3.55% | 1.563 | 0.234 | 0.103 | -6.46% |
| YEN | FXY | currencies | -0.05% | -1.45% | -4.05% | 6.43% | -3.35% | -0.820 | 0.365 | 0.331 | -5.31% |
| BITCOIN_ETF | IBIT | crypto_assets | -4.00% | -3.63% | 7.46% | 38.76% | -5.61% | -0.348 | 0.346 | 1.193 | -32.28% |
| ETHEREUM_ETF | ETHA | crypto_assets | -8.05% | 177.26% | 6.54% | 687.29% | -8.52% | -1.031 | 0.123 | 4.476 | -8.05% |
