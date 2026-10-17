# Recovery state candidate — untested, not shipped

Replace only the exact R62 addition in `references/interactive-products.md` in an isolated candidate snapshot. Do not add this as another paragraph in the maintained Skill before behavioral verification.

> For multi-step entry, preserve unfinished input when retention fits the task. Keep draft, committed and explicitly discarded states distinct across reloads; completing or cancelling work must not silently make it new pending work. Recheck dependent results and save/export status after edits.

Observed trigger: R64 pair-two after restores a committed record as an unfinished draft; completing that restored form again creates another equivalent history record. The other five normal products preserve unfinished work without that observed saved-state problem. This is a candidate acceptance invariant, not evidence that R62 caused the failure.

The next frozen comparison must preserve partial-entry recovery and explicit temporary-input exclusions, check saved-state re-entry, and exercise cancellation/discard where tools permit. Allow a user to explicitly start another genuine event, including another repair with identical content; do not substitute global content deduplication. Keep the exposed repair separate from a fresh workflow and retain before/after failures, costs and shared success. No result or improvement is claimed for this text yet.
