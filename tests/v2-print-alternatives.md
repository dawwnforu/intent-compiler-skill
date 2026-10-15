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

No generated result, user preference or adoption is claimed. The candidate remains outside the shipped Skill until evidence supports it. Read-only evaluator PDF checks follow the PDF skill; this does not enable additional Skills inside generator conditions.
