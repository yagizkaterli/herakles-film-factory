from pathlib import Path

out = Path("/root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_oda-kuyruk/sistem-analizi-s106")
for i, category in enumerate(["world_binding", "provenance", "testing"], 1):
    (out / f"d-PRIOR-ART-11-{i:02d}.md").write_text(
        f"---\nkanal: oda\ndokunur: evet\ngerektirir: [oku, kos, yaz]\nsinif: 4\naile: aracli\n---\n# PRIOR-ART-11-{i:02d} — {category}\n\nFind one final NEW primary-source precedent for {category}. Read ATLAS.json and every batch receipt. Do not duplicate any title or URL. Return one decision atom JSON with one source-bound entry. No invented sources.\n",
        encoding="utf-8",
    )
