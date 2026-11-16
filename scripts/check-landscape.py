#!/usr/bin/env python3
"""Check input logos and the generated landscape's item logo references."""

import argparse
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parent.parent
LOGOS = ROOT / "hosted_logos"
parser = argparse.ArgumentParser()
parser.add_argument("--built-dir", type=Path)
args = parser.parse_args()

data = yaml.safe_load((ROOT / "landscape.yml").read_text(encoding="utf-8"))
items = [
    item
    for category in data["landscape"]
    for subcategory in category["subcategories"]
    for item in subcategory["items"]
]
errors = []
for item in items:
    name = item["name"]
    logo = item["logo"]
    if Path(logo).name != logo or not logo.endswith(".svg"):
        errors.append(f"{name}: logo must be an SVG filename relative to hosted_logos: {logo}")
        continue
    try:
        root = ET.parse(LOGOS / logo).getroot()
        if root.tag != "{http://www.w3.org/2000/svg}svg":
            errors.append(f"{name}: {logo} is not an SVG")
    except (OSError, ET.ParseError) as exc:
        errors.append(f"{name}: cannot read {logo}: {exc}")

if args.built_dir:
    html = (args.built_dir / "index.html").read_text(encoding="utf-8")
    match = re.search(r"window\.baseDS\s*=\s*(\{.*?\});", html)
    if not match:
        errors.append("Generated index.html does not contain landscape item data")
    else:
        built_items = json.loads(match.group(1))["items"]
        if len(built_items) != len(items):
            errors.append(f"Generated {len(built_items)} items; expected {len(items)}")
        for item in built_items:
            logo = item.get("logo", "")
            path = (args.built_dir / logo).resolve()
            if not logo or not path.is_relative_to(args.built_dir.resolve()) or not path.is_file():
                errors.append(f"{item['name']}: generated logo is missing: {logo!r}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Verified {len(items)} landscape items and their {'generated ' if args.built_dir else ''}logos.")
