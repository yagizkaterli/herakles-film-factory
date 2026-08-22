from manim import *


class HeraklesTraceToReceipt3D(ThreeDScene):
    """HERAKLES-native grammar pilot: trace -> gate -> route -> EON -> seal."""

    def construct(self):
        self.camera.background_color = "#070A0F"
        self.set_camera_orientation(phi=67 * DEGREES, theta=-53 * DEGREES, focal_distance=20)
        title = Text("TRACE BECOMES A RECEIPT", font="DejaVu Sans Mono", font_size=27, color="#E8E2D7", weight=BOLD)
        title.to_edge(UP, buff=.25); self.add_fixed_in_frame_mobjects(title); self.play(FadeIn(title), run_time=.4)

        # EON strata: persistent world layers, not a dashboard.
        strata = VGroup()
        for i, (x, c) in enumerate([(-3.6, "#162A23"), (-1.2, "#26321E"), (1.2, "#222A38"), (3.6, "#30301D")]):
            s = Prism(dimensions=[2.0, .22, 1.7], fill_color=c, fill_opacity=.98, stroke_color="#365B55", stroke_width=1.5)
            s.move_to([x, -.28, 0]); strata.add(s)
        self.play(LaggedStart(*[FadeIn(s) for s in strata], lag_ratio=.12), run_time=.8)

        trace = Sphere(radius=.25, resolution=(12, 8), fill_color="#86D8FF", stroke_color="#D8F6FF", stroke_width=2)
        trace.move_to([-3.6, .35, 0])
        gate = Torus(major_radius=.42, minor_radius=.1, color="#F0BC67").rotate(PI/2, axis=RIGHT)
        gate.move_to([-1.2, .5, 0])
        route_a = Line([-1.2, .5, 0], [1.2, .5, .45], color="#86D8FF", stroke_width=3)
        route_b = Line([-1.2, .5, 0], [1.2, .5, -.45], color="#F0BC67", stroke_width=3)
        eon = Prism(dimensions=[1.2, .3, 1.0], fill_color="#1C2D3A", stroke_color="#B7E8FF", stroke_width=2).move_to([1.2, .42, .45])
        seal = Prism(dimensions=[1.2, .36, 1.0], fill_color="#173524", stroke_color="#B9F3CB", stroke_width=3).move_to([3.6, .55, .45])
        self.play(GrowFromCenter(trace), GrowFromCenter(gate), run_time=.5)
        self.play(Create(Line(trace.get_right(), gate.get_left(), color="#86D8FF", stroke_width=4)), run_time=.5)
        self.play(Create(route_a), Create(route_b), run_time=.6)
        self.play(FadeIn(eon), run_time=.4)
        self.play(Create(Line(eon.get_right(), seal.get_left(), color="#B9F3CB", stroke_width=4)), FadeIn(seal), run_time=.6)

        labels = VGroup(
            Text("TRACE", font="DejaVu Sans Mono", font_size=12, color="#86D8FF"),
            Text("QUESTION-GATE", font="DejaVu Sans Mono", font_size=12, color="#F0BC67"),
            Text("EON-STRATUM", font="DejaVu Sans Mono", font_size=12, color="#B7E8FF"),
            Text("RECEIPT-SEAL", font="DejaVu Sans Mono", font_size=12, color="#B9F3CB"),
        )
        for lab, x in zip(labels, [-3.6, -1.2, 1.2, 3.6]):
            lab.to_edge(DOWN, buff=.38).shift(RIGHT * x * .48)
        self.add_fixed_in_frame_mobjects(labels); self.play(LaggedStart(*[Write(l) for l in labels], lag_ratio=.12), run_time=.7)
        note = Text("WORLD SNAPSHOT · 17 agents · 2 tasks · 2 queues · 4 EON strata · 2 receipts", font="DejaVu Sans Mono", font_size=13, color="#E8E2D7")
        note.to_edge(DOWN, buff=.08); self.add_fixed_in_frame_mobjects(note); self.play(Write(note), run_time=.5)
        stamp = Text("HERAKLES GRAMMAR v1 · deterministic geometry · World link pending", font="DejaVu Sans Mono", font_size=9, color="#778492")
        stamp.to_edge(UP, buff=.05); self.add_fixed_in_frame_mobjects(stamp); self.wait(1.0)
