# R50: co-watching from a real project intent

Status: all three generations complete; all three independently checked through real HTTP and actual CUA browser operations. No new runtime rule adopted. [Exact runner, protocol and Skill snapshot](results/v2-cowatch.json).

## Final comparison

All three unchanged products load the90-second video, synchronize play/pause/seek between clients, advance late-join playback position, preserve room position on explicit rejoin, isolate another room and visibly report connection failure. Independent HTTP checks use each delivered API; actual browser operations inspect media time and paused state, not just labels. Original inputs are retained. Model-side browser failures, recovery commands and self-tests remain distinct from these evaluator checks.

| Arm | Output tokens | Seconds | Observed usability differences |
|---|---:|---:|---|
| Raw A | 10865 | 423.22 | Refresh returns to lobby; user re-enters code. Disconnect status changes while local playback continues. |
| Current Skill V2 | 9374 | 338.69 | Refresh automatically rejoins remembered room; browser may require a displayed autoplay unlock. Disconnect disables controls, but sidebar retains stale online-count text. |
| Generic G | 9448 | 363.52 | Refresh retains code in URL/input but requires clicking join. Disconnect pauses actual media and displays failure. |

V2 has a verified convenience difference in refresh recovery; core synchronization is not an exclusive gain. Its output/time are lower in this single trial, but differing model-side browser recovery work and one sample do not establish stable savings. V2's new-window button did not produce an observable new tab in IAB; that convenience is not counted as working. G's comparable button was not independently tested. File counts, screenshots and model self-test claims are not substituted for behavior.

V2's late join and post-refresh browser needed an explicit playback-unlock gesture. Before that click, time advanced via synchronization while `video.paused` remained true. Only readings after real playback began count: late pair32.798/32.260seconds, isolated-room check41.097/40.648 playing versus0 paused. Both reverse seek checks converge at0 and9 after2200ms; refresh eventually returns to9 without resetting the other client. Main disconnect status is accurate, but cached sidebar text still says two windows online/automatic synchronization: preserve this UI inconsistency rather than reporting flawless failure handling.

G actual playback pairs are7.759/7.749seconds, late join30.685/30.677, and isolated-room17.081/17.035 versus0 paused. Reverse pause/seek converge at0 and9 after2200ms. Reload leaves a prefilled code; clicking join restores9. After stopping its service the browser reports disconnection and actual media is paused. A's detailed evidence follows below.

All generated runs are terminal, independent servers are stopped and evaluator-created test tabs are closed. V2 was tested on its required8765 origin only after all generators ended and the port was free; A/G handlers used separate loopback ports. No generated sources were repaired. Native launcher double-click, physical other-device tests, service-restart persistence, third-party video and public hosting remain unverified. This bounded local project slice does not prove the full source project works or that Skill generally understands intent better. No new Skill paragraph is justified by this comparison alone.

Earlier pending statements below are retained as chronology, not current status.

The novice request is reconstructed from [cloud-itting](https://github.com/dawwnforu/cloud-itting), not recovered from its original chat. On 2026-10-15 the public GitHub API resolved master to `02d89b05a13cf32f6ed2e125e4fec33c325ea0c5`. Read scope: README, server socket handler and client socket hook. They establish room-based play/pause/seek intent and an actual client/server implementation; no source-repository runtime or full audit is claimed. The generators do not receive that implementation.

Compare raw, current Skill and short generic instruction in that order, each once with gpt-6.1-sol low. All receive the same locally generated90-second MP4 and source-preservation/offline/no-install/no-publication boundary. The request asks for two local browser windows before later remote use; voice, accounts, playlist and third-party video access are outside this particular trial, not declared solved or removed from the full project.

Frozen acceptance covers a real local entry and video, independent clients, bidirectional play/pause/seek, late joining during playback, reload/rejoin, separate-room isolation, visible connection failure and truthful remote-delivery limitations. Compare media positions within2seconds after settling2seconds; account for required initial autoplay gestures. Browser shared storage alone is not a server test. Record actual browser and direct protocol checks separately. Preserve failed outputs without repairing them during scoring.

This is a new practical P04-derived workflow, not evidence of general intent recognition, stable token savings or human preference. Runtime Skill is unchanged before these comparisons.

## First independent result: raw A

A completed in423.22seconds. Its unchanged Python server passes real HTTP checks with separate member credentials: bidirectional control, another-room isolation, elapsed position for late joining, new-session rejoin without reset and actual MP4 range bytes. This is protocol evidence, not browser playback.

Actual CUA browser operations then verify video decoding, two simultaneous players (11.648/11.574seconds), reverse pause and seek (both paused at0, then9 after2200ms), late join (24.696/24.696), refresh followed by explicit room-code rejoin at9, and independent room isolation (17.100/17.007 playing versus0 paused). Stopping the independent server displays a Chinese connection-interrupted/retry message plus raw `Failed to fetch`; local media continues but the UI does not falsely say connected. No generated source was repaired.

The first evaluator server launched inside the sandbox could not be reached across processes; it was stopped, then the same Handler was started with parent execution permission and worked. An early combined seek/play interaction overwrote the seek before polling settled; it was not scored as a settled seek. The later isolated actions follow the frozen2200ms wait. These evaluator details remain separate from the model's earlier browser decode failures and its final self-test claims.

The independent server and three test tabs are closed. Native launcher double-click, physical devices, automatic recovery of expired sessions and internet delivery remain untested. V2 generation has finished but is not yet independently evaluated; G is still running. No comparison winner is claimed.
