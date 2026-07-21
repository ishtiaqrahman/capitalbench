# LLM Quality-Input Replay Results

Decision: **rejected**

| Treatment | Valid pairs | Return improvement | Treatment alpha | Positive pairs/models/periods | Regret reduction | Capture change | Worst-period change | Gate |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| Q1 | 9 | 1.59% | 0.13% | 8/3/3 | -3.11% | -2 | 0.33% | fail |
| Q2 | 8 | 2.90% | 1.50% | 8/3/3 | -1.40% | 0 | 1.55% | fail |

## Execution

- New provider calls: 26
- Valid calls: 17
- Input tokens: 142,216
- Output tokens: 20,188
- Reasoning tokens: 12,383

## Interpretation

The treatments change information and instructions inside the LLM call. No post-response portfolio overlay or reranking is applied. Historical reuse can reject weak treatments but cannot confirm prospective skill.
