# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-10
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.96% |
| spy_return_21s | -1.65% |
| rsp_return_5s | -2.48% |
| rsp_return_21s | -3.41% |
| hyg_return_5s | -0.62% |
| hyg_return_21s | -0.58% |
| tlt_return_5s | -1.43% |
| tlt_return_21s | -1.34% |
| uup_return_5s | -0.50% |
| uup_return_21s | -0.39% |
| uso_return_5s | 12.21% |
| uso_return_21s | 24.11% |
| iau_return_5s | -1.55% |
| iau_return_21s | -1.11% |
| rsp_minus_spy_5s | -1.53% |
| rsp_minus_spy_21s | -1.76% |
| positive_asset_share_5s | 21.74% |
| positive_asset_share_21s | 21.74% |
| active_return_dispersion_5s | 2.35% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.96% | 0.70% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.02% | 1.03% | 0.91% | 0.15% | 0.00% | -0.418 | -0.007 | -0.000 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.60% | 0.00% | 0.00% | 8.41% | -2.58% | -0.655 | 1.000 | 1.000 | -2.58% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.71% | -0.01% | -0.29% | 8.79% | -2.88% | -0.195 | 0.992 | 0.981 | -2.88% |
| NASDAQ100 | QQQ | technology_and_growth | -1.43% | 0.88% | -0.58% | 13.00% | -3.52% | -0.833 | 0.911 | 1.698 | -4.92% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.69% | 0.56% | -0.75% | 13.77% | -3.68% | -0.619 | 0.889 | 1.420 | -5.70% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.67% | -0.50% | 0.38% | 8.49% | -2.33% | -0.306 | 0.649 | 0.544 | -2.33% |
| MID_CAP | IJH | diversified_us_equity | -2.62% | -0.71% | -2.72% | 11.28% | -6.11% | -0.640 | 0.781 | 0.828 | -6.11% |
| SMALL_CAP | IWM | diversified_us_equity | -2.81% | -1.19% | -1.62% | 12.82% | -5.70% | -0.480 | 0.755 | 0.902 | -5.70% |
| SMALL_VALUE | IWN | diversified_us_equity | -2.52% | -0.87% | -0.16% | 10.28% | -3.72% | -0.411 | 0.617 | 0.591 | -3.72% |
| DIVIDEND | SCHD | diversified_us_equity | -2.33% | -1.96% | 2.86% | 10.68% | -3.46% | 0.829 | 0.078 | 0.074 | -3.46% |
| LOW_VOL | SPLV | diversified_us_equity | -1.43% | -0.37% | -0.42% | 8.74% | -3.34% | -0.398 | -0.154 | -0.145 | -5.34% |
| MOMENTUM | MTUM | diversified_us_equity | -0.56% | 3.01% | -2.96% | 21.59% | -7.93% | -1.145 | 0.656 | 1.858 | -12.19% |
| TECHNOLOGY | XLK | technology_and_growth | -1.10% | 1.84% | -0.64% | 20.79% | -5.62% | -0.764 | 0.804 | 2.010 | -6.44% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.47% | 0.14% | 1.73% | 16.65% | -2.25% | -0.737 | 0.387 | 0.611 | -6.60% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.57% | -1.57% | -2.97% | 16.52% | -6.11% | -0.346 | 0.674 | 1.143 | -9.73% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.76% | -1.89% | 1.69% | 15.11% | -5.03% | 0.144 | -0.150 | -0.200 | -6.52% |
| HEALTHCARE | XLV | healthcare_and_biotech | -3.38% | -3.26% | 3.64% | 20.05% | -5.70% | -0.626 | -0.119 | -0.183 | -5.70% |
| FINANCIALS | XLF | financials | -2.12% | -0.41% | 0.46% | 12.79% | -2.89% | -0.294 | 0.369 | 0.382 | -2.89% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.69% | -0.33% | -6.26% | 12.32% | -8.56% | -0.081 | 0.652 | 0.913 | -8.56% |
| ENERGY | XLE | energy | 1.36% | 0.70% | 7.54% | 15.15% | -2.65% | -0.274 | -0.438 | -0.767 | -0.58% |
| MATERIALS | XLB | materials_and_mining | -3.20% | -3.18% | 0.16% | 15.29% | -5.42% | 0.222 | 0.382 | 0.570 | -5.42% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.30% | 0.61% | -1.50% | 13.81% | -4.69% | -0.049 | -0.038 | -0.044 | -9.73% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -2.00% | -0.60% | -0.09% | 11.98% | -5.09% | -0.305 | -0.086 | -0.100 | -6.43% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.16% | -0.13% | 0.32% | 5.02% | -2.14% | -0.169 | 0.431 | 0.171 | -4.76% |
| LONG_TREASURY | TLT | rates_and_duration | -1.74% | -0.47% | 0.79% | 10.65% | -2.85% | 0.174 | 0.331 | 0.260 | -8.67% |
| TIPS | TIP | rates_and_duration | -0.60% | 0.46% | 0.67% | 3.84% | -1.22% | -0.423 | 0.338 | 0.096 | -1.78% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.06% | 0.02% | 0.52% | 6.09% | -1.93% | -0.613 | 0.495 | 0.217 | -4.01% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.68% | 0.34% | 0.74% | 2.93% | -1.09% | 0.004 | 0.771 | 0.186 | -1.09% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.98% | 0.14% | 0.55% | 4.41% | -1.66% | 0.003 | 0.466 | 0.154 | -3.02% |
| DEVELOPED_EX_US | VEA | international_equity | -2.49% | 0.03% | 0.56% | 12.46% | -2.53% | -0.159 | 0.770 | 1.067 | -2.53% |
| EMERGING_MARKETS | VWO | international_equity | -2.44% | -0.41% | 1.78% | 10.78% | -2.44% | -0.378 | 0.812 | 1.102 | -2.44% |
| EUROPE | VGK | international_equity | -2.53% | -0.74% | -0.75% | 9.02% | -4.05% | -0.942 | 0.711 | 0.763 | -4.05% |
| JAPAN | EWJ | international_equity | -1.87% | 1.37% | 0.45% | 16.00% | -4.27% | -0.586 | 0.728 | 1.298 | -2.06% |
| CHINA | MCHI | international_equity | -3.84% | -2.23% | -1.24% | 12.75% | -5.14% | -0.574 | 0.383 | 0.517 | -19.69% |
| INDIA | INDA | international_equity | -3.61% | -2.76% | 0.46% | 11.28% | -4.22% | -0.457 | 0.555 | 0.581 | -12.99% |
| GOLD | IAU | precious_metals | -2.54% | -0.59% | 1.15% | 27.66% | -7.40% | -0.189 | 0.397 | 0.809 | -19.99% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 5.47% | 6.15% | 7.12% | 17.01% | -2.57% | -0.269 | -0.337 | -0.593 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | -1.19% | 2.74% | -3.22% | 30.82% | -8.22% | -0.677 | 0.709 | 2.761 | -16.24% |
| SOFTWARE | IGV | technology_and_growth | -3.22% | -1.19% | 0.22% | 39.49% | -8.27% | -0.743 | 0.462 | 1.218 | -14.07% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.93% | 0.96% | 0.51% | 19.42% | -3.59% | -0.664 | 0.813 | 2.180 | -10.06% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.44% | 1.17% | -5.58% | 23.10% | -7.91% | -0.120 | 0.830 | 2.248 | -16.22% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.45% | 1.62% | -5.68% | 39.16% | -9.53% | -0.835 | 0.518 | 1.296 | -7.87% |
| SOLAR | TAN | clean_energy | -2.08% | 0.47% | -9.60% | 24.29% | -11.08% | -0.635 | 0.714 | 2.167 | -36.37% |
| METALS_MINING | XME | materials_and_mining | -3.25% | -2.97% | 2.08% | 36.51% | -6.69% | -0.970 | 0.559 | 1.679 | -13.54% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -2.66% | -1.53% | -0.25% | 9.90% | -4.31% | -0.639 | 0.667 | 0.582 | -4.31% |
| BIOTECH | XBI | healthcare_and_biotech | -4.27% | -4.21% | 5.32% | 32.95% | -7.51% | -0.939 | 0.267 | 0.628 | -7.51% |
| REGIONAL_BANKS | KRE | financials | -1.94% | 0.38% | -2.65% | 15.65% | -6.81% | -0.566 | 0.234 | 0.325 | -5.29% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.23% | -1.30% | -10.63% | 18.99% | -13.78% | -0.087 | 0.440 | 0.835 | -13.78% |
| CANADA | EWC | international_equity | -2.82% | -0.64% | 0.31% | 13.62% | -3.75% | 0.704 | 0.556 | 0.518 | -3.75% |
| UNITED_KINGDOM | EWU | international_equity | -2.18% | -0.47% | 0.54% | 8.89% | -3.77% | -0.267 | 0.359 | 0.360 | -3.77% |
| AUSTRALIA | EWA | international_equity | -3.80% | -2.21% | 0.97% | 14.26% | -4.44% | 1.369 | 0.558 | 0.716 | -4.44% |
| SOUTH_KOREA | EWY | international_equity | -3.22% | 3.15% | 7.65% | 48.59% | -8.13% | -0.743 | 0.621 | 3.513 | -16.61% |
| TAIWAN | EWT | international_equity | -2.91% | 0.49% | 5.98% | 22.48% | -4.15% | -0.854 | 0.737 | 2.254 | -2.91% |
| BRAZIL | EWZ | international_equity | 1.85% | 2.19% | 12.80% | 21.72% | -1.40% | 1.079 | 0.275 | 0.491 | -6.71% |
| MEXICO | EWW | international_equity | -1.80% | -0.31% | 0.67% | 15.17% | -3.34% | -0.644 | 0.569 | 0.828 | -6.01% |
| SOUTH_AFRICA | EZA | international_equity | -2.93% | 0.32% | 2.74% | 27.62% | -4.10% | -0.331 | 0.636 | 1.454 | -12.98% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.33% | -0.16% | 0.51% | 5.06% | -2.08% | 0.003 | 0.495 | 0.194 | -3.22% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -1.26% | -0.48% | -0.64% | 3.82% | -2.97% | 4.067 | 0.490 | 0.133 | -3.98% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.12% | 0.17% | 0.42% | 5.27% | -1.63% | 1.170 | 0.711 | 0.303 | -2.27% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -1.02% | 0.35% | -0.24% | 4.07% | -1.72% | 0.106 | 0.512 | 0.155 | -2.96% |
| SILVER | SLV | precious_metals | -3.88% | -1.70% | 1.59% | 41.11% | -8.40% | -0.282 | 0.484 | 1.657 | -45.55% |
| COPPER | CPER | non_energy_commodities | -2.28% | -0.28% | -1.01% | 25.52% | -4.90% | 1.530 | 0.518 | 1.020 | -4.90% |
| AGRICULTURE | DBA | non_energy_commodities | 1.63% | 1.13% | 6.79% | 11.72% | -2.17% | 0.237 | 0.025 | 0.026 | -0.58% |
| OIL | USO | energy | 11.57% | 13.16% | 11.31% | 37.87% | -6.31% | -0.047 | -0.425 | -1.798 | 0.00% |
| US_DOLLAR | UUP | currencies | -0.18% | 0.46% | 0.81% | 5.19% | -1.13% | -0.416 | -0.338 | -0.142 | -1.99% |
| EURO | FXE | currencies | -0.02% | 1.17% | 1.14% | 4.46% | -0.76% | -0.243 | 0.329 | 0.125 | -3.06% |
| YEN | FXY | currencies | 1.24% | 3.85% | 0.87% | 10.51% | -1.41% | 0.434 | 0.279 | 0.214 | -5.44% |
| BITCOIN_ETF | IBIT | crypto_assets | -3.43% | 0.71% | 22.54% | 45.90% | -5.76% | 0.131 | 0.364 | 1.104 | -38.73% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.22% | 3.78% | 27.99% | 56.47% | -4.35% | 0.226 | 0.337 | 1.379 | -48.14% |
