"""Validate/update the latest-film pointer before a release commit."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pointer = json.loads((ROOT / "showcase/latest-film.json").read_text(encoding="utf-8"))
for key in ("preview", "render", "receipt"):
    path = ROOT / pointer[key]
    if not path.exists():
        raise SystemExit(f"missing latest asset: {path}")
print(json.dumps({"status": "valid", "id": pointer["id"], "assets": [pointer[k] for k in ("preview", "render", "receipt")]}, ensure_ascii=False))
