# R34: repair decorative motion without removing gameplay

Four actual runs completed on 2026-10-13, in order A/V2/G/V1, using gpt-6.1-sol/low and the same historical R2 V2 HTML. Candidate snapshot: `5e5fa2b`. This is an exposed repair, not an unseen generation task or human comfort rating. The reconstructed novice request likes the existing game but finds scrolling ground stripes uncomfortable despite enabling reduced motion; keep jumping, collision and immediate restart.

The [record](results/v2-game-motion.json) contains the complete prompt, runner, invocations, environment records, responses, HTML, counters and independent checks. Existing shared-runner Skill isolation and Python discovery apply equally.

## Actual findings

The original script still moves all 16 ground markers under reduced motion. The old canvas-presence check missed this. The independent [verifier](check_game_motion.cjs) executes unchanged scripts with a mocked DOM/canvas at deterministic 60 Hz and observes drawing calls. Its repair assertions reject the original and accept all four repairs.

Every repair makes the ground offset conditional and adds a system-preference listener. Non-script HTML/CSS is independently identical to the fixture. V1 omits the older listener fallback used by the others; no obsolete-browser requirement or score is inferred. No Skill rule was added.

Both preference modes retain input-triggered rise, moving obstacles, collision end and restart with zero score. Reduced mode keeps all 16 markers stationary; ordinary mode retains their scrolling. Coordinates/colors make this verifier specific to this fixture. Preference changes during play, subjective comfort, actual mobile touch and varied refresh rates are not independently verified.

| Arm | Output tokens | Seconds | Independent fixture checks |
|---|---:|---:|---|
| Raw A | 2,496 | 90.27 | Pass |
| Generic G | 1,839 | 90.94 | Pass |
| Release V1 | 1,784 | 68.31 | Pass |
| Candidate V2 | 2,245 | 105.00 | Pass |

No exclusive candidate quality gain. V2 is slower than all baselines and its output exceeds G/V1. One run cannot establish stable savings. Model-authored tests remain separate from independent checks.

## Boundaries and failed attempts

The in-app browser loaded V2 and start hid the overlay; a local screenshot shows the rendered game. Subsequent observations did not establish animation progression or collision/end, even after showing the browser. No console warnings/errors returned. The cause is unestablished; unit checks do not fill this browser gap. No browser reduced-motion emulation or device-experience claim is made.

The initial sandbox attempt ended with `queue.Empty` during Skill initialization, before generation; its directory is retained separately. All recovery runs completed. An inaccessible sandbox preview server and the approved loopback replacement were both stopped. Some PowerShell reads displayed garbled Chinese; saved UTF-8 non-script content is independently unchanged, but uniform model-side decoding is not claimed.

## Reproduce the independent check

From the repository, with existing Node and no dependencies:

```sh
node -e "const fs=require('node:fs');const r=JSON.parse(fs.readFileSync('tests/results/v2-game-motion.json','utf8'));fs.writeFileSync('motion-replay.html',r.runs.find(x=>x.arm==='V2').html)"
node tests/check_game_motion.cjs motion-replay.html --expect-fixed
```

Change the arm for another exact artifact. Extract `r.fixture` instead for the negative control: `--expect-fixed` must fail because the original ground scrolls. Omit the flag to inspect measurements without asserting a repair. Replaying the Node check does not reproduce model generation, which requires the host/account described in the record.
