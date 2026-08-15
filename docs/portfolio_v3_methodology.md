# Portfolio V3.0 Methodology

Status: **production default for newly initialized portfolio rounds from August 15, 2026**

Portfolio V3.0 separates model judgment from portfolio construction. Each model
ranks and classifies a balanced set of candidates in one frozen, tool-free
response. CapitalBench then applies one fixed allocation rule. Existing V1,
V2.0, and V2.2 rounds remain frozen under their original manifests.

## Why V3 Replaced V2.2

V2.2 asked each model to search the full universe, forecast candidates, and
construct its own portfolio. Saved results showed that candidate selection and
recent-winner extrapolation were recurring weaknesses.

V3 development and holdout work tested a smaller intervention:

- a deterministic, balanced candidate slate;
- explicit continuation-versus-reversal judgments;
- a 55% probability hurdle for reversal candidates; and
- automatic SPY allocation when active evidence is insufficient.

The eleven-cell development diagnostic averaged **+1.04% alpha versus SPY**.
The subsequent holdout produced eight valid cells averaging **+1.94% alpha
versus SPY** and **+2.45 percentage points versus exact paired V2.2 controls**.
All eight valid cells were nonnegative, and all represented model families and
periods were positive.

The frozen holdout gate nevertheless failed because it required 10 valid cells
and only eight responses were valid. On August 15, 2026, the operator explicitly
adopted V3 despite that validity shortfall. This is an operator methodology
decision supported by promising return evidence; it must not be described as a
passed research gate or definitive proof of future outperformance.

## Model Input

Every participating model receives the same frozen information:

1. round metadata and the research cutoff;
2. the complete option-level quality evidence table;
3. a deterministic candidate slate;
4. the frozen factual briefing;
5. the complete horizon-specific decision context; and
6. the complete allowed universe for at most two optional wildcards.

The deterministic slate is formed before any model call from five fixed lanes:

| Lane | Count | Entry-time rule |
| --- | ---: | --- |
| Shock reversal | 5 | Lowest recent horizon active return |
| Medium strength | 3 | Highest preceding-window active return |
| Short continuation | 2 | Highest recent horizon active return |
| Quality pullback | 3 | Highest fixed quality-evidence score |
| Volume dislocation | 2 | Largest absolute horizon-profile volume z-score |

Duplicates are removed in lane order and SPY is added. The model must assess
every slate candidate and may add no more than two evidence-backed wildcards.
Slate inclusion and row order are search aids, not recommendations.

Weekly rounds use five-session active return, prior 16-session active return,
21-session risk, and five-versus-60-session volume. Monthly rounds use
21-session active return, prior 105-session active return, 63-session risk, and
20-versus-120-session volume. The lane counts and allocation rule do not change.

## Required Model Judgment

In one response, each model must:

- rank every assessed candidate without ties;
- estimate its probability of beating SPY and finishing in the top three;
- provide p10, p50, and p90 excess-return estimates relative to SPY;
- label the recent move as `overreaction`, `fundamental_deterioration`,
  `supported_continuation`, or `no_edge`;
- identify a likely mechanism and concise frozen-input evidence; and
- state market context, portfolio rationale, and key risks.

The model does **not** submit allocations.

## Deterministic Portfolio Rule

CapitalBench constructs the scored portfolio after validating the model
judgment:

1. Preserve the model's original rank order.
2. A non-SPY candidate is eligible only if it is labeled `overreaction` and
   has at least a 55% model-estimated probability of beating SPY.
3. Select at most the first three eligible candidates.
4. Fill fixed slots of 35%, 35%, and 30% in rank order.
5. Put every unused slot in SPY.

Examples:

- three eligible candidates: 35% / 35% / 30% active;
- two eligible candidates: 35% / 35% active and 30% SPY;
- one eligible candidate: 35% active and 65% SPY; and
- no eligible candidates: 100% SPY.

The production implementation is
`capitalbench.portfolio_v3.build_portfolio_v3_allocation`. The raw provider
response is preserved. The parsed submission stores the complete model
assessment and deterministic construction audit in `metadata.portfolio_v3`.

## Execution Contract

- One scored call per model.
- No participant tools, browsing, retrieval, agent loop, or follow-up.
- No best-of-many selection or outcome-based retry.
- Technical failures remain preserved and disclosed.
- Prompt 1, Prompt 2, and Prompt 3 prepare the frozen research artifacts; they
  do not replace the participant model call.
- Mechanical price APIs remain allowed for cutoff-safe market data and later
  scoring.

## Evidence Boundary

V3 is now the forward production default, not a retroactive rewrite. Do not:

- relabel the failed holdout validity gate as passed;
- tune the rule on the July 21, July 22, July 28, July 29, August 4, or August 5
  research windows;
- add confident continuation to the eligible set without a separately frozen
  experiment; or
- convert an existing V2.2 round to V3 after initialization.

Evaluate V3 prospectively as new weekly and monthly rounds resolve. Future
changes require a new methodology version and a new forward-only record.
