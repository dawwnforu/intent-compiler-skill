# Interactive products

Load for a working UI, animation or small game; exclude static copy edits, backend-only work and fabrication. Reuse the project's framework and installed browser tools. Determine target devices, main action and existing data; choose reversible styling defaults.

## UI and forms

A screenshot is not a working flow. Identify start, interaction, result and reachable empty/error states. Test the primary path at a narrow viewport and with keyboard focus. Preserve answers on back navigation; a changed answer must update dependent results. Prevent repeated clicks from double counting or premature submission.

If a result must be saved/shared, deliver an actual downloadable artifact or supported share path with fallback. A decorative button is incomplete. Visual choices do not authorize accounts, analytics or cloud storage.

## Motion and simple games

Identify moving object, trigger, duration, terminal state and restart. Use elapsed time rather than frame count; prevent duplicate loops/listeners on reset. Test start → play → fail/finish → restart, repeated input, background/resume and relevant touch/keyboard controls. Inspect actual frames, not just an animation flag.

Respect reduced-motion for decorative effects; keep controls usable. A simple game does not require a game engine. Route digital 3D assets to [render-model.md](render-model.md), never infer physical manufacture.

## Sources, execution and stop

Inspect existing components and relevant specialist Skills, then needed [MDN](https://developer.mozilla.org/en-US/docs/Web) or engine documentation. Verify current API support when it affects the route. Implement the smallest complete flow, then inspect real rendering and interaction. Retrieve further only for a failed interaction or missing capability. Stop after relevant checks, or label missing device/browser verification.

Common omissions: fake persistence, inert buttons, lost answers, inaccessible focus, stale restart state. Do not turn this into a full product redesign or unrelated accessibility audit.
