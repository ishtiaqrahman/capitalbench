# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-08-25
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.20% |
| spy_return_21s | 3.63% |
| rsp_return_5s | 0.90% |
| rsp_return_21s | 3.06% |
| hyg_return_5s | 0.49% |
| hyg_return_21s | 1.31% |
| tlt_return_5s | 2.22% |
| tlt_return_21s | 0.07% |
| uup_return_5s | -0.71% |
| uup_return_21s | -2.31% |
| uso_return_5s | -3.45% |
| uso_return_21s | 1.11% |
| iau_return_5s | 7.40% |
| iau_return_21s | 14.30% |
| rsp_minus_spy_5s | 1.10% |
| rsp_minus_spy_21s | -0.57% |
| positive_asset_share_5s | 68.12% |
| positive_asset_share_21s | 88.41% |
| active_return_dispersion_5s | 5.10% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.20% | -3.84% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 0.27% | -3.60% | 0.17% | 0.00% | -0.861 | -0.122 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.43% | 0.00% | 0.00% | 12.96% | -1.96% | -0.995 | 1.000 | 1.000 | -1.54% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.42% | -0.03% | -0.04% | 13.20% | -2.01% | -0.533 | 0.993 | 0.987 | -1.60% |
| NASDAQ100 | QQQ | technology_and_growth | -0.03% | -0.75% | 1.35% | 22.31% | -3.52% | -0.700 | 0.920 | 1.718 | -4.64% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.01% | -0.81% | 1.23% | 20.64% | -3.68% | -0.491 | 0.904 | 1.393 | -5.31% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.82% | 0.80% | -1.04% | 9.18% | -1.00% | -0.050 | 0.697 | 0.567 | -0.19% |
| MID_CAP | IJH | diversified_us_equity | -0.30% | -1.22% | -2.21% | 13.88% | -3.22% | 0.183 | 0.793 | 0.783 | -3.22% |
| SMALL_CAP | IWM | diversified_us_equity | 0.52% | -0.13% | -1.34% | 15.45% | -2.43% | -0.896 | 0.787 | 0.951 | -1.92% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.37% | 0.29% | -2.81% | 11.23% | -1.59% | -0.975 | 0.652 | 0.629 | -1.23% |
| DIVIDEND | SCHD | diversified_us_equity | 0.80% | 1.94% | -0.61% | 11.26% | -1.42% | 0.451 | 0.107 | 0.093 | -0.28% |
| LOW_VOL | SPLV | diversified_us_equity | 0.16% | -0.13% | -5.38% | 9.36% | -3.41% | -0.242 | -0.296 | -0.282 | -2.81% |
| MOMENTUM | MTUM | diversified_us_equity | -0.89% | -2.82% | -0.70% | 34.11% | -6.67% | -0.717 | 0.699 | 1.948 | -12.40% |
| TECHNOLOGY | XLK | technology_and_growth | -0.74% | -1.89% | 2.66% | 32.68% | -5.62% | -1.081 | 0.830 | 2.115 | -8.20% |
| COMMUNICATIONS | XLC | technology_and_growth | 2.26% | 2.64% | -1.22% | 20.57% | -2.82% | -1.160 | 0.402 | 0.579 | -5.20% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.09% | 1.57% | 1.14% | 19.14% | -2.92% | -0.869 | 0.666 | 1.064 | -4.90% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.41% | 1.30% | -3.58% | 16.87% | -3.07% | -0.405 | -0.281 | -0.363 | -2.66% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.68% | 3.48% | 0.04% | 20.15% | -3.09% | -0.251 | -0.127 | -0.182 | -0.22% |
| FINANCIALS | XLF | financials | 2.39% | 1.01% | -2.15% | 11.96% | -2.25% | -0.509 | 0.284 | 0.276 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.76% | -2.62% | -3.64% | 17.63% | -4.35% | -0.354 | 0.651 | 0.872 | -4.35% |
| ENERGY | XLE | energy | -2.65% | -2.34% | 5.28% | 24.43% | -3.76% | -0.772 | -0.310 | -0.520 | -2.65% |
| MATERIALS | XLB | materials_and_mining | 2.21% | 3.68% | -3.08% | 19.00% | -3.65% | -0.116 | 0.421 | 0.594 | 0.00% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.05% | -1.41% | -7.47% | 13.15% | -6.37% | -0.518 | -0.128 | -0.151 | -8.05% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.62% | 1.84% | -6.31% | 11.70% | -4.19% | -0.804 | -0.173 | -0.200 | -1.41% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.55% | 0.82% | -3.87% | 5.07% | -0.65% | -0.128 | 0.444 | 0.155 | -2.68% |
| LONG_TREASURY | TLT | rates_and_duration | 1.37% | 2.42% | -5.94% | 12.41% | -3.04% | 0.755 | 0.322 | 0.229 | -5.99% |
| TIPS | TIP | rates_and_duration | 0.11% | 0.78% | -3.45% | 3.23% | -0.36% | 0.401 | 0.396 | 0.102 | -0.57% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.75% | 1.16% | -4.04% | 6.23% | -0.99% | 0.107 | 0.516 | 0.202 | -2.12% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.45% | 0.69% | -3.02% | 2.77% | -0.33% | 0.059 | 0.815 | 0.181 | 0.00% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.53% | 0.88% | -3.84% | 4.43% | -0.56% | -0.957 | 0.486 | 0.141 | -1.39% |
| DEVELOPED_EX_US | VEA | international_equity | 1.30% | 2.13% | -0.42% | 16.20% | -1.76% | 0.084 | 0.809 | 1.113 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | 1.03% | 1.88% | -1.42% | 14.55% | -2.25% | -1.011 | 0.844 | 1.169 | -0.98% |
| EUROPE | VGK | international_equity | 1.28% | 1.99% | -0.79% | 10.80% | -1.13% | -0.350 | 0.736 | 0.760 | 0.00% |
| JAPAN | EWJ | international_equity | 1.44% | 0.47% | 0.38% | 23.76% | -4.27% | -0.808 | 0.751 | 1.301 | -2.88% |
| CHINA | MCHI | international_equity | -0.70% | 0.60% | -2.66% | 14.03% | -4.41% | -1.163 | 0.408 | 0.560 | -16.16% |
| INDIA | INDA | international_equity | 1.37% | 1.92% | -2.83% | 10.10% | -2.34% | -0.894 | 0.578 | 0.564 | -9.15% |
| GOLD | IAU | precious_metals | 3.09% | 7.60% | 2.58% | 24.72% | -1.68% | 0.470 | 0.480 | 0.915 | -13.60% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -2.05% | 0.04% | 1.12% | 23.12% | -3.81% | -0.325 | -0.169 | -0.272 | -3.91% |
| SEMICONDUCTORS | SMH | technology_and_growth | -1.21% | -2.25% | 0.03% | 44.67% | -8.08% | -0.661 | 0.747 | 2.896 | -16.91% |
| SOFTWARE | IGV | technology_and_growth | -0.06% | 0.09% | 8.32% | 30.32% | -4.17% | -1.285 | 0.475 | 1.227 | -13.52% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.08% | 1.08% | 3.42% | 30.91% | -3.98% | -0.608 | 0.828 | 2.355 | -10.06% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -0.76% | -3.00% | 6.55% | 37.01% | -6.62% | -1.082 | 0.858 | 2.374 | -14.66% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.06% | -4.91% | 5.52% | 29.51% | -9.53% | 0.105 | 0.552 | 1.336 | -9.53% |
| SOLAR | TAN | clean_energy | -1.77% | -1.84% | -7.11% | 40.91% | -9.46% | 0.109 | 0.765 | 2.431 | -33.92% |
| METALS_MINING | XME | materials_and_mining | 5.44% | 6.63% | 6.37% | 43.77% | -5.36% | 1.147 | 0.647 | 1.950 | -8.89% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.68% | 1.10% | -1.69% | 10.87% | -1.34% | -1.066 | 0.697 | 0.559 | -0.45% |
| BIOTECH | XBI | healthcare_and_biotech | 3.50% | 5.82% | 2.48% | 33.56% | -3.64% | 1.075 | 0.310 | 0.722 | -0.27% |
| REGIONAL_BANKS | KRE | financials | -0.51% | -3.08% | -2.08% | 14.76% | -4.62% | 0.174 | 0.153 | 0.211 | -4.62% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.37% | -6.88% | -0.45% | 24.96% | -7.83% | -0.315 | 0.431 | 0.797 | -7.47% |
| CANADA | EWC | international_equity | 1.41% | 1.92% | -0.15% | 9.98% | -1.04% | -0.394 | 0.595 | 0.510 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 1.75% | 2.75% | -2.17% | 8.68% | -1.07% | -0.661 | 0.399 | 0.370 | 0.00% |
| AUSTRALIA | EWA | international_equity | 2.29% | 2.97% | -1.31% | 17.43% | -2.83% | -0.256 | 0.588 | 0.719 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 1.12% | 6.14% | 1.65% | 71.42% | -10.54% | -0.922 | 0.675 | 3.845 | -17.81% |
| TAIWAN | EWT | international_equity | 1.28% | 1.17% | 2.89% | 38.53% | -8.59% | -1.408 | 0.786 | 2.393 | -5.50% |
| BRAZIL | EWZ | international_equity | 5.10% | 6.67% | -9.89% | 23.25% | -8.05% | 0.848 | 0.391 | 0.618 | -13.20% |
| MEXICO | EWW | international_equity | 3.11% | 4.75% | -6.55% | 16.26% | -3.95% | -0.069 | 0.576 | 0.808 | -2.76% |
| SOUTH_AFRICA | EZA | international_equity | 2.89% | 8.26% | 4.49% | 29.81% | -3.77% | -0.565 | 0.673 | 1.527 | -9.26% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.50% | 0.94% | -3.78% | 5.22% | -0.80% | 1.407 | 0.492 | 0.167 | -1.16% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.10% | 0.40% | -3.97% | 2.96% | -0.77% | 0.452 | 0.532 | 0.114 | -1.58% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.75% | 0.98% | -3.74% | 5.77% | -0.76% | -0.890 | 0.725 | 0.289 | -0.65% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.55% | 0.87% | -4.28% | 3.95% | -0.83% | 0.103 | 0.490 | 0.127 | -1.26% |
| SILVER | SLV | precious_metals | 1.07% | 8.70% | 4.68% | 36.29% | -3.58% | 0.340 | 0.552 | 1.781 | -40.98% |
| COPPER | CPER | non_energy_commodities | 3.58% | 4.23% | -2.78% | 19.11% | -4.09% | 0.095 | 0.631 | 1.170 | -0.22% |
| AGRICULTURE | DBA | non_energy_commodities | -0.35% | 1.09% | -2.35% | 11.29% | -1.47% | 0.036 | 0.149 | 0.140 | -1.57% |
| OIL | USO | energy | -6.24% | -3.25% | 0.89% | 53.98% | -11.16% | -0.824 | -0.316 | -1.226 | -17.53% |
| US_DOLLAR | UUP | currencies | 0.11% | -0.51% | -5.45% | 5.64% | -2.52% | -1.426 | -0.391 | -0.147 | -2.31% |
| EURO | FXE | currencies | 0.00% | 1.10% | -1.96% | 4.80% | -0.32% | -0.357 | 0.404 | 0.145 | -2.53% |
| YEN | FXY | currencies | -0.05% | 0.46% | -1.21% | 12.23% | -1.74% | -0.209 | 0.261 | 0.151 | -8.26% |
| BITCOIN_ETF | IBIT | crypto_assets | 8.54% | 22.39% | -4.30% | 39.61% | -3.18% | 3.584 | 0.332 | 1.007 | -37.27% |
| ETHEREUM_ETF | ETHA | crypto_assets | 5.98% | 29.01% | -5.67% | 54.31% | -4.35% | 4.613 | 0.416 | 1.800 | -48.03% |
