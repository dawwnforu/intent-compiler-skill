# R10: additional product-scope guidance was not retained

R9 improved waiting for necessary answers but still sometimes retained a broad feature list in a local-demo plan. R10 tested additional guidance in the existing Product and process section: tie each capability to the present action/decision, identify when deferred ideas become useful, preserve reaffirmed visual requirements, and retain real-workflow reliability. The knowledge-index row was adjusted to route product tradeoffs there. The source entry pointed to scoped GOV.UK alpha guidance. No new subsystem or dependency was added.

## Protocol fixed before generation

Before is commit `b8215a744440cceb7d69a9b50d5f184381939364`; after changes only `references/domain-lenses.md` and `references/knowledge-index.md`. In the records V1/V2 mean these two 2.0 candidate variants, not release0.2.0 or a raw-model baseline. Both used the same gpt-6.1-sol low-reasoning CLI setup, tool boundary and enabled-Skill check.

Six sequential runs: spreadsheet/before, spreadsheet/after, visual/after, visual/before, workflow/before, workflow/after. One sample per condition, no within-batch tuning,900-second limit per run. All prompts explicitly requested a brief without code. The exact prompts, criteria, all responses/documents/counters and both versions of the changed instruction files are in [the retained record](results/v2-product-scope.json).

| Case | Present outcome | Criteria recorded before running |
|---|---|---|
| Replace spreadsheet | A manager must decide whether a local training-registration demo could improve two colleagues' inconsistent class-change records | Connect scope/acceptance to reconciliation and change consistency; request actual workflow/data needed; do not fabricate savings |
| Visual pitch | A phone story must demonstrate scene transitions, choice-dependent character actions and an actually savable result card | Preserve all three reaffirmed outputs and relevant checks; do not substitute a static concept or require irrelevant live social infrastructure |
| Operating workflow | Five people must really use a text-to-task workflow despite revisions, duplicate submissions and bad files; no external model account/platform yet | Preserve shared utility, source/confirmed-task separation, missing facts, edits, partial failure, conflicts and recovery; do not pretend a live model/integration exists |

## Observations

All six processes completed. Each delivered a single primary Markdown brief plus a short response; no code or running product was delivered. The evaluator read every response and full document. Both variants met the principal criteria:

- Spreadsheet: both focused on consistent registration/class-change records, deferred payment/social features, requested actual workflow and representative data, and separated local-demo evidence from concurrent collaboration and economic value. Both proposed a30% time-reduction discussion target and labeled it as a suggestion, not a measured saving or an approved business requirement. It is not this project's improvement percentage.
- Visual: both retained scene transitions, distinct actions and a real saved image, with route/reset/device/failure checks and separate creative feedback. They used different explicit assumptions about scene/transition counting; no rendering or phone execution occurred to settle these assumptions. More or fewer proposed scenes is not automatically a quality score.
- Workflow: both retained five-person shared use, preserved confirmed edits/status when sources change, isolated bad files, addressed duplicates/concurrent edits and required actual recovery checks. Both proposed human-confirmed assistance without claiming automatic understanding or live platform integration. The after variant recommended one importer as an unconfirmed role choice; it did not establish that this was the team's actual workflow.

| Case | Before output tokens / seconds | After output tokens / seconds |
|---|---:|---:|
| Replace spreadsheet | 3344 / 204.00 | 3764 / 157.31 |
| Visual pitch | 3133 / 134.80 | 3332 / 122.07 |
| Operating workflow | 3923 / 213.22 | 3647 / 166.65 |

After was faster in all three observed samples, while output increased in two and decreased in one. Input/cache counts are also retained. These single samples, server variability and changed document content do not establish a causal or stable speed advantage. No composite quality score, runtime pass or user preference result is inferred.

## Decision and limits

No unique consequential capability was demonstrated by the extra guidance beyond the existing candidate in these cases. The two-file addition was withdrawn, restoring the active Skill to R9; exact experimental text remains in the record for reproduction. This is a decision not to add unproven instruction load, not proof that such guidance can never help.

The clearer spreadsheet problem was handled well by both variants. It suggests that obtaining the actual problem may matter, but these tasks differ from the earlier generic training-platform conversation and cannot establish that causal claim alone. A separate request for the user's preference between two actual training plans is pending; silence is not preference evidence. All six trials are terminal. Real UI/workflow implementation, human experience and broader repeated superiority remain unverified by this batch.
