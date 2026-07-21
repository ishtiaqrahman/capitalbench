# LLM Quality-Input Replay Results

Decision: **rejected**

| Treatment | Valid pairs | Return improvement | Treatment alpha | Positive pairs/models/periods | Regret reduction | Capture change | Worst-period change | Gate |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| Q2 | 8 | 1.25% | -0.42% | 3/3/1 | -1.14% | 0 | 2.80% | fail |

## Execution

- New provider calls: 12
- Valid calls: 8
- Input tokens: 187,876
- Output tokens: 9,667
- Reasoning tokens: 7,927

## Interpretation

The treatments change information and instructions inside the LLM call. No post-response portfolio overlay or reranking is applied. Historical reuse can reject weak treatments but cannot confirm prospective skill.
