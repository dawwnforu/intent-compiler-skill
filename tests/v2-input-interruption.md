# R60: input interruption follow-up

No new generations or product changes. This checks the unchanged R53 V1/V2 deliveries. [Results and exact checker source](results/v2-input-interruption.json); original delivered HTML remains in the [R53 record](results/v2-outcome-feedback.json).

Twelve independent Node VM checks passed: pointer and keyboard charging followed by blur or visibility change, plus pointer cancellation and lost capture, in each arm. Each asserts charge was positive, cancellation resets it to zero, the old release is ignored, and a fresh throw succeeds. The checker compares its input bytes with the original deliveries, invokes their registered handlers and advances explicit frames with stub DOM/canvas/storage. These are event-handler unit checks, not browser input tests.

In the actual in-app browser, V2 completed an ordinary five-second hold and release, displayed100% excessive-force feedback, and reset to ready while retaining feedback. The attempted overlapping observation did not establish a held middle state, so no actual focus interruption was performed. That acceptance item remains unverified, as do real touch, narrow layout and background timing. The local server and test tab were closed afterward.

To repeat the unit checks, reconstruct the unchanged R53 HTML at the paths named in the preserved checker, save `checkerSource` as a CommonJS file, and run it with Node from the workspace root. To close the separate UI gap, hold pointer or Space, switch away before releasing, return and verify zero charge, no accidental throw, and a successful new attempt. Record actual host and input method; do not count simulated handler invocation as this test.

Decision: both arms pass the bounded logic checks; no comparative benefit, Skill rule adoption, host installation or discovery conclusion follows.
