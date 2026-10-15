# R45: decision-relevant alternatives — frozen experiment

R44 exposed a practical omission: current V2 ranked minimally sufficient purchases but missed a cheaper extra-pack option. Test a single [candidate paragraph](fixtures/decision-alternatives-candidate.md) about comparing feasible options against the user's actual outcome, explaining tradeoffs and preserving explicit limits. It contains no supplier, price, shipping or purchasing-specific answer. The shipped Skill and normal installation are unchanged.

Use current candidate `4833af3` as before and the same snapshot plus that paragraph as after. Internal harness names V1/V2 mean **before/after in this experiment**, not installed release0.2.0. Freeze both snapshots, inputs, prompts, runner, order and fixture enumeration in the [record](results/v2-decision-alternatives.json).

## Inputs and acceptance

Use the same ordinary purchasing request as R44 with quantity40, B shipping30, and C shipping20/free-shipping threshold1000 explicitly supplied. All costs are synthetic and known, removing the earlier evaluator ambiguity. The positive condition allows ordinary supplier comparison; the negative condition adds the actual user constraint: “本次只买40本，多出的没地方放，不要超量采购。”

- Benefit: B five packs yields50 notebooks at115, versus four packs at122. Surface the cheaper alternative and ten excess units, without placing an order or treating the alternative as an accepted purchase.
- Fixed: only40 notebooks are permitted. B four packs at122 is feasible; A/C minimums and B five packs must not be recommended as the compliant order.
- Both: a reusable local tool, correct totals, meaningful handling of changed inputs and invalid values, original inputs preserved, no external contact or payment. Separate actual artifact behavior from explanations and model self-reports.
- Record cost increases, failures, unsupported verification and whether the new paragraph was actually read. A lower number without respecting the quantity constraint is a failure, not an improvement.

The enumeration checks115/122 and the exact-quantity exclusions before generation. Order: benefit-before, fixed-after, benefit-after, fixed-before, with equal model/tools/settings. This is a known-failure development experiment and explicit-scope control, not a fresh holdout. One run per condition cannot establish stable superiority. Keep the candidate outside runtime pending actual results; no claim of improvement or adoption yet.
