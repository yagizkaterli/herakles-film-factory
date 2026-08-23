from manim import *
import numpy as np


INDIGO = "#050816"
CYAN = "#75D9FF"
BLUE = "#2388FF"
VIOLET = "#9B7BFF"
CRIMSON = "#FF416C"
GOLD = "#FFC45C"
AMBER = "#FFB347"


def path_curve():
    return ParametricFunction(
        lambda t: np.array([t, 0.28 * np.sin(t * 0.75), -0.55 + 0.05 * np.cos(t)]),
        t_range=[-5.6, 5.6],
        color="#38516B",
        stroke_width=2,
    )


def caption(text, color="#F4F7FB"):
    bar = RoundedRectangle(corner_radius=0.12, width=11.6, height=0.62,
                           stroke_width=0, fill_color="#030712", fill_opacity=0.88)
    label = Text(text, font="DejaVu Sans", font_size=18, color=color, weight=BOLD)
    label.move_to(bar.get_center())
    group = VGroup(bar, label).to_edge(DOWN, buff=0.18)
    return group


class S6UniverseRebuild3D(ThreeDScene):
    """Geometry-first S6 film; ImageGen frames are visual priors, Manim is truth."""

    def construct(self):
        self.camera.background_color = INDIGO
        self.set_camera_orientation(phi=68 * DEGREES, theta=-58 * DEGREES, focal_distance=22)

        # Deterministic atmosphere: a fixed seed, never random per render.
        rng = np.random.default_rng(6)
        stars = VGroup(*[
            Dot3D([rng.uniform(-7, 7), rng.uniform(-4, 4), rng.uniform(-2.5, 2.5)],
                  radius=rng.uniform(0.006, 0.014), color="#7A91A8")
            for _ in range(42)
        ])
        self.add(stars)
        chapter = Text("S⁶  /  A GEOMETRIC JOURNEY", font="DejaVu Sans", font_size=10,
                       color="#8FA8BD").to_corner(UL, buff=0.22)
        self.add_fixed_in_frame_mobjects(chapter)

        # F01 — the question is an open shell, not an answer.
        shell = Sphere(radius=1.55, resolution=(20, 12), fill_opacity=0.025, fill_color=CYAN,
                       stroke_color=CYAN, stroke_width=1.7)
        seam = ParametricFunction(
            lambda t: np.array([1.56 * np.cos(t), 1.56 * np.sin(t), 0.0]),
            t_range=[-0.42, 0.42], color=GOLD, stroke_width=7,
        ).rotate(PI / 2, axis=RIGHT)
        line = caption("Can S⁶ carry a complex structure?", "#F4F7FB")
        self.add_fixed_in_frame_mobjects(line)
        self.play(FadeIn(shell), Create(seam), FadeIn(line), run_time=1.4)
        self.wait(0.8)

        # F02 — five identical fibres along one continuous base path.
        base = path_curve()
        tori = VGroup()
        positions = np.linspace(-4.4, 4.4, 5)
        for i, x in enumerate(positions):
            torus = Torus(major_radius=0.54, minor_radius=0.16, color=BLUE, stroke_width=1.5)
            torus.set_fill(BLUE, opacity=0.14)
            torus.move_to([x, 0.28 * np.sin(x * 0.75), 0])
            if i == 2:
                torus.set_color(CYAN)
                torus.scale(1.18)
            tori.add(torus)
        line2 = caption("Build a smooth family of 2-tori.", "#9FE5FF")
        self.add_fixed_in_frame_mobjects(line2)
        self.play(FadeOut(shell), FadeOut(seam), ReplacementTransform(line, line2), Create(base),
                  LaggedStart(*[FadeIn(t) for t in tori], lag_ratio=0.12), run_time=2.2)
        self.wait(0.8)

        # F03 — three visually distinct boundary events.
        gate3 = Torus(major_radius=0.65, minor_radius=0.09, color=CRIMSON, stroke_width=3).move_to([-3.3, 0, 0.15])
        gate4 = Torus(major_radius=0.82, minor_radius=0.09, color=VIOLET, stroke_width=3).move_to([0.0, 0, 0.15])
        gate3.set_fill(CRIMSON, opacity=0.20)
        gate4.set_fill(VIOLET, opacity=0.20)
        # One wide cusp portal, intentionally not a fourth gate.
        cusp = Circle(radius=0.82, color=GOLD, stroke_width=5).move_to([3.45, 0, 0.18]).stretch(1.75, dim=0)
        gates = VGroup(gate3, gate4, cusp)
        gate3.rotate(PI * 0.7, axis=OUT, about_point=gate3.get_center())
        gate4.rotate(-PI * 0.45, axis=OUT, about_point=gate4.get_center())
        line3 = caption("Three boundary events shape the family.", "#FFD36A")
        self.add_fixed_in_frame_mobjects(line3)
        self.play(FadeOut(tori), ReplacementTransform(line2, line3), run_time=0.55)
        self.play(FadeIn(gates), run_time=1.7)
        self.wait(1.25)

        # F04 — cusp passage: persistent centre fibre twists and becomes a hexagonal surface.
        fibre = Torus(major_radius=1.0, minor_radius=0.28, color=BLUE, stroke_width=2).move_to([0, 0, 0.1])
        hex_surface = RegularPolygon(n=6, radius=1.3, color=AMBER, stroke_width=4).rotate(PI / 6)
        hex_surface.set_fill(AMBER, opacity=0.12)
        line4 = caption("At the cusp, the cycles twist into a hexagonal fibre.", "#FFCD7A")
        self.add_fixed_in_frame_mobjects(line4)
        self.play(FadeOut(gates), FadeOut(base), ReplacementTransform(line3, line4), FadeIn(fibre),
                  Rotate(fibre, PI / 2, axis=OUT), run_time=1.0)
        self.play(Transform(fibre, hex_surface), run_time=2.0)
        self.wait(0.8)

        # F05 — boundary seams fold closed; the film ends on a complete world.
        closure = Sphere(radius=1.55, resolution=(22, 14), fill_opacity=0.10, fill_color=AMBER,
                         stroke_color=CYAN, stroke_width=2)
        closure.set_shade_in_3d(True)
        trace = ParametricFunction(
            lambda t: np.array([3.4 * np.cos(t), 0.25 * np.sin(t * 2), -0.9]),
            t_range=[0, TAU], color="#3A5870", stroke_width=1.5,
        )
        line5 = caption("Glue the boundary: the total space closes as S⁶.", "#BDF6E0")
        self.add_fixed_in_frame_mobjects(line5)
        self.play(ReplacementTransform(line4, line5), Create(trace), run_time=0.55)
        self.wait(0.35)
        self.play(FadeOut(fibre), FadeIn(closure), run_time=1.25)
        self.play(Indicate(closure, color=CYAN, scale_factor=1.08), run_time=0.8)
        self.wait(1.5)
