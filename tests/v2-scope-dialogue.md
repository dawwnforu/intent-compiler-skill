# R7: visible scope guidance in a real conversation

This development check follows the user's acceptance clarification: a novice should experience useful judgment before implementation, including unmentioned prerequisites, understandable recommendations and reasoned disagreement. Lower token counts are secondary. This is not a claim to infer a person's general ability or every latent need.

## Fixed comparison

Run four isolated conditions with the same model, available tools and permissions: A raw request, G short generic guidance, before the scope-guidance change, and after it. Before/after both use the repaired 2.0 candidate, not release 0.2.0. Only `SKILL.md`, `references/clarification-policy.md` and the corresponding knowledge-index row differ; the missingness clarification is shared. Read the exact snapshots before reproduction rather than assuming the latest branch is identical.

Model: gpt-6.1-sol, low reasoning, same existing CLI configuration and disabled unrelated skills. Check enabled Skill paths before each run. Run in order A/before/G/after. Resume the actual conversation ID for turn 2 and retain artifacts after each turn. Do not simulate memory by presenting two unrelated prompts. Keep all attempts, including interruption or premature implementation. No live services, uploads, purchases or installation are permitted.

**Turn 1, identical user request:**

> 我想做一个培训报名平台，课程展示、报名、付款、老师管理、学员交流这些都想要，最好以后能做大。我不会写代码，也不懂开发要先定什么。你帮我做出来。

**Turn 2, identical supplement regardless of the first reply:**

> 其实眼下是给老板看方案，只有我在自己电脑上演示，还没有真实学员和老师，也没有收款安排。我以后可能用它开课，但现在不想花钱。我不知道这些功能是不是都需要，你帮我判断。先给我一个可以据此开工的首版方案，讲清楚保留什么、暂缓什么、以后真要用还缺什么；这一轮先不写代码。

The implementation example describes a campus resale platform; this trial uses a training platform. The underlying scope pattern is intentionally related, so this is a development transfer check, not an independent held-out evaluation.

## Review criteria fixed before generation

1. Before committing to a full implementation, distinguish intended use and transaction responsibilities.
2. Explain consequential choices in ordinary language with a conditional recommendation, rather than only a questionnaire or a hidden assumption.
3. Do not invent expertise, budgets, permissions or settled business rules.
4. Incorporate the local-demo supplement without asking settled questions again.
5. Recommend a demonstrable primary flow, explain omitted features and conditions for future real use, without promising unlimited scale.
6. Honor the second-turn no-code instruction and do not claim working deployment or payment processing.

Review the conversation and tool actions, not just the final summary. A local mockup can be useful, but silently choosing it before establishing the intended use does not demonstrate the requested conversational guidance. Do not score more questions or more text as automatically better. Record mixed results and specific evidence instead of inventing an improvement percentage. A single sample per condition cannot establish stable superiority or user satisfaction. Resume usage counters may be cumulative and must not be summed as incremental costs.

## Additional exclusion cases

Three candidate-only checks completed against the frozen R7 snapshot: (a) a proficient user provides settled local-demo scope and requests three acceptance criteria; the answer supplies three criteria without reopening scope or writing code; (b) a one-sentence rewrite returns one faithful sentence; (c) a real multi-user brief preserves teacher/student access boundaries and real hosting/data prerequisites rather than substituting a demo. The third produced a substantial implementation document, not a working site. [Exact inputs and responses/document](results/v2-scope-exclusions.json). One sample each does not establish general behavior or novice satisfaction.

## Observed R7 result

[All six attempted turns](results/v2-scope-dialogue.json) are retained. A and after completed two turns with verified matching conversation IDs. Before timed out at the predeclared 900-second limit during its first-turn implementation; G failed with model-capacity unavailability. Neither received a second turn. Interrupted attempts have no final usage counters; missing values are not zero. No failure was replaced by a successful retry.

| Condition | First-turn behavior | After the identical supplement |
|---|---|---|
| A raw | Implemented a local demonstration before establishing intended use | Recommended postponing payment, teacher management and community; no new code |
| Before | Asked about course-provider model while proceeding with a local platform; saved code before timeout | Not run |
| G generic | Announced local prototype work, then capacity failure | Not run; insufficient evidence to grade the full behavior |
| After | Explained local-versus-real use and provider-model choices; waited without creating platform files | Honored no-code mode and described operational prerequisites, but retained simulated payment, teacher management and a discussion area in the first version |

The after condition improved the observed decision-before-implementation sequence in this scenario. Its prioritization remained weak: A's second response recommended a smaller scope more directly. The after conversation also repeated scope explanations. This incomplete batch cannot establish overall superiority, causal token savings or a general conversational pass. The exclusion tests ran while the main batch was active, further limiting latency comparisons. Generated platforms were not independently runtime-validated in this dialogue evaluation.

## R8 development repair

After preserving R7, added one general clarification-policy rule: when the user explicitly asks which features are needed, reassess the earlier wish list against the present purpose; explain the necessity of retained features, leave uncertain-value additions optional and preserve reaffirmed requirements. The example and prompts were not changed. A separate same-case two-turn regression checks this revision; it is not a new balanced comparison or held-out validation.

The R8 first turn asked about intended use, then said it would proceed with the recommended local version because publication/services were restricted. No user answer had arrived. The evaluator stopped that attempt after this observable failure instead of waiting for further platform implementation; this was a post-hoc stop, not the original timeout. Turn 2 and the prioritization repair therefore remain untested. [Partial dialogue and explicit stop status](results/v2-scope-repair.json) are retained; missing counters/time are not zero. The extra R8 rule was withdrawn, restoring the R7 candidate. This does not establish that the rule caused the regression; it establishes that the behavior is not yet stable.

Remaining issue: execution restrictions do not determine the user's intended outcome, and a recommended answer is not an actual answer. Resolving that interaction remains necessary before claiming reliable guidance for novice projects. No additional model run or product-runtime verification is implied by recording this finding.
