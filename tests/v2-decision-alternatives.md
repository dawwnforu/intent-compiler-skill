# R45: decision-relevant alternatives — completed development experiment

All four generations and independent program checks are complete. The added paragraph fixes the exposed benefit omission in this sample; both before/after exact-quantity controls pass. Both after runs visibly read the candidate paragraph. **Keep the paragraph outside the shipped Skill pending transfer checks.** One known case, one control, unequal browser coverage and the retained source conflict do not establish broad improvement.

| Condition | Output tokens | Seconds | Independent outcome |
| --- | ---: | ---: | --- |
| Benefit before | 12,063 | 316.85 | Offers four packs122; misses feasible five packs115. |
| Benefit after | 9,353 | 251.34 | Shows both122 and115 options, with surplus10; actual browser updates pass. |
| Exact40 before | 7,738 | 505.19 | B4 packs122; excludes oversupply and updates on input changes. |
| Exact40 after | 4,669 | 131.96 | Same boundary retained; actual browser changes/reload pass. |

Costs include tool-driven generation, errors and verification; the slower before-control does not prove the rule saves time. Both before-control and after-control generated browser-verification failures, separately retained from evaluator checks. No retries were selected to improve outcomes. The observations below preserve the chronological evidence, including earlier pending states.

R44 exposed a practical omission: current V2 ranked minimally sufficient purchases but missed a cheaper extra-pack option. Test a single [candidate paragraph](fixtures/decision-alternatives-candidate.md) about comparing feasible options against the user's actual outcome, explaining tradeoffs and preserving explicit limits. It contains no supplier, price, shipping or purchasing-specific answer. The shipped Skill and normal installation are unchanged.

Use current candidate `4833af3` as before and the same snapshot plus that paragraph as after. Internal harness names V1/V2 mean **before/after in this experiment**, not installed release0.2.0. Freeze both snapshots, inputs, prompts, runner, order and fixture enumeration in the [record](results/v2-decision-alternatives.json).

## Inputs and acceptance

Use the same ordinary purchasing request as R44 with quantity40, B shipping30, and C shipping20/free-shipping threshold1000 supplied in CSV. All costs are synthetic. The positive condition allows ordinary supplier comparison; the negative condition adds the actual user constraint: “本次只买40本，多出的没地方放，不要超量采购。”

- Benefit: B five packs yields50 notebooks at115, versus four packs at122. Surface the cheaper alternative and ten excess units, without placing an order or treating the alternative as an accepted purchase.
- Fixed: only40 notebooks are permitted. B four packs at122 is feasible; A/C minimums and B five packs must not be recommended as the compliant order.
- Both: a reusable local tool, correct totals, meaningful handling of changed inputs and invalid values, original inputs preserved, no external contact or payment. Separate actual artifact behavior from explanations and model self-reports.
- Record cost increases, failures, unsupported verification and whether the new paragraph was actually read. A lower number without respecting the quantity constraint is a failure, not an improvement.

The enumeration checks115/122 and the exact-quantity exclusions before generation. Order: benefit-before, fixed-after, benefit-after, fixed-before, with equal model/tools/settings. This is a known-failure development experiment and explicit-scope control, not a fresh holdout. One run per condition cannot establish stable superiority. Keep the candidate outside runtime pending actual results; no claim of improvement or adoption yet.

## Fixture limitation discovered during generation

The inherited merchant note still says C shipping has not been asked, conflicting with its updated CSV. The earlier description that all costs were known was too strong. Preserve the frozen fixtures/protocol; do not silently correct later arms. Benefit-before notices the conflict and marks C shipping unknown. Treat that handling as reasonable, not an error against the numeric oracle. B's115/122 comparison and the exact40 exclusion of A/C do not depend on C shipping: C goods alone cost180 and its minimum quantity100 already exceeds40. This bounds what the experiment can establish; it cannot test conflict-free import or confirmed C-total accuracy.

## First completed condition

Benefit-before finished in316.85 seconds. Independent execution of the original final HTML script and quantity handlers reproduces the omission: requesting40 gives four packs at122; explicitly changing the requested quantity to50 gives five packs at115. Thus the tool can calculate the cheaper order but does not surface it for the user's40-unit requirement. Quantity30 correctly gives99 under the changed shipping30; negative input is rejected and original source files remain unchanged. This is mock-DOM handler evidence, not an independent browser/export/restore check. The model's self-reported27 browser checks and rejected temporary-file cleanup are preserved separately. Other conditions are pending, so there is no candidate-effect conclusion.

Fixed-after finished in131.96 seconds. Independent original-module checks confirm exact40: B4 packs122, A/C excluded. Changes to quantity, pack price and shipping update correctly; unknown shipping remains unknown and invalid values are rejected. Actual browser checks confirm original122, no exact feasible option for41, changed pack price20 gives110, and that price/result survives reload. This supports the explicit-scope boundary for this one candidate sample; before-control and benefit-after are still pending. Native file import/export and direct file:// persistence are unverified independently. The model-reported browser failure and cleanup rejection remain preserved separately from the successful evaluator browser checks.

Benefit-after subsequently finished in251.34 seconds. Independent original-script/handler execution confirms both options are present: four packs122 and five packs115, with50 supplied and10 excess explicitly represented. Quantity30 changes the best result to99; pack price20 at quantity40 yields five packs100; setting shipping0 then chooses four packs80. Invalid quantity is rejected, original source bytes are preserved. This is a positive development result alongside the passing exact-quantity control, but independent browser/save/reopen coverage is still missing for benefit-after, and fixed-before remains pending. Keep the candidate unadopted until the comparison and relevant transfer checks are complete.

Subsequent actual browser checks confirm benefit-after displays both original alternatives, changes to99 for quantity30, and selects four packs92 when the original pack price23 is retained and shipping becomes0. Negative quantity is rejected. These browser updates differ from the earlier sequential price20 handler test, which correctly yielded80. The screenshot is a viewport capture after a failed full-page attempt. Native file operations, backup reopening and direct file:// use remain unverified independently; the final fixed-before condition is still pending.

Final condition: fixed-before completed in505.19 seconds. Original HTML/input-handler execution confirms B4 packs122 at exact40, exclusion of A/C, no exact offer at41,110 after B pack price20, unknown shipping remaining unconfirmed, negative quantity clearing results, and source files preserved. No independent actual-browser check was performed for this condition. Thus scope preservation is shared behavior, not an after-only benefit. All generated products remain unmodified by the evaluator.

The subsequent [R46 transfer](v2-print-alternatives.md) is complete: both variants already find valid print alternatives and preserve orientation, while both miss a zero-copy use case. No exclusive transfer benefit was established; the paragraph remains outside runtime Skill. R45 retains its narrow development result, not cross-domain superiority or actual user preference.
