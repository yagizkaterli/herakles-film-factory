"""Build the 100-iteration execution ledger without inventing visual scores."""
from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "canonical" / "iteration-100-imagegen-to-3d.v1.json"
MANIFEST = ROOT / "iterations" / "w1" / "W1-MANIFEST.json"
OUT = ROOT / "iterations" / "EXECUTION-LEDGER.json"


def main() -> None:
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    waves = spec["iterations"]["waves"]
    entries = []
    for wave in waves:
        start, end = (int(x) for x in wave["range"].split("-"))
        for number in range(start, end + 1):
            item = next((x for x in manifest.get("iterations", []) if x["id"] == f"I{number:02d}"), None)
            entries.append({
                "id": f"I{number:02d}",
                "wave": wave["id"],
                "focus": wave["focus"],
                "source_pointer": item.get("source_pointer") if item else None,
                "question": item.get("question") if item else None,
                "status": "pending",
                "score": None,
                "decision": "pending",
                "falsifier": "missing source-bound visual review or deterministic receipt",
            })
    OUT.write_text(json.dumps({
        "schema": "herakles.iteration-execution-ledger.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(entries),
        "completed": 0,
        "pending": len(entries),
        "truth_boundary": "No score is assigned until a source-bound visual review and receipt exist.",
        "waves": waves,
        "iterations": entries,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
