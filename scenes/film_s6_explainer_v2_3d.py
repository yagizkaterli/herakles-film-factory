from manim import *


class S6ExplainerV2(ThreeDScene):
    """Outsider-QA revision: legend, explicit morph, formula substitution, closure."""

    def construct(self):
        self.camera.background_color = "#05070B"
        self.set_camera_orientation(phi=66 * DEGREES, theta=-55 * DEGREES, focal_distance=20)
        title = Text("DOES S^6 ADMIT A COMPLEX STRUCTURE?", font="DejaVu Sans Mono", font_size=22, color="#F2F5F7", weight=BOLD)
        title.to_edge(UP, buff=.2); self.add_fixed_in_frame_mobjects(title); self.play(FadeIn(title), run_time=.4)
        answer = Text("YUP — HERE IS THE GEOMETRIC STORY", font="DejaVu Sans Mono", font_size=16, color="#F0BC67")
        answer.to_edge(UP, buff=.68); self.add_fixed_in_frame_mobjects(answer); self.play(Write(answer), run_time=.5)

        legend = VGroup(
            Text("BLUE torus = smooth fibre", font="DejaVu Sans Mono", font_size=10, color="#86D8FF"),
            Text("AMBER hexagon = cusp dP6 fibre", font="DejaVu Sans Mono", font_size=10, color="#F0BC67"),
            Text("WHITE sphere = closed total space", font="DejaVu Sans Mono", font_size=10, color="#E8EEF5"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=.08).to_corner(UR, buff=.25)
        self.add_fixed_in_frame_mobjects(legend); self.play(LaggedStart(*[Write(x) for x in legend], lag_ratio=.1), run_time=.7)

        base = Line([-5, -1, 0], [5, -1, 0], color="#2A6CFF", stroke_width=3); self.play(Create(base), run_time=.4)
        for x, lab in [(-3.5, "3: order-3"), (0, "4: order-4"), (3.5, "∞: cusp")]:
            p = Dot3D([x, -1, .05], radius=.1, color="#F0BC67"); t = Text(lab, font="DejaVu Sans Mono", font_size=10, color="#F0BC67").to_edge(DOWN, buff=.55).shift(RIGHT*x*.4)
            self.add(p); self.add_fixed_in_frame_mobjects(t); self.play(FadeIn(p), Write(t), run_time=.25)

        torus = Torus(major_radius=1.0, minor_radius=.3, color="#86D8FF", stroke_width=2).move_to([-3.3, .55, 0])
        label = Text("smooth complex 2-torus fibre", font="DejaVu Sans Mono", font_size=13, color="#86D8FF").to_edge(DOWN, buff=.18)
        self.add_fixed_in_frame_mobjects(label); self.play(FadeIn(torus), Write(label), run_time=.6)
        self.wait(.5)

        cusp = Text("at ∞, monodromy twists the fibre", font="DejaVu Sans Mono", font_size=13, color="#F0BC67").to_edge(DOWN, buff=.18)
        self.add_fixed_in_frame_mobjects(cusp); self.play(ReplacementTransform(label, cusp), run_time=.5)
        twisted = torus.copy().move_to([.5, .55, 0]).rotate(PI/5, axis=OUT).stretch(.65, dim=0)
        self.play(Transform(torus, twisted), run_time=1.0)

        hexagon = RegularPolygon(n=6, radius=1.05, color="#F0BC67", stroke_width=3).rotate(PI/6).move_to([2.7, .55, 0])
        morph = Text("twisted torus → hexagonal moment polygon = dP6", font="DejaVu Sans Mono", font_size=12, color="#FFD6A0").to_edge(DOWN, buff=.18)
        self.add_fixed_in_frame_mobjects(morph); self.play(ReplacementTransform(cusp, morph), Transform(torus, hexagon), run_time=1.4)

        formula = Text("π₁ = Z / |12·0 − 4·1 − 3·(−1)| = Z/1 = 0", font="DejaVu Sans Mono", font_size=15, color="#B9F3CB").to_edge(DOWN, buff=.18)
        self.add_fixed_in_frame_mobjects(formula); self.play(ReplacementTransform(morph, formula), run_time=.7)
        sphere = Sphere(radius=1.35, resolution=(18, 12), fill_opacity=.12, fill_color="#DDEEFF", stroke_color="#DDEEFF", stroke_width=1).move_to([5.0, .55, 0])
        close = Text("the total space closes as the homology of S^6", font="DejaVu Sans Mono", font_size=14, color="#E8EEF5").to_edge(DOWN, buff=.18)
        self.add_fixed_in_frame_mobjects(close); self.play(FadeIn(sphere), ReplacementTransform(formula, close), run_time=.8)
        final = Text("one family · one cusp · one six-sphere", font="DejaVu Sans Mono", font_size=17, color="#F2F5F7", weight=BOLD).to_edge(DOWN, buff=.18)
        self.add_fixed_in_frame_mobjects(final); self.play(ReplacementTransform(close, final), run_time=.7)
        stamp = Text("source: s6.pdf · outsider-QA revision v2", font="DejaVu Sans Mono", font_size=8, color="#6B8090").to_edge(UP, buff=.04)
        self.add_fixed_in_frame_mobjects(stamp); self.wait(1.5)
