from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

manifest = json.loads(
    (ROOT / "plugin.json").read_text(encoding="utf-8")
)

# Validate basic plugin metadata
assert manifest.get("$schema") == (
    "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
)
assert re.fullmatch(
    r"[a-z0-9]+(?:-[a-z0-9]+)*",
    manifest.get("name", "")
)
assert re.fullmatch(
    r"\d+\.\d+\.\d+",
    manifest.get("version", "")
)
assert manifest.get("description", "").strip()

# Validate our two skill files
for slug in ("create-roadmap", "teach-roadmap"):
    path = ROOT / "skills" / slug / "SKILL.md"

    assert path.is_file(), f"Missing skill: {path}"

    content = path.read_text(encoding="utf-8")

    match = re.match(
        r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z",
        content,
        re.S
    )
    assert match, f"Invalid frontmatter: {path}"

    frontmatter, body = match.groups()

    name = re.search(
        r"(?m)^name:\s*(\S.*?)\s*$",
        frontmatter
    )
    description = re.search(
        r"(?m)^description:\s*(\S.*?)\s*$",
        frontmatter
    )

    assert name and name.group(1) == slug
    assert description and description.group(1).strip()
    assert body.strip(), f"Empty instructions: {path}"

    print(f"OK: {slug}")

print("OK: basic plugin checks passed")
