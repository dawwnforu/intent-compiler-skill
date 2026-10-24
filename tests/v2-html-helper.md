# R42: a narrow executable HTML check

R41's extra verification sentence did not repair the vocabulary entry. R42 tests an executable alternative: a Python standard-library helper, conditionally referenced for standalone HTML, that reads script markup and checks relative script-file existence. It makes no network requests, changes no product files and explicitly does not test JavaScript startup, rendering or interaction.

The original helper remains a frozen [experimental fixture](fixtures/html-entry-helper/check_html_scripts.py). The initial suite at commit `c3d433f` passed three unittest methods, including eight markup/resource subcases. The initial sandbox temp-directory permission failure was resolved by placing test temporary directories under the repository. Tests cover comments, script text, XML-style self-closing scripts, encoded relative paths, missing resources, explicitly unchecked remote/root-relative resources and unreadable input. This is not a full HTML validator.

The [frozen protocol and artifacts](results/v2-html-helper.json) use the same known broken vocabulary and explanation products as R41. Both arms receive identical original self-tests, guides and synthetic inputs without the evaluator's diagnosis. The after snapshot adds only the helper and its conditional instruction; the failed R41 sentence is absent. Four fresh runs use identical prepared tools and model settings, in the order vocabulary-after, explanation-before, vocabulary-before, explanation-after.

Acceptance requires the actual delivered entry with original data to start, while practice, feedback/self-rating, progress reload and material updates remain usable. Check helper invocation and completion claims separately. Its direct diagnosis must reject the known vocabulary markup, while its pass on the broken explanation HTML demonstrates why markup checks cannot establish JavaScript initialization success.

All four runs completed. Both after runs actually execute the helper. Costs retain failed browser attempts and other commands; do not interpret one pair as stable efficiency.

| Product | Before output tokens / seconds | After output tokens / seconds | Independent result |
|---|---:|---:|---|
| Vocabulary | 4,278 / 184.75 | 7,809 / 334.03 | Before remains blank; after starts and retains tested behavior |
| Explanation | 9,419 / 347.96 | 5,785 / 296.47 | Both start and retain tested behavior |

Vocabulary-after executes the helper, receives the unclosed-script diagnosis, repairs the markup and passes recheck. Independent original-entry/handler execution verifies startup, wrong-answer retry, persistence, material update, idempotent import, retained statistics, invalid-input preservation and unchanged inputs. Actual IAB interaction confirms eight-word startup, an initially hidden answer, a wrong response retained after reload, successful mistake review and correct daily versus round accuracy. Before repairs secondary issues but leaves the missing script closure; its actual browser has an empty body with the intended body swallowed as script text. No evaluator product repair was made.

Both explanation products pass independent actual-HTML initialization, original-data, three-topic self-rating, note/reload, selective material-reset, invalid-update preservation and unchanged-input checks. Actual IAB interactions also confirm startup, hidden reference until requested, manual self-assessment and retained notes/progress after reload for both arms. Their model-side headless-browser attempts failed and temporary-file cleanup was rejected; these attempts remain recorded separately from evaluator browser passes. All preview servers were stopped.

## Adoption and subsequent compatibility correction

Adopt the optional helper in the 2.0 candidate, conditional on standalone HTML and an existing Python runtime. It provides a concrete diagnostic that the prose-only condition missed. Preserve useful functionality and actual interaction verification; markup-only success is never completion. This supports one known-failure repair, not general intent-recognition superiority or prevention on unseen tasks. Vocabulary cost increased; explanation cost decreased without an exclusive quality gain.

Before adoption, expanded tests exposed an incorrect missing-resource report on a page using a base URL. The [packaged script](../skills/intent-compiler/scripts/check_html_scripts.py) now leaves those resources explicitly unchecked. The [expanded suite](test_html_scripts_candidate.py) passes four methods, including ten markup/resource subcases and the separate base-URL case on Python 3.12.14. Textarea/title examples containing script-like text also pass. The frozen model snapshots were not changed; this mechanical correction and final routing wording were not rerun through model comparisons. The record stores the revised script and tests separately.

Reproduce current helper tests with `python -X utf8 -B tests/test_html_scripts_candidate.py`; reproduce model comparisons using the frozen runner, fixtures and snapshots in fresh isolated workspaces. The original pre-adoption suite is preserved at `c3d433f`. Browser file selection, actual backup download/restore and native double-click were not tested. Installed Skill, license and marketplace upload/package remain unchanged; only the candidate repository gains the helper.

Local adoption checks: the expanded helper suite and repository integrity check pass. The host's separate `quick_validate.py` could not start because its PyYAML dependency is unavailable; it is not reported as passing and no dependency was installed. The existing repository check covers local links, basic Skill metadata and package manifests, not every host validator rule or installation behavior.
