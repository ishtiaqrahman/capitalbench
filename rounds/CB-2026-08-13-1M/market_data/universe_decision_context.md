# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-12
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.35% |
| spy_return_21s | 2.75% |
| rsp_return_5s | 0.61% |
| rsp_return_21s | 3.57% |
| hyg_return_5s | 0.11% |
| hyg_return_21s | 0.40% |
| tlt_return_5s | -1.07% |
| tlt_return_21s | -1.95% |
| uup_return_5s | 0.39% |
| uup_return_21s | -0.67% |
| uso_return_5s | 10.81% |
| uso_return_21s | 5.93% |
| iau_return_5s | 3.92% |
| iau_return_21s | 8.80% |
| rsp_minus_spy_5s | 0.26% |
| rsp_minus_spy_21s | 0.83% |
| positive_asset_share_5s | 59.42% |
| positive_asset_share_21s | 72.46% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.75% | -9.20% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.09% | -2.45% | -7.69% | 0.21% | -0.01% | -0.253 | -0.107 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.35% | 0.00% | 0.00% | 13.96% | -4.49% | -0.774 | 1.000 | 1.000 | -0.10% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.57% | 0.13% | 0.04% | 13.89% | -4.36% | -0.778 | 0.995 | 1.013 | 0.00% |
| NASDAQ100 | QQQ | technology_and_growth | 0.89% | -2.19% | 8.77% | 25.86% | -11.22% | -0.672 | 0.931 | 1.416 | -2.90% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.43% | -1.78% | -1.75% | 21.10% | -11.35% | -0.751 | 0.937 | 1.282 | -3.29% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.64% | 1.68% | 1.48% | 11.47% | -2.40% | -0.624 | 0.806 | 0.710 | -0.21% |
| MID_CAP | IJH | diversified_us_equity | 1.38% | 0.55% | -3.39% | 14.31% | -3.09% | -0.877 | 0.805 | 0.989 | 0.00% |
| SMALL_CAP | IWM | diversified_us_equity | 0.98% | 0.04% | 1.91% | 18.10% | -4.03% | -1.017 | 0.816 | 1.229 | 0.00% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.38% | 0.18% | 4.18% | 14.47% | -3.50% | -0.408 | 0.726 | 0.972 | -0.46% |
| DIVIDEND | SCHD | diversified_us_equity | 1.84% | 3.65% | -4.63% | 11.73% | -2.95% | 0.207 | 0.291 | 0.251 | -0.03% |
| LOW_VOL | SPLV | diversified_us_equity | -0.67% | -2.68% | -7.23% | 13.16% | -3.75% | -0.710 | 0.016 | 0.013 | -2.76% |
| MOMENTUM | MTUM | diversified_us_equity | 1.53% | -4.32% | 16.41% | 38.65% | -17.99% | 0.890 | 0.777 | 1.563 | -8.83% |
| TECHNOLOGY | XLK | technology_and_growth | 1.59% | 0.11% | 19.92% | 35.29% | -15.86% | -0.951 | 0.858 | 1.732 | -4.60% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.54% | -3.98% | -12.20% | 20.11% | -9.78% | -0.392 | 0.579 | 0.689 | -7.64% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.63% | -1.03% | -10.87% | 22.06% | -10.72% | -0.593 | 0.777 | 1.174 | -4.95% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.29% | -0.76% | -12.28% | 16.87% | -4.95% | -0.749 | -0.071 | -0.078 | -4.29% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.61% | 3.66% | -6.43% | 18.16% | -3.74% | -0.672 | 0.226 | 0.274 | 0.00% |
| FINANCIALS | XLF | financials | -0.14% | 0.35% | -3.38% | 13.47% | -2.08% | -0.898 | 0.547 | 0.620 | -0.14% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.25% | -0.11% | -1.07% | 19.33% | -4.80% | -1.025 | 0.716 | 0.958 | -0.28% |
| ENERGY | XLE | energy | 6.49% | 4.42% | -1.45% | 24.34% | -13.21% | -0.910 | -0.154 | -0.259 | -1.74% |
| MATERIALS | XLB | materials_and_mining | -0.11% | 1.08% | -12.71% | 20.32% | -5.95% | -0.508 | 0.538 | 0.746 | -1.24% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.41% | -6.80% | -4.45% | 16.35% | -6.83% | -0.492 | 0.125 | 0.145 | -6.92% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.57% | -2.73% | -3.76% | 16.15% | -4.19% | -0.642 | 0.239 | 0.263 | -3.30% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.38% | -2.76% | -10.54% | 5.05% | -2.00% | -0.271 | 0.292 | 0.105 | -3.26% |
| LONG_TREASURY | TLT | rates_and_duration | -1.07% | -4.70% | -12.45% | 9.23% | -5.60% | -0.002 | 0.236 | 0.171 | -7.52% |
| TIPS | TIP | rates_and_duration | -0.07% | -3.86% | -8.80% | 3.92% | -2.01% | -0.606 | 0.252 | 0.068 | -1.96% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.58% | -3.34% | -10.63% | 5.28% | -2.83% | -0.397 | 0.483 | 0.198 | -2.80% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.11% | -2.35% | -8.18% | 3.41% | -0.80% | -0.641 | 0.780 | 0.234 | 0.00% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.29% | -2.98% | -10.01% | 4.09% | -1.71% | -0.271 | 0.400 | 0.116 | -1.97% |
| DEVELOPED_EX_US | VEA | international_equity | 1.31% | 1.08% | -5.48% | 19.62% | -4.85% | -0.903 | 0.804 | 1.081 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | 0.67% | -0.50% | -7.24% | 20.01% | -7.05% | -0.695 | 0.813 | 1.116 | -1.36% |
| EUROPE | VGK | international_equity | 0.44% | 1.73% | -8.42% | 15.61% | -3.12% | -0.814 | 0.748 | 0.921 | -0.38% |
| JAPAN | EWJ | international_equity | 2.76% | 1.41% | -7.81% | 23.33% | -7.86% | -0.933 | 0.718 | 1.174 | 0.00% |
| CHINA | MCHI | international_equity | -1.66% | 0.73% | -22.77% | 20.81% | -15.01% | -0.520 | 0.547 | 0.879 | -16.22% |
| INDIA | INDA | international_equity | -0.72% | -1.43% | -16.67% | 15.30% | -5.28% | -0.555 | 0.541 | 0.638 | -9.66% |
| GOLD | IAU | precious_metals | 3.92% | 6.05% | -28.67% | 24.96% | -15.68% | -0.476 | 0.315 | 0.691 | -18.30% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 5.83% | 3.58% | 8.16% | 22.67% | -16.55% | 0.185 | -0.177 | -0.277 | -4.97% |
| SEMICONDUCTORS | SMH | technology_and_growth | 2.66% | -5.33% | 39.11% | 54.17% | -24.62% | 0.581 | 0.786 | 2.380 | -12.57% |
| SOFTWARE | IGV | technology_and_growth | 1.75% | 7.34% | 0.44% | 34.81% | -21.29% | -0.927 | 0.508 | 1.176 | -12.47% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.26% | 0.17% | 12.84% | 39.76% | -20.19% | -0.330 | 0.849 | 1.911 | -9.08% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 5.33% | 2.69% | -11.00% | 38.75% | -23.82% | -0.640 | 0.802 | 2.193 | -10.35% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.89% | 3.23% | 28.78% | 32.39% | -11.74% | -0.481 | 0.539 | 1.103 | -0.21% |
| SOLAR | TAN | clean_energy | 2.07% | -7.52% | -10.78% | 47.12% | -35.51% | -0.362 | 0.599 | 1.853 | -29.22% |
| METALS_MINING | XME | materials_and_mining | 4.35% | 9.10% | -24.27% | 41.89% | -26.49% | -0.295 | 0.604 | 1.761 | -12.02% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.61% | 0.83% | -3.25% | 11.06% | -2.04% | -0.815 | 0.769 | 0.703 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | 4.17% | -0.21% | 14.94% | 30.20% | -10.51% | -0.443 | 0.486 | 1.026 | -2.98% |
| REGIONAL_BANKS | KRE | financials | 0.05% | 0.43% | -4.75% | 19.33% | -3.73% | -0.719 | 0.435 | 0.773 | -0.69% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.26% | 2.26% | -3.12% | 25.78% | -8.58% | -0.381 | 0.568 | 1.012 | -0.26% |
| CANADA | EWC | international_equity | 1.63% | 1.63% | -4.38% | 12.09% | -3.20% | -0.481 | 0.672 | 0.743 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 0.00% | 1.70% | -8.71% | 14.75% | -3.40% | -0.547 | 0.608 | 0.708 | -0.64% |
| AUSTRALIA | EWA | international_equity | -0.83% | 3.24% | -6.49% | 16.80% | -5.17% | -0.854 | 0.668 | 0.917 | -1.71% |
| SOUTH_KOREA | EWY | international_equity | 3.98% | -3.38% | 33.01% | 80.47% | -34.21% | 0.234 | 0.643 | 2.751 | -19.77% |
| TAIWAN | EWT | international_equity | 4.41% | 1.47% | 33.40% | 44.23% | -19.83% | -0.275 | 0.760 | 1.843 | -4.80% |
| BRAZIL | EWZ | international_equity | -6.23% | -8.77% | -14.29% | 23.54% | -11.90% | -0.909 | 0.507 | 0.997 | -18.09% |
| MEXICO | EWW | international_equity | -0.30% | -1.26% | -14.21% | 19.44% | -7.30% | -0.565 | 0.549 | 0.939 | -4.49% |
| SOUTH_AFRICA | EZA | international_equity | 2.21% | 4.94% | -23.22% | 31.45% | -12.74% | -0.540 | 0.632 | 1.609 | -14.43% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.16% | -2.89% | -9.74% | 4.87% | -1.85% | -0.349 | 0.396 | 0.136 | -1.78% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.15% | -3.34% | -8.70% | 3.36% | -2.15% | 0.852 | 0.381 | 0.089 | -1.21% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.24% | -3.81% | -7.52% | 5.71% | -1.98% | -0.708 | 0.680 | 0.303 | -1.53% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.35% | -3.16% | -9.14% | 4.06% | -1.44% | -0.724 | 0.450 | 0.124 | -1.69% |
| SILVER | SLV | precious_metals | 5.33% | 8.33% | -36.78% | 47.41% | -36.50% | -0.540 | 0.358 | 1.715 | -44.07% |
| COPPER | CPER | non_energy_commodities | -2.03% | 3.27% | -2.08% | 27.55% | -10.57% | -0.529 | 0.544 | 1.179 | -2.03% |
| AGRICULTURE | DBA | non_energy_commodities | 0.76% | -1.99% | -1.82% | 13.84% | -8.67% | -0.610 | 0.090 | 0.077 | -3.10% |
| OIL | USO | energy | 10.81% | 3.19% | 44.80% | 53.77% | -32.49% | -0.560 | -0.333 | -1.243 | -16.78% |
| US_DOLLAR | UUP | currencies | 0.39% | -3.42% | -3.27% | 4.99% | -1.85% | -0.326 | -0.315 | -0.141 | -1.40% |
| EURO | FXE | currencies | -0.24% | -1.88% | -11.89% | 4.89% | -3.57% | -0.875 | 0.299 | 0.134 | -3.93% |
| YEN | FXY | currencies | -1.08% | -1.07% | -14.24% | 7.62% | -3.90% | 1.365 | 0.183 | 0.116 | -8.44% |
| BITCOIN_ETF | IBIT | crypto_assets | -2.31% | -4.63% | -15.34% | 36.31% | -27.90% | -0.618 | 0.508 | 1.751 | -49.66% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.21% | -2.89% | -15.91% | 52.74% | -32.37% | -0.409 | 0.537 | 2.772 | -61.30% |
