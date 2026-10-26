# R29: supported intent versus suggested choices — not adopted

R28 exposed a specific error: the candidate paraphrased an unconfirmed completion time as the user's goal. Test one sentence replacement in isolated copies of `e407386`, retaining the repository Skill unchanged. Replace “state a tentative understanding” with “restate the supported outcome; present unconfirmed choices as recommendations, not as the user's intent.” [Exact sentence, full responses, core snapshots, runner, commands and counters](results/v2-intent-assumption.json).

Three fixed before/after pairs use gpt-6.1-sol/low, offline explanation-only boundaries and fresh isolated workspaces. Timing repeats the exposed meeting-assistant prompt. The new animation prompt tests whether “I do not know modeling” incorrectly becomes a 3D requirement. The control settles 8 seconds, portrait, 2D and existing photos: preserve those choices and provide a useful plan without asking again. Order: timing-before, visual-after, settled-before, timing-after, visual-before, settled-after. All six runs completed; no product files or external actions occurred.

## Findings from full responses

- **Timing:** both frame the flow as a recommendation, while both still suggest completion before the workday ends. After labels the time as recommended; before introduces the flow as a recommendation and says timing remains to be determined. The exact R28 false paraphrase did not recur in this fresh before run. No exclusive fix established.
- **Animation:** both conditionally recommend photo animation and explain filming/3D alternatives without requiring 3D. Before includes optional AI backgrounds and leaves duration open; after suggests 10–15 seconds explicitly as a suggestion. Both ask about product/materials. No demonstrated improvement.
- **Settled scope:** both preserve duration, orientation, 2D and photo-based approach, give timed storyboards, leave business facts as placeholders and do not re-ask settled decisions. Actual photo inspection or production was not requested or performed.

| Case | Before seconds / output counter | After seconds / output counter |
|---|---:|---:|
| Timing | 63.34 / 722 | 50.70 / 826 |
| Animation | 31.72 / 678 | 40.11 / 661 |
| Settled scope | 54.11 / 893 | 66.79 / 889 |

No stable efficiency conclusion: one pair per task, mixed costs and differing module reads. Timing-after additionally loaded source policy and knowledge organization. Initial bilingual index reads lacked explicit UTF-8 in all runs; some text was garbled, while English guidance and later domain reads were visible. No human preference or implementation test.

**Do not adopt the substitution.** It adds instruction without a demonstrated exclusive gain. Retain the original error and mixed findings; do not claim the original wording reliably prevents false assumptions either. Repository and installed Skill remain unchanged.

## Verification limits

Checked enabled Skill paths, exact sentence in each workspace, successful exits and absence of product files. Read all six responses and actual module commands. The first exporter incorrectly required a shell command printing the core; no run issued one. Corrected that assertion to the enabled, explicitly invoked Skill snapshot. Do not claim independent visibility into host prompt injection or that the core appeared in shell output. This is candidate-versus-candidate development testing, not a four-arm benchmark or a blinded preference study.
