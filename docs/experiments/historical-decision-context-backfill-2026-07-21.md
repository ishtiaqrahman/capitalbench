# Historical Decision-Context Backfill

## Question

Do the richer horizon-specific price features now used by Portfolio V2.0 contain
a stable cross-sectional ranking signal that was unavailable in the original
historical screen?

## Frozen Design

The experiment uses the same 46 resolved V1 rounds already admitted by the
predictability audit: 30 weekly and 16 monthly. It does not modify frozen round
artifacts. Daily adjusted prices and reported volume are fetched once per
symbol and sliced at each round's entry date, so no feature may use a later
observation.

Weekly features use five recent sessions, the preceding 16 sessions, 21-session
volatility and drawdown, 5-versus-60-session volume, and 63-session SPY beta.
Monthly features use 21 recent sessions, the preceding 105 sessions,
63-session volatility and drawdown, 20-versus-120-session volume, and
252-session SPY beta. Active returns are measured relative to SPY.

Five rules are frozen before price retrieval:

1. Horizon trend.
2. Risk-adjusted trend.
3. Quality pullback.
4. Volume-confirmed trend.
5. Low-beta active strength.

Each rule ranks the complete available universe and holds the top five options
at equal weight. SPY remains an eligible candidate. Ties receive equal
selection probability at the cutoff.

## Evaluation

The primary outcome is portfolio alpha versus SPY. Secondary diagnostics are
beat rate, top-three capture, shortlist regret, chronological discovery and
holdout alpha, a greedy non-overlapping-round subset, and leave-best-round-out
alpha.

Only a weekly rule may advance. It must have at least 90% feature coverage, at
least six non-overlapping rounds, positive non-overlapping alpha, a
non-overlapping beat rate above 50%, positive discovery and holdout alpha, and
positive leave-best-round-out alpha. Monthly results are diagnostic because
the completed windows provide too few independent observations.

Historical reuse can reject a weak rule but cannot establish prospective
skill. A pass authorizes only a private prospective shadow, not a production
change.

## Data Source Policy

Tiingo adjusted EOD history is preferred when a local credential is present.
The existing Yahoo chart adjusted-close endpoint is the permitted fallback.
The report must disclose the source, failures, and coverage. Model APIs are not
used.
