from manim import *


class CTXC05Gate(Scene):
    def construct(self):
        self.camera.background_color = "#050816"
        title = Text("CONTEXT CAPSULE / FAIL-CLOSED", font_size=18, color="#B9C8D8").to_edge(UP, buff=0.25)
        self.add(title)

        gate = RoundedRectangle(corner_radius=0.15, width=2.0, height=4.2, color="#F2B84B", stroke_width=5)
        gate.move_to([2.7, 0, 0])
        gate_label = Text("RENDER", font_size=16, color="#F2B84B").next_to(gate, UP, buff=0.18)
        self.play(Create(gate), FadeIn(gate_label), run_time=0.8)

        missing_box = RoundedRectangle(corner_radius=0.18, width=2.6, height=1.0, color="#F25F5C", stroke_width=4)
        missing_mark = Text("?", font_size=34, color="#F25F5C").move_to(missing_box)
        missing = VGroup(missing_box, missing_mark)
        missing.move_to([-3.1, 0.7, 0])
        warning = Text("MISSING CONTEXT  ·  STOP", font_size=15, color="#F25F5C").to_edge(DOWN, buff=0.3)
        self.add(warning)
        self.play(FadeIn(missing), run_time=0.5)
        self.play(missing.animate.shift(RIGHT * 1.8), run_time=0.7)
        self.play(missing.animate.shift(LEFT * 1.8), rate_func=rush_from, run_time=0.65)
        self.play(FadeOut(missing), FadeOut(warning), run_time=0.4)

        capsule_box = RoundedRectangle(corner_radius=0.18, width=2.6, height=1.0, color="#69D2E7", stroke_width=4)
        capsule_mark = Text("CTX", font_size=18, color="#69D2E7").move_to(capsule_box)
        capsule = VGroup(capsule_box, capsule_mark)
        capsule.move_to([-3.1, -0.5, 0])
        ok = Text("COMPLETE CAPSULE  ·  PASS", font_size=15, color="#9BE7B1").to_edge(DOWN, buff=0.3)
        self.add(ok)
        self.play(FadeIn(capsule), run_time=0.5)
        self.play(capsule.animate.move_to([2.7, -0.5, 0]), run_time=1.5)
        result = RoundedRectangle(corner_radius=0.12, width=2.2, height=1.5, color="#9BE7B1", fill_color="#173B2A", fill_opacity=0.9, stroke_width=4)
        result_text = Text("RENDERED", font_size=17, color="#9BE7B1").move_to(result)
        self.play(ReplacementTransform(capsule, result), FadeIn(result_text), run_time=0.8)
        self.wait(1.2)
