# Anti-Momentum-Chasing Controls

CapitalBench model portfolios have shown a strong tendency to chase recent winners. A local audit of official submissions with frozen trailing-return data found:

- 187 official submissions analyzed.
- Weekly portfolios averaged 61.8% weight in top-5 7-day return assets and 56.0% in top-5 30-day return assets.
- Monthly portfolios averaged 47.9% weight in top-5 7-day return assets and 54.9% in top-5 30-day return assets.
- 184 of 187 rationales mentioned momentum, recent returns, trailing performance, leadership, continuation, or similar language.
- Semiconductors were the largest recurring holding: 21.7% average weekly weight and 26.7% average monthly weight.

This is not automatically wrong. Momentum is a documented market anomaly, especially at intermediate horizons. But the current benchmark horizon is often one week or one month, where blind recent-winner extrapolation is fragile and can become a benchmark artifact rather than useful market reasoning.

## Research Basis

The controls follow several robust findings:

- Jegadeesh and Titman document momentum over 3- to 12-month holding periods, not simply "buy what led last week."
  Source: https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf
- Short-horizon return reversal is a distinct documented effect; prior-week or prior-month winners can reverse.
  Source: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr513.pdf
- Value and momentum diversify each other across asset classes, so a pure momentum read can ignore important valuation and regime context.
  Source: https://pages.stern.nyu.edu/~lpederse/papers/ValMomEverywhere.pdf
- Price momentum may be partly explained by fundamental or earnings momentum; continuation cases should not rely on price action alone.
  Source: https://www.nber.org/system/files/working_papers/w20984/w20984.pdf
- Momentum crashes are related to state variables such as bear-market and volatility conditions, so recent-winner allocations need reversal and drawdown context.
  Source: https://www.nber.org/system/files/working_papers/w20439/w20439.pdf

## Implemented Controls

Future generated model inputs now include:

- A prompt-level price-history discipline: trailing returns are descriptive data, not forecasts.
- A requirement that momentum-based rationales do not present price history alone as independent evidence.
- A requirement that models mention independent support present in the briefing, or state that support is limited, rather than inventing unsupported continuation reasons.
- Round metadata that repeats the evidence standard when a holding relies on recent price strength.
- A full-universe trailing-return appendix with:
  - 7-day, 30-day, 6-month, and 1-year returns in option order, not performance order.
  - 30-day return versus the S&P 500 benchmark.
  - 30-day annualized volatility.
  - 30-day max drawdown.
  - 30-day up-day share.
  - Distance from the 52-week high and low.
  - One-year beta and correlation to the S&P 500 benchmark.
  - A neutral price-history note explaining that trailing returns are not forecasts.
- A research-import failure when final briefings include a selected mechanical return section, because it duplicates the full appendix and makes a subset of assets too salient.

## Recommended Next Additions

The highest-value additions are split between automatically available price diagnostics and optional vendor-backed data.

### Tier 1: implement automatically from current sources

- Benchmark-relative diagnostics: return versus SPY over 7-day, 30-day, 6-month, and 1-year windows; one-year beta to SPY; one-year correlation to SPY.
- Path-quality diagnostics: 30-day up-day share, 30-day annualized volatility, 30-day max drawdown, and distance from 52-week high and low.
- Regime snapshot: Treasury-yield moves, real-yield moves, dollar move, oil move, gold move, VIX level/change, investment-grade spread move, high-yield spread move, and equal-weight versus cap-weight equity return.
- Breadth and concentration: share of universe positive over 7-day and 30-day windows, top-five-minus-median return spread, and SPY versus RSP return spread.
- Scheduled catalyst exposure: macro releases, Fed events, major earnings clusters, and market holidays inside the scoring window.

### Tier 2: add when a reliable vendor is available

- Valuation context by ETF or sector: P/E, forward P/E, earnings yield, dividend yield, and relative valuation versus recent history.
- Fundamental momentum context: earnings revisions, revenue/earnings surprise, margin trend, and sector-level analyst revision direction.
- Flow and crowding context: ETF flow concentration, AUM change, short interest, options-implied volatility, options skew, put-call ratios, and futures positioning.

### Tier 3: add only after validation

- Reference-class base rates: for each high-momentum asset group, show how similar past 7-day and 30-day setups performed over the next week and month once CapitalBench has enough history.
- Model-input factor summaries: value, quality, momentum, low-volatility, carry, and liquidity exposures, but only if they are consistently sourced for every option and do not become hidden recommendations.

The goal is not to remove momentum information. The goal is to force a continuation case to compete with reversal risk, valuation/fundamental support, and macro/regime evidence before a model allocates heavily to recent winners.
