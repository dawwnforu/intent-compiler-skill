# R24: decision detail versus requested teaching

2026-10-12. One paragraph in an isolated Skill snapshot replaces the broad permission for detailed artifacts with detail selected by purpose. Decision work should retain decisive evidence and omit redundant derivations; explicit teaching/audit requests should retain requested explanations and calculations. **The substitution is not adopted.** [Full protocol and records](results/v2-decision-detail.json).

Two fresh before/after pairs use the same exposed synthetic dataset from [R23](v2-conversion-decision.md). One asks for a short page-selection decision; the other explicitly asks for a complete novice-training example, including all four row rates, pooled rates, percentage-point and relative changes, a common-mix worked example and causal interpretation. Run order is decision-before, teaching-after, decision-after, teaching-before. Model, permissions and all other Skill files are fixed.

The decision report became shorter but retained an algebraic generalization that does not change the recommendation. Necessary counts, source-mix explanation, timing/causal limits and authorized next steps remain. Output fell from 2,151 to 1,923 tokens while time changed from 81.16 to 82.03 seconds. The unchanged rule in R23 already produced 1,935 tokens on the same prompt; these single runs do not isolate a stable rule effect.

The explicit-detail countercheck is assessed from the complete artifacts, not merely the final messages or process status. Independent rational arithmetic checks all rates and differences; byte comparison checks unchanged inputs, and actual tool output confirms each model read its intended paragraph. This is a same-dataset purpose contrast, not a new-domain holdout, human readability study or cross-model evaluation.

All four actual generations completed successfully. Both teaching artifacts retain every requested calculation, distinguish percentage points from relative change, and preserve the limits of common-weight comparisons. The changed paragraph did not omit required detail, but it also did not yield a clear overall benefit:

| Purpose | Variant | Output tokens | Wall seconds | Artifact characters |
|---|---|---:|---:|---:|
| Decision | Before | 2,151 | 81.16 | 1,759 |
| Decision | After | 1,923 | 82.03 | 1,318 |
| Explicit teaching | Before | 4,977 | 165.66 | 5,665 |
| Explicit teaching | After | 5,318 | 256.50 | 5,698 |

Characters count the full artifact, not human reading effort. Output tokens cover the entire model turn. No universal brevity target was imposed on the explicitly detailed request. Necessary calculations and limits pass review in both variants; shorter decision text alone does not justify another shared instruction. Current Skill remains core R15 plus workflow R21, with the unsuccessful trial preserved.
