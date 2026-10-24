# R44: quantity-sensitive purchasing — completed comparison

A novice asks for a reusable local tool to compare suppliers for the quantity they need. Ordinary supplier documents specify pack sizes, minimum packs, shipping, free-shipping thresholds and unquoted fields. The user does not request these professional calculation steps explicitly. All data are synthetic; no supplier contact, order, payment or publication is authorized.

Compare raw request A, current Skill V2 (`8b304b4`, behavior unchanged from R42), and short generic rule G, in that order. Tools, model settings and source files are identical. Generators do not receive the evaluator criteria or expected numbers. The [frozen record](results/v2-purchase-comparison.json) contains source inputs, exact request, Skill snapshot, runner and independently calculated fixture values.

## Acceptance

- Deliver a working reusable local tool, preserving original source data.
- For 30 notebooks, A must buy 120 for a total of 260; B buys 30 for 81; C buys 100 for goods cost 180 plus unquoted shipping. Do not replace unknown shipping with zero.
- At the withheld quantity 110, A totals 260; B totals 253; C has goods cost 198 and an unresolved final total. A cheapest-known offer is not a definitive cheapest supplier.
- Supplying C shipping of 20 and then 80 must change the 110-unit comparison appropriately: C totals 218 and then 278, while B remains 253. Verify actual quantity/quote updates, not just a precomputed example.
- Reject invalid values rather than producing a valid recommendation from zero/default substitutions. Expose excess purchased units and missing cost information understandably. Assess supporting reuse capabilities through the user's work, not a feature-count score.
- Separate generated self-tests, independent program checks and actual browser checks. Preserve failed commands, unsupported checks and costs.

The independent fixture calculation passes. Single generations will not establish stable broad superiority. Reproduction requires the existing local evaluation harness and equal prepared environments, not new hosted services or paid API dependencies.

## Evaluator correction retained

The original shipping-only follow-ups leave C's free-shipping threshold unknown. The source says blanks mean unprovided information, so an unspecified waiver could affect the final cost; the frozen expected 218/278 values require an extra condition. After observing V2's interval treatment, the evaluator clarified **C's free-shipping threshold as 1000 for both shipping updates**, equally for all arms. Original inputs, protocol and fixture-oracle source are retained unchanged; the record adds this correction explicitly. This is an evaluator correction, not a generator repair or new holdout. Earlier A browser checks used shipping-only updates and cannot resolve the waiver ambiguity; A's independent core was rerun with the clarified condition.

## Actual results

| Arm | Output tokens | Seconds | Checked result |
| --- | ---: | ---: | --- |
| Raw A | 6,095 | 211.21 | Correct initial costs, unknown-shipping case and clarified shipping updates; local draft survives actual reload. |
| Current V2 | 8,550 | 264.57 | Correct final costs and clarified updates; editable fields, original save/reopen handlers work. Opening message wrongly says B total69; final says81 without explicitly acknowledging omission. |
| Generic G | 5,762 | 197.54 | Correct costs and clarified updates; additionally checks whether buying extra packs to reach free shipping lowers total cost. |

All three independently preserve original source inputs and reject tested invalid quantities. A also rejects zero pack size and negative shipping; G rejects zero pack size. V2's original input/save/reopen/export handlers run with mock DOM/files/download; saved data round-trips and malformed project JSON preserves current state. Browser checks separately confirm V2's initial sample, quantity110, both clarified shipping changes and negative-input export blocking. G's actual browser confirms initial/changed quantities and both clarified shipping changes. A's actual browser confirms negative-input rejection and draft persistence. These scopes differ; they are not interchangeable pass counts.

A already identifies packaging, order minimums and unknown costs and supplies drafts/backups. V2 has more direct editing fields but requires manual JSON saving; it has no automatic persistence. G is explicitly limited to one item and saves two CSVs. Native file selection/download, V2/G restore in a real browser, direct file:// compatibility and cross-browser usability remain independently unverified. V2's generated Chrome check failed; its honest report is preserved separately from successful evaluator browser work.

## Useful omission found, not a V2 win

G's generated explanation proposed checking extra packs for free shipping. A post-hoc diagnostic sets quantity40 and B shipping30, retaining its pack price23 and free-shipping threshold100. Four packs cost92+30=122; five packs cost115+0=115 and supply10 extra notebooks. Independently executing original products yields A122, V2 122 and G115; actual G browser shows five packs, the surplus and the lower cost. No product was patched.

This exploratory scenario was selected after seeing G's feature; it is **not** a frozen-score improvement or proof G is broadly better. It exposes a concrete V2 limitation relevant to the user's objective: ranking a single minimally sufficient purchase does not necessarily find the most useful feasible option. Showing a cheaper alternative is appropriate here because the user asked for comparison, with no order/payment authority; choosing it or changing a fixed user requirement would need separate justification.

Keep the Skill unchanged for this round. Next tuning should test decision-relevant alternatives against stated constraints, with both a genuine benefit case and a case where extra quantity is expressly unwanted. Do not hard-code “always buy more” or add a generic feature checklist. Preserve the opening69 error and higher V2 cost; all three final outputs correctly state81 for the original order. No new human preference or general superiority is claimed.
