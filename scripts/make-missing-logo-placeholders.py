#!/usr/bin/env python3
"""Create plain text placeholders for missing landscape logos, without overwriting logos.

Requires PyYAML. Replace placeholders with properly sourced SVGs when available.
"""

from pathlib import Path
from xml.sax.saxutils import escape

import yaml

ROOT = Path(__file__).resolve().parent.parent
LOGOS = ROOT / "hosted_logos"
SHARED_NAMES = {
    "amazonaws.svg": "AWS",
    "microsoft.svg": "Microsoft",
    "onnxruntime.svg": "ONNX Runtime",
}

data = yaml.safe_load((ROOT / "landscape.yml").read_text(encoding="utf-8"))
for category in data["landscape"]:
    for subcategory in category["subcategories"]:
        for item in subcategory["items"]:
            logo = LOGOS / item["logo"]
            if logo.exists():
                continue
            name = SHARED_NAMES.get(logo.name, item["name"])
            # These are neutral labels, not replicas of the organizations' trademarks.
            svg = (
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 80">\n'
                '  <rect x="1" y="1" width="298" height="78" rx="8" fill="#f4f8fb" stroke="#b8cedd"/>\n'
                '  <text x="150" y="50" text-anchor="middle" font-family="sans-serif" '
                'font-size="24" font-weight="600" fill="#143b57" '
                f'textLength="{min(260, len(name) * 15)}" lengthAdjust="spacingAndGlyphs">{escape(name)}</text>\n'
                '</svg>\n'
            )
            logo.write_text(svg, encoding="utf-8")
            print(f"Created placeholder: {logo.relative_to(ROOT)}")
