# VNext Historical Replay

Frozen on: `2026-07-20`

Status: private retrospective screening experiment. It is not an official
CapitalBench round, does not change production V2.1, and must not enter public
leaderboards, cumulative scores, insights, or market-environment calculations.

## Objective

Test whether one of three narrowly specified changes improves short-horizon
candidate discovery relative to a V2.1-style control when every comparison uses
the same model and historical market window.

The experiment is diagnostic. Current models may possess historical knowledge,
so retrospective success can reject weak treatments but cannot establish live
predictive skill.

## Models

Only these closed-capability models participate:

- `google-gemini-3-1-pro` (`gemini-3.5-flash` replay override; the available
  AuraDNA key has no Gemini Pro API quota)
- `xai-grok-4-3` (`grok-4.3`)
- `xai-grok-4-5` (`grok-4.5`)
- `openai-gpt-5-6-sol` (`gpt-5.6-sol`)

No Anthropic model and no GPT-5.5 call is allowed. Tools, search, browsing, and
external retrieval remain disabled. Temperature is zero where supported. Each
saved model-treatment-period response is one paid decision; only a transport
failure before a usable response may be retried.

## Historical Episodes

The episodes were selected chronologically without consulting their winners.
They do not overlap:

| Phase | Replay | Source round | Entry | Exit |
| --- | --- | --- | --- | --- |
| discovery | `D1` | `CB-2026-05-24-1W` | 2026-05-22 | 2026-05-29 |
| discovery | `D2` | `CB-2026-06-02-1W` | 2026-06-01 | 2026-06-08 |
| discovery | `D3` | `CB-2026-06-09-1W` | 2026-06-09 | 2026-06-16 |
| confirmation | `C1` | `CB-2026-06-17-1W` | 2026-06-17 | 2026-06-24 |
| confirmation | `C2` | `CB-2026-06-25-1W` | 2026-06-25 | 2026-07-02 |
| confirmation | `C3` | `CB-2026-07-06-1W` | 2026-07-06 | 2026-07-13 |

Monthly replays are excluded because the resolved monthly windows overlap too
heavily to provide a useful screening sample.

## Treatments

Every treatment receives the same frozen option universe and only facts that
were present in the source round before its decision deadline. The shared
response contract records a ten-option shortlist, a ranked five-option final
list, a separate S&P 500 forecast, and whether the model prefers SPY.

### H0: Control

The full frozen briefing and the common raw comparison table. The task directly
requests the shortlist and final ranking without a prescribed decision process.

### H1: Rank First

The H0 input plus a fixed process: screen the full universe, compare
continuation and reversal, check horizon timing, forecast SPY separately, then
reduce ten candidates to five. H1 changes instructions only.

### H2: Cross-Sectional Comparison

The H1 process plus a compact table containing raw 7-day, 30-day, 6-month, and
1-year returns and mechanically derived within-round ranks, SPY-relative
returns, recent-versus-medium rank shift, and trend-rank dispersion. These are
the only fields consistently reproducible from all six frozen source packets.
No learned score, recommendation, or outcome-derived feature is supplied.

### H3: Horizon-Focused Briefing

The H1 process and raw comparison table, but the briefing is deterministically
limited to current macro data, rates/volatility/currency/commodity data, market
facts, and scheduled events inside the scoring window. Setup identifiers,
historical outcome data, option mapping, and directional labels are excluded.

## Discovery Assignment

Each discovery model-period cell contains one H0 call and one challenger call.
Each model receives H1, H2, and H3 exactly once:

| Model | D1 | D2 | D3 |
| --- | --- | --- | --- |
| Gemini 3.5 Flash | H1 | H2 | H3 |
| Grok 4.3 | H2 | H3 | H1 |
| Grok 4.5 | H3 | H1 | H2 |
| GPT-5.6 SOL | H1 | H2 | H3 |

Discovery therefore costs at most 24 calls: 12 H0 and 12 challenger calls.

## Discovery Gate

For every response, calculate:

- whether the realized best non-SPY option appears in the final top five;
- equal-weight return of the final top five versus SPY;
- top-one return versus SPY;
- top-ten capture;
- realized percentile of the top-one prediction;
- regret of the best shortlisted option versus the realized best option;
- validity and uniqueness of the required option IDs.

A challenger is eligible for confirmation only when, across its four paired
discovery comparisons:

1. mean paired top-five alpha improvement over H0 is strictly positive;
2. winner capture count is strictly greater than H0;
3. at least three of four responses are valid.

If multiple challengers pass, select the largest mean paired top-five alpha
improvement. Ties within 0.01 percentage point prefer the simpler treatment in
the order H1, H2, H3. If none pass, stop after discovery.

## Confirmation

The selected challenger and H0 run for all four models on C1, C2, and C3. This
costs at most 24 additional calls. The challenger advances only if:

1. confirmation winner capture count exceeds H0;
2. mean paired top-five alpha improvement is positive;
3. the paired top-five improvement is positive for at least three models;
4. the paired top-five improvement is positive in at least two episodes;
5. at least ten of twelve challenger responses are valid.

Passing means eligible for a future live shadow test, not production adoption.

## Leakage And Audit Rules

1. Packet preparation may read only frozen prompt, briefing, options, and
   pre-decision market-context files.
2. Input packets and their SHA256 hashes must be written before scoring code
   loads realized returns.
3. The packet builder removes source round IDs and round setup rows. Source
   observation dates may remain when they are part of a frozen factual table.
4. Packet generation is deterministic and cannot contain manual option-level
   edits.
5. Raw and parsed provider responses, usage, errors, packet hashes, and
   validation results remain private under ignored `output/` storage.
6. No response may be revised after outcomes are joined.
7. No production or historical round artifact may be edited.
