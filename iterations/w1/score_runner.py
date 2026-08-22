"""Create a truthful W1 score envelope; human/image review fills scores later."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "W1-MANIFEST.json"
OUT = HERE / "top-10-contact-sheet.json"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    candidates = []
    for item in manifest["iterations"]:
        candidates.append({
            "id": item["id"],
            "question": item["question"],
            "source_pointer": item["source_pointer"],
            "scores": None,
            "total": None,
            "decision": "pending_review",
            "falsifier": "source-bound image review plus render receipt absent",
        })
    OUT.write_text(json.dumps({
        "schema": "herakles.w1-score-envelope.v1",
        "status": "pending_review",
        "candidate_count": len(candidates),
        "top10": [],
        "candidates": candidates,
        "rule": "Never promote without six scores, source parity, falsifier, and receipt.",
        "fake_evidence": False,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
