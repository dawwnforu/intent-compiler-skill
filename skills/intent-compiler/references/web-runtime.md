# Web behavior, URLs and access

Load for shared state, APIs, URL handling or access beyond one device; exclude static local style edits. Inspect app, client/server boundary, URL and runtime before choosing hosting.

- Frontend display, localStorage and shared server state differ. Same-profile tabs do not prove collaboration across devices. Test independent clients and late join/reconnect when sync is requested.
- Define state authority and stale/duplicate event handling. A spinner is not proof the server saved data; check reload and a failed request.
- Localhost is local. Separate interface/network reachability, hosting, DNS, TLS and authentication. DNS does not host a backend; a static host cannot run an arbitrary persistent server.
- For URL diagnosis, inspect scheme, host, path, redirects and status/content. Link text does not prove destination. Never log credentials.
- If a server fetches arbitrary user URLs, constrain schemes/targets and redirects for its actual purpose so private/internal endpoints are not exposed. This is conditional, not a security audit for every link.
- Screen/microphone access needs actual permission and supported context. Selecting a region does not authorize continuous full-screen capture or provider uploads.

Prerequisites: intended audience/access, stack and available account/domain rights. Local reversible defaults are fine; DNS changes, public exposure and purchases require existing authorization. Route deployment to [website-delivery.md](website-delivery.md).

Sources: actual config/app and relevant [MDN](https://developer.mozilla.org/en-US/docs/Web) or exact host/DNS documentation. Verify changing features/prices/terms. Accept by testing the requested scope: local, independent clients or external URL. Stop on verified access or a specific missing account/permission.
