# R17: internal instructions versus useful sources

Six fixed real-model attempts completed with gpt-6.1-sol, low reasoning, browsing/network disabled. Before is `90e14d338b48d665063777158fbf0d57b87bf253`; the isolated after snapshot adds one paragraph only to `references/source-policy.md`. It distinguishes internal methods from evidence about actual resources, makes the evidence table optional, and preserves explicit audit requests and host-required disclosures. [Exact instructions, prompts, responses, commands and counters](results/v2-source-presentation.json).

The missing-font condition repeats R13 twice per variant. The supplied-source condition uses the two unchanged font distributions from R11, excluding the editor HTML. Their provenance pins Google Fonts commit `bd8f81ddb5c74d5c8897b36ad88b440266245103`. This is a text/source-inspection test, not a new font-rendering test or live rights check.

| Condition | Before seconds / output tokens | After seconds / output tokens |
|---|---:|---:|
| Missing fonts, repeat 1 | 33.20 / 591 | 31.07 / 552 |
| Missing fonts, repeat 2 | 33.00 / 585 | 32.40 / 559 |
| Supplied sources | 46.47 / 1120 | 45.85 / 1067 |

All four missing-font responses retained resource/rights gaps, real loading rather than a names-only selector, failure fallback and truthful non-implementation. Both before responses added internal-module compliance prose; neither after response did. However, after repeat 2 called **at least two real fonts** a minimum prerequisite, although the request did not establish that quantity. This unnecessary constraint is retained as a limitation; this small experiment does not establish that the added paragraph caused it.

Both supplied-source responses actually read each license, metadata and provenance record. Both cited the real files, scoped the conclusion to the supplied distributions and local poster use, separated source-retention advice from license obligations, and acknowledged that upstream bytes/links were not independently verified during the run. Neither used an internal module as proof. Review checked the exact supplied permission/conditions, including notice retention and the document exception. No external legal guarantee follows from this test.

All six actual command lists contain reads only; generated-path lists are empty and supplied assets remain byte-identical. The two snapshots differ in only the declared policy file. Some initial PowerShell reads omitted explicit UTF-8, so bilingual index text was garbled in tool output; English rules remained readable. No inference about Chinese-only module reliability follows.

**Decision:** retain the evidence, but do not adopt this extra paragraph in the active Skill in this iteration. It removed decorative attribution in two exposed repeats while preserving useful citations in one supplied-source pair, but the original already handled actual source evidence well. The narrow presentation benefit and small output difference do not establish better overall task judgment or stable savings. Active instructions remain R15. This does not reject the distinction between methods and evidence; it avoids treating a small wording experiment as a demonstrated general improvement.

Limits: nonblind development review, two repeats of one exposed task and one supplied-source pair, no raw/generic/release arm, no human preference test, no new rendering or live deployment, no cross-model result. The text-only boundary itself prohibits implementation. Full outputs and unsuccessful details remain available; there were no failed or replaced attempts.
