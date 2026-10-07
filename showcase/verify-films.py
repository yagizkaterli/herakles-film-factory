"""Re-derive the digests a film receipt claims, so a stranger can check the showcase.

Checks per film-index entry:
  1. every listed asset (render/preview/poster/receipt) exists;
  2. every digest the receipt records is re-hashed from the file on disk
     (media digests and the receipt.sources[] list);
  3. receipt.source_digest is recomputed from sources[] with the rule the receipt states;
  4. receipts that declare the publish contract carry its required receipt fields
     and validate against contracts/film-receipt.v1.schema.json;
  5. the latest-film pointer resolves to real assets and to an index entry.

Legacy receipts that predate the publish contract are reported as warnings, not failures:
they are listed, not blessed. Exit code 1 if any hard check fails. Nothing here trusts a
receipt: it only trusts the bytes.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "herakles.final-film-publish.v1"
CONTRACT_RECEIPT_FIELDS = ("source_digest", "render_command", "sha256", "world_link", "outsider_qa", "reduced_motion_qa")
MANIFEST_RULE = "sha256 of 'path\\0sha256\\n' lines, sources in listed order"

fails = []
warnings = []


def read_json(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def manifest_digest(sources):
    h = hashlib.sha256()
    for s in sources:
        h.update(f"{s['path']}\0{s['sha256']}\n".encode())
    return h.hexdigest()


def check_sources(receipt, film, problems):
    sources = receipt.get("sources")
    if sources is None:
        return 0
    if not isinstance(sources, list):
        problems.append("sources: liste degil")
        return 0
    checked = 0
    for s in sources:
        path = (s or {}).get("path")
        expected = (s or {}).get("sha256")
        if not path or not expected:
            problems.append(f"sources kaydi eksik: {s}")
            continue
        full = ROOT / path
        if not full.exists():
            problems.append(f"sources dosyasi yok: {path}")
            continue
        actual = sha256(full)
        checked += 1
        if actual != expected:
            problems.append(f"sources uyusmuyor: {path} makbuz={expected[:12]} disk={actual[:12]}")
    rule = receipt.get("source_digest_rule")
    declared = receipt.get("source_digest")
    if declared and rule == MANIFEST_RULE and checked == len(sources):
        if declared != manifest_digest(sources):
            problems.append(f"source_digest kurala uymuyor: makbuz={declared[:12]}")
    elif declared and rule and rule != MANIFEST_RULE:
        warnings.append(f"{film}: bilinmeyen source_digest_rule, manifest dogrulanmadi")
    return checked


def check_media_digests(entry, receipt, problems):
    """Map each receipt digest key to the repository file it should match, then re-hash it."""
    film = entry["id"]
    targets = {
        "film_sha256": entry.get("render"),
        "preview_sha256": entry.get("preview"),
        "poster_sha256": entry.get("poster"),
        "reduced_motion_sha256": f"showcase/films/{film}-reduced-motion.mp4",
        "scene_sha256": (receipt.get("source") or {}).get("scene") if isinstance(receipt.get("source"), dict) else None,
    }
    checked = 0
    for key, expected in (receipt.get("digests") or {}).items():
        target = targets.get(key)
        if not target:
            continue
        path = ROOT / target
        if not path.exists():
            problems.append(f"{key}: hedef dosya yok ({target})")
            continue
        actual = sha256(path)
        checked += 1
        if actual != expected:
            problems.append(f"{key} uyusmuyor: makbuz={expected[:12]} disk={actual[:12]} ({target})")
    return checked


def check_entry(entry):
    film = entry.get("id", "<id yok>")
    status = entry.get("status", "<status yok>")
    problems = []
    checked = 0

    for key in ("render", "preview", "poster", "receipt"):
        rel = entry.get(key)
        if rel and not (ROOT / rel).exists():
            problems.append(f"eksik dosya: {key}={rel}")

    receipt = None
    rel = entry.get("receipt")
    if rel and (ROOT / rel).exists():
        receipt = read_json(rel)
        claimed = receipt.get("contract") == CONTRACT
        if claimed:
            for field in CONTRACT_RECEIPT_FIELDS:
                if field not in receipt:
                    problems.append(f"sozlesme alani yok: {field}")
        if receipt.get("schema") == "herakles.film-receipt.v1":
            try:
                import jsonschema
            except ImportError:
                warnings.append(f"{film}: jsonschema kurulu degil, sema dogrulamasi atlandi")
            else:
                schema = read_json("contracts/film-receipt.v1.schema.json")
                try:
                    jsonschema.validate(receipt, schema)
                except Exception as exc:  # jsonschema.ValidationError
                    line = str(exc).splitlines()[0][:110]
                    if claimed:
                        problems.append(f"sema ihlali: {line}")
                    else:
                        warnings.append(f"{film}: legacy makbuz semaya uymuyor ({line})")
        elif not claimed:
            warnings.append(f"{film}: legacy makbuz (sozlesme beyani yok)")
        checked += check_media_digests(entry, receipt, problems)
        checked += check_sources(receipt, film, problems)

    gates = (receipt or {}).get("gates", {})
    open_gates = [k for k, v in gates.items() if v is False]
    label = f"{film:34s} {status:24s} dogrulanan={checked:2d} acik_kapi={','.join(open_gates) if open_gates else '-'}"
    if problems:
        fails.append(film)
        print(f"FAIL {label}")
        for p in problems:
            print(f"       - {p}")
    else:
        print(f"ok   {label}")
    return checked


def main():
    index = read_json("showcase/film-index.json")
    entries = index.get("films", [])
    only = None
    argv = sys.argv[1:]
    if argv:
        if argv[0] == "--id" and len(argv) > 1:
            only = argv[1]
        else:
            raise SystemExit("Kullanim: verify-films.py [--id <film>]")

    verified = 0
    for entry in entries:
        if only and entry.get("id") != only:
            continue
        verified += check_entry(entry)

    pointer = read_json("showcase/latest-film.json")
    ids = {e.get("id") for e in entries}
    pointer_problems = []
    for key in ("preview", "render", "receipt"):
        rel = pointer.get(key)
        if not rel or not (ROOT / rel).exists():
            pointer_problems.append(f"pointer {key} cozulmuyor: {rel}")
    if pointer.get("id") not in ids:
        pointer_problems.append(f"pointer id indekste yok: {pointer.get('id')}")
    if pointer_problems:
        fails.append("latest-film.json")
        print("FAIL latest-film.json")
        for p in pointer_problems:
            print(f"       - {p}")
    else:
        print(f"ok   latest-film.json -> {pointer.get('id')} ({pointer.get('status')})")

    for w in warnings:
        print(f"uyari {w}")
    print(f"\n{len(entries)} kayit | yeniden hesaplanan digest={verified} | uyari={len(warnings)} | hata={len(fails)}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
