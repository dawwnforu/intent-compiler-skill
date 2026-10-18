# 本轮试用兼容状态（2026-10-19）

共享核心是清单0.2.0／2.0未发布候选，核心固定于6d18460。这里的“安装”指在隔离的新项目复制完整文件夹，没有替换个人或正式安装。

| 宿主 | 安装／发现与触发 | 引用与实际工具 | 权限与交付 | 恢复／限制 |
|---|---|---|---|---|
| Codex CLI 0.163.0-alpha.10.2，gpt-6.1-sol/low | 从实际试用ZIP向新项目安装24个文件，重新发现且只启用目标Skill；`$intent-compiler` 显式读取已验 | 实际读核心、知识索引、knowledge-organization、source-policy、quality-check；shell/Python生成已记录 | 经批准的外层启动；子进程workspace-write、禁网；合成客户ZIP与内部表已做文件/独立收件副本HTTP验收 | 本轮会话恢复、真实用户手动安装、GUI及所有模式未验；浏览器控制连接中断，未完成视觉验收 |
| Claude Code 2.1.201 | 项目 `.claude/skills/intent-compiler` 实际复制，初始化清单出现skill及slash入口 | 尚未进入实际工具执行 | auth status显示已登录，但业务请求返回401；不能宣称任务兼容 | 命令请求sonnet，实际初始化报告deepseek-v4-pro[1M]，不是已验证的Anthropic Sonnet；恢复、引用加载与交付未验 |
| Cursor／GitHub Copilot | 本轮未找到可调用的对应CLI，不安装新软件 | 未验 | 不宣称支持，不把通用Markdown当适配结果 | 先完成首批用户在Codex路径，再按真实用户宿主需求决定扩展 |
| Agensi Agent连接 | 未连接、未上传 | 引用文件及可选脚本加载未验 | 本地ZIP试用不等于平台交付；许可关系待确认 | 不宣称上架或连接兼容 |

Claude 的PowerShell包装脚本受当前执行策略阻止；使用已安装的官方`.cmd`入口能读取版本和启动，不改变执行策略。但本地“已登录”不证明远端凭据有效，也不证明请求解析到期望模型。没有更换凭据、提供商或绕过权限。

Codex 官方项目路径见[Build skills](https://learn.chatgpt.com/docs/build-skills)；Claude 项目路径见[Skills](https://code.claude.com/docs/en/skills)。文档描述与实际测试分开；不能由格式检查或其他宿主的结果推断本宿主成功。需要工具、模型和账户已经可用；本包不会替你配置付款或提供访问权。
