# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-21
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.47% |
| spy_return_21s | 0.21% |
| rsp_return_5s | -0.32% |
| rsp_return_21s | 1.73% |
| hyg_return_5s | -0.04% |
| hyg_return_21s | 0.01% |
| tlt_return_5s | -0.50% |
| tlt_return_21s | -3.21% |
| uup_return_5s | 0.32% |
| uup_return_21s | 0.64% |
| uso_return_5s | 7.22% |
| uso_return_21s | 12.17% |
| iau_return_5s | 0.72% |
| iau_return_21s | -3.16% |
| rsp_minus_spy_5s | 0.15% |
| rsp_minus_spy_21s | 1.52% |
| positive_asset_share_5s | 34.78% |
| positive_asset_share_21s | 49.28% |
| active_return_dispersion_5s | 1.72% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.47% | -0.68% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | 0.53% | -0.45% | 0.23% | -0.01% | 0.026 | -0.227 | -0.004 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.33% | 0.00% | 0.00% | 11.75% | -2.38% | -0.486 | 1.000 | 1.000 | -1.23% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.30% | 0.01% | -0.08% | 10.86% | -1.82% | -0.720 | 0.993 | 0.990 | -1.03% |
| NASDAQ100 | QQQ | technology_and_growth | 0.43% | -1.02% | -3.40% | 24.86% | -6.01% | -0.434 | 0.919 | 1.721 | -4.88% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.11% | -1.07% | -0.65% | 22.06% | -4.13% | 0.823 | 0.887 | 1.285 | -5.69% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.81% | 0.91% | 1.05% | 10.46% | -1.06% | 0.096 | 0.709 | 0.644 | -0.81% |
| MID_CAP | IJH | diversified_us_equity | -0.36% | 0.67% | -0.96% | 12.01% | -3.09% | -0.818 | 0.774 | 0.867 | -1.80% |
| SMALL_CAP | IWM | diversified_us_equity | 0.32% | 1.16% | -1.05% | 11.65% | -2.71% | -0.748 | 0.788 | 1.113 | -1.30% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.57% | 1.98% | 0.58% | 10.02% | -1.83% | -0.797 | 0.675 | 0.800 | -0.57% |
| DIVIDEND | SCHD | diversified_us_equity | -0.67% | 2.40% | 1.19% | 12.56% | -1.18% | -0.102 | 0.096 | 0.088 | -0.67% |
| LOW_VOL | SPLV | diversified_us_equity | -1.39% | 0.42% | 3.37% | 14.88% | -1.89% | -0.795 | -0.289 | -0.298 | -1.39% |
| MOMENTUM | MTUM | diversified_us_equity | 3.65% | -1.18% | -6.22% | 42.96% | -12.49% | 1.575 | 0.769 | 2.148 | -8.90% |
| TECHNOLOGY | XLK | technology_and_growth | 1.84% | -1.07% | -4.65% | 32.91% | -8.62% | -0.839 | 0.844 | 2.165 | -8.68% |
| COMMUNICATIONS | XLC | technology_and_growth | -2.33% | -0.80% | 1.41% | 18.46% | -3.28% | -0.260 | 0.447 | 0.528 | -7.84% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.10% | -0.42% | -1.56% | 18.21% | -3.06% | -0.035 | 0.739 | 1.047 | -7.38% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.04% | 1.24% | 0.16% | 19.29% | -2.11% | -0.595 | -0.314 | -0.397 | -5.43% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.96% | 1.71% | 5.74% | 21.74% | -3.74% | -0.521 | -0.092 | -0.128 | -2.55% |
| FINANCIALS | XLF | financials | -1.13% | 0.35% | 4.56% | 13.56% | -2.08% | 0.151 | 0.179 | 0.180 | -1.13% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.83% | -0.52% | -0.69% | 17.23% | -4.01% | -0.800 | 0.646 | 0.959 | -3.72% |
| ENERGY | XLE | energy | 2.60% | 3.19% | 6.00% | 19.54% | -3.03% | -0.802 | -0.375 | -0.696 | -5.82% |
| MATERIALS | XLB | materials_and_mining | -1.55% | -0.59% | -2.57% | 17.10% | -3.81% | -0.577 | 0.548 | 0.804 | -5.80% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.21% | -1.21% | 2.05% | 14.77% | -3.10% | -0.684 | -0.048 | -0.064 | -4.62% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.57% | 2.09% | 1.62% | 16.38% | -2.67% | -0.876 | -0.089 | -0.112 | -0.57% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.44% | 0.22% | -1.21% | 4.72% | -1.54% | -0.637 | 0.529 | 0.203 | -3.22% |
| LONG_TREASURY | TLT | rates_and_duration | -0.65% | -0.03% | -3.40% | 8.83% | -3.98% | -0.686 | 0.402 | 0.272 | -6.15% |
| TIPS | TIP | rates_and_duration | -0.08% | 0.35% | -0.98% | 3.50% | -0.88% | -0.578 | 0.540 | 0.147 | -1.08% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.60% | 0.14% | -2.04% | 4.82% | -2.26% | 0.049 | 0.562 | 0.228 | -2.55% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.19% | 0.43% | -0.63% | 2.10% | -0.44% | -0.730 | 0.768 | 0.213 | -0.28% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.40% | 0.21% | -1.26% | 3.76% | -1.34% | -0.289 | 0.568 | 0.180 | -2.00% |
| DEVELOPED_EX_US | VEA | international_equity | 0.63% | 0.29% | -3.05% | 19.15% | -4.37% | -0.613 | 0.839 | 1.364 | -2.65% |
| EMERGING_MARKETS | VWO | international_equity | 0.03% | 0.10% | -3.46% | 19.90% | -5.55% | -0.436 | 0.872 | 1.385 | -3.89% |
| EUROPE | VGK | international_equity | -0.03% | 0.99% | -0.65% | 14.07% | -2.53% | -1.208 | 0.723 | 1.020 | -1.34% |
| JAPAN | EWJ | international_equity | 0.90% | -0.75% | -3.14% | 25.31% | -6.74% | -0.312 | 0.792 | 1.373 | -4.36% |
| CHINA | MCHI | international_equity | -0.26% | 1.92% | 0.19% | 20.78% | -4.50% | -0.019 | 0.517 | 0.846 | -17.86% |
| INDIA | INDA | international_equity | 0.18% | 0.57% | -2.40% | 12.65% | -2.74% | -0.683 | 0.588 | 0.692 | -11.77% |
| GOLD | IAU | precious_metals | 2.70% | 1.19% | -4.54% | 23.14% | -5.71% | -0.272 | 0.698 | 1.301 | -24.37% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 4.07% | 3.81% | 2.83% | 22.06% | -4.36% | 3.773 | -0.111 | -0.179 | -6.66% |
| SEMICONDUCTORS | SMH | technology_and_growth | 2.66% | -2.23% | -9.71% | 54.85% | -16.80% | 0.307 | 0.791 | 3.212 | -12.68% |
| SOFTWARE | IGV | technology_and_growth | -2.01% | -1.46% | 4.41% | 25.51% | -4.86% | -1.364 | 0.336 | 0.890 | -22.03% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.85% | -1.08% | -7.93% | 37.92% | -12.51% | -0.226 | 0.832 | 2.521 | -13.03% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.66% | -1.31% | -8.86% | 34.28% | -12.79% | -0.954 | 0.853 | 2.519 | -16.49% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.43% | -3.91% | 11.47% | 27.53% | -4.38% | -0.209 | 0.411 | 1.034 | -4.38% |
| SOLAR | TAN | clean_energy | -0.81% | -2.05% | -9.68% | 37.60% | -13.78% | -1.360 | 0.743 | 2.608 | -27.31% |
| METALS_MINING | XME | materials_and_mining | 2.64% | -2.23% | -11.39% | 32.87% | -16.42% | -0.746 | 0.710 | 2.232 | -23.46% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.07% | 0.15% | 1.37% | 9.80% | -1.30% | -0.634 | 0.713 | 0.592 | -1.07% |
| BIOTECH | XBI | healthcare_and_biotech | 1.64% | -0.14% | 9.89% | 30.21% | -8.12% | -0.287 | 0.366 | 0.861 | -5.95% |
| REGIONAL_BANKS | KRE | financials | -2.49% | 1.78% | 4.50% | 20.19% | -3.73% | 0.353 | 0.158 | 0.252 | -2.49% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.50% | -1.88% | -2.24% | 18.92% | -8.58% | -0.751 | 0.486 | 0.960 | -8.39% |
| CANADA | EWC | international_equity | -0.57% | 0.25% | 1.58% | 8.90% | -1.46% | -0.286 | 0.606 | 0.624 | -0.74% |
| UNITED_KINGDOM | EWU | international_equity | -0.43% | 1.47% | 1.19% | 13.52% | -1.93% | -0.728 | 0.497 | 0.658 | -2.55% |
| AUSTRALIA | EWA | international_equity | 0.17% | 0.37% | -0.16% | 12.77% | -3.01% | -0.309 | 0.609 | 0.864 | -3.89% |
| SOUTH_KOREA | EWY | international_equity | 5.84% | -1.83% | -19.94% | 76.67% | -25.85% | 0.652 | 0.758 | 4.556 | -21.12% |
| TAIWAN | EWT | international_equity | 0.42% | -0.80% | -8.06% | 43.55% | -13.98% | 0.929 | 0.796 | 2.593 | -9.82% |
| BRAZIL | EWZ | international_equity | 0.82% | -0.67% | 6.14% | 19.00% | -2.22% | -0.756 | 0.444 | 0.783 | -13.83% |
| MEXICO | EWW | international_equity | 0.82% | 1.14% | -3.26% | 18.02% | -4.58% | -0.825 | 0.634 | 1.000 | -5.26% |
| SOUTH_AFRICA | EZA | international_equity | -1.05% | -1.37% | -5.61% | 22.05% | -7.66% | -0.468 | 0.772 | 1.955 | -22.00% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.37% | 0.19% | -1.18% | 4.17% | -1.45% | -0.434 | 0.578 | 0.214 | -1.91% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.42% | -0.26% | -0.77% | 2.23% | -1.30% | -0.333 | 0.572 | 0.118 | -1.30% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.22% | 0.27% | -1.47% | 3.98% | -1.09% | -1.126 | 0.739 | 0.328 | -1.08% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.27% | 0.20% | -1.26% | 3.44% | -1.22% | -0.618 | 0.555 | 0.181 | -1.67% |
| SILVER | SLV | precious_metals | 5.34% | 0.30% | -11.34% | 45.72% | -15.33% | -0.727 | 0.663 | 2.609 | -49.73% |
| COPPER | CPER | non_energy_commodities | 3.86% | 3.04% | -1.51% | 25.86% | -6.56% | -0.688 | 0.717 | 1.624 | -2.64% |
| AGRICULTURE | DBA | non_energy_commodities | 2.03% | 2.35% | 3.07% | 14.69% | -1.52% | -0.748 | 0.004 | 0.004 | -2.02% |
| OIL | USO | energy | 8.01% | 7.70% | 3.93% | 48.75% | -10.10% | -0.538 | -0.304 | -1.202 | -15.76% |
| US_DOLLAR | UUP | currencies | 0.49% | 0.79% | -0.36% | 4.52% | -0.98% | -0.303 | -0.535 | -0.203 | -0.18% |
| EURO | FXE | currencies | -0.32% | 0.32% | -0.97% | 4.28% | -0.95% | -0.660 | 0.565 | 0.205 | -4.93% |
| YEN | FXY | currencies | -0.41% | -0.15% | -1.17% | 5.27% | -1.28% | -0.067 | 0.205 | 0.103 | -10.55% |
| BITCOIN_ETF | IBIT | crypto_assets | 3.52% | 3.45% | 2.01% | 36.70% | -8.79% | -0.389 | 0.483 | 1.429 | -47.16% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.83% | 2.94% | 9.41% | 50.25% | -10.11% | 0.290 | 0.581 | 2.373 | -60.29% |
