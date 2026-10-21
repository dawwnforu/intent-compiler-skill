# R79: deliver a versioned Skill candidate without inventing marketplace readiness

## Outcome and scope

Continue the Intent Compiler product goal after R78; 静档 remains evaluation evidence only. Prepare a standalone candidate ZIP and publish it on the existing GitHub candidate branch, with clear deployment/pricing and separate remaining marketplace gates. No new model generations, original-app work, formal-install replacement, Release, PR merge, licence change, seller-account action, customer-data upload or external message.

The [submission plan](../commercial/SUBMISSION.md) uses public primary sources and bounded actual-browser comparable-price observations. The private email review and an unsent proposed reply remain in local `outputs/intent-compiler-v2/submission-r79/`; email text, headers, identities and source business materials are not committed or packaged. Reading correspondence is not permission to send it or to accept platform terms.

## Package that actually exists

- File: `commercial/artifacts/intent-compiler-2.0-candidate-abef76f.zip`.
- Source Git commit: `abef76fae0056073a09e2a95b866050049b2c613`; runtime-method commit: `f51b2ccb7d1ca7b3a5e6e58dcb202b672d1399ed`.
- Size:36,403 bytes;25 members, consisting of24 committed Skill files plus SOURCE.json.
- SHA-256:`24bfdec81a303ec4d9e852d436363eb11129f9ad7887c54004da0ed5b714a490`.
- Root SKILL.md, references, optional checker, agent metadata, original SVG, source README and unchanged standard MIT are included. No pilot logs, mail, source application, experiments, credentials or caches.

`commercial/build_submission.py` reads committed Git blobs, validates the controlled name/description header, allowed paths/types, relative resources and a small set of known credential patterns, writes deterministic ZIP metadata, then verifies CRC, member hashes and provenance. It refuses an existing output file. No new dependency or general YAML/security-engine claim. Five initial tests cover exact/deterministic source, unsafe/unexpected members, missing reference, known synthetic credential pattern and post-build tampering. A sixth test covers shallow Git history: runtimeCommit must be null rather than inventing the last runtime change from incomplete history; sourceCommit and file hashes remain authoritative. The delivered artifact was built with full history and actually records f51b2cc. This does not replace platform scan/manual review or prove absence of all secrets/injections.

Reproduce without overwriting a frozen artifact: `python commercial/build_submission.py <new-empty-directory> --ref abef76fae0056073a09e2a95b866050049b2c613`. Compare the resulting digest with the adjacent checksum file. `python tests/test_submission_package.py` tests structural boundaries; host and model behavior are separate.

The repository's required local CI commands were run: integrity526 links, four HTML-checker tests, the existing trial-encoding check, five submission tests and the original revenue-model self-checks pass. Preserve the reference-input suite's first Windows sandbox-temp permission failure (four of six error on temporary writes/cleanup); rerun only that suite with an explicitly workspace-contained process-local temporary directory, without editing tests, credentials, ACLs or host settings. The first runpy wrapper also omitted the ordinary script-directory import path and failed; adding that process-local path restores the normal direct-script environment and all six tests pass. Both invocation failures remain in the local receipt. This is environment handling, not a Skill gain. The system Skill creator's separate PyYAML-dependent validator remains unverified from R78; these checks are not described as a general YAML validator or platform scan.

## Actual installation and discovery

The new ZIP is verified and extracted into a fresh project at local `outputs/intent-compiler-v2/submission-r79/preflight/smoke/workspace/.agents/skills/intent-compiler/`. Its24 source files exactly match the ZIP bytes. SOURCE.json is present. The existing approved local Codex launch completes forceReload inventory and a sole-project-Skill isolation probe; the enabled path is that extracted project's SKILL.md. This is author-side installation/discovery, not a participant independently starting.

Preserve the initial verifier failure: an exact comparison to R78's historical Windows worktree snapshot failed after extraction. Fifteen runtime files differ only by CRLF/LF; decoded text is equal after line-ending normalization. The archive remains exact committed Git bytes. No source/ZIP/history is edited to hide this. Local `package-install.json` records the failed assumption and affected paths.

No new business task is generated from the installed ZIP: reuse R78's separately scoped actual behavior evidence, with the line-ending qualification. This cycle cannot establish fewer professional prompts, lower rework, owner adoption, Claude business compatibility or connected Agensi delivery. Formal installed core hash and old pilot ZIP remain protected.

## Pricing and deployability decision

The current product is an Agent-loaded Markdown Skill; no new seller-operated database, backend, domain or licence service is required. Agensi upload/connection/review requirements remain platform gates, not evidence that the seller should build a new hosted app.

Actual browser pages on2026-10-21 show $5 and $15 on the two linked comparable listings, both without reviews; no purchase, sales or quality measurement. Recommend free GitHub core and a conditional $15 one-time convenience price test without bundled human support, not an immediate proven-profit launch. Keep the original $19 maintenance-pack scenario distinct and unchanged. A parallel $15 model retains all non-price assumptions and zero-sale scenarios; its economic results remain negative under those assumptions. It is not an income forecast or actual loss. No price, conversion or time assumption is disguised as measured user data.

Public platform terms still require clarifying the interaction with MIT and verifying reference/script delivery and business-output retention. Do not claim that a free listing solves the licence question. Keep personal correspondence and the prepared follow-up local; no message has been sent in this cycle. Marketplace upload, actual scan, connected use, seller eligibility, payout and live listing remain unverified/unexecuted.

## Remote acquisition and next action

The archive was pushed at hosting commit `cdb385d87c189cfe162ba23df9ebc2a9e66f97af`, separate from the package's source commit. An approved GitHub connector actually acquired the fixed file; decoded bytes, Git blob `494c18616b9304c0f6f3bed6bd5d4c9bb7a6bc74`, SHA-256 and25 verified members match the built archive. A browser then clicked Download raw file on the same fixed file page with bounded8-second event/path waits. The download event and saved file were obtained in about2.45seconds; that actual36,403-byte file has the same SHA-256. No repeat click or indefinite wait was required. Local `remote-receipt.json`, `browser-download.json` and `github-candidate.png` retain the receipt and observed page.

The hosting commit's remote Repository integrity workflow run39586540559 completed successfully. Static CI, remote byte acquisition, actual browser download, installation/discovery and external-user receipt remain different categories. No external recipient receipt or adoption is recorded. Earlier failed downloads remain historical failures, not evidence that GitHub cannot distribute this file. Fixed links are in the submission guide and bilingual README; no Release or marketplace upload was created.

The next external action is review of the prepared licence/delivery questions, then explicit authorization for sending and any unpublished connector review. Do not contact the platform, change an existing connection or onboard payouts without that scoped authorization. Meanwhile the locally verified GitHub candidate is available for bounded Codex trials; external adoption and paid demand are still unknown.
