from manim import *


class EvidenceTerrain3D(ThreeDScene):
    """Pilot P01: source nodes -> causal path -> receipt, deterministic geometry."""

    def construct(self):
        self.camera.background_color = "#080B10"
        self.set_camera_orientation(phi=66 * DEGREES, theta=-52 * DEGREES, focal_distance=18)

        title = Text("ONE TRACE, ONE RECEIPT", font="DejaVu Sans Mono", font_size=28, color="#E8E2D7", weight=BOLD)
        title.to_edge(UP, buff=.25)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=.5)

        terrain = VGroup()
        for x in range(-5, 6, 2):
            for z in range(-3, 4, 2):
                height = .12 + ((x + z) % 3) * .08
                tile = Prism(dimensions=[1.65, height, 1.3], fill_color="#122019", fill_opacity=.96,
                             stroke_color="#315344", stroke_width=1)
                tile.move_to([x, -0.35 + height / 2, z])
                terrain.add(tile)
        self.play(LaggedStart(*[FadeIn(t) for t in terrain], lag_ratio=.025), run_time=1.0)

        source = Sphere(radius=.34, resolution=(16, 10), fill_color="#86D8FF", stroke_color="#D8F6FF", stroke_width=2)
        source.move_to([-4.2, .35, 0])
        source_label = Text("SOURCE", font="DejaVu Sans Mono", font_size=14, color="#86D8FF")
        source_label.to_edge(LEFT, buff=.25).shift(DOWN * 1.05)
        self.add(source)
        self.add_fixed_in_frame_mobjects(source_label)
        self.play(GrowFromCenter(source), Write(source_label), run_time=.55)

        gate = Prism(dimensions=[1.45, .25, 1.15], fill_color="#382B18", stroke_color="#F0BC67", stroke_width=2)
        gate.move_to([-1.25, .2, 0])
        gate_label = Text("QUESTION", font="DejaVu Sans Mono", font_size=14, color="#F0BC67")
        gate_label.to_edge(LEFT, buff=.25).shift(DOWN * 1.38)
        self.add(gate)
        self.add_fixed_in_frame_mobjects(gate_label)
        self.play(FadeIn(gate), Write(gate_label), run_time=.5)

        receipt = Prism(dimensions=[1.8, .3, 1.2], fill_color="#153323", stroke_color="#B9F3CB", stroke_width=3)
        receipt.move_to([3.9, .55, 0])
        receipt_label = Text("RECEIPT", font="DejaVu Sans Mono", font_size=16, color="#B9F3CB", weight=BOLD)
        receipt_label.to_edge(RIGHT, buff=.3).shift(DOWN * 1.05)
        self.add(receipt)
        self.add_fixed_in_frame_mobjects(receipt_label)
        self.play(GrowFromCenter(receipt), Write(receipt_label), run_time=.6)

        path_a = Line(source.get_right(), gate.get_left(), color="#F0BC67", stroke_width=5)
        path_b = Line(gate.get_right(), receipt.get_left(), color="#86D8FF", stroke_width=5)
        self.play(Create(path_a), run_time=.6)
        self.play(Create(path_b), run_time=.7)

        evidence = Text("source -> question -> receipt", font="DejaVu Sans Mono", font_size=18, color="#E8E2D7")
        evidence.to_edge(DOWN, buff=.3)
        self.add_fixed_in_frame_mobjects(evidence)
        self.play(Write(evidence), run_time=.5)

        stamp = Text("P01 · deterministic scene · art reference is not evidence", font="DejaVu Sans Mono", font_size=10, color="#778492")
        stamp.to_edge(UP, buff=.05)
        self.add_fixed_in_frame_mobjects(stamp)
        self.wait(1.0)
