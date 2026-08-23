from manim import *


class S6PhrasingV3(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#05070B"
        self.set_camera_orientation(phi=66 * DEGREES, theta=-55 * DEGREES, focal_distance=20)
        title = Text("CAN S^6 CARRY A COMPLEX STRUCTURE?", font="DejaVu Sans Mono", font_size=21, color="#F2F5F7", weight=BOLD)
        title.to_edge(UP, buff=.2); self.add_fixed_in_frame_mobjects(title); self.play(FadeIn(title), run_time=.5)
        line = Text("Start with a family, not the answer.", font="DejaVu Sans Mono", font_size=16, color="#B9D9EC")
        line.to_edge(DOWN, buff=.25); self.add_fixed_in_frame_mobjects(line)
        torus = Torus(major_radius=1.0, minor_radius=.32, color="#86D8FF", stroke_width=2).move_to([-2.7, .55, 0])
        self.play(FadeIn(torus), Write(line), run_time=.7); self.wait(.7)
        line2 = Text("A complex 2-torus can change while staying a torus.", font="DejaVu Sans Mono", font_size=13, color="#B9D9EC").to_edge(DOWN, buff=.25)
        self.add_fixed_in_frame_mobjects(line2); self.play(ReplacementTransform(line, line2), run_time=.6)
        torus2 = torus.copy().move_to([-.5, .55, 0]).scale(.9); self.play(TransformFromCopy(torus, torus2), run_time=1.0)
        points = VGroup(*[Dot3D([x, -1, .05], radius=.1, color="#F0BC67") for x in [-3.5, 0, 3.5]])
        labels = VGroup(*[Text(v, font="DejaVu Sans Mono", font_size=12, color="#F0BC67") for v in ["order 3", "order 4", "cusp ∞"]])
        for l, x in zip(labels, [-3.5, 0, 3.5]): l.to_edge(DOWN, buff=.62).shift(RIGHT*x*.38)
        self.add(points); self.add_fixed_in_frame_mobjects(labels); self.play(LaggedStart(*[FadeIn(p) for p in points], lag_ratio=.12), LaggedStart(*[Write(l) for l in labels], lag_ratio=.12), run_time=.8)
        line3 = Text("At ∞, the cycles twist. This is monodromy.", font="DejaVu Sans Mono", font_size=14, color="#F0BC67").to_edge(DOWN, buff=.25)
        self.add_fixed_in_frame_mobjects(line3); twisted = torus2.copy().move_to([1.1, .55, 0]).rotate(PI/5, axis=OUT).stretch(.68, dim=0); self.play(ReplacementTransform(line2, line3), Transform(torus2, twisted), run_time=1.2)
        hexagon = RegularPolygon(n=6, radius=1.05, color="#F0BC67", stroke_width=3).rotate(PI/6).move_to([3.4, .55, 0])
        line4 = Text("The twisted fibre becomes a six-sided dP6 surface.", font="DejaVu Sans Mono", font_size=14, color="#FFD6A0").to_edge(DOWN, buff=.25)
        self.add_fixed_in_frame_mobjects(line4); self.play(ReplacementTransform(line3, line4), Transform(twisted, hexagon), run_time=1.4)
        line5 = Text("The gluing removes the loop obstruction: π₁ = 0.", font="DejaVu Sans Mono", font_size=14, color="#B9F3CB").to_edge(DOWN, buff=.25)
        self.add_fixed_in_frame_mobjects(line5); self.play(ReplacementTransform(line4, line5), run_time=.7)
        sphere = Sphere(radius=1.35, resolution=(18, 12), fill_opacity=.12, fill_color="#DDEEFF", stroke_color="#DDEEFF", stroke_width=1).move_to([5.2, .55, 0])
        final = Text("So the total space closes as S^6. Yup.", font="DejaVu Sans Mono", font_size=17, color="#F2F5F7", weight=BOLD).to_edge(DOWN, buff=.25)
        self.add_fixed_in_frame_mobjects(final); self.play(FadeIn(sphere), ReplacementTransform(line5, final), run_time=1.0); self.wait(1.5)
        stamp = Text("source: s6.pdf · v3 phrasing · outsider-first camera contract", font="DejaVu Sans Mono", font_size=8, color="#6B8090").to_edge(UP, buff=.04); self.add_fixed_in_frame_mobjects(stamp)
