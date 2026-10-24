# R40: domain-method routing — completed development comparison

R39 motivates an experimental distinction between building quiz UI and supporting actual learning. This round adds one selectively routed [learning-practice candidate](fixtures/learning-practice-candidate.md) to a frozen copy of current V2; SKILL.md and existing modules are unchanged. The module is outside the shipped Skill. Its research scope is two primary-study abstracts, documented in [research notes](../docs/v2-research.md); no learning-effectiveness claim follows from software checks.

Two identical-prompt before/after pairs cover a novice's reusable museum-explanation practice tool and a brief-only entertainment personality quiz. Positive acceptance concerns attempted explanation, honest reference/self-assessment, source fidelity and ongoing use; the near-miss control should not acquire teaching, correct-answer scoring or diagnosis. The [record](results/v2-learning-route.json) preserves prompts, synthetic materials, snapshots, attempts and executable verifiers.

Before-training completed in 258.97 seconds with 7,929 output tokens. It already proposes recall followed by source comparison, self-rating, revision import and review dates, so these plans are not candidate-exclusive. But its **actual original HTML entry fails**: serialized PowerShell file metadata is passed where the parser expects a string. Independent execution of the original inline initialization and actual browser opening both report `text.replace is not a function`; clicking the visible start button has no effect. Its internal function self-tests did not cover this entry. No evaluator repair or original-delivery pass is claimed.

After-playful initially failed with HTTP 401 missing authentication before any answer. The runner terminated. Read-only CLI login status reported ChatGPT login; one unchanged-config retry in a new directory succeeded, retaining the original failed attempt. No credential change or alternative billing route was used. The retried brief provides six questions, four weather results and tie rules, explicitly for entertainment with no correct answers or psychological diagnosis; no implementation code was generated. Before-playful likewise provides a four-question entertainment brief with tie rules and no teaching or diagnostic expansion. Neither brief has a human fun/usability rating.

The resumed runner completed only remaining conditions; before-training was not regenerated. Command records show after-training read the learning-practice module, while the successful after-playful run did not. This is observed conditional routing on two tasks, not general domain-classification accuracy.

| Condition | Output tokens | Generation seconds |
|---|---:|---:|
| Training before | 7,929 | 258.97 |
| Training after | 6,915 | 269.38 |
| Entertainment before | 1,277 | 73.29 |
| Entertainment after retry | 1,702 | 78.56 |

The excluded failed auth attempt took 15.5 seconds and produced no scored answer. These are single samples with different implementation/self-check paths; lower training output does not establish stable savings, and both after conditions took longer.

## Independent candidate checks

The actual single-file candidate starts in both original-script execution and IAB. Before the learner requests comparison, only the question and blank draft are shown. Requesting feedback shows the supplied reference and source, explicitly without automatic oral scoring. Marking one topic as understood, then reloading, retains one understood and two pending topics; pending-only practice skips the previously rated topic.

Original UI handlers exercised with mock DOM/storage independently verify all three self-ratings, reload, pending-only practice, an unseen material revision and invalid-material rejection. A changed topic becomes pending, an unchanged topic retains its status, historical records remain stored and a malformed import leaves state intact. Input files match the supplied fixture and each other. Stored drafts are not automatically shown on a fresh attempt; do not claim a browsable draft history.

## Decision and limits

**Do not adopt the new module yet.** Its routing behaves appropriately and its generated training artifact is usable where this baseline is not. However, both versions already select honest recall/self-assessment; the baseline's startup serialization mistake does not isolate an educational-method benefit. Preserve the positive delivery evidence and mixed costs rather than adding a module solely to grow the knowledge library. The experiment remains available outside the shipped Skill.

The original baseline failure is unrepaired and retained. Checks used local HTTP browser origins, not native file double-click. Real import/restore file pickers, candidate backup download, narrow viewport and learning effectiveness were not independently verified. The generator's own verification remains a separate self-report. Preview servers were stopped. No installed Skill, license, dependency or marketplace change; the larger user goal remains open.
