# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-10
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 2.03% |
| spy_return_21s | 2.39% |
| rsp_return_5s | 1.43% |
| rsp_return_21s | 2.76% |
| hyg_return_5s | 0.21% |
| hyg_return_21s | 0.20% |
| tlt_return_5s | -0.16% |
| tlt_return_21s | -2.46% |
| uup_return_5s | -0.11% |
| uup_return_21s | -0.88% |
| uso_return_5s | 3.11% |
| uso_return_21s | 15.84% |
| iau_return_5s | 8.30% |
| iau_return_21s | 6.80% |
| rsp_minus_spy_5s | -0.59% |
| rsp_minus_spy_21s | 0.37% |
| positive_asset_share_5s | 78.26% |
| positive_asset_share_21s | 68.12% |
| active_return_dispersion_5s | 3.20% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.03% | -0.36% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -1.96% | -0.15% | 0.17% | 0.00% | -0.220 | -0.133 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.42% | 0.00% | 0.00% | 14.02% | -3.38% | -0.461 | 1.000 | 1.000 | -0.03% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.52% | 0.06% | -0.05% | 14.03% | -3.29% | -0.044 | 0.993 | 0.990 | -0.04% |
| NASDAQ100 | QQQ | technology_and_growth | 0.50% | 0.94% | -3.87% | 25.59% | -8.79% | -0.581 | 0.923 | 1.714 | -3.28% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.23% | 0.70% | -2.85% | 24.18% | -7.99% | -0.932 | 0.910 | 1.374 | -3.49% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.85% | -0.43% | 2.64% | 9.19% | -1.31% | -0.542 | 0.720 | 0.583 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 0.70% | -0.15% | 0.22% | 13.03% | -1.71% | -0.581 | 0.798 | 0.824 | -0.32% |
| SMALL_CAP | IWM | diversified_us_equity | 0.07% | -0.76% | -0.28% | 15.37% | -2.69% | -1.182 | 0.788 | 1.030 | -0.57% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.35% | -2.10% | 1.68% | 12.44% | -1.61% | -0.574 | 0.660 | 0.696 | -1.18% |
| DIVIDEND | SCHD | diversified_us_equity | 1.63% | -0.15% | 3.22% | 13.16% | -1.42% | 0.569 | 0.086 | 0.073 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | -0.83% | -2.70% | 0.31% | 12.00% | -2.91% | -0.304 | -0.278 | -0.264 | -2.91% |
| MOMENTUM | MTUM | diversified_us_equity | -0.86% | -0.19% | -6.57% | 37.65% | -12.01% | -0.237 | 0.734 | 2.034 | -10.98% |
| TECHNOLOGY | XLK | technology_and_growth | 0.22% | 2.62% | -4.53% | 35.17% | -10.34% | -0.943 | 0.844 | 2.145 | -5.89% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.87% | -1.59% | -0.63% | 23.92% | -7.06% | -0.891 | 0.395 | 0.537 | -6.33% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.87% | -0.79% | 0.47% | 24.82% | -7.31% | -0.869 | 0.687 | 1.087 | -3.51% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.45% | -1.92% | 0.52% | 18.29% | -3.03% | -1.095 | -0.341 | -0.420 | -4.43% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.61% | 1.79% | 0.51% | 18.17% | -3.09% | 0.142 | -0.173 | -0.230 | 0.00% |
| FINANCIALS | XLF | financials | -0.33% | -1.28% | 2.64% | 10.91% | -1.62% | -0.969 | 0.277 | 0.269 | -0.33% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.94% | -1.24% | 0.32% | 17.41% | -3.57% | -0.771 | 0.679 | 0.915 | -0.97% |
| ENERGY | XLE | energy | 5.01% | 0.34% | 6.38% | 25.92% | -3.87% | -0.439 | -0.333 | -0.593 | -3.11% |
| MATERIALS | XLB | materials_and_mining | 1.03% | 2.23% | -0.12% | 18.88% | -3.65% | 0.270 | 0.473 | 0.689 | -0.01% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.21% | -4.80% | -2.67% | 13.49% | -6.83% | 0.948 | -0.063 | -0.073 | -8.42% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.77% | -3.75% | 1.28% | 13.94% | -3.50% | 0.117 | -0.168 | -0.192 | -3.50% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.59% | -2.09% | -0.89% | 4.59% | -1.05% | 3.492 | 0.500 | 0.180 | -3.46% |
| LONG_TREASURY | TLT | rates_and_duration | -1.13% | -2.19% | -2.67% | 9.27% | -2.69% | 2.357 | 0.405 | 0.272 | -7.58% |
| TIPS | TIP | rates_and_duration | -0.13% | -2.03% | -0.81% | 2.51% | -0.81% | -0.331 | 0.491 | 0.120 | -1.29% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.73% | -2.17% | -1.19% | 5.30% | -1.26% | -0.116 | 0.578 | 0.221 | -2.94% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.05% | -1.81% | -0.38% | 3.03% | -0.73% | -0.354 | 0.790 | 0.195 | -0.16% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.48% | -2.05% | -0.85% | 3.98% | -0.88% | 0.391 | 0.547 | 0.163 | -2.16% |
| DEVELOPED_EX_US | VEA | international_equity | 0.21% | 0.03% | -0.29% | 18.30% | -2.87% | -0.500 | 0.819 | 1.158 | -0.54% |
| EMERGING_MARKETS | VWO | international_equity | 0.53% | 0.12% | -1.75% | 17.92% | -4.96% | -0.696 | 0.855 | 1.243 | -1.49% |
| EUROPE | VGK | international_equity | 0.45% | -0.56% | 2.30% | 13.63% | -1.60% | -0.528 | 0.723 | 0.817 | -0.37% |
| JAPAN | EWJ | international_equity | 0.94% | 1.35% | -2.09% | 25.40% | -5.50% | -1.228 | 0.748 | 1.243 | -0.95% |
| CHINA | MCHI | international_equity | 1.64% | -0.18% | 4.85% | 16.42% | -2.22% | -0.562 | 0.408 | 0.594 | -13.41% |
| INDIA | INDA | international_equity | -0.34% | -2.07% | 1.38% | 12.76% | -3.39% | -0.587 | 0.555 | 0.613 | -9.31% |
| GOLD | IAU | precious_metals | 3.33% | 6.27% | -1.75% | 25.41% | -3.18% | 0.749 | 0.539 | 0.962 | -18.77% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 5.01% | 1.34% | 4.57% | 27.66% | -6.42% | 0.106 | -0.187 | -0.308 | -5.71% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.05% | 2.36% | -11.09% | 50.80% | -17.48% | -0.946 | 0.774 | 3.020 | -14.87% |
| SOFTWARE | IGV | technology_and_growth | 3.65% | 5.76% | 5.06% | 31.10% | -7.28% | -0.983 | 0.442 | 1.104 | -10.83% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.84% | 2.83% | -4.88% | 37.01% | -11.76% | -0.854 | 0.827 | 2.386 | -9.45% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 4.49% | 5.79% | -4.69% | 39.73% | -11.64% | -0.349 | 0.872 | 2.436 | -11.08% |
| CYBERSECURITY | CIBR | technology_and_growth | 3.11% | 5.10% | 1.85% | 27.67% | -7.40% | -0.081 | 0.536 | 1.246 | 0.00% |
| SOLAR | TAN | clean_energy | 1.15% | -0.82% | -7.13% | 45.89% | -14.55% | -0.132 | 0.754 | 2.539 | -29.85% |
| METALS_MINING | XME | materials_and_mining | 5.02% | 11.97% | -0.92% | 43.22% | -6.55% | 1.071 | 0.671 | 2.037 | -11.45% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.22% | -0.59% | 0.95% | 10.64% | -1.46% | -0.915 | 0.700 | 0.556 | -0.00% |
| BIOTECH | XBI | healthcare_and_biotech | 3.28% | 5.25% | -7.73% | 27.52% | -7.56% | -0.287 | 0.361 | 0.780 | -3.80% |
| REGIONAL_BANKS | KRE | financials | -1.69% | -3.36% | 2.36% | 16.68% | -3.55% | -0.904 | 0.193 | 0.272 | -2.43% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.46% | 0.02% | 2.58% | 24.22% | -4.10% | -0.459 | 0.486 | 0.874 | -0.46% |
| CANADA | EWC | international_equity | 1.18% | 1.07% | 1.34% | 10.91% | -1.46% | 0.021 | 0.591 | 0.512 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 0.25% | -1.49% | 3.14% | 11.83% | -1.23% | 0.768 | 0.417 | 0.441 | -0.39% |
| AUSTRALIA | EWA | international_equity | -0.30% | 0.18% | 2.98% | 17.51% | -1.61% | -0.031 | 0.613 | 0.753 | -1.18% |
| SOUTH_KOREA | EWY | international_equity | -3.56% | -0.23% | -13.05% | 78.00% | -21.42% | -0.638 | 0.701 | 4.078 | -25.58% |
| TAIWAN | EWT | international_equity | 0.47% | 2.26% | -8.09% | 44.70% | -15.80% | -0.949 | 0.794 | 2.540 | -8.38% |
| BRAZIL | EWZ | international_equity | -2.55% | -5.40% | 1.00% | 21.10% | -3.98% | -0.161 | 0.393 | 0.642 | -14.87% |
| MEXICO | EWW | international_equity | 0.31% | -1.53% | 1.90% | 16.84% | -2.23% | 1.153 | 0.605 | 0.842 | -3.90% |
| SOUTH_AFRICA | EZA | international_equity | 4.31% | 6.37% | 0.44% | 28.36% | -5.31% | -0.701 | 0.732 | 1.649 | -12.67% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.45% | -1.81% | -1.06% | 5.12% | -1.01% | -0.564 | 0.547 | 0.195 | -2.06% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.03% | -1.65% | -1.55% | 3.46% | -1.64% | 0.697 | 0.563 | 0.128 | -1.33% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.35% | -1.93% | -1.22% | 5.61% | -1.52% | -0.590 | 0.741 | 0.301 | -1.20% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.42% | -2.13% | -0.61% | 3.64% | -0.77% | -0.429 | 0.527 | 0.157 | -1.51% |
| SILVER | SLV | precious_metals | 5.96% | 11.22% | -3.12% | 39.51% | -6.60% | -0.227 | 0.574 | 2.037 | -43.74% |
| COPPER | CPER | non_energy_commodities | -1.64% | -0.67% | 3.98% | 22.39% | -3.26% | -0.089 | 0.629 | 1.273 | -1.64% |
| AGRICULTURE | DBA | non_energy_commodities | 0.69% | -1.92% | -0.29% | 13.78% | -2.87% | -0.523 | 0.131 | 0.131 | -3.17% |
| OIL | USO | energy | 9.61% | 1.08% | 11.99% | 70.38% | -17.64% | -0.462 | -0.341 | -1.343 | -17.68% |
| US_DOLLAR | UUP | currencies | 0.18% | -2.13% | -1.14% | 5.79% | -1.85% | 0.045 | -0.420 | -0.151 | -1.61% |
| EURO | FXE | currencies | -0.08% | -1.73% | 0.56% | 4.66% | -0.81% | -0.321 | 0.448 | 0.154 | -3.69% |
| YEN | FXY | currencies | -0.91% | -3.53% | 2.74% | 12.02% | -1.50% | 0.490 | 0.239 | 0.131 | -8.28% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.39% | -1.83% | -0.55% | 27.38% | -5.39% | -0.551 | 0.454 | 1.197 | -49.18% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.35% | -1.81% | 3.93% | 39.48% | -4.35% | -0.389 | 0.540 | 2.052 | -61.36% |
