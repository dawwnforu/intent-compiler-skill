# R36: four-arm internal-document lookup

All four generations completed and were independently checked. This round does **not** demonstrate a candidate advantage in query accuracy, maintenance correctness or output cost. Keep the existing Skill unchanged. The [complete record](results/v2-internal-lookup.json) retains prompts, fixtures, snapshots, commands, final products, usage, failed commands and verifier sources.

## Protocol

A novice asks for a local tool to find operating instructions in a small collection and maintain changing documents without programming. Synthetic Chinese files include an explicitly obsolete reimbursement process, its current replacement, meeting-room booking/cancellation and visitor handling. No account, external AI, dependency installation or publication is permitted. The generation prompt does not give a feature checklist or the evaluator queries.

Order: generic instructions G, candidate V2 (`80953d9`), raw request A, installed release V1. The same model (`gpt-6.1-sol`, low), prepared Python environment and isolated Skill configuration apply. All original input texts remain unchanged. One trial per condition; this is a development comparison, not a repeated or blinded study.

| Arm | Output tokens | Generation seconds | Delivered maintenance path |
|---|---:|---:|---|
| Raw A | 6,118 | 204.89 | Direct editing, import, browser storage, full-tool export and JSON backup/restore |
| Generic G | 5,117 | 156.77 | Same-name Markdown import replaces that document; full-tool export |
| Release V1 | 6,037 | 256.86 | Import the complete Markdown collection; full-tool export |
| Candidate V2 | 16,572 | 595.67 | Direct editing, draft imports, full-tool export and explicit save confirmation |

Feature presence is source-inspected; only the checks below establish runtime behavior. V2 spent more output and time, including encoding repairs and browser self-testing. One sample cannot isolate causal Skill overhead. Do not claim savings for this pair or remove useful functions to manufacture them.

## Independent observations

All four final search implementations return the correct current reimbursement source for both “报销” and “买了办公用品怎么拿回垫的钱”, the meeting-room source for “预约会议室” and “不开会了要怎么办”, and no result for “年假能休几天”. These are five fixed queries; the tools use local keyword/phrase matching, not general semantic understanding.

Original generated import/edit/render handlers also pass the relevant maintenance operation in an in-memory DOM: replace Zhou Ning/Wednesday with Li Yue/Thursday, display the changed result, and reject an empty replacement without losing the valid update. G uses one same-name import; V1 requires the complete collection, which the check supplies and confirms retains the meeting instructions. A and V2 edit the current entry directly. These different workflows are not interchangeable; direct editing is not exclusive to V2. A's storage write is checked, but its backup restoration is only source-inspected.

Actual browser checks independently confirm G's novice reimbursement query and explicit unknown-query state. V2 was edited through its real form, downloaded through the actual control, then the unchanged downloaded bytes were reopened in a fresh browser tab over loopback HTTP. The new contact/day survives and is searchable. The downloaded HTML is embedded in the record; local screenshots show G's no-match state and V2's reopened result. This does not test OS file associations. Original-source links need the `inputs` folder beside the download, as explained by the product; the standalone reopened preview tests embedded content only.

G upload/download/reopen, A/V1 browser interaction, and V2 file-import clicks were not independently tested. V2's model-authored Chrome checks remain self-tests. Unequal browser verification depth must not become a product-quality ranking. There is no human preference result for these four products.

## Failures retained

The first sandbox attempt stopped at app-server initialization before a model invocation. A separate recovery directory retained the same inputs. G initially classified the current reimbursement document as historical because it mentioned the old version; its generator repaired this before completion. V2 had Windows Chinese pipe-encoding failures and repaired them during its run. Failed commands remain in the record. The evaluator initially expected different blank-field wording in V2 and corrected that assertion without changing the product. The first sandbox browser-preview connection failed; a separate loopback preview succeeded and was stopped afterwards.

## Decision and reproduction

No new Skill rule is adopted. This transfer shows usable functionality across all arms and concrete maintenance tradeoffs, not a striking quality gain. A useful next optimization must address an observed failure or avoid execution rework while retaining useful functionality; a new domain name or shorter final answer alone is insufficient evidence.

Reproduce with the record's frozen runner, snapshots, inputs and model settings using the existing evaluator. Save each embedded verifier and run `node <verifier> <arm-workspace> <evaluator-queries.json>`; G's additional update verifier takes only its workspace. Restore decoded Windows PowerShell files with appropriate UTF-8 BOM if reconstructing them. Run only against synthetic copies, preserving original products. The record embeds product sources and the actual downloaded V2 HTML so the checks do not depend solely on a prose summary.
