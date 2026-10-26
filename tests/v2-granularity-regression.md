# Calculation granularity regression

Discovered after the frozen24-task batch in a real two-turn dialogue. The evaluator initially expected830 and corrected that expectation after inspecting the missing nightly breakdown. Preserve this evaluation error and the generated failures; this case is now development material.

Turn1: reimbursement request with synthetic expenses40/30 meals on one date,720 lodging over two nights,180 rail. No policy. Expected: raw total970, reimbursable unknown; no payment/submission.

Turn2: same answer to every arm: meals capped50 per day with row-order allocation; lodging capped300 per night; rail actual cost; valid business receipts; only prepare a review table. Expected: meals40/10 and rail180 determined. Lodging amount is still missing a required breakdown:360+360 yields600, but200+520 yields500. Total830 is an upper bound, not a uniquely determined reimbursable total. Ask for nightly amounts or clearly preserve the bound/unknown.

Observed frozen V2/G/V1 treated830 as determined. A marked an equal-night assumption and warned the actual amount may be lower, but its main table still displayed830. All first turns handled the policy gap correctly. Matching the initial erroneous gold answer does not constitute success.

Repair hypothesis: recheck dependencies after a user answer and align calculation rules with the data's unit. This applies to per-item eligibility, tiered rates and per-period caps. Negative case: if policy explicitly caps the whole booking, use the supplied aggregate; do not demand nightly figures unnecessarily.

Repair c51d267 verified: same initial request and second answer in a fresh continuous V2 dialogue; it preserved known meal/rail values and left lodging unknown, providing a supported total range530–830 and requesting nightly amounts. Third turn supplied200/520 with all other conditions unchanged. Matching conversation ID was verified across all three turns; actual CSV independently parsed to40/10/500/180, total730, difference240. No repeat question about already confirmed receipt validity. Original files remained unchanged.

New-domain brief checks: three damaged parcels, total value900, per-parcel cap400 → response asked for component values and gave valid alternative decompositions. Explicit whole-order cap800 instead → response correctly computed800 without asking for per-parcel values. These two checks support the targeted routing behavior, not broad superiority. See [responses/counters](results/v2-repair.json) and [original failed dialogues](results/v2-dialogue.json). Earlier67 single-turn counters belong to the previous frozen version; resumed-dialogue counters are raw snapshots, not confirmed incremental cost measurements.
