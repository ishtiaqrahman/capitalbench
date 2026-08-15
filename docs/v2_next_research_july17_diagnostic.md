# Portfolio V2 Resolution Diagnostic

Round: `CB-2026-07-17-1W`

## Bottom Line

The dominant loss stage is **none**. The frozen branch rule selects `collect_more_resolved_v2_observations`.

## Aggregate Results

- V2 average alpha versus SPY: 1.71%
- Mean paired improvement versus control: n/a
- Winner present in candidate ledger: 5/8 models
- Mean realized top-three assets captured: 0.75/3
- Search regret share: 27.37%
- Ranking regret share: 41.72%
- Preselection regret: 6.32%
- Construction regret share: 30.91%
- Mean candidate forecast rank correlation: 0.34448537471183743
- Mean candidate forecast error: 1.85 percentage points
- Candidate interval coverage: 77.01%
- Cross-model candidate overlap: 34.61%

## Model Diagnostics

| Model | Alpha vs SPY | Search regret | Ranking regret | Preselection regret | Construction regret | Winner captured | Forecast rank IC |
| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| anthropic-claude-fable-5 | 1.39% | 6.91% | 0.00% | 6.91% | 2.56% | No | 0.892 |
| anthropic-claude-opus-4-7 | 1.18% | 0.00% | 6.91% | 6.91% | 2.77% | Yes | 0.383 |
| anthropic-claude-opus-4-8 | 1.76% | 6.91% | 0.00% | 6.91% | 2.19% | No | 0.690 |
| google-gemini-3-1-pro | 3.37% | 0.00% | 0.00% | 0.00% | 7.49% | Yes | 0.393 |
| openai-gpt-5-5 | 1.44% | 0.00% | 6.91% | 6.91% | 2.51% | Yes | 0.048 |
| openai-gpt-5-6-sol | 1.05% | 0.00% | 9.11% | 9.11% | 0.69% | Yes | -0.126 |
| xai-grok-4-3 | 1.94% | 0.00% | 6.91% | 6.91% | 2.01% | Yes | 0.476 |
| xai-grok-4-5 | 1.54% | 6.21% | 0.69% | 6.91% | 2.41% | No | -0.000 |

## Interpretation

This is one prospective decision window and cannot establish a production improvement. No stage exceeded the frozen 50% dominance threshold, so this result does not authorize a targeted challenger branch. Preserve the completed diagnostic and use multiple later resolved observations before attributing underperformance to one stage.
