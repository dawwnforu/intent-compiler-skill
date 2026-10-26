# R26: repair evaluation isolation after host updates

2026-10-13. The R25 preflight exposed an outdated disable inventory after a host plugin update. The model was correctly stopped before generation, but the common runners needed a reusable repair rather than repeated fixture-specific workarounds.

The single-turn and resumed-dialogue runners now inspect actual enabled Skills before a model turn. On mismatch, they merge newly observed paths into the disable inventory, preserve the first probe, rebuild the configuration and probe once more. A remaining mismatch raises an assertion before model execution. The intended Skill must match by exact resolved path, not merely name. No plugin is uninstalled and no user setting is changed.

[Exact helper/check code and live preflight results](results/v2-isolation-refresh.json) record five deterministic checks: clean raw configuration, exact target, newly discovered Skill disabled on refresh, persistent extra Skill rejected and missing target rejected. Actual app-server probes also confirm zero enabled Skills for A and only the isolated candidate for V2. The raw probe required a refresh. No model generation was invoked.

This checks the host's declared Skill inventory, not every hidden instruction or tool, and is not a model-quality gain. Historical invocations/results remain unchanged; specialized legacy runners still require their own preflight. Reproduce by running the recorded check script with the common runner module available; it uses local standard-library mocks followed by actual inventory probes, not a paid model test.

An inline user-feedback question separately compares two short actual R18 excerpts about choosing authentication versus first deciding whether cross-device recovery is needed. On 2026-10-13 the user answered “乙：先说明使用需求如何影响方案”. This is a preference for B in this excerpt, not an overall satisfaction result. Prior R15 opening preference remains distinct.
