from pathlib import Path

out = Path("/root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_oda-kuyruk/sistem-analizi-s106")
categories = ["world_binding", "story_grammar", "camera_control", "provenance", "accessibility", "3d_composition", "timing", "testing"]
for i, category in enumerate(categories, 1):
    (out / f"d-PRIOR-ART-10-{i:02d}.md").write_text(
        f"---\nkanal: oda\ndokunur: evet\ngerektirir: [oku, kos, yaz]\nsinif: 4\naile: aracli\n---\n# PRIOR-ART-10-{i:02d} — {category}\n\nFind one final NEW primary-source precedent for {category}. Read ATLAS.json, batch-08-merged.json and batch-09-merged.json. Do not duplicate any title or URL. Return one decision atom JSON containing one source-bound entry with id, category, title, source_url, observed_pattern, transferable_rule, rejection_rule, citation_receipt and status. No invented sources.\n",
        encoding="utf-8",
    )
