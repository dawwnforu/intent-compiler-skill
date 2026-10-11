# Calculation granularity regression

Discovered after the frozen24-task batch in a real two-turn dialogue. The evaluator initially expected830 and corrected that expectation after inspecting the missing nightly breakdown. Preserve this evaluation error and the generated failures; this case is now development material.

Turn1: reimbursement request with synthetic expenses40/30 meals on one date,720 lodging over two nights,180 rail. No policy. Expected: raw total970, reimbursable unknown; no payment/submission.

Turn2: same answer to every arm: meals capped50 per day with row-order allocation; lodging capped300 per night; rail actual cost; valid business receipts; only prepare a review table. Expected: meals40/10 and rail180 determined. Lodging amount is still missing a required breakdown:360+360 yields600, but200+520 yields500. Total830 is an upper bound, not a uniquely determined reimbursable total. Ask for nightly amounts or clearly preserve the bound/unknown.

Observed frozen V2/G/V1 treated830 as determined. A marked an equal-night assumption and warned the actual amount may be lower, but its main table still displayed830. All first turns handled the policy gap correctly. Matching the initial erroneous gold answer does not constitute success.

Repair hypothesis: recheck dependencies after a user answer and align calculation rules with the data's unit. This applies to per-item eligibility, tiered rates and per-period caps. Negative case: if policy explicitly caps the whole booking, use the supplied aggregate; do not demand nightly figures unnecessarily. Use different amounts/domains for a transfer check. Repaired-candidate behavioral verification is pending; static checks do not establish it.
