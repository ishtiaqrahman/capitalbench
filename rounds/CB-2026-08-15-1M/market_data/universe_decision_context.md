# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-14
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.40% |
| spy_return_21s | 3.41% |
| rsp_return_5s | 1.22% |
| rsp_return_21s | 3.59% |
| hyg_return_5s | 0.13% |
| hyg_return_21s | 0.52% |
| tlt_return_5s | -0.87% |
| tlt_return_21s | -2.18% |
| uup_return_5s | 0.14% |
| uup_return_21s | -0.81% |
| uso_return_5s | 7.31% |
| uso_return_21s | 6.12% |
| iau_return_5s | 0.73% |
| iau_return_21s | 10.00% |
| rsp_minus_spy_5s | 0.82% |
| rsp_minus_spy_21s | 0.17% |
| positive_asset_share_5s | 65.22% |
| positive_asset_share_21s | 75.36% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.41% | -10.78% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -3.11% | -9.27% | 0.21% | -0.01% | -0.408 | -0.109 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.40% | 0.00% | 0.00% | 13.92% | -4.49% | -0.843 | 1.000 | 1.000 | -0.20% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.54% | 0.17% | 0.17% | 13.86% | -4.36% | -0.797 | 0.995 | 1.012 | -0.12% |
| NASDAQ100 | QQQ | technology_and_growth | 1.11% | 0.15% | 7.03% | 25.85% | -11.22% | -0.776 | 0.931 | 1.419 | -1.91% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.55% | -0.04% | -2.61% | 20.99% | -11.35% | -0.828 | 0.937 | 1.285 | -2.62% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.39% | 0.24% | 2.27% | 11.31% | -2.40% | -0.591 | 0.804 | 0.700 | -0.05% |
| MID_CAP | IJH | diversified_us_equity | 1.13% | 0.69% | -4.96% | 14.28% | -3.09% | -0.892 | 0.803 | 0.987 | 0.00% |
| SMALL_CAP | IWM | diversified_us_equity | 1.17% | -0.20% | 3.58% | 18.09% | -4.03% | -1.091 | 0.817 | 1.213 | 0.00% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.85% | -1.96% | 3.64% | 14.60% | -2.75% | -0.479 | 0.731 | 0.960 | 0.00% |
| DIVIDEND | SCHD | diversified_us_equity | 1.83% | 1.07% | -3.62% | 11.74% | -2.95% | 0.113 | 0.286 | 0.245 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 0.20% | -3.98% | -7.50% | 13.14% | -3.75% | -0.745 | 0.018 | 0.015 | -2.06% |
| MOMENTUM | MTUM | diversified_us_equity | 2.55% | 1.14% | 10.73% | 38.62% | -17.99% | 0.493 | 0.777 | 1.565 | -8.11% |
| TECHNOLOGY | XLK | technology_and_growth | 1.09% | 3.62% | 17.05% | 35.21% | -15.86% | -1.022 | 0.858 | 1.734 | -4.02% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.53% | -3.15% | -11.95% | 19.30% | -9.78% | -0.506 | 0.578 | 0.673 | -5.39% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.38% | -2.68% | -9.33% | 22.08% | -10.72% | -0.717 | 0.777 | 1.172 | -4.70% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.14% | -3.09% | -13.38% | 16.99% | -4.95% | -0.816 | -0.069 | -0.076 | -3.15% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.02% | 0.03% | -6.18% | 18.22% | -3.74% | -0.784 | 0.223 | 0.270 | -0.64% |
| FINANCIALS | XLF | financials | 0.97% | -0.93% | -0.04% | 13.22% | -2.08% | -0.938 | 0.544 | 0.617 | -0.17% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.72% | 0.12% | -5.95% | 18.65% | -4.80% | -1.056 | 0.717 | 0.951 | 0.00% |
| ENERGY | XLE | energy | 7.67% | 5.16% | -3.69% | 24.44% | -13.21% | -0.923 | -0.157 | -0.266 | -0.33% |
| MATERIALS | XLB | materials_and_mining | -0.61% | -0.17% | -13.66% | 20.30% | -5.09% | -0.461 | 0.533 | 0.735 | -1.31% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.61% | -5.96% | -8.94% | 16.23% | -6.83% | -0.482 | 0.123 | 0.144 | -5.92% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.64% | -3.83% | -3.09% | 16.24% | -4.19% | -0.580 | 0.241 | 0.267 | -1.61% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.14% | -3.80% | -12.41% | 5.04% | -2.00% | -0.289 | 0.293 | 0.105 | -3.17% |
| LONG_TREASURY | TLT | rates_and_duration | -0.87% | -5.60% | -14.63% | 9.38% | -5.60% | 0.080 | 0.244 | 0.176 | -7.60% |
| TIPS | TIP | rates_and_duration | -0.08% | -3.59% | -11.14% | 3.44% | -1.40% | -0.412 | 0.284 | 0.073 | -1.17% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.40% | -4.27% | -12.30% | 5.40% | -2.83% | -0.406 | 0.485 | 0.200 | -2.80% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.13% | -2.89% | -9.75% | 3.53% | -0.80% | -0.632 | 0.783 | 0.237 | -0.10% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.12% | -3.73% | -11.68% | 4.14% | -1.71% | -0.207 | 0.404 | 0.118 | -1.92% |
| DEVELOPED_EX_US | VEA | international_equity | 0.95% | 1.66% | -7.83% | 19.55% | -4.85% | -0.933 | 0.803 | 1.079 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | -0.60% | -1.25% | -8.79% | 19.94% | -7.05% | -0.744 | 0.811 | 1.112 | -1.85% |
| EUROPE | VGK | international_equity | -0.25% | 0.62% | -8.90% | 15.58% | -3.12% | -0.803 | 0.746 | 0.918 | -0.25% |
| JAPAN | EWJ | international_equity | 1.35% | 3.44% | -11.81% | 23.15% | -7.86% | -0.997 | 0.717 | 1.171 | -0.26% |
| CHINA | MCHI | international_equity | -3.43% | -2.51% | -20.82% | 19.40% | -12.54% | -0.483 | 0.543 | 0.862 | -16.91% |
| INDIA | INDA | international_equity | -1.17% | -1.17% | -19.10% | 13.56% | -4.59% | -0.579 | 0.544 | 0.642 | -9.97% |
| GOLD | IAU | precious_metals | 0.73% | 6.59% | -29.90% | 25.10% | -14.55% | -0.487 | 0.312 | 0.688 | -18.99% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.83% | 2.19% | 8.99% | 22.10% | -16.24% | -0.333 | -0.173 | -0.271 | -5.29% |
| SEMICONDUCTORS | SMH | technology_and_growth | 0.88% | -0.09% | 29.31% | 54.02% | -24.62% | 0.222 | 0.786 | 2.379 | -12.12% |
| SOFTWARE | IGV | technology_and_growth | 1.35% | 7.67% | 4.98% | 35.27% | -21.29% | -0.841 | 0.509 | 1.188 | -11.62% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.34% | 4.83% | 9.74% | 39.71% | -20.19% | -0.505 | 0.849 | 1.915 | -8.47% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.99% | 6.96% | -12.83% | 38.73% | -23.82% | -0.659 | 0.801 | 2.189 | -9.34% |
| CYBERSECURITY | CIBR | technology_and_growth | 1.79% | 4.98% | 30.74% | 32.50% | -11.74% | -0.359 | 0.537 | 1.105 | -2.54% |
| SOLAR | TAN | clean_energy | -1.48% | -7.49% | -15.49% | 46.00% | -35.51% | -0.253 | 0.604 | 1.878 | -29.70% |
| METALS_MINING | XME | materials_and_mining | 1.21% | 14.92% | -25.83% | 41.92% | -26.49% | -0.344 | 0.597 | 1.741 | -11.75% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.22% | 0.17% | -2.80% | 11.06% | -2.04% | -0.861 | 0.771 | 0.699 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | 0.03% | 0.15% | 12.74% | 30.35% | -10.51% | -0.579 | 0.479 | 1.007 | -4.18% |
| REGIONAL_BANKS | KRE | financials | 2.26% | -3.40% | 0.72% | 18.94% | -3.73% | -0.878 | 0.430 | 0.753 | 0.00% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.99% | 6.26% | -11.35% | 25.13% | -8.58% | -0.399 | 0.569 | 1.008 | 0.00% |
| CANADA | EWC | international_equity | 1.52% | 1.37% | -2.80% | 11.88% | -3.20% | -0.537 | 0.672 | 0.745 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | -0.78% | -0.67% | -9.43% | 14.66% | -3.40% | -0.559 | 0.604 | 0.703 | -0.86% |
| AUSTRALIA | EWA | international_equity | -2.50% | 1.17% | -11.06% | 16.84% | -5.17% | -0.824 | 0.666 | 0.915 | -2.50% |
| SOUTH_KOREA | EWY | international_equity | 8.22% | 6.61% | 14.11% | 79.71% | -34.21% | 0.065 | 0.643 | 2.757 | -18.00% |
| TAIWAN | EWT | international_equity | 3.86% | 3.49% | 27.26% | 44.24% | -19.83% | -0.465 | 0.761 | 1.849 | -4.00% |
| BRAZIL | EWZ | international_equity | -3.99% | -7.38% | -18.12% | 22.27% | -9.26% | -0.833 | 0.503 | 0.985 | -17.92% |
| MEXICO | EWW | international_equity | -3.24% | -3.69% | -15.28% | 19.37% | -6.47% | -0.534 | 0.543 | 0.932 | -6.30% |
| SOUTH_AFRICA | EZA | international_equity | -3.04% | 3.88% | -24.04% | 31.59% | -12.38% | -0.510 | 0.626 | 1.594 | -15.43% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.08% | -3.64% | -11.53% | 4.94% | -1.85% | -0.280 | 0.399 | 0.137 | -1.77% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.08% | -3.99% | -10.44% | 3.40% | -2.15% | 0.826 | 0.385 | 0.091 | -1.32% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.20% | -3.76% | -10.01% | 5.78% | -1.96% | -0.747 | 0.682 | 0.306 | -1.42% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.48% | -3.66% | -11.38% | 4.10% | -1.44% | -0.728 | 0.464 | 0.129 | -1.65% |
| SILVER | SLV | precious_metals | 1.70% | 12.64% | -36.38% | 46.56% | -33.27% | -0.529 | 0.356 | 1.709 | -44.62% |
| COPPER | CPER | non_energy_commodities | 0.28% | 2.04% | -7.60% | 26.54% | -10.57% | -0.496 | 0.541 | 1.173 | -2.06% |
| AGRICULTURE | DBA | non_energy_commodities | 0.54% | -2.76% | -4.21% | 13.52% | -7.21% | -0.655 | 0.080 | 0.069 | -3.34% |
| OIL | USO | energy | 7.31% | 2.71% | 45.41% | 53.84% | -32.49% | -0.562 | -0.333 | -1.246 | -17.23% |
| US_DOLLAR | UUP | currencies | 0.14% | -4.22% | -5.11% | 4.96% | -1.85% | -0.413 | -0.309 | -0.138 | -1.71% |
| EURO | FXE | currencies | 0.10% | -2.18% | -14.08% | 4.77% | -2.66% | -0.852 | 0.289 | 0.129 | -3.44% |
| YEN | FXY | currencies | -1.13% | -1.41% | -17.02% | 7.60% | -3.45% | 1.454 | 0.179 | 0.114 | -8.34% |
| BITCOIN_ETF | IBIT | crypto_assets | -3.18% | -5.50% | -12.56% | 35.84% | -27.90% | -0.656 | 0.508 | 1.750 | -50.02% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.00% | -3.06% | -13.06% | 52.52% | -32.37% | -0.478 | 0.533 | 2.738 | -61.25% |
