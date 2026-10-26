# Frozen evaluation cases / 冻结测试材料

These cases were new to candidate tuning when frozen. They are now public regression material; a future tuned version needs fresh held-out tasks. Read the [protocol](v2-protocol.md) before reproducing. Keep expected answers and other arms' artifacts outside the generation workspace.

## Setup

The recorded experiment used Codex CLI, `gpt-6.1-sol`, low reasoning, Windows PowerShell, live web access and existing local tools. Each run had a fresh workspace/conversation, a900-second limit and no other enabled Skills/plugins. Project instructions were disabled. V1 is release0.2.0; V2 Skill content is frozen at commit `25c5d9669db1a9f3f1e050d70e937c3a767ecb98`. Exact discovery was checked through the host before generation. Host defaults and sampling can change; results are not guaranteed across models or hosts.

A receives the raw request. G prepends exactly:

```text
理解目标，必要时补充条件，使用可用工具完成任务并验证；不要编造事实或授权，简洁交付。
```

V1/V2 enable only their respective project-local Skill snapshot and prepend `$intent-compiler`. All arms append:

```text
本次只在当前工作目录制作成果，可查询公开资料和读取已启用技能。不要读取其他会话、其他测试目录或私人文件；不要安装依赖、付款、上传、公开发布或修改真实项目。使用已有工具完成能完成的工作。
```

Run each task/arm three times with fresh state (24 generations). Submitted arm order by repetition: A/G/V1/V2, G/V2/A/V1, V1/A/V2/G; up to four simultaneous processes, one task batch at a time. Preserve every result, including failures. Compare medians/ranges only after checking quality. Do not silently replace disappointing runs.

## Course feedback

Copy only the two files in [fixtures/v2-course](fixtures/v2-course/说明.md) into `inputs/` in each workspace. Request:

```text
我做了一次小课程，收了这些反馈。帮我看大家最需要补什么、学完有没有变化，做一份能给同事看的结果，建议下一次先改哪里。资料在 inputs。
```

Independent reference:9 rows become8 people. Completed has7 valid answers,5 yes. Multi-select denominator7: practice4, video3, Q&A3. Conditional practice time has4 valid values20/30/0/15, mean16.25; retain zero and do not fill blanks. Five paired ratings:2.8→3.8, average difference+1;3 rise/1 unchanged/1 fall. No causal claim, real-participant claim, invented course topic or inferred optimal practice time. Recommendations may go beyond the data when labeled as proposals. Review the actual readable artifact, not only the final response.

## Local habit page

Empty workspace. Request:

```text
做个手机上用的学习打卡小页面。我能添加自己的学习项目，每天勾选完成，点错也能取消，看今天完成了多少。关掉再打开记录还在，能导出自己的数据。界面清爽，有一点反馈动效，先在本机用，不需要账号。
```

Use an independent browser profile at390×844. Add two projects, one named `阅读 <b>复习</b> & 记录`, the other `英语单词`. Target the newly added item even if examples already exist. Check/undo/check: count1→0→1 with the correct total. Reload: same state. Download and parse the actual export: both names and the completed record must exist. Inspect screenshot/readability and horizontal overflow; input stays literal text. Record exceptions and incomplete paths.

Post-hoc diagnostic, introduced after first-round generation and applied equally to every arm: reload with browser Date advanced24h, expect today's count0; restore real Date and reload, expect original1 and retained history. This tests date ownership on reopen, not continuous midnight rollover, timezone changes or sleep/resume. Keep this distinction in the report.

## Record and reproduce

Save the exact prompt, model/settings, discovered Skills, frozen snapshot, exit/timeout, response, generated artifacts and CLI JSON events. Independently retain browser observations/downloads/screenshots or source-data calculations. Record output/input/cached tokens as exposed by the CLI, elapsed time and message characters separately. No model calls are made by the repository's static checker; running these cases consumes the evaluator's host/model quota. No new service or paid API is required by the Skill.
