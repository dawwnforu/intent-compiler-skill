# R52: a playable charge-and-throw loop

Status: all three generations and bounded independent actual-browser checks complete. V2 has a demonstrated misleading failure hint; no runtime change or overall winner. [Exact protocol, runner, snapshot and records](results/v2-throw-game.json).

## Final comparison

All three deliver a working pointer-play loop: charge/release, observable wins and losses, retry/continuation, capped charge, best-score persistence and successful390px play. These are not exclusive Skill gains. Candidate2.0 is the slowest and largest output in this single trial; different model-side verification work prevents a stable efficiency conclusion.

| Arm | Seconds | Output tokens | Observed practical difference / failure |
|---|---:|---:|---|
| Raw A |178.66|7172|Manual retry/next station, best score and working Space continuation; failure text is randomly selected encouragement.|
| Skill V2 |291.93|9983|Automatic retry/next station, manual in-flight reset; actionable23% underthrow advice is demonstrably wrong and result text quickly disappears.|
| Generic G |224.32|8735|Persistent result view, correct advice for tested17% short and100% long shots; focused retry button ignores Space but works with Enter and pointer.|

G's actual first-level49% throw succeeds; next-level17% fails with a correct increase-force suggestion, and100% fails with a decrease-force suggestion. At390px,50% succeeds with no horizontal overflow; best1 survives reload. A failed Space retry and the following attempted press on a still-disabled throw control remain recorded rather than counted as a successful input. Source inspection suggests global Space keyup suppresses native button activation. Correct advice in two extremes does not validate every G miss; its diagnostic also uses a later body position.

The next useful improvement is outcome-based feedback verification: use evidence from the event that decides success/failure and test whether the recommended adjustment actually improves the attempt, while keeping useful feedback available for the next try. This is a proposed follow-up from an exposed failure, not an adopted generic rule or a passed fix. Simply adding more helpful-sounding functions is not the goal.

All evaluator tabs/servers are closed, viewport overrides reset, and original deliveries unchanged. Physical touch, held-input interruption, native file entry, sound, broad frame-rate behavior and subjective enjoyment remain unverified independently. No PEAK compatibility or multiplayer claim. The whole upgrade objective is still unproven.

## Candidate V2: usable loop, incorrect corrective advice

V2 completes in291.93seconds with9983 output tokens. Actual browser play verifies flight, visible successful landing, automatic next station, automatic failure retry, capped100% charge, manual restart during flight, persistent best score and390px pointer gameplay without horizontal overflow. Short Space press initiates flight. These retain practical functions, but raw A already supports the core loop and best score.

The candidate adds calculated directional failure advice. At70% the UI says the throw overshot; reducing to65% produces an actual successful landing. However, on station2, two actual23% throws also say “飞过头啦！下次温柔一点。” This is wrong: applying the delivered fixed-step flight equations to the displayed rounding interval's endpoints and midpoint places descending platform-height crossing at x410–418, before the minimum possible target x540. The fail handler instead compares the later fallen body's x with the target's left edge. The post-hoc diagnostic and actual screenshot are separate evidence; no evaluator repair is made.

Failure feedback resets after0.65seconds in the source; the first actual observation missed the message. Semantic waits subsequently captured it. A wait for the expected correct underthrow message timed out and remains recorded; a broader result wait revealed the wrong advice. A helpful-sounding feature is not a benefit when it recommends the wrong adjustment. The candidate's higher observed time/output is not justified merely by its larger feature list, nor does this one case establish general harm.

At this intermediate stage G had completed generation but browser acceptance was pending; its completed observations are now above. Physical mobile, held-input interruption, sound, direct-file entry and frame-rate variation remain unverified independently. Model self-test claims and failures are preserved separately.

## First actual product: raw A

A completes in178.66seconds with7172 output tokens. Independent CUA operations confirm charge/release, visible flight, actual success and failure, immediate retry, next-station continuation and a capped long hold. An800ms hold displays60% and misses; a650ms hold displays49% and lands on the cushion with score1; a2second hold caps at100% and misses. An additional ordinary-click attempt is preserved as a real0% failure, not silently omitted. Success screenshots show the person on the target, not only a score change.

At390x844, actual pointer play again succeeds at49%; document width equals390 without horizontal overflow. After reload, best1 remains while the current run resets. Space from a successful result advances to the next station. The delivered raw request already supplies progression, retry and a persistent best score; these cannot later be attributed exclusively to Skill.

Source inspection finds bounded elapsed-time updates and cancellation handlers; held-input interruption and frame-rate invariance have not been independently demonstrated. A resized desktop is not a physical touch-device test. Native file launch, sound and sustained keyboard charge remain untested. The temporary browser tab and server are closed and the viewport reset. No generated source was repaired during scoring.

The source inspiration is [Throwteammate](https://github.com/dawwnforu/Throwteammate), README at commit02508d213c32e3f95fda36af6b9db55cd7a2fa49, retrieved2026-10-15 through the public GitHub API. Its charge/release/cancellation mechanics motivate a new browser-game request. This is deliberately a separately stated browser task, not a conversion of a request to modify PEAK into an easier deliverable. No original conversation, gameplay audit, engine compatibility or multiplayer validation is claimed. The source implementation and README are withheld from generators.

Compare raw request, current Skill and a short generic instruction, one generation each with identical tools, permissions and model settings. The runtime snapshot includes adopted knowledge through7395bfb and excludes the unadopted R51 candidate. No new rule is introduced merely to make this trial win.

Acceptance requires actual charge/release flight, observable success/failure, quick retry and continued use, understandable controls and preserved useful supporting features. Inspect interruption, bounded charge, reset behavior and timing; test actual browser controls and narrow layout. A visible score or function named collision does not prove the game works. Static timing inspection and a resized desktop are not substitutes for frame-rate or physical-mobile testing.

Record practical additions without requiring every game to have an identical feature list. Preserve generated failures and do not repair products during scoring. This trial cannot establish stable token savings, general superiority, subjective enjoyment or a successful PEAK mod. No outcome is reported before the relevant checks run.
