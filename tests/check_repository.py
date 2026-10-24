"""Offline package integrity checks; deliberately not a model-behavior evaluator."""

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/intent-compiler"


def local_target(base, value):
    target = (base / unquote(urlsplit(value).path)).resolve()
    assert target.is_relative_to(ROOT), f"Path leaves repository: {value}"
    assert target.exists(), f"Missing local target: {base} -> {value}"
    return target


def check():
    count = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        assert "\ufffd" not in text, f"Replacement character in {path}"
        # ponytail: inline repository links only; use a Markdown parser if reference-style links are introduced.
        links = re.findall(r"!?\[[^\]]*\]\(([^)\s]+)\)", text)
        links += re.findall(r'<img[^>]+src="([^"]+)"', text)
        for link in links:
            if not urlsplit(link).scheme and not link.startswith("#"):
                local_target(path.parent, link)
                count += 1

    manifests = [
        json.loads((ROOT / host / "plugin.json").read_text(encoding="utf-8"))
        for host in (".codex-plugin", ".claude-plugin")
    ]
    assert len({item["version"] for item in manifests}) == 1, "Manifest versions differ"
    assert (SKILL / "LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes(), "Standalone license differs"
    for path in (ROOT / "README.md", ROOT / "README_EN.md", SKILL / "README.md"):
        notice = path.read_text(encoding="utf-8")
        for value in (manifests[0]["version"], manifests[0]["author"]["name"], manifests[0]["repository"]):
            assert value in notice, f"Missing source/version attribution in {path}"
    for item in manifests:
        assert item["name"] == "intent-compiler"
        skill_dir = local_target(ROOT, item["skills"])
        assert (skill_dir / "intent-compiler/SKILL.md").is_file()
    for key in ("composerIcon", "logo"):
        local_target(ROOT, manifests[0]["interface"][key])

    for name in (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"):
        data = json.loads((ROOT / name).read_text(encoding="utf-8"))
        assert data["name"] == "intent-compiler"
        assert [p["name"] for p in data["plugins"]] == ["intent-compiler"]
    claude_market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    local_target(ROOT, claude_market["plugins"][0]["source"])

    metadata = (SKILL / "agents/openai.yaml").read_text(encoding="utf-8")
    for value in re.findall(r'icon_(?:small|large):\s*"([^"]+)"', metadata):
        local_target(SKILL, value)
    assert "$intent-compiler" in metadata

    entrypoint = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert entrypoint.startswith("---\nname: intent-compiler\n")
    assert "\ndescription: " in entrypoint.split("\n---\n", 1)[0]
    for name in ("intent-brief", "intent-teach", "intent-improve"):
        text = (ROOT / "commands" / f"{name}.md").read_text(encoding="utf-8")
        assert text.startswith("---\n") and "$ARGUMENTS" in text
    assert not list((ROOT / "commands").glob("*.toml")), "Unsupported command wrapper"
    cases = (ROOT / "examples/validation-cases.md").read_text(encoding="utf-8")
    assert re.findall(r"^## (C\d+) —", cases, re.M) == [f"C{i}" for i in range(1, 7)]
    assert len(re.findall(r"\*\*Model status:\*\*", cases)) == 6
    assert f'## {manifests[0]["version"]} -' in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    print(f"PASS: {count} local links; manifests, package assets, commands and six case records")
    print("Model behavior and host installation: NOT TESTED by this check")


if __name__ == "__main__":
    check()
