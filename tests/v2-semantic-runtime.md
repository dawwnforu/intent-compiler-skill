# R56: real semantic-runtime feasibility

Status: actual invocation complete; response and source evidence independently reviewed. [Exact input, prompt, response and runner](results/v2-semantic-runtime.json).

The model correctly interprets all7 unambiguous R55 cases, including the3 clear decisions missed by the old processor. For `defer.txt`, it labels the agreed postponement as a decision while explicitly stating that the budget increase remains unapproved. This is the annotation ambiguity declared before execution, not a fabricated approval; do not convert it into an8/8 accuracy claim by changing the frozen label.

All8 identifiers occur once, statuses are valid, quoted evidence is an exact nonempty source substring, reasons are present, and input text remains unchanged. These mechanical checks are separate from the manual semantic review. The invocation took21.49 seconds; full counters are in the record. No current Skill was enabled, so this is evidence for an available interpretation method, not a Skill improvement or offline replacement.

The next design must keep the object of each decision: postponement can be agreed while expenditure is not. A whole-line status field alone cannot preserve that distinction. This requirement follows from the observed output; it has not yet been implemented or compared in a repeated workflow. No new runtime paragraph is adopted on this result alone.

R55 identifies a finite-pattern limitation in a previously generated processor. Before adding another Skill paragraph, invoke the existing host model on exactly those source statements, without labels, old code or evaluation findings. Require source evidence, a decision/unresolved status and a brief explanation; preserve ambiguity rather than silently treating the coarse labels as perfect ground truth.

This is a method feasibility check, not a Skill A/B result. It adds no paid API integration, dependency, database, service or unattended product. The normal isolated evaluation runner disables other Skills, browsing and tool network access, while using its existing authenticated model connection. Keep the current runtime Skill unchanged.

On2026-10-15, local `codex exec --help` confirmed noninteractive invocation, last-message output and optional output-schema flags. The official [iterative repair example](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex), structured-output/review sections, illustrates machine-readable phase handoffs and checking process results. That supports an invocation mechanism, not meeting-classification accuracy or an account's availability. This probe asks for JSON but does not enforce an output schema; actual response validation remains required. No API key was read or changed, and no API-backed application was built.

If the batch works, the next requirement remains real repeatable integration: source/version identity, validated results, truthful unavailable/failed states and nonduplicating retry. A one-time model answer cannot be presented as a working automatic semantic workflow. If it fails, retain the failure without silently falling back to keyword guesses or pushing every clear decision back to the user.
