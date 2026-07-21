# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-20
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.95% |
| spy_return_21s | 0.41% |
| rsp_return_5s | -0.84% |
| rsp_return_21s | 2.03% |
| hyg_return_5s | 0.20% |
| hyg_return_21s | 0.40% |
| tlt_return_5s | -0.10% |
| tlt_return_21s | -2.47% |
| uup_return_5s | -0.39% |
| uup_return_21s | 0.75% |
| uso_return_5s | 6.55% |
| uso_return_21s | 9.87% |
| iau_return_5s | 0.13% |
| iau_return_21s | -5.39% |
| rsp_minus_spy_5s | 0.10% |
| rsp_minus_spy_21s | 1.62% |
| positive_asset_share_5s | 39.13% |
| positive_asset_share_21s | 46.38% |
| active_return_dispersion_5s | 2.17% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.95% | -1.37% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 1.01% | -1.11% | 0.25% | -0.01% | -0.068 | -0.213 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.69% | 0.00% | 0.00% | 11.95% | -2.38% | -0.406 | 1.000 | 1.000 | -2.05% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.66% | -0.01% | 0.02% | 11.19% | -1.82% | -0.440 | 0.992 | 0.989 | -1.88% |
| NASDAQ100 | QQQ | technology_and_growth | -3.02% | -1.26% | -2.75% | 25.63% | -6.01% | -0.524 | 0.918 | 1.713 | -6.61% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.33% | -0.80% | -1.38% | 21.84% | -4.13% | 0.292 | 0.886 | 1.275 | -7.14% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.13% | 0.68% | 1.64% | 10.70% | -1.06% | 0.106 | 0.713 | 0.651 | -1.00% |
| MID_CAP | IJH | diversified_us_equity | -0.93% | 0.53% | -1.02% | 12.02% | -3.09% | -0.639 | 0.763 | 0.855 | -2.83% |
| SMALL_CAP | IWM | diversified_us_equity | -1.17% | 0.55% | -0.13% | 12.57% | -2.71% | -0.723 | 0.781 | 1.098 | -2.71% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.20% | 1.43% | 1.48% | 10.74% | -1.83% | -0.721 | 0.667 | 0.792 | -1.49% |
| DIVIDEND | SCHD | diversified_us_equity | 1.27% | 1.53% | 1.42% | 12.63% | -1.18% | 0.333 | 0.096 | 0.088 | -0.88% |
| LOW_VOL | SPLV | diversified_us_equity | 0.82% | 0.53% | 3.06% | 14.91% | -1.89% | -0.725 | -0.278 | -0.289 | -1.10% |
| MOMENTUM | MTUM | diversified_us_equity | -3.21% | -2.87% | -5.52% | 42.05% | -12.49% | 1.512 | 0.766 | 2.109 | -12.33% |
| TECHNOLOGY | XLK | technology_and_growth | -3.23% | -2.13% | -3.68% | 33.09% | -8.62% | -0.986 | 0.841 | 2.143 | -11.25% |
| COMMUNICATIONS | XLC | technology_and_growth | -2.28% | 0.24% | 1.09% | 18.27% | -3.28% | -0.155 | 0.461 | 0.547 | -7.19% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.04% | -0.29% | -0.69% | 18.94% | -3.06% | -0.074 | 0.741 | 1.056 | -7.59% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.67% | 1.26% | 0.42% | 19.04% | -2.11% | -0.622 | -0.303 | -0.382 | -4.53% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.61% | -0.39% | 6.20% | 22.12% | -3.74% | -0.175 | -0.093 | -0.131 | -3.16% |
| FINANCIALS | XLF | financials | -0.92% | 0.89% | 2.73% | 14.11% | -2.08% | 0.621 | 0.178 | 0.180 | -1.25% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.08% | -0.30% | -0.69% | 17.40% | -4.01% | -0.636 | 0.646 | 0.964 | -4.01% |
| ENERGY | XLE | energy | 2.55% | 3.06% | 3.17% | 20.72% | -3.03% | -0.585 | -0.386 | -0.720 | -6.72% |
| MATERIALS | XLB | materials_and_mining | -0.93% | -0.14% | -3.77% | 17.10% | -3.81% | -0.557 | 0.544 | 0.805 | -5.93% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.62% | -0.76% | 2.12% | 14.92% | -3.10% | -0.616 | -0.043 | -0.058 | -4.58% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.50% | 2.13% | 1.18% | 16.43% | -2.67% | -0.788 | -0.090 | -0.113 | -0.51% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.26% | 1.21% | -1.82% | 4.85% | -1.54% | -0.448 | 0.546 | 0.210 | -2.99% |
| LONG_TREASURY | TLT | rates_and_duration | -0.42% | 0.85% | -3.74% | 9.09% | -3.72% | -0.416 | 0.411 | 0.280 | -5.90% |
| TIPS | TIP | rates_and_duration | -0.02% | 1.07% | -1.43% | 3.67% | -0.85% | -0.507 | 0.556 | 0.152 | -0.92% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.40% | 1.12% | -2.69% | 4.92% | -2.16% | 0.315 | 0.579 | 0.235 | -2.28% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.16% | 1.15% | -1.17% | 2.42% | -0.44% | -0.709 | 0.777 | 0.217 | -0.24% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.19% | 1.19% | -1.95% | 3.88% | -1.34% | -0.367 | 0.585 | 0.186 | -1.79% |
| DEVELOPED_EX_US | VEA | international_equity | -2.25% | 0.19% | -3.97% | 18.30% | -4.37% | -0.285 | 0.837 | 1.351 | -4.37% |
| EMERGING_MARKETS | VWO | international_equity | -2.61% | -0.52% | -2.96% | 20.03% | -5.55% | 0.032 | 0.870 | 1.375 | -5.40% |
| EUROPE | VGK | international_equity | -1.60% | 0.75% | -1.56% | 13.43% | -2.53% | -1.450 | 0.720 | 1.012 | -2.53% |
| JAPAN | EWJ | international_equity | -3.28% | -1.52% | -3.20% | 24.53% | -6.74% | -0.493 | 0.792 | 1.350 | -6.74% |
| CHINA | MCHI | international_equity | -0.13% | 3.90% | -2.26% | 20.85% | -4.75% | -0.121 | 0.520 | 0.855 | -17.74% |
| INDIA | INDA | international_equity | -0.35% | 0.45% | -1.92% | 13.12% | -2.74% | -0.676 | 0.583 | 0.700 | -12.19% |
| GOLD | IAU | precious_metals | -1.22% | 1.08% | -6.88% | 21.85% | -6.08% | -0.275 | 0.693 | 1.280 | -25.81% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.22% | 3.79% | 0.81% | 21.68% | -4.59% | 3.866 | -0.134 | -0.218 | -8.09% |
| SEMICONDUCTORS | SMH | technology_and_growth | -5.41% | -3.63% | -7.51% | 56.43% | -16.80% | 0.334 | 0.787 | 3.177 | -16.46% |
| SOFTWARE | IGV | technology_and_growth | -1.02% | 1.25% | 2.60% | 25.02% | -4.93% | -1.174 | 0.344 | 0.916 | -21.05% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -3.24% | -2.58% | -6.08% | 38.80% | -12.51% | -0.180 | 0.830 | 2.500 | -15.68% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -4.02% | -2.43% | -9.54% | 32.62% | -12.79% | -0.892 | 0.851 | 2.492 | -18.91% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.40% | 0.89% | 7.76% | 26.85% | -3.10% | -0.493 | 0.428 | 1.077 | -3.10% |
| SOLAR | TAN | clean_energy | -5.57% | 0.14% | -10.49% | 39.40% | -13.78% | -1.340 | 0.738 | 2.597 | -28.73% |
| METALS_MINING | XME | materials_and_mining | -5.29% | -3.32% | -15.08% | 28.32% | -17.39% | -0.757 | 0.699 | 2.171 | -26.37% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.26% | 0.10% | 1.54% | 9.89% | -1.30% | -0.446 | 0.713 | 0.596 | -1.23% |
| BIOTECH | XBI | healthcare_and_biotech | -3.38% | -1.89% | 10.18% | 29.48% | -8.12% | -0.179 | 0.357 | 0.837 | -8.12% |
| REGIONAL_BANKS | KRE | financials | 0.15% | 1.97% | 4.83% | 20.25% | -3.73% | 0.107 | 0.158 | 0.254 | -2.61% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.02% | -1.51% | -4.56% | 19.45% | -8.58% | -0.794 | 0.487 | 0.967 | -8.58% |
| CANADA | EWC | international_equity | -1.46% | 0.76% | -0.44% | 8.85% | -1.55% | -0.304 | 0.597 | 0.615 | -1.46% |
| UNITED_KINGDOM | EWU | international_equity | -0.81% | 1.01% | -0.41% | 13.83% | -1.93% | -0.587 | 0.493 | 0.653 | -3.34% |
| AUSTRALIA | EWA | international_equity | -0.97% | 1.54% | -2.42% | 12.67% | -3.32% | -0.352 | 0.608 | 0.866 | -4.43% |
| SOUTH_KOREA | EWY | international_equity | -5.12% | -2.13% | -19.44% | 77.55% | -25.85% | 0.997 | 0.754 | 4.514 | -25.70% |
| TAIWAN | EWT | international_equity | -6.39% | -4.89% | -4.44% | 43.26% | -13.98% | 0.798 | 0.794 | 2.539 | -13.98% |
| BRAZIL | EWZ | international_equity | -1.11% | 1.20% | 2.38% | 19.58% | -2.22% | -0.649 | 0.438 | 0.778 | -14.17% |
| MEXICO | EWW | international_equity | -0.40% | 2.21% | -5.46% | 17.60% | -4.58% | -0.544 | 0.625 | 0.989 | -6.20% |
| SOUTH_AFRICA | EZA | international_equity | -3.31% | -0.86% | -7.01% | 21.63% | -7.66% | -0.669 | 0.771 | 1.961 | -22.82% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.28% | 1.28% | -2.00% | 4.30% | -1.45% | -0.306 | 0.591 | 0.220 | -1.74% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.34% | 0.48% | -1.17% | 2.47% | -1.09% | -0.280 | 0.599 | 0.123 | -1.09% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.38% | 0.93% | -1.89% | 4.36% | -1.09% | -0.952 | 0.744 | 0.332 | -1.09% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.44% | 0.80% | -2.01% | 3.46% | -1.22% | -0.571 | 0.558 | 0.183 | -1.69% |
| SILVER | SLV | precious_metals | -2.36% | -1.32% | -15.31% | 42.68% | -16.86% | -0.740 | 0.658 | 2.566 | -51.72% |
| COPPER | CPER | non_energy_commodities | -0.54% | 2.21% | -3.18% | 23.87% | -6.56% | -0.816 | 0.714 | 1.598 | -5.37% |
| AGRICULTURE | DBA | non_energy_commodities | 0.14% | 2.03% | 1.91% | 15.11% | -1.52% | -0.784 | -0.005 | -0.005 | -2.47% |
| OIL | USO | energy | 3.40% | 7.50% | 1.75% | 48.17% | -10.10% | -0.409 | -0.322 | -1.292 | -17.95% |
| US_DOLLAR | UUP | currencies | 0.50% | 0.56% | -0.23% | 4.62% | -0.98% | 0.015 | -0.547 | -0.209 | -0.49% |
| EURO | FXE | currencies | -0.42% | 1.29% | -2.28% | 4.35% | -1.21% | -0.565 | 0.568 | 0.208 | -4.80% |
| YEN | FXY | currencies | -0.12% | 0.95% | -2.47% | 5.27% | -1.16% | -0.080 | 0.223 | 0.112 | -10.17% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.22% | 5.69% | -4.50% | 36.92% | -8.79% | -0.346 | 0.478 | 1.413 | -48.25% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.31% | 8.13% | 0.93% | 50.67% | -10.18% | 0.538 | 0.578 | 2.397 | -60.84% |
