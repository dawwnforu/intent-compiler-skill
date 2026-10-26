# R27: separate source questions from execution guidance

Subsequent scope correction (2026-10-13): the workflow title/intro still named knowledge collections and conflicting project knowledge after the split. Align them with the index and link source-only questions to the organization module; remove “lookup” from the workflow stopping sentence. The execution section is unchanged. The four historical runs below predate this correction and do not prove its effect on loading or model quality. Repository checks and comparison of the preserved execution section cover this maintenance change; no new model runs.

2026-10-13. Split the knowledge-organization paragraphs out of the workflow module and give them their own index row. Move the paragraphs unchanged; retain a conditional link to execution guidance when an actual processor is needed. Core instructions are unchanged. Adopt this for narrower source-only loading, not general savings or superior answers.

[Exact snapshots, prompts, fixtures, responses and commands](results/v2-route-split.json) cover four actual runs: one before/after pair for project-record questions and one for a local meeting-processing brief. Base `d41e4a3`, `gpt-6.1-sol`, low reasoning, isolated Skills, offline/read-only. The common refreshed preflight ran before each model invocation.

| Task | Variant | Output tokens | Wall seconds | Tool output characters |
|---|---|---:|---:|---:|
| Project questions | Before | 986 | 22.71 | 16,603 |
| Project questions | After | 950 | 26.44 | 15,365 |
| Workflow brief | Before | 2,044 | 57.35 | 21,305 |
| Workflow brief | After | 2,071 | 61.25 | 21,339 |

Actual outputs confirm that the before project task loaded execution and organization paragraphs; the after task loaded only organization. Both answers preserve confirmed scope, unresolved launch/budget, unconfirmed handoff, source locations and rejection of injected instructions. After omits an explicit current verification date that before prints; historical source dates/locations remain available. Do not treat every presentation property as preserved.

Both workflow answers inspect sample files and the invalid-encoding input, propose per-file state, preserved original bytes, duplicate prevention, repair/retry and meaningful acceptance. Both read execution and organization guidance: this is relevant to a combined processing/notes task, so splitting cannot eliminate those reads. Both suggest local SQLite as part of the future design, but no database, dependency or product is created. Their plans differ in encoding support and detail; neither is runtime evidence.

All fixtures are byte-identical and no files were generated. Assertions verify the moved knowledge paragraphs are unchanged and the remaining workflow text equals the original minus those paragraphs. Review covers whole answers and actual tool returns, not filename mentions alone.

Reproduce with the stored snapshots, prompts and fixtures in isolated workspaces, validating enabled paths first. Compare actual sections returned and full-task correctness, not just length. Character counts are not tokens; full-turn counters are not final-answer length. One pair per known task does not establish stable efficiency, unseen generalization, human preference or cross-model behavior. The earlier pending human-feedback question is still separate.
