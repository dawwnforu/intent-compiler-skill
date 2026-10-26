# R21: partial improvement in text-to-status repair

Before is `3b11d953bda7444550dd2de2515fa3bac4b72679`. After substitutes one paragraph in `references/workflow-knowledge.md`: assess the statement rather than its heading or isolated vocabulary, preserve proposal/condition/decision distinctions, test contrasting wording and update derived records. The exact tested paragraph is now retained in the candidate; core instructions remain R15. [Exact change, inputs, generated code, full responses, commands and independent observations](results/v2-status-evidence.json).

Two fixed actual repairs completed in order after/before, using gpt-6.1-sol low, isolated Skill discovery, disabled browsing/network and the unchanged R20 ordinary-language request plus original wrong cache. Actual tool output confirms the after module was read. Ten independent processor executions then replay old cache, repeat, introduce new cases plus an empty input, repair that input, and repeat again. Both processors preserve source bytes, archive bytes, displayed source text/anchors, no-duplicate behavior and accurate failure/retry status. Both final scripts retain UTF-8 BOM and run through the original PowerShell `-File` invocation.

## Observed classification

Both repair all four original records correctly. The ten additional cases were fixed before either repair result was reviewed; five carry over from R20 development evidence, and five are new wording/meaning cases. Six before and eight after match the declared categories. This count describes this tiny selected set, not general semantic accuracy.

| Boundary | Before | After |
|---|---|---|
| Not yet decided whether to postpone | Correct unresolved | Correct unresolved |
| Decided not to extend registration | Correct decision | Correct decision |
| Confirmed not to increase budget | Correct decision | Correct decision |
| Budget proposal only for discussion | **Wrong decision** | **Wrong decision** |
| Confirm date if venue approved | Conditional/unresolved label | Conditional/unresolved label |
| Delete the quoted “待确认” UI text | **Wrong unresolved** | Correct decision |
| Proposal not yet voted on | **Wrong decision** | Correct unresolved |
| Reject the budget-increase proposal | Correct decision | Correct decision |
| Meeting reached no common conclusion | **Wrong decision** | **Wrong decision** |
| Previously tentative date now confirmed | Correct decision | Correct decision |

The conditional case can also represent an agreed conditional procedure. Matching our condition/unresolved category is not proof that an alternative coarse decision label invents actual approval. Original text remains visible; keep this annotation limit when interpreting counts. The discussion-only and no-conclusion cases remain unambiguous failures.

The after code strips quoted vocabulary before matching and tests conditions more broadly. It still falls back to the heading when its patterns miss an expression. Thus it only partly follows the intended evidence rule: adding guidance has not supplied a general semantic engine or eliminated unsupported classification. The generated page now acknowledges its heuristic scope; that disclosure does not turn wrong categories into passes.

| Variant | Seconds | Input / cached input | Output tokens |
|---|---:|---:|---:|
| Before | 157.66 | 186404 / 165632 | 4583 |
| After | 189.65 | 256094 / 221568 | 5434 |

No savings claim. After repaired intermediate syntax and test-assertion errors; before encountered an empty search result and an execution-policy failure before successful invocation. All are retained. Independent successful mechanical checks are separate from both models' self-tests and the two remaining semantic errors.

## Decision and limits

Retain the exact tested paragraph as a partial domain strengthening: two new distinctions improve in this pair, with no regression in the fixed original/transfer checks or mechanical behavior. It adds no parser, dependency, provider or database to the Skill. It does not resolve the entire R20 failure, establish causality from one pair, or make the candidate ready for a broad success claim. Future work must address the unsupported heading fallback, rather than add a keyword per failed sentence or silently redefine all decisions as unknown.

The [research note](../docs/v2-research.md) records the contrast-set paper's actual reading scope. This development experiment is retrospective, selected after a known failure, not a replication of its expert-curated datasets or a representative user study. No release/raw/generic arm in this pair; those R20 records remain separate. No browser click, concurrency, crash, human comprehension or cross-model claim.

Reproduce using the JSON's initial processor and source files to create old cached notes, then run fresh copies with the recorded before/after Skill and identical request. Independently replay the resulting processors against the original wrong cache; add the recorded acceptance cases, empty file and repaired file. Preserve exact input bytes, run/status output, HTML, records and failures. Use the same semantic judgments and report disputed labels instead of replacing a failed example. The complete generated scripts and tests are embedded for artifact replay.
