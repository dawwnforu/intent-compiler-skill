# R43: reusable volunteer scheduling — in progress

This new office scenario returns to practical-use transfer after R42's narrow delivery repair. A novice asks for a local tool to arrange community volunteers each week, avoiding conflicts and unfilled roles and reusing it with next week's roster. It is not a request to contact volunteers or publish their information. All people and activities are synthetic.

Compare raw request (A), a short generic rule (G) and the current Skill at `77f52ec` (V2), in the order G, V2, A, using equal prepared tools and recorded model settings. The same ordinary-language request and CSV/Markdown source files go to all three. No generator receives the independent acceptance criteria, expected schedule or evaluator follow-up files. The [frozen record](results/v2-volunteer-schedule.json) preserves inputs, protocol, snapshot, runner and exhaustive fixture oracle.

## Acceptance

- A usable, repeatable local tool, not just a static schedule or technical plan.
- Initial full coverage: seven seats across six people. Respect confirmed roles, availability covering the whole shift, overlapping intervals and weekly hour limits. People with the same name retain distinct IDs.
- After v05 withdraws, at most six seats can be filled. Explain the vacancy without inventing a person, availability or qualification.
- After adding a 10:00–12:00 guide shift, at most seven of eight seats can be covered. Different start/end labels do not make overlapping shifts compatible.
- Examine actual correction, reuse, persistence and useful export/history support. Do not award points simply for more features or require one prescribed UI or algorithm. Distinguish necessary constraints from optional support.
- Check the delivered entry with original inputs, then actual handlers/browser where available. Keep model self-reports separate from independent evidence. Preserve original data and the no-notification/no-publication boundary.

The exhaustive oracle confirms the three fixture bounds (7/7, 6/7 and 7/8); its solution is kept outside generator workspaces. This checks the test input, not any generated product. Model generation is in progress. No improvement, token saving, user preference or Skill change is claimed.

To reproduce, use the frozen request, files and conditions in fresh isolated workspaces with equal tool access. The embedded runner uses the existing local evaluation harness; it is not a standalone hosted service. Run the embedded oracle against the fixed synthetic fixtures, then validate each actual product without replacing its initialization/data with a passing substitute. Never use real volunteer information for public evaluation artifacts.
