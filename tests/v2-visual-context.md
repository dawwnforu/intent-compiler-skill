# R75: owner feedback, visual references and a bounded repair

## Decision

Keep the core unchanged. Add a scoped visual-method paragraph that resolves referenced colors/images, preserves approved interaction placement and relates the primary use to the visual hierarchy. Update the existing pilot instructions to distinguish visual inspection and owner preference from functional checks. This is a correction prompted by an exposed failure, not a new unseen task or a demonstrated general Skill advantage.

Base: `fce533cd5eed4eb683b330aede5fd7f714893c34`. The owner preferred the original product to both R74 replays. The original conversation had been compacted without its screenshots while keeping visual references; source/logic acceptance did not cover that loss. R74 remains frozen. Its successful logic checks do not establish aesthetic success.

The formal installed core matches historical `6bcc84a` after line-ending normalization; it was not replaced by the isolated V2 evaluations. The installed and R74 visual guides are text-identical after normalization. There is no evidence that V2 removed the old visual rules or that an installation mistake caused this preference. Historical centered-add-button feedback is distinguished from the owner's now explicit bottom-navigation choice.

## One model repair, then a direct requested refinement

Exactly one `gpt-6.1-sol`/low repair used the existing artifact, two original screenshots and the frozen candidate guide; its event log confirms reading that guide. The existing approved local launcher retained child workspace-write, disabled network/web and the original safety boundaries. No model retry or new weak model was used.

The repair retains all four pages and existing hooks, uses one bottom navigation with the centered add action, restores the warm-white/teal/font references, and starts with writing. The core business helper is byte-identical; initial app logic changes only the default page. Source/resource/syntax and the existing independent simulated-DOM checks pass. The old test's archive-default assertion failed; a model in-memory adjustment is separate from the unchanged test file and independent regression.

The owner then actually reviewed the page: **slightly prefers the repair to the original**, but asks for further tuning. They like the current-date/calendar feeling and find record summaries too tall. This is project-owner feedback, not an external participant, adoption, repeat use or a blind whole-product comparison.

A direct follow-up compacts only list summaries, leaves full content reachable and renders 20 records per batch. Search and export still cover all records. This reduces initial DOM work; the demo still reads and serializes its entire localStorage data. Do not describe it as server pagination or a completed storage migration. The owner has not rated this follow-up yet.

## Actual checks and boundaries

- Real CUA in-app browser at 1280×720: bottom navigation, date, title-to-full-record opening and final summary rendering observed. The three unchanged example rows measure 122px each in the final follow-up; the preserved first repair measured 254/315/285px at the same viewport. This is a local geometry observation, not a broad usability score.
- At 390×844: date visible, bottom navigation in the viewport, no measured horizontal overflow; each example summary measures 136px. Actual search for a record and full-text opening work. Physical phone/touch and a usability study are unverified. The temporary viewport is reset afterward.
- The retained independent simulated-DOM checker passes existing create/edit/tag/calendar/draft/export paths. Additional 205-record checks cover initial20/load-more40/all205, search in a not-yet-rendered record, full details, zero matches/reset, unchanged data and complete export. This is not browser bulk-interaction evidence.
- Eight final runtime/font/licence resources are read through loopback HTTP and match delivered bytes. Earlier repair sources, model logs and R74 snapshots remain unchanged. Screenshots and private business artifacts remain local.

The owner separately authorized **local database configuration in the original native project**. Four local files add an unseeded shared daily-task migration, operating notes and existing-test integration. Effective signed-in users can read published editorial tasks; drafts are hidden and ordinary/anonymous writes denied. Personal answers/completion are not stored in that plaintext table; the existing encrypted vault remains. Two actual Node tests pass, including PGlite migration/RLS with synthetic Auth/Storage and existing offline backup checks. No database reset, real migration/deployment, new account, private-data upload or client integration occurs. The later tear-off animation is deferred as requested. These native changes are local and are not shipped as part of this Skill repository.

## Cost and interpretation

The one model repair took194.89s: input388092, cached input321152, output9156, reasoning output299 tokens. Direct density/database work adds zero model evaluation calls. These counters are not a cash bill. Restored screenshots, explicit new owner feedback, a guide change and an artifact repair occur together, so the result cannot isolate the guide's causal effect.

Raw local evidence: `outputs/intent-compiler-v2/visual-intent-r75/` contains the frozen protocol, actual invocation/events/response, initial repair, initial independent receipt/HTTP hashes and `density-followup/` containing the dated owner reply, native before/after manifest, logic output, browser screenshots and final delivery hashes. The initial receipt's pending-owner state is retained; the later reply is a separate event. Reproduction requires the owner's private references; this public report does not distribute them.

No formal installation replacement, frozen trial ZIP rebuild, MIT change, PR merge, marketplace publication or new host-compatibility claim. The preview-tab deliverable marker was rejected by automatic review as potentially publishing/handing off; it was not retried. Local inspection and link delivery continued without that marker.
