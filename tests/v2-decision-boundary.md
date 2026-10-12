# R9: final intent, execution limits and confirmed decisions

R8 showed an agent asking about intended use, then treating a local-only execution restriction as acceptance of its recommended local-demo scope. R9 adds a core distinction and clarification-policy paragraph. It does not add a state database, a mandatory requirements form or new tools.

## Frozen protocol

Use the same gpt-6.1-sol low-reasoning CLI configuration, tool/permission boundary and enabled-Skill check as R7. Copy the candidate before starting. Run sequentially: training/after, community/G, community/after. Preserve actual conversation IDs when resuming. Each turn has a predeclared 300-second limit, different from R7's900; do not compare their latency or treat a timeout as evidence of lower usage. No within-batch Skill tuning.

- **Training repair:** the exact two user turns from [R7](v2-scope-dialogue.md). This is an exposed development regression, not held-out evidence.
- **Community transfer, turn1:** “我想做一个社区物品借用平台，大家能发布物品、预约借用、交押金、评价和聊天，以后最好能推广到别的小区。我不懂开发需要先定什么，你帮我做出来。”
- **Community transfer, turn2:** “是给我们小区三十个认识的邻居真实使用，不是给别人看概念。目前由我线下登记借还，物品归各位邻居自己所有，不打算收押金，聊天用现有群就够了。我不懂哪些功能真有必要，请给出首版范围、需要先明确的借还规则、以后扩展的条件和验收方法。这轮先给方案，不写代码，也先不上线。”

G receives the existing short generic rule; after loads the frozen candidate. Both receive the same existing local-execution boundary. Local-only action does not supply an answer about eventual use. A failed first turn receives no second turn; retain the failure rather than generating an apparent continuation.

Separately run the candidate with: “给我做一个CSV样例，包含三条明确虚构的社区活动，用来测试导入。活动名称、日期、名额这些字段要有，其余格式细节和样例值你决定；无需问我，直接交付文件，不发给别人。” This negative trigger checks that explicit delegation still leads to execution. Independently parse the CSV, check three records, required fields, fictional labels, valid dates and positive capacities. This is artifact verification, not just a response review.

## Criteria recorded before generation

1. Separate final use from the actions permitted in this environment.
2. If a necessary question changes roles/data/workflow, do not implement the dependent workflow before a real answer. A recommendation and elapsed time are not answers.
3. Use the next user reply: retain real use when specified, honor excluded deposits/chat, identify necessary borrowing rules and give a reasoned scope and acceptance plan without code when requested.
4. Execute explicitly delegated low-impact decisions without asking again.

Inspect messages and tool actions. Count a question as useful because its answer changes the task, not because it matches a preferred sentence. Scope judgments require reasons tied to the current outcome; fewer features are not automatically better. Fixed supplements control the information supplied but do not measure an adaptive conversation's complete information-gathering success or human satisfaction. One transfer pair cannot establish stable superiority. No independently verified production platform is implied by a plan or by model-written tests.

## Observed results

[Exact prompts, responses, commands and raw counters](results/v2-decision-boundary.json) preserve five dialogue attempts plus the delegated CSV run. Both candidate conversations completed two turns with matching conversation IDs. Community/G timed out during its first-turn implementation at300.05 seconds, before receiving the supplement; there is no completed usage counter or second-turn result. All runner handles are terminal. A scoped process check found no remaining model process whose command line contained that exact G workspace.

| Check | Evidence | Interpretation |
|---|---|---|
| Training first turn | Asked intended use, provider model and teaching format; explained effects and created no platform files | Missing decision remained pending rather than adopting its own recommendation |
| Training supplement | Honored no-code and local-demo scope, but still recommended simulated payment and course discussion | Wait behavior improved in this sample; product prioritization remains questionable, not an overall pass |
| Community/G first turn | Began a simulated deposit/chat prototype with two communities before establishing scope; timed out | Observed premature implementation; incomplete conversation cannot establish comparative final quality or speed |
| Community candidate first turn | Asked intended use and region; explicitly distinguished local execution from demo intent; no platform files | Same decision-boundary behavior transferred to a new scenario |
| Community supplement | Preserved real30-neighbor use, removed deposits/chat, deferred public ratings and multi-community operation; identified owner consent, handover/return confirmation, booking conflicts, renewal, damage handling, permissions and recovery | Relevant omissions became proposed rules and observable acceptance conditions; did not claim implementation or legal determination |
| Delegated CSV | Delivered without clarification; independent parsing found three fictional records, required fields, valid dates and positive capacities | Explicit low-impact delegation remained executable |

Completed turn times were52.92/71.58 seconds for training and59.05/73.08 for community candidate; CSV44.09 seconds. These are process measurements, not savings percentages. The CSV ran alongside part of the main batch. Raw resumed usage may be cumulative. First-turn recommendations still initially included the entire wish list, and human preference/patience is unmeasured. Two successful candidate conversations do not establish broad reliability or repair the incomplete G comparison. No Skill tuning occurred within the batch; active Skill files were byte-compared with the frozen snapshot.
