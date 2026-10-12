# 非程序员维护 / Maintenance without programming

日常维护是修改 Markdown；Skill 没有数据库或后台。Python 只用于可选的仓库静态检查，不参与任务执行。

候选版已有[实测结果](docs/v2-results.md)和[公开回归材料](tests/v2-heldout-cases.md)。修改后可用它们查回归；若用这些题调优，就不能继续称为未见集。新效果声明需保留失败、输入/缓存/输出用量和实际产物检查，不把CI绿灯当作行为改善。

## 修正一次真实失败

文字被整理成“决定／待办”等状态时，要保存原句，并用含义相反或措辞变化的句子检查：未批准不等于批准，明确禁止仍是决定，引号里的词不代表整句状态。也要检查旧缓存是否更新。参考[实际工作流对照](tests/v2-status-evidence.md)；少数句子通过不等于任意表达都能识别。

2.0 候选开发遵循[四组对照协议](tests/v2-protocol.md)。先记录原始请求与失败证据，再改通用根因；保留未改善和退步结果。论文依据留在开发文档，不加进普通任务的默认上下文。不要为了缩短答复而删验收，也不要把同一份重复说明移到额外文件后声称节省。

1. 保存脱敏的原始请求、相关输入、实际结果与希望的结果。不要只写“更专业”。
2. 先看 [SKILL.md](skills/intent-compiler/SKILL.md) 和[知识索引](skills/intent-compiler/references/knowledge-index.md)。跨领域共同问题才改核心；场景问题改对应模块。
3. 添加可观察的判断规则，说明何时适用、何时不适用。保持既有目标和授权。
4. 在 [examples/validation-cases.md](examples/validation-cases.md) 增加或更新脱敏案例，按 [TESTING.md](TESTING.md) 检查。静态审查、模型实测、宿主安装测试分开记录。
5. 更新中英文 README（若外部行为变化）和 CHANGELOG，提交分支＋PR。

可以直接告诉 AI：“它把只要渲染图的请求扩展成制造。请检查相关规则，修正适用条件并加入反例。”这只授权维护请求本身，不自动授权发布版本或合并其他改动。

如果问题是“用户不懂怎么定范围，AI 就直接写了一堆代码”，保存实际多轮对话和开始实施的时点。检查它是否解释必要选择、提出有理由的建议，并根据补充信息调整行动；不要只检查最终总结是否提到了边界。同时保留简单任务、已定范围和真实上线目标的反例，避免把修复变成每次都盘问或强制缩小项目。可参考[对话验证协议](tests/v2-scope-dialogue.md)。

如果它问过问题后仍把愿望清单全部做成演示，检查是否弄清这版要支持的工作、体验或决定，以及每项保留/暂缓的理由。参考[目的与范围对照](tests/v2-outcome-elicitation.md)，同时保留用户明确坚持的创意要求；不能以功能少或问得多直接判为更好。

如果提问前已经展开大量功能，参考[先问用途的对照](tests/v2-purpose-gate.md)，分别检查首轮和补充后的实际行为。不要把较短开场当作整段会话省时，也不要把引用内部规则当作面向用户的有用解释。

## 新增知识模块

1. 检查已有模块、可用专业 Skill 和项目资料能否解决；不要重复造知识库。
2. 在 GitHub 打开[模板](skills/intent-compiler/references/knowledge-module-template.md)，复制全文，在同一 references 目录新建有意义的 Markdown 文件。
3. 填写适用/触发/排除条件、前提、判断、遗漏、来源、执行、验收、继续检索和停止条件。专业术语可让 AI 帮助解释，业务事实不能让它编造。
4. 在知识索引加入一行和相对链接，至少添加一个应加载案例与一个不应加载案例。无需改代码。
5. 动态价格、平台功能、具体许可与地区规则写成执行时核验任务；记录实际查阅的来源、范围与日期，不把未知写成已核验。

## GitHub 操作和检查

使用文件的编辑按钮修改，选择新分支并提交 PR。仓库工作流运行 `python tests/check_repository.py`，只检查打包路径、链接与案例结构。若检查失败，打开日志定位缺失文件或字段。绿色检查不证明 Skill 行为正确；仍需按测试文档审查案例。模型运行不了就写“未实测”。

## 版本发布

行为变化同步更新 `.codex-plugin/plugin.json` 与 `.claude-plugin/plugin.json` 的版本、CHANGELOG 和对应文档。核对 [COMPATIBILITY.md](COMPATIBILITY.md) 的官方来源及实际测试状态。只有获得发布授权才创建 release；不要把 PR 创建说成已经合并或安装更新。

## English

Maintain this Skill by editing Markdown. Capture a redacted request, inputs, observed failure and desired observable behavior. Change the relevant module; change the core only for shared behavior. Add an applicable case and an exclusion case, update the index and changelog, and open a branch/PR.

For premature implementation, retain the actual conversation and timing of actions. Check whether consequential choices were explained before affected work began and whether later answers changed the plan. Include simple, settled-scope and genuine multi-user cases so guidance does not become a mandatory interview or automatic downsizing.

If a wish list still becomes a full demo after clarification, inspect the actual job, experience or decision and the reasons for keeping/deferring work. Preserve reaffirmed creative requirements; fewer features or more questions alone do not establish better judgment.

Check purpose questions before detailed scope separately from the follow-up: a shorter opening does not prove lower whole-conversation cost, and citing internal instructions is not a useful user-facing explanation.

To add a module, copy the linked template and fill its applicability, prerequisites, decisions, sources, execution, acceptance and stop conditions. Prefer existing specialist skills. No routing code or database changes are needed. Keep time-sensitive claims as execution-time verification tasks.

Run the repository check and follow TESTING.md. Record static review, model behavior and installation tests separately; never call an unrun test successful. Keep both READMEs and manifest versions consistent. Release only with authorization.

来源记录应保留具体依据、范围和核验时间，不要求每次面向用户输出固定证据表格。知识模块的可填写模板仍完整保留。改动这类规则时，至少检查有明确资料和资料冲突的情形，记录实际读取而非只匹配引用文字。

Source records retain evidence, scope and dates without requiring a fixed user-facing ledger. Keep the fillable knowledge template; test supplied-evidence and conflicting-record cases, and inspect actual reads.
