# R22: feedback-driven repair / 连续反馈修复

2026-10-12. No Skill instruction changed. This follows the two remaining errors in [R21](v2-status-evidence.md); it does not replace those results.

The attempted R21 resume failed before a model response because the original run used an ephemeral session. A separate persistent session then completed two real turns with `gpt-6.1-sol`, low reasoning, network disabled. Turn two resumed the same new session. The failed attempt is retained in the [full record](results/v2-status-feedback.json), alongside exact prompts, generated processors, usage and independent execution results.

## What happened

The first repair correctly stopped treating discussion-only and no-conclusion statements as decisions, but became too conservative: six of fifteen declared contrast cases became false unknowns. A seventh clear decision in the retry check also became unknown. Examples include “不再延长报名”, removing a quoted “待确认” label, and a previously undecided date now confirmed for Friday.

Actual follow-up supplied those failures and requested correction without sentence-specific exceptions, heading-based fallback or making everything unknown. The generated processor now handles clause scope, quoted terms and historical versus current uncertainty. Unrelated cache hardening introduced in the first repair was removed.

Independent execution after turn two matched all fifteen declared labels, the original four records and the repaired-input decision. Old derived cache records were recomputed; source bytes and archive text were preserved; unchanged reruns created no new records; an empty file failed independently and succeeded after repair. Ten independent processor executions covered the two stages. Reported model time was 233.53 seconds for turn one and 250.62 seconds for turn two. Resume usage is preserved without treating it as verified incremental cost.

## Reproduction and limits

Use the processors, source statements and prompts in the JSON. Run each processor through PowerShell `-NoProfile -ExecutionPolicy Bypass -File organize.ps1 -Root <isolated fixture>`. Replay the previous derived cache, rerun unchanged, add contrast inputs plus an empty file, repair that input, then rerun again. Compare actual categories with the declared labels, source bytes, archive text and status records; process exit success alone is insufficient.

After feedback, these are exposed regression cases, not unseen generalization evidence. “If the venue is approved, confirm the date” receives a coarse unresolved label; it can also express an agreed conditional procedure and does not establish approval. The classifier remains a finite heuristic. No browser clicks, concurrency or crash recovery were tested. Model-reported internal test counts are not independent evidence. There is no baseline comparison or general accuracy/savings claim here; current Skill remains core R15 plus workflow R21.
