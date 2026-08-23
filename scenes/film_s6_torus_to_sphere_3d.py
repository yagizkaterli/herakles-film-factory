from manim import *


class S6TorusToSphere3D(ThreeDScene):
    """Faithful visual thesis from s6.pdf: smooth torus family -> cusp hexagon -> S6 closure."""

    def construct(self):
        self.camera.background_color = "#05070B"
        self.set_camera_orientation(phi=66 * DEGREES, theta=-55 * DEGREES, focal_distance=20)
        title = Text("WHEN A TORUS FAMILY BECOMES S6", font="DejaVu Sans Mono", font_size=23, color="#E8E2E7", weight=BOLD)
        title.to_edge(UP, buff=.22); self.add_fixed_in_frame_mobjects(title); self.play(FadeIn(title), run_time=.4)

        base = Line([-5, -.9, 0], [5, -.9, 0], color="#2A6CFF", stroke_width=3)
        self.play(Create(base), run_time=.5)
        points = []
        for x, lab in [(-3.5, "3"), (0, "4"), (3.5, "∞")]:
            p = Dot3D([x, -.9, .05], radius=.11, color="#F0BC67")
            t = Text(lab, font="DejaVu Sans Mono", font_size=17, color="#F0BC67")
            t.to_edge(DOWN, buff=.65).shift(RIGHT * x * .45)
            points.append((p, t)); self.add(p); self.add_fixed_in_frame_mobjects(t); self.play(FadeIn(p), Write(t), run_time=.25)

        torus = Torus(major_radius=1.0, minor_radius=.32, color="#86D8FF", stroke_width=2)
        torus.move_to([-3.5, .65, 0]); self.play(FadeIn(torus), run_time=.5)
        torus2 = torus.copy().move_to([0, .65, 0]); torus3 = torus.copy().move_to([2.2, .65, 0]).scale(.82)
        self.play(TransformFromCopy(torus, torus2), run_time=.8)
        self.play(Transform(torus2, torus3), run_time=.8)

        hexagon = RegularPolygon(n=6, radius=1.15, color="#F0BC67", stroke_width=3)
        hexagon.rotate(PI/6); hexagon.move_to([3.5, .65, 0])
        self.play(Transform(torus3, hexagon), run_time=1.0)
        inner = RegularPolygon(n=6, radius=.48, color="#FF9B63", stroke_width=2)
        inner.rotate(PI/6); inner.move_to([3.5, .65, .02]); self.play(FadeIn(inner), run_time=.35)

        sphere = Sphere(radius=1.45, resolution=(16, 10), fill_opacity=.12, fill_color="#B8D9FF", stroke_color="#B8D9FF", stroke_width=1)
        sphere.move_to([5.8, .65, 0])
        self.play(FadeIn(sphere), run_time=.6)
        caption = Text("3, 4, cusp · unipotent monodromy · hexagonal dP6 · S6", font="DejaVu Sans Mono", font_size=12, color="#D8E9F6")
        caption.to_edge(DOWN, buff=.18); self.add_fixed_in_frame_mobjects(caption); self.play(Write(caption), run_time=.6)
        stamp = Text("source: alpo.ge/s6.pdf · deterministic geometry · proof receipt required", font="DejaVu Sans Mono", font_size=8, color="#6B8090")
        stamp.to_edge(UP, buff=.04); self.add_fixed_in_frame_mobjects(stamp); self.wait(1.0)
