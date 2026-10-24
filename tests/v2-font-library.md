# R11: real font-library integration comparison

This is a new development test, not a relabeling of the older fictional-font C3 case. Generation and independent browser checks must both finish before a result is claimed. The Skill is frozen at candidate commit `d1d23a23273b3a4941f4338a6717720c4106abbc` (same executable instructions as R9). No within-batch instruction tuning is allowed.

## Fixed request and inputs

> 我想把 inputs 里的小海报编辑器做成能用的字体库，选不同字体时，海报上的中文真的跟着变，保存下来的图片也要一样。我不懂字体和开发，给店里做活动海报用；先在自己电脑上用，断网也能打开。朋友给了两款字体文件，你帮我判断能不能用，把能用的接好，讲清楚还缺什么。两款够用了，不做上传和字体下载功能，也不要发布到网上。

All arms receive the same small canvas editor, initially containing only two font names without loading code. They also receive the two real TTF files, individual OFL notices, metadata and source record from Google Fonts commit `bd8f81ddb5c74d5c8897b36ad88b440266245103`, retrieved 2026-10-12. The fixture does not tell the agent its conclusions: inspect the evidence for the requested local commercial-poster use. This supplies equal resource availability; it does not test finding unspecified fonts from scratch.

Four sequential arms, one trial each: raw request (A), frozen candidate (V2), short generic rule (G), installed release0.2.0 snapshot (V1). The base model is gpt-6.1-sol with low reasoning effort, identical available tools and900-second generation limit. Other Skills/plugins are disabled equally and actual enabled-Skill paths are checked before each run. Read public sources and write isolated outputs only; no installation, payment, upload, publication or real-project modification.

## Acceptance recorded before generation

- Inspect actual resources and scoped license evidence; retain notices and do not infer blanket rights from a font label.
- Both selected fonts actually render the tested Chinese text, rather than silently using a system fallback.
- Local use works offline without runtime CDN requirements or installing dependencies.
- Download a real PNG for each selected font and compare decoded pixels with the corresponding displayed canvas after changing the title.
- Inject a cold font-load failure in an isolated browser. Record whether the user receives an accurate unavailable/fallback state, rather than a false selected-font claim.
- Explain relevant conditions in ordinary language and retain the requested two-font, no-upload scope.

## Independent checks and limits

Use installed Edge with a fresh profile and a dynamically allocated debugging port. Inspect the generated entry point/controls before mapping selectors. Open the actual file while network access is emulated offline, select both fonts with the same Chinese title, inspect loaded FontFace records and draw calls, save canvas pixels, click the actual download button and inspect the downloaded PNGs. Compare tested Chinese glyphs with a monospace fallback to detect silent substitution. This is sample coverage, not proof of every Unicode character.

For the failure condition, serve the same files on an ephemeral localhost server that returns404 for font requests, with caching disabled. Programmatic `FontFace.load()` calls reject with a standard decode-error exception, covering embedded font buffers as well as file sources. Record intercepted calls/failed requests and the UI; this does not corrupt or remove delivered fonts. CSS-embedded data that bypasses both mechanisms is untested rather than passed. This injection method was adapted after inspecting the first implementation's embedded buffers, before evaluating its result; the failure-handling criterion is unchanged. A separate fresh file-open check establishes offline behavior.

The unmodified starter is the verifier's negative control: it must fail real-font loading and distinct-font canvas checks even though its PNG download works. It did fail both checks in an actual Edge run on2026-10-12. No generated arm result is inferred from that self-check.

One sample per arm, nonblind review, no human usability study and no statistical superiority claim. Process exit0 is generation completion, not a functional pass. Report failures, interruptions and untested conditions alongside successful checks. Font licensing evidence applies to exact supplied resources/use at this retrieval time; it does not amend the project's MIT license or establish future platform terms.

## Results: three completed deliveries, one interrupted generation

All four attempts are terminal. A, V2 and G completed. V1 exited1 after the service returned “Selected model is at capacity. Please try a different model.” It has no final response or final usage record. This is not a Skill-function failure, a zero-cost run or a completed delivery. No replacement trial is silently substituted. [All four attempt records](results/v2-font-library.json) retain the error, messages, commands, raw counters, inspected source code and independent browser reports; embedded binary strings are explicitly omitted from the public record, with originals retained locally.

| Arm | Generation | Output tokens | Wall seconds | Independent saved-artifact result |
|---|---|---:|---:|---|
| A — raw request | Completed | 7728 | 333.48 | Both fonts loaded offline, distinct tested Chinese glyphs, two real matching PNG downloads |
| V2 — candidate | Completed | 6458 | 307.06 | Same core checks passed |
| G — short rule | Completed | 7394 | 311.54 | Same core checks passed |
| V1 — release0.2.0 | Capacity interruption | Unavailable | 358.64 until failure | Same checks passed on saved partial artifact only |

For each saved page, actual Edge opened the file with network access disabled, loaded both supplied custom fonts, rendered the same title `春日花市欢迎你` differently and downloaded two900×600 PNGs through the real button. Independent Pillow decoding found each exported RGBA pixel array equal to its corresponding canvas image. The seven tested characters differed from the monospace fallback for both loaded families. This is not a complete Unicode-coverage or cross-device print test. Normal and failure screenshots were inspected.

The failure injection reached actual `FontFace.load()` calls in all four products. All prevented saving an unavailable selected font. A displayed the raw English decode error. V2 explained the failure in Chinese and suggested another font; G explained keeping the complete folder and reopening; V1's partial page explained reopening or switching and marked its preview unavailable. V2 therefore had a clearer observed failure explanation than A, but G and the partial V1 also did so. Both fonts were deliberately failed; recovery after restoring a resource was not tested. These messages do not prove a successful recovery path.

The implementations inspect character coverage and include missing-character handling. The generating agents' own coverage/edge-case checks are recorded separately from the independent seven-character test. All saved products retain font notices. A/G explicitly rely on the supplied source record rather than claiming remote byte verification. V2 additionally fetched and byte-compared the exact upstream fonts, licenses and metadata. V1 read upstream license sources but did not finish a final provenance report before interruption. None of these checks is blanket approval for unrelated fonts or future platform terms.

Product tradeoffs also remain visible: A lets both title and editable description use the selected font; V2 explicitly limits it to the title and keeps the editable description in a system font; G retains a fixed fictional-sample footer and explains the need for actual promotional copy; partial V1 makes both text fields editable in the selected font. No unrequested composite aesthetic score or claim of identical feature scope is assigned.

V2 used fewer output tokens than the two completed baselines in this single sample. Input and cache counts differ and are retained. Wall time includes several browser-control troubleshooting attempts by the generating agents; one fixed-order trial cannot establish a stable or causal cost advantage. There is no complete four-way final-response ranking and no unique core-font capability gain. The active Skill remains unchanged from R9. This closes the scoped real-resource/runtime evidence gap, not the older missing-resource C3 condition, human preference testing or general superiority.
