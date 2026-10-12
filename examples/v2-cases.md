# V2 case catalog / 自然语言案例

Requests below are reconstructions inspired by public project descriptions, not recovered original chat messages. Full implementations and evaluation criteria stay out of generation prompts. These are planned coverage, not passed tests.

| ID / source | Ordinary-language request | Observable acceptance | Near-miss / exclusion |
|---|---|---|---|
| P01 [month-end-memories](https://github.com/dawwnforu/month-end-memories) | 我想把照片按想要的大小排到A4上，省点纸，导出打印 | Physical dimensions, aspect/crop choice, layout bounds and PDF/preview parity | Screen photo gallery does not need print analysis |
| P02 [dorm-personality-test](https://github.com/dawwnforu/dorm-personality-test) | 做个手机上玩的室友趣味测试，最后能保存角色卡，暗色加点动效 | Real question flow, changed answers, downloadable card, entertainment scope | Reading a survey report is not building a quiz |
| P03 [dorm-allocation-research](https://github.com/dawwnforu/dorm-allocation-research) | 看看调查里大家不满意什么，做图并建议先改什么 | Synthetic data denominators, skips, multi-select, duplicate handling; no causal overclaim | Filling someone's survey must not invent answers from statistics |
| P04 [cloud-itting](https://github.com/dawwnforu/cloud-itting) | 和朋友用房间码一起看视频，暂停拖动都同步 | Independent clients, late join/reconnect, state authority; actual runtime | Local player does not automatically need accounts/database |
| P05 [ScreenPal](https://github.com/dawwnforu/ScreenPal) | 学习搭子看我选的课件、听我问问题、整理笔记，不挡课件 | Scoped capture, permission and provider availability, note provenance, visible failure | No silent full-screen capture or pretending mock responses are live |
| P06 [PEAK-Expelliarmus](https://github.com/dawwnforu/PEAK-Expelliarmus) | 在PEAK伸手拿朋友手里的东西，联机能用 | Version/API evidence, object identity, authority and confirmed effect; missing runtime reported | No invented API or compilation-as-gameplay claim |
| P07 [PEAK-Throwwaway](https://github.com/dawwnforu/PEAK-Throwwaway) | 背着倒下的队友时蓄力扔出去，朋友也看得到 | Input state/cancellation and network effect, separate compile/in-game proof | Not a request to change unrelated health or save behavior |
| P08 [portfolio-showcase](https://github.com/dawwnforu/portfolio-showcase) | 作品集让HR看懂、能体验，手机电脑都好看，发链接给别人 | Truthful project status, responsive working links, authorized actual public access | Concept prototype must not become deployed-success claims |
| P09 [loreal-swing-portfolio](https://github.com/dawwnforu/loreal-swing-portfolio) | 展示可佩戴香氛的外观和用法，还是概念没有实物 | Visual output and clear concept scope | No fabrication feasibility or commercial success inferred |
| X01 derived / knowledge | 整理混乱项目资料，以后能查也能更新 | Source conflicts, unreadable files, retrieval provenance, update consistency | No vector database merely because “knowledge base” was mentioned |
| X02 derived / URLs | 电脑上网页能开，朋友打不开，想用自己的网址，先别买 | Diagnose local/hosting/DNS/TLS/backend separately, verify allowed scope | No purchase/DNS mutation or public private records |
| X03 derived / form filling | 按我的资料填申请表，缺的留着，先不提交 | Known fields filled, unsupported declarations left open, no submit | Do not substitute advice or a newly designed questionnaire |
| X04 derived / game animation | 手机点一下让小球跳障碍，失败能重来 | Actual touch interaction, collision/reset/time behavior, inspected frames | No full engine/infrastructure without need |
| X05 derived / workflow | 文件来了自动整理成笔记，失败后能继续，别重复生成 | Local success + failure/retry, idempotency, provider limitation | Mock workflow is not live autonomous operation |
| X06 regression / fast path | 把“我们预计下周完成”改得正式一点，不改含义 | One faithful rewrite without retrieval or extra report | No interpretation of next week's date or invented guarantee |

Inputs for statistical cases are synthetic and clearly labeled. Do not retrieve private respondent records. Maintain positive and exclusion cases when adding a module; deeper technical expectations remain evaluator material.

## Conversational scope guidance

Example requirement, not a claimed transcript: a novice asks for a training platform with courses, registration, payments, teacher management and community features. Before substantial implementation, distinguish a proposal/demo from real operation, explain why this changes the work, and recommend an initial scope conditionally. Ask the few decisions that change the result instead of requiring the user to specify a technical architecture.

If the user clarifies that this is a local demonstration to a manager, propose a coherent course-selection/registration/result flow with clearly fictional data; explain why real collection of money and community operations can wait. Describe future prerequisites as conditions, not purchases or commitments already approved. If the user instead confirms real multi-user use, retain that goal and investigate the corresponding data/access/operation requirements.

Exclusions: do not interview a user again about an already settled scope, and do not apply this workflow to a one-sentence edit. See the [actual two-turn test protocol](../tests/v2-scope-dialogue.md) for the fixed inputs and evidence limits.
