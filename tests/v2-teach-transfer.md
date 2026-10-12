# R18: explain a novice's real shared-registration goal

Six completed turns, three actual resumed conversations: raw A, short generic G, and current candidate V2. Candidate snapshot is `542041d`; instructions are unchanged from R15. Fixed run order G/V2/A, gpt-6.1-sol low, browsing/network disabled, 300-second per-turn limit. Skill discovery checks isolated the candidate from baselines and actual resume IDs matched. [Full prompts, responses, commands and counters](results/v2-teach-transfer.json).

The first request describes a club registration page that works on the user's computer and survives refresh. The user asks to understand what is missing before implementation. The fixed second message reveals localhost/localStorage, real members using separate phones, a shared organizer list, own-record visibility, no deployment account/budget and no publication. This tests natural-language teaching intent without requiring the literal `teach` command. It does not test command-wrapper dispatch.

## Observations

All three first responses correctly avoid inferring shared storage from reload persistence. They explain reachable URLs, common storage and organizer access in ordinary language, ask for observable facts rather than architecture, and leave implementation untouched. All three second responses preserve real multi-phone use, explain server-enforced access rather than hidden buttons, distinguish phone-number entry from identity proof, avoid provider/free-service promises, and propose independent-client and unauthorized-read checks.

Candidate adds a useful conditional distinction: whether a member must recover a submission after changing phones or clearing the browser. It recommends recovery but does not treat it as already confirmed. A/G more directly assume a recoverable login flow. Conversely, A uniquely warns that existing local registrations do not automatically migrate into the shared system. This is a conditional warning, not a claim that real existing records are known to exist. There is no overall candidate correctness win.

Candidate mentions export as a possible organizer action even though not requested; it also retains internal-Skill attribution. A/G also raise optional export, and G recommends temporarily retaining the current page as a demo before real implementation. None actually substitutes a demo for the stated real-use objective. These details matter more than scoring a checklist of domain words.

| Arm | Turn 1 seconds / output counter | Turn 2 seconds / output counter |
|---|---:|---:|
| A | 34.69 / 875 | 37.08 / 1737 |
| G | 32.58 / 670 | 37.81 / 1476 |
| V2 | 54.55 / 1113 | 47.19 / 2169 |

Resume counters may be cumulative; do not add them as verified incremental cost. Candidate is longer/slower in these observed turns, with additional module reads. No stable savings follow from a single conversation per arm. Actual first-turn candidate reads cover index, clarification, sources, web runtime and deployment; there are no subsequent tool commands. Baselines use no commands. All workspaces have no generated products. Initial index/policy reads omitted explicit UTF-8, so bilingual index text was garbled; English rules remained readable.

## Decision and reproduction

No Skill modification. This supplies a completed narrow teaching-mode transfer and records mixed relative strengths. To reproduce, use the exact two messages and boundary in the JSON, fresh isolated workspaces, the recorded candidate snapshot, no Skill for A/G, and only the recorded generic prefix for G. Send the second message through actual resume after turn 1; never replace failed runs or silently adapt the second message to favor an arm. Preserve all responses, loaded Skill paths, command events and counters.

Limits: nonblind development review, fixed supplemental answer rather than a human interview, one conversation per arm, no release arm, no live backend or access-control test, no measured comprehension/satisfaction. The explicit no-code boundary helps all arms avoid implementation. Teaching explanations are verified here; deployment, actual security and all mode/command variations remain unverified. The existing product's code was not supplied, so the described conditions are user-provided facts rather than discovered runtime evidence.
