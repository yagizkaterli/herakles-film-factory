# Scene contract

Scenes are deterministic functions of a validated source manifest and a storyboard state machine.

Each scene must expose:

- stable object IDs;
- a `construct()` entry point for Manim or ManimGL-compatible execution;
- named holds before prediction and reveal;
- a final state that is meaningful with motion disabled;
- no operational numbers that are not present in the source manifest.

The first production scene will be the HERAKLES contextless-agent proof: a blank Claude process reads a task card, traverses source surfaces, and emits a receipt-backed paper section. The visual objects are the real card, source pointers, event receipt, and output pointer—not a fabricated world.
