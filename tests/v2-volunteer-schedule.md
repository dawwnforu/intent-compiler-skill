# R43: reusable volunteer scheduling — completed comparison

This new office scenario returns to practical-use transfer after R42's narrow delivery repair. A novice asks for a local tool to arrange community volunteers each week, avoiding conflicts and unfilled roles and reusing it with next week's roster. It is not a request to contact volunteers or publish their information. All people and activities are synthetic.

Compare raw request (A), a short generic rule (G) and the current Skill at `77f52ec` (V2), in the order G, V2, A, using equal prepared tools and recorded model settings. The same ordinary-language request and CSV/Markdown source files go to all three. No generator receives the independent acceptance criteria, expected schedule or evaluator follow-up files. The [frozen record](results/v2-volunteer-schedule.json) preserves inputs, protocol, snapshot, runner and exhaustive fixture oracle.

## Acceptance

- A usable, repeatable local tool, not just a static schedule or technical plan.
- Initial full coverage: seven seats across six people. Respect confirmed roles, availability covering the whole shift, overlapping intervals and weekly hour limits. People with the same name retain distinct IDs.
- After v05 withdraws, at most six seats can be filled. Explain the vacancy without inventing a person, availability or qualification.
- After adding a 10:00–12:00 guide shift, at most seven of eight seats can be covered. Different start/end labels do not make overlapping shifts compatible.
- Examine actual correction, reuse, persistence and useful export/history support. Do not award points simply for more features or require one prescribed UI or algorithm. Distinguish necessary constraints from optional support.
- Check the delivered entry with original inputs, then actual handlers/browser where available. Keep model self-reports separate from independent evidence. Preserve original data and the no-notification/no-publication boundary.

The exhaustive oracle confirms the three fixture bounds (7/7, 6/7 and 7/8); its solution is kept outside generator workspaces. Separate independent validation of original product handlers and actual exported CSV confirms all three products meet those bounds without violating identity, role, availability, overlap or hours constraints. Original source inputs remain unchanged.

## Observed results

| Condition | Output tokens | Generation seconds | Initial / withdrawal / overlap | Practical follow-through |
| --- | ---: | ---: | --- | --- |
| Raw A | 5,959 | 225.38 | 7/7, 6/7, 7/8 | Re-import next week's CSV; export schedule. No manual assignment editor or saved-project reopen. |
| Generic G | 5,524 | 200.85 | 7/7, 6/7, 7/8 through import handlers | Manual assignment with error display and export blocking. Built-in sample button fails: `text.replace is not a function`. No saved-project reopen. |
| Current V2 | 13,679 | 474.81 | 7/7, 6/7, 7/8 | Working preloaded example; invalid manual changes rejected and reverted; save full project and reopen a valid edited draft with fresh validation. |

These are three actual single generations with the same model/tools, not authored answer examples. All three solve the core scheduling problem. V2's useful difference is support for continuing and correcting real work, rather than superior constraint solving. It takes substantially longer and produces more output; there is no token-saving claim. The user's earlier preference for quotation history/backup over a few minutes of waiting supports the evaluation priority, but is **not** a user evaluation of this scheduling product.

## Independent verification and limits

- Run original HTML scripts in their delivered order and invoke actual import, regenerate and export handlers with mock DOM/file/download objects. Validate normalized schedules and actual CSV output with a separate Python constraint checker. Re-import is repeatable; invalid input is rejected. No product repair or passing replacement sample is substituted.
- V2: valid manual vacancy survives save/reopen in a fresh instance; invalid manual collision is reverted; malformed project JSON preserves the current draft. This is handler-level save/reopen verification, not native file-picker/download verification. There is **no automatic persistence**: users must save before closing.
- Actual browser: V2 starts from its original sample, generates 7/7, rejects and reverts a conflicting manual assignment, and produces 6/7 and 7/8 after visible textarea edits. G renders but its sample action fails visibly. A has handler-level coverage only. Browser coverage is asymmetric and is not counted as an A failure.
- A G file-chooser tool attempt requested 10-second operation timeouts and a 20-second outer timeout, but returned after 3,712.81 seconds without verified import. Preserve this evaluation-tool limitation separately from generation time; do not attribute it to product or Skill performance. Native downloads, printing and cross-browser compatibility remain unverified independently.
- Invalid raw input clears the displayed schedule in all three; none supplies automatic recovery of unsaved edits. V2 supports one week's inputs at a time and reports search limits. Large-scale scheduling performance is not tested.

Keep the current Skill unchanged. This fresh office scenario supplies limited evidence that its practical-use criterion transfers beyond learning and quotations, but a single sample cannot establish reliable general superiority. Preserve model self-tests separately from independent results in the record.

To reproduce, use the frozen request, files and conditions in fresh isolated workspaces with equal tool access. The embedded runner uses the existing local evaluation harness; it is not a standalone hosted service. Run the embedded oracle against the fixed synthetic fixtures, then validate each actual product without replacing its initialization/data with a passing substitute. Never use real volunteer information for public evaluation artifacts.
