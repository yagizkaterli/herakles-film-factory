from manim import *


class S6ExplainerLong3D(ThreeDScene):
    """Longer public explainer: hook, family, cusp, dP6, closure."""

    def construct(self):
        self.camera.background_color = "#05070B"
        self.set_camera_orientation(phi=66 * DEGREES, theta=-55 * DEGREES, focal_distance=20)
        hook = Text("DOES S^6 ADMIT A COMPLEX STRUCTURE?", font="DejaVu Sans Mono", font_size=22, color="#F2F5F7", weight=BOLD)
        hook.to_edge(UP, buff=.22); self.add_fixed_in_frame_mobjects(hook); self.play(FadeIn(hook), run_time=.5)
        answer = Text("YUP.", font="DejaVu Sans Mono", font_size=32, color="#F0BC67", weight=BOLD)
        answer.to_edge(DOWN, buff=.3); self.add_fixed_in_frame_mobjects(answer); self.play(Write(answer), run_time=.6); self.wait(.5)
        self.play(FadeOut(answer), run_time=.3)

        base = Line([-5, -.9, 0], [5, -.9, 0], color="#2A6CFF", stroke_width=3)
        self.play(Create(base), run_time=.5)
        points = []
        for x, lab in [(-3.5, "3"), (0, "4"), (3.5, "∞")]:
            p = Dot3D([x, -.9, .05], radius=.11, color="#F0BC67")
            t = Text(lab, font="DejaVu Sans Mono", font_size=17, color="#F0BC67").to_edge(DOWN, buff=.65).shift(RIGHT * x * .45)
            points.append((p, t)); self.add(p); self.add_fixed_in_frame_mobjects(t); self.play(FadeIn(p), Write(t), run_time=.25)

        torus = Torus(major_radius=1.0, minor_radius=.32, color="#86D8FF", stroke_width=2).move_to([-3.5, .65, 0])
        family = Text("a smooth family of complex 2-tori", font="DejaVu Sans Mono", font_size=14, color="#B9D9EC").to_edge(UP, buff=.75)
        self.add_fixed_in_frame_mobjects(family); self.play(FadeIn(torus), Write(family), run_time=.7)
        torus2 = torus.copy().move_to([0, .65, 0]); torus3 = torus.copy().move_to([2.2, .65, 0]).scale(.82)
        self.play(TransformFromCopy(torus, torus2), run_time=1.0); self.play(Transform(torus2, torus3), run_time=1.0)

        cusp_text = Text("at the cusp: monodromy twists the fibre", font="DejaVu Sans Mono", font_size=14, color="#F0BC67").to_edge(UP, buff=.75)
        self.add_fixed_in_frame_mobjects(cusp_text); self.play(ReplacementTransform(family, cusp_text), run_time=.5)
        hexagon = RegularPolygon(n=6, radius=1.2, color="#F0BC67", stroke_width=3).rotate(PI/6).move_to([3.5, .65, 0])
        self.play(Transform(torus3, hexagon), run_time=1.4)
        dplabel = Text("hexagonal moment polygon → dP6 toric fibre", font="DejaVu Sans Mono", font_size=14, color="#FFD6A0").to_edge(DOWN, buff=.25)
        self.add_fixed_in_frame_mobjects(dplabel); self.play(Write(dplabel), run_time=.6); self.wait(.5)

        formula = Text("π₁(X) = Z / |12ℓ₀ − 4ℓ₁ − 3ℓ₂| = 1", font="DejaVu Sans Mono", font_size=17, color="#B9F3CB")
        formula.to_edge(DOWN, buff=.25); self.add_fixed_in_frame_mobjects(formula); self.play(ReplacementTransform(dplabel, formula), run_time=.7)
        sphere = Sphere(radius=1.5, resolution=(18, 12), fill_opacity=.12, fill_color="#B8D9FF", stroke_color="#B8D9FF", stroke_width=1).move_to([5.8, .65, 0])
        self.play(FadeIn(sphere), run_time=.7)
        close = Text("the total space closes with the homology of S^6", font="DejaVu Sans Mono", font_size=15, color="#D8E9F6").to_edge(DOWN, buff=.25)
        self.add_fixed_in_frame_mobjects(close); self.play(ReplacementTransform(formula, close), run_time=.7)
        final = Text("A torus family, one cusp, one six-sphere.", font="DejaVu Sans Mono", font_size=18, color="#F2F5F7", weight=BOLD).to_edge(DOWN, buff=.25)
        self.add_fixed_in_frame_mobjects(final); self.play(ReplacementTransform(close, final), run_time=.8)
        stamp = Text("source: alpo.ge/s6.pdf · tweet hook: @__alpoge__ · deterministic render", font="DejaVu Sans Mono", font_size=8, color="#6B8090").to_edge(UP, buff=.04)
        self.add_fixed_in_frame_mobjects(stamp); self.wait(2.0)
