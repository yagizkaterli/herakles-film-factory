# Frontier repository study

This is a pattern study, not a code clone.

## 3b1b / Manim

The repository separates the animation engine from video-specific scene code and makes examples/docs the first navigation surface.

**We take:** engine vs film separation, runnable examples, deterministic scene entry points, explicit installation/runtime contract.

**We add:** HERAKLES source manifests, evidence gates, World links, and audience-first narration.

Source: https://github.com/3b1b/manim

## Three.js

The repository treats examples as a browsable catalog and keeps a small, runnable scene as the first code witness.

**We take:** example gallery, one-click runnable scenes, source links beside the visual result.

**We add:** each scene must show its source event, receipt and authority state.

Source: https://github.com/mrdoob/three.js/

## Mapbox Storytelling

The story is divided into chapters; each chapter binds to a map view and may run a callback that changes the visualization.

**We take:** chapter manifest, camera waypoint, callback, persistent narrative state.

**We add:** EON/event IDs and a no-fake rule for every callback.

Source: https://github.com/mapbox/storytelling

## Flow Story / 3D storytelling

The project turns data into waypoints, camera transitions and annotated 3D scenes.

**We take:** explicit waypoint data and camera choreography as data, not ad hoc code.

**We add:** each waypoint carries a source pointer and a reversible QA assertion.

Source: https://github.com/Poolchaos/flow-story

## Genblaze / provenance-first media

The project makes media workflows manifest-driven and keeps schemas shared between producers.

**We take:** manifest as the central object, provider-neutral stages, generated output provenance.

**We add:** HERAKLES snapshot/event/receipt authority and World read-only linking.

Source: https://github.com/backblaze-labs/genblaze

## Our synthesis

`source manifest -> chapter/waypoint plan -> ImageGen art direction -> deterministic Manim scene -> render QA -> film receipt -> HERAKLES World pointer`

The README must show the result first, then let a reader descend through the source, scene, receipt and World link. A film that is not generated is listed as `planned`, never displayed as if it exists.
