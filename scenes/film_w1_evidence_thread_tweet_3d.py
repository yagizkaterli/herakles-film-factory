from manim import *


class W1EvidenceThreadTweet(Scene):
    def construct(self):
        self.camera.background_color = "#05070A"
        header = Text("SOURCE-BOUND FILM / S⁶", font_size=15, color="#8EA8B8").to_edge(UP, buff=0.22)
        self.add(header)

        def cap(text, color="#F2F7FA"):
            bar = RoundedRectangle(corner_radius=0.12, width=11.8, height=0.58, stroke_width=0,
                                   fill_color="#020409", fill_opacity=0.9).to_edge(DOWN, buff=0.18)
            label = Text(text, font_size=17, color=color, weight=BOLD).move_to(bar)
            g = VGroup(bar, label)
            self.add_fixed_in_frame_mobjects(g)
            return g

        source = RoundedRectangle(corner_radius=0.08, width=1.55, height=2.15, color="#F4C77B",
                                  fill_color="#47371C", fill_opacity=0.85).move_to([-4.7, 0.25, 0])
        source_lines = VGroup(*[Line([-0.45, y, 0], [0.45, y, 0], color="#F4C77B", stroke_width=2)
                                for y in [0.75, 0.45, 0.15, -0.15, -0.45]]).move_to(source)
        stream = CubicBezier([-3.8, 0.25, 0], [-2.5, 1.1, 0], [-1.4, -1.0, 0], [0.0, 0.0, 0], color="#F8D89A", stroke_width=4)
        line1 = cap("A paper makes a claim.", "#F4C77B")
        self.play(FadeIn(source), Create(source_lines), FadeIn(line1), run_time=0.9)
        self.play(Create(stream), run_time=1.3)
        line2 = cap("Source → trace", "#F8D89A")
        self.play(ReplacementTransform(line1, line2), run_time=0.5)

        capsule = RoundedRectangle(corner_radius=0.18, width=2.9, height=2.5, color="#7DE7FF",
                                   fill_color="#0B2530", fill_opacity=0.35, stroke_width=4).move_to([0.5, 0, 0])
        capsule_glow = Circle(radius=0.65, color="#7DE7FF", stroke_width=2).move_to(capsule)
        line3 = cap("Context is not consensus.", "#7DE7FF")
        self.play(FadeIn(capsule), FadeIn(capsule_glow), ReplacementTransform(line2, line3), run_time=0.9)

        tori = VGroup(*[
            Ellipse(width=1.15 + i * 0.15, height=0.58 + i * 0.08, color="#B9F3FF", stroke_width=3)
            .move_to([0.5 + i * 0.45, 0.0, 0])
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(t) for t in tori], lag_ratio=0.18), run_time=1.1)
        line4 = cap("A smooth family reaches one cusp.", "#B9F3FF")
        self.play(ReplacementTransform(line3, line4), run_time=0.55)

        cusp = Circle(radius=0.72, color="#FFC45C", stroke_width=5).move_to([3.4, 0, 0])
        hexagon = RegularPolygon(n=6, radius=0.9, color="#FFC45C", stroke_width=4).rotate(PI / 6).move_to([3.4, 0, 0])
        self.play(FadeOut(tori), FadeOut(capsule_glow), FadeOut(capsule), FadeIn(cusp), run_time=0.8)
        self.play(Transform(cusp, hexagon), run_time=1.4)

        receipt = RoundedRectangle(corner_radius=0.1, width=2.2, height=1.35, color="#9BE7B1",
                                   fill_color="#173B2A", fill_opacity=0.85, stroke_width=4).move_to([5.3, 0, 0])
        receipt_mark = Text("RECEIPT", font_size=15, color="#9BE7B1").move_to(receipt)
        close_stream = Line([4.25, 0, 0], [4.2, 0, 0], color="#9BE7B1", stroke_width=4)
        line5 = cap("The paper claims yes; the receipt bounds the story.", "#BDF6E0")
        self.play(FadeIn(receipt), FadeIn(receipt_mark), Create(close_stream), ReplacementTransform(line4, line5), run_time=0.9)
        self.wait(1.4)
