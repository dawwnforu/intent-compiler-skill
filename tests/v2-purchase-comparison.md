# R44: quantity-sensitive purchasing — frozen protocol

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

## Progress: raw request completed

A finished in 211.21 seconds. Its original calculation module passes independent checks for the initial quantity, changed quantity, both shipping updates, six invalid values and unchanged source inputs. Actual browser operations also pass: 30 → 110 quantity change, unknown-cost warning, C shipping 20 → 80 changes the winner correctly, saved draft survives reload, and negative quantity clears valid results with an error. Native file selection/download and backup restoration remain unverified; localhost storage behavior does not establish direct file:// compatibility.

A already identifies packaging, order minimums and unknown costs, and supplies local drafts and backups. Those capabilities therefore cannot be presumed exclusive Skill gains. V2/G are still pending; no comparative improvement, new user preference or Skill change is claimed.

An observed V2 intermediate message states “乙店需买 3 包，合计 69 元”, omitting the quoted 12 shipping. This is an inaccurate explanation of order cost even if its supplier choice is right. Preserve it separately from final artifact correctness; final generation and any later correction are still pending. A's intermediate explanation correctly gave 81.
