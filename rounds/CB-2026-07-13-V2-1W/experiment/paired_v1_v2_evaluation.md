# Portfolio V2 Paired Evaluation

Decision: **REJECTED**

- Average V1 alpha vs SPY: 5.46%
- Average V2 alpha vs SPY: 3.34%
- Average paired improvement: -2.13%
- Models improved: 0/4
- V1 portfolios beating SPY: 4/4
- V2 portfolios beating SPY: 4/4

## Acceptance Gates

- PASS: all_v2_submissions_valid_and_frozen
- PASS: average_v2_alpha_above_zero
- FAIL: average_v2_alpha_above_v1
- FAIL: at_least_three_models_improved
- PASS: v2_beat_count_not_lower
- PASS: controlled_inputs_match

## Paired Results

| model | V1 return | V2 return | improvement |
| --- | ---: | ---: | ---: |
| openai-gpt-5-5 | 4.75% | 1.57% | -3.18% |
| openai-gpt-5-6-sol | 3.09% | 2.12% | -0.97% |
| xai-grok-4-3 | 6.55% | 3.89% | -2.66% |
| xai-grok-4-5 | 3.67% | 1.98% | -1.69% |
