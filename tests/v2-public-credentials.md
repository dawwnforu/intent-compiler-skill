# R31: conditional credential rule — not adopted

Four completed candidate-before/after runs on the exposed R30 synthetic repair and a simple button-copy control. Base `966c50a`; gpt-6.1-sol/low; isolated Skills; offline local execution. The proposed paragraph asks for server ownership checks and inspection of public client assets for reusable authority-bearing credentials, only when access boundaries matter. [Exact rule, prompts, generated files, responses, commands and checks](results/v2-public-credentials.json).

Both arms receive the existing Python interpreter directory on PATH, fixing the R30 command-discovery obstacle equally. This environment change prevents direct causal comparison with R30. No installed dependency or user setting changed.

| Task | Before seconds / output counter | After seconds / output counter |
|---|---:|---:|
| Access repair | 155.26 / 3954 | 185.31 / 6147 |
| Button copy | 24.79 / 414 | 32.66 / 409 |

Both repairs pass the same 11 independent HTTP checks and remove the known credential from delivered HTML. Full server/client inspection confirms both use an authenticated session-role response to show the organizer button instead of embedding its credential. Actual browser operations verify Alice sees only her record, the organizer sees both records, switching to Bob clears the prior list and hides the organizer button, and Bob sees only his record. The two temporary verification servers were stopped afterward. No delayed-response race stress test, full security audit, real identity verification or production deployment was performed.

Both copy controls change only the requested button text. Independent byte comparison verifies the exact replacement and no additional product files; the public promotion code remains intact. Skill isolation paths were checked. The proposed rule exists only in experimental snapshots; repository and installed Skill remain unchanged.

**Decision: do not adopt the paragraph.** The new baseline already repairs the observed exposure, so no exclusive gain is demonstrated. After uses more output and time for repair. One pair does not establish reliable equivalence or causal inefficiency. Keep R30's failures rather than overwriting them; the reason for the improved baseline remains uncertain.

The supporting source is [OWASP Web Frontend Security](https://cheatsheetseries.owasp.org/cheatsheets/Web_Frontend_Security_Cheat_Sheet.html), sections on client-side security logic, client-visible secrets and direct service calls, read on 2026-10-13. These principles support the test rationale; they do not prove the Skill's effect or certify the repaired app. No paper algorithm was implemented in this round.
