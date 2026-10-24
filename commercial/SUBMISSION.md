# Intent Compiler：上架候选交付

核验日期：2026-10-24（Europe/Budapest）。**用户亲自提交审核后，Agensi已将现有af3d2c8候选批准并免费公开**：[正式商品页](https://www.agensi.io/skills/intent-compiler-client-brief-handoff)。Creator Studio为1 Live、0 Pending；只读接口为`review_status: live / security_status: approved`；无Cookie或Authorization的HTTP请求返回200；一次固定产品名搜索返回本商品。没有代点再次发布或重复提交。上架不等于完整业务交付已验证；当前安装、评价、外部试用和订单均为0，未收款。标准MIT及贡献者署名不变。原始仓库：[dawwnforu/intent-compiler-skill](https://github.com/dawwnforu/intent-compiler-skill)。平台条目版本1.0与包内清单0.2.0／未发布稳定2.0的候选身份分开标注，完整来源以`SOURCE.json`为准。

本轮先修正公开介绍遗留的“仅草稿、未审核或公开”状态；随后用户明确批准免费启用与合成业务验收。页面显示“Security scan passed with 1 warning”；尚未取得警告详情，不宣称零警告或完整安全审计。没有替换ZIP、改价或提交新版本。本机R92保存实际接口、搜索、匿名访问、文案前后值和截图；web读取工具失败但浏览器/匿名HTTP成功，不能误报站点不可访问。

**[R92真实交付结果](../tests/v2-agensi-delivery.md)：** 现有Codex/Agensi实际加载核心、SOURCE及任务引用，独立渠道文本核对一致。首次生成的中文正文和文件名被PowerShell文本管道损坏，模型自测仍报通过；保留失败，停止原定第二条时间变更。剩余一次调用明确用于开发者编码救场：修复包经独立读取、实际Python解压、隐私和浏览器检查通过。两次模型调用合计355.53秒、13,757输出tokens，不是现金账单或每单支持数据。开发者专业救场1次，用户实际提示/返工需求未知，外部试用仍为0。原线程恢复、继续修改、可选脚本渠道执行及原生应用操作未验。本分支只给现有质量引用补上具体UTF-8与独立原文核验方法，未上传；不能把修复结果冒充原包无干预成功。公开介绍、兼容说明、限制及FAQ据此更新，保留失败和人工帮助。

**[R93–R94续验](../tests/v2-agensi-continuation.md)：** 复用R92修复产物，不重新生成已通过的初稿。实际中断时内部表已改下午、客户ZIP仍是上午；R93评测器误用磁盘恢复接口而失败。仅修正客户端调用后，R94在原仍加载的临时会话继续，最终客户包与内部表一致，保留其他约定、待定事项及本轮用户来源，独立文件/解压/浏览器检查通过。共3次调用、203.20秒、4,550输出tokens，失败不删除；不是进程重启恢复、无干预首交或减少专业提示的证据。完整MIT、SVG及脚本内容已能经连接读取并匹配原包，脚本执行未验。本轮没有追加Skill规则、上传业务文件或替换商品包。

**[R95新段落的定向回归](../tests/v2-encoding-regression.md)：** 在本地隔离项目用确切cefba82包做一次已曝光R92首交任务，没有追加编码提示。实际读取新方法，生成中文客户ZIP和独立内部表；开发者另行字节/操作、语义和桌面浏览器检查通过。1次调用、126.23秒、5,118输出tokens；与Agensi加载条件不同，不是因果提升、渠道新包或用户少返工的证据。更新预览已据此准确补充；未提交审核，原公开包不变。商业页旧“当前未发布”已改为区分现有免费版、未审核更新与未启用收费方案；未取得用户支持时间，收入参数不变。

## 本周交付窗口：2026-10-24至10-25

目标是准备好可审核、可开始试用的候选；Agensi公开上架以官方页面为准，不能由本表日期推定。本周日是10月25日。**推荐首发为有限范围的免费Codex试用；15美元一次性便利包继续作为待批准、待验证的后续假设。** 免费不需要开通收款，但不自动解决许可或连接交付问题；不为赶日期先开收费。

R93已重新成功读取原邮件线程（4封）并定向检索负责人10月21日后的来信，未见新答复；最近收到仍为10月12日，21日补问只发送一次。R92曾遇服务限流，保留该失败，不把它当成当时无回复的证据。既有答复允许公开MIT仓库挂牌、免费无须收款及如实说明兼容；渠道副本更严格条款如何适用MIT仍未明确。实际批准不消除该问题，未追发、未改凭据，私人邮件留本机。

10月24日再次重查[条款](https://www.agensi.io/terms)，页面现标10月23日更新；§5.2/§8买方保存/复制限制仍在，创作者可下载自己的Skill；更新须审核，批准后下次加载使用新版。§6.6的首次使用通知排除作者，不提供买方邮箱，也不等于研究同意或采用。当前收款条件另见[商业记录](README.md)，不沿用旧“按月”结算说法；不接受新协议或设置收款，不据此认定MIT关系已解决。

| 时间与责任 | 可执行动作 | 完成证据 / 停止条件 |
| --- | --- | --- |
| 10月24日，本分支 | 修复已复现的检查器路径缺陷；从已提交源构建新候选，核对来源、字节、完整目录和安装后工具调用；旧包冻结 | [R82](../tests/v2-resource-paths.md)的失败/修复与独立读取；不再生成已通过的客户业务题凑效果 |
| 10月24日，用户与平台 | 用户亲自提交后平台已批准、免费公开；实际页面、只读状态和匿名访问已验 | Agent未重复提交、启用、接受协议或设置收款；用户自行提交不等于其他外部操作的许可，不擅自追发邮件 |
| 已获准的本商品连接验收 | R92首交失败及专业修复保留；R93失败、R94同会话中断/继续分别记录，限定流程已有证据 | 停止模型调用，不重跑已通过任务；进程重启、脚本执行及真实用户效果仍未验 |
| 最迟10月25日作判断 | 公开可见门槛已通过；接下来按真实连接交付证据决定是否引导首批用户使用该渠道 | 完整交付未验就明确保留；GitHub固定版本免费试用可独立进行，不把挂牌算作用户采用 |
| 首批实际使用后 | 沿用[现有招募/观察](../pilot/feedback.md)邀请3位已有可用Codex的目标用户，自带有权处理的专业任务 | 记录交付合格、专业救场、质量返工、采用与帮助分钟；次日/第7天仅按实际事件填写。未授权不代联系 |

首发承诺聚焦“客户资料→可确认文件与内部执行清单”，使用共享核心；其他领域仍可探索，不写成已经验证的收费收益。免费页面可复用下方描述，价格标免费；收费描述及收入测算单独保留。本轮不合并PR、不替换正式安装、不修改MIT，且不会为日期绕过平台限制。

## 现在交付什么

一个独立Skill ZIP：根目录直接包含`SKILL.md`，并保留`references/`、`scripts/`、`agents/`、`assets/`、README、MIT及来源清单。使用已提交Git原始对象构建，排除本机缓存、历史实验、私人对话、邮件、业务文件、凭据和反馈日志。它与旧239553d试用包是不同产物，旧包不重打、不覆盖。

更新预览包为`intent-compiler-2.0-candidate-cefba82.zip`：37,716字节、25成员，来源/runtime提交`cefba82343fef6512a31f96013fc20793f878dd5`，SHA-256 `7bc4ba9400c1b604aca9cd7c787a322df47641b0c4d3a64b93e51d4638d7cb61`。实际成员均匹配提交对象，只与现有上架包的SOURCE和质量核验段落不同；MIT/清单不变。文件留任务本机`outputs/intent-compiler-v2/continuation-r93/candidate/`。用户另行明确批准此包上传和更新预览；现有商品替换控件已显示新文件及SKILL.md识别成功，变更说明和预览已填写。平台自动生成的TypeScript示例及虚构测试通过描述已清除，没有上传业务样例。

**停在审核前：**页面仅提供“Resubmit / Save & Resubmit for Review”，没有单独保存更新按钮，未点击；不能声称刷新后可恢复草稿。已保留打开的预览及本机`continuation-r94/update-preview.json`、文本和截图，R95本地结果的字段补充另存`encoding-r95/update-preview.json`。公开页重新读取仍为af3d2c8；独立只读MCP返回live/approved/Free、版本1.0、`pending_update: null`、安装0。当前公开包、领取默认版、MIT和价格不变；新段落仅完成上述已曝光本地回归，渠道及未见迁移未验。后续提交审核不在本次上传授权内。

构建：`python commercial/build_submission.py <新的输出目录> --ref <已提交版本>`。输出的ZIP文件名包含来源提交短号，并附SHA-256校验文件；同一来源和环境再次构建应得到相同字节。脚本拒绝覆盖已有文件。来源哈希用于追溯与完整性核对，不是防复制或所有权证明。

浅克隆无法可靠追溯最后一次运行规则变化时，`runtimeCommit`留空；不要据此捏造版本。始终核对`sourceCommit`和成员哈希。本次交付使用完整历史，已核实运行方法来源。

打包检查仅覆盖文件、链接、已知凭据模式与来源字节，不是Agensi的安全扫描或完整安全审计。只有拿到平台实际结果，才可标注平台审核通过。

## 非技术用户怎样开始

1. 领取本页“GitHub候选领取入口”指向的固定版本ZIP，解压时保留全部文件。
2. 在自己的现有Codex项目中使用项目级候选：让Agent把解压内容放到`.agents/skills/intent-compiler/`，使该目录直接包含`SKILL.md`。遇到已有同名目录先检查，不覆盖；不要求替换全局安装版。
3. 在该项目新开会话，选择显示为“Intent Compiler 2.0 候选 / Candidate”的候选，并先说：“请读取本项目的`.agents/skills/intent-compiler/SKILL.md`和`SOURCE.json`，报告实际完整路径和sourceCommit，之后用这个项目候选处理任务。任一文件缺失先告诉我，不替换用户级安装，也不改用其他同名Skill。”宿主显示可能不同；同名Skill不会合并，仍核对路径，不仅凭名称判断。旧abef76f包的显示名尚未区分，保留其原快照。
4. 用自己的语言说明用途并提供有权处理的资料。例如：“帮我把这些客户消息整理成客户能确认的交付文件和内部执行清单，还没确定的标出来，先不要发给客户。”不要求先写专业提示词。
5. 检查并修改实际成果，按[既有反馈方式](../pilot/feedback.md)记录是否采用、专业救场、质量返工及帮助时间。模型等待和业务补充分别记录。

Windows上生成后先打开实际文件，确认中文与附件名正常。R92曾出现正文变问号但自测报通过；遇到同类问题请邀请人协助，记录帮助和返工，不要求用户先学编码。当前已上架ZIP尚未包含本分支新核验方法。

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
| Agensi经Codex | R92核心/引用及来源匹配通过；一例合成交付首败，开发者修复后独立文件/浏览器检查通过 | 原包无干预成功、原线程恢复或用户提示减少 |
| Cursor / Copilot | 未完成本项目业务交付验证 | 仅凭共同格式就写“全面兼容” |

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

## 商品描述与当前字段

**Intent Compiler — Client Brief & Handoff / 需求编译器：客户需求与交付**

面向已有可用Codex、需要整理客户资料的自由职业者与小型团队。把零散客户消息和确认资料整理成客户可审阅的需求文件，以及分开的内部执行清单；区分已确认范围、变更请求和待定事项，在现有授权内制作、修改并核验实际文件。先聚焦这一业务路径，其他领域方法仍保留在共享核心中。

包含MIT核心、按需引用和可选本地检查脚本。原始源码公开，现有署名Intent Compiler contributors，清单0.2.0／2.0未发布候选。买家需自备Agent与模型；本机Codex已有限定测试，其他宿主及Agensi连接交付尚未完成本项目验证。不保证优于直接提问，不代发、不收款、不提供账户或模型额度。Agensi现已将此包免费公开，平台条目版本1.0；完整连接验收与MIT渠道条款澄清仍待完成。

For freelancers and small teams who already use Codex: turn scattered client notes and confirmed materials into a reviewable client brief and a separate internal action list. Keep agreed scope, requested changes and open decisions distinct; create and check actual files within the user's authorization. Includes the public MIT core, scoped references and an optional local checker. Original source: https://github.com/dawwnforu/intent-compiler-skill — Intent Compiler contributors; manifest0.2.0, unreleased2.0 candidate. Bring your own Agent/model. Bounded local Codex testing exists; other hosts and Agensi delivery are not yet verified for this product. No guaranteed advantage over direct prompting or included one-to-one service, perpetual maintenance or model credits. Now listed free on Agensi (listing version1.0); connected delivery and MIT/channel clarification remain open.

### 当前公开字段与文件

下述标题、摘要、用途、来源、兼容说明、工具条件、权限说明、分类、限制和三项FAQ已填写并保存；R92又将实际失败与修复范围同步到介绍/兼容/限制/FAQ。名称上限60字符，ZIP上传上限50MB，必须含SKILL.md；实际选用Business & Operations为主分类、Productivity为第二分类。页面通用兼容标志不是产品验证。早期草稿的“Not scanned yet”保留为历史；当前公开页的实际扫描状态与1条警告以本页开头为准。

平台自动生成过未经实测的S3演示及“优于直接提示”的宣传，已整体清除，未用作证据。演示字段暂空，未上传客户样例、内部执行表或其他媒体。早期桌面预览在窄侧栏把标题挤成竖排，移动预览可读；本轮公开页标题可读。文件树显示平台`v1.0`，实际来源/清单为`0.2.0／2.0候选`，未发现网页可编辑的版本字段；公开介绍现已明确区分二者，没有重传包或编造新源版本。

| 字段 | 拟填内容 / 状态 |
| --- | --- |
| 标题 | Intent Compiler — Client Brief & Handoff |
| 短介绍 | Turn scattered client notes into a reviewable brief and a separate internal action list, keeping confirmed facts and open decisions distinct. |
| 分类/标签候选 | Productivity；Business & Operations；client handoff；requirements。以平台实际选项为准，不创建虚构字段 |
| 目标用户/输入 | 已有可用Codex的自由职业者与小型团队；有权处理的客户消息、已确认资料及现有交付格式 |
| 输出 | 客户可审阅的需求/确认文件＋分开的内部执行清单；格式取决于实际任务与宿主工具 |
| 首发价格 | 用户亲自提交的Free条目已获平台批准并公开；15美元仍为后续便利包假设，不自动改价或设置收款 |
| 人工服务/更新 | 不含一对一代做、模型额度或永久维护承诺；售后范围须另行确定 |
| 兼容说明 | 本机Codex历史证据保留；af3d2c8渠道核心/引用及一次曝光修复已验，首交失败、继续修改/恢复未验。Claude业务、Cursor/Copilot未验证；不作无干预成功声明 |
| 来源/署名/版本 | 本页原始GitHub仓库、Intent Compiler contributors、0.2.0／2.0未发布候选；完整标准MIT随包 |
| 主上传文件 | [intent-compiler-2.0-candidate-af3d2c8.zip](artifacts/intent-compiler-2.0-candidate-af3d2c8.zip)，37,504字节，SHA-256 `4aad2ccccaac4869f5b5b9b958b6a97e8764b0e54ed5f7ea076ba6a0961c4bc5`；来源af3d2c8，固定承载提交d4648d8 |
| 示例 | 复用[239553d历史合成摄影包](../pilot/README.md)：客户ZIP与内部执行表分开。只展示交付形态，不冒充af3d2c8或Agensi生成结果；不把旧Skill给新试用者安装 |

### 用户提交后的历史回执（R90，随后已上线）

2026-10-24用户告知已点击Submit for review。实际Creator Studio显示本商品“Pending Review / In review / Free”，总计1、Live 0、Pending 1。现有OAuth只读`my_skills({status:"pending"})`独立返回同名唯一条目：`review_status: pending`、`security_status: pass`、`rejection_reason: null`、`pricing: Free`、`version: 1.0`、`installs: 0`、`pending_update: null`，创建时间为`2026-10-24T13:27:46.435994+00:00`。此pass为真实接口状态，与先前空白预览的假定扫描标签不同；没有取得逐项扫描明细，也不代表完整安全审计或人工批准。

平台分配slug `intent-compiler-client-brief-handoff`及[商品地址](https://agensi.io/skills/intent-compiler-client-brief-handoff)，尚未验证未登录公开访问或实际Skill交付。待审条目仍为平台版本1.0；包内清单0.2.0和完整来源未变，不能合并成同一个版本结论。没有通过重新上传、重复提交或更新版本接口来处理差异。此前启用测试的确认仍未得到回答；本次只读核对不绕过R89的启用动作审批拒绝。

上述为R90待审时点，保留其原始响应和截图；最新状态以本页开头R92实际上线核验为准。没有新建目标、商品、账户或安装版本，亦未代发邮件。

本机已从公开旧包原样提取`client.zip`和`internal.md`供本人审阅，文件哈希、旧来源和角色边界记录在任务本机`outputs/intent-compiler-v2/launch-handoff-r83/receipt.json`；未上传或发给任何人。客户ZIP有页面、回复单和打开说明，内部表不在其中。示例的内部资料也是合成的，仍按用途分开，不默认将内部表作为商品附件公开。

### 本轮实际入口与待授权动作

2026-10-24实际打开[Creator Dashboard](https://www.agensi.io/dashboard)：首次导航超时后检查原有标签，页面随后到达[登录页](https://www.agensi.io/auth)，显示“Sign in to your account”。只证明当前应用内浏览器会话需要登录；未推断其他浏览器账号状态，未注册、填写密码、连接新Agent或提交商品。

**同日后续更新：**用户已完成登录，明确批准启用Creator Mode及添加Agensi连接，并亲自完成OAuth Allow。Creator Studio已出现；Codex命令返回“Successfully logged in”，平台显示“Codex Connected”；经现有本机Codex实际调用只读`my_library({})`成功，返回技能库为空。没有模型生成、购买、上传或提交。实际[提交页](https://www.agensi.io/dashboard/submit)已只读检查，未填写；页面“Draft”标签不代表已保存草稿。原生目标仍显示blocked，不代表登录或连接仍失败。

**随后获准的预览操作：**用户明确批准上传af3d2c8现有ZIP并填写介绍，停在Submit for review之前。上传前再次核对37,504字节和本页SHA-256；页面识别25文件、18个references及原LICENSE/来源文件。出现独立草稿URL及“All changes saved”，刷新后同一草稿、ZIP名称、完整介绍、权限、分类和三项FAQ仍在。只有本候选ZIP及商品字段传给Agensi；没有点击审核/公开，也未新增媒体或替换正式安装。本机R88记录保留具体草稿URL、字段读取、截图和失败操作，不公开账号草稿标识。平台自动生成文案曾触发，不能把“本机Codex模型调用0次”说成平台未运行生成。

已发现的Agensi MCP工具描述另提供`submit_skill`预览接口：不传`confirm`会接收文本文件并返回暂存7天的`draft_id`，`confirm:true`才提交审核。这只是已发现的接口说明，**尚未调用，也未验证未发布交付或持久化**；生成远端预览仍会传输文件，必须先获上传授权。不能因工具可用而自动执行。

| 动作 | 目前能做什么 | 本人需要决定/完成什么 |
| --- | --- | --- |
| 账号入口 | 已登录、Creator Mode已启用、Codex OAuth与只读技能库调用成功 | 此步骤无需再次授权或登录；不重新配置连接 |
| 核对卖家界面 | 已有1个Live商品，profile、上传、批准三项完成；普通编辑器的元数据修正已保存并在公开页确认 | 不重复建立商品、上传或审核；如遇协议或本人验证，由本人处理 |
| 上传 | 已获授权且已上传上述确切ZIP；同一草稿经刷新确认保存 | 无需重复授权或上传；示例/媒体仍未上传，不自动追加业务资料 |
| 提交审核 | 用户亲自提交后已获平台批准，状态live/approved，公开页可见；Agent未重复操作 | 无需再次提交或公开；保留1条扫描警告详情未知的限制 |
| 连接验收 | 启用已获准；核心/引用和本地产物、R94同会话中断/继续已运行，R92首败及专业修复保留 | 无需再次问既有启用；停止追加抽样，进程重启、脚本执行、其他宿主及真实采用未验 |
| 价格和公开 | 实际Free、已公开；平台显示0安装 | 不自动改收费、不设置收款、不用自己激活冒充外部试用 |

平台问题分项：MIT保留及公开仓库挂牌为既有答复；完整通知、引用/资源/脚本的技术读取已有实际证据，但买方MIT权利、脚本执行、业务成果法律范围及未发布环境仍待10月21日补问答复。本次原线程读取及定向检索成功，无新回复，未追发。公开与技术运行均不能冒充平台对其他问题的答复。

## 公开上架后的剩余验证

| 门槛 | 当前状态 | 下一步与证据 |
| --- | --- | --- |
| 来源与包 | 当前af3d2c8包已推送；R82程序化获取、解压与安装后工具检查，R96本机浏览器实际下载及同一字节/来源检查分别通过 | 使用下方固定提交入口；未新增宿主发现或模型业务，R92–R94渠道证据单列；外部试用者收件与采用另记 |
| MIT与渠道许可 | 标准MIT保留；公开条款仍有复制/保存限制，批准不自动消除该问题 | 等平台澄清原MIT材料权利、客户用途与通知；不更换MIT、不自行增加限制或接受新协议 |
| 连接交付 | 核心/引用及本地产物真实运行；首交失败、专业修复后通过；R94同会话中断/继续通过 | R92与R93/R94成本各自保留；下一步让真实用户做真实任务，不把已有回归算未见或继续堆合成题 |
| 商品扫描与审核 | live/approved；公开页显示扫描通过、1条警告，明细未取得 | 保留批准和警告事实，不称零问题或完整安全审计，不重复提交 |
| 收款资格 | 未核实账户实际资格 | 用户自行提供实际经营/收款地区状态，在官方流程完成适用验证；不用时区推断，不索取密码或私钥 |
| 发布与试价 | 已有1 Live、Free；匿名公开页HTTP200；本轮仅内部启用验收，外部使用仍为0 | 有限试用如实说明已知编码问题与帮助；不自动改收费，平台计数、内部启用、外部采用和订单分开 |

平台需确认的最小技术问题：相对路径引用如何提供给Agent；可选脚本是否可执行且无需保存受限Skill文件；用户生成的业务文件能否正常保留/导出；未发布环境能否进行上述测试及更新/恢复。这些已在10月21日获准的同线程补问中发送，等回复，不重复发信。不要为“跑通”关闭安全限制或擅自重配现有连接。

## GitHub候选领取入口

[领取当前候选ZIP：af3d2c8（固定文件页）](https://github.com/dawwnforu/intent-compiler-skill/blob/d4648d8375456fe7a11c29d9f498a98573c03040/commercial/artifacts/intent-compiler-2.0-candidate-af3d2c8.zip) · [SHA-256文件](https://github.com/dawwnforu/intent-compiler-skill/blob/d4648d8375456fe7a11c29d9f498a98573c03040/commercial/artifacts/intent-compiler-2.0-candidate-af3d2c8.zip.sha256)

来源/运行文件提交`af3d2c80e37e77b03d661fd803422f949d04ee89`，承载提交`d4648d8375456fe7a11c29d9f498a98573c03040`。37,504字节、25成员，SHA-256：`4aad2ccccaac4869f5b5b9b958b6a97e8764b0e54ed5f7ea076ba6a0961c4bc5`。新包修复可选HTML检查器的UNC/根路径/盘符误探测，并同步该工具限制说明；核心、路由、标准MIT与显示字段不变。独立重建字节、新项目全部解压成员及安装后检查器五项测试通过；初始验收器把LF/CRLF许可证比较成不同的失败已保留，修正的是验收器，未改许可证。[R82证据及R96领取补验](../tests/v2-resource-paths.md)：固定文件页点击Download raw file，在8秒事件/路径限时内实际下载；所得文件的字节、SHA-256、25成员及24项声明哈希一致。R96另一次过严许可证字段比较的核验器失败也保留，只修验收器、不改包、不重下。未新增宿主发现或模型业务；外部试用者收件及采用仍未知，不借用旧包或本机下载作结论。

### 旧2881c73候选保持冻结

[旧候选ZIP：2881c73](https://github.com/dawwnforu/intent-compiler-skill/blob/7801146aec0353051dcb14060ea64fb724fe50d6/commercial/artifacts/intent-compiler-2.0-candidate-2881c73.zip)

来源提交`2881c7331e0e9de156317ac98d03a5b9afa4a4ff`，承载提交`7801146aec0353051dcb14060ea64fb724fe50d6`；运行方法来源仍为`f51b2ccb7d1ca7b3a5e6e58dcb202b672d1399ed`。37,426字节、25成员，SHA-256：`53615833bbee2ab5f1ad6d123e6c9972a46a67e3bea94b93b0118f98e40df634`。新包只改双语包内启动说明和宿主已有显示名字段，核心及方法不变。以上是候选身份，不是新的正式版本号或平台审核结论。

新包实际解压字节、继承用户配置的同名发现及一次明确路径启动通过；前后两个同名条目均启用，候选新标签可区分。模型额外尝试业务项目Git HEAD失败的记录保留，不影响来源字段读取，但不能称启动毫无摩擦。已从固定承载提交程序化取得新包，37,426字节、Git blob、SHA-256及25成员与本地构建一致。尚无本包浏览器下载或外部收件证据，不沿用旧包的下载结论。

[旧abef76f候选](https://github.com/dawwnforu/intent-compiler-skill/blob/cdb385d87c189cfe162ba23df9ebc2a9e66f97af/commercial/artifacts/intent-compiler-2.0-candidate-abef76f.zip)保持冻结；R79曾实际程序化获取和浏览器下载36,403字节并核对哈希，其承载提交CI通过。旧239553d摄影包也不重打。各自安装、发现、下载与外部用户状态见[分项记录](../tests/v2-submission-candidate.md)。
