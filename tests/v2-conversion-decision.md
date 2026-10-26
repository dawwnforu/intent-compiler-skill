# R23: a new page-selection decision / 新任务决策对照

2026-10-12. Frozen candidate `4a83fcf`; no instruction changes between runs or adopted afterward. One actual task each for raw request A, short generic rule G and full candidate V2, in order G/V2/A, `gpt-6.1-sol`, low reasoning. Other skills disabled equally; only synthetic local inputs, no network or real-site changes. [Exact prompts, inputs, reports, commands and counters](results/v2-conversion-decision.json).

The novice asks whether to replace an event registration page because the new version's aggregate registration rate looks much higher. They request a short decision note for colleagues, not statistical terminology or a preset method. Supplied documentation establishes consistent units but different weeks and traffic-source proportions, with no random assignment or rollout authorization. Six acceptance criteria were written before running any arm.

## Independent checks

From the four CSV rows, the old page has 38/110 registrations (34.55%) and the new page 72/110 (65.45%). Within community traffic, old/new are 80%/70%; within advertising, 30%/20%. Source composition explains the aggregate reversal. These observations still do not establish a causal effect of either page: timing and visitor differences remain.

All three complete reports calculate those values correctly, distinguish composition from causality, recommend a provisional choice rather than automatic replacement, and propose an authorized future simultaneous randomized comparison within source. Each creates one Markdown report and preserves the input bytes. Existing material suffices for the analysis, so none blocks it with a questionnaire. No website or live experiment was implemented.

G illustrates two common source mixes; V2 adds a formula using p; A specifies a 95% interval for a future comparison. These differences do not demonstrate superior novice understanding. The formula is a potential readability burden, not a measured human preference. Future experiment recommendations were reviewed as plans, not validated implementations.

| Arm | Reported output tokens | Wall seconds |
|---|---:|---:|
| A: raw request | 1,690 | 65.87 |
| G: short generic rule | 1,869 | 86.47 |
| V2: full candidate | 1,935 | 81.29 |

Counters cover the model turn, not just the final report. All returned exit code zero; independent checking uses exact rational arithmetic and full-artifact review. The first exporter incorrectly compared Windows-written CRLF inputs against LF bytes; correcting the verifier's fixture reconstruction passed without modifying sources or rerunning models. This correction is retained in the record.

## Reproduce and interpret

Create isolated directories with the two input files from the JSON and apply the stored raw/generic/Skill invocation. Keep the candidate version and environment fixed. Compare the entire delivered note against all six declared criteria, recompute values directly from rows and compare source bytes. Do not grade solely by exit status, fluent wording or a model's self-check.

This adds a new decision task beyond the earlier missing-data tests. It shows all three groups can discover this consequential condition; it does not show a unique candidate gain, stable cost savings, human satisfaction or causal validity on live data. It is one task per arm, with no release V1 run, repeated sample, cross-model test or blinded human rating. The Skill remains core R15 plus workflow R21.
