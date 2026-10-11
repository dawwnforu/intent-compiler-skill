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
