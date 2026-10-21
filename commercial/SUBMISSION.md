# Intent Compiler：上架候选交付

核验日期：2026-10-21。这里准备可审阅的商品与发布路径；尚未提交Agensi、收款、通过平台扫描或公开上架。保留标准MIT及现有贡献者署名。原始仓库：[dawwnforu/intent-compiler-skill](https://github.com/dawwnforu/intent-compiler-skill)。清单仍为0.2.0，2.0是未发布候选，候选身份以包内`SOURCE.json`的提交标识为准。

## 现在交付什么

一个独立Skill ZIP：根目录直接包含`SKILL.md`，并保留`references/`、`scripts/`、`agents/`、`assets/`、README、MIT及来源清单。使用已提交Git原始对象构建，排除本机缓存、历史实验、私人对话、邮件、业务文件、凭据和反馈日志。它与旧239553d试用包是不同产物，旧包不重打、不覆盖。

构建：`python commercial/build_submission.py <新的输出目录> --ref <已提交版本>`。输出的ZIP文件名包含来源提交短号，并附SHA-256校验文件；同一来源和环境再次构建应得到相同字节。脚本拒绝覆盖已有文件。来源哈希用于追溯与完整性核对，不是防复制或所有权证明。

浅克隆无法可靠追溯最后一次运行规则变化时，`runtimeCommit`留空；不要据此捏造版本。始终核对`sourceCommit`和成员哈希。本次交付使用完整历史，已核实运行方法来源。

打包检查仅覆盖文件、链接、已知凭据模式与来源字节，不是Agensi的安全扫描或完整安全审计。只有拿到平台实际结果，才可标注平台审核通过。

## 非技术用户怎样开始

1. 领取本页“已发布候选入口”指向的固定版本ZIP，解压时保留全部文件。
2. 在自己的现有Codex项目中使用项目级候选：让Agent把解压内容放到`.agents/skills/intent-compiler/`，使该目录直接包含`SKILL.md`。遇到已有同名目录先检查，不覆盖；不要求替换全局安装版。
3. 新开会话，先说：“请报告这次实际采用的intent-compiler/SKILL.md完整路径和SOURCE.json来源提交；使用这个项目候选处理我的任务。”若路径指向旧版，先修正选用路径，不重复安装。
4. 用自己的语言说明用途并提供有权处理的资料。例如：“帮我把这些客户消息整理成客户能确认的交付文件和内部执行清单，还没确定的标出来，先不要发给客户。”不要求先写专业提示词。
5. 检查并修改实际成果，按[既有反馈方式](../pilot/feedback.md)记录是否采用、专业救场、质量返工及帮助时间。模型等待和业务补充分别记录。

旧摄影样例可用于熟悉流程，不能代替真实使用价值；使用其素材时不要用旧样例包中的Skill覆盖本候选。[旧试用说明](../pilot/README.md)继续保留其原版本限制。

## 要部署哪些服务

当前产品是Markdown工作流与可选本地只读检查脚本，在买家的Agent中运行。GitHub保存源码和候选包；不需要为售卖这个Skill新增服务器、用户数据库、域名、后台账号或许可证验证服务。买家自行提供可用Agent、模型和任务所需工具/权限；包不含模型额度。

Agensi是另一条交付通道。[创作者指南](https://www.agensi.io/learn/how-to-sell-skills-on-agensi)要求提交含SKILL.md的ZIP及支持材料；[当前条款](https://www.agensi.io/terms)规定通过Agent连接交付、平台审核及付费卖家的收款准备。2026-10-18条款优先于旧指南中“免费也必须收款设置”的说法；不要替用户开通收款、接受条款或连接新账号。

[连接指南](https://www.agensi.io/docs/mcp-setup)说明更换连接应用会断开原连接。上传包可被读取不等于`references`和可选脚本已通过连接运行；按下面验收，不新建自有代理服务来绕过未知。

## 支持范围与有效性

| 项目 | 已有证据 | 尚不能声称 |
| --- | --- | --- |
| Codex本机项目Skill | 旧试用安装/发现、R78同模型实际工具运行与独立浏览器验收；本包安装/发现另行留档 | 全部宿主、模型或Agensi连接都能完成同等任务 |
| 专业交付 | R70/R71客户材料，R76印刷通知，R78交互微调均有真实产物及限定检查 | 这些任务均优于原始请求；历史不同版本的统一提升率 |
| 局部改善 | R78条件性选择入口方法，R62恢复及R67独立回忆等各有自己的证据范围 | 更少专业提示/返工已获用户验证、稳定省token或绝对安全 |
| Claude Code | 既有项目安装可发现，业务受认证/第三方路由阻塞 | Anthropic模型业务验证通过 |
| Cursor / Copilot / Agensi | 未完成本项目业务交付验证 | 仅凭共同格式就写“全面兼容” |

完整结果及失败见[决策](../docs/v2-decision.md)、[结果](../docs/v2-results.md)和[测试范围](../TESTING.md)。R78候选维修表单分隔符缺陷、混合成本及基线额外功能继续保留。没有外部采用、复用或付费证据。

## 定价建议：区分公开核心与付费便利

GitHub核心继续免费MIT。若许可和连接交付均解决，建议先把**15美元一次性**作为小规模商品的试价假设，范围仅为整理好的工作流及接入便利，不承诺人工一对一、模型额度、永久维护或结果提升。15美元尚未获批或实测，不是市场估值。服务型产品单独评估，不能把79美元服务假设混入本商品。

2026-10-21实际浏览器查看两个公开商品：

| 可比页面 | 挂牌价 | 能说明什么 |
| --- | ---: | --- |
| [Client Proposal & Scope Optimization Master](https://www.agensi.io/skills/client-proposal-scope-optimization-master) | $5 | 同类报价信息；页面显示尚无评价，销量和质量未验证 |
| [Agency Proposal & Scope Builder](https://www.agensi.io/skills/agency-proposal-scope-builder) | $15 | 同上；不是本项目愿付价格或销售预测 |

旧19美元“场景维护包”条件模型及其负结果保持，不悄悄替换假设；15美元是本页不含人工或长期维护承诺的接入便利包试价，两种产品不能混成一项。按平台当前30%份额，15美元无退款时作者应计份额10.50美元；退款率假设10%时为9.45美元，尚未扣工具、人工、税费或固定成本，也不是实际到账。此处仅取当前公开条款的结算结构，不预测成交。

在原模型其他假设不变（激活后付费15%、退款10%、人工20美元/小时及相同工具/退款处理成本）时，15美元的每位激活支持时长门槛：每单售后20分钟约0.79分钟，每单售后5分钟约3.04分钟；必须低于门槛才有正变动贡献，还未覆盖固定投入。若需要代做，低价不能解决亏损；没有真实支持数据前不扩大收费。

[15美元30/90天条件情景](launch-15-scenarios.json)复用原漏斗和全部非价格假设，包含零成交、现金与人工时间、结算前应计及空的实际到账字段。这些情景经济结果仍均为负；不能靠降低价格就宣布盈利，也不能把假设负值写成产品必亏。正式付费试点要等实际交付价值和支持负担证据。

先观察实际任务采用，再问愿意为何付费。通过价格页/试用/激活/付款/退款分别记录，不能用口头意愿或其他创作者的销量替代自己的订单。沿用[收入模型](README.md)和既有三人试用记录，不增加另一套问卷。

## 可粘贴商品描述（审批草案）

**Intent Compiler — Guided Professional Workflows / 需求编译器**

面向已有Codex的非技术用户，把日常语言和已有文件变成具体可检查的成果。按任务加载相关专业方法，区分已确认事实、必要条件和待决定事项，在当前权限内制作、修改并核验交付物。适用于客户资料整理、交互原型和可打印文件等有明确验收标准的任务。

包含MIT核心、按需引用和可选本地检查脚本。原始源码公开，现有署名Intent Compiler contributors，清单0.2.0／2.0未发布候选。买家需自备Agent与模型；本机Codex已有限定测试，其他宿主及Agensi连接交付尚未完成本项目验证。不保证优于直接提问，不代发、不收款、不提供账户或模型额度。许可关系与连接验收完成后才能提交这份描述。

For nontechnical users who already use Codex: turn ordinary-language goals and existing files into concrete, checkable deliverables. The workflow loads relevant domain methods, keeps facts and pending decisions distinct, and executes within the user's actual authorization. Includes the public MIT core, scoped references and an optional local checker. Original source: https://github.com/dawwnforu/intent-compiler-skill — Intent Compiler contributors; manifest0.2.0, unreleased2.0 candidate. Bring your own Agent/model. Bounded local Codex testing exists; other hosts and Agensi delivery are not yet verified for this product. No guaranteed advantage over direct prompting or included human service/model credits. Submission awaits the licence and delivery gates below.

## 公开上架前剩余动作

| 门槛 | 当前状态 | 下一步与证据 |
| --- | --- | --- |
| 来源与包 | ZIP已推送；程序化获取、实际浏览器下载及新项目安装/发现通过 | 使用下方固定提交入口；外部用户收件与业务采用另记，不能由本机检查代替 |
| MIT与渠道许可 | 标准MIT保留；公开条款仍有复制/保存限制 | 明确平台条款如何保留原MIT材料的权利、商业/客户用途及通知；未明确不提交，免费也不视为自动解决 |
| 连接交付 | 未上传/未连接 | 在获准审核或草稿环境检查核心→索引→引用→工具→成果→恢复；不能要求Agent违反平台条款导出Skill文件 |
| 商品扫描与审核 | 未执行 | 经用户批准上传确切ZIP，保留平台实际扫描及人工结果；本地检查不能替代 |
| 收款资格 | 未核实账户实际资格 | 用户自行提供实际经营/收款地区状态，在官方流程完成适用验证；不用时区推断，不索取密码或私钥 |
| 发布与试价 | 未获本轮发布授权，未成交 | 用户审阅描述、价格、权限及成本后批准实际提交；取官方公开链接后才标已上架 |

平台需确认的最小技术问题：相对路径引用如何提供给Agent；可选脚本是否可执行且无需保存受限Skill文件；用户生成的业务文件能否正常保留/导出；未发布环境能否进行上述测试及更新/恢复。不要为“跑通”关闭安全限制或擅自重配现有连接。

## 已发布候选入口

[领取独立候选ZIP：abef76f（固定提交文件页）](https://github.com/dawwnforu/intent-compiler-skill/blob/cdb385d87c189cfe162ba23df9ebc2a9e66f97af/commercial/artifacts/intent-compiler-2.0-candidate-abef76f.zip) · [直接下载](https://github.com/dawwnforu/intent-compiler-skill/raw/cdb385d87c189cfe162ba23df9ebc2a9e66f97af/commercial/artifacts/intent-compiler-2.0-candidate-abef76f.zip) · [固定SHA-256文件](https://github.com/dawwnforu/intent-compiler-skill/blob/cdb385d87c189cfe162ba23df9ebc2a9e66f97af/commercial/artifacts/intent-compiler-2.0-candidate-abef76f.zip.sha256)

来源提交`abef76fae0056073a09e2a95b866050049b2c613`，运行方法来源`f51b2ccb7d1ca7b3a5e6e58dcb202b672d1399ed`；36,403字节、25个成员。SHA-256：`24bfdec81a303ec4d9e852d436363eb11129f9ad7887c54004da0ed5b714a490`。这些是构建产物身份，不是已发布版本号或平台审核结论。

承载提交为`cdb385d87c189cfe162ba23df9ebc2a9e66f97af`，与包内来源提交不同。已从该固定提交程序化取得实际文件；浏览器点击Download raw file也获得下载事件与实际保存文件，二者字节和SHA-256均与本地构建一致。该提交远端Repository integrity工作流通过。外部用户是否收到、安装或采用仍未验证，不能由作者侧下载代替。

实际解压、安装字节、宿主发现已分项检查；运行文本与R78按CRLF/LF归一后相同，不能写成历史工作树快照逐字节相同。[候选交付记录](../tests/v2-submission-candidate.md)保留检查范围和失败。旧239553d摄影试用ZIP保持原样。
