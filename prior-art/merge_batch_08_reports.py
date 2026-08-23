from __future__ import annotations

import json
import sys
from pathlib import Path


def decode_report(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    start = text.find("\n{")
    if start < 0:
        return None
    try:
        return json.JSONDecoder().raw_decode(text[start + 1 :])[0]
    except json.JSONDecodeError:
        return None


def main() -> None:
    src = Path(sys.argv[1])
    out = Path(sys.argv[2])
    entries = []
    reports = 0
    for path in sorted(src.glob("d-PRIOR-ART-09-*.md.rapor.md")):
        report = decode_report(path)
        if not report:
            continue
        reports += 1
        evidence = report.get("entries", report.get("kanit", ""))
        if isinstance(evidence, str):
            try:
                evidence = json.loads(evidence)
            except json.JSONDecodeError:
                continue
        if isinstance(evidence, list):
            source_entries = evidence
        else:
            source_entries = (evidence or {}).get("entries", [])
        for item in source_entries:
            item = dict(item)
            item["report"] = path.name
            entries.append(item)
    unique = {}
    for item in entries:
        key = item.get("source_url") or item.get("title")
        if key and key not in unique:
            unique[key] = item
    out.write_text(json.dumps({
        "schema": "herakles.prior-art-batch-08-merged.v1",
        "reports_scanned": reports,
        "entries_seen": len(entries),
        "unique_entries": len(unique),
        "entries": list(unique.values()),
        "fake_evidence": False,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
