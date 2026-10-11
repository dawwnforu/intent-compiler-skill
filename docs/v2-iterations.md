# Candidate iteration log

## R1 — initial candidate 852ac71

Changes: shorter task-oriented core, explicit output restraint, six targeted domain modules, four-arm protocol and reconstructed public-project cases.

Development probes: synthetic application form, synthetic dorm survey and interactive quiz. Model gpt-6.1-sol / low, A/raw, G/generic, V1/0.2.0, V2/candidate. All results must be retained; quiz acceptance and repeated holdout trials remain pending.

Observed form run: all four arms preserved missing salary/contact/consent and did not claim an unearned undergraduate degree. V1 generated an additional explanations file; V2 used one draft. Reported output tokens: A1199, G937, V11289, V2890. This is one observation, not a stable percentage claim.

Observed analysis run: all four responses reported the correct deduplicated base and multi-select counts. Artifact review is required beyond these summaries. V2 generated both HTML and Markdown with substantially repeated report content; output tokens4426 versus V12996, A3399 and G3234. No statistical advantage is established.

## R2 — testable output adjustment

Failure: the “no unsolicited extra guide” rule still allowed duplicating a report across human-readable formats.

Change: default to one primary human-readable deliverable; extra formats require a user need or operational purpose. Preserve source/assets, requested exports and independent check scripts.

Prediction: on the same analysis case, fewer redundant report formats with the same denominator correctness, readability and traceable computation.

Observed R2: one Markdown report, 1900 output tokens and 55.88 seconds, versus R1 V2's two formats, 4426 tokens and 112.51 seconds. Read the full report: 10 unique records, 8 valid multi-select respondents, counts 5/4/4, 9 valid bothered responses, and five valid night counts averaging 2 remain correct. Synthetic/nonrepresentative scope and unknown causes remain explicit. This is a single development rerun with sampling variation, not a causal or stable improvement estimate. Traceable written methods are present; independent numerical recomputation and held-out repetitions remain required.

## R1 quiz: external browser verification

All four outputs completed the six-question flow, allowed returning to an earlier question, and downloaded a valid PNG in Edge at a 390×844 emulated viewport. A had horizontal document overflow; G/V1/V2 did not. No runtime exceptions occurred during the checked paths. Output tokens A7363, G8391, V110886, V29923; elapsed seconds A163.71, G182.38, V1277.87, V2257.69. V2 is not the cheapest arm and no marked visual advantage is established.

The independent verifier initially tried to read V1's block-scoped state and failed; that is an evaluator error, not a product defect. It was corrected to inspect the visible result. A stale browser debugger file caused one additional verifier startup failure; fresh browser profiles resolved it. Generated artifacts were not edited. Screenshots and downloaded images are retained outside the model workspaces. Real mobile system sharing, exhaustive answer-change scoring, accessibility, and repeated trials remain unverified.
