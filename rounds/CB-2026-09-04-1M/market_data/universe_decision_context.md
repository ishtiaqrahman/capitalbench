# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-09-04
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.11% |
| spy_return_21s | 0.21% |
| rsp_return_5s | -0.77% |
| rsp_return_21s | 0.19% |
| hyg_return_5s | -0.18% |
| hyg_return_21s | 0.17% |
| tlt_return_5s | -0.43% |
| tlt_return_21s | 0.01% |
| uup_return_5s | -0.35% |
| uup_return_21s | -0.39% |
| uso_return_5s | 9.45% |
| uso_return_21s | 19.42% |
| iau_return_5s | -0.51% |
| iau_return_21s | 4.41% |
| rsp_minus_spy_5s | -0.87% |
| rsp_minus_spy_21s | -0.02% |
| positive_asset_share_5s | 53.62% |
| positive_asset_share_21s | 59.42% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.21% | -14.91% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.09% | 0.09% | -13.42% | 0.20% | -0.01% | -0.589 | -0.105 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.11% | 0.00% | 0.00% | 12.83% | -3.38% | -1.125 | 1.000 | 1.000 | -0.99% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.10% | -0.04% | 0.16% | 12.66% | -3.29% | -0.641 | 0.995 | 1.012 | -1.19% |
| NASDAQ100 | QQQ | technology_and_growth | 0.35% | 0.39% | 4.53% | 23.94% | -10.96% | -1.119 | 0.929 | 1.422 | -3.54% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.54% | -0.28% | -4.22% | 20.37% | -8.29% | -0.766 | 0.934 | 1.289 | -4.08% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.27% | 0.38% | 3.55% | 10.59% | -1.39% | -0.619 | 0.799 | 0.699 | -0.67% |
| MID_CAP | IJH | diversified_us_equity | 0.12% | -1.38% | -1.86% | 13.35% | -5.17% | -0.744 | 0.806 | 0.972 | -3.58% |
| SMALL_CAP | IWM | diversified_us_equity | 0.09% | -0.96% | 4.46% | 14.78% | -4.76% | -1.148 | 0.817 | 1.199 | -2.98% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.66% | 0.14% | 3.39% | 11.77% | -3.29% | -0.932 | 0.733 | 0.937 | -1.24% |
| DIVIDEND | SCHD | diversified_us_equity | -0.29% | 3.05% | -4.87% | 11.59% | -2.93% | 0.043 | 0.282 | 0.243 | -1.16% |
| LOW_VOL | SPLV | diversified_us_equity | -0.45% | -2.02% | -13.72% | 12.38% | -4.22% | -0.720 | 0.017 | 0.014 | -3.96% |
| MOMENTUM | MTUM | diversified_us_equity | 1.72% | -1.29% | 12.96% | 35.99% | -17.99% | -0.373 | 0.764 | 1.568 | -11.69% |
| TECHNOLOGY | XLK | technology_and_growth | 0.86% | 0.84% | 20.41% | 32.09% | -13.31% | -1.395 | 0.851 | 1.747 | -5.40% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.85% | 0.55% | -19.71% | 19.80% | -7.06% | -1.078 | 0.566 | 0.674 | -6.16% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.96% | -2.91% | -11.30% | 21.46% | -8.09% | -1.285 | 0.765 | 1.161 | -7.35% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.02% | -0.83% | -14.44% | 17.04% | -3.58% | -0.949 | -0.066 | -0.074 | -4.85% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.17% | 4.04% | -6.30% | 18.76% | -3.74% | -1.080 | 0.222 | 0.278 | -2.41% |
| FINANCIALS | XLF | financials | 0.00% | 0.29% | 0.40% | 12.80% | -2.25% | -0.898 | 0.537 | 0.615 | -0.79% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.06% | -5.35% | -5.62% | 18.65% | -7.39% | -0.854 | 0.710 | 0.950 | -6.03% |
| ENERGY | XLE | energy | 2.20% | 9.93% | -10.68% | 22.34% | -8.81% | -0.866 | -0.179 | -0.303 | -1.60% |
| MATERIALS | XLB | materials_and_mining | -1.39% | 0.31% | -9.42% | 19.38% | -4.75% | -0.491 | 0.527 | 0.738 | -2.29% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.82% | -0.90% | -20.85% | 14.67% | -8.77% | -0.350 | 0.117 | 0.139 | -8.53% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.24% | -2.18% | -8.81% | 15.31% | -4.96% | -0.452 | 0.240 | 0.263 | -4.52% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.29% | -0.61% | -16.92% | 4.75% | -2.11% | -0.358 | 0.279 | 0.100 | -3.65% |
| LONG_TREASURY | TLT | rates_and_duration | -0.43% | -0.21% | -19.81% | 9.66% | -6.26% | -0.138 | 0.226 | 0.165 | -7.05% |
| TIPS | TIP | rates_and_duration | 0.03% | -0.12% | -15.72% | 3.47% | -1.33% | -0.467 | 0.252 | 0.065 | -1.19% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.40% | -0.62% | -16.45% | 5.28% | -2.92% | -0.583 | 0.468 | 0.192 | -2.98% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.18% | -0.04% | -12.71% | 2.89% | -0.80% | -0.677 | 0.775 | 0.228 | -0.41% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.16% | -0.31% | -15.94% | 3.93% | -1.71% | -0.398 | 0.386 | 0.113 | -2.06% |
| DEVELOPED_EX_US | VEA | international_equity | 0.96% | 2.06% | -3.66% | 17.42% | -4.75% | -0.752 | 0.799 | 1.082 | -0.04% |
| EMERGING_MARKETS | VWO | international_equity | 1.07% | 2.26% | -4.70% | 16.87% | -7.05% | -0.843 | 0.810 | 1.111 | 0.00% |
| EUROPE | VGK | international_equity | -0.26% | -0.31% | -3.91% | 13.39% | -2.65% | -0.917 | 0.744 | 0.911 | -1.56% |
| JAPAN | EWJ | international_equity | 2.51% | 3.08% | -2.06% | 22.82% | -7.86% | -0.881 | 0.720 | 1.183 | -0.19% |
| CHINA | MCHI | international_equity | -0.58% | -2.00% | -15.69% | 16.47% | -8.10% | -0.733 | 0.554 | 0.862 | -16.48% |
| INDIA | INDA | international_equity | 0.71% | -0.63% | -14.65% | 12.44% | -4.59% | -1.087 | 0.555 | 0.654 | -9.73% |
| GOLD | IAU | precious_metals | -0.51% | 4.20% | -32.55% | 26.61% | -8.22% | -0.446 | 0.327 | 0.740 | -17.90% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.37% | 10.12% | -9.72% | 21.61% | -10.44% | -0.488 | -0.172 | -0.272 | -0.42% |
| SEMICONDUCTORS | SMH | technology_and_growth | 2.51% | -0.99% | 35.26% | 50.12% | -24.62% | -0.810 | 0.773 | 2.376 | -15.23% |
| SOFTWARE | IGV | technology_and_growth | -4.50% | 4.97% | -1.87% | 33.49% | -11.55% | -1.037 | 0.506 | 1.242 | -11.21% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.16% | 3.61% | 11.26% | 34.76% | -16.56% | -0.859 | 0.847 | 1.926 | -8.30% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -0.06% | -0.98% | -11.12% | 34.73% | -18.66% | -1.315 | 0.806 | 2.208 | -15.00% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.03% | -2.08% | 31.51% | 31.86% | -9.53% | 0.099 | 0.524 | 1.159 | -7.45% |
| SOLAR | TAN | clean_energy | -1.25% | -6.48% | -18.72% | 38.47% | -26.84% | -0.772 | 0.628 | 1.882 | -35.02% |
| METALS_MINING | XME | materials_and_mining | -0.10% | 7.28% | -14.59% | 37.62% | -19.05% | -0.495 | 0.596 | 1.780 | -10.64% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.77% | -0.02% | -3.70% | 10.83% | -2.33% | -1.107 | 0.771 | 0.698 | -1.69% |
| BIOTECH | XBI | healthcare_and_biotech | 0.88% | 5.81% | 9.81% | 29.52% | -10.51% | -0.421 | 0.476 | 1.039 | -3.39% |
| REGIONAL_BANKS | KRE | financials | 1.31% | -1.81% | 4.31% | 17.19% | -6.81% | -0.734 | 0.414 | 0.716 | -3.41% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.10% | -9.96% | -11.56% | 24.17% | -11.79% | -0.452 | 0.569 | 1.032 | -10.90% |
| CANADA | EWC | international_equity | 0.50% | 2.00% | -6.69% | 11.16% | -3.26% | -0.283 | 0.675 | 0.759 | -0.96% |
| UNITED_KINGDOM | EWU | international_equity | 0.08% | 0.39% | -8.45% | 12.42% | -2.43% | -0.597 | 0.599 | 0.697 | -1.62% |
| AUSTRALIA | EWA | international_equity | 0.77% | 0.02% | -6.96% | 15.35% | -4.42% | -0.461 | 0.672 | 0.930 | -0.66% |
| SOUTH_KOREA | EWY | international_equity | 4.81% | 14.87% | 14.59% | 71.69% | -34.21% | -0.771 | 0.632 | 2.764 | -13.84% |
| TAIWAN | EWT | international_equity | 3.97% | 9.79% | 31.78% | 38.66% | -19.83% | -1.067 | 0.749 | 1.827 | 0.00% |
| BRAZIL | EWZ | international_equity | 6.50% | 5.51% | -15.27% | 21.92% | -8.05% | -0.209 | 0.487 | 0.957 | -8.41% |
| MEXICO | EWW | international_equity | 0.20% | -0.21% | -9.43% | 17.98% | -5.37% | -0.558 | 0.548 | 0.941 | -4.27% |
| SOUTH_AFRICA | EZA | international_equity | 1.30% | 6.91% | -18.00% | 28.91% | -11.18% | -0.601 | 0.628 | 1.624 | -10.28% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.12% | -0.16% | -15.81% | 4.60% | -1.85% | 0.147 | 0.382 | 0.131 | -1.92% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.86% | -1.48% | -15.35% | 2.98% | -2.79% | 0.903 | 0.367 | 0.087 | -2.76% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.01% | -0.28% | -13.55% | 5.18% | -1.96% | -0.638 | 0.679 | 0.301 | -1.16% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.06% | -0.88% | -14.87% | 3.60% | -1.90% | -0.389 | 0.460 | 0.129 | -1.96% |
| SILVER | SLV | precious_metals | -0.33% | 6.90% | -41.37% | 42.44% | -20.61% | -0.663 | 0.366 | 1.777 | -43.35% |
| COPPER | CPER | non_energy_commodities | 0.71% | -2.20% | -0.51% | 22.89% | -8.42% | -0.594 | 0.564 | 1.249 | -2.20% |
| AGRICULTURE | DBA | non_energy_commodities | -1.16% | 4.96% | -12.22% | 12.90% | -2.87% | 0.109 | 0.066 | 0.057 | -2.17% |
| OIL | USO | energy | 9.45% | 19.21% | -5.63% | 52.03% | -23.59% | -0.632 | -0.337 | -1.277 | -7.19% |
| US_DOLLAR | UUP | currencies | -0.35% | -0.60% | -12.29% | 5.23% | -2.52% | -1.013 | -0.295 | -0.130 | -1.82% |
| EURO | FXE | currencies | 0.24% | 0.67% | -15.31% | 4.75% | -2.19% | -0.694 | 0.272 | 0.118 | -3.04% |
| YEN | FXY | currencies | 2.48% | 1.14% | -15.43% | 9.10% | -2.49% | 0.298 | 0.183 | 0.120 | -6.61% |
| BITCOIN_ETF | IBIT | crypto_assets | 3.03% | 23.74% | -20.38% | 39.14% | -11.79% | 0.689 | 0.486 | 1.719 | -36.55% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.82% | 28.40% | -18.46% | 53.28% | -14.68% | 1.013 | 0.505 | 2.553 | -48.25% |
