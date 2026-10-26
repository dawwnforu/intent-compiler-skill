# Knowledge index / 知识路由索引

Use goals, context, artifacts, project state, and intended use together. Words are discovery hints, not automatic triggers. Select only rows affecting this delivery; do not read the entire library.

| Outcome / module | Load now when | Continue retrieval only when | Do not load / stop when |
|---|---|---|---|
| [Rendering and modeling](render-model.md) | A still, animation, or digital model is requested | Missing model/reference, material, camera, export, or tool capability prevents faithful delivery | Stop when visual inputs, output and inspection criteria are clear; no fabrication analysis for display-only work |
| [Physical fabrication](physical-fabrication.md) | The user intends to print, fabricate, assemble, or physically use an object | Fit needs dimensions/tolerances/process data; load or motion makes mechanics, joints and validation necessary | Skip for a render alone; stop when applicable checks are defined, or essential measurements/testing are unavailable |
| [Font library](font-library.md) | A product must offer real selectable fonts | Actual use adds embedding, packaging, server processing, distribution, download, or upload rights; exact files/terms or loading behavior are missing | Skip for revising copy; stop when selected resources, scoped evidence and fallback checks suffice, or rights remain unresolved |
| [Website delivery](website-delivery.md) | Someone must access a site outside its current environment | Inspected stack needs backend/storage/auth/upload support, public exposure needs a decision, or a chosen host/domain needs current terms and access | Skip for local text/style edits; stop when authorized path and access checks are defined, or an account/decision blocks deployment |
| [Interactive products](interactive-products.md) | Working UI, quiz, animation or simple game | A reachable state, entry resource, save/share path or frame check is missing; standalone HTML can use the optional local script check | Skip backend-only work; stop after actual interaction checks, not a markup-only pass |
| [Surveys and data](data-surveys.md) | Filling/designing a form, interpreting data or applying calculation rules | Missing facts, observation units, skip rules or denominators affect the answer | Read matching section only; stop at supported evidence |
| [Repeated workflows and Agents](workflow-knowledge.md) | Repeated processing or tool orchestration | Retry/state, extraction or live capability blocks delivery | Skip source-only questions and one-off edits; stop after relevant success/failure checks |
| [Knowledge organization](knowledge-organization.md) | Organizing records or answering project questions | A conflicting or unavailable source changes the answer; automated processing requires the workflow module | Skip runtime-only work; stop after supported answers or concrete missing evidence |
| [Web runtime](web-runtime.md) | Shared state, backend, URL diagnosis or access scope | Client/server, redirect, DNS or permissions are uncertain | Skip local style edits; stop at requested verified scope |
| [Print layout](print-layout.md) | Output needs physical dimensions | Units, resolution, preview/export parity or fit is unresolved | Skip screen galleries; stop after real output-size checks |
| [Game mod](game-mod.md) | An existing game's behavior must change | Version/API or multiplayer authority is missing | Skip standalone games; stop at verified runtime level or blocker |
| [Domain lenses](domain-lenses.md) | Other office, research, UI, image, product, coding, or writing work needs domain judgment | A relevant section reveals a necessary specialist method; reuse a skill or retrieve that method | Read only that section; no domain expansion from a loose keyword association |
| [Visual quality](visual-quality.md) | Appearance affects acceptance | Actual inspection reveals a composition, readability, material, lighting, or export problem | Skip nonvisual work; stop after relevant checks/targeted repair |
| [Source policy](source-policy.md) | External facts, current claims, or rights affect a decision | Evidence does not cover the actual resource/version/use/region, or materially conflicts | Stop on sufficient scoped evidence; unavailable evidence stays unknown |
| [Clarification policy](clarification-policy.md) | An unfamiliar project needs a visible scope recommendation, or an unresolved choice materially changes the result or exceeds authorization | New information changes a consequential boundary or reveals a necessary knowledge gap | Stop asking when scope and acceptance suffice; skip settled choices and reversible details |
| [Quality check](quality-check.md) | A substantial artifact or external outcome needs verification | A failed check justifies repair and rerun | Stop after relevant checks; report unresolved failure rather than looping |

## Three tiers

“Render this chair for a catalog, no fabrication”: rendering is required now; export-specific docs are conditional on the actual format/tool; printing and structural analysis stay out of scope. “Print a bracket to carry a shelf”: fabrication is required now; mechanics becomes required because carrying a load is explicit. Decorative rendering remains optional.

Keep a short task note only when helpful: `module → required reason / conditional trigger / excluded reason → next evidence or check`. Promote conditional knowledge only on evidence. Recommendations do not become prerequisites because a module mentions them.

## Continue and stop

First inspect existing files/docs, then the applicable authoritative source section. Every further retrieval must answer a named open question that changes implementation or acceptance. Stop when prerequisites are known, acceptance is testable, and no new critical gap remains. Stop a blocked branch when access or an essential user decision is missing; finish unaffected work and name the dependency. Do not expand into adjacent disciplines to fill waiting time.

## Add knowledge without code / 无代码维护

Copy [knowledge-module-template.md](knowledge-module-template.md), fill it in plain language, and add one row here with positive and negative triggers plus a stopping condition. Add an applicable and an exclusion case under repository `examples/`. The agent reads this index; there is no database, automatic search service, or code router to update.
