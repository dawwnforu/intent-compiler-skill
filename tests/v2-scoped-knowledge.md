# R49: effective dates and scoped knowledge maintenance

Status: frozen before generation; not yet behaviorally tested. [Exact protocol, fixtures, runner and current Skill snapshot](results/v2-scoped-knowledge.json).

Protocol freeze commit: bb0e231. The first runner exited before skill discovery/model invocation because app-server initialization timed out; the accompanying CLI diagnostic reported denied access to its temporary directory. The prepared workspace is preserved as `V2-preflight-failed`. A retry uses the same frozen inputs and child workspace-write/offline boundaries with parent execution permission. This is an environment recovery, not an answer retry or model failure. Initial generation is now running; independent answers and update checks are still pending.

Compare an ordinary request, the existing short generic instruction and current candidate 7395bfb on a new synthetic shared-studio knowledge task. This tests a common knowledge-base workflow, not a newly added rule or a GitHub-derived project. All arms receive the same sources, tool preparation and offline/no-install/no-publication boundary. Order: Skill, raw, generic. Each uses gpt-6.1-sol low once; isolated skill discovery must confirm the intended arm.

The novice asks for maintainable local answers. Materials contain an approved general policy, a narrow branch/member exception, a future-effective deposit change, an unapproved suggestion, an external reference containing an irrelevant instruction, a duplicate, and five practical questions. Expected answers are frozen before generation: 3h/100, 2h/100, 2h/150 for the specified branch/member/date combinations; cancellation still requires 24h and there is no approved student waiver; lost-key fee remains unknown.

Independently inspect actual answers and source links, preservation of input files, and the delivered maintenance path. A withheld approved update changes only one branch/member duration on October25. Check historical and future queries without changing unaffected rules. Record whether updating requires manual editing, an AI follow-up or an actual automatic mechanism; do not imply one where only instructions exist. Practical additions are judged by use, not feature count. Preserve initial failures rather than repairing them during scoring.

One run per arm does not prove stable cost savings, broad superiority or user preference. This round does not change the installed Skill, license or release status.

## First completed arm: current candidate

V2 completed in 124.50 seconds. Independent reading of the delivered `知识库.md` against the frozen source facts confirms all five initial answers: 3h/100, 2h/100, 2h/150, no approved waiver or cancellation relaxation, and an unknown lost-key charge. The document preserves separate source/effective-date/member/branch scopes, labels the duplicate and external reference, and provides manual maintenance steps and date-boundary examples. It does not deliver an automatic answer engine, nor claim one. Input-byte preservation is recorded by the evaluator exporter separately from generated self-checks.

Raw and generic arms are still pending. The withheld D update has not yet been applied or checked. In particular, inspect whether the maintenance instruction to end-date an old version preserves unaffected branch/member scopes when a new exception arrives; initial answer correctness cannot prove this. No exclusive benefit or complete-workflow pass is claimed.
