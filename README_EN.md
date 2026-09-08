<p align="center">
  <img src="skills/intent-compiler/assets/intent-compiler.svg" width="220" alt="Intent Compiler line-art avatar turning natural language into an executable task">
</p>

<h1 align="center">Intent Compiler</h1>

<p align="center"><strong>You speak naturally. The agent supplies the missing professional structure and gets the work done.</strong></p>

<p align="center"><a href="README.md">中文</a> · <a href="LICENSE">MIT License</a></p>

Intent Compiler is an Agent Skill for office workers, creators, students, and other non-technical users. Describe the outcome in ordinary language; the Skill reconstructs the intent, adds only the domain knowledge needed, chooses an execution path, checks the result, and delivers it.

## How it works

```text
Natural language → intent → relevant domain knowledge → internal brief → execution → repair → delivery
```

It does not merely return a longer prompt. It executes the task by default. It asks a question only when an answer would materially change the result, authorize an external effect, or cannot be inferred safely.

## Before and after

For the same request—prepare a three-minute AI customer-service pilot proposal for a budget-conscious manager—the baseline produced a useful five-page plan but introduced a fixed budget that the user had not supplied. Intent Compiler produced a tighter four-page decision brief, treated the missing budget as an explicit assumption, and added measurable continuation and stop conditions.

In this single directional test, the Skill output used about 3.6% fewer characters but 5.9% more total tokens. Its value is more consistent intent handling, not guaranteed token savings. See the [full comparison](examples/before-after.md).

## Install

### Codex

```bash
codex plugin marketplace add dawwnforu/intent-compiler-skill
codex plugin add intent-compiler@intent-compiler
```

Restart Codex after installation.

### Claude Code

```text
/plugin marketplace add dawwnforu/intent-compiler-skill
/plugin install intent-compiler@intent-compiler
```

### Skill only

Copy `skills/intent-compiler` into your agent's Skills directory. If you do not know where that is, ask your current AI agent to install the Skill from this GitHub repository.

## Use

Speak normally, or invoke it explicitly:

```text
$intent-compiler Turn these meeting notes into an action list.
$intent-compiler brief -- Structure this idea without executing it.
$intent-compiler teach -- Explain the missing UI concepts I should know.
$intent-compiler improve -- Improve this existing proposal.
```

Slash-command hosts may also expose `/intent-compiler`, `/intent-brief`, and `/intent-improve`.

## What is included

- Office, research, visual/design, 3D, product, and coding lenses
- A low-friction clarification policy
- A single-pass result quality loop
- Examples written for non-technical users
- Markdown-only maintenance guidance
- Codex and Claude Code plugin manifests
- An original SVG line-art identity

## Maintenance

Most updates only require editing Markdown. Add a real example, adjust one relevant rule, update `CHANGELOG.md`, and open a pull request. See [MAINTAINING.md](MAINTAINING.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

Licensed under the [MIT License](LICENSE).
