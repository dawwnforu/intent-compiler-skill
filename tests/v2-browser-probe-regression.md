# Browser capability probing: fixed development comparison

Status: six sequential attempts ended; five completed and the last hit the model account's usage limit. The experimental paragraph was removed from the active Skill because improvement remains unproven. No replacement run was substituted.

## Evidence motivating the change

The six-run post-repair batch exposed browser verification overhead. All three habit-page generations encountered runner startup/control failures. The e3 trace wrote a full custom CDP harness before its first control request, then timed out on `Emulation.setDeviceMetricsOverride`. The e1 and e3 scripts both selected port9337 while generated concurrently. This establishes an isolation risk, not proof that a collision actually caused either failure. Some diagnostics returned connection refused. Do not reclassify all elapsed time or generated tests as waste.

The candidate changes only `references/interactive-products.md`: prove a minimal browser observation before expanding custom tests, reuse available tools, distinguish tool failure from product failure, preserve behavioral acceptance under fallback, and keep browser state/processes local to the task. No acceptance criterion is removed.

Exact experimental paragraph, inserted before the retrieval/stop sentence and retained here for reproduction:

> Before writing a custom browser test harness, prove the available runner can open a page and return a simple observation; an executable path alone is not a working capability. Reuse an existing runner when available. Keep tool-startup failures separate from product failures: diagnose the smallest failing operation before extending or rewriting tests. A fallback must check the same behavior; static checks do not establish rendered interaction. Use task-local browser state and an available port, and stop only processes started for this task.

## Frozen comparison

- Before: repaired V2 Skill as captured for the prior six-run batch; core repairc51d267. This is **not** the release0.2.0 baseline.
- After: identical files except the browser-probe paragraph in the interactive-products module.
- Three runs each; fixed order before/after, after/before, before/after. Run serially, not concurrently. Preserve failures; no winner-based stopping or tuning within the batch.
- Same model `gpt-6.1-sol`, low reasoning, tools, 900-second limit and fresh workspaces. Enable only the tested Skill and verify its actual path. Both arms receive the same existing local-only boundary plus task-local browser profile/automatically assigned port requirement.
- Local harness labels `V1` and `V2` mean before/after **only for this batch**. Do not pool with historical V1/V2 records.

Request, unchanged from the exposed habit task:

> 做个手机上用的学习打卡小页面。我能添加自己的学习项目，每天勾选完成，点错也能取消，看今天完成了多少。关掉再打开记录还在，能导出自己的数据。界面清爽，有一点反馈动效，先在本机用，不需要账号。

## Observe and decide

Record CLI input/cache/output counters, elapsed time, tool failures and whether the minimal probe was actually attempted before full harness construction. Counters alone do not establish unnecessary output or improvement.

Inspect every generated page independently in a real browser at390px: empty state; add two named projects including literal markup characters; check/undo/recheck and counts; reload retention; actual parseable export; no horizontal overflow or runtime exceptions; readable screenshot. Apply the same date-reopen diagnostic to both arms and retain original storage. Do not modify generated artifacts to pass checks. Record unavailable checks or product defects separately from evaluator failures.

This is an exposed single-task ablation with three repeats per variant, not a new holdout, cross-domain proof or a universal efficiency claim. Sequential execution reduces simultaneous interference but does not eliminate temporal variance or all shared-host effects. Earlier raw outcomes remain unchanged.

## Observed results and decision

| Pair | Before output tokens / seconds | After output tokens / seconds | Generation status |
|---|---|---|---|
| p1 | 7079 / 214.33 | 8279 / 308.87 | Both completed |
| p2 | 10026 / 376.20 | 7447 / 218.66 | Both completed |
| p3 | 6448 / 177.01 | unavailable / 100.42 until interruption | Before completed; after hit usage limit |

[All six attempt records](results/v2-browser-probe.json) retain input/cache/output counters where available and the actual service error. After p3 has no `turn.completed` usage record; its incomplete duration is not a speed result. Any available-case summaries have unequal sample counts and must not be presented as the planned complete three-versus-three comparison.

Independent Edge checks of all six saved artifacts (including the explicitly marked partial generation) passed add/check/undo/count/reload/export/literal-name/mobile-layout and date-reopen observations; all six screenshots were inspected. This validates those artifacts, not completion of the interrupted model run. Full accessibility, real phones and live-midnight behavior remain untested. Before p3 itself honestly reported unavailable browser verification, so generation latency also reflects different self-verification completion, not equal work alone.

After p1 attempted a probe but already contained the larger harness before successful capability confirmation; adoption was partial. After p2 obtained a minimal browser evaluation before adding its full test file. Before p2 wrote an extra WebSocket helper while diagnosing connection problems. These are observed behaviors, not proof of a causal reduction in waste. Host GPU/path/startup failures affected the runs.

The two complete pairs point in opposite directions. Remove the experimental paragraph from the active module; preserve it here and retain both frozen local snapshots. A general tool-capability boundary already remains in the core. Further model trials require available account usage; do not buy credits, change models, or silently replace failed attempts to produce a favorable result.
