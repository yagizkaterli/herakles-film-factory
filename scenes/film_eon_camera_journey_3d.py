from manim import *


class EonCameraJourney3D(ThreeDScene):
    """Pilot P02: named waypoints and chapter gates, rendered deterministically."""

    def construct(self):
        self.camera.background_color = "#090C12"
        self.set_camera_orientation(phi=64 * DEGREES, theta=-55 * DEGREES, focal_distance=18)

        title = Text("AN EON IS A JOURNEY", font="DejaVu Sans Mono", font_size=28, color="#E8E2D7", weight=BOLD)
        title.to_edge(UP, buff=.25)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=.5)

        slabs = VGroup()
        colors = ["#183027", "#3A2A1A", "#172631", "#24371D"]
        for i, x in enumerate([-4.2, -1.4, 1.4, 4.2]):
            slab = Prism(dimensions=[2.2, .28, 2.1], fill_color=colors[i], fill_opacity=.98,
                         stroke_color="#536B6A", stroke_width=2)
            slab.move_to([x, -.2, 0])
            slabs.add(slab)
        self.play(LaggedStart(*[FadeIn(s) for s in slabs], lag_ratio=.18), run_time=1.0)

        names = ["A0", "R1", "R2", "R5"]
        gates = VGroup()
        for i, name in enumerate(names):
            gate = Torus(major_radius=.42, minor_radius=.08, color="#F0BC67")
            gate.rotate(PI / 2, axis=RIGHT)
            gate.move_to([-4.2 + i * 2.8, .62, 0])
            label = Text(name, font="DejaVu Sans Mono", font_size=14, color="#F0BC67")
            label.to_edge(DOWN, buff=.8).shift(RIGHT * (-4.2 + i * 2.8) * .48)
            gates.add(VGroup(gate, label))
        self.play(LaggedStart(*[FadeIn(g) for g in gates], lag_ratio=.15), run_time=1.0)

        rail = Line([-4.2, .45, 0], [4.2, .45, 0], color="#86D8FF", stroke_width=4)
        self.play(Create(rail), run_time=.8)
        camera_dot = Sphere(radius=.16, fill_color="#86D8FF", stroke_color="#D8F6FF", stroke_width=2)
        camera_dot.move_to([-4.2, .65, 0])
        self.add(camera_dot)

        chapter = Text("chapter waypoint / pause / resume", font="DejaVu Sans Mono", font_size=16, color="#B9F3CB")
        chapter.to_edge(DOWN, buff=.3)
        self.add_fixed_in_frame_mobjects(chapter)
        self.play(Write(chapter), run_time=.5)

        for x in [-1.4, 1.4, 4.2]:
            self.play(camera_dot.animate.move_to([x, .65, 0]), run_time=.7)
            self.wait(.3)

        stamp = Text("P02 · named waypoint manifest · deterministic camera rail", font="DejaVu Sans Mono", font_size=10, color="#778492")
        stamp.to_edge(UP, buff=.05)
        self.add_fixed_in_frame_mobjects(stamp)
        self.wait(1.0)
