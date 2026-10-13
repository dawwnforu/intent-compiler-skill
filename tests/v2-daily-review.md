# R39: daily learning usefulness transfer — in progress

This new development case checks a novice's daily vocabulary-practice tool with raw request A, current V2 and brief generic guidance G, in that order. The user asks for practice, seeing progress and future vocabulary additions; the generator does not receive the evaluator's feature checklist. Identical synthetic inputs and execution boundaries apply. The frozen protocol, current snapshot and completed artifacts are in the [record](results/v2-daily-review.json).

The first attempt terminated during environment initialization before generation. A fresh isolated recovery run preserves that failure rather than counting it as model performance. No runtime rule is changed for this experiment.

A completed in 243.52 seconds. Independent execution of its original UI handlers with mock DOM/storage passes wrong-answer persistence, mistake-only retry, correct-answer recovery, reload, unseen vocabulary correction/addition, repeat-import idempotence, retention of learning statistics and rejection of an invalid import without changing data. The verifier initially lacked a lazily created form element; correcting the mock fixed that harness error without editing the product.

This raw-request baseline already implements useful follow-through. Those capabilities must not be counted as an exclusive V2 benefit. Browser layout, real file selection/download and learning effectiveness have not been independently verified. V2/G generation and remaining comparison checks were not complete when this record was written; no winner or overall cost conclusion is claimed.
