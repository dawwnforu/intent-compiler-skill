# R39: daily learning usefulness transfer

This new development case checks a novice's daily vocabulary-practice tool with raw request A, current V2 and brief generic guidance G, in that order. The user asks for practice, seeing progress and future vocabulary additions; the generator does not receive the evaluator's feature checklist. Identical synthetic inputs and execution boundaries apply. The frozen protocol, current snapshot and completed artifacts are in the [record](results/v2-daily-review.json).

The first attempt terminated during environment initialization before generation. A fresh isolated recovery run preserves that failure rather than counting it as model performance. No runtime rule is changed for this experiment.

A, V2 and G all completed. Independent execution of their original UI handlers with mock DOM/storage passes wrong-answer persistence, mistake-only retry, correct-answer recovery, reload, unseen vocabulary correction/addition, repeat-import idempotence, retention of learning statistics and rejection of an invalid import without changing data. V2/G also retain unfinished practice counts in history/daily records. The A verifier initially lacked a lazily created form element; correcting the mock fixed that harness error without editing the product. An export check initially compared Windows file newlines to an in-memory LF string; comparison against preserved original fixture bytes confirms all inputs are unchanged.

| Arm | Output tokens | Generation seconds |
|---|---:|---:|
| Raw A | 9,049 | 243.52 |
| Current V2 | 10,923 | 336.17 |
| Generic G | 8,283 | 337.41 |

These single development samples differ in implementation and self-verification. V2 is neither shortest nor fastest; do not infer stable cost savings or causation. An evaluator browser download call took 606 seconds despite bounded event/path requests; that observation-tool delay is excluded from generation time.

## Real browser findings

**A:** actual one-question practice, wrong-answer marking, completed-history persistence after reload and mistake-only correct retry work. But the unanswered quiz still displays the complete English/Chinese vocabulary table, including the tested answer. This fails the predeclared recall-without-unrequested-answer criterion. The earlier empty-feedback handler assertion covered only one feedback region, not all rendered content; it was insufficient to prove concealment. The frozen product remains unchanged.

**V2:** actual practice hides the vocabulary/management section and shows no answer before submission. A wrong answer followed by reload before finishing retains both the wrong word and the unfinished 0/1 record. Mistakes-only retry produces a completed 1/1 record. Pasting the withheld correction/addition yields nine words; repeating it stays at nine while preserving cumulative 1/2 answers. A real downloaded backup independently parses to nine unique words, corrected apple meaning, new remember entry and both recorded answers. This is concrete follow-through evidence beyond a feature list.

**G:** the original IAB page shows only the background with an empty body. Follow-up read-only DOM inspection finds the cause: the `app.js` script tag lacks its closing `</script>`, so the browser parses the remaining page as script text. The earlier cause-unknown observation is preserved in the record; it is now a demonstrated original-delivery defect. JavaScript syntax and mock-DOM tests did not exercise HTML parsing. Its own failed Edge GPU check is a separate model report.

A **separate evaluator repair** copies the three product files and inserts only the missing closing tag; original HTML and both scripts stay unchanged. In a fresh local browser origin, the repaired page renders and passes wrong-answer marking, reload persistence, same-word retry and completion: two daily answers, one correct, zero pending mistakes. The answer table is collapsed by default. This restores G's useful behavior but does not retroactively turn its original delivery into a pass, nor count an evaluator fix as Skill improvement. Actual CSV chooser/backup checks were not repeated in the repaired browser.

## Decision and limits

Retain the existing practical-usefulness rule; this round adds no core instructions. The V2/A answer-concealment difference is a useful new-domain result, while all arms already implement much of the requested ongoing workflow. No broad superiority or human preference is established. Future iteration should target an observed user-impacting gap, not require identical features or add more generic rules.

The record embeds all prompts, frozen Skill, original products, commands, model responses, independent verifiers, browser observations, downloaded backup and isolated HTML repair. Local screenshots are `daily-review-r39-recovery/A-answer-visible.png`, `V2-answer-hidden.png` and `G-repaired-browser.png`. Mock handlers do not prove HTML parsing, layout or file-chooser behavior. Actual browser checks used local HTTP origins, not native file double-click; independent backup restore, narrow viewport and learning effectiveness are not verified. Temporary preview servers were stopped. No installed Skill, license or marketplace change.
