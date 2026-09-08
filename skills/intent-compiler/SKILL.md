---
name: intent-compiler
description: Turn vague or ordinary-language goals into domain-aware execution briefs and finished results for non-technical users. Use when a user knows the outcome they want but may lack prompt-engineering, design, research, office, 3D, product, or coding vocabulary. Do not use merely to rewrite an already precise prompt unless the user asks for refinement.
license: MIT
---

# Intent Compiler

Let the user speak naturally. Reconstruct the real outcome, add only the professional structure the task needs, then do the work.

## Modes

- `do` (default): compile internally, execute, check, and deliver. Do not show the internal brief unless useful.
- `brief`: return a compact execution-ready brief; do not execute it.
- `teach`: explain the few domain concepts or decisions the user needs in plain language, then offer a usable brief.
- `improve`: evaluate an existing draft against its intended outcome and return a repaired version.

Infer the mode from the request. An explicit mode wins.

## Compile the request

Identify only what changes execution:

- desired outcome and deliverable
- audience and use context
- supplied source material and facts
- hard constraints, preferences, and exclusions
- relevant domain standards
- definition of done

Treat wording, tone, format, and professional terminology as implementation details when the user has not chosen them.

## Resolve gaps

Proceed with a visible, reasonable assumption when it is reversible and low impact. Ask one concise question only when the answer would materially change the deliverable, authorize an external commitment, affect safety or privacy, or supply an input that cannot be recovered elsewhere.

Never make the user translate their request into prompt-engineering language. When asking, describe the real-world choice and its consequence.

For the full rule, read [clarification-policy.md](references/clarification-policy.md).

## Add domain knowledge

Read only the relevant section of [domain-lenses.md](references/domain-lenses.md). Use professional vocabulary and standards internally; explain them only when they help the user decide or learn.

For visual, UI, image, and 3D work, also read [visual-quality.md](references/visual-quality.md).

## Execute

In `do` mode, use available tools and source material to produce the deliverable. Do not stop after emitting a prompt, plan, or checklist unless that is the requested deliverable.

Preserve the user's authorization boundary. A compiled brief clarifies intent; it does not grant permission for purchases, publishing, sending messages, deleting data, or other external actions.

For current facts, research, legal, medical, or financial claims, verify with suitable authoritative sources rather than filling gaps from intuition.

## Check once

Before delivery, compare the result with the outcome, audience, constraints, source facts, and relevant domain standards. Repair material misses once. Do not expose routine self-critique or loop indefinitely.

Use [quality-check.md](references/quality-check.md) when the deliverable is substantial or crosses domains.

## Output

Lead with the finished result. Mention assumptions only when they affect how the user should interpret or use it. Keep explanations at the user's level and offer the compiled brief only when requested.
