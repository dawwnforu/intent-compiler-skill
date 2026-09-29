# 非程序员维护 / Maintenance without programming

日常维护是修改 Markdown；Skill 没有数据库或后台。Python 只用于可选的仓库静态检查，不参与任务执行。

## 修正一次真实失败

1. 保存脱敏的原始请求、相关输入、实际结果与希望的结果。不要只写“更专业”。
2. 先看 [SKILL.md](skills/intent-compiler/SKILL.md) 和[知识索引](skills/intent-compiler/references/knowledge-index.md)。跨领域共同问题才改核心；场景问题改对应模块。
3. 添加可观察的判断规则，说明何时适用、何时不适用。保持既有目标和授权。
4. 在 [examples/validation-cases.md](examples/validation-cases.md) 增加或更新脱敏案例，按 [TESTING.md](TESTING.md) 检查。静态审查、模型实测、宿主安装测试分开记录。
5. 更新中英文 README（若外部行为变化）和 CHANGELOG，提交分支＋PR。

可以直接告诉 AI：“它把只要渲染图的请求扩展成制造。请检查相关规则，修正适用条件并加入反例。”这只授权维护请求本身，不自动授权发布版本或合并其他改动。

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

To add a module, copy the linked template and fill its applicability, prerequisites, decisions, sources, execution, acceptance and stop conditions. Prefer existing specialist skills. No routing code or database changes are needed. Keep time-sensitive claims as execution-time verification tasks.

Run the repository check and follow TESTING.md. Record static review, model behavior and installation tests separately; never call an unrun test successful. Keep both READMEs and manifest versions consistent. Release only with authorization.
