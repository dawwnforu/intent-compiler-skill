<p align="center"><img src="skills/intent-compiler/assets/intent-compiler.svg" width="220" alt="Original Intent Compiler line-art avatar"></p>

# Intent Compiler

**Describe the outcome. The agent discovers, retrieves and applies the knowledge needed to get it done.**

[中文](README.md) · [MIT License](LICENSE)

2.0 now checks usefulness beyond the first successful action: add supporting capabilities when the actual workflow warrants them, rather than cutting utility to shorten output. [Loan and quotation comparisons](tests/v2-practical-utility.md) record concrete additions, higher costs and incomplete UI verification.

[Current candidate decision and optional starter prompt (Chinese)](docs/v2-decision.md) separates observed improvements from unresolved effectiveness claims. The broad goal remains open; the next behavior change should target an observed decision or user-experience failure, with fixed baselines and unseen transfer checks rather than more synonymous instructions.

Source guidance is shorter while retaining evidence, scope and verification dates. Four project-record/font-evidence comparisons preserve required judgments; this is not established general token savings. See [tests and limits](tests/v2-evidence-trim.md).

Source questions and repeated workflows now route separately, combining only when needed. [Four actual comparisons](tests/v2-route-split.md) show narrower loading for source questions, without establishing overall time or token savings.

Candidate workflow guidance now distinguishes proposals, conditions, confirmed decisions and quoted terms, and checks updates to derived records. The [latest actual comparison](tests/v2-status-evidence.md) shows only partial improvement, with remaining errors and higher cost; general semantic understanding is not established.

This branch develops a **2.0 candidate**; the released version remains 0.2.0. It adds task-specific rules for surveys/data, interactive motion, workflows, web runtime, print layouts and game mods while reducing redundant narration and unsolicited documents. Effectiveness requires the [four-arm evaluation](tests/v2-protocol.md); [research hypotheses](docs/v2-research.md) and [reconstructed cases](examples/v2-cases.md) are not improvement claims.

An intent-driven, knowledge-enhanced workflow for non-technical users. Users need no prompt-engineering, coding, design, deployment or asset-licensing vocabulary. A longer prompt is not the default deliverable.

```text
Understand intent → route knowledge → retrieve what matters → discover prerequisites
→ explain consequential choices → execute within authorization → verify → deliver
```

## Behavior

Simple edits go straight to the result. For substantive work, inspect context and existing artifacts, keep a compact execution brief, and consult the [knowledge index](skills/intent-compiler/references/knowledge-index.md):

1. Required now: read the relevant module/section.
2. Conditional: load only when its actual dependency appears.
3. Irrelevant to delivery: leave unloaded and out of scope.

Stop retrieval when prerequisites and acceptance are clear with no new critical gap. If necessary evidence is inaccessible, stop that branch, finish independent work and name the blocker. Never invent business facts, budgets, permissions, sources or completion.

For an unfamiliar project with unsettled scope, clarify the goal and consequential choices before substantial implementation. A feature list is not its purpose: if the job, experience or decision this version enables is unclear, ask a concrete purpose question with enough explanation to answer before drafting detailed scope. Then explain what stays and what can wait. Preserve reaffirmed creative requirements and real-use conditions. Explain concrete effects at the user's stated experience level instead of delegating architecture questions to them; execute once enough is known without reopening settled choices. This guidance belongs in the conversation; delivery reports actual completion and remaining gaps. It is not a claim that every latent need can be inferred correctly.

Distinguish final use, current execution limits and confirmed choices: “do not publish now” does not mean “only a demo.” Recommendations and silence are not user answers. Wait on work affected by a necessary missing answer, while executing explicitly delegated low-impact choices. Reliability still requires evidence; see the [decision-boundary check](tests/v2-decision-boundary.md).

## Three core scenarios

| Goal | Missing knowledge supplied | Boundary |
|---|---|---|
| Render or fabricate a product | Models/references, materials, lighting, composition and output; dimensions, units, materials, process and assembly only for physical use; mechanics only for relevant functional demands | No fabrication escalation from rendering; an image proves no strength |
| Add an editor font library | Real files, loading/fallback, glyph coverage, source/license and use-specific rights | A dropdown is insufficient; “free” does not authorize every use |
| Let others access a website | Existing stack/runtime, backend/storage/auth/uploads, public content, account/deployment prerequisites and real access checks | Distinguish local preview, temporary demo, persistent deployment and custom domain; no assumed payment or exposure of private data |

Prices, official capabilities, licenses and regional requirements are verified against applicable authoritative sources at execution time, recording source, scope and date. Static docs promise neither fixed prices nor permanent free service or blanket compliance.

## Install and use

Non-programmers can give their current agent the repository URL and ask it to check the host's supported installation method, install the Skill and verify discovery. Host permissions still apply.

Codex CLI (syntax checked against local CLI help; full installation untested):

```bash
codex plugin marketplace add dawwnforu/intent-compiler-skill
codex plugin add intent-compiler@intent-compiler
```

Claude Code (checked against official documentation; full installation untested):

```text
/plugin marketplace add dawwnforu/intent-compiler-skill
/plugin install intent-compiler@intent-compiler
```

Start a fresh session and check discovery. Alternatively copy the complete `skills/intent-compiler` folder to the host's supported local Skills location. See [COMPATIBILITY.md](COMPATIBILITY.md) for paths, manifests, invocation differences, source dates and smoke checks. A GitHub repository is not a public plugin-directory listing or a universal compatibility claim.

Codex examples:

```text
$intent-compiler do -- Add a usable font library to my editor.
$intent-compiler brief -- Outline website launch requirements without deploying.
$intent-compiler teach -- Explain why this joint affects printed-part assembly.
$intent-compiler improve -- Inspect and repair this existing proposal.
```

`do` executes and verifies; `brief` delivers a specification only; `teach` explains necessary concepts; `improve` preserves constraints and repairs an existing artifact. Brief/teach do not implement external actions. Claude uses namespaced invocation; see the compatibility guide.

## Capabilities and dependencies

This project supplies Markdown behavior, routing, domain judgments, evidence boundaries, acceptance rules and cases. Routing is followed by the host model, not an independent program; model compliance is not guaranteed.

Retrieval, file editing, image generation, modeling and deployment depend on the host model, specialist skills/tools, source access, accounts and authorization. Installing this Skill does not supply those tools or credentials. There is no database, backend service or paid API dependency. Optional repository checks use Python's standard library; the Skill requires no Python runtime.

## Validation and maintenance

[Six regression cases](examples/validation-cases.md) cover render-only scope, fabrication prerequisites, font resources/rights, deployment exposure/cost, fast text edits and unavailable data/tools/permissions.

The frozen candidate snapshot has 67 actual generations, including 24 new-task runs across two tasks, four arms and three repetitions, with independent content/runtime checks. It had lower median output than V1 on both repeated tasks; general superiority over generic instructions was not established. Later dialogues exposed an aggregate/per-item rule error; the repair has a separate three-turn regression and two positive/negative transfer checks. Earlier cost figures do not validate the new repair's efficiency. Read [results and limits](docs/v2-results.md) and [testing methods](TESTING.md), including failures and worse outcomes.

A separate [real-font four-arm trial](tests/v2-font-library.md) had three completed deliveries and one service-capacity interruption. All saved pages passed independent offline loading and PNG pixel checks; the interrupted run remains a partial artifact. Candidate output was lower in this sample, without a unique core capability or stable superiority claim.

Six additional efficiency regressions on the repaired version preserved core statistics and basic UI functionality, but UI output/time medians exceeded the historical V1 results. Universal token savings are not established; the specific correctness repair and efficiency tradeoff are reported separately.

A later browser-capability-probe paragraph was tested and removed: two complete pairs disagreed, and the last attempt hit an account usage limit. All attempts remain recorded; interruption is not counted as a saving or a completed comparison.
A separate recovery after usage became available completed and passed independent page checks, without establishing a reliable cost benefit from that paragraph.

To add knowledge, fill the [Markdown template](skills/intent-compiler/references/knowledge-module-template.md), add an index row and cases. No routing code changes are needed. See [MAINTAINING.md](MAINTAINING.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

CI runs `python tests/check_repository.py` for links, packaged paths, manifest consistency and case completeness. This does not establish model behavior or host installation success.

## Entry points

- [SKILL.md](skills/intent-compiler/SKILL.md): core behavior and modes.
- [references](skills/intent-compiler/references/knowledge-index.md): conditional domain guidance, sources and acceptance.
- [examples](examples/validation-cases.md): regression cases alongside existing office, design, research and coding examples.
- [CHANGELOG](CHANGELOG.md): behavior and compatibility changes.

The user expresses the outcome. The system supplies necessary knowledge and does the work, without inventing facts or authority, expanding requirements, or claiming unverified completion.
