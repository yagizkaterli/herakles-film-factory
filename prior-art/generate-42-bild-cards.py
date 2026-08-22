from pathlib import Path

OUT = Path("/root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_oda-kuyruk/sistem-analizi-s106")
CATEGORIES = [
    "procedural_graphics", "visual_state_machines", "scientific_3d_visualization",
    "camera_waypoint_control", "narrative_identity_continuity", "provenance_replay",
    "accessible_cinematic_controls", "realtime_rendering", "data_story_timing",
]

for i in range(1, 43):
    category = CATEGORIES[(i - 1) % len(CATEGORIES)]
    path = OUT / f"d-PRIOR-ART-08-{i:02d}.md"
    path.write_text(
        "---\n"
        "kanal: oda\n"
        "dokunur: evet\n"
        "gerektirir: [oku, kos, yaz]\n"
        "sinif: 4\n"
        "aile: aracli\n"
        "---\n"
        f"# PRIOR-ART-08-{i:02d} — {category}\n\n"
        "Find one NEW primary-source precedent for this category. Do not duplicate ATLAS.json, batch-04, batch-05, batch-06 or batch-07. Return a decision atom JSON and include exactly one entry with id, category, title, source_url, observed_pattern, transferable_rule, rejection_rule, citation_receipt and status. No invented sources.\n",
        encoding="utf-8",
    )
