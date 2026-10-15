# R52: a playable charge-and-throw loop

Status: all three generations complete. A and V2 have bounded independent actual-browser acceptance; G UI remains pending. V2 has a demonstrated misleading failure hint; no comparison winner or runtime change. [Exact protocol, runner, snapshot and available records](results/v2-throw-game.json).

## Candidate V2: usable loop, incorrect corrective advice

V2 completes in291.93seconds with9983 output tokens. Actual browser play verifies flight, visible successful landing, automatic next station, automatic failure retry, capped100% charge, manual restart during flight, persistent best score and390px pointer gameplay without horizontal overflow. Short Space press initiates flight. These retain practical functions, but raw A already supports the core loop and best score.

The candidate adds calculated directional failure advice. At70% the UI says the throw overshot; reducing to65% produces an actual successful landing. However, on station2, two actual23% throws also say “飞过头啦！下次温柔一点。” This is wrong: applying the delivered fixed-step flight equations to the displayed rounding interval's endpoints and midpoint places descending platform-height crossing at x410–418, before the minimum possible target x540. The fail handler instead compares the later fallen body's x with the target's left edge. The post-hoc diagnostic and actual screenshot are separate evidence; no evaluator repair is made.

Failure feedback resets after0.65seconds in the source; the first actual observation missed the message. Semantic waits subsequently captured it. A wait for the expected correct underthrow message timed out and remains recorded; a broader result wait revealed the wrong advice. A helpful-sounding feature is not a benefit when it recommends the wrong adjustment. The candidate's higher observed time/output is not justified merely by its larger feature list, nor does this one case establish general harm.

Both A/V2 evaluator servers and tabs are closed, with viewport overrides reset. G completed in224.32seconds with8735 output tokens but has not yet received independent browser acceptance. Physical mobile, held-input interruption, sound, direct-file entry and frame-rate variation remain unverified independently. Model self-test claims and failures are preserved separately.

## First actual product: raw A

A completes in178.66seconds with7172 output tokens. Independent CUA operations confirm charge/release, visible flight, actual success and failure, immediate retry, next-station continuation and a capped long hold. An800ms hold displays60% and misses; a650ms hold displays49% and lands on the cushion with score1; a2second hold caps at100% and misses. An additional ordinary-click attempt is preserved as a real0% failure, not silently omitted. Success screenshots show the person on the target, not only a score change.

At390x844, actual pointer play again succeeds at49%; document width equals390 without horizontal overflow. After reload, best1 remains while the current run resets. Space from a successful result advances to the next station. The delivered raw request already supplies progression, retry and a persistent best score; these cannot later be attributed exclusively to Skill.

Source inspection finds bounded elapsed-time updates and cancellation handlers; held-input interruption and frame-rate invariance have not been independently demonstrated. A resized desktop is not a physical touch-device test. Native file launch, sound and sustained keyboard charge remain untested. The temporary browser tab and server are closed and the viewport reset. No generated source was repaired during scoring.

The source inspiration is [Throwteammate](https://github.com/dawwnforu/Throwteammate), README at commit02508d213c32e3f95fda36af6b9db55cd7a2fa49, retrieved2026-10-15 through the public GitHub API. Its charge/release/cancellation mechanics motivate a new browser-game request. This is deliberately a separately stated browser task, not a conversion of a request to modify PEAK into an easier deliverable. No original conversation, gameplay audit, engine compatibility or multiplayer validation is claimed. The source implementation and README are withheld from generators.

Compare raw request, current Skill and a short generic instruction, one generation each with identical tools, permissions and model settings. The runtime snapshot includes adopted knowledge through7395bfb and excludes the unadopted R51 candidate. No new rule is introduced merely to make this trial win.

Acceptance requires actual charge/release flight, observable success/failure, quick retry and continued use, understandable controls and preserved useful supporting features. Inspect interruption, bounded charge, reset behavior and timing; test actual browser controls and narrow layout. A visible score or function named collision does not prove the game works. Static timing inspection and a resized desktop are not substitutes for frame-rate or physical-mobile testing.

Record practical additions without requiring every game to have an identical feature list. Preserve generated failures and do not repair products during scoring. This trial cannot establish stable token savings, general superiority, subjective enjoyment or a successful PEAK mod. No outcome is reported before the relevant checks run.
