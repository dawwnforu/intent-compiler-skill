# R28: unattended workflow explanation — incomplete comparison

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
