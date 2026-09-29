# Installation and compatibility / 安装与兼容性

Checked on 2026-09-29. This is an evidence record, not a permanent compatibility guarantee. Recheck the linked official instructions when host behavior changes. GitHub publication does not mean admission to a public plugin directory.

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

**Evidence:** CLI version and subcommand help inspected; manifest/path checks run locally. **Not tested:** complete plugin installation/discovery in a fresh host session or model behavior.

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

**Evidence:** official docs inspected, JSON/path checks run. **Not tested:** Claude installation, command dispatch or behavioral compatibility. Before claiming support for a release, run `claude plugin validate .`, install a local checkout, and verify all four modes.

## Other hosts and limitations

Other Agent Skills hosts: copy only using that host's documented installation route, verify discovery, then run the fast-path and blocked-input cases. Compatibility is untested; `commands/*.md` are not universal commands. A chat that cannot read local references needs those files made accessible; pasting the entrypoint alone loses the knowledge modules.

The package supplies instructions only, with no bundled search, renderer, font files, hosting account or permission manager. Tools and credentials come from the host/user. Source access or execution may be unavailable even when the Skill loads successfully.

## 中文说明

- 核验日期：2026-09-29；官方说明、静态清单检查、完整安装和模型行为是不同层级的证据。
- Codex 的命令语法已在本地帮助中核对；Claude 的 marketplace 与 Markdown 命令格式已核对官方资料。
- 两个宿主的完整安装、发现和模式调用均未实测。请在新会话按上面的命令验证，不能因为 JSON 合法就宣布兼容。
- 主分支安装不会自动得到尚未合并的 PR；测试修改时使用本地副本或明确的测试分支。
- 安装整个 Skill 文件夹；安装不会提供建模、部署等工具、账号或授权。其他宿主未验证。
