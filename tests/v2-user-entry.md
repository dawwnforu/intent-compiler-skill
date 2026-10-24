# R38: actual user entry-point repair

Four repaired products were generated and independently exercised. Do not adopt the extra core paragraph yet: the modified CSV run costs less with equal observed checks, but modified XLSX leaves unreadable log text. This is mixed quality/cost evidence, not a stable improvement. The [complete record](results/v2-user-entry.json) includes exact inputs, snapshots, commands, repaired sources, independent results and the separate evaluator repair.

## Protocol and interrupted attempt

The two real R37 registration artifacts fail through their default launchers. The user asks for repair on this computer without learning configuration, preserving existing processing and export formats. Both conditions receive the same actual failure output. The experiment adds a paragraph about verifying the documented user entry/environment rather than only the agent's prepared session, and probing command usability rather than path existence.

Order: XLSX-after, CSV-before, XLSX-before, CSV-after. Same model (gpt-6.1-sol/low), isolated Skill configuration and prepared generation environment. Independent acceptance uses the inherited, unprepared host PATH. These are two implementations of one already-reported failure, not cross-domain transfer or proof of spontaneously finding an unstated problem.

The initial attempt's fixture additionally instructed both arms how to test the user environment, duplicating the candidate instruction. It was interrupted, retained and excluded. The execution session terminated; a read-only process check found no remaining matching child processes before a new directory was used. The revised fixture contains actual error output only. This protocol correction must not be hidden as a successful or scored trial.

| Repair | Before output tokens / seconds | After output tokens / seconds |
|---|---:|---:|
| CSV | 4,812 / 163.96 | 3,680 / 131.74 |
| XLSX | 5,461 / 220.43 | 5,088 / 200.61 |

These are single observed repairs; lower cost does not establish a causal or repeatable saving. Modified XLSX also misses a check that the existing Skill's run ultimately satisfies.

## Independent checks and findings

The original delivered CMD/BAT entries run in isolated copies without adding Python to PATH. All four generate correct initial results (3 and 2), preserve comma-containing Chinese names and empty emails, reject conflicting duplicate IDs with exit 1 and no new CSV/XLSX result, preserve previous results and input bytes, then accept unseen next-week data (1 and 2). CSV is parsed independently and XLSX opened with the existing openpyxl library. No Explorer mouse double-click or spreadsheet GUI test is claimed.

Both CSV repairs and before-XLSX produce readable Chinese output/logs. After-XLSX's data and exit statuses pass, but its persisted log contains damaged text. Its `-I` Python invocation ignores the UTF-8 environment setting; an actual host probe reports GBK under `-I` and UTF-8 under `-I -X utf8`. The first verifier recorded data checks only; when unreadable output was observed, the persisted log was inspected and incremental log capture added. Do not retroactively present the first functional pass as complete novice usability.

A **separate evaluator repair** adds only `-X utf8` to the after-XLSX application invocation in a copied artifact. Running its actual entry again passes initial, invalid and next-week cases with readable new log text. The frozen comparison product remains unchanged. This verifies a concrete fix, not a gain attributable to the experimental Skill. Existing historical log lines are retained.

## Decision and reproduction

Keep the current core unchanged. Preserve the lower observed CSV cost as a useful signal, the XLSX readability miss as a real limitation, and the implemented repair as an example of resolving an execution prerequisite. Do not add more general rules based solely on one positive cost pair. Human judgments of utility remain separate from runtime correctness and output length.

The embedded runner reproduces generation with the existing evaluator. Save the embedded verifier as `check_user_entry.py`; it takes `before|after` and `csv|xlsx`, expects fresh isolated directories, and must run only on synthetic data. `after xlsx --utf8-repair` produces the separately labelled repair. Preserve UTF-8 BOMs when reconstructing PowerShell artifacts. Reproduce initial/unseen/conflicting inputs from the record and R37 fixture; do not apply the repair to the frozen comparison copy. No global PATH, machine policy, installed Skill, license or marketplace package changed.
