# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-11
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.15% |
| spy_return_21s | -1.06% |
| rsp_return_5s | -2.35% |
| rsp_return_21s | -2.81% |
| hyg_return_5s | -0.77% |
| hyg_return_21s | -0.73% |
| tlt_return_5s | -1.46% |
| tlt_return_21s | -1.13% |
| uup_return_5s | 0.21% |
| uup_return_21s | -0.46% |
| uso_return_5s | 9.02% |
| uso_return_21s | 21.68% |
| iau_return_5s | -2.84% |
| iau_return_21s | -1.53% |
| rsp_minus_spy_5s | -1.21% |
| rsp_minus_spy_21s | -1.75% |
| positive_asset_share_5s | 20.29% |
| positive_asset_share_21s | 23.19% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.06% | -16.60% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.09% | 1.36% | -15.09% | 0.20% | -0.01% | -0.517 | -0.091 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.15% | 0.00% | 0.00% | 12.21% | -3.38% | -1.016 | 1.000 | 1.000 | -1.75% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.21% | -0.38% | 0.55% | 12.04% | -3.29% | -0.644 | 0.995 | 1.012 | -2.08% |
| NASDAQ100 | QQQ | technology_and_growth | -0.39% | -0.16% | 4.86% | 22.44% | -10.96% | -1.047 | 0.929 | 1.419 | -4.09% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.94% | -0.67% | -4.13% | 19.87% | -8.29% | -0.725 | 0.934 | 1.286 | -4.97% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.47% | 0.21% | 4.31% | 9.98% | -2.33% | -0.546 | 0.802 | 0.703 | -1.47% |
| MID_CAP | IJH | diversified_us_equity | -1.73% | -3.58% | 0.47% | 12.40% | -6.11% | -0.678 | 0.812 | 0.979 | -5.38% |
| SMALL_CAP | IWM | diversified_us_equity | -2.13% | -3.50% | 6.26% | 13.79% | -5.70% | -0.971 | 0.820 | 1.202 | -5.31% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.80% | -1.70% | 4.85% | 11.14% | -3.72% | -0.915 | 0.738 | 0.942 | -3.40% |
| DIVIDEND | SCHD | diversified_us_equity | -2.74% | 0.65% | -3.61% | 11.93% | -3.46% | 0.207 | 0.291 | 0.252 | -3.10% |
| LOW_VOL | SPLV | diversified_us_equity | -1.93% | -1.43% | -13.96% | 11.76% | -5.34% | -0.683 | 0.025 | 0.021 | -5.18% |
| MOMENTUM | MTUM | diversified_us_equity | 2.54% | -1.38% | 12.70% | 34.38% | -17.99% | -0.459 | 0.762 | 1.557 | -11.06% |
| TECHNOLOGY | XLK | technology_and_growth | 0.91% | 0.43% | 20.75% | 30.59% | -13.31% | -1.279 | 0.851 | 1.740 | -5.21% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.69% | 3.17% | -20.38% | 19.83% | -7.06% | -1.029 | 0.569 | 0.675 | -5.68% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -3.01% | -3.12% | -10.46% | 20.75% | -8.09% | -1.066 | 0.769 | 1.165 | -8.92% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.21% | -0.94% | -14.34% | 16.73% | -5.03% | -0.741 | -0.056 | -0.063 | -6.20% |
| HEALTHCARE | XLV | healthcare_and_biotech | -4.56% | -0.77% | -3.47% | 19.26% | -5.87% | -0.934 | 0.230 | 0.290 | -5.87% |
| FINANCIALS | XLF | financials | -2.24% | -0.10% | 3.04% | 13.00% | -2.89% | -0.703 | 0.542 | 0.617 | -2.24% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.25% | -6.21% | -3.52% | 16.44% | -8.56% | -0.668 | 0.713 | 0.956 | -7.58% |
| ENERGY | XLE | energy | 0.80% | 7.80% | -9.03% | 21.54% | -7.58% | -0.762 | -0.184 | -0.309 | -0.26% |
| MATERIALS | XLB | materials_and_mining | -3.17% | -2.04% | -9.90% | 17.58% | -5.42% | -0.452 | 0.537 | 0.748 | -5.07% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.49% | -2.25% | -21.06% | 14.45% | -8.77% | -0.360 | 0.117 | 0.138 | -10.00% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.88% | -1.34% | -9.40% | 14.74% | -6.43% | -0.444 | 0.252 | 0.276 | -5.63% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.38% | -0.68% | -17.81% | 4.77% | -3.27% | -0.337 | 0.287 | 0.103 | -4.94% |
| LONG_TREASURY | TLT | rates_and_duration | -1.46% | -0.07% | -20.34% | 9.45% | -6.55% | 0.030 | 0.242 | 0.172 | -8.56% |
| TIPS | TIP | rates_and_duration | -1.08% | 0.05% | -16.92% | 3.61% | -2.04% | -0.341 | 0.252 | 0.065 | -2.23% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.12% | -0.22% | -16.92% | 5.20% | -3.75% | -0.487 | 0.476 | 0.195 | -4.04% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.77% | 0.34% | -13.77% | 2.78% | -1.11% | -0.531 | 0.774 | 0.229 | -1.11% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -1.00% | -0.08% | -16.80% | 3.96% | -2.41% | -0.376 | 0.397 | 0.116 | -3.09% |
| DEVELOPED_EX_US | VEA | international_equity | -1.02% | 0.23% | -2.28% | 15.95% | -4.75% | -0.718 | 0.803 | 1.088 | -1.49% |
| EMERGING_MARKETS | VWO | international_equity | -1.05% | 0.96% | -5.24% | 16.40% | -7.05% | -0.847 | 0.815 | 1.115 | -1.77% |
| EUROPE | VGK | international_equity | -1.87% | -1.36% | -3.81% | 11.94% | -4.05% | -0.860 | 0.749 | 0.917 | -3.40% |
| JAPAN | EWJ | international_equity | 0.67% | 1.85% | 0.18% | 21.88% | -7.86% | -0.778 | 0.728 | 1.190 | 0.00% |
| CHINA | MCHI | international_equity | -2.59% | -2.79% | -20.48% | 16.93% | -8.10% | -0.881 | 0.564 | 0.872 | -19.44% |
| INDIA | INDA | international_equity | -2.70% | -1.70% | -13.65% | 13.10% | -4.79% | -0.927 | 0.561 | 0.664 | -12.15% |
| GOLD | IAU | precious_metals | -2.84% | -0.47% | -29.84% | 24.90% | -8.22% | -0.374 | 0.331 | 0.748 | -19.55% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.67% | 11.19% | -12.18% | 22.14% | -8.47% | -0.502 | -0.188 | -0.299 | -1.30% |
| SEMICONDUCTORS | SMH | technology_and_growth | 2.88% | -1.73% | 34.08% | 47.01% | -24.62% | -0.841 | 0.772 | 2.369 | -15.01% |
| SOFTWARE | IGV | technology_and_growth | -5.08% | -0.45% | 4.71% | 33.06% | -8.55% | -1.133 | 0.509 | 1.243 | -13.80% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -0.50% | 1.39% | 14.65% | 32.69% | -16.56% | -0.836 | 0.849 | 1.923 | -8.78% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.18% | -4.81% | -8.08% | 32.60% | -18.66% | -1.232 | 0.804 | 2.199 | -15.62% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.97% | -4.91% | 37.54% | 31.01% | -9.53% | -0.126 | 0.525 | 1.154 | -7.63% |
| SOLAR | TAN | clean_energy | -1.19% | -8.84% | -21.02% | 36.36% | -25.65% | -0.700 | 0.638 | 1.889 | -36.22% |
| METALS_MINING | XME | materials_and_mining | -4.01% | -1.64% | -12.93% | 36.20% | -19.05% | -0.468 | 0.596 | 1.778 | -14.40% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -2.35% | -1.75% | -1.43% | 10.62% | -4.31% | -1.067 | 0.775 | 0.707 | -3.55% |
| BIOTECH | XBI | healthcare_and_biotech | -4.98% | -0.94% | 13.51% | 29.09% | -10.51% | -0.300 | 0.484 | 1.053 | -7.87% |
| REGIONAL_BANKS | KRE | financials | -1.30% | -3.44% | 6.74% | 17.33% | -6.81% | -0.606 | 0.415 | 0.716 | -5.17% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.08% | -11.90% | -7.76% | 21.54% | -13.78% | -0.363 | 0.572 | 1.034 | -13.51% |
| CANADA | EWC | international_equity | -3.03% | -0.86% | -5.48% | 11.42% | -3.75% | -0.227 | 0.678 | 0.766 | -3.29% |
| UNITED_KINGDOM | EWU | international_equity | -1.52% | 0.17% | -9.65% | 11.77% | -3.77% | -0.663 | 0.604 | 0.704 | -2.94% |
| AUSTRALIA | EWA | international_equity | -3.62% | -1.01% | -9.94% | 15.21% | -4.44% | -0.296 | 0.676 | 0.938 | -3.81% |
| SOUTH_KOREA | EWY | international_equity | 4.52% | 8.37% | 25.81% | 67.43% | -34.21% | -0.821 | 0.633 | 2.768 | -13.91% |
| TAIWAN | EWT | international_equity | 0.71% | 5.52% | 35.61% | 37.49% | -19.83% | -1.146 | 0.752 | 1.832 | -1.13% |
| BRAZIL | EWZ | international_equity | 0.16% | 13.85% | -21.96% | 21.75% | -8.05% | -0.170 | 0.478 | 0.939 | -7.61% |
| MEXICO | EWW | international_equity | -2.07% | -0.35% | -9.10% | 16.46% | -5.37% | -0.652 | 0.551 | 0.943 | -5.84% |
| SOUTH_AFRICA | EZA | international_equity | -2.39% | 3.65% | -15.50% | 27.08% | -11.18% | -0.577 | 0.633 | 1.626 | -12.27% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.38% | -0.52% | -16.62% | 4.71% | -2.72% | 0.298 | 0.392 | 0.135 | -3.33% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.80% | -1.32% | -16.20% | 3.50% | -3.98% | 2.503 | 0.394 | 0.093 | -3.56% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.18% | -0.19% | -14.28% | 4.95% | -2.34% | -0.421 | 0.687 | 0.304 | -2.34% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.86% | -0.42% | -15.96% | 3.60% | -2.49% | -0.292 | 0.468 | 0.133 | -2.91% |
| SILVER | SLV | precious_metals | -4.01% | -0.53% | -39.37% | 41.58% | -20.61% | -0.609 | 0.367 | 1.786 | -44.96% |
| COPPER | CPER | non_energy_commodities | -1.83% | -1.04% | -4.09% | 23.86% | -8.42% | -0.251 | 0.556 | 1.248 | -4.56% |
| AGRICULTURE | DBA | non_energy_commodities | -0.55% | 4.98% | -12.52% | 13.48% | -2.87% | 0.293 | 0.049 | 0.042 | -1.90% |
| OIL | USO | energy | 9.02% | 22.74% | -9.07% | 52.54% | -19.84% | -0.612 | -0.349 | -1.325 | -2.20% |
| US_DOLLAR | UUP | currencies | 0.21% | 0.60% | -14.72% | 5.23% | -2.52% | -1.104 | -0.296 | -0.129 | -1.85% |
| EURO | FXE | currencies | -0.25% | 1.77% | -16.18% | 4.73% | -2.19% | -0.620 | 0.276 | 0.118 | -3.17% |
| YEN | FXY | currencies | 1.38% | 4.82% | -16.79% | 9.63% | -2.49% | 0.337 | 0.178 | 0.118 | -5.00% |
| BITCOIN_ETF | IBIT | crypto_assets | -5.57% | 23.02% | -26.76% | 37.78% | -11.79% | 0.824 | 0.489 | 1.718 | -38.60% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.74% | 36.37% | -26.00% | 51.27% | -14.68% | 1.591 | 0.505 | 2.547 | -46.47% |
