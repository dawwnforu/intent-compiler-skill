# Installation and compatibility / 安装与兼容性

2026-10-24 continuation update: [R93–R94](tests/v2-agensi-continuation.md) preserves a test-client disk-resume failure, then verifies one actual interruption and continuation on the same still-loaded ephemeral Codex thread. The final client ZIP/internal table agree, retain user-update provenance and pass independent extraction/privacy/browser checks. Exact full MIT, SVG and optional script contents are retrievable; script execution is untested. This is not process-restart recovery, a fresh initial-delivery pass or a test of the unpublished encoding guidance. Earlier evidence below retains its own version/status.

2026-10-24 Agensi update: the af3d2c8 product is live/approved, anonymously visible and searchable. [R92](tests/v2-agensi-delivery.md) verifies actual core/reference calls, exact source/reference text and local business files through Codex. The first Chinese delivery failed; one developer-guided encoding repair then passed independent byte, extraction, privacy and browser checks. This is assisted delivery, not automatic success or a reduced-prompt claim. Continued-session updates, optional-script channel execution, native Explorer extraction/offline double-click and other-host business use remain unverified. Platform listing1.0 and source manifest0.2.0 are distinct; the new encoding guidance is on this branch, not in the published ZIP.

2026-10-24 package update: [R82](tests/v2-resource-paths.md) verifies the new af3d2c8 archive's extraction and installed optional checker. No fresh host discovery or model business run was performed for that archive. [R80](tests/v2-submission-candidate.md#r80-distinguish-the-project-candidate-from-a-same-name-release) startup and the business evidence below retain their original versions; static/tool success is not a new compatibility pass. Agensi delivery and non-Codex business compatibility remain unverified.

Latest trial evidence: 2026-10-19, [detailed host matrix](pilot/compatibility.md) and [R71 actual continuous business checks](tests/v2-continuous-pilot.md). Codex project-local ZIP installation/discovery, explicit project-file selection alongside a same-name user copy, actual generation and one bounded six-turn resumed task are verified. Claude discovery succeeds but inherited third-party routing/remote authentication blocks business verification. Cursor/Copilot and Agensi delivery remain unverified. No desktop/global plugin installation, all-mode or general resumed-task compatibility claim. The instructions below retain their original2026-09-29 date; current evidence supersedes older status notes. A PR-branch trial ZIP is not a Release or public plugin-directory admission.

## Codex

The existing `.codex-plugin/plugin.json` compatibility manifest points to `./skills/`; `.agents/plugins/marketplace.json` supplies this repository's marketplace entry. The [official packaging documentation](https://developers.openai.com/plugins/build/plugins) still describes this compatibility format. We retain it rather than introducing a second portable manifest.

Local `codex-cli 0.158.0-alpha.2.1` help confirms:

```bash
codex plugin marketplace add dawwnforu/intent-compiler-skill
codex plugin add intent-compiler@intent-compiler
```

For a PR preview, use the CLI's documented `--ref BRANCH` marketplace option and ensure the marketplace plugin source also selects that branch in a local test copy. Normal installation tracks main, so an unmerged PR is not installed by the commands above.

Alternatively, copy the **whole** `skills/intent-compiler` folder to `.agents/skills/intent-compiler` in a project, or `~/.agents/skills/intent-compiler` for the user, as described in the [official local skills guide](https://learn.chatgpt.com/docs/build-skills). Do not copy SKILL.md alone or install duplicate copies by both methods.

In a fresh session, confirm discovery and invoke `$intent-compiler brief -- Describe launch prerequisites without deploying`. Explicit name display can vary with plugin namespacing; use the host's skill selector if needed. Automatic selection remains model-dependent.

**Historical evidence:** CLI help and static checks. **Current evidence:** Codex CLI 0.163.0-alpha.10.2, actual project-local ZIP installation/discovery and bounded business generation; marketplace plugin installation and GUI compatibility still untested. See the matrix above.

## Claude Code

The [official marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces) requires `.claude-plugin/marketplace.json`. It is now included, with the repository root as plugin source. The [manifest reference](https://code.claude.com/docs/en/plugins-reference) describes Markdown command files; old TOML wrappers were replaced.

```text
/plugin marketplace add dawwnforu/intent-compiler-skill
/plugin install intent-compiler@intent-compiler
```

In a fresh session, check the installed plugin and use its namespaced skill:

```text
/intent-compiler:intent-compiler brief -- Describe launch prerequisites only
```

The core Skill supplies that entrypoint; no duplicate same-name command is packaged. Markdown wrappers provide `/intent-compiler:intent-brief`, `/intent-compiler:intent-teach` and `/intent-compiler:intent-improve`. Discovery must be smoke-tested on the target host; natural-language modes in the core remain sufficient if a wrapper is not exposed.

**Current evidence:** Claude Code 2.1.201 project-local copy and initialized Skill/slash entry observed; business request failed with 401. The requested sonnet alias resolved to a different locally configured model, so no Anthropic-model success is claimed. Marketplace plugin dispatch, four modes and business compatibility remain unverified. See the matrix above.

## Other hosts and limitations

### Historical candidate evidence / 历史候选证据（2026-10-15）

| Evidence layer / 层级 | What is established / 已知范围 | Remaining limit / 限制 |
|---|---|---|
| Static checks / 静态检查 | Repository link, manifest, attribution and license-copy checks | Does not install or discover a Skill / 不验证安装发现 |
| Actual installation / 实际安装 | No installation or replacement performed in this change | Current candidate installation on Codex/Claude remains unverified / 当前候选安装未验证 |
| Skill discovery / Skill 发现 | No fresh-session discovery test performed in this change | Existing session catalog or legal YAML cannot prove candidate discovery / 不能由现有目录或格式推断 |
| Behavior / 行为测试 | Frozen snapshots and actual generated-product checks are recorded separately in TESTING.md, including R57 and the current-core R58 local handover | R58 is one bounded explicit-user-boundary case, not causal benefit or general protection; Claude compatibility unverified / R58 是单一明确边界案例，不证明因果收益或普遍防护；Claude 兼容性未验证 |

Keep the standalone folder's README and LICENSE when copying it. Source and copyright information live there. The candidate label uses the existing supported `interface.display_name`; Skill name, description and discovery paths are unchanged. / 复制时保留README和LICENSE，用于来源与署名；候选名称使用已有宿主字段，不新增配置字段或改变Skill名称、描述与发现路径。同名版本须核对实际路径，不能假定自动替代。

Other Agent Skills hosts: copy only using that host's documented installation route, verify discovery, then run the fast-path and blocked-input cases. Compatibility is untested; `commands/*.md` are not universal commands. A chat that cannot read local references needs those files made accessible; pasting the entrypoint alone loses the knowledge modules.

The package supplies instructions and an optional read-only HTML script check, with no bundled search, renderer, font files, hosting account or permission manager. The check uses an existing Python standard library; Python is not required for other Skill work and should not be installed just for this check. Tools and credentials come from the host/user. Source access or execution may be unavailable even when the Skill loads successfully. A markup check does not establish browser compatibility or working interaction.

## 中文说明

- 核验日期：2026-09-29；官方说明、静态清单检查、完整安装和模型行为是不同层级的证据。
- Codex 的命令语法已在本地帮助中核对；Claude 的 marketplace 与 Markdown 命令格式已核对官方资料。
- 最新逐项结果见上方试用矩阵：Codex项目内安装、发现、明确项目文件选用和六轮恢复业务有实测；Claude发现后受继承的第三方路由/远端认证阻塞。完整插件安装、四模式和一般任务恢复仍未验证，不能因为 JSON 合法就宣布兼容。
- 主分支安装不会自动得到尚未合并的 PR；测试修改时使用本地副本或明确的测试分支。
- 安装整个 Skill 文件夹；安装不会提供建模、部署等工具、账号或授权。其他宿主未验证。
