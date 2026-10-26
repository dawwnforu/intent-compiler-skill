# Intent Compiler / 需求编译器

- Original repository / 原始仓库：[dawwnforu/intent-compiler-skill](https://github.com/dawwnforu/intent-compiler-skill)
- Existing attribution / 现有署名：Intent Compiler contributors
- Copyright (c) 2026 Intent Compiler contributors
- Manifest version / 清单版本：0.2.0. This checkout is an unreleased 2.0 candidate / 当前副本是未发布的 2.0 候选版。
- License / 许可证：[standard MIT](LICENSE). Retain its copyright and permission notice in copies or substantial portions / 复制或包含实质部分时保留版权与许可声明。

These labels provide attribution and traceability, not copy protection or proof of ownership. MIT permits copying, modification, redistribution and commercial use under its conditions; redistribution alone is not evidence of infringement.

以上标识用于署名与追溯，不承诺防盗、无法复制或证明所有权。符合 MIT 条件的复制、修改、再分发及商业使用是被允许的，不自动判断为侵权。

Copy this whole folder, including this README, LICENSE, SKILL.md, references, agents, assets and scripts. Keep one candidate copy per project. Before copying over an existing project Skill, inspect its source; do not overwrite or remove it automatically. A separately installed user-level release can remain untouched, but same-name Skills do not merge and a name alone does not identify this candidate. Host installation and discovery must be checked separately from file-format validation; no universal compatibility is claimed.

独立安装时保留整个文件夹及以上材料，每个项目只留一份候选。项目内已有同名文件夹时先核对来源，不自动覆盖或删除；用户级正式版可以保持原样。同名Skill不会合并，仅凭名称不能确认选中了候选。静态格式通过不等于安装、发现或行为验证通过；其他宿主兼容性仍需实际验证。打包、平台扫描、连接交付及公开上架是不同状态，请按对应版本的发布记录核对。

## Start in an existing Codex project / 在现有Codex项目开始

Place this folder at `.agents/skills/intent-compiler/`, with SKILL.md directly inside. Start a new conversation in that project. The candidate's supported UI label is **Intent Compiler 2.0 候选 / Candidate**; hosts may display labels differently, so check the path as well. First ask:

> Read this project's `.agents/skills/intent-compiler/SKILL.md` and `SOURCE.json`. Report the resolved Skill path and sourceCommit, then use that project candidate for my tasks. If either file is missing, tell me before proceeding. Do not replace my user-level installation or choose a different same-name Skill.

把本文件夹放到项目的`.agents/skills/intent-compiler/`，确保其中直接有SKILL.md。在该项目新开对话；候选显示名称为**Intent Compiler 2.0 候选 / Candidate**，宿主显示可能不同，仍需核对实际路径。先说：

> 请读取本项目的`.agents/skills/intent-compiler/SKILL.md`和`SOURCE.json`，报告实际完整路径和sourceCommit，之后用这个项目候选处理任务。任一文件缺失先告诉我，不替换用户级安装，也不改用其他同名Skill。

Then describe your actual task in ordinary language and supply only materials you are allowed to use. No separate specialist prompt is required. SOURCE.json is added to distributed ZIPs; a source checkout without it is not a verified packaged candidate.

确认路径后直接用日常语言描述真实任务，并提供有权处理的材料，不需要另写专业提示词。SOURCE.json由分发ZIP提供；缺少该文件的源码副本不能冒充已核验的打包候选。

The Skill itself needs no account, paywall or license-validation service. Do not add obfuscation, self-destruction, hidden network access, device binding, remote disabling, tracking or unconsented uploads for copy prevention. Do not package credentials, payment details or buyer identities. Existing host/model services may have their own requirements; this folder provides no credentials or authorization.

纯本地 Skill 不新增账户、付费墙或许可证验证服务，不以防复制为由加入混淆、自毁、隐藏联网、设备绑定、远程停用、追踪或未经同意上传。代码和发布材料不包含密钥、令牌、个人收款信息或买家身份。实际工具能力和权限由宿主及用户提供。
