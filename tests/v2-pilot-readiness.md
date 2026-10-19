# R72: fixed-package receipt and first-cohort handoff

## Decision

Proceed with the limited free Codex pilot. Runtime, published trial ZIP, MIT, manifests and formal installation remain unchanged. This cycle fixes the invitation/start/recording path; it does **not** establish user value, adoption, lower support cost or new model superiority. The requested real-task observation and feedback-driven reuse phases are waiting for actual participants. No simulated participant fills that gap.

Base and public PR head: `239553dfd2629a14fb0cdef6ec8fc044d3a7a080`. GitHub connector metadata confirms public repository, PR #2 open/draft/unmerged. Local branch began clean. CLI PR lookup returns401; existing R71 metadata-update403 remains unresolved. No credential/provider/security-policy change; a replacement description is retained for owner review rather than repeatedly trying metadata writes.

## Acquisition, inspection, correction and recheck — author-side

The [fixed ZIP file page](https://github.com/dawwnforu/intent-compiler-skill/blob/239553dfd2629a14fb0cdef6ec8fc044d3a7a080/pilot/intent-compiler-local-pilot.zip) is the cohort entry. Its [raw URL](https://raw.githubusercontent.com/dawwnforu/intent-compiler-skill/239553dfd2629a14fb0cdef6ec8fc044d3a7a080/pilot/intent-compiler-local-pilot.zip) is an alternative, not a successfully tested browser receipt. Download failure alone does not prove GitHub is unavailable.

| Check | Observed result |
|---|---|
| Bounded curl, restricted command | Raw-file and public-API requests each stop after about5s DNS timeout, zero bytes |
| Bounded curl, approved host command | Raw-file request stops after11.43s, zero bytes; maximum25s, no retry |
| GitHub connector | `fetch_file` at exact commit, `encoding=base64`; actual bytes decoded locally. Initial default UTF-8 attempt rejects binary, then supported encoding succeeds |
| Received package |54,242 bytes; SHA-256 `f151d04da35ee21e824ccb2b160b6682610c794b19c4bf4eef7af9eae70973df`; Git blob `b1bcf02d5c7978abc88e5e055185f3eb581680e3`; exact local/published package match |
| Python check |37 unique members; outer/sample-client ZIP CRC passes;24 Skill files, source, licences, sample inputs/output and instructions present; private participant log absent |
| Fresh project copy |Complete Skill copied to `.agents/skills/intent-compiler`, inputs copied, sample recipient extracted; no existing/formal install touched |
| Different implementation |PowerShell `Get-FileHash` and `Expand-Archive` independently agree on hash and37/24 file counts in a new path containing spaces and Chinese text |
| Browser / actual participant receipt |Not verified. R71's2747.97s browser-tool block remains a failed operation, not a GitHub outage or current support time. No repeated download-event wait |

Initial inspection fails a raw Git-blob equality assertion at `LICENSE`. Diagnosis across all24 files finds18 CRLF/LF-only differences: every archive file equals its original worktree bytes, and normalized text equals the commit's Git content. The checker is corrected to report byte identity and line-ending equivalence separately; it passes in a separate fresh destination. The failed checker, failed destination and diagnosis remain. This is a **checker correction**, not a product repair, MIT change or hidden alteration of the frozen package.

`SOURCE.json` names core source `c204e14`; the enclosing trial ZIP is fixed at239553d; manifest0.2.0 and unreleased2.0 are distinct labels. R70/R71 actual discovery/trigger/business evidence is retained, not rerun or inferred from copying. Windows Explorer double-click, native editor/printing, bare-name selection with duplicates and other host business paths remain unverified.

## Existing materials repaired, not another questionnaire

[One start page](../pilot/README.md) now explains value, existing account/tools, fixed acquisition, fresh-project steps, explicit project-file selection and feedback without requiring experiment history. The frozen ZIP is not rebuilt; its embedded old instructions/log remain identifiable, while the observer uses the current repository materials linked from the start page.

[The existing handoff](../pilot/feedback.md) supplies the reviewed invitation, consent wording, first observation, real-task choice, follow-up and concrete information needed from the owner. The participant describes a real authorized task in their own words. Help is allowed and recorded. The synthetic photography task is only onboarding; no forced raw/generic/Skill repetition.

The existing CSV now has35 distinct fields and **zero participant rows**. An identical empty working copy is prepared under ignored `pilot/local-feedback/`; this is readiness, not feedback. Event time/version, actual adoption, available new task, spontaneous/reminded reuse and developer interpretation are distinct. Installation help, business explanation and result correction sum once into human help; model waiting and research interviews are separate. Unknown remains blank. Observed action and interview report are labelled separately. No complete conversation or business files are collected by default.

No participant/consent is available in current records; the owner has been asked for aliases, usable Codex versions, available times and consent scope. Until they arrive, real participants, real-task completions, adoption and new day1/day7 reuse records are0; those follow-up observations have not occurred. There is no new purchase-intent or order evidence. No invitation, platform message or real-data upload was sent.

## Costs, compatibility and next decision

No additional behavior-model generations, new services or new host installs. Tool cash invoices are unavailable; tokens are not dollar bills. Developer work and bounded tool failures are internal preparation, not measured per-user support. No participant support duration exists, so revenue assumptions are unchanged. The1.92-minute example remains conditional. After actual value, ask separately about scenario materials, maintained updates and human service; willingness is not an order or payout.

Codex remains the first cohort path based on its existing bounded evidence. Claude still has only discovery, with third-party routing/authentication blocking business validation. There is no user-demand evidence to prioritize Cursor/Copilot; they remain unverified. Existing Agensi licensing/connector questions remain unsent and do not block local trial. No merge, Release, marketplace publication, collection or MIT change.

Next external action: the owner uses the existing invitation and start page to recruit up to three consenting users with working Codex, then reports only aliases/version/time/consent. Record first real task and actual adoption; wait for real day1/day7 dates. Fix repeated or costly observed blockers, regress the exposed case and inspect the next real task. Without feedback, do not generate more synthetic conversations or assume improved usability.

## Evidence and reproducibility

[Machine-readable receipt](results/v2-pilot-readiness.json) keeps successful checks, failures, unknowns and source identifiers separately. Full local records live under workspace `outputs/intent-compiler-v2/pilot-acquisition-r72/`: actual received ZIP/base64, before/after `verify_received` checker, `core-byte-diagnosis.json`, `received-check.json`, PowerShell extraction check and public PR metadata. No participant data or credentials.

To recheck receipt without a model: retrieve that exact repository file with base64 support or a bounded download, verify the SHA-256 above, inspect/extract all37 members, copy the complete24-file Skill into a fresh project, and inspect `SOURCE.json`/MIT and the nested recipient ZIP. Compare raw Git bytes separately from CRLF-normalized text; copying alone does not verify discovery or behavior. Browser download and external receipt require their own actual observations.

R71's simulated packer failure occurred in **turn1**, not turn5; that remains unchanged. No earlier frozen experiment, exposed repair, failure, no-difference result or sample product is replaced by this readiness record.
