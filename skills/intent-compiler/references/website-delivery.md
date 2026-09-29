# Website access and deployment

## Applies and trigger
Load when the user wants others to access a site outside its current environment.

## Exclude
Do not load for a purely local content edit. Deployment is not “changing a private domain to a public domain”. Custom domains, paid plans and production operations are not prerequisites for every public demo.

## Prerequisites
Inspect where the site runs, stack/build commands, backend, database, login, uploads and sensitive configuration. Identify actual runtime/tool/account access and the intended audience/duration from context. If unclear and consequential, ask “Temporary demo for friends, or long-term public service?” rather than asking for an architecture.

## Decisions
Distinguish local preview, temporary public demo, persistent public deployment and custom domain binding. Choose based on inspected requirements and current official provider information. Cloudflare is an option, not the default; compare only viable alternatives when choice matters.

Identify exactly what becomes public: content, uploaded files, APIs and client-visible configuration. Keep credentials/server-only values out of public bundles and logs. Prepare a reviewable build before requesting any missing publication decision. Reuse explicit authorization to publish the specified content/audience; do not request it again.

Check whether an account, domain, database/storage service or paid resource is actually needed. Verify current prices, quotas, renewal/ongoing costs and operational limits for the proposed use. Do not assume payment is required or promise perpetual free service. Buying/subscribing/expanding spend needs corresponding authorization; a budget suggestion is not approval.

Scope privacy, asset rights and applicable regional checks to operating region, audience, data processing and intended use. Do not issue a blanket “all laws satisfied” assurance or a generic compliance course.

## Common omissions
Production build differs from development; a working localhost URL is inaccessible to others. Deep links, backend endpoints, database persistence, login callbacks and upload access can fail after deployment. A public tunnel may expire. Domain ownership, DNS access, HTTPS, renewal and maintenance matter only where the chosen path needs them.

## Sources
Use project deployment docs and relevant available hosting skills first. Provider entry points include [Cloudflare docs](https://developers.cloudflare.com/), [GitHub Pages docs](https://docs.github.com/en/pages) and the selected host's official docs/pricing/terms. These are candidates, not claims of feature/plan suitability. Check the chosen path at execution time and record scope/date with [source-policy.md](source-policy.md).

## Execute
Inspect → choose a supported path → verify current conditions → prepare/configure/build within permissions → resolve only missing publication/account/payment decisions → deploy if authorized and capable → test real external access. Never include secret values in evidence or public artifacts.

## Accept
Open the real resulting URL from an external/browser context and test key pages, deep links and relevant backend/auth/upload behavior. Check public artifacts for sensitive configuration. Verify HTTPS/domain resolution if part of the target. Report address, observed access, actual checks, ongoing obligations and unresolved limitations. Provider “success” without access verification is deployed-but-unverified, not confirmed live.

## Continue and stop
Retrieve backend/storage/domain guidance only when inspected requirements trigger it. Stop when the authorized path, prerequisites and verification are defined. Missing account, credential or decision blocks that step; finish local preparation, explain the missing capability, and do not invent a public URL.
