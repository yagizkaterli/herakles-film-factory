# Film showcase

This is the public-facing index inside the repository. It is intentionally honest: only rendered films with receipts appear as `released`.

## Film states

- `planned`: brief exists; no render yet.
- `in-progress`: scene or render is running; not a finished film.
- `qa-blocked`: a gate failed or browser capture is missing.
- `released`: MP4/poster/receipt/source link all exist.

## Current films

The first film is now rendered but not released: [contextless-agent-proof-3d.mp4](films/contextless-agent-proof-3d.mp4). Its source and render receipt are present; World linking, reduced-motion and outsider-read gates remain open.

## Viewer contract

Every released film page must answer, in order:

1. What am I looking at?
2. What changed?
3. Why did it change?
4. Where is the source?
5. What does this film not prove?
