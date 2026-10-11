# 贡献指南 / Contributing

欢迎贡献真实、可复现的使用案例。最有价值的改进通常很小：一个失败示例、一条更准确的判断规则，或一处更清楚的普通话说明。

## 不会代码也可以贡献

1. 在 GitHub 打开 Issue，写清楚“你说了什么、AI 做了什么、你希望它怎么做”。
2. 或直接编辑 Markdown 文件并提交 Pull Request。
3. 不要放入客户姓名、账号、密钥、内部文件或其他隐私信息。

## Pull Request 检查

- 改动是否解决一个真实问题，而不是假设未来需求？
- 是否放在最相关的一个文件里？
- `SKILL.md` 是否仍然简短，细节是否应放入 `references/`？
- 新规则是否保留用户意图与授权边界？
- 是否更新 `CHANGELOG.md`？

---

Contributions from non-programmers are welcome. The best report includes the original request, the observed result, and the desired result. Markdown edits are enough for most improvements.

Keep changes narrow, remove private information, place conditional detail in `references/`, and update `CHANGELOG.md` when behavior changes.

Use the [module template](skills/intent-compiler/references/knowledge-module-template.md) for new domain guidance and update the [knowledge index](skills/intent-compiler/references/knowledge-index.md) with loading, exclusion and stop conditions. Add a realistic positive case and an exclusion case. Follow [TESTING.md](TESTING.md); distinguish static checks from model tests and never invent improvement figures. Python is optional for maintainers and unnecessary for Skill use.

新增领域请填写模板并更新知识索引，提供应加载和不应加载的案例。按测试文档区分静态检查、模型实测和安装测试；未实测就明确注明，不编造提升比例。

