# Film showcase

This directory is the public artifact surface for HERAKLES Film Factory.

A file existing here does not by itself mean it is current or released. Use [`latest-film.json`](latest-film.json) for the moving promoted pointer and use each film's receipt for source/render bindings and limitations.

## Current promoted render

[`latest-film.json`](latest-film.json) currently points to **`terra-revenue-curve-20260908`** with status `deterministic-render`.

![Current promoted preview](latest-preview.gif)

[MP4](films/terra-revenue-curve-20260908.mp4) · [poster](films/terra-revenue-curve-20260908-poster.png) · [receipt](films/terra-revenue-curve-20260908.receipt.json)

The receipt limits the visible revenue milestones to **scenario assumptions**; they are not presented as measured paying-customer MRR/ARR.

## Film states

- `pilot` / `baseline`: useful visual research; not the promoted current film.
- `in-progress`: a render exists but one or more publication gates remain open.
- `qa-blocked`: a required gate failed or required evidence is missing.
- `deterministic-render`: render and receipt are bound, with claim limits carried by the receipt.
- `released`: reserved for an explicitly released artifact under the repository's publication contract.

## Other useful artifacts

The repository retains earlier pilots and baselines intentionally. For example, [`contextless-agent-proof-3d.mp4`](films/contextless-agent-proof-3d.mp4) is a rendered baseline with a receipt, while the Evidence Terrain, EON Camera Journey and trace-to-receipt pieces are visual-language pilots.

Do not infer chronology or authority from filename order. Historical experiments can coexist with a newer promoted pointer.

## Viewer contract

A promoted film should make it possible to answer:

1. What am I looking at?
2. What changed?
3. Why did it change?
4. Where is the source/receipt?
5. What does this film not prove?

If those answers disagree with the receipt, the receipt/source wins and the README or film surface needs correction.
