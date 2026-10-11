<p align="center"><img src="skills/intent-compiler/assets/intent-compiler.svg" width="220" alt="Intent Compiler 原创线稿头像"></p>

# Intent Compiler｜需求编译器

**你表达想实现的结果，系统发现、检索并运用必要知识，帮助把事情做成。**

[English](README_EN.md) · [MIT License](LICENSE)

面向非技术用户的“意图驱动、知识增强的自动化工作流”。不要求用户掌握提示词工程、编程、设计、部署或素材授权术语，也不以生成更长的 Prompt 作为默认交付。

```text
理解意图 → 识别相关领域 → 按需检索 → 发现必要缺口
→ 解释关键选择 → 授权范围内执行 → 核验 → 交付
```

## 实际行为

简单文本修改直接完成，不启动完整流程。实质性任务先检查上下文与现有文件，形成简洁的执行说明，再按[知识索引](skills/intent-compiler/references/knowledge-index.md)加载：

1. 当前必需：立即读取相关模块或章节。
2. 条件触发：出现实际依赖时再读。
3. 不影响当前交付：不加载、不增加需求。

前提明确、验收可判断且没有新关键缺口时停止检索。关键资料无法访问时停止该分支，完成不受影响的工作并说明阻塞。不会编造业务数据、预算、授权、来源或完成状态。

## 三个重点场景

| 用户目标 | 主动补足 | 边界 |
|---|---|---|
| 产品渲染或制作实物 | 渲染检查模型/参考、材质、灯光、构图、输出；实物才检查尺寸、单位、材料、工艺、装配；承重/运动才继续检查功能条件 | 不把渲染升级为制造，不把漂亮图当作强度证明 |
| 编辑器字体库 | 实际字体文件、加载/失败回退、字符覆盖、具体来源与许可证、当前用途对应的权利 | 下拉菜单不等于可用字体库；“免费”不等于所有使用方式获准 |
| 网站供别人访问 | 当前技术和运行位置、后端/存储/登录/上传、公开内容、账号和部署条件、实际访问验证 | 区分本地、临时演示、正式部署、自定义域名；不默认付费，不自动购买或公开私密内容 |

价格、平台功能、许可证及地区规则在执行时查询适用权威来源，记录来源、范围和日期；静态文档不承诺具体价格、永久免费或全面合规。

## 安装与调用

推荐非程序员把仓库链接交给当前 AI，并说：“请检查当前宿主支持的安装方式，安装这个 Skill，并验证能发现它。”安装仍受宿主权限约束。

Codex CLI（已核对当前 CLI 帮助；完整安装未实测）：

```bash
codex plugin marketplace add dawwnforu/intent-compiler-skill
codex plugin add intent-compiler@intent-compiler
```

Claude Code（已核对官方文档；完整安装未实测）：

```text
/plugin marketplace add dawwnforu/intent-compiler-skill
/plugin install intent-compiler@intent-compiler
```

安装后在新会话检查 Skill 是否可见。也可复制完整的 `skills/intent-compiler` 文件夹，按宿主支持的本地 Skill 位置安装。具体路径、清单、调用差异、官方来源及验证步骤见 [COMPATIBILITY.md](COMPATIBILITY.md)。GitHub 上有仓库不等于已上架公共插件目录，也不等于所有宿主兼容。

Codex 显式调用示例：

```text
$intent-compiler do -- 给我的编辑器增加一个可切换的字体库
$intent-compiler brief -- 先整理网站上线需要什么，不执行部署
$intent-compiler teach -- 解释这个连接为什么会影响打印后的装配
$intent-compiler improve -- 检查并修好这份现有方案
```

`do` 默认执行并核验；`brief` 仅交付执行说明；`teach` 解释必要知识；`improve` 保留已有约束并改进成品。方案和教学模式不会擅自实施外部动作。Claude 插件使用带命名空间的调用，见兼容性说明。

## 能力与依赖

本项目提供 Markdown 行为规则、知识路由、场景判断、来源边界、验收与案例。路由由宿主模型遵循指令执行，不是独立程序；不能保证模型始终遵守。

真正检索、修改文件、生成图片、建模或部署，依赖宿主模型、可用专业 Skill/工具、资料访问、账号和授权。安装本项目不会提供这些软件或凭证。没有数据库、后台服务或付费 API 依赖；仓库静态检查可选用 Python 标准库，Skill 本身无需 Python。

## 验证与维护

新增[六组验证案例](examples/validation-cases.md)，覆盖渲染不扩展、实物条件、字体资源/授权、网站公开/付费边界、文本快速路径及缺少资料/工具/权限。

已进行规则与案例的静态审查；模型行为对照**未实测**，不发布提升比例。已有旧版示例中的百分比因缺少可复查原始记录而撤下。三组 raw request / 简短通用规则 / 完整 Skill 的公平执行方法和记录表见 [TESTING.md](TESTING.md)。

非程序员只需填写[知识模块模板](skills/intent-compiler/references/knowledge-module-template.md)、增加索引行和案例，无需改路由代码。详见[维护指南](MAINTAINING.md)与[贡献指南](CONTRIBUTING.md)。

仓库 CI 执行 `python tests/check_repository.py` 检查链接、包内路径、清单一致性和案例完整性；它不能证明模型行为或宿主安装成功。

## 文件入口

- [SKILL.md](skills/intent-compiler/SKILL.md)：核心行为和模式。
- [references](skills/intent-compiler/references/knowledge-index.md)：按需领域规则、知识入口、验收。
- [examples](examples/validation-cases.md)：回归案例及原有办公、设计、研究、代码示例。
- [CHANGELOG](CHANGELOG.md)：行为和兼容性变化。

用户负责表达结果；系统负责补足必要知识并执行，但不能伪造事实、创造授权、扩大需求，或把未核验结果当作完成。
