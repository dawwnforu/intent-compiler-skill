# 开始使用 / Start here

给已有可用 **Codex**、希望把普通想法变成专业需求说明或成果的人。当前免费试用，模型和外部工具费用另计。没有 Codex 或没有模型额度时，先看样例，不必为参加试用购买新服务。

**先看交付：** [实际建模说明](../tests/results/intent-handoff-r99/C-brief.md)。[中英文可操作演示](demo/index.html)是本地候选页；[领取完整演示 ZIP](intent-compiler-demo-r100.zip)，解压后打开 `pilot/demo/index.html`，不要只移动 HTML。演示包不是 Skill 安装包。GitHub 文件页需点 Download raw file，HTML 预览只显示源码；此新包浏览器下载和外部收件尚未验证。它复用内部合成案例，不是客户作品或已完成的 3D 模型。[对照四组均通过](../tests/v2-intent-handoff.md)，没有证明 Skill 独有优势。

## 三步开始

1. 打开 [Agensi 免费商品](https://www.agensi.io/skills/intent-compiler-everyday-ideas-to-usable-work)，按页面正常连接自己的 Codex，亲自登录并授权。已经连接就不重复配置，不要求买积分或另装同名副本。
2. 在已连接的 Codex 中说：

   > 请从 Agensi 加载 Intent Compiler — Everyday Ideas to Usable Work，读取 SOURCE.json 并报告实际来源。找不到或来源不同就先告诉我，不另装同名 Skill、不替换正式安装。然后用它处理我接下来提出的任务；先检查实际工具和授权。

   2026-10-26核对的商品为平台 **1.1 / cefba82 / Free**；清单 **0.2.0** 与 **2.0 候选**是不同标识。平台会更新，请记录实际来源，不能只看名称判断版本。
3. 用自己的话提出一个真实小目标，只用公开、自制或明确有权使用的素材。可以先要“给建模同学的需求说明”，也可以让 Agent 按实际工具继续制作；不用照抄完美提示词。打开真实文件，提出一次你需要的修改，再决定是否采用。

## 卡住怎么办

告诉原邀请人或在你看到的招募帖反馈：卡在领取、连接、来源、生成、打开还是修改。可以正常接受帮助，不要求先学编码。生成后打开文件检查中文和附件名；旧包实测发生过乱码及开发者修复，**新版渠道完整业务仍未验证**。

愿意接受观察时先约定范围。沿用[现有反馈安排](feedback.md)，只需说明是否采用、补过几次专业要求、质量返工几轮及需要哪些帮助；普通偏好修改另记。无需默认提供完整对话、私人文件或录屏。本页/演示不自动采集反馈，输入仍受所用模型服务的数据政策约束。

## Agensi 不适用时：固定 GitHub 备用

[领取固定 af3d2c8 ZIP](https://raw.githubusercontent.com/dawwnforu/intent-compiler-skill/d4648d8375456fe7a11c29d9f498a98573c03040/commercial/artifacts/intent-compiler-2.0-candidate-af3d2c8.zip)。该旧备用包为37,504字节，不含 cefba82 后加的编码核验方法，不与当前渠道混记。

完整解压到**新空项目**的 `.agents/skills/intent-compiler/`，直接包含 `SKILL.md`、`SOURCE.json` 和其余文件；已有同名目录时换空项目，不覆盖正式安装。新会话明确要求读取该完整项目路径的 SKILL 和 SOURCE，核对 sourceCommit 为 `af3d2c8` 对应完整提交；发现其他来源先求助。下载、安装复制、发现和业务验证的范围见[兼容记录](compatibility.md)，不推断其他宿主都支持。

---

## English quick start

For people with a working **Codex** who need help with an unfamiliar professional task. The skill is free; model and external-tool costs are separate. Start with a small task using public or self-created materials. Do not send company/customer secrets.

1. Open the [free Agensi listing](https://www.agensi.io/skills/intent-compiler-everyday-ideas-to-usable-work), connect your Codex normally and complete sign-in/consent yourself. Do not reconnect an existing setup or install a second copy.
2. Ask your agent to load **Intent Compiler — Everyday Ideas to Usable Work**, read `SOURCE.json`, and report the actual source before using it. If missing/different, ask for help; do not replace your formal installation. Checked on2026-10-26: platform1.1 / source cefba82. Record the version actually loaded.
3. Describe what you want in your own words. Open the deliverable, request a change you actually need, and decide whether to adopt it. A brief is a brief, not a completed model/site.

Inspect the [actual Chinese brief](../tests/results/intent-handoff-r99/C-brief.md) or download the [complete bilingual demo ZIP](intent-compiler-demo-r100.zip). Extract it and open `pilot/demo/index.html`; it is not a Skill installer. On GitHub choose Download raw file; the HTML file view is source only. Browser acquisition and external receipt of this new demo package remain unverified. The synthetic case passed in all four comparison arms and does not prove unique gains, automatic long-term memory or fewer user interventions.

If stuck, contact the person who invited you through the original channel. Full conversations and private files are not required. Agree any observation scope first; use the [existing feedback process](feedback.md). The older channel package needed assisted encoding repair; full updated-package channel behavior and other hosts remain unverified. The pinned af3d2c8 GitHub fallback above is a different version and lacks the later encoding-check method.

Original project: [dawwnforu/intent-compiler-skill](https://github.com/dawwnforu/intent-compiler-skill) · Intent Compiler contributors · MIT. No new installation, model purchase or account is performed by this page.
