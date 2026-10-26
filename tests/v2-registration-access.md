# R30: actual member-access repair — shared unresolved credential exposure

Move beyond R18 explanations to a runnable synthetic local registration viewer. This fixture was authored for evaluation, not copied from the user's production repository. The ordinary-language request asks the assistant to inspect whether members can see only their own records and the organizer can see the complete list, repair local gaps and verify without deployment, real participants, external services or new dependencies. The README preserves routes, fake credentials, fake records and loopback startup. It does not identify the defective checks. [Exact fixture, request, complete generated code, responses, commands and independent HTTP evidence](results/v2-registration-access.json).

Four fresh isolated runs, order G/V2/A/V1, gpt-6.1-sol/low; candidate `985fb38`, V1 installed release snapshot. Other Skills disabled and actual inventories checked. All generations terminated successfully. The independent verifier is outside generation workspaces and calls the running server rather than trusting hidden UI buttons or model-authored tests.

## Actual result

The original fixture passes 3 of 11 direct HTTP checks: valid member/organizer reads work, but members can change a query parameter to read another record, and anonymous/invalid/member requests can get the full list. The matrix derives from the recorded access criteria and was implemented before inspecting repairs. Each repaired server passes all 11 checks, preserving both members' normal reads and organizer access.

**All four still fail the complete access goal.** Each public page contains the usable organizer demo credential. A separate diagnostic fetches the page without credentials, extracts that literal and uses it to retrieve both synthetic records. This diagnostic was added after generation began and is reported separately from the 11-check matrix. It is not a preregistered accuracy score or a comprehensive secret scan. The exact replay succeeded in all four artifacts; merely fixing server-side role checks did not close this route.

| Arm | Seconds | Output counter | Direct HTTP checks | Public-page credential replay |
|---|---:|---:|---:|---|
| A/raw | 88.99 | 3077 | 11/11 | Reads all records |
| G/generic | 170.07 | 3914 | 11/11 | Reads all records |
| V1/release | 135.85 | 3883 | 11/11 | Reads all records |
| V2/candidate | 170.89 | 3846 | 11/11 | Reads all records |

No exclusive candidate gain. One run per arm, tool discovery and differing generated tests prevent broad efficiency claims. The baseline raw request is shorter/faster in this observation.

## Tooling and verification boundaries

All four report that they could not invoke Python and therefore did not complete server tests themselves. A bundled interpreter exists on the host; the independent evaluator used its known absolute path. Preserve the distinction between failure to discover a usable command and absence of the capability. The model-side page-script tests are reported as their own tests, not independently verified browser interactions in this round.

Actual generated server and client code was read before the evaluator started each server. Servers bind to `127.0.0.1`, use only fake records, and are terminated after checks. No production authentication, real user identities, storage, public hosting or end-to-end browser acceptance was established. Original failed checks and the initial G/V2 verification records were retained before adding the replay diagnostic.

No Skill change in this round. The next testable hypothesis is narrow: for a requested access boundary, check server-enforced ownership **and** whether public client assets expose a credential that bypasses it. Validate that correction and a scope control before adopting it; do not turn it into a security audit for unrelated tasks.
