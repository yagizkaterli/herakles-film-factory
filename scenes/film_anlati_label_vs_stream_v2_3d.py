from manim import *


class AnlatiLabelVsStreamV2(ThreeDScene):
    """Prior-art-derived redesign: explicit state transitions and one contradiction."""

    def construct(self):
        self.camera.background_color = "#05070B"
        self.set_camera_orientation(phi=70 * DEGREES, theta=-58 * DEGREES, focal_distance=20)

        title = Text("THE LABEL SAID RUNNING", font="DejaVu Sans Mono", font_size=27, color="#F2F5F7", weight=BOLD)
        title.to_edge(UP, buff=.22); self.add_fixed_in_frame_mobjects(title); self.play(FadeIn(title), run_time=.4)

        # Persistent isometric evidence slab (Narrowest Range grammar seed).
        slab = Prism(dimensions=[8.5, .18, 3.4], fill_color="#0D1B25", fill_opacity=.95, stroke_color="#1E4B68", stroke_width=2)
        slab.move_to([0, -.55, 0]); self.add(slab); self.play(FadeIn(slab), run_time=.45)
        for x in range(-4, 5):
            self.add(Line([x, -.43, -1.5], [x, -.43, 1.5], color="#163447", stroke_width=1))
        for z in [-1, 0, 1]:
            self.add(Line([-4.2, -.43, z], [4.2, -.43, z], color="#163447", stroke_width=1))

        # State 1: a label with no visible stream evidence.
        label_box = Prism(dimensions=[2.3, .3, 1.25], fill_color="#153A2C", stroke_color="#7CE0B0", stroke_width=2)
        label_box.move_to([-2.9, .25, .35])
        label = Text("RUNNING", font="DejaVu Sans Mono", font_size=19, color="#7CE0B0", weight=BOLD)
        label.to_edge(LEFT, buff=.35).shift(DOWN * 1.05)
        self.add(label_box); self.add_fixed_in_frame_mobjects(label); self.play(FadeIn(label_box), Write(label), run_time=.55)

        # State 2: persistent stream lane appears as measured time, not decorative dots.
        lane = Line([-1.8, .05, -.35], [3.7, .05, -.35], color="#79C9E8", stroke_width=4)
        ticks = VGroup(*[Line([x, -.05, -.35], [x, .15, -.35], color="#79C9E8", stroke_width=2) for x in [-1.7,-.7,.3,1.3,2.3,3.3]])
        time_label = Text("last observed event · 23 AUG · 02:14", font="DejaVu Sans Mono", font_size=12, color="#9FD7EC")
        time_label.to_edge(DOWN, buff=.55)
        self.add_fixed_in_frame_mobjects(time_label)
        self.play(Create(lane), LaggedStart(*[Create(t) for t in ticks], lag_ratio=.08), Write(time_label), run_time=.9)

        # State 3: one source-bound red point, then surface contradiction.
        point = Sphere(radius=.22, resolution=(12, 8), fill_color="#FF5060", stroke_color="#FFE0E3", stroke_width=2)
        point.move_to([1.3, .18, .05])
        source_tag = Text("model=<synthetic> · output_tokens=0", font="DejaVu Sans Mono", font_size=13, color="#FF8A93")
        source_tag.to_edge(RIGHT, buff=.3).shift(DOWN * 1.02)
        self.add_fixed_in_frame_mobjects(source_tag)
        self.play(GrowFromCenter(point), Write(source_tag), run_time=.55)

        crack = VGroup(
            Line([-1.2, .05, .03], [.8, .05, .03], color="#FF5060", stroke_width=3),
            Line([1.8, .05, .03], [3.7, .05, .03], color="#FF5060", stroke_width=3),
            Line([.8, .05, .03], [1.3, .55, .04], color="#FF5060", stroke_width=3),
            Line([1.3, .55, .04], [1.8, .05, .03], color="#FF5060", stroke_width=3),
        )
        self.play(Create(crack), run_time=.7)
        verdict = Text("LABEL ≠ STREAM", font="DejaVu Sans Mono", font_size=23, color="#FF6672", weight=BOLD)
        verdict.to_edge(DOWN, buff=.12); self.add_fixed_in_frame_mobjects(verdict); self.play(Write(verdict), run_time=.55)

        stamp = Text("one move · source-bound contradiction · receipt pending", font="DejaVu Sans Mono", font_size=9, color="#60798A")
        stamp.to_edge(UP, buff=.04); self.add_fixed_in_frame_mobjects(stamp); self.wait(1.0)
