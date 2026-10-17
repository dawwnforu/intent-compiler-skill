# R13: font resources absent, text-only C3

This executes C3's missing-resource condition separately from R11's real-font artifact test. The original request is unchanged. The fixture explicitly supplies only a description of the editor, no code/assets/licenses, and fictional Demo Sans/Serif names. All conditions receive the same no-browsing, no-file/code-generation boundary. Thus this tests judgment and honest next steps, not editing or rendering.

Fixed order G/V2/A/V1, one fresh gpt-6.1-sol low-reasoning session each. V2 is commit `0ee5b23765a2ad6c6b69e867dcd93ee032504080`; V1 is the installed0.2.0 snapshot. Web search and workspace network are disabled. Actual enabled-Skill paths were checked before each run; baseline arms have no enabled Skill. No within-batch changes or replacement runs. [Exact inputs, every response, commands and counters](results/v2-font-gap.json).

| Arm | Seconds | Output tokens | Observed approach |
|---|---:|---:|---|
| A, raw | 19.41 | 288 | Suggest system families as an explicit limited alternative; remove fictitious fonts; fixed fonts need files and applicable license evidence |
| G, generic | 14.97 | 283 | Suggest system families, acknowledge device differences and absent files/rights; gives basic switching checks |
| V1, release | 34.17 | 537 | Keep requested real-resource path, identify files/source/embedding evidence, glyphs/weights, load failure and keyboard checks |
| V2, candidate | 31.47 | 572 | Similar complete prerequisite path; additionally explains that browser resource loading differs from a user download feature |

All four completed, produced no files/code, invented no resources or verified licenses, and explicitly did not claim implementation/runtime success. A/G's system-family proposal is a legitimate fallback, not automatically a failure. A explicitly leaves the real library incomplete; G describes its limited system approach and does not claim implementation. V1/V2 more fully describe actual-font verification and failure behavior; this benefit is shared with the release, not unique to2.0. Candidate wording distinguishes a resource request from the excluded download feature, but the other arms did not add a forbidden download feature either.

V2 read the index, source policy, clarification policy and font module. V1 read the index, font, source and quality references. A/G used no tools. Inspection of all completed command records shows only Skill reads, and workspace enumeration shows no generated artifacts. The candidate's extra clarification read had no demonstrated necessity in this case; do not infer efficient routing merely from the presence of an index.

No stable efficiency gain: candidate output was higher than every comparator and it used more input than the release in this single trial. Time differences and cached input are not causal savings evidence. Keep current instructions unchanged: adding another rule is not supported by a correctness failure here. No actual font loading, current license verification, human preference or cross-model conclusion follows. All four processes are terminal.

To reproduce, give only the recorded request, fixture and boundary to fresh sessions with the four recorded instruction conditions, equal model/tool settings and isolated workspaces. Check actual Skill discovery and tool records; review full responses for unsupported completion/resource claims, purpose-preserving alternatives and useful missing conditions. Never supply the expected outcomes as instructions to the tested model.
