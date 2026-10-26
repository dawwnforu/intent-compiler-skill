# Historical game jump verification correction

Reviewed 2026-10-13. The original local `work/verify_v2_game.cjs` dispatched touch after starting, compared two screenshots, waited for the end overlay and restarted. Its `animation_frame_changed` check could pass because obstacles and backgrounds move, even if the player ignores touch. Its `reduced_motion_canvas_present` check only establishes canvas presence, not reduced decorative motion. Retain those observations without the stronger interpretation.

The original task requested a mobile ball-jumping obstacle game, tap to jump, collision ends the game, immediate restart, some bounce and speed without excessive visual disturbance. The follow-up executes each historical A/G/V1/V2 HTML's unchanged inline script in Node's VM. A minimal mocked DOM supplies the original registered event handlers, and a canvas spy observes the player's vertical translation. No script text or game state is rewritten. The files are the old R2 artifacts, not fresh outputs of the current Skill.

Start, advance 54 frames at 60 Hz so V2's automatic starting jump lands, invoke the registered pointer handler, and advance six frames. A separate fresh instance follows the same timeline but suppresses the pointer event. Deterministic randomness holds the environment fixed. This tests input-to-render-coordinate logic; it does not reproduce browser touch dispatch, layout, event bubbling or hit testing.

| Arm | Upward displacement after input (game coordinates) | Suppressed-input displacement |
|---|---:|---:|
| A | 49.22 | 0 |
| G | 55.25 | 0 |
| V1 | 52.93 | 0 |
| V2 | 55.25 | 0 |

All four pass the preselected checks: input causes more than 20 units of rise; suppressed input changes height by less than 2 units. Heights use different game coordinate systems and are not a quality ranking. The negative control would reject the old false inference that any animated frame proves a jump. There is no new Skill improvement or model-cost measurement.

Run from the repository with existing Node, without dependencies:

```sh
node tests/check_game_jump.cjs > game-jump-replay.json
```

The [test](check_game_jump.cjs) defaults to the complete HTML snapshots in the [record](results/v2-game-jump.json). Optionally supply the original `runs/r2/game` directory to compare local historical files. A nonzero exit rejects an assertion. Actual touch responsiveness on devices, reduced-motion behavior, varied refresh rates, background/resume behavior and broad accessibility are outside this new check. No historical browser result is overwritten, and no runtime Skill rule is added on the strength of this verification correction.
