from manim import *


class EvidenceWorldV1(ThreeDScene):
    """Evidence-world film: trace excavation -> capsule -> falsifier -> world state."""

    def construct(self):
        self.camera.background_color = "#05080D"
        self.set_camera_orientation(phi=68 * DEGREES, theta=-58 * DEGREES, focal_distance=20)

        title = Text("A TRACE BECOMES A WORLD", font="DejaVu Sans Mono", font_size=28,
                     color="#E8E2D7", weight=BOLD)
        title.to_edge(UP, buff=.22)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=.45)

        terrain = VGroup()
        for x in range(-6, 7, 2):
            for z in range(-4, 5, 2):
                h = .12 + ((x * 3 + z * 5) % 4) * .055
                tile = Prism(dimensions=[1.72, h, 1.5], fill_color="#111A20",
                             fill_opacity=.98, stroke_color="#263D43", stroke_width=1)
                tile.move_to([x, -0.42 + h / 2, z])
                terrain.add(tile)
        self.play(LaggedStart(*[FadeIn(t, shift=0.12 * UP) for t in terrain],
                              lag_ratio=.018), run_time=1.2)

        # Act 1: amber intake basin and trace fragments.
        basin = Cylinder(radius=1.18, height=.12, direction=UP, resolution=32,
                         fill_color="#3A2412", fill_opacity=.98, stroke_color="#D7923D", stroke_width=2)
        basin.move_to([-4.3, .05, 0])
        ember = Sphere(radius=.22, resolution=(16, 10), fill_color="#F0A94B",
                       stroke_color="#FFE7AE", stroke_width=2).move_to([-4.3, .34, 0])
        amber_ring = Torus(major_radius=.74, minor_radius=.025, color="#F0A94B").move_to([-4.3, .20, 0])
        self.play(FadeIn(basin), GrowFromCenter(ember), Create(amber_ring), run_time=.7)

        trace_label = Text("TRACE", font="DejaVu Sans Mono", font_size=15, color="#F0BC67")
        trace_label.to_edge(LEFT, buff=.25).shift(DOWN * .92)
        self.add_fixed_in_frame_mobjects(trace_label)
        self.play(Write(trace_label), run_time=.35)

        fragments = VGroup(*[
            Sphere(radius=.07 + i * .01, resolution=(10, 6), fill_color="#D88B39",
                   stroke_color="#FFE0A2", stroke_width=1).move_to([-4.3 + .25 * i, .5 + .06 * (i % 2), -.2 + .12 * i])
            for i in range(5)
        ])
        self.play(LaggedStart(*[MoveAlongPath(f, Line(f.get_center(), [-1.55, .38, .08 * i]))
                                for i, f in enumerate(fragments)], lag_ratio=.08), run_time=1.0)

        # Act 2: context capsule.
        capsule = Prism(dimensions=[1.55, 2.15, 1.35], fill_color="#8EDCFF", fill_opacity=.13,
                        stroke_color="#C9F4FF", stroke_width=2)
        capsule.move_to([-1.0, .8, 0])
        capsule_core = Octahedron(radius=.48, fill_color="#BDEFFF", fill_opacity=.36,
                                  stroke_color="#E9FCFF", stroke_width=2).move_to([-1.0, .8, 0])
        capsule_ring = Torus(major_radius=.59, minor_radius=.022, color="#9BE9FF").rotate(PI / 2, axis=RIGHT).move_to([-1.0, .8, 0])
        self.play(FadeIn(capsule), GrowFromCenter(capsule_core), Create(capsule_ring), run_time=.8)
        capsule_label = Text("CAPSULE", font="DejaVu Sans Mono", font_size=15, color="#AEEBFF")
        capsule_label.to_edge(DOWN, buff=.72).shift(LEFT * 1.25)
        self.add_fixed_in_frame_mobjects(capsule_label)
        self.play(Write(capsule_label), run_time=.35)

        # Act 3: falsifier gate; one stream is visibly rejected.
        gate = Torus(major_radius=.82, minor_radius=.055, color="#66E4FF").rotate(PI / 2, axis=RIGHT)
        gate.move_to([1.42, .8, 0])
        gate_inner = Sphere(radius=.13, fill_color="#75E7FF", stroke_color="#E9FFFF", stroke_width=2).move_to([1.42, .8, 0])
        self.play(Create(gate), GrowFromCenter(gate_inner), run_time=.55)
        gate_label = Text("FALSIFIER", font="DejaVu Sans Mono", font_size=15, color="#75E7FF")
        gate_label.to_edge(DOWN, buff=.72).shift(RIGHT * 1.1)
        self.add_fixed_in_frame_mobjects(gate_label)
        self.play(Write(gate_label), run_time=.35)

        rejected = DashedLine([-1.0, .8, .15], [1.42, .8, .15], color="#F06A5B", dash_length=.12, stroke_width=3)
        accepted = Line([-.75, .8, -.15], [1.42, .8, -.15], color="#8FE9FF", stroke_width=5)
        self.play(Create(rejected), run_time=.45)
        self.play(Create(accepted), run_time=.55)
        self.play(rejected.animate.set_opacity(.18), run_time=.25)

        # Act 4: signed receipt bridge into a living network.
        receipt = Prism(dimensions=[1.42, .34, 1.02], fill_color="#163B3B", fill_opacity=.95,
                        stroke_color="#B9F3CB", stroke_width=3).move_to([3.85, .52, 0])
        receipt_mark = Sphere(radius=.15, fill_color="#B9F3CB", stroke_color="#F2FFF6", stroke_width=2).move_to([3.85, .76, 0])
        bridge = Line([1.42, .65, -.15], [3.15, .65, -.15], color="#B9F3CB", stroke_width=6)
        self.play(Create(bridge), FadeIn(receipt), GrowFromCenter(receipt_mark), run_time=.8)
        receipt_label = Text("RECEIPT", font="DejaVu Sans Mono", font_size=15, color="#B9F3CB")
        receipt_label.to_edge(RIGHT, buff=.28).shift(DOWN * .92)
        self.add_fixed_in_frame_mobjects(receipt_label)
        self.play(Write(receipt_label), run_time=.35)

        islands = VGroup()
        for i, p in enumerate([(4.9, 1.35, -1.1), (5.5, 1.0, 1.2), (4.9, .92, 2.7), (3.8, 1.0, 2.35)]):
            island = Sphere(radius=.18 + .03 * (i % 2), fill_color="#62D9E8",
                            stroke_color="#D6FBFF", stroke_width=1).move_to(p)
            islands.add(island)
            self.play(GrowFromCenter(island), run_time=.18)
        for a, b in zip(islands[:-1], islands[1:]):
            self.play(Create(Line(a.get_center(), b.get_center(), color="#4DAAB8", stroke_width=2)), run_time=.2)

        footer = Text("TRACE  →  CAPSULE  →  FALSIFIER  →  RECEIPT  →  WORLD STATE",
                      font="DejaVu Sans Mono", font_size=16, color="#E8E2D7")
        footer.to_edge(DOWN, buff=.22)
        self.add_fixed_in_frame_mobjects(footer)
        self.play(Write(footer), run_time=.65)
        self.wait(1.2)
