# Portfolio V2 Resolution Diagnostic

Round: `CB-2026-07-13-V2-1W`

## Bottom Line

This legacy pilot did not save candidate ledgers, so search and ranking losses cannot be separated without hindsight reconstruction. The frozen branch rule therefore selects `test_equal_weight_and_cap_counterfactuals_without_calls`.

## Aggregate Results

- V2 average alpha versus SPY: 3.34%
- Mean paired improvement versus control: -2.13%
- Winner present in selected portfolio: 0/4 models
- Mean realized top-three assets captured: 1.00/3
- Search regret share: n/a
- Ranking regret share: n/a
- Preselection regret: 0.63%
- Construction regret share: 86.92%
- Mean candidate forecast rank correlation: n/a
- Mean candidate forecast error: n/a
- Candidate interval coverage: n/a
- Cross-model selected-portfolio overlap: 50.00%

## Model Diagnostics

| Model | Alpha vs SPY | Search regret | Ranking regret | Preselection regret | Construction regret | Winner captured | Forecast rank IC |
| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| openai-gpt-5-5 | 2.51% | n/a | n/a | 0.63% | 4.99% | No | n/a |
| openai-gpt-5-6-sol | 3.07% | n/a | n/a | 0.63% | 4.43% | No | n/a |
| xai-grok-4-3 | 4.84% | n/a | n/a | 0.63% | 2.66% | No | n/a |
| xai-grok-4-5 | 2.93% | n/a | n/a | 0.63% | 4.57% | No | n/a |

## Construction Counterfactuals

These rules keep each model's selected assets fixed and change weights only. They are one-window diagnostics, not production recommendations.

| Rule | Mean return | Improvement vs submitted | Models improved | Alpha vs SPY |
| --- | ---: | ---: | ---: | ---: |
| cap_35_to_sp500 | 2.11% | -0.28% | 0/4 | 3.05% |
| cap_50_to_sp500 | 2.31% | -0.08% | 0/4 | 3.26% |
| equal_selected | 2.17% | -0.22% | 2/4 | 3.11% |

## Interpretation

This is one prospective decision window and cannot establish a production improvement. The July 17 production round includes the candidate ledger needed for complete search, ranking, and construction diagnostics after it resolves on July 24. Paid challenger calls remain unauthorized until that zero-cost analysis passes its feasibility gate.
