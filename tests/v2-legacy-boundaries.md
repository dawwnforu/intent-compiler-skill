# R16: remaining legacy text conditions

Fixed candidate `b42004da33e7bc157550c0ae33df8cf2cb4a3178` (R15), gpt-6.1-sol low, fresh isolated sessions, actual enabled-Skill checks, disabled browsing/network. Compare raw A, fixed short generic G and full candidate V2 on C1/C2/C4/C5/C6. No release arm in this batch. Inputs are the requests and text fixtures from the legacy case specifications, with no expected answers supplied. The supplied C6 note is real fixture text, not a trusted instruction. [Every input, response, command, status and counter](results/v2-legacy-boundaries.json).

Twelve attempts completed across C1/C2/C4/C5. C6/V2 then failed at model startup with “Selected model is at capacity. Please try a different model.” It produced no response or usage. Following the predeclared stopping rule, C6/G and C6/A were not attempted. Do not treat missing usage as zero, a service failure as Skill failure, or the incomplete C6 comparison as passed. No replacement runs and no instruction changes.

| Case | Raw seconds / output | Generic seconds / output | Candidate seconds / output | Reviewed outcome |
|---|---:|---:|---:|---|
| C1 render only | 14.82 / 270 | 13.70 / 222 | 29.14 / 450 | All retain blue material/silhouette,1600×1200 PNG and display-only scope; explain absent scene/renderer without claiming an image |
| C2 load-bearing bracket | 23.80 / 484 | 20.80 / 397 | 39.33 / 652 | All seek real fit/load/mounting/printing data, keep dimensions and capacity unknown, and require actual validation |
| C4 temporary site access | 25.15 / 456 | 18.63 / 350 | 38.90 / 781 | All separate demo data/backend from private records, keep secrets server-side, explain localhost and leave provider terms/publication unverified |
| C5 one polite sentence | 6.91 / 16 | 5.27 / 16 | 5.85 / 16 | All produce the same polite sentence, preserve tomorrow/report, with no tool calls |
| C6 absent inputs/tools | not attempted | not attempted | 5.06 / unavailable | Model capacity error before any substantive response or note read |

The evaluator read all twelve full responses and all command records. Completed workspaces contain no generated artifacts; the failed C6 workspace contains only the unchanged supplied note. Candidate C1 reads render/visual guidance and excludes fabrication; C2 reads fabrication/source/clarification; C4 reads website/runtime/source/clarification; C5 reads no references. These are actual observed routes, not inferred from matching final keywords.

Candidate C2 first asks where/how the bracket mounts, then offers a conditional structure; A starts with a provisional reinforced bracket and G also clarifies bracket versus bookend. All retain material uncertainty and avoid a rated safe load. Candidate C4 offers more explicit checks of builds, responses and logs, while A/G already cover the main privacy/access conditions. A/G/V2 all leave current free-service limits unresolved; no specific provider's current capabilities were verified.

There is no unique candidate correctness win in these completed cases. Candidate output and time are higher in the three domain cases; fast-path output is equal. One sample per arm cannot establish stable efficiency, and more verification detail alone is not a user-preference result.

These are capability-limited text fixtures, not independent measurements of the machine's installed tool inventory. C4 has only a stack description, no actual code or private records. No render, load-bearing object, live deployment or provider/legal check was performed. Explicit no-file/no-publication boundaries also mean this batch does not demonstrate safe autonomous deployment. C3 remains separately reported in R13 on its recorded snapshot; mode variations remain unrun. All attempted processes are terminal.

Reproduce with the recorded inputs, equal instruction/tool conditions and isolated workspaces, checking the legacy semantic expectations against full responses and actual actions. Preserve service interruptions and unavailable counters. Any later C6 recovery must be labeled separately, not replace this failed attempt.
