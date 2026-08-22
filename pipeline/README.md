# Production system

This repository is a production system, not a folder of renders.

## State machine

`SOURCE_CAPTURED -> QUESTION_LOCKED -> STORYBOARD_LOCKED -> ART_DIRECTION_LOCKED -> SCENE_IMPLEMENTED -> RENDERED -> QA_REVIEWED -> WORLD_LINKED`

Every transition has a machine-readable receipt. A film cannot move forward when its source digest, scene state, or QA gate is missing.

## Partitions

- `source/`: canonical HERAKLES snapshot/event adapters
- `storyboard/`: one-question, one-causal-transform scene plans
- `art-direction/`: ImageGen references and teardown notes; never operational evidence
- `scenes/`: Manim/ManimGL-compatible deterministic scene code
- `renders/`: ignored binary outputs; only selected deliverables are released
- `receipts/`: JSON receipts, hashes, source pointers, QA results
- `world-link/`: event/receipt pointers consumed by HERAKLES World

## Acceptance gates

1. Source parity: every visible number/object has a source pointer and digest.
2. Narrative: first concrete witness precedes abstraction; every motion has a semantic verb.
3. Identity: the same object ID survives each morph.
4. Authority: provisional/blocked/verified states never collapse into one visual state.
5. Render: deterministic frame range, resolution, fps, codec and seed are recorded.
6. QA: silent-open, reduced-motion, source-parity and outsider-read gates pass.
7. World link: the film points to a real event/receipt; it never creates one.
