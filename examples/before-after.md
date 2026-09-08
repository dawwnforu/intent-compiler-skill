# Before / after: AI customer-service pilot

## Same task

> 我们公司有30人的客服团队，想试试AI，但预算有限。我下周要给老板汇报，老板只看3分钟，我不懂AI。帮我做一份能直接用的AI客服试点方案。

The same Codex model handled this task once without the Skill and once with `$intent-compiler do --`.

## Directional result

| | Without Skill | With Intent Compiler |
|---|---|---|
| Presentation | 5 pages | 4 pages |
| Main framing | Explains the pilot | Centers the approval decision |
| Missing budget | Introduces a fixed ¥20,000 ceiling | Uses a relative ceiling and labels it as an assumption |
| Decision gate | Continue, adjust, or stop | Quantified continuation and immediate-stop conditions |
| Length | 1,876 characters, 132 lines | 1,809 characters, 112 lines |
| Total tokens | 13,875 | 14,699 |

## What changed

The baseline was already useful. Intent Compiler's improvement was narrower and practical: it made the decision clearer, treated missing business inputs more carefully, and tightened the deliverable for the stated three-minute audience.

This is one comparison, not a benchmark. It does not show that the Skill always reduces cost, time, or output length.
