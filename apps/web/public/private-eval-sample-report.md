# CapitalBench Private Eval Sprint - Sample Report

Sample based on public round: CB-2026-05-28-1W

Underlying public audit packet: https://www.capitalbench.org/rounds/CB-2026-05-28-1W/

This sample uses an existing public CapitalBench round and presents it in the structure used for a private evaluation report. It is not a private-client result, endorsement, investment advice, or evidence of persistent investment skill.

## 1. Cover And Evaluation Identity

- Evaluation format: Private CapitalBench Eval Sprint sample
- Evidence source: Public CapitalBench May 28 2026 one-week portfolio round
- Track: Weekly
- Entry date: 2026-05-28
- Exit date: 2026-06-04
- Methodology version: portfolio-v1.0
- Universe version: v2.0
- Official run ID: official-20260528-1W
- Benchmark option: S&P 500
- Systems in public comparison: 5

## 2. Executive Recommendation

In a private client report, this section states whether the tested configuration is ready to ship, should be revised, should be compared with another system, or needs more evidence.

For this public sample, no client recommendation is issued. The round demonstrates the report structure: frozen inputs, official allocations, market-window scoring, comparator ranking, audit hashes, and explicit limitations.

## 3. System And Version Tested

Private reports identify the exact client system, version, endpoint, prompt configuration, tool setting, and execution mode.

This public sample uses public comparator systems only. No client system was evaluated.

## 4. Evaluation Methodology

Every system receives the same approved market packet, asset universe, portfolio constraints, and response schema. One official response determines the live outcome score. Repeated runs, when included in a private sprint, are reported separately as consistency evidence and are not used to replace the official response.

## 5. Comparator Roster

The public round included five model submissions. A standard private sprint compares one client system against up to four frontier comparators selected and frozen in the Evaluation Plan.

## 6. Official Scorecard

| Rank | Public model ID | Portfolio return | Portfolio minus S&P 500 | CapitalBench Score | Regret versus maximum |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | google-gemini-3-1-pro | 3.9317% | 3.6017 pp | 85.1383 | 0.6863 pp |
| 2 | anthropic-claude-opus-4-8 | 3.5764% | 3.2464 pp | 77.4446 | 1.0416 pp |
| 3 | anthropic-claude-opus-4-7 | 2.9112% | 2.5812 pp | 63.0408 | 1.7068 pp |
| 4 | xai-grok-4-3 | 2.6065% | 2.2765 pp | 56.4430 | 2.0115 pp |
| 5 | openai-gpt-5-5 | 2.4714% | 2.1414 pp | 53.5171 | 2.1466 pp |

## 7. Performance Attribution

In a private report, this section decomposes the tested system's return by holding. The sample public round shows that leading submissions concentrated in semiconductors, technology, and momentum-oriented exposures during the outcome window.

Required private-report fields:

- Holding and weight
- Entry and exit price
- Holding return
- Contribution to portfolio return
- Risk classification
- Comparison with comparator allocations

## 8. Consistency Results

Private sprints include five non-official repeated runs per system. This sample public report does not contain private repeated-run data, so consistency values are intentionally omitted.

Private consistency tables include:

- Portfolio overlap
- Weight dispersion
- Most frequent holdings
- Allocation range
- Invalid or incomplete responses
- Confidence dispersion
- Official-run representativeness

## 9. Risk And Concentration Analysis

Private reports identify top-holding concentration, theme concentration, defensive allocation, cash allocation, risk appetite, and peer similarity. For the public sample, inspect the underlying round page for official holding-level allocations and audit hashes.

## 10. Cost And Latency

Private reports include cost and latency when provider usage information is available. This public sample does not publish private provider billing or latency telemetry.

## 11. Failure Modes

Private reports include a failure-mode register with severity, evidence, business impact, recommended action, and retest condition. Example categories include invalid output, unstable allocation, excessive concentration, unsupported rationale, and poor cost-performance trade-off.

## 12. Recommended Actions

Private reports translate the evidence into a decision: ship, iterate, switch, or gather more evidence. This public sample does not make a client-specific recommendation.

## 13. Limitations

A one-week market result can be affected by noise, unusual events, and the chosen asset universe. The result applies only to the tested model versions, inputs, constraints, and outcome window. It does not constitute investment advice, a recommendation to trade, certification, endorsement, or a guarantee of future performance.

## 14. Audit-File Index

The public round preserves SHA-256 hashes for key inputs:

| File | SHA-256 |
| --- | --- |
| briefing.md | 4cb4196311a734b680d071464b72238455ef94411a458c401e5178729688dabe |
| manifest.yaml | 12df79a7b7b742013b7573b72b1c996905e41e43f99b297d7160ddb098f001d3 |
| market_data/universe_trailing_returns.csv | 095124e477ab6e8a42084248334a5b1d3bb36d4192a4ea77c152f7ac49fea380 |
| market_data/universe_trailing_returns.json | 47ec7b55b64d30846bb8f3fbb7944a458a5ab63a791a33eabebdb0e5406102d9 |
| market_data/universe_trailing_returns.md | 73926262ce4f8fdccc02f0d6251617a114526b1b8bd1d369b4524065e19ef8ac |
| options.yaml | 8e07e0a1d09976c253d8b385fffa546b2e406bbad7499c7fc9f3fe35f15afcb1 |
| prompt.md | 97a40630adcdf21e0976f9bd2bebc6d4fe0e021a2670d4da7e6189586412e63b |

The underlying public audit page remains the authoritative record.
