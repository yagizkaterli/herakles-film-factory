# Lobi production machine → Film Factory

Lobi is not only the place where the team discusses the film. It is the production machine that turns a plain-language intention into a bounded project, a room, a repo, a partitioned queue, a cross-review path and receipts.

## Machine input

One human intention in plain language:

> Make the work understandable to someone who has never seen HERAKLES.

## Machine output

```text
intention
  -> room + project identity
  -> research / prior-art partition
  -> storyboard and source manifest
  -> image direction partition
  -> Manim/Three.js scene partition
  -> render + browser QA
  -> receipt + World pointer
```

## Film-specific operating rules

- One project room is the coordination surface; no parallel shadow room.
- Every chapter is named and directly inspectable.
- A stable owner/source anchor remains readable while surrounding context changes.
- Pause freezes the film clock, chapter state and pending human cue.
- Restart resets the state machine.
- Reduced motion preserves the same state and copy without travel or autoplay.
- Factual trace reveal comes from the source manifest; no decorative event stream.
- Human-owned actions remain visibly human-owned.
- ImageGen is art direction only; it cannot create a receipt or World fact.

## Scale model

Lobi partitions the film into independent work units. Each unit carries:

- source pointer;
- output path;
- dependency gate;
- acceptance test;
- receipt writer;
- cross-review route.

The coordinator never asks a worker to “make it look better” without a named visual proposition and a falsifier. The worker returns an artifact or a measured blocker.

## World integration

The World is the film’s living context, not its backdrop. A chapter may read the World snapshot and event stream, focus the camera on a real object, and point to a receipt. It may not write canonical construction or invent a task, agent, count or outcome.
