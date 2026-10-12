# R19: do not repeat settled concepts — not adopted

Six fixed attempts completed: an actual two-turn registration dialogue per candidate variant, followed by one explicit re-explanation control per variant. Before is `fd320874366a6c31fd37d4d808b9d4ef375de704`; after replaces one output paragraph in `SKILL.md`. It asks follow-ups to advance using new information without reteaching settled concepts, while preserving requested explanations and necessary reasons/checks. [Exact replacement, prompts, complete responses and commands](results/v2-followup-focus.json).

Same gpt-6.1-sol low setup, isolated discovered Skill, disabled browsing/network. The dialogue reuses R18 verbatim with the same fixed second message; resume IDs match. Order: after dialogue, before dialogue, before control, after control. No within-batch changes, replacements or failed attempts. The active repository Skill remains byte-identical to before.

| Attempt | Before seconds / output counter | After seconds / output counter |
|---|---:|---:|
| Dialogue turn 1 | 57.39 / 1235 | 45.83 / 1046 |
| Dialogue turn 2 | 48.86 / 2296 | 49.27 / 2208 |
| Re-explanation control | 32.86 / 556 | 31.35 / 592 |

Resume usage may be cumulative; do not sum counters as verified incremental cost. Single pairs and different cache counters do not establish a causal or stable saving.

Both dialogue variants explain shared storage, protected organizer access, false-success handling and independent-client acceptance without implementing or inventing deployment. After still re-explains localhost, localStorage and component responsibilities. It adds identity options and a useful conditional check of old local records, but assumes recoverable access more directly. Before more explicitly asks whether changing devices or clearing the browser must preserve access. Neither supplies a clear overall judgment advantage.

Both controls honor the request to explain again through personal notebooks versus a common register, without an unwanted deployment lesson. After correctly uses an authorized organizer's aggregated view; before suggests ordinary participants see each other's entries. The control does not specify the earlier dialogue's role restriction, so this is a narrower privacy/design limitation, not violation of a carried-over instruction: the control is standalone. There is no evidence that the output-rule substitution caused the difference.

**Decision:** do not adopt the replacement. The main targeted repetition remains, second-turn time does not improve, and substantive strengths are mixed. Keep the smaller existing rule and all negative evidence. Neither zero repetition nor shortest output is the objective; explanations that change an informed decision are useful.

An additional validity limit is important: the second dialogue message supplies technical facts but does not explicitly say the user understood the earlier explanation. Repeating a short bridge may be helpful. This experiment therefore cannot establish whether a user found the repetition wasteful or whether the concepts were genuinely settled. Future claims about unnecessary repetition need actual comprehension/feedback or an explicit understood premise, not only word-count differences.

All completed commands are Skill reads; every workspace has no generated product files. Initial reads without explicit UTF-8 garble some bilingual index text, while English rules remain readable. No live service, runtime security, human satisfaction, cross-model or general efficiency claim follows. Reproduce from the JSON, applying only the recorded paragraph to the pinned before snapshot and preserving the order, isolation, fixed answers and all outputs.
