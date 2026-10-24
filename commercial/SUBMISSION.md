# Intent Compiler：上架候选交付

核验日期：2026-10-24（Europe/Budapest）。这里准备可审阅的商品与发布路径；尚未提交Agensi、收款、通过平台扫描或公开上架。保留标准MIT及现有贡献者署名。原始仓库：[dawwnforu/intent-compiler-skill](https://github.com/dawwnforu/intent-compiler-skill)。清单仍为0.2.0，2.0是未发布候选，候选身份以包内`SOURCE.json`的提交标识为准。

## 本周交付窗口：2026-10-24至10-25

目标是准备好可审核、可开始试用的候选；Agensi公开上架以官方页面为准，不能由本表日期推定。本周日是10月25日。**推荐首发为有限范围的免费Codex试用；15美元一次性便利包继续作为待批准、待验证的后续假设。** 免费不需要开通收款，但不自动解决许可或连接交付问题；不为赶日期先开收费。

截至10月24日，既有同线程最近收到的仍是10月12日负责人答复：可保留公开MIT仓库并挂牌；免费不要求收款；兼容范围由描述如实说明；平台副本按其更严格买方条款处理。10月21日经授权补问MIT权利、相对引用/脚本、业务产物和未发布验收，**已发送一次，尚无新答复**。这是平台说明，不是许可冲突已消除或我们已获上架批准的证据。邮件原文和发送回执留本机，不公开私人往来。

10月24日重查[条款](https://www.agensi.io/terms)，页面仍标10月18日更新；§5.2/§8仍限制保存/复制Skill，§6要求ZIP与平台审核。[创作者指南](https://www.agensi.io/learn/how-to-sell-skills-on-agensi#step-4-security-review)写常见24—48小时，邮件说通常24小时：二者都是估计，不是审核SLA。不要把“可以售卖公开MIT项目”改写成所有交付权利均已解决。

| 时间与责任 | 可执行动作 | 完成证据 / 停止条件 |
| --- | --- | --- |
| 10月24日，本分支 | 修复已复现的检查器路径缺陷；从已提交源构建新候选，核对来源、字节、完整目录和安装后工具调用；旧包冻结 | [R82](../tests/v2-resource-paths.md)的失败/修复与独立读取；不再生成已通过的客户业务题凑效果 |
| 10月24—25日，用户与平台 | 平台答复现有四个问题后，审阅下方文案与确切ZIP；由用户确认免费首发或价格、上传/审核范围；账户或协议由用户正常处理 | 无答复或未授权时不上传、不接受协议、不设置收款；不擅自追发邮件 |
| 获准的未发布审核环境 | 通过真实连接核对核心→一个相对引用→实际本地业务产物→中断恢复；可选脚本如不可执行，明确降级范围且不得声称已运行 | 保留实际加载、工具、可导出产物和失败；未能读取必要引用，不能以单个SKILL.md冒充完整产品 |
| 最迟10月25日作判断 | 门槛都通过且用户批准公开发布才执行平台步骤；拿到官方公开链接并在独立访问中确认可见 | 审核排期或门槛未解决就记录“Agensi待上架”，不标完成；GitHub固定版本免费试用可以独立进行 |
| 首批实际使用后 | 沿用[现有招募/观察](../pilot/feedback.md)邀请3位已有可用Codex的目标用户，自带有权处理的专业任务 | 记录交付合格、专业救场、质量返工、采用与帮助分钟；次日/第7天仅按实际事件填写。未授权不代联系 |

首发承诺聚焦“客户资料→可确认文件与内部执行清单”，使用共享核心；其他领域仍可探索，不写成已经验证的收费收益。免费页面可复用下方描述，价格标免费；收费描述及收入测算单独保留。本轮不合并PR、不替换正式安装、不修改MIT，且不会为日期绕过平台限制。

## 现在交付什么

一个独立Skill ZIP：根目录直接包含`SKILL.md`，并保留`references/`、`scripts/`、`agents/`、`assets/`、README、MIT及来源清单。使用已提交Git原始对象构建，排除本机缓存、历史实验、私人对话、邮件、业务文件、凭据和反馈日志。它与旧239553d试用包是不同产物，旧包不重打、不覆盖。

构建：`python commercial/build_submission.py <新的输出目录> --ref <已提交版本>`。输出的ZIP文件名包含来源提交短号，并附SHA-256校验文件；同一来源和环境再次构建应得到相同字节。脚本拒绝覆盖已有文件。来源哈希用于追溯与完整性核对，不是防复制或所有权证明。

浅克隆无法可靠追溯最后一次运行规则变化时，`runtimeCommit`留空；不要据此捏造版本。始终核对`sourceCommit`和成员哈希。本次交付使用完整历史，已核实运行方法来源。

打包检查仅覆盖文件、链接、已知凭据模式与来源字节，不是Agensi的安全扫描或完整安全审计。只有拿到平台实际结果，才可标注平台审核通过。

## 非技术用户怎样开始

1. 领取本页“GitHub候选领取入口”指向的固定版本ZIP，解压时保留全部文件。
2. 在自己的现有Codex项目中使用项目级候选：让Agent把解压内容放到`.agents/skills/intent-compiler/`，使该目录直接包含`SKILL.md`。遇到已有同名目录先检查，不覆盖；不要求替换全局安装版。
3. 在该项目新开会话，选择显示为“Intent Compiler 2.0 候选 / Candidate”的候选，并先说：“请读取本项目的`.agents/skills/intent-compiler/SKILL.md`和`SOURCE.json`，报告实际完整路径和sourceCommit，之后用这个项目候选处理任务。任一文件缺失先告诉我，不替换用户级安装，也不改用其他同名Skill。”宿主显示可能不同；同名Skill不会合并，仍核对路径，不仅凭名称判断。旧abef76f包的显示名尚未区分，保留其原快照。
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
| Codex本机项目Skill | 旧试用安装/发现、R78同模型实际工具运行与独立浏览器验收；本包解压及工具核验见R82，发现/模型业务未重跑 | 全部宿主、模型或Agensi连接都能完成同等任务 |
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

**Intent Compiler — Client Brief & Handoff / 需求编译器：客户需求与交付**

面向已有可用Codex、需要整理客户资料的自由职业者与小型团队。把零散客户消息和确认资料整理成客户可审阅的需求文件，以及分开的内部执行清单；区分已确认范围、变更请求和待定事项，在现有授权内制作、修改并核验实际文件。先聚焦这一业务路径，其他领域方法仍保留在共享核心中。

包含MIT核心、按需引用和可选本地检查脚本。原始源码公开，现有署名Intent Compiler contributors，清单0.2.0／2.0未发布候选。买家需自备Agent与模型；本机Codex已有限定测试，其他宿主及Agensi连接交付尚未完成本项目验证。不保证优于直接提问，不代发、不收款、不提供账户或模型额度。许可关系与连接验收完成后才能提交这份描述。

For freelancers and small teams who already use Codex: turn scattered client notes and confirmed materials into a reviewable client brief and a separate internal action list. Keep agreed scope, requested changes and open decisions distinct; create and check actual files within the user's authorization. Includes the public MIT core, scoped references and an optional local checker. Original source: https://github.com/dawwnforu/intent-compiler-skill — Intent Compiler contributors; manifest0.2.0, unreleased2.0 candidate. Bring your own Agent/model. Bounded local Codex testing exists; other hosts and Agensi delivery are not yet verified for this product. No guaranteed advantage over direct prompting or included one-to-one service, perpetual maintenance or model credits. Submission awaits the licence and delivery gates below.

### 当前待审字段与文件

以下内容供本人审阅和后续填写，不是已保存的平台草稿。实际字段名、字数、分类可选值尚待登录后核对。

| 字段 | 拟填内容 / 状态 |
| --- | --- |
| 标题 | Intent Compiler — Client Brief & Handoff |
| 短介绍 | Turn scattered client notes into a reviewable brief and a separate internal action list, keeping confirmed facts and open decisions distinct. |
| 分类/标签候选 | Productivity；Business & Operations；client handoff；requirements。以平台实际选项为准，不创建虚构字段 |
| 目标用户/输入 | 已有可用Codex的自由职业者与小型团队；有权处理的客户消息、已确认资料及现有交付格式 |
| 输出 | 客户可审阅的需求/确认文件＋分开的内部执行清单；格式取决于实际任务与宿主工具 |
| 首发价格 | 建议免费；**尚未批准**。15美元是后续便利包假设，不自动选用 |
| 人工服务/更新 | 不含一对一代做、模型额度或永久维护承诺；售后范围须另行确定 |
| 兼容说明 | 本机Codex有历史限定任务证据；af3d2c8包已核对获取/解压/工具。此包发现和模型业务未重跑；Claude业务、Cursor/Copilot及Agensi连接未验证 |
| 来源/署名/版本 | 本页原始GitHub仓库、Intent Compiler contributors、0.2.0／2.0未发布候选；完整标准MIT随包 |
| 主上传文件 | [intent-compiler-2.0-candidate-af3d2c8.zip](artifacts/intent-compiler-2.0-candidate-af3d2c8.zip)，37,504字节，SHA-256 `4aad2ccccaac4869f5b5b9b958b6a97e8764b0e54ed5f7ea076ba6a0961c4bc5`；来源af3d2c8，固定承载提交d4648d8 |
| 示例 | 复用[239553d历史合成摄影包](../pilot/README.md)：客户ZIP与内部执行表分开。只展示交付形态，不冒充af3d2c8或Agensi生成结果；不把旧Skill给新试用者安装 |

本机已从公开旧包原样提取`client.zip`和`internal.md`供本人审阅，文件哈希、旧来源和角色边界记录在任务本机`outputs/intent-compiler-v2/launch-handoff-r83/receipt.json`；未上传或发给任何人。客户ZIP有页面、回复单和打开说明，内部表不在其中。示例的内部资料也是合成的，仍按用途分开，不默认将内部表作为商品附件公开。

### 本轮实际入口与待授权动作

2026-10-24实际打开[Creator Dashboard](https://www.agensi.io/dashboard)：首次导航超时后检查原有标签，页面随后到达[登录页](https://www.agensi.io/auth)，显示“Sign in to your account”。只证明当前应用内浏览器会话需要登录；未推断其他浏览器账号状态，未注册、填写密码、连接新Agent或提交商品。

| 动作 | 目前能做什么 | 本人需要决定/完成什么 |
| --- | --- | --- |
| 账号入口 | 登录页已定位，现有会话断点保留 | 在网站完成现有账号登录，密码/验证码直接填网站，不发到对话 |
| 只读核对卖家界面 | 登录后核对实际字段、草稿/审核/发布流程及已有商品，避免重复创建 | 如遇协议或本人验证，由本人处理；不以浏览能力推定许可 |
| 上传 | 上传目标仅为Agensi、确切主ZIP如上；示例是否上传另行列清单 | 尚未获授权，当前不上传 |
| 提交审核 | 当前指南说审核通过后会进入公开目录；实际账号是否有独立发布开关未知 | 在实际流程明确前，把可能自动公开的审核提交按发布审阅，不能当作“只存草稿” |
| 连接验收 | 核心→引用→工具→文件保留/导出→恢复；只用合成资料 | 确认平台允许的测试路径；新连接会断开旧连接，不能擅自重配 |
| 价格和公开 | 建议免费，所有商品信息与文件先给本人审阅 | 免费/付费选择、确切上传及公开范围均需本人明确；已有对应授权不重复问 |

平台问题分项：MIT保留及公开仓库可挂牌是既有答复；更严格条款如何适用MIT、引用/脚本提供、业务成果导出、未发布测试仍待10月21日补问答复。本轮邮件线程及域名检索均未发现新回复，未追发。审核后是否自动公开另由实际界面/平台说明确认，不把这一点说成已在旧补问里回答。公开指南与当前[条款](https://www.agensi.io/terms)是平台声明，不替代本产品的连接运行证据。

## 公开上架前剩余动作

| 门槛 | 当前状态 | 下一步与证据 |
| --- | --- | --- |
| 来源与包 | 当前af3d2c8包已推送，程序化获取、字节/来源、解压和安装后工具检查通过；本包浏览器下载/发现/模型业务未重验 | 使用下方固定提交入口；旧包的浏览器和发现证据不转移，外部收件与采用另记 |
| MIT与渠道许可 | 标准MIT保留；公开条款仍有复制/保存限制 | 明确平台条款如何保留原MIT材料的权利、商业/客户用途及通知；未明确不提交，免费也不视为自动解决 |
| 连接交付 | 未上传/未连接 | 在获准审核或草稿环境检查核心→索引→引用→工具→成果→恢复；不能要求Agent违反平台条款导出Skill文件 |
| 商品扫描与审核 | 未执行 | 经用户批准上传确切ZIP，保留平台实际扫描及人工结果；本地检查不能替代 |
| 收款资格 | 未核实账户实际资格 | 用户自行提供实际经营/收款地区状态，在官方流程完成适用验证；不用时区推断，不索取密码或私钥 |
| 发布与试价 | 未获本轮发布授权，未成交 | 用户审阅描述、价格、权限及成本后批准实际提交；取官方公开链接后才标已上架 |

平台需确认的最小技术问题：相对路径引用如何提供给Agent；可选脚本是否可执行且无需保存受限Skill文件；用户生成的业务文件能否正常保留/导出；未发布环境能否进行上述测试及更新/恢复。这些已在10月21日获准的同线程补问中发送，等回复，不重复发信。不要为“跑通”关闭安全限制或擅自重配现有连接。

## GitHub候选领取入口

[领取当前候选ZIP：af3d2c8（固定文件页）](https://github.com/dawwnforu/intent-compiler-skill/blob/d4648d8375456fe7a11c29d9f498a98573c03040/commercial/artifacts/intent-compiler-2.0-candidate-af3d2c8.zip) · [SHA-256文件](https://github.com/dawwnforu/intent-compiler-skill/blob/d4648d8375456fe7a11c29d9f498a98573c03040/commercial/artifacts/intent-compiler-2.0-candidate-af3d2c8.zip.sha256)

来源/运行文件提交`af3d2c80e37e77b03d661fd803422f949d04ee89`，承载提交`d4648d8375456fe7a11c29d9f498a98573c03040`。37,504字节、25成员，SHA-256：`4aad2ccccaac4869f5b5b9b958b6a97e8764b0e54ed5f7ea076ba6a0961c4bc5`。新包修复可选HTML检查器的UNC/根路径/盘符误探测，并同步该工具限制说明；核心、路由、标准MIT与显示字段不变。独立重建字节、新项目全部解压成员及安装后检查器五项测试通过；初始验收器把LF/CRLF许可证比较成不同的失败已保留，修正的是验收器，未改许可证。[R82证据](../tests/v2-resource-paths.md)。本包尚无新的宿主发现、模型业务、浏览器下载或外部收件验证，不能沿用旧包的分项结论。

### 旧2881c73候选保持冻结

[旧候选ZIP：2881c73](https://github.com/dawwnforu/intent-compiler-skill/blob/7801146aec0353051dcb14060ea64fb724fe50d6/commercial/artifacts/intent-compiler-2.0-candidate-2881c73.zip)

来源提交`2881c7331e0e9de156317ac98d03a5b9afa4a4ff`，承载提交`7801146aec0353051dcb14060ea64fb724fe50d6`；运行方法来源仍为`f51b2ccb7d1ca7b3a5e6e58dcb202b672d1399ed`。37,426字节、25成员，SHA-256：`53615833bbee2ab5f1ad6d123e6c9972a46a67e3bea94b93b0118f98e40df634`。新包只改双语包内启动说明和宿主已有显示名字段，核心及方法不变。以上是候选身份，不是新的正式版本号或平台审核结论。

新包实际解压字节、继承用户配置的同名发现及一次明确路径启动通过；前后两个同名条目均启用，候选新标签可区分。模型额外尝试业务项目Git HEAD失败的记录保留，不影响来源字段读取，但不能称启动毫无摩擦。已从固定承载提交程序化取得新包，37,426字节、Git blob、SHA-256及25成员与本地构建一致。尚无本包浏览器下载或外部收件证据，不沿用旧包的下载结论。

[旧abef76f候选](https://github.com/dawwnforu/intent-compiler-skill/blob/cdb385d87c189cfe162ba23df9ebc2a9e66f97af/commercial/artifacts/intent-compiler-2.0-candidate-abef76f.zip)保持冻结；R79曾实际程序化获取和浏览器下载36,403字节并核对哈希，其承载提交CI通过。旧239553d摄影包也不重打。各自安装、发现、下载与外部用户状态见[分项记录](../tests/v2-submission-candidate.md)。
