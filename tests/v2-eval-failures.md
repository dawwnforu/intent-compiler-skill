# R68: evaluation failure records

Adopt the bounded common-runner repair, not a Skill behavior change. R66's failed preflight left only a workspace; both common runners previously wrote terminal metadata only after successful setup. A failed setup could therefore obscure the original error with a later missing `run.json` read. No old snapshot or result is replaced.

## Changes

The local single-turn and two-turn runners now retain failure stage, error, direct execution start status and terminal metadata for setup, Skill isolation, interpreter preparation, command launch, exit, timeout and continuation validation. Existing `exit_code` and `wall_seconds` remain: execution duration when attempted, otherwise time to preflight failure; `elapsed_seconds` includes setup. A failed continuation keeps the actual `process_exit_code` separately and does not report overall success. No response or token usage is fabricated. For dialogue, arm-level metadata covers setup failure before `turn1` exists; each attempted turn retains its own record. Failure stops later turns.

App-server discovery preserves its stderr, reports closed stdout immediately instead of waiting for the RPC timeout, checks RPC errors, and terminates/waits for the direct probe process. No broader process-tree termination, safety-setting change or automatic retry is added. Historical specialized runners/exporters are not automatically migrated; they must inspect terminal status before assuming generation artifacts exist.

## Actual evidence and reproduction

[Frozen sources, inventory, original and replay results, raw local logs](results/v2-eval-failures.json). Reconstruct in a **new writable directory** using the existing Python interpreter:

```text
python tests/replay_eval_failures.py <new-writable-directory>
```

The launcher reconstructs the two helpers, their existing dependency/inventory and the check driver. It runs short local Python children and controlled failures, never `codex exec` or a model turn. It also attempts one real `codex app-server` discovery under existing permissions, with web search and sandbox network disabled; no global configuration changes. A future replay can produce a different host discovery result.

The first 10 driver checks passed; the replay added dialogue-preflight coverage and a well-formed missing-thread event probe, and passed all 11 checks. These cover failed isolation/environment, missing executable, normal and nonzero exit, real child timeout, failed dialogue setup/first turn/continuation, successful controlled two-turn transport, and prompt EOF/reaping. Controlled transport is **not an actual successful model execution or resume**. The launcher was actually exercised from the archived sources; no new dependency or model call was needed.

Real host discovery still fails with access denied while initializing the state runtime under the existing `.codex` directory. The new runner records the failed discovery in approximately 0.08 seconds and retains its stderr. CLI version was actually observed as `0.163.0-alpha.10.2`, evaluator Python as `3.12.14`, and Node as `v24.18.0` on 2026-10-18. The shell's plain `python` resolves to a WindowsApps alias; the existing evaluator interpreter remains explicit. These observations do not establish current model availability, a refreshed Skill inventory or model-side tools.

## Boundaries and next action

No Skill/core/knowledge route, MIT, installed version, external publication, model choice or permission changed. Existing R62/R67 local improvements and R63/R65 shared outcomes retain their original meaning. This cycle improves failure diagnosis, not output quality, cost efficiency or compatibility.

Current real model/discovery execution remains blocked by state-runtime access. Resolve that access within the host's supported permission configuration before another behavior comparison; do not disable safety, relocate credentials, expand network permissions or fabricate a successful run. Direct-process reaping is checked, not arbitrary descendant cleanup. Successful-run legacy key compatibility is exercised locally; frozen historical callers/exporters are not all rerun. Static checks and this driver evidence do not establish desktop installation or Claude Code compatibility.
