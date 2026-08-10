# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-07
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 3.51% |
| spy_return_21s | 2.87% |
| rsp_return_5s | 2.36% |
| rsp_return_21s | 3.09% |
| hyg_return_5s | 0.65% |
| hyg_return_21s | 0.31% |
| tlt_return_5s | 1.03% |
| tlt_return_21s | -1.65% |
| uup_return_5s | -0.35% |
| uup_return_21s | -1.02% |
| uso_return_5s | -8.66% |
| uso_return_21s | 8.23% |
| iau_return_5s | 7.23% |
| iau_return_21s | 5.38% |
| rsp_minus_spy_5s | -1.15% |
| rsp_minus_spy_21s | 0.22% |
| positive_asset_share_5s | 88.41% |
| positive_asset_share_21s | 72.46% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.87% | -11.52% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | -2.55% | -10.02% | 0.21% | -0.01% | -0.249 | -0.102 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 3.51% | 0.00% | 0.00% | 14.02% | -4.49% | -0.797 | 1.000 | 1.000 | 0.00% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 3.69% | -0.09% | 0.39% | 13.95% | -4.36% | -0.846 | 0.995 | 1.013 | 0.00% |
| NASDAQ100 | QQQ | technology_and_growth | 5.09% | -2.90% | 9.91% | 26.28% | -11.22% | -0.689 | 0.931 | 1.415 | -2.99% |
| LARGE_GROWTH | IWF | technology_and_growth | 5.31% | -1.81% | -0.77% | 21.06% | -11.35% | -0.758 | 0.937 | 1.281 | -3.15% |
| LARGE_VALUE | IWD | diversified_us_equity | 2.28% | 1.67% | 0.82% | 11.37% | -2.40% | -0.634 | 0.805 | 0.704 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 3.35% | -0.11% | -2.12% | 14.38% | -3.43% | -0.889 | 0.804 | 0.987 | 0.00% |
| SMALL_CAP | IWM | diversified_us_equity | 3.56% | -1.41% | 5.15% | 18.20% | -4.32% | -1.034 | 0.816 | 1.227 | -0.05% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.93% | -0.12% | 1.86% | 14.70% | -3.50% | -0.429 | 0.728 | 0.976 | -0.64% |
| DIVIDEND | SCHD | diversified_us_equity | 1.28% | 2.22% | -5.64% | 11.65% | -2.95% | 0.140 | 0.295 | 0.253 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | -0.03% | -1.74% | -9.49% | 13.20% | -3.75% | -0.695 | 0.016 | 0.013 | -2.26% |
| MOMENTUM | MTUM | diversified_us_equity | 3.25% | -6.57% | 20.31% | 38.96% | -17.99% | 1.289 | 0.779 | 1.560 | -10.40% |
| TECHNOLOGY | XLK | technology_and_growth | 7.20% | -1.45% | 25.47% | 35.97% | -15.86% | -0.952 | 0.859 | 1.731 | -5.05% |
| COMMUNICATIONS | XLC | technology_and_growth | 2.78% | -2.20% | -15.88% | 18.91% | -9.99% | -0.345 | 0.583 | 0.675 | -6.82% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 3.25% | -0.29% | -11.69% | 22.06% | -10.72% | -0.480 | 0.778 | 1.171 | -3.36% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.08% | -0.56% | -14.60% | 17.14% | -4.95% | -0.788 | -0.072 | -0.078 | -4.24% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.93% | -0.70% | -5.90% | 18.40% | -3.74% | -0.595 | 0.230 | 0.278 | -0.94% |
| FINANCIALS | XLF | financials | 1.16% | 0.84% | -6.40% | 13.62% | -2.08% | -0.721 | 0.548 | 0.623 | -0.69% |
| INDUSTRIALS | XLI | industrials_and_defense | 2.97% | -0.62% | -3.39% | 18.80% | -4.80% | -0.977 | 0.721 | 0.955 | -0.65% |
| ENERGY | XLE | energy | -3.44% | 2.02% | -5.08% | 23.05% | -13.21% | -0.857 | -0.151 | -0.248 | -7.43% |
| MATERIALS | XLB | materials_and_mining | 4.82% | 2.31% | -11.18% | 20.30% | -6.16% | -0.558 | 0.541 | 0.748 | -0.61% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.67% | -6.23% | -5.41% | 16.21% | -6.29% | -0.612 | 0.124 | 0.144 | -7.41% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.20% | -1.17% | -2.58% | 15.77% | -3.31% | -0.733 | 0.234 | 0.256 | -2.24% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.58% | -3.10% | -12.39% | 4.99% | -2.00% | -0.346 | 0.287 | 0.102 | -3.04% |
| LONG_TREASURY | TLT | rates_and_duration | 1.03% | -4.52% | -13.13% | 9.30% | -5.60% | -0.143 | 0.234 | 0.168 | -6.79% |
| TIPS | TIP | rates_and_duration | 0.22% | -3.10% | -11.12% | 3.47% | -1.53% | -0.481 | 0.275 | 0.071 | -1.09% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.72% | -3.52% | -12.20% | 5.30% | -2.83% | -0.353 | 0.479 | 0.196 | -2.40% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.65% | -2.56% | -10.02% | 3.49% | -0.99% | -0.629 | 0.779 | 0.234 | 0.00% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.59% | -3.11% | -11.77% | 4.11% | -1.71% | -0.244 | 0.397 | 0.115 | -1.80% |
| DEVELOPED_EX_US | VEA | international_equity | 3.21% | 0.19% | -3.45% | 19.95% | -4.85% | -0.956 | 0.804 | 1.079 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | 2.93% | -1.22% | -5.24% | 20.29% | -7.05% | -0.665 | 0.810 | 1.110 | -1.26% |
| EUROPE | VGK | international_equity | 2.22% | 1.87% | -7.76% | 15.81% | -3.12% | -0.823 | 0.746 | 0.919 | 0.00% |
| JAPAN | EWJ | international_equity | 4.88% | 0.75% | -2.32% | 23.20% | -7.86% | -0.889 | 0.720 | 1.176 | -0.07% |
| CHINA | MCHI | international_equity | 1.38% | 3.49% | -22.43% | 20.28% | -15.01% | -0.540 | 0.548 | 0.874 | -13.96% |
| INDIA | INDA | international_equity | 1.14% | -0.11% | -18.95% | 15.36% | -5.28% | -0.491 | 0.540 | 0.636 | -8.90% |
| GOLD | IAU | precious_metals | 7.23% | 2.51% | -25.91% | 24.80% | -16.01% | -0.517 | 0.314 | 0.689 | -19.58% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -1.77% | 2.19% | 4.77% | 21.98% | -16.55% | 0.187 | -0.173 | -0.266 | -8.78% |
| SEMICONDUCTORS | SMH | technology_and_growth | 7.80% | -6.99% | 47.96% | 55.02% | -24.62% | 0.715 | 0.787 | 2.373 | -12.89% |
| SOFTWARE | IGV | technology_and_growth | 8.57% | 6.52% | 6.33% | 34.60% | -21.29% | -0.912 | 0.509 | 1.177 | -12.80% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 7.57% | -3.62% | 20.17% | 40.91% | -20.19% | -0.236 | 0.848 | 1.906 | -9.68% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 11.11% | -0.34% | -3.73% | 39.56% | -23.82% | -0.664 | 0.802 | 2.193 | -11.10% |
| CYBERSECURITY | CIBR | technology_and_growth | 6.56% | 0.94% | 33.98% | 32.46% | -11.74% | -0.505 | 0.540 | 1.102 | -0.09% |
| SOLAR | TAN | clean_energy | 6.93% | -6.87% | -13.10% | 47.50% | -35.51% | -0.278 | 0.606 | 1.875 | -28.65% |
| METALS_MINING | XME | materials_and_mining | 14.99% | 9.24% | -22.15% | 42.20% | -26.49% | -0.350 | 0.604 | 1.763 | -12.81% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 2.36% | 0.22% | -3.12% | 11.08% | -2.04% | -0.808 | 0.770 | 0.703 | -0.06% |
| BIOTECH | XBI | healthcare_and_biotech | 7.05% | -7.07% | 24.69% | 30.19% | -10.51% | -0.357 | 0.485 | 1.024 | -4.21% |
| REGIONAL_BANKS | KRE | financials | 0.20% | -0.78% | -7.07% | 19.70% | -4.26% | -0.671 | 0.439 | 0.778 | -2.19% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 4.63% | 1.78% | -5.44% | 25.06% | -8.58% | -0.377 | 0.574 | 1.011 | -0.61% |
| CANADA | EWC | international_equity | 3.22% | 2.13% | -3.18% | 12.09% | -3.20% | -0.553 | 0.670 | 0.742 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 0.48% | 1.94% | -9.05% | 14.80% | -3.40% | -0.693 | 0.606 | 0.704 | -0.08% |
| AUSTRALIA | EWA | international_equity | 3.65% | 4.97% | -8.81% | 16.94% | -5.17% | -0.900 | 0.677 | 0.928 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 5.72% | -12.97% | 42.17% | 82.46% | -34.21% | 0.513 | 0.645 | 2.744 | -24.23% |
| TAIWAN | EWT | international_equity | 6.77% | -4.73% | 43.28% | 44.68% | -19.83% | -0.057 | 0.760 | 1.837 | -7.57% |
| BRAZIL | EWZ | international_equity | -3.57% | -1.78% | -15.90% | 22.83% | -13.88% | -0.977 | 0.503 | 0.981 | -14.51% |
| MEXICO | EWW | international_equity | 0.92% | 1.55% | -13.47% | 19.34% | -7.30% | -0.590 | 0.545 | 0.932 | -3.16% |
| SOUTH_AFRICA | EZA | international_equity | 9.48% | 7.20% | -21.21% | 31.47% | -13.92% | -0.515 | 0.629 | 1.599 | -12.77% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.75% | -3.09% | -11.53% | 4.96% | -1.93% | -0.320 | 0.395 | 0.135 | -1.69% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.56% | -3.53% | -11.00% | 3.16% | -2.15% | 0.690 | 0.378 | 0.087 | -1.25% |
| EMERGING_MARKET_BONDS | EMB | credit | 1.05% | -3.18% | -9.84% | 5.63% | -1.98% | -0.670 | 0.684 | 0.303 | -0.79% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.63% | -2.76% | -11.46% | 4.10% | -1.44% | -0.720 | 0.457 | 0.126 | -1.18% |
| SILVER | SLV | precious_metals | 9.82% | 3.34% | -30.34% | 49.17% | -36.50% | -0.578 | 0.358 | 1.711 | -45.55% |
| COPPER | CPER | non_energy_commodities | 0.86% | 2.83% | -4.40% | 28.59% | -10.57% | -0.524 | 0.550 | 1.201 | -2.33% |
| AGRICULTURE | DBA | non_energy_commodities | 0.40% | -3.19% | -4.00% | 13.96% | -8.67% | -0.487 | 0.081 | 0.070 | -3.86% |
| OIL | USO | energy | -8.66% | 5.36% | 30.62% | 53.18% | -32.49% | -0.531 | -0.334 | -1.234 | -22.87% |
| US_DOLLAR | UUP | currencies | -0.35% | -3.89% | -6.84% | 5.03% | -1.85% | -0.209 | -0.314 | -0.141 | -1.85% |
| EURO | FXE | currencies | 0.26% | -1.59% | -14.21% | 4.87% | -3.57% | -0.899 | 0.298 | 0.133 | -3.54% |
| YEN | FXY | currencies | 1.01% | 0.25% | -14.96% | 7.35% | -4.44% | 1.198 | 0.181 | 0.114 | -7.29% |
| BITCOIN_ETF | IBIT | crypto_assets | 3.25% | -0.10% | -12.33% | 36.66% | -28.36% | -0.601 | 0.503 | 1.734 | -48.38% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.84% | 6.84% | -17.71% | 52.88% | -33.56% | -0.325 | 0.533 | 2.773 | -60.45% |
