from manim import *


class AnlatiLabelVsStream3D(ThreeDScene):
    """Anlati single move: a green label contradicted by a frozen stream tail."""

    def construct(self):
        self.camera.background_color = "#070A10"
        self.set_camera_orientation(phi=67 * DEGREES, theta=-53 * DEGREES, focal_distance=18)
        title = Text("THE LABEL SAID RUNNING", font="DejaVu Sans Mono", font_size=26, color="#E8E2D7", weight=BOLD)
        title.to_edge(UP, buff=.25); self.add_fixed_in_frame_mobjects(title); self.play(FadeIn(title), run_time=.4)

        surface = Prism(dimensions=[6.5, .28, 3.1], fill_color="#183B32", fill_opacity=.95, stroke_color="#7CE0B0", stroke_width=2)
        surface.move_to([0, -.35, 0]); self.play(FadeIn(surface), run_time=.5)
        label = Text("RUNNING", font="DejaVu Sans Mono", font_size=22, color="#7CE0B0", weight=BOLD)
        label.to_edge(LEFT, buff=.45).shift(DOWN * 1.0); self.add_fixed_in_frame_mobjects(label); self.play(Write(label), run_time=.5)

        stream = VGroup()
        for i in range(12):
            dot = Sphere(radius=.08, resolution=(8, 6), fill_color="#7CE0B0", stroke_width=0)
            dot.move_to([-2.6 + i * .45, .35, .18])
            stream.add(dot)
        self.play(LaggedStart(*[FadeIn(d) for d in stream], lag_ratio=.04), run_time=.6)

        frozen = Text("model=<synthetic>  output_tokens=0", font="DejaVu Sans Mono", font_size=15, color="#FF6370")
        frozen.to_edge(DOWN, buff=.38); self.add_fixed_in_frame_mobjects(frozen)
        self.play(Write(frozen), run_time=.6)

        red = Sphere(radius=.32, resolution=(12, 8), fill_color="#FF4D5E", stroke_color="#FFD5D9", stroke_width=2)
        red.move_to([0, .45, .4]); self.play(GrowFromCenter(red), run_time=.5)
        crack = VGroup(Line([-2.7, .15, .42], [-.3, .15, .42], color="#FF4D5E", stroke_width=3), Line([.3, .15, .42], [2.7, .15, .42], color="#FF4D5E", stroke_width=3))
        self.play(Create(crack), run_time=.6)

        hold = Text("LABEL ≠ STREAM", font="DejaVu Sans Mono", font_size=21, color="#FF6370", weight=BOLD)
        hold.to_edge(DOWN, buff=.08); self.add_fixed_in_frame_mobjects(hold); self.play(Write(hold), run_time=.5)
        stamp = Text("source-bound contradiction · one move · receipt pending", font="DejaVu Sans Mono", font_size=9, color="#778492")
        stamp.to_edge(UP, buff=.05); self.add_fixed_in_frame_mobjects(stamp); self.wait(1.0)
