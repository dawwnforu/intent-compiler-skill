"""Read-only script markup/resource checks for standalone UTF-8 HTML.

Not a browser, JavaScript evaluator or complete HTML validator.
"""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote, urlsplit


class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.open_script = None
        self.sources = []
        self.has_base = False

    def handle_starttag(self, tag, attrs):
        if tag == "base" and dict(attrs).get("href") is not None:
            self.has_base = True
        if tag == "script":
            self.open_script = self.getpos()[0]
            source = dict(attrs).get("src")
            if source is not None:
                self.sources.append((self.getpos()[0], source))

    def handle_endtag(self, tag):
        if tag == "script":
            self.open_script = None

    def handle_startendtag(self, tag, attrs):
        # HTML script elements cannot be closed with XML's /> syntax.
        if tag == "script":
            self.handle_starttag(tag, attrs)
            self.set_cdata_mode(tag)


def check(path):
    path = Path(path)
    parser = Scripts()
    parser.feed(path.read_text(encoding="utf-8-sig"))
    parser.close()
    errors, skipped = [], []
    if parser.open_script is not None:
        errors.append({"line": parser.open_script, "error": "Script element has no closing </script>; later page markup may be swallowed."})
    for line, source in parser.sources:
        url = urlsplit(source)
        resource = unquote(url.path)
        # Decoding can turn an apparent relative URL into a Windows drive or UNC path.
        if (parser.has_base or url.scheme or url.netloc
                or resource.startswith(("/", "\\")) or PureWindowsPath(resource).drive):
            skipped.append({"line": line, "src": source, "reason": "Base URL, remote or rooted/drive resource requires the actual serving environment."})
        elif not resource or not (path.parent / resource).is_file():
            errors.append({"line": line, "src": source, "error": "Local script file is missing or source is empty."})
    return {"file": str(path), "passed": not errors, "errors": errors,
            "skipped": skipped, "limits": "Script markup and relative file existence only. JavaScript startup, browser rendering and interactions are NOT tested."}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("html", type=Path)
    args = cli.parse_args()
    try:
        result = check(args.html)
    except (OSError, UnicodeError, ValueError) as exc:
        result = {"file": str(args.html), "passed": False, "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
