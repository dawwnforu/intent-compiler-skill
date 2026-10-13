# R37: text-transfer rule before/after

Four actual runs completed. Do **not** adopt the experimental core paragraph: both after runs used more output and time, with no exclusive correctness gain. This does not prove the paragraph causes higher cost; there is only one pair per domain. The [record](results/v2-text-transfer.json) preserves the exact paragraph, frozen snapshots, prompts, inputs, commands including failures, product sources and independent verifier sources.

The experiment adds guidance to prefer explicit-encoding files over unverified nested shell strings/pipes and distinguish transport damage from artifact logic. This follows R36's actual Unicode and quoting failures. It does not remove functions or change input requirements. Order: catalog-before, summary-after, catalog-after, summary-before; same isolated Skill evaluator, gpt-6.1-sol/low and prepared Python environment. All original input texts remain unchanged.

| Case | Before output tokens / seconds | After output tokens / seconds |
|---|---:|---:|
| Exhibition catalog | 3,594 / 126.59 | 4,663 / 186.88 |
| Registration summary | 4,771 / 151.17 | 5,294 / 169.71 |

## Independent artifact checks

Both catalogs preserve exact titles/authors/descriptions including Chinese and literal special symbols, produce resolvable index/return links, and regenerate correctly after renaming one work, removing another and adding a new one. Tests run on copies and check input bytes are unchanged. Before's delivered CMD launcher was executed. After's original PowerShell generator was executed; its CMD also auto-opens a browser, which was not invoked. HTML was parsed rather than visually/browser tested. Do not treat different validation scopes as a usability ranking.

Both registration implementations correctly deduplicate by submission ID, count the initial activities as 3 and 2, preserve the quoted-comma name and empty emails, and process unseen next-week input into counts 1 and 2 with the new activity and no stale group. Before emits BOM CSV; after emits an XLSX workbook independently loaded by the existing openpyxl library. CSV/XLSX GUI appearance is unverified. These are format tradeoffs, not an exclusive gain.

## Launcher failure matters

The default host environment does not reliably provide an executable `python`. Independent original-launcher checks produced no output in **both** registration arms. Before reported `python` unavailable; after selected a WindowsApps placeholder that could not execute instead of trying its existing-runtime fallback. Both launchers eventually returned zero after the failure/pause, so a successful exit code alone would have falsely passed them.

On fresh copies with the known existing interpreter prepended to child PATH, matching the generation environment, both original launchers and unseen-input data checks passed. This is conditional processing success, **not** a repair or a successful default launch. No global PATH or machine execution policy was changed. No generated product was repaired to improve its comparison score.

The first after-summary independent check found no output but had not persisted the subprocess text. A fresh copy reproduced the failure with captured output; both attempts are retained locally. The before-summary generator also hit a Chinese-pipe failure and batch-file parsing issues and repaired them during generation. Read command outputs as well as exit codes because a compound command can mask an earlier failure.

## Decision and next evidence

Keep the current Skill. The extra general encoding reminder did not show a useful comparative benefit. The concrete next hypothesis is about testing the **user's delivered entry point in its actual runtime environment**, rather than only the evaluator's prepared environment. The evaluation harness should keep equal generation conditions and report that distinction; it must not hide launcher defects by counting interpreter-level execution as full usability. This is a discovered prerequisite gap relevant to non-programmers, not grounds to add generic platform rules everywhere.

Reproduce generation using the embedded runner and snapshots with the existing evaluator. The embedded independent checks use isolated copies; catalog verification takes `--after` for the PowerShell variant, and summary verifiers use `--recovery` for the explicitly prepared-PATH checks. Default-launcher failures are expected evidence, not a reason to patch the evaluated artifacts. Verifiers create fresh directories and must not be rerun against user data. Decoded PowerShell artifacts should be reconstructed with the original BOM requirements. No installed Skill, license or marketplace package changed.
