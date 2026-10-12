# 2.0 candidate: research and hypotheses

Status: development, not a released or validated effectiveness claim. Reviewed 2026-10-11 UTC. The Skill changes instructions and available task knowledge; it does not retrain the host model or reveal a proprietary model's internal mechanism.

| Source | Read scope | Design hypothesis, not a reproduced finding |
|---|---|---|
| [Transformer](https://arxiv.org/abs/1706.03762) | Abstract | Interpret context rather than isolated trigger words; no claim to modify attention |
| [InstructGPT](https://arxiv.org/abs/2203.02155) | Abstract | Separate model capability from extra instructions; include a generic-instruction baseline |
| [Schema-Guided Dialogue](https://arxiv.org/html/1909.05855v2) | Abstract and accessible paper body | Describe domain outcomes and necessary fields in natural language; carry unresolved task state across turns |
| [AmbigQA](https://arxiv.org/abs/2004.10645) | Abstract | Detect materially different interpretations before committing to an artifact |
| [ReAct](https://arxiv.org/html/2210.03629v3) | Abstract, action/observation and evaluation passages | Update work from tool observations; do not replace runtime verification with a written plan |
| [Lost in the Middle](https://arxiv.org/abs/2307.03172) | Abstract | Load relevant sections, preserve constraints and avoid gratuitous context growth |
| [Intrinsic self-correction limits](https://arxiv.org/abs/2310.01798) | Abstract | Trigger repair from external evidence rather than repeated unsupported self-critique |

These studies cover different models and tasks. Ambiguous QA is not engineering intent recognition; historical long-context results do not establish today's model performance; lack of intrinsic correction does not imply externally verified repair is impossible. No paper's improvement percentage is attributed to this Skill.

## What is being tested

The candidate removes repeated execution narration and unsolicited secondary guides, represents outcome/inputs/constraints before domain routing, and adds concrete decision rules for interactive products, survey work, workflows, shared web state, print dimensions and game mods.

Hypotheses: fewer unsupported assumptions and omitted prerequisites; equally usable artifacts with less nonessential narration; more relevant validation. Counter-hypotheses: the base model already does this; additional modules cost more than they help; concise delivery hides necessary explanations; domain routing overfits examples.

Test all of these with [the evaluation protocol](../tests/v2-protocol.md), including unchanged and worse results. Keep research out of routine Skill loading.

## Dialogue follow-up reviewed 2026-10-12

| Source | Actual read scope | Application and limit |
|---|---|---|
| [Clarify When Necessary](https://arxiv.org/pdf/2311.09469) | Abstract, then PDF sections 2.1 and 6.1 on 2026-10-12; the earlier v3 HTML attempt was unavailable | Separate ambiguity from missing knowledge and assess whether clarification can improve the answer. INTENT-SIM samples possible user answers and groups them with a separate NLI model. That estimator and its experiments are not implemented or reproduced here. |
| [ClarQ-LLM](https://arxiv.org/html/2409.06097v2) | Abstract, introduction and sections III–V on task construction, provider behavior and evaluation | Evaluate acquisition of required information, not similarity to a preferred sentence; guessing a correct answer is not confirmed intent. Track irrelevant/repeated questions separately. Our fixed-supplement tests do not replicate its adaptive provider or establish human satisfaction. |

The [GOV.UK alpha guidance](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works), read in the overview, risky-assumptions and scope passages, motivates a separate product-judgment hypothesis: a prototype should help resolve a consequential uncertainty. Do not score fewer features as automatically better; examine the decision each feature supports. This is transferable design guidance, not a requirement to import government delivery phases or a claim that our current candidate reliably prioritizes features. No new runtime guidance was added during the frozen R9 batch.

The later PDF read makes the implementation boundary more concrete: uncertainty alone is not a reason to ask the user. Missing specialist knowledge may require retrieval; an unknown user choice may require clarification. This is a design interpretation, not an entropy estimator. Reproducing the paper's sampled-answer/NLI pipeline would add calls and a model dependency; this lightweight Skill does not silently introduce them or claim their reported gains. Its question quality still needs observed task outcomes and real answers.

## Meaning-changing checks reviewed 2026-10-12

[Evaluating Models' Local Decision Boundaries via Contrast Sets](https://aclanthology.org/2020.findings-emnlp.117/) (Gardner et al., 2020): read the abstract and PDF sections 1 and 2.1–2.4. The paper motivates small, meaningful changes with expert-judged labels, and warns that retrospective examples can be biased by known model behavior. Our workflow checks borrow the distinction between tentative, conditional and confirmed statements, including negative decisions and quoted terms. They are developer-designed tests of generated rule-based code after a known failure, not a reproduction of the paper's datasets, expert annotation process or model-consistency results. No paper performance number transfers to this Skill. Preserve full source statements and review ambiguous expected labels rather than treating matching category words as semantic evidence.
