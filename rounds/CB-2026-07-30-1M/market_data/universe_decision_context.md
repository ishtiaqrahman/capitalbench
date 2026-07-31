# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-30
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.48% |
| spy_return_21s | -0.68% |
| rsp_return_5s | 1.63% |
| rsp_return_21s | 1.23% |
| hyg_return_5s | 0.30% |
| hyg_return_21s | -0.16% |
| tlt_return_5s | -0.44% |
| tlt_return_21s | -3.83% |
| uup_return_5s | -1.47% |
| uup_return_21s | -0.95% |
| uso_return_5s | -8.61% |
| uso_return_21s | 19.77% |
| iau_return_5s | 1.51% |
| iau_return_21s | 2.37% |
| rsp_minus_spy_5s | 1.16% |
| rsp_minus_spy_21s | 1.91% |
| positive_asset_share_5s | 68.12% |
| positive_asset_share_21s | 50.72% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.68% | -7.95% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | 0.98% | -6.47% | 0.21% | -0.01% | -0.426 | -0.110 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.48% | 0.00% | 0.00% | 13.71% | -4.49% | -0.946 | 1.000 | 1.000 | -2.10% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.43% | -0.34% | 0.55% | 13.62% | -4.36% | -0.828 | 0.995 | 1.012 | -1.88% |
| NASDAQ100 | QQQ | technology_and_growth | -1.22% | -6.50% | 8.61% | 25.54% | -11.22% | -0.835 | 0.931 | 1.401 | -8.29% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.98% | -4.75% | -2.83% | 20.03% | -11.35% | -0.802 | 0.936 | 1.270 | -8.73% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.84% | 4.10% | 3.36% | 12.21% | -2.40% | -0.656 | 0.805 | 0.711 | -0.53% |
| MID_CAP | IJH | diversified_us_equity | -0.13% | -1.60% | 3.61% | 14.81% | -4.25% | -0.972 | 0.802 | 0.983 | -2.28% |
| SMALL_CAP | IWM | diversified_us_equity | 0.17% | -1.94% | 6.63% | 18.65% | -4.81% | -1.177 | 0.817 | 1.231 | -2.62% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.55% | 0.95% | 6.46% | 15.31% | -4.01% | -0.708 | 0.731 | 0.989 | -1.07% |
| DIVIDEND | SCHD | diversified_us_equity | 1.86% | 6.04% | 2.06% | 12.42% | -2.95% | -0.178 | 0.293 | 0.255 | -1.42% |
| LOW_VOL | SPLV | diversified_us_equity | 0.03% | 2.84% | -4.11% | 13.45% | -4.09% | -0.866 | 0.032 | 0.027 | -2.04% |
| MOMENTUM | MTUM | diversified_us_equity | -4.84% | -12.17% | 24.12% | 39.19% | -17.99% | 1.450 | 0.776 | 1.538 | -13.46% |
| TECHNOLOGY | XLK | technology_and_growth | -1.52% | -7.08% | 20.03% | 35.11% | -15.86% | -0.968 | 0.861 | 1.710 | -11.24% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.14% | 0.17% | -15.66% | 17.93% | -9.99% | -0.087 | 0.584 | 0.667 | -10.73% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 3.34% | -3.49% | -11.26% | 20.91% | -10.72% | -0.361 | 0.790 | 1.182 | -9.38% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 2.72% | 3.57% | -5.77% | 17.50% | -4.95% | -0.747 | -0.065 | -0.071 | -3.85% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.29% | 3.74% | -4.26% | 18.73% | -3.74% | -0.582 | 0.239 | 0.295 | -2.24% |
| FINANCIALS | XLF | financials | 2.10% | 7.00% | -5.91% | 13.66% | -2.42% | -0.706 | 0.560 | 0.642 | -1.04% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.95% | -3.01% | 5.49% | 20.06% | -4.80% | -1.099 | 0.716 | 0.941 | -3.86% |
| ENERGY | XLE | energy | -0.71% | 11.70% | -0.38% | 24.23% | -13.21% | -0.882 | -0.130 | -0.214 | -5.07% |
| MATERIALS | XLB | materials_and_mining | 2.68% | 2.27% | -5.36% | 20.11% | -6.43% | -0.620 | 0.544 | 0.746 | -2.90% |
| UTILITIES | XLU | rate_sensitive_defensive | -3.31% | -0.82% | -1.91% | 17.22% | -8.00% | -0.858 | 0.138 | 0.160 | -5.18% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.78% | 3.56% | 1.51% | 16.29% | -3.38% | -0.875 | 0.240 | 0.266 | -1.54% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.39% | -0.43% | -7.74% | 4.99% | -2.00% | -0.997 | 0.233 | 0.085 | -3.33% |
| LONG_TREASURY | TLT | rates_and_duration | -0.44% | -3.15% | -7.44% | 9.35% | -4.97% | -0.776 | 0.197 | 0.143 | -7.12% |
| TIPS | TIP | rates_and_duration | 0.23% | 0.10% | -7.21% | 3.51% | -1.53% | -0.765 | 0.244 | 0.065 | -1.21% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.14% | -1.42% | -7.50% | 5.31% | -2.83% | -0.454 | 0.434 | 0.178 | -2.95% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.30% | 0.52% | -6.78% | 3.65% | -1.01% | -0.739 | 0.772 | 0.231 | -0.50% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.29% | -0.36% | -7.48% | 4.11% | -1.71% | -0.461 | 0.343 | 0.101 | -2.12% |
| DEVELOPED_EX_US | VEA | international_equity | 1.88% | 0.46% | -0.42% | 21.49% | -4.85% | -0.706 | 0.804 | 1.078 | -1.80% |
| EMERGING_MARKETS | VWO | international_equity | 0.15% | -1.83% | -4.67% | 20.78% | -7.05% | -0.571 | 0.804 | 1.098 | -4.98% |
| EUROPE | VGK | international_equity | 3.60% | 3.45% | -5.32% | 18.36% | -3.86% | -0.916 | 0.748 | 0.926 | 0.00% |
| JAPAN | EWJ | international_equity | 2.40% | 0.70% | 2.10% | 23.96% | -7.86% | -0.798 | 0.718 | 1.167 | -3.79% |
| CHINA | MCHI | international_equity | 4.03% | 9.44% | -27.58% | 21.04% | -15.01% | -0.370 | 0.559 | 0.896 | -15.58% |
| INDIA | INDA | international_equity | 4.35% | 1.31% | -12.03% | 15.98% | -5.64% | -0.513 | 0.520 | 0.612 | -10.11% |
| GOLD | IAU | precious_metals | 1.51% | 3.05% | -33.38% | 24.06% | -16.01% | -0.610 | 0.309 | 0.671 | -23.89% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -3.10% | 10.88% | -0.80% | 22.26% | -16.55% | -0.047 | -0.135 | -0.206 | -7.46% |
| SEMICONDUCTORS | SMH | technology_and_growth | -7.11% | -17.16% | 49.47% | 55.23% | -24.62% | 1.100 | 0.783 | 2.345 | -19.44% |
| SOFTWARE | IGV | technology_and_growth | 7.13% | 3.67% | -14.59% | 33.45% | -21.29% | -0.742 | 0.502 | 1.135 | -20.77% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.08% | -9.87% | 14.43% | 40.31% | -20.19% | -0.074 | 0.846 | 1.876 | -16.32% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.46% | -13.11% | -6.62% | 39.42% | -23.82% | -0.959 | 0.796 | 2.146 | -20.75% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.62% | 0.87% | 18.02% | 32.28% | -11.74% | -0.265 | 0.532 | 1.073 | -4.97% |
| SOLAR | TAN | clean_energy | -5.70% | -15.06% | -4.83% | 46.70% | -35.51% | -0.735 | 0.593 | 1.808 | -32.58% |
| METALS_MINING | XME | materials_and_mining | -1.27% | -4.06% | -24.77% | 41.00% | -26.49% | -0.506 | 0.597 | 1.712 | -23.26% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.63% | 1.91% | 0.24% | 11.21% | -2.04% | -0.850 | 0.768 | 0.703 | -1.06% |
| BIOTECH | XBI | healthcare_and_biotech | -0.51% | -3.61% | 17.82% | 30.43% | -9.96% | -0.222 | 0.483 | 1.005 | -7.80% |
| REGIONAL_BANKS | KRE | financials | 1.00% | 2.08% | 3.77% | 19.93% | -5.29% | -0.645 | 0.443 | 0.790 | -2.59% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.04% | -1.09% | -4.08% | 25.92% | -8.58% | -0.399 | 0.563 | 0.982 | -5.04% |
| CANADA | EWC | international_equity | 1.65% | 4.41% | -5.18% | 13.19% | -3.20% | -0.733 | 0.683 | 0.762 | -0.08% |
| UNITED_KINGDOM | EWU | international_equity | 4.24% | 6.19% | -6.74% | 17.04% | -3.94% | -0.487 | 0.612 | 0.712 | 0.00% |
| AUSTRALIA | EWA | international_equity | 4.67% | 6.58% | -6.59% | 18.97% | -6.84% | -0.900 | 0.681 | 0.925 | -0.07% |
| SOUTH_KOREA | EWY | international_equity | -7.28% | -19.47% | 52.84% | 82.92% | -34.21% | 0.590 | 0.644 | 2.712 | -26.46% |
| TAIWAN | EWT | international_equity | -5.85% | -12.77% | 44.61% | 44.35% | -19.83% | 0.090 | 0.745 | 1.775 | -15.72% |
| BRAZIL | EWZ | international_equity | 1.00% | 6.56% | -17.09% | 24.26% | -15.56% | -1.053 | 0.519 | 1.012 | -11.63% |
| MEXICO | EWW | international_equity | 2.81% | 3.12% | -10.94% | 20.75% | -7.30% | -0.900 | 0.542 | 0.929 | -3.68% |
| SOUTH_AFRICA | EZA | international_equity | 6.09% | 2.14% | -27.38% | 32.92% | -14.17% | -0.514 | 0.627 | 1.582 | -19.71% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.44% | -0.27% | -7.44% | 4.86% | -1.93% | -0.475 | 0.340 | 0.117 | -2.03% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.48% | -0.78% | -6.80% | 3.07% | -2.15% | 0.396 | 0.329 | 0.076 | -1.68% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.28% | -0.62% | -5.98% | 5.87% | -2.10% | -0.670 | 0.669 | 0.295 | -1.69% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.36% | -0.23% | -6.98% | 4.22% | -1.44% | -0.572 | 0.427 | 0.117 | -1.57% |
| SILVER | SLV | precious_metals | 2.77% | 0.74% | -57.32% | 50.61% | -36.50% | -0.647 | 0.355 | 1.693 | -49.34% |
| COPPER | CPER | non_energy_commodities | 2.88% | 4.95% | -5.37% | 29.42% | -10.57% | -0.649 | 0.465 | 1.235 | -3.10% |
| AGRICULTURE | DBA | non_energy_commodities | -2.69% | 3.72% | -4.90% | 14.01% | -8.67% | -0.392 | 0.086 | 0.074 | -4.35% |
| OIL | USO | energy | -8.61% | 20.45% | 30.96% | 53.51% | -32.49% | -0.537 | -0.305 | -1.110 | -16.66% |
| US_DOLLAR | UUP | currencies | -1.47% | -0.27% | -1.27% | 5.39% | -1.61% | -0.181 | -0.282 | -0.131 | -1.61% |
| EURO | FXE | currencies | 1.37% | 1.72% | -12.07% | 4.97% | -3.57% | -0.805 | 0.261 | 0.122 | -3.80% |
| YEN | FXY | currencies | 2.80% | 2.70% | -13.81% | 8.32% | -4.58% | 0.524 | 0.140 | 0.090 | -8.34% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.14% | 10.92% | -42.05% | 37.21% | -28.36% | -0.638 | 0.514 | 1.771 | -48.52% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.83% | 22.72% | -55.67% | 52.99% | -34.41% | -0.401 | 0.554 | 2.899 | -60.34% |
