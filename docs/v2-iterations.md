# Candidate iteration log

## R1 — initial candidate 852ac71

Changes: shorter task-oriented core, explicit output restraint, six targeted domain modules, four-arm protocol and reconstructed public-project cases.

Development probes: synthetic application form, synthetic dorm survey and interactive quiz. Model gpt-6.1-sol / low, A/raw, G/generic, V1/0.2.0, V2/candidate. All results must be retained; quiz acceptance and repeated holdout trials remain pending.

Observed form run: all four arms preserved missing salary/contact/consent and did not claim an unearned undergraduate degree. V1 generated an additional explanations file; V2 used one draft. Reported output tokens: A1199, G937, V11289, V2890. This is one observation, not a stable percentage claim.

Observed analysis run: all four responses reported the correct deduplicated base and multi-select counts. Artifact review is required beyond these summaries. V2 generated both HTML and Markdown with substantially repeated report content; output tokens4426 versus V12996, A3399 and G3234. No statistical advantage is established.

## R2 — testable output adjustment

Failure: the “no unsolicited extra guide” rule still allowed duplicating a report across human-readable formats.

Change: default to one primary human-readable deliverable; extra formats require a user need or operational purpose. Preserve source/assets, requested exports and independent check scripts.

Prediction: on the same analysis case, fewer redundant report formats with the same denominator correctness, readability and traceable computation. Must rerun rather than infer success from wording. R2 results pending.
