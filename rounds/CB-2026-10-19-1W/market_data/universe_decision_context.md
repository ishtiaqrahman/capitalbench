# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-10-16
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.97% |
| spy_return_21s | 0.33% |
| rsp_return_5s | 0.49% |
| rsp_return_21s | 0.74% |
| hyg_return_5s | -0.48% |
| hyg_return_21s | -1.93% |
| tlt_return_5s | 2.65% |
| tlt_return_21s | -1.72% |
| uup_return_5s | -0.34% |
| uup_return_21s | 1.90% |
| uso_return_5s | 9.15% |
| uso_return_21s | 4.15% |
| iau_return_5s | -0.67% |
| iau_return_21s | -4.10% |
| rsp_minus_spy_5s | 2.46% |
| rsp_minus_spy_21s | 0.41% |
| positive_asset_share_5s | 49.28% |
| positive_asset_share_21s | 30.43% |
| active_return_dispersion_5s | 4.27% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.97% | -2.35% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 2.03% | -2.08% | 0.26% | -0.01% | -0.051 | 0.198 | 0.004 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.90% | 0.00% | 0.00% | 10.21% | -2.03% | -0.185 | 1.000 | 1.000 | -2.03% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.90% | -0.09% | -0.33% | 10.50% | -2.21% | -0.466 | 0.996 | 1.013 | -2.42% |
| NASDAQ100 | QQQ | technology_and_growth | -4.54% | -3.55% | 2.55% | 18.25% | -6.56% | 0.930 | 0.910 | 1.541 | -6.56% |
| LARGE_GROWTH | IWF | technology_and_growth | -4.44% | -3.06% | 2.04% | 17.25% | -5.97% | 1.982 | 0.937 | 1.506 | -5.97% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.49% | 2.85% | -2.06% | 7.44% | -2.18% | 0.192 | 0.736 | 0.571 | -1.03% |
| MID_CAP | IJH | diversified_us_equity | -1.24% | 0.50% | -2.05% | 11.97% | -2.34% | 0.060 | 0.787 | 0.869 | -7.75% |
| SMALL_CAP | IWM | diversified_us_equity | -2.26% | -1.08% | -4.62% | 14.31% | -5.84% | 1.492 | 0.792 | 1.011 | -11.13% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.06% | 0.96% | -5.05% | 11.96% | -4.16% | 0.497 | 0.703 | 0.706 | -7.84% |
| DIVIDEND | SCHD | diversified_us_equity | 2.94% | 5.93% | -4.08% | 10.71% | -3.25% | 0.257 | 0.161 | 0.157 | -1.66% |
| LOW_VOL | SPLV | diversified_us_equity | 2.06% | 5.21% | -3.41% | 9.72% | -3.30% | 0.005 | 0.032 | 0.026 | -4.11% |
| MOMENTUM | MTUM | diversified_us_equity | -6.37% | -6.42% | 2.19% | 19.63% | -9.64% | -0.211 | 0.643 | 1.532 | -14.91% |
| TECHNOLOGY | XLK | technology_and_growth | -6.53% | -5.73% | 3.48% | 21.80% | -9.17% | 1.411 | 0.800 | 1.869 | -9.17% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.75% | 1.91% | -3.78% | 21.93% | -4.19% | 0.714 | 0.396 | 0.745 | -7.29% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.09% | 1.62% | -0.81% | 13.62% | -3.13% | 0.691 | 0.652 | 1.110 | -9.12% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 4.07% | 6.99% | -1.76% | 15.11% | -3.15% | 1.808 | -0.079 | -0.107 | -0.78% |
| HEALTHCARE | XLV | healthcare_and_biotech | 4.16% | 5.42% | -0.78% | 16.26% | -2.97% | 0.367 | 0.029 | 0.045 | -0.27% |
| FINANCIALS | XLF | financials | 1.28% | 3.41% | -4.06% | 12.69% | -4.47% | 0.669 | 0.516 | 0.573 | -4.86% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.54% | 1.09% | -1.94% | 12.89% | -2.65% | 0.516 | 0.596 | 0.801 | -9.81% |
| ENERGY | XLE | energy | 1.55% | 6.82% | -0.82% | 21.33% | -4.05% | -0.263 | -0.303 | -0.589 | 0.00% |
| MATERIALS | XLB | materials_and_mining | 2.41% | 4.98% | -4.42% | 14.78% | -3.94% | -0.465 | 0.349 | 0.515 | -4.69% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.81% | 3.90% | -2.29% | 16.61% | -5.16% | 0.392 | 0.127 | 0.173 | -9.72% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.79% | 3.29% | -4.63% | 14.21% | -4.74% | 1.439 | 0.290 | 0.333 | -7.60% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.98% | 3.11% | -4.04% | 6.37% | -2.22% | 0.260 | 0.436 | 0.209 | -5.24% |
| LONG_TREASURY | TLT | rates_and_duration | 2.14% | 4.62% | -6.61% | 11.31% | -5.35% | 0.437 | 0.387 | 0.363 | -9.13% |
| TIPS | TIP | rates_and_duration | 0.94% | 3.04% | -3.57% | 4.88% | -1.64% | -0.486 | 0.217 | 0.077 | -2.51% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.83% | 2.93% | -4.54% | 6.83% | -2.83% | -0.222 | 0.513 | 0.278 | -4.48% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.30% | 1.49% | -3.80% | 4.29% | -1.99% | 0.759 | 0.718 | 0.227 | -2.87% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.71% | 2.80% | -3.81% | 5.22% | -1.94% | 0.639 | 0.466 | 0.189 | -3.36% |
| DEVELOPED_EX_US | VEA | international_equity | -0.81% | 0.75% | -4.60% | 13.33% | -4.69% | -0.376 | 0.766 | 1.004 | -5.59% |
| EMERGING_MARKETS | VWO | international_equity | -2.76% | -0.93% | -2.41% | 15.53% | -5.09% | 0.638 | 0.806 | 1.038 | -5.37% |
| EUROPE | VGK | international_equity | 1.14% | 3.43% | -5.85% | 13.78% | -4.47% | 0.815 | 0.676 | 0.746 | -6.10% |
| JAPAN | EWJ | international_equity | -2.51% | -1.08% | -2.40% | 16.72% | -4.47% | -0.228 | 0.696 | 1.203 | -4.47% |
| CHINA | MCHI | international_equity | -1.80% | -0.60% | -2.58% | 18.16% | -5.62% | -0.210 | 0.353 | 0.483 | -20.46% |
| INDIA | INDA | international_equity | 0.89% | 5.51% | -6.47% | 15.56% | -6.06% | 1.422 | 0.576 | 0.715 | -13.80% |
| GOLD | IAU | precious_metals | 0.12% | 1.30% | -5.80% | 20.83% | -6.29% | -0.220 | 0.373 | 0.807 | -22.87% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.65% | 4.26% | -2.60% | 15.73% | -3.59% | -0.432 | -0.468 | -0.860 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | -8.22% | -8.56% | 5.27% | 31.41% | -14.85% | 0.648 | 0.676 | 2.298 | -19.30% |
| SOFTWARE | IGV | technology_and_growth | -5.98% | -5.43% | 4.17% | 28.93% | -7.39% | -0.363 | 0.545 | 1.712 | -10.86% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -5.82% | -4.91% | 1.12% | 23.58% | -7.50% | 0.217 | 0.858 | 2.012 | -11.58% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -6.55% | -7.16% | -1.54% | 25.83% | -11.76% | -0.165 | 0.844 | 2.257 | -21.96% |
| CYBERSECURITY | CIBR | technology_and_growth | -8.05% | -8.20% | 5.86% | 31.99% | -10.16% | 2.303 | 0.502 | 1.561 | -10.16% |
| SOLAR | TAN | clean_energy | -5.70% | -2.38% | -7.98% | 31.33% | -10.40% | 0.903 | 0.696 | 2.133 | -43.39% |
| METALS_MINING | XME | materials_and_mining | -2.74% | -3.14% | -6.75% | 28.29% | -10.79% | -0.109 | 0.598 | 1.943 | -23.92% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.37% | 2.46% | -2.10% | 9.52% | -2.25% | 0.644 | 0.684 | 0.618 | -3.54% |
| BIOTECH | XBI | healthcare_and_biotech | -1.69% | -4.18% | -5.18% | 31.36% | -10.84% | 0.464 | 0.381 | 1.029 | -14.88% |
| REGIONAL_BANKS | KRE | financials | 1.09% | 3.13% | -6.94% | 15.37% | -5.25% | 0.355 | 0.359 | 0.472 | -9.91% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 2.49% | 3.14% | -5.73% | 15.37% | -5.80% | 0.551 | 0.392 | 0.706 | -17.34% |
| CANADA | EWC | international_equity | 1.12% | 4.59% | -4.63% | 15.40% | -4.64% | -0.029 | 0.600 | 0.714 | -3.29% |
| UNITED_KINGDOM | EWU | international_equity | 2.54% | 5.17% | -5.33% | 13.12% | -4.30% | -0.515 | 0.424 | 0.432 | -2.79% |
| AUSTRALIA | EWA | international_equity | -0.14% | 2.35% | -4.10% | 14.81% | -3.91% | 0.369 | 0.662 | 0.971 | -5.59% |
| SOUTH_KOREA | EWY | international_equity | -9.68% | -13.15% | -5.17% | 41.32% | -21.90% | 0.553 | 0.577 | 2.915 | -31.37% |
| TAIWAN | EWT | international_equity | -6.35% | -5.07% | 0.97% | 26.97% | -9.95% | 0.419 | 0.723 | 2.074 | -9.95% |
| BRAZIL | EWZ | international_equity | -2.43% | -1.96% | 13.02% | 49.34% | -5.36% | 0.713 | 0.271 | 0.828 | -3.93% |
| MEXICO | EWW | international_equity | 2.32% | 6.12% | -5.50% | 19.79% | -6.30% | -0.188 | 0.528 | 0.844 | -6.39% |
| SOUTH_AFRICA | EZA | international_equity | 1.49% | 4.29% | -9.47% | 25.66% | -9.92% | -0.242 | 0.540 | 1.349 | -18.25% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.61% | 2.78% | -4.15% | 7.13% | -2.56% | 0.332 | 0.462 | 0.240 | -3.85% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.57% | 3.22% | -4.09% | 7.02% | -2.79% | 1.273 | 0.376 | 0.175 | -4.07% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.28% | 2.35% | -4.53% | 7.09% | -3.41% | 0.143 | 0.663 | 0.358 | -3.77% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.26% | 2.29% | -2.38% | 3.45% | -0.89% | 1.618 | 0.576 | 0.190 | -2.38% |
| SILVER | SLV | precious_metals | -3.70% | -4.00% | -9.45% | 39.20% | -17.31% | 0.739 | 0.492 | 1.750 | -51.22% |
| COPPER | CPER | non_energy_commodities | -2.35% | -0.04% | -0.71% | 18.95% | -4.78% | -0.094 | 0.491 | 1.016 | -4.66% |
| AGRICULTURE | DBA | non_energy_commodities | -0.70% | 1.61% | -2.66% | 11.74% | -2.15% | -0.903 | 0.143 | 0.161 | -4.27% |
| OIL | USO | energy | 5.66% | 11.12% | -6.93% | 38.53% | -7.70% | -0.794 | -0.549 | -2.417 | -0.06% |
| US_DOLLAR | UUP | currencies | -0.34% | 1.62% | -0.09% | 5.19% | -0.72% | 0.162 | -0.253 | -0.121 | -0.72% |
| EURO | FXE | currencies | 0.36% | 2.34% | -4.66% | 5.23% | -2.76% | 0.927 | 0.215 | 0.094 | -6.04% |
| YEN | FXY | currencies | 0.19% | 2.14% | -3.81% | 5.58% | -1.84% | -0.777 | 0.356 | 0.317 | -5.15% |
| BITCOIN_ETF | IBIT | crypto_assets | -2.08% | 1.11% | 5.16% | 36.62% | -5.84% | -0.507 | 0.364 | 1.216 | -29.30% |
| ETHEREUM_ETF | ETHA | crypto_assets | -3.83% | -0.68% | -1.30% | 44.01% | -12.85% | -0.476 | 0.283 | 1.190 | -42.77% |
