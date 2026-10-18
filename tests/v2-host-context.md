# R69: restore actual local evaluation through the approved launcher

R68 improved failure records but did not establish that the host itself was broken. This cycle tests the narrower alternative: a restricted outer command cannot initialize Codex's existing state, while an approval-mediated host launch may work without changing the model's tool sandbox. This affects whether an ordinary local task can reach any actual model/tool execution at all; adding another domain rule would not resolve it.

## Frozen budget and acceptance

[Exact protocol, runner, snapshot, metadata, commands, failures and independent acceptance](results/v2-host-context.json). Base commit is `5c76520`. Two discovery attempts, then at most one `gpt-6.1-sol` / low smoke generation with a 120-second timeout; no failed-model resampling. No A/G/Skill or before/after product comparison is claimed. R62/R67 gains and R63/R65 shared results remain separate historical evidence.

Both discovery attempts use the same executable arguments and workspace. Only the reviewed outer launch context differs. Accept recovery only after actual model/Skill discovery, verified isolation, and an actual model-generated receipt whose values match real command events and independent interpreter checks. Keep all failed commands and stop if the single model run fails.

## Observed result

- Restricted discovery fails in 0.09 seconds while initializing the existing `.codex` state runtime. The stderr and terminal record remain intact.
- The same discovery script invoked through `exec_command` with `require_escalated` succeeds in 1.88 seconds after approval. It lists the exact historical model `gpt-6.1-sol` with low effort supported and 25 Skill entries. No model name substitution, state database repair, ACL edit, credential relocation or global configuration change was needed.
- The initial stale inventory leaves newly relocated plugin paths enabled; this is not accepted isolation. The existing inventory-refresh method disables those paths before the model is launched. The actual smoke inventory contains exactly one enabled Skill: the frozen current Intent Compiler. A listed/enabled Skill is separate from actual use: its body was also read in a recorded shell command.
- One actual CLI smoke completes in 25.55 seconds, with 676 output tokens (59,802 aggregate input tokens, 38,400 cached). It reads the exact synthetic marker, obtains Python `3.12.14` and Node `v24.18.0` plus executable paths, and writes a real `receipt.json`. These counters are not an efficiency comparison or billable-cost estimate.
- One model-authored Python quoting command fails with `NameError`; the next command uses simpler actual version/path probes and succeeds. Both commands are preserved. This is an internal repair within one generation, not an extra sampled model run.
- Parent acceptance checks the unchanged frozen Skill and input, only-one-Skill inventory, configured sandbox/network flags, parsed receipt against successful command output, and independent existing Python/Node paths and versions. No self-rating or subjective product score is involved.

## Operational change to retain

Use the supported approval path for the **outer evaluation launcher** when the restricted command cannot initialize the host state. The evaluator must not silently retry outside its permissions or disable the child sandbox. Approval authorizes that launch, not arbitrary future launches or generated commands. Keep `workspace-write`, disabled web search, disabled child network and Skill isolation in the actual CLI invocation. If approval is unavailable or denied, keep the failure record and stop that branch.

App Server is the local control interface; model tool permissions remain a distinct sandbox/approval concern. See [official App Server documentation](https://learn.chatgpt.com/docs/app-server) and [sandbox documentation](https://learn.chatgpt.com/docs/sandboxing), consulted for this diagnosis on 2026-10-18 UTC. No full-access or external-sandbox mode was used. The existing elevated Windows sandbox setting is retained; this is not a request to turn off sandboxing.

The frozen runner remains in the result record. To reproduce deliberately, reconstruct `sources` into a new `work/` directory under a writable project root, restore `snapshot` into `work/intent-compiler-skill/skills/intent-compiler`, create `outputs/intent-compiler-v2`, and use the existing Python interpreter:

```text
python work/v2_host_recovery.py prepare
python work/v2_host_recovery.py discover restricted
```

Then request host approval for the **same script** with `discover approved-host`. Only if that succeeds, request approval for its single `smoke` action, then run `python work/verify_host_recovery.py`. The launcher itself cannot grant those approvals. `prepare` refuses an existing experiment folder; `smoke` refuses an existing terminal result. Raw model/Skill metadata can vary on a future host; preserve it rather than overwriting this result. No API key or service installation is required by these instructions; they rely on the user's existing authorized local Codex environment.

## Decision and limits

Adopt this launch diagnosis and workflow documentation; no new Skill rule or common-runner code is justified. The current environment is usable through the approved launch path. The R68 restricted-context failure remains true for that context and is not rewritten as a successful historical run.

No exhaustive sandbox-enforcement or unauthorized-operation denial test, real resumed model dialogue, UI/mobile validation, desktop installation, Claude Code compatibility or domain quality improvement is established. The model had no reason to invoke adjacent knowledge modules. PATH preparation is local to this smoke child; the host PATH is unchanged. Only explicit Python/Node and this task's shell operations are verified. Any later A/G/Skill comparison must freeze its own inputs/versions/budget and apply the same approved launcher and child restrictions to all arms.
