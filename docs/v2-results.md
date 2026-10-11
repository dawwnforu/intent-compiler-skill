# V2 candidate evaluation / 候选版实测

2026-10-12 local date. **Partial efficiency gains, no general superiority established.** 共67次真实生成：43次开发集，冻结后24次新题；没有删掉较慢或无改善的结果。候选版本仍未正式发布。

随后补充4个真实连续对话（每组2轮），发现冻结V2的一个必要条件遗漏；同样的计算错误也出现在G/V1。初始评测答案本身亦有错误，已通过反例纠正并保留记录。修复c51d267已通过一个三轮开发回归和两个新领域正反例；下面67次成本数据只支持此前冻结版本，不作为新修复的成本结论。见[回归案例](../tests/v2-granularity-regression.md)。

## Repeated new tasks

A=原始请求，G=一句通用规则，V1=0.2.0，V2=冻结候选。每任务每组3次，模型`gpt-6.1-sol`、low reasoning、工具/权限一致、独立工作目录。方法、原始中文需求和材料见[可复测用例](../tests/v2-heldout-cases.md)，每次用量/耗时及中位数范围见[记录](../tests/results/v2-runs.json)。

下面都是中位数，输入包含CLI报告的缓存输入；各列分别取中位数，不能相减来推算某一次的未缓存量。输出包含代码和推理等，不能全部称为闲聊或浪费。没有换算费用。

| Task | Arm | Input tokens | Cached input | Output tokens | Seconds |
|---|---|---:|---:|---:|---:|
| Course analysis | A | 118897 | 107648 | 4497 | 109.72 |
| Course analysis | G | 98017 | 90368 | 3325 | 90.38 |
| Course analysis | V1 | 181663 | 164352 | 4852 | 123.55 |
| Course analysis | V2 | 140749 | 128000 | 3705 | 101.88 |
| Habit UI | A | 125758 | 106880 | 11599 | 223.70 |
| Habit UI | G | 91205 | 75904 | 8437 | 175.90 |
| Habit UI | V1 | 340780 | 320256 | 8778 | 212.62 |
| Habit UI | V2 | 259321 | 238976 | 7211 | 185.64 |

12份课程报告均通过独立内容审阅：正确去重、有效分母、条件时长零值/缺失、前后配对，不把合成数据或自评变化说成真实因果效果。12个页面均经过独立Edge390px操作：添加、取消/再次完成、刷新保留、实际JSON下载、字面量名称、计数、无横向溢出及截图可读性。所有组均通过这些核心检查，未发现新版独有质量优势。

全部页面通过事后日期诊断：次日重新加载为0项，回到原日为1项，历史保留。它不是预注册终点，也不证明持续打开跨午夜。浏览器使用DOM点击/表单提交，未覆盖真实手机触控或完整键盘/屏幕阅读器流程。截图未显示明显的V2独有视觉优势。

V2比V1在两个任务的输入/输出和耗时中位数低。G的数据分析更省；UI中G输入更少、耗时更短，V2输出更少。不能把输出优势写成总费用一定更低。A的部分页面附带历史/周视图和示例项目，各组报告格式也不完全相同。采样、实现范围与缓存影响结果；三次重复、一个模型和两个新任务不足以证明跨领域普遍提升。

## Development cases and changes

[迭代记录](v2-iterations.md)保留每轮正反结果。九个公开项目README用于还原自然语言需求，没有声称恢复原始聊天或审计全部代码。

| Area | Observed outcome / change |
|---|---|
| Forms | Four arms preserved missing salary/contact facts; no exclusive V2 gain. |
| Survey/data | Initial V2 duplicated reports; changed to one primary reading format. Retests stayed numerically correct, but output varied with format. |
| Interactive quiz | All flows/export checked; A had mobile horizontal overflow, G/V1/V2 did not. V2 was slower than A/G. |
| Knowledge/update | All resolved current vs historical facts and updated from the same new decision; inputs/links checked. V2 retained one document with lower update output. File continuity is not conversation-memory proof. |
| Recovery workflow | All unchanged processors passed sequential partial-failure and2→2→3→3 idempotence checks; V2 did not beat G/V1 output cost. |
| URLs/frontend/backend | All repaired same-origin API access, save failure and restart persistence; local server/Edge checks passed. No public deployment/domain purchase tested. |
| Touch game/animation | All passed touch jump, moving frames, collision/end and restart at mobile size; V2 had highest output/time in this development trial. |
| Agent gap | All delivered local drafts and reported absent live integrations. Post-hoc negation/conditional/unaccepted-proposal inputs broke A's extractor; G/V1/V2 retained uncertainty. Not V2-only or a pre-registered intent score. |
| Simple edit | All produced the sentence without tool work; no efficiency advantage established. |

Core text compressed from5495 to4241 Unicode characters while preserving routing, modes, boundaries and verification. Text size is not a token-saving percentage. Papers informed hypotheses and modules; no model training or reproduction of paper results occurred. See [research/read scope](v2-research.md).

## Evidence limits and next decision

The repaired dialogue keeps lodging reimbursement unknown after the policy arrives because nightly amounts remain missing. After the same conversation receives actual nightly amounts200/520, the generated CSV correctly computes lodging500 and total730 instead of assuming830. Independent CSV parsing checked every original/allowed/difference value and unchanged source inputs. Two new parcel examples distinguish per-parcel caps (need component values) from an explicit whole-order cap (800 determined; no extra question). [Repair evidence](../tests/results/v2-repair.json) includes actual responses and raw CLI counters. This is one targeted regression and two brief transfer checks, not a repeated superiority benchmark. Resumed-conversation counters are retained as returned and may include accumulated session usage; do not sum them or treat them as verified per-turn increments.

The committed JSON contains all67 CLI counter records, not independent semantic grades. Full raw events, generated artifacts, browser profiles/downloads and screenshots remain in the local evaluation workspace, outside this lightweight repository. Published fixtures allow a new reproduction, not exact regeneration. Review was by the development agent using external calculations/runtime observations; no blinded human preference study occurred.

Untested: cross-model/Claude behavior, repeated new tasks in every domain, live third-party Agent integrations, real manufacturing/load tests, full font-rights/provider checks, internet deployment, actual phones, full accessibility/storage failures and concurrent/power-loss workflow stress. The added identical-answer two-turn experiment is completed, with the failure above; it is not a broad conversational-capability pass. Earlier six scenario records remain separately labeled static cases. These limits are not implied passes.

Recommended status: reviewable candidate. Use routing/gap discovery where useful; simple work may need only a brief instruction. Do not market this as universally smarter, cheaper or an “astonishing” improvement. No license change, marketplace upload, purchase or normal-installation replacement occurred during these experiments.
