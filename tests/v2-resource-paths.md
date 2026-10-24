# R82: keep non-relative script URLs out of filesystem checks

## Problem and decision

The optional HTML checker was intended to check relative files and leave remote/server-root resources unverified. Inspection of the maintained helper at `8f3c454` found that it classified a URL **before** decoding its path, then passed the decoded value to `Path.is_file()`. Encoded slashes, Windows drive paths and backslash UNC paths could consequently reach a filesystem metadata operation. On Windows, joining a rooted path can discard the intended parent; a UNC lookup may involve a remote share. No actual share access, authentication disclosure or exploitation was attempted or observed.

The new intercepted regression reproduces six unexpected metadata calls before the correction. The ordinary protocol-relative URL already skips correctly. Classify the decoded path as well, using the standard library's lexical `PureWindowsPath.drive` and leading slash/backslash checks, before any file probe. Preserve the original URL in diagnostics and explicitly report these resources as **skipped**, not checked or loaded. No network fetch, new dependency, global configuration or Skill prose rule is introduced.

This changes the shipped helper, not the core Skill or its routing. It prevents this specific inappropriate probe and associated misleading missing-file diagnoses; it does not prove less user prompting or rework. Relative symlinks, arbitrary HTML validity, JavaScript execution and the serving environment remain outside this check.

## Actual checks

[Machine-readable observations](results/v2-resource-paths.json) retain the original commit, before/after helper hashes, seven source cases, intercepted probe counts and actual CLI results. The separate developer harness reads frozen helper copies and uses synthetic `example.invalid` strings. It replaces `Path.is_file` before inspecting non-relative cases, so no remote path is contacted. This is a developer regression check, not independent human feedback or a browser/network penetration test.

- Before: the new test fails on six source subcases. The existing four test methods still pass.
- After: all five methods pass, including all seven path subcases. No path subcase reaches the intercepted metadata call.
- Both: actual CLI checks accept an existing percent-encoded Chinese relative filename and reject a missing relative script with exit codes 0 and 1. The HTML inputs remain byte-identical.
- Model calls: **0**. This deterministic tool defect does not need another generation of the already-passed business tasks. Professional rescue prompts, user rework, adoption and external feedback remain unmeasured.

Reproduce with `python -X utf8 -B tests/test_html_scripts_candidate.py`. The tests are already part of GitHub CI. The new case can also run against a saved pre-fix helper by passing its path as the script's first argument. Local interpreter: Python 3.12.14 on Windows. Remote CI and exact new-package installation are recorded separately when completed; this test does not establish host discovery or marketplace compatibility.

Repository preparation also ran the existing packaging (6), method-exposure (7) and reference-input (6) tests, the trial-package self-check and the unchanged revenue model. The first reference-input invocation failed on four sandbox temporary-directory permission errors; rerunning only that suite with process-local TEMP/TMP pointing to a writable task directory passed. No security setting or global environment was changed. Initial repository integrity checked 542 links; later package-link edits have their own count. These routine checks do not create business-effectiveness evidence.

Sources: [Python 3.12 pathlib operators](https://docs.python.org/3.12/library/pathlib.html#operators), [pure Windows drives and UNC paths](https://docs.python.org/3.12/library/pathlib.html#pathlib.PurePath.drive), and the [HTML script resource definition](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-src), checked 2026-10-24. This is conservative local checking, not a complete browser URL resolver.

## Launch consequence

Build a **new** committed-source candidate containing the corrected helper; retain the old archives and their own evidence. No PR merge, formal Skill replacement, MIT change, platform submission or publication occurs in this correction. The launch decision and remaining platform gates live in [the existing submission plan](../commercial/SUBMISSION.md#本周交付窗口2026-10-24至10-25).

The actual new archive is `intent-compiler-2.0-candidate-af3d2c8.zip`: source/runtime `af3d2c80e37e77b03d661fd803422f949d04ee89`, 37,504 bytes, 25 members, SHA-256 `4aad2ccccaac4869f5b5b9b958b6a97e8764b0e54ed5f7ea076ba6a0961c4bc5`. Rebuilding from committed blobs produces exactly the same bytes. Fresh project extraction matches every member, and the installed helper passes all five test methods. The first installation verifier incorrectly compared committed LF LICENSE bytes with Windows worktree CRLF bytes and stopped **before extraction**; its source and failure note are retained locally. The corrected verifier compares the archive to the original committed MIT blob, not a modified licence or rebuilt product.

At R82, this exact archive has no fresh host-discovery/model-business or browser-download observation. Previous Codex evidence remains separately scoped; the new installation/tool checks do not replace it. The CLI version query still reports `0.163.0-alpha.10.2` and emits temporary-alias cleanup warnings; no global configuration was repaired. The machine-readable package receipt retains those original unverified stages; later acquisition evidence is separate below.

## R96 — actual browser acquisition of af3d2c8

2026-10-24: close the still-unverified browser-download step for the current GitHub fallback, not another model task. Reuse R82's successful programmatic acquisition; no new fetch or model generation. Freeze one click on the fixed d4648d8 file page's **Download raw file**, with8-second download-event and8-second saved-path waits. The actual download event returns a saved file in4,371ms, without another click or indefinite wait.

The actual downloaded ZIP is37,504bytes and matches the SHA-256 above, the prior Git blob, all25 member names and all24 declared member byte/hash entries. The18 references, SKILL/SOURCE/README/LICENSE, supported host metadata and optional checker are present. No new installation/discovery/business run is inferred. The first verifier wrongly requires the explanatory `license` field to equal bare `MIT`; preserve that script and failed report. Inspecting the actual standard LICENSE shows its bytes already match the original committed hash. Remove only the verifier's unsupported string restriction, then all12 acquisition checks pass on the **same downloaded file**, without redownloading or changing the product.

Local `outputs/intent-compiler-v2/acquisition-r96/` retains the protocol, browser event/path receipt, actual byte copy, failed/corrected verifiers/reports and file-page screenshot. `verify_download.py` repeats only local file checks. External trial-user receipt/installation/adoption remains unknown; browser download on the author's machine is not real-user feedback. Earlier browser failures remain preserved. Source, ZIP, MIT, live Agensi package, update-preview review status, formal installation and revenue assumptions are unchanged.
