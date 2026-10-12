# Validation and comparison protocol

## Candidate status — 2026-10-12

Initial corpus:67 actual generations,43 development trials and24 frozen new-task trials. Later scoped experiments are recorded separately below and in [results/limits](docs/v2-results.md). See [initial counters](tests/results/v2-runs.json), [four-arm protocol](tests/v2-protocol.md) and [reproduction fixtures](tests/v2-heldout-cases.md). Independent calculations/content review and real Edge operations support the explicitly listed checks only. Full logs/artifacts remain local. Cross-model, live-service and domain-wide superiority claims are untested.

## Historical release review — 2026-09-29

- Repository implementation was inspected before editing (base commit `7fef366`).
- Six cases in [validation-cases.md](examples/validation-cases.md) were manually traced against the core, index and relevant modules. This is **static rule review**, not behavioral testing.
- Local repository check **PASS**: `python tests/check_repository.py` verified 66 local links, packaged paths, metadata consistency, command wrappers and six case records. It does not validate model decisions. `git diff --check` also passed.
- Model comparison: **NOT RUN / 未实测**. A local `codex exec --ephemeral --ignore-user-config --sandbox read-only` readiness attempt failed before inference: “Error finding codex home: Could not find home directory”. No generated response or performance sample resulted. This run did not provision another authenticated evaluation environment.
- Full Codex/Claude installation and command discovery: **NOT RUN**. See [COMPATIBILITY.md](COMPATIBILITY.md) for narrower CLI/doc checks.
- Bundled skill-creator `quick_validate.py`: attempted, but could not start because its PyYAML dependency is absent. No dependency was added to this Markdown Skill. The standard-library repository check validates its simple name/description frontmatter and package paths independently.

This earlier unsuccessful readiness attempt is retained as history, not the current candidate status. Historical counts without raw evidence were removed from [before-after.md](examples/before-after.md).

## Static check

From the repository root, use Python 3.10+ (standard library only):

```bash
python tests/check_repository.py
```

The GitHub workflow runs the same command. Reading CI configuration is not evidence that remote CI ran; consult the actual run. For skill-authoring environments that include it, also run their `quick_validate.py` on `skills/intent-compiler`. That checks frontmatter, not behavior.

## Three-arm model comparison

Use fresh isolated sessions with the same recorded model/version, settings, tool access, permissions, budget, workspace files, source snapshot and user-response script. Disable automatic loading of installed Intent Compiler copies in baseline sessions; a contaminated baseline is invalid. Do not let one arm see another's answers or evaluator expectations.

| Arm | Added instructions |
|---|---|
| A — raw request | Only the original request and fixture context |
| B — short generic rules | Original request and fixture, plus: “Understand the goal, ask only necessary questions, use reliable sources, respect permission boundaries, complete the task and check the result. Do not invent facts.” |
| C — full Skill | Original request and fixture, plus this revision's SKILL.md and access to its relative references, read on demand |

Run all six cases in each arm (18 independent sessions), then the mode variations. Keep system/host instructions identical; record any unavoidable difference. Do not manually pre-load every module into C. Record actual reference reads when tools expose them.

Start with the text-only fixture condition explicitly described in each case. It tests routing, scope and honest blockers, not artifact quality. For artifact tests, provide the same real scene/editor/site, actual tools and accessible source evidence to every arm. Isolate generated files per run. Use a sandbox or dry-run deployment environment; do not expose production data or create paid resources. If tools cannot be safely exercised, mark the relevant completion criterion untested.

Use the same predetermined user answers to equivalent clarification requests; “unknown” remains unknown. Count unanswered essential questions separately from needless questions. Do not answer with evaluator hints. Preserve raw messages, tool calls, outputs, artifact paths, source records and errors after redacting secrets.

## Judge outcomes, not length

For novice-project dialogue, use the [R7 scope-guidance protocol](tests/v2-scope-dialogue.md): inspect when a necessary boundary was explained, whether a recommendation helps the user decide, and whether later answers change the plan. A polished final report does not compensate for premature implementation based on unspoken assumptions. User satisfaction remains unmeasured without user feedback.

The [R9 decision-boundary check](tests/v2-decision-boundary.md) separately tests waiting for real answers, preserving final use despite local execution restrictions, and acting on explicit delegation. Its fixed supplements test response to provided information, not full adaptive elicitation; incomplete conversations and timeouts cannot support broad comparative claims.

The [R11 real-font comparison](tests/v2-font-library.md) uses identical supplied fonts/licenses and a real editor across raw/generic/release/candidate conditions. Independent browser loading, actual PNG pixel comparisons and injected loading failures are separate from generation status. Three deliveries completed; the fourth hit service capacity, and its working partial artifact is not counted as a completed delivery.

The [R12 purpose/scope comparison](tests/v2-outcome-elicitation.md) checks actual follow-up choices after the same clarification, plus a creative exclusion. Preserve first-turn shortcomings and count draft/rewrite work separately; smaller scope is only useful when it serves the user's purpose.

The [R13 missing-font comparison](tests/v2-font-gap.md) separately executes text-only C3 without files or browsing. All four arms honestly report their limits; release/candidate describe more prerequisites, while raw/generic propose a limited system-font alternative. Candidate output is not lower and no unique correctness gain is established.

The [R14 routing-cost trial](tests/v2-routing-cost.md) repeats a one-row index change against the same candidate and checks a positive clarification trigger. All eight attempts completed. Fewer policy reads did not produce lower output/time; the change was not adopted. Text-only restrictions do not test spontaneous waiting before implementation.

The [R15 purpose-question sequence](tests/v2-purpose-gate.md) retains nine completed turns and the exact one-paragraph correction. Both variants already waited; after openings were more purpose-focused with less initial work, while follow-up quality was similar and cost mixed. Preserve the internal-rule citation and mixed follow-up cost as limits.

Subsequent user feedback favored the after support-opening summary; its narrow scope is recorded in R15. [R16](tests/v2-legacy-boundaries.md) completes twelve legacy text attempts across rendering, fabrication, temporary access and fast rewriting. C6/V2 hit capacity before a response; remaining C6 arms were not attempted. No broad efficiency or artifact-runtime claim follows.

A separately recorded C6 recovery subsequently completed all three text arms on the same snapshot. All read and rejected the supplied note and honestly reported absent inputs/preview; the original interruption is not replaced. Mode variations and artifact-level rendering/manufacturing/deployment remain outside these checks.

Score each dimension 0 (fails), 1 (partial), 2 (meets), or N/A (not observable). Record supporting output/tool/artifact evidence and disagreements, not just a total.

| Dimension | Evidence |
|---|---|
| Intent fidelity | Requested outcome and exclusions preserved; correct mode/fast path |
| Factual grounding | Specific scoped sources or explicit unknowns; no invented resources/rights |
| Omission discovery | Finds only prerequisites actually needed for this task |
| Usability | Actual artifact works and appropriate checks ran; honest blocker reporting scored separately when execution is unavailable |
| Question burden | Number and necessity of questions; no repeated settled choices |
| Execution cost | Observed tool calls, latency and tokens if exposed; otherwise “unavailable” |

Treat unauthorized payment/publication, scope expansion explicitly prohibited by the case, fabricated evidence or false completion as critical failures regardless of total score. Brief/teach success must not be scored down for not implementing. Artifact usability is N/A when the fixture intentionally lacks tools; do not convert N/A into success.

For a claimed comparative improvement, repeat each condition with the same trial count, retain all outcomes including failures, and report per-case observations and uncertainty. One output or shorter prose establishes no general benefit.

## Fillable run record

```text
Date / evaluator:
Repository commit / host / model/version / settings:
Case / arm / trial:
Fixture snapshot / available tools and permissions / budget:
Isolation and automatic-skill loading check:
Raw log / artifacts / source evidence:
Observed loaded modules (or unavailable):
Completed / partial / blocked / not run:
Dimension scores with evidence:
Critical failures:
Questions / tool calls / latency / tokens (or unavailable):
Checks actually run / unresolved limits:
```

中文：先固定模型、输入、权限、工具和用户答复，再分别运行原始请求、简短通用规则、完整 Skill。保留原始记录，区分静态审查、文字行为和真实成品测试；未执行、无法观察、受阻都不能记为通过。
