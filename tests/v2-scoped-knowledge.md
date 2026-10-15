# R49: effective dates and scoped knowledge maintenance

Status: all three initial generations and initial answer checks complete; AI-assisted maintenance continuation running. [Exact protocol, fixtures, runner and current Skill snapshot](results/v2-scoped-knowledge.json).

## Initial comparison

Independent inspection of each delivered knowledge artifact and five-answer document against the frozen source facts confirms all five initial answers in all three arms. All distinguish applicable scope, effective date, unapproved suggestions, external text, duplicates and unsupported fees. Each supplies manual maintenance guidance; no automatic question engine or ingestion service is claimed. The initial outcome is shared capability, not an exclusive Skill gain.

| Arm | Output tokens | Seconds | Initial artifact and outcome |
|---|---:|---:|---|
| Raw A | 5160 | 157.50 | Five Markdown documents; all five answers correct |
| Generic G | 4304 | 130.62 | Entry plus knowledge folder; all five answers correct |
| Current Skill V2 | 4529 | 124.50 | Single knowledge document; all five answers correct |

V2 uses less output than raw but more than generic in this one sample. It takes less time than both here; this does not establish stable cost savings. File count alone is not usability evidence, and no human preference for these outputs has been collected.

The independent integrity check confirms seven unchanged input files per arm and existing local Markdown targets: A29, G16, V2 28. It does not validate anchors or semantic accuracy. Its first implementation incorrectly compared Windows-written CRLF files with LF string literals, producing false modification flags; comparing to the actual frozen fixture bytes corrects this evaluator error. The initial failed check remains locally preserved. No generated source was repaired.

The exact AI-assisted continuation is frozen separately before continuation calls. It copies each initial delivery, adds the same held-out D source and asks the historical/current/future queries. This is not a human novice manually performing maintenance or an automated ingestion test. Initial outputs remain unchanged. Outcome checks are pending.

Protocol freeze commit: bb0e231. The first runner exited before skill discovery/model invocation because app-server initialization timed out; the accompanying CLI diagnostic reported denied access to its temporary directory. The prepared workspace is preserved as `V2-preflight-failed`. A retry uses the same frozen inputs and child workspace-write/offline boundaries with parent execution permission. This is an environment recovery, not an answer retry or model failure. Initial generation is now running; independent answers and update checks are still pending.

Compare an ordinary request, the existing short generic instruction and current candidate 7395bfb on a new synthetic shared-studio knowledge task. This tests a common knowledge-base workflow, not a newly added rule or a GitHub-derived project. All arms receive the same sources, tool preparation and offline/no-install/no-publication boundary. Order: Skill, raw, generic. Each uses gpt-6.1-sol low once; isolated skill discovery must confirm the intended arm.

The novice asks for maintainable local answers. Materials contain an approved general policy, a narrow branch/member exception, a future-effective deposit change, an unapproved suggestion, an external reference containing an irrelevant instruction, a duplicate, and five practical questions. Expected answers are frozen before generation: 3h/100, 2h/100, 2h/150 for the specified branch/member/date combinations; cancellation still requires 24h and there is no approved student waiver; lost-key fee remains unknown.

Independently inspect actual answers and source links, preservation of input files, and the delivered maintenance path. A withheld approved update changes only one branch/member duration on October25. Check historical and future queries without changing unaffected rules. Record whether updating requires manual editing, an AI follow-up or an actual automatic mechanism; do not imply one where only instructions exist. Practical additions are judged by use, not feature count. Preserve initial failures rather than repairing them during scoring.

One run per arm does not prove stable cost savings, broad superiority or user preference. This round does not change the installed Skill, license or release status.

## First completed arm: current candidate

V2 completed in 124.50 seconds. Independent reading of the delivered `知识库.md` against the frozen source facts confirms all five initial answers: 3h/100, 2h/100, 2h/150, no approved waiver or cancellation relaxation, and an unknown lost-key charge. The document preserves separate source/effective-date/member/branch scopes, labels the duplicate and external reference, and provides manual maintenance steps and date-boundary examples. It does not deliver an automatic answer engine, nor claim one. Input-byte preservation is recorded by the evaluator exporter separately from generated self-checks.

Raw and generic arms are still pending. The withheld D update has not yet been applied or checked. In particular, inspect whether the maintenance instruction to end-date an old version preserves unaffected branch/member scopes when a new exception arrives; initial answer correctness cannot prove this. No exclusive benefit or complete-workflow pass is claimed.
