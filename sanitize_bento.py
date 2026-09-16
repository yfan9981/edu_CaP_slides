import json
import re
from pathlib import Path

input_file = Path("slides/CaP_Original.bento.html")
output_file = Path("slides/CaP_AI_Working.bento.html")

html = input_file.read_text(encoding="utf-8")

pattern = re.compile(
    r'(<script\b[^>]*\bid=["\']bento-doc["\'][^>]*>)([\s\S]*?)(</script>)',
    re.IGNORECASE,
)

match = pattern.search(html)

if not match:
    raise RuntimeError("Could not find the bento-doc script element")

document_data = json.loads(match.group(2).strip())

print("Input had collab:", "collab" in document_data)
print(
    "Input had ownerPriv:",
    bool(document_data.get("collab", {}).get("ownerPriv")),
)

document_data.pop("collab", None)

clean_json = json.dumps(
    document_data,
    ensure_ascii=False,
    indent=2,
).replace("<", "\\u003c")

clean_html = (
    html[: match.start()]
    + match.group(1)
    + "\n"
    + clean_json
    + "\n"
    + match.group(3)
    + html[match.end() :]
)

output_file.write_text(clean_html, encoding="utf-8")

print("Output has collab:", "collab" in document_data)
print("Created:", output_file)