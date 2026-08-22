# HERAKLES Film Factory

Evidence-bound film production for HERAKLES: ImageGen for art direction, Manim/ManimGL-compatible scenes for causal explanation, and HERAKLES World as the live source of verified system state.

## Core rule

The film never invents a world event. It reads a canonical snapshot/event, turns that event into a storyboard, renders the explanation, and stores a receipt that points back to the source.

The audience contract is in `pipeline/AUDIENCE-FIRST.md`; the legacy pipeline findings are in `research/LEGACY-PIPELINE-INVENTORY.json`.

## Pipeline

1. `source` — HERAKLES World snapshot, event stream, receipt, EON pointer
2. `storyboard` — one unresolved question and one causal transformation
3. `art-direction` — ImageGen reference only; no fake operational evidence
4. `scene` — Manim/ManimGL-compatible code using persistent objects
5. `render` — MP4 + poster + machine-readable receipt
6. `world-link` — film pointer attached to the corresponding World event/receipt
7. `qa` — source parity, reduced motion, readable outsider test

## HERAKLES World connection

- Lobi room: `de2b53bf-a6a6-459b-a393-b30210d6fb46`
- World UI: local `5174` or VPS-tunneled `5173`
- Live events: `/events`
- Snapshot: `/v2/snapshot`
- Commands: `/v2/commands` compatibility route
- Authority: World is a read-only mirror; verified receipt/evidence/review remains canonical.

## First film partition

- P0: snapshot hydration and event cursor
- P1: semantic event-to-world mapping
- P2: canonical visual state mapping
- P3: camera focus and browser QA

The four P0–P3 cards live in the Sistem Analizi Lobi queue and are linked to `BUYUK-RESIM-s110-WORLD-VISUAL-INTEGRATION.d2`.

## Non-goals

- no generated image presented as live system evidence
- no fake task, receipt, agent count, or world construction
- no new ontology or second coordination surface
