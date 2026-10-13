# R35: useful follow-through across two new domains

User feedback favored the raw habit app because “功能更实用、完整”. The user then explicitly requested broader optimization without cutting useful functionality to save tokens. This round tests a single replacement paragraph against current 2.0 (`8943b1b`), not against raw requests or release V1. Both snapshots, complete prompts, synthetic inputs, commands, outputs, product sources and independent checks are in the [record](results/v2-practical-utility.json).

## User feedback received, 2026-10-13

The user was shown a textual comparison of the quotation tools: both find the current lowest unit price; after adds historical quotes and complete backup/restore, with generation time increasing from about 219 to 434 seconds. The user answered: **“值得，实用功能比这点等待更重要”** (worth it; useful functionality matters more than this extra wait).

This supports keeping these concrete capabilities and evaluating usefulness before output/time cost. It is feedback on the described tradeoff, not a new hands-on UI test, a blanket preference for more features, approval of unlimited latency/spending, or evidence of general Skill superiority. The question also described manual-copy backup in the old quotation tool; that workaround was not independently verified as a delivered feature and must not be counted as one. The historical-view and after backup/restore checks remain the recorded behavioral evidence.

## Change and cases

The replacement asks the agent to consider use beyond the first successful action and include small supporting capabilities when their absence forces recurring manual work or loses useful work. It retains authorization, exclusions and settled scope. It does not prescribe charts, accounts, backup buttons or a feature count for every task. The tested paragraph is adopted exactly; no habit-specific rule or dependency is added.

Two new tasks ask for usable local products: a single organizer's equipment lending/return tool, and a weekly supplier CSV comparison tool. A third asks only for one button-label replacement. Input documents establish stock quantities and quote semantics; user prompts do not contain the evaluation checklist. Run order is quotes-before, loans-after, quotes-after, loans-before, copy-before, copy-after. All six gpt-6.1-sol/low attempts completed, using the common isolated-Skill and prepared-Python environment. Inputs are unchanged.

| Case | Before output tokens / seconds | After output tokens / seconds |
|---|---:|---:|
| Equipment loans | 5,464 / 182.15 | 6,744 / 368.57 |
| Weekly quotations | 6,656 / 219.27 | 11,863 / 434.23 |
| Exact copy edit | 478 / 34.04 | 412 / 26.53 |

Generation cost increased in both substantive tasks. Browser/self-test choices and implementation differences contribute; one sample cannot establish causation, stable savings or general superiority. Observer browser delays are not included in these generation times.

## Actual results and tradeoffs

**Loans:** both generated Windows desktop tools and independently passed stock reservation, overbooking rejection, return and save/reload checks. Before supports a stock overview and open/all record filtering. After adds name/equipment/note search, notes, explicit mistaken-entry cancellation and a backup action. Independent execution confirms cancellation releases stock, preserves the cancelled record and permits a corrected entry that survives reload. Before has no equivalent cancellation operation or search control in its source; its manual backup instructions are not treated as no backup support at all. After's available stock is in the item selector instead of the separate stock grid. These are tradeoffs, not an all-features superset.

**Quotations:** both correctly choose South at CNY 0.05 per unit for A4-80gsm paper and CNY 1.4 for the specified pen, keep A4-70gsm separate, preserve sources, replace older quotes and exclude conflicting current offers. Both pass an independently supplied next-week update, which changes the paper winner to West at 0.065. These correct calculations are not a new-rule-exclusive benefit.

After adds an in-app historical-quote view and complete backup/restore instead of requiring the user to reopen source CSVs. Independent core execution round-trips all nine records with equal comparison results and confirms duplicate restoration adds zero rows. Source review shows per-file error handling continues with other files; this UI path is not independently exercised. Before aborts an invalid batch without changing existing records and has folder selection; after uses multiple-file selection. Before exports the filtered view, after explicitly exports all items. Do not label these differences universal wins.

**Scope control:** both produce exactly the requested label substitution with no other product files or content changes. It is one narrow control, not proof against all scope expansion.

## Verification scope

Independent JavaScript checks execute original pricing/restore modules. Independent PowerShell checks use the AST to load only the original reviewed business functions into isolated test data; they do not open native windows. Check source and results are embedded in the JSON. Model-authored GUI tests remain separate self-reports; native interface usability is not independently verified.

For before quotations, an actual browser imported both CSVs, showed the correct three groups, filtered a specification, downloaded a parsed three-offer CSV and restored nine records after reload. A screenshot is retained locally. After quotation file selection, download and native lending clicks were not independently browser/UI-tested. Two browser file operations unexpectedly took approximately 419 and 518 seconds despite bounded operation requests; no cause or performance claim is inferred.

Before-quote generation reported failed browser verification and rejected temporary-cache cleanup; after-quote generation also reported cleanup rejection. These are retained, not hidden as successful cleanup. The initial independent lending check could not start inside the sandbox; the same reviewed script passed outside it without modifying execution policy. Initial export encountered a UTF-16 artifact, then used its BOM to decode it correctly. No product was repaired to improve the comparison.

## Decision and reproduction

### Follow-up: quote UI data flow (2026-10-13)

The unchanged after-quote UI event handlers now have an independent [integration check](check_quote_ui_flow.cjs) and [execution record](results/v2-quote-ui-flow.json). It executes the original UI and core with an in-memory DOM, storage and download dispatch. Ten assertions cover valid/invalid/valid batch import, historical rendering, backup Blob contents, cancelled and confirmed clear, complete restoration, duplicate restoration, corrupted-backup preservation, fresh-context reload, search and the explicitly unfiltered export. A deliberately mutated temporary copy stops at the invalid file; the same check rejects it. Original products and inputs were not changed, and no new model generation occurred.

Run `node tests/check_quote_ui_flow.cjs <after-quotes-workspace>` against the original artifact, or reconstruct `quote-ui.js`, `quote-core.js` and `inputs` from the R35 record. This closes the handler/data-flow gap, not the browser file-picker, actual download, layout or native desktop usability gaps. It does not add a comparative win or token claim.

Adopt this limited usefulness criterion because it produced concrete support for continued use in both new domains while preserving the tested simple-edit boundary. Treat this as a development signal requiring further transfer/user evaluation, not a measured increase in satisfaction or a token reduction. Preserve the cost increase and capability tradeoffs.

To reproduce, use the exact protocol, snapshots and synthetic files in the JSON, fresh workspaces and recorded model settings. Its embedded runner makes real model calls through the existing local evaluator. The four independent verifier sources can be saved and run against the corresponding unchanged artifacts. PowerShell records must be written to a fresh isolated directory; do not run these checks against user loan data. JSON artifact strings retain decoded text; save PowerShell with UTF-8 BOM for Windows PowerShell when reconstructing files. The existing local artifacts retain their original encoding. No installed Skill, license or marketplace package is changed.
