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

        # World-bound agents: each live agent is a visible object, not a counter label.
        agents = VGroup()
        for i in range(17):
            a = Sphere(radius=.085, resolution=(8, 6), fill_color="#86D8FF", stroke_color="#D8F6FF", stroke_width=1)
            a.move_to([-4.25 + (i % 6) * .22, .22 + (i // 6) * .18, -.42 + (i % 3) * .42])
            agents.add(a)
        self.play(LaggedStart(*[FadeIn(a) for a in agents], lag_ratio=.025), run_time=.6)
        trace = Sphere(radius=.25, resolution=(12, 8), fill_color="#86D8FF", stroke_color="#D8F6FF", stroke_width=2)
        trace.move_to([-3.6, .35, 0])
        tasks = VGroup()
        for z in [-.32, .32]:
            task = Prism(dimensions=[.48, .18, .34], fill_color="#382B18", stroke_color="#F0BC67", stroke_width=1.5)
            task.move_to([-1.2, .25, z]); tasks.add(task)
        self.play(LaggedStart(*[FadeIn(t) for t in tasks], lag_ratio=.1), run_time=.35)
        gate = Torus(major_radius=.42, minor_radius=.1, color="#F0BC67").rotate(PI/2, axis=RIGHT)
        gate.move_to([-1.2, .5, 0])
        route_a = Line([-1.2, .5, 0], [1.2, .5, .45], color="#86D8FF", stroke_width=3)
        route_b = Line([-1.2, .5, 0], [1.2, .5, -.45], color="#F0BC67", stroke_width=3)
        queues = VGroup(Line([-.8, .5, -.32], [1.0, .5, -.32], color="#F0BC67", stroke_width=2), Line([-.8, .5, .32], [1.0, .5, .32], color="#86D8FF", stroke_width=2))
        self.play(Create(queues), run_time=.35)
        eon = VGroup()
        for z in [-.32, .32]:
            e = Prism(dimensions=[.52, .24, .42], fill_color="#1C2D3A", stroke_color="#B7E8FF", stroke_width=1.5)
            e.move_to([1.2, .42, z]); eon.add(e)
        self.play(LaggedStart(*[FadeIn(e) for e in eon], lag_ratio=.1), run_time=.35)
        seals = VGroup()
        for z in [-.32, .32]:
            s = Prism(dimensions=[.52, .28, .42], fill_color="#173524", stroke_color="#B9F3CB", stroke_width=2)
            s.move_to([3.6, .55, z]); seals.add(s)
        self.play(GrowFromCenter(trace), GrowFromCenter(gate), run_time=.5)
        self.play(Create(Line(trace.get_right(), gate.get_left(), color="#86D8FF", stroke_width=4)), run_time=.5)
        self.play(Create(route_a), Create(route_b), run_time=.6)
        self.play(Create(Line([1.45, .5, -.32], [3.25, .55, -.32], color="#B9F3CB", stroke_width=3)), Create(Line([1.45, .5, .32], [3.25, .55, .32], color="#B9F3CB", stroke_width=3)), FadeIn(seals), run_time=.6)

        labels = VGroup(
            Text("TRACE", font="DejaVu Sans Mono", font_size=12, color="#86D8FF"),
            Text("QUESTION-GATE", font="DejaVu Sans Mono", font_size=12, color="#F0BC67"),
            Text("EON-STRATUM", font="DejaVu Sans Mono", font_size=12, color="#B7E8FF"),
            Text("RECEIPT-SEAL", font="DejaVu Sans Mono", font_size=12, color="#B9F3CB"),
        )
        for lab, x in zip(labels, [-3.6, -1.2, 1.2, 3.6]):
            lab.to_edge(DOWN, buff=.38).shift(RIGHT * x * .48)
        self.add_fixed_in_frame_mobjects(labels); self.play(LaggedStart(*[Write(l) for l in labels], lag_ratio=.12), run_time=.7)
        note = Text("WORLD SNAPSHOT BOUND · OBJECTS CARRY THE STORY", font="DejaVu Sans Mono", font_size=13, color="#E8E2D7")
        note.to_edge(DOWN, buff=.08); self.add_fixed_in_frame_mobjects(note); self.play(Write(note), run_time=.5)
        stamp = Text("HERAKLES GRAMMAR v1 · deterministic geometry · World link pending", font="DejaVu Sans Mono", font_size=9, color="#778492")
        stamp.to_edge(UP, buff=.05); self.add_fixed_in_frame_mobjects(stamp); self.wait(1.0)
