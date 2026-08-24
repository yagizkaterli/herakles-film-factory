from manim import *


class CTXC06ContextEventDecision(Scene):
    def construct(self):
        self.camera.background_color = "#050816"
        title = Text("CONTEXT  →  EVENT  →  DECISION", font_size=20, color="#D8E6F3").to_edge(UP, buff=0.25)
        self.add(title)

        files = VGroup(*[
            RoundedRectangle(corner_radius=0.08, width=1.75, height=0.42, color="#7A91A8", stroke_width=2)
            for _ in range(5)
        ]).arrange(DOWN, buff=0.10).move_to([-4.7, 0, 0])
        file_words = VGroup(*[Text("file", font_size=11, color="#AFC2D4") for _ in range(5)])
        for word, box in zip(file_words, files):
            word.move_to(box)
        source = VGroup(files, file_words)
        source_label = Text("raw inputs", font_size=14, color="#9DB0C2").next_to(source, DOWN, buff=0.25)
        self.play(LaggedStart(*[FadeIn(x) for x in files], lag_ratio=0.1), FadeIn(file_words), FadeIn(source_label), run_time=0.9)

        capsule = RoundedRectangle(corner_radius=0.22, width=2.5, height=2.1, color="#69D2E7", fill_color="#0D2834", fill_opacity=0.9, stroke_width=4).move_to([-1.6, 0, 0])
        cap_label = Text("CONTEXT\nCAPSULE", font_size=16, color="#69D2E7", line_spacing=0.9).move_to(capsule)
        arrow1 = Arrow([-3.7, 0, 0], [-2.85, 0, 0], color="#69D2E7", stroke_width=4)
        self.play(Create(arrow1), FadeIn(capsule), FadeIn(cap_label), run_time=0.9)

        event = Circle(radius=0.95, color="#F2B84B", fill_color="#3A2B0C", fill_opacity=0.9, stroke_width=4).move_to([1.4, 0, 0])
        event_label = Text("EVENT", font_size=16, color="#F2B84B").move_to(event)
        arrow2 = Arrow([-0.25, 0, 0], [0.4, 0, 0], color="#F2B84B", stroke_width=4)
        self.play(Create(arrow2), FadeIn(event), FadeIn(event_label), run_time=0.8)

        decision = RegularPolygon(n=4, radius=1.0, color="#9BE7B1", fill_color="#173B2A", fill_opacity=0.9, stroke_width=4).rotate(PI / 4).move_to([4.2, 0, 0])
        decision_label = Text("DECIDE", font_size=15, color="#9BE7B1").move_to(decision)
        arrow3 = Arrow([2.35, 0, 0], [3.2, 0, 0], color="#9BE7B1", stroke_width=4)
        self.play(Create(arrow3), FadeIn(decision), FadeIn(decision_label), run_time=0.8)
        foot = Text("The hero is not a file pile. It is a trace with a next move.", font_size=15, color="#D8E6F3").to_edge(DOWN, buff=0.3)
        self.play(FadeIn(foot), run_time=0.5)
        self.wait(1.5)
