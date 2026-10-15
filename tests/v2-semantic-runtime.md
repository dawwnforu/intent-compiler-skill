# R56: real semantic-runtime feasibility

Status: protocol frozen before invocation; not yet run. [Exact input, prompt and runner](results/v2-semantic-runtime.json).

R55 identifies a finite-pattern limitation in a previously generated processor. Before adding another Skill paragraph, invoke the existing host model on exactly those source statements, without labels, old code or evaluation findings. Require source evidence, a decision/unresolved status and a brief explanation; preserve ambiguity rather than silently treating the coarse labels as perfect ground truth.

This is a method feasibility check, not a Skill A/B result. It adds no paid API integration, dependency, database, service or unattended product. The normal isolated evaluation runner disables other Skills, browsing and tool network access, while using its existing authenticated model connection. Keep the current runtime Skill unchanged.

On2026-10-15, local `codex exec --help` confirmed noninteractive invocation, last-message output and optional output-schema flags. The official [iterative repair example](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex), structured-output/review sections, illustrates machine-readable phase handoffs and checking process results. That supports an invocation mechanism, not meeting-classification accuracy or an account's availability. This probe asks for JSON but does not enforce an output schema; actual response validation remains required. No API key was read or changed, and no API-backed application was built.

If the batch works, the next requirement remains real repeatable integration: source/version identity, validated results, truthful unavailable/failed states and nonduplicating retry. A one-time model answer cannot be presented as a working automatic semantic workflow. If it fails, retain the failure without silently falling back to keyword guesses or pushing every clear decision back to the user.
