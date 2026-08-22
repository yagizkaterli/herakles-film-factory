from manim import *


class ContextlessAgent3D(ThreeDScene):
    """Source-bound first film: no prior chat, only a real task/report surface."""

    def construct(self):
        self.camera.background_color = "#0B0D10"
        self.set_camera_orientation(phi=68 * DEGREES, theta=-48 * DEGREES, focal_distance=18)

        title = Text("CAN A BLANK AGENT FIND THE THREAD?", font="DejaVu Sans Mono", font_size=28, color="#E8E2D7", weight=BOLD)
        title.to_edge(UP, buff=.25)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=.6)

        ground = VGroup()
        for x in range(-5, 6, 2):
            for z in range(-2, 3, 2):
                tile = Prism(dimensions=[1.7, .16, 1.4], fill_color="#15201C", fill_opacity=.92, stroke_color="#2E473C", stroke_width=1)
                tile.move_to([x, -.25, z])
                ground.add(tile)
        self.add(ground)
        self.play(FadeIn(ground), run_time=.5)

        agent = Sphere(radius=.38, resolution=(16, 10), fill_color="#8AD6FF", fill_opacity=.95, stroke_color="#D2F2FF", stroke_width=2)
        agent.move_to([-4.4, .35, 0])
        agent_label = Text("SONNET · no prior chat", font="DejaVu Sans Mono", font_size=14, color="#8AD6FF")
        agent_label.to_edge(LEFT, buff=.25).shift(DOWN * 1.15)
        self.add(agent)
        self.add_fixed_in_frame_mobjects(agent_label)
        self.play(FadeIn(agent), FadeIn(agent_label), run_time=.6)

        card = Prism(dimensions=[2.5, .35, 1.55], fill_color="#302518", fill_opacity=.98, stroke_color="#E7B86A", stroke_width=2)
        card.move_to([-1.5, .35, 0])
        card_label = Text("TASK CARD", font="DejaVu Sans Mono", font_size=18, color="#E7B86A", weight=BOLD)
        card_label.to_edge(LEFT, buff=.25).shift(DOWN * 1.55)
        self.add(card)
        self.add_fixed_in_frame_mobjects(card_label)
        self.play(FadeIn(card), FadeIn(card_label), run_time=.6)

        trace = Line(agent.get_right(), card.get_left(), color="#E7B86A", stroke_width=5)
        self.play(Create(trace), run_time=.7)

        source_nodes = VGroup()
        names = ["PAPER", "DESTAN-YAPI", "OUTPUT", "SOURCE / MEASURED"]
        for i, name in enumerate(names):
            node = Prism(dimensions=[2.25, .26, 1.0], fill_color="#172129", fill_opacity=.98, stroke_color="#8AD6FF", stroke_width=2)
            node.move_to([1.25 + (i % 2) * 2.7, .2, 1.45 - (i // 2) * 2.3])
            source_nodes.add(node)
        self.play(LaggedStart(*[FadeIn(n) for n in source_nodes], lag_ratio=.14), run_time=1.0)

        for node in source_nodes:
            link = Line(card.get_right(), node.get_left(), color="#8AD6FF", stroke_width=2)
            self.play(Create(link), run_time=.25)

        evidence = Text("265 LINES   ·   49 SOURCE   ·   10 MEASURED", font="DejaVu Sans Mono", font_size=17, color="#B7F0CD", weight=BOLD)
        evidence.to_edge(DOWN, buff=.3)
        self.add_fixed_in_frame_mobjects(evidence)
        self.play(Write(evidence), run_time=.55)

        receipt = Prism(dimensions=[2.8, .38, 1.15], fill_color="#153022", fill_opacity=.98, stroke_color="#B7F0CD", stroke_width=3)
        receipt.move_to([4.1, .55, 0])
        receipt_label = Text("REPORT + RECEIPT", font="DejaVu Sans Mono", font_size=17, color="#B7F0CD", weight=BOLD)
        receipt_label.to_edge(RIGHT, buff=.25).shift(DOWN * 1.25)
        self.add(receipt)
        self.add_fixed_in_frame_mobjects(receipt_label)
        self.play(GrowFromCenter(receipt), Write(receipt_label), run_time=.8)

        answer = Text("CONTEXT LIVES IN THE SYSTEM.", font="DejaVu Sans Mono", font_size=24, color="#E8E2D7", weight=BOLD)
        answer.to_edge(DOWN, buff=.3)
        self.add_fixed_in_frame_mobjects(answer)
        self.play(ReplacementTransform(evidence, answer), run_time=.6)

        stamp = Text("source: d-SONNET-DESTAN-D2-B3 · narrative-only · World link pending", font="DejaVu Sans Mono", font_size=10, color="#778492")
        stamp.to_edge(UP, buff=.05)
        self.add_fixed_in_frame_mobjects(stamp)
        self.wait(1.2)

