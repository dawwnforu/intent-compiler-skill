# R46: physical print-layout transfer — frozen experiment

Test the unchanged R45 alternatives paragraph on a new domain: a novice wants a reusable local label tool, printable PDF, and less wasted paper. Six synthetic name/group records each request one100×60mm label. Ordinary A4 paper,10mm margins and5mm gaps are supplied physical requirements, not optional suggestions. There are no historical finished products in generator workspaces.

Use the exact R45 before/after snapshots with identical tools/model/settings. This is transfer of the added paragraph, not another revision; the existing print-layout module is present in both arms. V1/V2 mean before/after here, not installed0.2.0. The [frozen record](results/v2-print-alternatives.json) preserves both snapshots, runner, materials, ordinary-language prompts, interleaved order and geometric checks.

## Acceptance before generation

- Flexible: deliver six correctly sized labels in one A4 PDF page, for example landscape with two columns and three rows, or portrait with rotated labels. Preserve complete readable names/groups,100×60mm physical size, margins and gaps. Do not achieve a page-count win by shrinking or omitting content.
- Fixed: the user expressly requires A4 portrait and upright labels. Use two pages for all six labels; do not rotate or shrink. At most one100mm-wide label can intersect a horizontal band in190mm usable width, and only four60mm-high labels with5mm gaps fit vertically, so one page cannot satisfy this constraint.
- Reusable tool: change the first copies value to2 and second to0, regenerate, and verify six labels with the intended duplicate/omission. Do not confuse requested copies with duplicate source rows. The update is evaluator-only, not supplied in the model prompt.
- Check actual PDF page dimensions, label geometry/overlap, content and rendered readability, alongside current-state UI/export agreement where available. Allow up to0.3mm numerical/stroke tolerance when assessing exported geometry, not systematic resizing.
- Invalid copy counts or oversized requests must not silently lose labels or scale their physical dimensions. Preserve original inputs and no-network/no-install/no-publication boundaries. Separate unsupported operations and physical-printer testing from digital verification.

Fixture capacities are4 per portrait upright grid,6 per landscape upright grid, and6 per portrait rotated grid. The one-page solution is feasible, not a claim to solve arbitrary rectangle packing. Order: flexible-after, fixed-before, flexible-before, fixed-after. One run per condition cannot establish stable cost savings or broad superiority. Reportlab and pypdf are available in the same prepared interpreter for all arms; no dependency is installed for this test.

The candidate remains outside the shipped Skill until evidence supports it. Read-only evaluator PDF checks follow the PDF skill; this does not enable additional Skills inside generator conditions.

## Interim observation: first completed condition

Flexible-after completed in398.43seconds with15856output tokens. Independent PDF operator/text checks found one A4 page, six100×60mm labels, correct copies, required margins/gaps and no overlaps. Poppler rendering was visually inspected: complete Chinese names/groups, readable and unclipped. The actual browser interface compares upright, rotated and mixed arrangements instead of silently choosing only the first feasible layout.

The held-out copies update **fails**: first person2/second person0 is rejected because this generated tool requires every row to have1–1000 copies. This was reproduced through both the original parser and the actual browser's Update Preview button. Negative and fractional copies are correctly rejected. Original input bytes remain unchanged. No evaluator repair was applied; a successful initial PDF is not a successful reusable-tool result.

The generator encountered unavailable desktop GUI support and delivered a local browser application. The evaluator verified that original app through its loopback server. Native file chooser/download, launcher double-click and physical printing remain untested. Other conditions are still pending; this observation establishes neither an improvement over the before condition nor a stable efficiency result. The linked record includes original artifact source and independent checker source for reproducibility.

## Interim observation: fixed-before

Fixed-before completed in500.5seconds. Independent inspection of both its supplied PDF and its generator-produced browser-print PDF confirms two upright A4 pages, exact requested copies,100×60mm labels and required spacing. Both pages of both files were rendered and visually inspected. The actual original browser UI shows four labels then two, and the held-out2/0 update rejects zero copies and clears the preview; the Python parser independently rejects it too. Inputs remain byte-identical.

This is a shared missing use case in the two completed conditions, not evidence that the added paragraph caused the failure. The fixed-after and flexible-before results are still needed for matched comparisons. The evaluator corrected a false rotation flag caused by a browser PDF's inverted drawing y-axis: absolute rectangle-axis lengths are checked, while name text direction is still checked separately. No generated product was repaired. Native browser printing was not repeated by the evaluator; only the already generated browser PDF was independently inspected. The generator's unsuccessful cache-cleanup approval is retained in its logs and is unrelated to the printable result.
