# V2 candidate evaluation / 候选版实测

[R37 文本传递规则](../tests/v2-text-transfer.md)：四次前后实测完成，两项 after 输出和耗时均增加，不采纳新增规则。目录原文与更新、报名表数据处理通过独立检查；两版报名启动入口在未准备 Python PATH 的宿主环境均失败，准备相同解释器环境后才通过。保留这个用户入口缺口，不以程序逻辑通过代替完整可用。

[R36 内部资料查询](../tests/v2-internal-lookup.md)：四组真实生成均完成，固定查询和资料更新逻辑均通过；2.0 的真实编辑、下载、重开验证也通过，但各组浏览器覆盖不同。普通请求组同样提供直接编辑与备份，不能作为 2.0 独有收益；2.0 本次输出和耗时最高。不新增规则，保留失败与完整作品。

[R35 实用性补全](../tests/v2-practical-utility.md)：器材借还、每周报价和简单编辑共六次前后实测完成。新版补充纠错、查找、历史查看与备份恢复等具体使用能力，独立逻辑检查通过，简单编辑未扩展范围；两项实质任务输出和耗时均增加，界面验证不完整。采用这段核心判断原则，不宣称普遍优于基础模型或节省 token。

[R34 游戏动态效果](../tests/v2-game-motion.md)：四组实修同一旧作品，均修复减弱动态下地面仍滚动的问题，独立脚本执行保留跳跃、障碍移动、碰撞和重开。候选版没有独有收益且更慢；浏览器只确认画面及开始操作，不宣称完整浏览器玩法或真人舒适度通过。不新增规则。

[R32 评测运行条件](../tests/v2-eval-environment.md)：共用单轮与多轮入口显式传入同一 Python 子进程环境并记录版本，五项进程/接线检查通过，无模型调用。修复的是比较条件，不是 Skill 能力；保留 R30/R31 的环境差异与初次临时目录失败。

[R31 条件权限规则](../tests/v2-public-credentials.md)：四次前后对照完成。两版都修复了 R30 中的公开凭据路径，通过独立 HTTP 与真实浏览器角色切换检查；简单编辑均只改指定文字。原版本轮已修好，不能把效果归于新规则；调整版修复输出和耗时更高，不采纳。两组统一补充已有 Python 的 PATH，与 R30 环境不同，旧失败继续保留。

[R30 报名权限实际修复](../tests/v2-registration-access.md)：四组都把接口检查从 3/11 修到 11/11，但公开页面仍含负责人演示凭据，独立重放可读取全部虚构记录。完整权限目标仍失败，不能把局部测试通过当成完成；候选版没有独有优势。所有组在生成环境中未找到 Python 命令，独立验证另用宿主已有解释器，保留工具发现差异。

[R29 意图复述规则](../tests/v2-intent-assumption.md)：六次前后对照完成。原版本轮没有重现把时间直接当成用户目标的复述，两版都保留动画路线选择和已定二维方案；成本有增有减。未证明这句新规则带来独有收益，因此不采纳，不把新增文字算成改进。

先看[当前判断与下一步](v2-decision.md)：它按用户目标整理有效改动、未证明事项和继续验证的条件。下文为保留的历史实验，各阶段“当前”仅指当时版本，不能合并为最新候选的统一成绩。

[R27 路由拆分](../tests/v2-route-split.md)：四次真实对照中，资料问答不再加载重复执行规则；完整工作流仍读取两个模块。必要结论保留，资料回答少了当前核验日期的显式展示；两题调整版均更慢，不能宣称整体节省。采纳原文段落拆分以缩小特定任务的加载范围。

[R25 来源规则精简](../tests/v2-evidence-trim.md)：移除重复表格示范，保留来源、范围、日期、冲突判断与权限边界。四次实际对照均保留必要结论和依据，输入未改动。采纳较短模块作为指令精简；单次成本差异及原版引号显示问题不能证明稳定节省。当前为核心 R15、工作流 R21、来源 R25。

[R24 按用途控制详略](../tests/v2-decision-detail.md)：四次真实前后对照完成。决策说明稍短但仍含额外推导，耗时未降；完整教学明细两版都保留，调整版输出更多、耗时更高。不采纳这段新规则，避免用单次字数下降宣称稳定收益。当前 Skill 不变。

[R23 新报名页决策题](../tests/v2-conversion-decision.md)：三组均发现总报名率被访客来源构成影响，给出正确计算、因果边界和后续判断方法。候选版没有独有质量优势，输出 1,935 tokens，高于原始组 1,690 和通用组 1,869；耗时介于两者之间。未追加规则，未把已有数据分析能力计为 Skill 独有提升。

[R22 连续反馈修复](../tests/v2-status-feedback.md)：另开持久会话后完成两轮修复。首轮十五条分类符合九条；提供实际错误反馈后，十五条已暴露回归及修复输入均符合预期，缓存、原文和重试检查通过。保留失败的临时会话恢复尝试和首轮误判。没有新增 Skill 规则，也不是新题泛化或组间优势证据。

[R21 状态依据对照](../tests/v2-status-evidence.md)保留一项局部改进：十条预先固定的边界句中，调整前六条、调整后八条符合预期分类；原四条修复和机械检查两版均通过。仅供讨论、未形成结论仍误判，调整后更慢、输出更多。当前核心仍为 R15，工作流模块采用 R21 的实测段落；这不是通用准确率或节省声明。

[R20 工作流实际修复](../tests/v2-workflow-classification.md)：三组均修正原有“未定却标为决定”的记录及旧缓存，独立验证原文保留、重复运行和坏文件重试通过；但新句子“仅供讨论”三组仍误标为明确决定。候选版更慢、输出更多。实际 improve 行为已补测，语义分类仍未修全，不能把机械检查通过当作整体正确。

[R19 后续解释精简实验](../tests/v2-followup-focus.md)六次全部完成。替换一段规则后仍重讲概念，第二轮用时未改善，判断质量各有长短；“没听懂，请再解释”的检查两版都完成。未采纳该替换。用户提供新事实不代表已经理解，所以不能仅按重复字数判断解释无用。

[R18 教学型连续对话](../tests/v2-teach-transfer.md)三组共六轮完成：三组都正确解释多人报名所需的共享存储和权限。候选版把换设备恢复身份作为待确认条件；原始组独自提醒旧数据迁移。候选版更长、更慢，未证明整体优势，也未新增规则。该证据只覆盖自然语言教学请求，不代表全部模式或实际部署已验证。

最新补充：[R17 来源表达对照](../tests/v2-source-presentation.md)六次全部完成。缺字体场景两次调整版省去内部规则归因，有资料场景两版均引用实际许可；其中一次调整版擅自要求至少两款字体。保留完整结果，不追加该实验指令，当前行为仍为 R15。用户此前明确偏好 R15 乙版客服开场的实际目的导向；该反馈只支持这组开场摘要比较。

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

### Post-repair efficiency regression

Six additional runs used the same already-exposed course/habit prompts, three each, with repaired corec51d267 (repository61423aa). These are regressions, not a new holdout or contemporaneous randomized comparison. All results retained; [raw counters/ranges](../tests/results/v2-efficiency-regression.json).

| Median | Historical G | Historical V1 | Frozen V2 | Repaired V2 |
|---|---:|---:|---:|---:|
| Course output tokens | 3325 | 4852 | 3705 | 4189 |
| Habit output tokens | 8437 | 8778 | 7211 | 9527 |
| Course seconds | 90.38 | 123.55 | 101.88 | 118.58 |
| Habit seconds | 175.90 | 212.62 | 185.64 | 243.39 |

Repaired input/cache medians: course146750/130304, habit359136/338560. Latest UI results did **not** retain the earlier output/time advantage; do not advertise the frozen numbers as the current version's savings. Phase, sampling and implementation choices prevent attributing this change to the added rule. Actual UI reads did not load the data-analysis module, so an unnecessary data-module load is not supported as the explanation.

All three course reports retained correct core statistics and synthetic/noncausal boundaries. One described an unknown completion state's blank as definitely structural missingness; the available record does not independently establish that path. This is an interpretation precision limitation, not an arithmetic error or an all-sentences-correct pass. All three pages passed the same independent Edge interaction, real export, persistence, literal-name, screenshot and date-reopen checks; no new core UI failure observed. The checkbox variant was located through its native label. Full accessibility and real-device tests remain outside these checks.

### Earlier development evidence

A later [browser-probe ablation](../tests/v2-browser-probe-regression.md) tested a small verification-planning paragraph with six sequential attempts. Five completed; the sixth hit an account usage limit and has no complete token record. Two complete pairs disagree on cost direction, and self-verification completion differs. Independent checks passed for the six saved pages, including the explicitly partial one, without repairing them. This is neither a complete balanced comparison nor evidence of general savings. The extra paragraph was removed; the active Skill remains the repaired pre-ablation version. All attempt records and the failed run are retained.

After ordinary usage became available, a separately recorded recovery completed with7731 output tokens and318.92 seconds; its saved page also passed independent core checks. The original failed record is unchanged. This additional phase does not establish a benefit or justify retaining the added paragraph; no further ablation process is running.

[迭代记录](v2-iterations.md)保留每轮正反结果。九个公开项目README用于还原自然语言需求，没有声称恢复原始聊天或审计全部代码。

| Area | Observed outcome / change |
|---|---|
| Forms | Four arms preserved missing salary/contact facts; no exclusive V2 gain. |
| Survey/data | Initial V2 duplicated reports; changed to one primary reading format. Retests stayed numerically correct, but output varied with format. |
| Interactive quiz | All flows/export checked; A had mobile horizontal overflow, G/V1/V2 did not. V2 was slower than A/G. |
| Knowledge/update | All resolved current vs historical facts and updated from the same new decision; inputs/links checked. V2 retained one document with lower update output. File continuity is not conversation-memory proof. |
| Recovery workflow | All unchanged processors passed sequential partial-failure and2→2→3→3 idempotence checks; V2 did not beat G/V1 output cost. |
| URLs/frontend/backend | All repaired same-origin API access, save failure and restart persistence; local server/Edge checks passed. No public deployment/domain purchase tested. |
| Touch game/animation | Historical browser checks observed changing frames after touch dispatch, collision/end and restart at mobile size; frame changes alone did not prove jumping. A later [saved-script unit check](../tests/v2-game-jump.md) directly verifies all four pointer handlers cause upward movement. Real-device touch and reduced-motion effectiveness remain unverified. V2 had highest output/time in this development trial. |
| Agent gap | All delivered local drafts and reported absent live integrations. Post-hoc negation/conditional/unaccepted-proposal inputs broke A's extractor; G/V1/V2 retained uncertainty. Not V2-only or a pre-registered intent score. |
| Simple edit | All produced the sentence without tool work; no efficiency advantage established. |

The earlier core was compressed from5495 to4241 Unicode characters while preserving routing, modes, boundaries and verification; subsequent dialogue guidance adds text and is outside that size comparison. Text size is not a token-saving percentage. Papers informed hypotheses and modules; no model training or reproduction of paper results occurred. See [research/read scope](v2-research.md).

## R7: scope guidance is visible, prioritization still weak

The user's clarified target is useful judgment in the conversation before unnecessary implementation. In the [fixed two-turn training-platform check](../tests/v2-scope-dialogue.md), the revised candidate explained consequential choices and waited for an answer without generating platform files. Raw A implemented first; the previous candidate asked a provider-model question but continued implementing and timed out after900 seconds. G encountered a capacity error, so this is an incomplete comparison, not a four-way ranking.

After the same local-demo supplement, both completed conversations respected the no-code instruction. The candidate explained later operating requirements but kept simulated payment, teacher management and course discussion in the first version. A more clearly recommended deferring these features. This negative result is retained: better timing of clarification is not proof of better feature prioritization. Three candidate-only exclusion checks preserved a simple rewrite, settled scope and real multi-user requirements. No human satisfaction study or independent runtime check of these new platform artifacts was performed. [Responses](../tests/results/v2-scope-dialogue.json), [exclusions](../tests/results/v2-scope-exclusions.json).

## Evidence limits and next decision

Separate C6 recovery: all three arms completed on the same R15 snapshot, actually read/rejected the supplied note and reported missing inputs without fake preview/publication. The original R16 capacity failure remains in place. Candidate output380 exceeded G182/A163 and took longer; no exclusive correctness or efficiency win. This completes the legacy text condition, not independent environment discovery or broad injection resistance. [Recovery details](../tests/v2-legacy-boundaries.md).

R16 adds twelve completed raw/generic/candidate text attempts for legacy C1/C2/C4/C5. All preserve the main boundaries and honest completion status; candidate C1 excludes fabrication and C5 performs no tool work. Domain-case candidate output/time are higher than the two baselines. C6 candidate failed at model capacity before a substantive turn; remaining arms are unattempted. [Complete records and limits](../tests/v2-legacy-boundaries.md). No rule was added and no image, physical part or deployment was produced.

Human feedback on2026-10-12: the user preferred R15 after's purpose-oriented support opening in a self-contained inline comparison: “乙，更贴近实际目的”. Both alternatives were described as waiting without code. This is one explicit preference about the summarized opening, not a blinded full-conversation study or a broad satisfaction result.

R15 retains one core-paragraph sequencing change: clarify an unknown purpose before detailed scope. All nine turns completed; both variants already waited without product files. After first turns asked more directly about the job/experience/decision and did less early preparation. Both follow-ups correctly prioritized evidence-based support assessment and interview-oriented case studies; portfolio after wrote a longer document and cited an internal rule in its opening. Creative requirements survived. [Every response, brief and counter](../tests/v2-purpose-gate.md). This supports a narrow ordering correction, not unique final quality, stable whole-task savings or human preference.

R14 tested a narrower clarification-index trigger in six repeated font responses and two platform responses. All completed; font policy reads changed from2/3 to1/3, but median output558→597 and time34.50→42.23 seconds worsened. Necessary font guidance remained; the platform pair offered no purpose-elicitation improvement. The row change was not adopted, and R12 remains active. [All attempts, exact rejected text and confounds](../tests/v2-routing-cost.md).

R13 completes the previously unrun missing-font C3 text condition in four arms. All avoided invented files, rights and completed implementation; A/G offered an explicit system-font alternative, while V1/V2 explained actual resource, loading and use-right prerequisites. V2's572 output tokens exceeded A288/G283/V1537. This is no exclusive2.0 correctness or efficiency win; [full results](../tests/v2-font-gap.md) preserve the differing approaches. No new rule was added.

R12 retains a two-bullet clarification change: identify the job, experience or decision before selecting scope, while preserving reaffirmed requirements. All nine attempted turns completed. In the exposed training follow-up, the revised candidate deferred simulated payment and community features and explained a course→registration→confirmation scope. Both first turns still suggested broad feature flows; knowledge transfer was correct in both variants, and a candidate-only creative check preserved all required interactions. Training output did not decrease; differing knowledge-draft work prevents a stable savings conclusion. [Full protocol, responses and briefs](../tests/v2-outcome-elicitation.md). This is a narrow correction, not a new four-arm superiority result or human preference evidence.

R11 closes a scoped font-runtime gap with [four identical-input attempts](../tests/v2-font-library.md). A/G/V2 completed; V1 hit model capacity without a final response or usage. All four saved pages passed independent offline loading, different tested Chinese rendering, two actual PNG downloads and decoded pixel equality; V1 remains a partial artifact. All blocked saving after font-load rejection. A exposed an English error; V2, G and partial V1 provided Chinese guidance, so this was not a V2-only capability. V2 output6458 tokens versus A7728/G7394 in this one trial; no repeated or causal efficiency conclusion follows. Fixed-footnote and title-only typography limitations are retained. No Skill rules were added, no interrupted result replaced, and the older missing-resource C3 remains unrun.

R10 tested extra product-scope guidance with six brief-only before/after runs. Both candidate variants already produced relevant scope and acceptance for spreadsheet replacement, visual storytelling and a real shared workflow. The extra text had no demonstrated unique consequential benefit; output/time effects were mixed in interpretation and single-sample. It was withdrawn, keeping R9 active. [All documents and measured counters](../tests/v2-product-scope.md). This does not prove the added guidance is universally ineffective, or that the base model alone would perform identically: both conditions used the repaired Skill.

R9 adds an explicit separation of final use, execution restrictions and confirmed/delegated choices. Both candidate two-turn conversations waited without writing platform files, then used the actual supplement. The new community case removed deposits/chat and translated missing borrowing conditions into rules and checks; a delegated CSV was independently parsed successfully. Training still retained more optional prototype features than clearly needed. Community/G began implementation before clarification and timed out at the predeclared300-second limit, so no balanced final-quality or efficiency advantage follows. [Full protocol and results](../tests/v2-decision-boundary.md). This is targeted progress, not the requested broad, stable advantage or a human satisfaction result.

The repaired dialogue keeps lodging reimbursement unknown after the policy arrives because nightly amounts remain missing. After the same conversation receives actual nightly amounts200/520, the generated CSV correctly computes lodging500 and total730 instead of assuming830. Independent CSV parsing checked every original/allowed/difference value and unchanged source inputs. Two new parcel examples distinguish per-parcel caps (need component values) from an explicit whole-order cap (800 determined; no extra question). [Repair evidence](../tests/results/v2-repair.json) includes actual responses and raw CLI counters. This is one targeted regression and two brief transfer checks, not a repeated superiority benchmark. Resumed-conversation counters are retained as returned and may include accumulated session usage; do not sum them or treat them as verified per-turn increments.

The committed JSON contains all67 CLI counter records, not independent semantic grades. Full raw events, generated artifacts, browser profiles/downloads and screenshots remain in the local evaluation workspace, outside this lightweight repository. Published fixtures allow a new reproduction, not exact regeneration. Review was by the development agent using external calculations/runtime observations; no blinded human preference study occurred.

Untested: cross-model/Claude behavior, repeated new tasks in every domain, live third-party Agent integrations, real manufacturing/load tests, full font-rights/provider checks, internet deployment, actual phones, full accessibility/storage failures and concurrent/power-loss workflow stress. The added identical-answer two-turn experiment is completed, with the failure above; it is not a broad conversational-capability pass. Legacy C1/C2/C4/C5 have R16 text results, C3 has separate R13 results, and C6 has a separate recovery after the retained capacity failure. Mode coverage remains incomplete: R18 checks natural-language teaching and R20 checks an explicit improve request, with the retained semantic failure. These limits are not implied passes.

Recommended status: reviewable candidate. Use routing/gap discovery where useful; simple work may need only a brief instruction. Do not market this as universally smarter, cheaper or an “astonishing” improvement. No license change, marketplace upload, purchase or normal-installation replacement occurred during these experiments.

## R28：关机后的自动整理，四组解释对照完成

[完整记录](../tests/v2-unattended-transfer.md)：四组两轮现已完成，旧版第二轮通过原会话恢复，保留全部容量失败。四组均解释夜间运行、补改、来源与人工修正，候选版没有独有质量优势；输出计数低于旧版，高于原始请求与通用规则。四组首轮均建议下班前整理，候选版把时间写成理解到的目标；全部第二轮均按明确补充修正。没有实际自动化验收或稳定节省结论，无新规则改动。
