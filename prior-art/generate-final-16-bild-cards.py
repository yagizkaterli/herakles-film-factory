from pathlib import Path

out = Path("/root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_oda-kuyruk/sistem-analizi-s106")
categories = ["world_binding", "story_grammar", "camera_control", "provenance", "accessibility", "3d_composition", "timing", "testing"]
for i in range(1, 17):
    category = categories[(i - 1) % len(categories)]
    (out / f"d-PRIOR-ART-09-{i:02d}.md").write_text(
        f"---\nkanal: oda\ndokunur: evet\ngerektirir: [oku, kos, yaz]\nsinif: 4\naile: aracli\n---\n# PRIOR-ART-09-{i:02d} — {category}\n\nFind one NEW primary-source precedent for {category}. Read the current ATLAS and batch-08 merged receipt. Do not duplicate any existing title or URL. Return one decision atom JSON with one source-bound entry: id, category, title, source_url, observed_pattern, transferable_rule, rejection_rule, citation_receipt, status. No invented sources.\n",
        encoding="utf-8",
    )
