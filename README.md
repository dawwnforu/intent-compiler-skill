<p align="center">
  <img src="skills/intent-compiler/assets/intent-compiler.svg" width="220" alt="Intent Compiler 线稿头像：把自然语言整理成可执行任务">
</p>

<h1 align="center">Intent Compiler｜需求编译器</h1>

<p align="center"><strong>你负责说人话，AI 负责补专业知识并把事情做完。</strong></p>

<p align="center"><a href="README_EN.md">English</a> · <a href="LICENSE">MIT License</a></p>

Intent Compiler 是一个面向普通办公人员、创作者、学生和非技术用户的 Agent Skill。用户不必学习提示词、UI 术语、编程概念或研究方法，只需描述目标；Skill 会在内部整理需求、补足必要的领域知识、选择执行方式、自检并交付结果。

## 它解决什么

你可以直接说：

> 帮我做一个给老板看的季度总结，数据在附件里，看起来专业一点。

Skill 会自行识别受众、交付物、信息缺口和质量标准。只有当某个选择会明显改变结果、造成外部影响或无法安全推断时，它才追问。

默认行为不是“替你写一段更长的提示词”，而是：

```text
自然语言 → 还原意图 → 补领域知识 → 形成内部执行说明 → 执行 → 自检修正 → 交付
```

## 安装

### Codex 插件

```bash
codex plugin marketplace add dawwnforu/intent-compiler-skill
codex plugin add intent-compiler@intent-compiler
```

重启 Codex 后即可使用。

### Claude Code 插件

```text
/plugin marketplace add dawwnforu/intent-compiler-skill
/plugin install intent-compiler@intent-compiler
```

### 只安装 Skill

下载仓库后，把 `skills/intent-compiler` 文件夹复制到你的 Agent Skills 目录。不同工具的目录位置不同；如果不确定，直接让当前 AI 帮你安装这个 GitHub 仓库里的 Skill。

## 使用

正常说话即可，Skill 可以自动识别适合的任务。也可以明确调用：

```text
$intent-compiler 帮我把这份会议记录整理成行动清单
$intent-compiler brief -- 先把我的想法整理成需求说明，不执行
$intent-compiler teach -- 告诉我这个 UI 项目缺少哪些关键概念
$intent-compiler improve -- 检查并改进这份现有方案
```

在支持斜杠命令的宿主中，也可使用：

```text
/intent-compiler 帮我规划一次客户访谈
/intent-brief 把这个模糊想法整理清楚
/intent-improve 改进这份海报方案
```

## 适用场景

- 办公：报告、邮件、会议纪要、表格、演示文稿、流程梳理
- 研究：问题定义、检索策略、证据判断、分析框架
- 设计：UI/UX、视觉层级、配色、排版、图像提示、可访问性
- 创作：文案、故事、图片、视频概念、Blender/3D 制作说明
- 产品与代码：需求拆解、原型、实现、测试和交付说明

领域补充不是百科全书。Skill 只加载当前任务相关的[领域指南](skills/intent-compiler/references/domain-lenses.md)，避免把简单任务变复杂。

## 对非程序员友好的维护

日常更新主要改 Markdown 文本，不需要写代码：

1. 在 `examples/` 增加真实的输入/输出例子。
2. 在 `skills/intent-compiler/references/` 调整判断规则。
3. 在 `CHANGELOG.md` 记录变化。
4. 提交 Pull Request；GitHub 会自动检查目录和关键文件。

完整步骤见[维护指南](MAINTAINING.md)。

## 仓库结构

```text
skills/intent-compiler/
├── SKILL.md                 核心行为
├── agents/openai.yaml       Codex 展示信息
├── assets/                  原创项目视觉
└── references/              按需读取的详细规则
commands/                    快捷命令入口
examples/                    普通用户示例
.codex-plugin/               Codex 插件清单
.claude-plugin/              Claude Code 插件清单
```

## 设计原则

- 少追问，但不替用户做高影响决定。
- 内部整理需求，默认直接执行；用户要求时再展示“编译稿”。
- 补专业能力，不虚构事实或工具能力。
- 一次有针对性的自检修正，不陷入无限反思。
- 保留用户原意、授权边界、隐私和交付格式。

## 贡献与许可

欢迎提交日常工作中的失败案例和改进建议。请先看[贡献指南](CONTRIBUTING.md)。本项目采用 [MIT License](LICENSE)。

