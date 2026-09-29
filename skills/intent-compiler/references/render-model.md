# Rendering and digital modeling

## Applies and trigger
Load for a requested still, animation, or digital model, after inspecting existing assets and intended use.

## Exclude
A display render does not require printing, manufacturing, mechanical analysis, rigging, or simulation. Add a stage only if it serves the actual deliverable. Physical use triggers [physical-fabrication.md](physical-fabrication.md).

## Prerequisites
Check available model/reference images, protected product geometry/identity, intended medium, output size/format and actual rendering/modeling tools. Distinguish visual references from measured geometry. Missing renderer means you may prepare a scene or instructions if tools permit, but cannot claim a rendered image.

## Decisions
For a catalog image, prioritize silhouette, materials, lighting, camera, composition and background appropriate to the catalog. Use reversible defaults for lights and framing; preserve requested colors and geometry. Do not invent real dimensions from an unscaled picture. For an editable model, verify target application's import/export needs; a flattened image does not satisfy that deliverable.

## Common omissions
Missing texture files can produce a plausible but wrong surface. Inspect asset paths. Intended display size affects crop, detail and text readability. Ask about the actual use only if context cannot establish it and it changes the result.

## Sources
Reuse the project's scene notes and applicable available image/3D skill. Consult the relevant version's [Blender manual](https://docs.blender.org/manual/en/latest/) sections on rendering, materials or import/export when needed. This URL is an entry point, not evidence that a particular tool/feature is available. Verify current capabilities and asset licenses at execution; use [source-policy.md](source-policy.md).

## Execute
Inspect inputs → choose only needed modeling/material/light/camera steps → render/export using available tools → inspect actual output using [visual-quality.md](visual-quality.md). Keep edits reversible where possible.

## Accept
Open the actual image/model, check requested format, dimensions, silhouette, materials, composition and preserved details. Inspect animation over relevant frames if requested. Report missing renderer, unrendered scenes or unverified export distinctly. A beautiful image proves no physical strength or fit.

## Continue and stop
Retrieve only a missing asset, applicable tool method or output constraint. Stop when the visual task's prerequisites and checks are clear; do not follow manufacturing associations. If source geometry or tools are unavailable, finish independent preparation and identify the blocked output.
