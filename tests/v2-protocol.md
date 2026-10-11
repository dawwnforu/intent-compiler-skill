# V2 evaluation protocol

Candidate-only work. No stable improvement is established by this document or the repository checker.

## Arms and isolation

A: raw request. G: same request plus “Understand the goal, resolve necessary gaps, use available tools, complete and verify; do not invent facts or permission; deliver concisely.” V1: fixed 0.2.0 release commit. V2: frozen candidate snapshot.

Use the same model, reasoning setting, enabled tools, permissions, inputs and timeout. Start fresh conversations with no other arm's history. Use actual skill-discovery configuration; telling a model to forget a loaded Skill is not isolation. Keep one normal installation; use project-local snapshots only inside evaluation workspaces. Record discovery and successful Skill reads.

Separate logs, scoring criteria and repository finished products from each model's workspace. Reconstructed first requests contain goals/presentation, not the eventual architecture or known fixes. Existing-project repair is a separate experiment from generation. Public README claims are case-selection context, not proof the source project works.

## Sets and rounds

1. Freeze developer cases and expected behavior before the run.
2. Pilot the runner, inputs and meaningful acceptance checks. Retain environment failures separately; rerun for diagnosed environment faults, not disappointing content.
3. Revise only observed generalizable failures; write failure → change → expected observable effect.
4. Run at least a second development round with all comparison arms where the inputs/environment changed.
5. Freeze the candidate. Run new task variants and input fixtures not used for tuning, at least three repetitions per key comparison, with interleaved order.

Do not repeatedly tune on a holdout then continue calling it a holdout. Re-label exposed cases and reserve fresh material. Preserve all completed trials and define any exclusions before comparing outputs.

## Evidence and measures

- Intent: requested outcome, audience, exclusions and meaningful ambiguity handled correctly.
- Necessary gaps: required unknowns become an appropriate question, retrieval, tool check or execution constraint; generic risk lists receive no credit.
- Completion: artifact actually exists and satisfies the observable task, not just source syntax or a screenshot.
- Boundaries: no fabricated facts, unperformed checks or new permissions; correctly blocked branches are reported separately from completed artifacts.
- User burden: unnecessary questions, specialist decisions pushed to the user, redundant explanations/secondary documents.
- Efficiency: CLI input/cache/output usage, elapsed time, tool invocations and output size; separate final/ongoing prose from required code and artifacts. Character counts are not token counts.

Gate correctness and critical boundaries before rewarding lower cost. Use actual browser input/frames, independent calculations, file-format checks and relevant failure transitions. Automated keyword checks can locate evidence but cannot establish understanding or task success. Any model judge is advisory and must cite observable evidence; report human/agent review limitations.

Show per-trial observations and medians, not only the best example or an aggregate that hides a failing domain. Small samples cannot support sweeping percentages or statistical certainty. Do not set “astonishing” as a mandatory conclusion.

## Case coverage

Use [the case catalog](../examples/v2-cases.md). Include simple edits and negative routing alongside complex tasks; include multi-turn clarification with an identical prepared answer available to every arm. Never let different user help explain an apparent Skill advantage.

No extra paid services, dependency installation, publication, purchases, live private data or real-project mutations in these tests unless separately authorized. Missing tools are evidence, not permission to bypass a boundary.
