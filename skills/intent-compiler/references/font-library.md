# A usable font library

## Applies and trigger
Load when an editor/product must offer selectable fonts, inspecting the product and code first.

## Exclude
Do not load merely because a document has text. A single local typography adjustment need not become a font marketplace. Upload, download, hosting and redistribution are separate optional features unless requested.

## Prerequisites
Determine platform and actual use: UI display, web embedding, application packaging, server-side output, file distribution, user download or upload. Inspect existing font files, sources, license texts/versions, character coverage and loading code. A family name is not a font file.

## Decisions
- Check each chosen resource's exact terms for each actual use. Do not infer packaging or redistribution rights from permission to display text.
- “Free”, “open source” and “commercial” are labels, not a complete license analysis. Commercial use is neither automatically paid nor automatically permitted.
- If suitable resources and use-specific evidence are accessible, use them and retain required notices/source information. Unclear rights or missing files remain unresolved.
- For requested uploads, include appropriate source/permission prompts and file validation at the upload boundary. A user's declaration does not establish a legal guarantee.
- Use the project's existing loading and selection patterns; add only resources/features needed now. System fallbacks can keep an editor usable but do not prove a bundled font library has been delivered.

## Common omissions
Required scripts/glyphs and weights; actual rendered font versus silent fallback; network failure; layout changes during loading; export/server rendering consistency when that output is in scope; retained notices when distributing files.

## Sources
Inspect exact upstream font distribution and accompanying license first. [Google Fonts repository](https://github.com/google/fonts) can identify candidate resources and their individual license files, not blanket approval. [CSS Font Loading API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Font_Loading_API) is an implementation entry point for web products. Verify selected APIs against the target environment and terms against the exact resource/use at execution; record evidence with [source-policy.md](source-policy.md).

## Execute
Inspect product → select obtainable resources with applicable evidence → integrate actual loading, preview/selection and failure handling → retain required notices → test actual rendering and relevant persistence/export paths. If sources cannot be verified, complete resource-independent interface/loading work while marking those fonts unavailable; do not quietly ship unknown files.

## Accept
Demonstrate actual selected font use, required glyphs/weights, and intentional loading-failure fallback. Check keyboard/accessibility basics and relevant export consistency. Deliver resource source/version, license evidence and scope, notices, tests performed and unresolved choices. A dropdown of names alone fails.

## Continue and stop
Retrieve additional licensing detail only when an actual use is uncovered. Stop when each selected resource is obtainable, scoped evidence supports intended use, and functional checks are defined. If evidence or files remain unavailable, stop dependent release claims and name the missing resource/terms.
