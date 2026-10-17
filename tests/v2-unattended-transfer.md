# R28: unattended workflow explanation — completed with preserved failures

**Completion update:** All four arms now have two completed answers. V1's second turn succeeded on a later resume of its original conversation; previous capacity failures and the preflight timeout remain recorded. All four cover the main second-turn explanation requirements, with no exclusive candidate quality gain. The initial-attempt and recovery narratives below are historical; see the final section for current status.

This new development transfer follows the user's R18 preference for explaining usage consequences before technical choices. The fixed task asks for a daily meeting-to-task assistant, then specifies a shut-down personal computer, results before work the next morning, edited shared-folder files, proposals versus decisions, recoverable corrections, and no accounts, approved budget or permission to execute/upload. It does not request implementation in these two turns.

Planned order: G/generic, V2/candidate, A/raw, V1/installed release snapshot. Same two messages, model gpt-6.1-sol/low, disabled browsing/network, isolated Skills, persistent two-turn conversations and 300-second turn limits. Candidate source is `79f130d`. [Exact prompts, snapshots, runner, responses, invocations, counters and failures](results/v2-unattended-transfer.json).

The initial sandbox attempt timed out in Skill discovery (`queue.Empty`) before generation. Its runner terminated and the attempt remains recorded. The separate approved host attempt passed actual Skill inventory checks: G had no enabled Skill; V2 had only its snapshot. G completed both turns; V2 failed its first turn with **“Selected model is at capacity. Please try a different model.”** The runner then stopped as specified. A and V1 were not attempted. No process remains running and no generated product files exist.

## Completed observations

G already explains that overnight completion while the user's computer is off needs an available execution environment. It keeps manual local validation distinct from the desired overnight result; recognizes edited files, task changes and duplicates; retains source evidence and human corrections; separates proposals from decisions; preserves permissions/budget unknowns; and gives concrete checks. Both full responses were read. These useful abilities cannot be credited as exclusive Skill gains.

| Completed arm | Turn | Seconds | Output counter |
|---|---|---:|---:|
| G | 1 | 27.98 | 541 |
| G | 2 | 29.64 | 1318 |

The first turn recovered from transient service errors within its original invocation. Resume counters may be cumulative; do not sum them as measured incremental cost. There is no candidate response, paired quality result, user preference, implementation validation or efficiency finding. **Do not change Skill rules based on the capacity failure.**

## Resume method

Keep both attempts. After model availability returns, run the unattempted A/V1 conversations and the failed V2 conversation in new isolated folders using the exact recorded prompts, model, snapshots and limits. Record their later execution time and the recovery order; do not overwrite this failed V2 invocation. If model or conditions must change, start a separately labelled complete comparison rather than combining incompatible arms. A future comparison must inspect full answers, loaded sources and scope preservation before asking for any excerpt-level human preference. This remains a development scenario, not an unseen test after its criteria and G response have been inspected.

## Recovery results — 2026-10-13

Later order V2/A/V1, with byte-identical frozen Skill trees, unchanged messages and the same model/configuration. Actual enabled-Skill inventory and same-thread continuation IDs were checked. Five new responses completed and were read in full. V1 turn 2 failed with the same model-capacity message; its first turn remains valid evidence, not a replacement full conversation. All processes are terminal. [Full recovery records and checks](results/v2-unattended-transfer-recovery.json).

| Arm | Turn 1 seconds / output counter | Turn 2 seconds / output counter |
|---|---:|---:|
| G, previous run | 27.98 / 541 | 29.64 / 1318 |
| V2, recovery | 70.97 / 763 | 39.48 / 1609 |
| A, recovery | 35.77 / 646 | 40.67 / 1483 |
| V1, recovery | 101.83 / 808 | Capacity failure; no response |

A/G/V2 second turns all cover the six predeclared explanation criteria: available execution while the personal computer is off, preserved next-morning goal, modified-source handling, source evidence and human correction, authorization limits, and meaningful acceptance checks. **No exclusive candidate quality gain.** V2 output counters are higher than A/G in both observed turns. Later execution, service errors, caching and possibly cumulative resume counters prevent stable causal efficiency claims.

All four first turns suggest completion before the workday ends although the first request does not settle timing. A/G ask about timing and V1 frames it as a recommendation; V2 begins by paraphrasing that time as understood intent. This is a concrete limitation: a plausible suggestion should not silently become the user's stated goal. All three completed second turns correctly update to next-morning completion. That correction does not erase the first-turn limitation. V2 initial module reads omit explicit UTF-8, garbling some bilingual index text; English rules remain visible. No added behavior rule, no implementation test and no new human preference claim.

Still missing: V1 turn 2. It can later resume the recorded persistent conversation with the exact second input in a separate log folder; preserve the failed invocation and confirm the thread ID before using its answer. Do not rerun completed arms solely to seek a more favorable result.

## Final release continuation — 2026-10-13

The previously missing V1 second turn completed in 34.00 seconds with output counter 1715. Its prompt and command flags match the failed invocation except for the new output log path. The original conversation ID, frozen Skill bytes and exact enabled Skill were verified; no product files were generated. [Response, events, invocation and checks](results/v2-unattended-release-completion.json). All execution handles are terminal.

V1 also explains the six required points, including source-version evidence, changed or withdrawn tasks, preserving human corrections, distinguishing proposals, authorized execution and tests of actual overnight completion. All four completed second turns follow the explicit next-morning goal. Candidate output counters (763/1609) are below V1 (808/1715) but above A (646/1483) and G (541/1318); this single scenario, staggered recovery and possibly cumulative resume accounting do not establish stable savings. No product behavior change follows from these results. The four-arm explanation comparison is complete; actual automation and broad goal completion remain unproven.
