from manim import *

BG = "#0B0D10"
INK = "#E8E2D7"
AMBER = "#E7B86A"
MINT = "#B7F0CD"
SLATE = "#778492"


class TraceIntake(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("TRACE", font="DejaVu Sans Mono", font_size=28, color=AMBER, weight=BOLD).to_edge(UP, buff=.35)
        source = Dot(LEFT * 4, radius=.16, color=AMBER)
        target = RoundedRectangle(width=2.6, height=1.1, corner_radius=.06, stroke_color=INK, stroke_width=2, fill_color="#141A1E", fill_opacity=1).move_to(RIGHT * 2.7)
        label = Text("work", font="DejaVu Sans Mono", font_size=21, color=INK).move_to(target.get_center())
        path = CubicBezier(source.get_center(), LEFT * 1.2 + UP * .8, RIGHT * .5 + DOWN * .7, target.get_left())
        path.set_stroke(AMBER, width=5)
        self.add(title, source, target, label)
        self.play(Create(path), run_time=.8)
        self.play(MoveAlongPath(source.copy(), path), run_time=1.0)
        self.wait(.8)


class QuestionHold(Scene):
    def construct(self):
        self.camera.background_color = BG
        q = Text("WHAT CHANGES NEXT?", font="DejaVu Sans Mono", font_size=29, color=INK, weight=BOLD)
        q.move_to(UP * .65)
        line = Line(LEFT * 3.7, RIGHT * 3.7, color=SLATE, stroke_width=2)
        mark = Dot(LEFT * 2.6, radius=.13, color=AMBER)
        end = Dot(RIGHT * 2.6, radius=.13, color=SLATE)
        caption = Text("hold the question", font="DejaVu Sans Mono", font_size=15, color=SLATE).move_to(DOWN * .8)
        self.add(q, line, mark, end, caption)
        self.play(FadeIn(q), FadeIn(line), FadeIn(mark), FadeIn(end), FadeIn(caption), run_time=.7)
        self.wait(1.8)


class ReceiptReturn(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("RECEIPT", font="DejaVu Sans Mono", font_size=27, color=MINT, weight=BOLD).to_edge(UP, buff=.35)
        card = RoundedRectangle(width=3.2, height=1.45, corner_radius=.06, stroke_color=MINT, stroke_width=2, fill_color="#122019", fill_opacity=1)
        card.move_to(ORIGIN)
        check = Text("✓", font="DejaVu Sans", font_size=46, color=MINT).move_to(card.get_center() + LEFT * .9)
        text = Text("verified", font="DejaVu Sans Mono", font_size=20, color=INK).move_to(card.get_center() + RIGHT * .55)
        source = Text("same object · same source", font="DejaVu Sans Mono", font_size=13, color=SLATE).to_edge(DOWN, buff=.45)
        self.add(title, card, check, text, source)
        self.play(GrowFromCenter(card), Write(check), Write(text), FadeIn(source), run_time=1.0)
        self.wait(1.0)


class WorldLink(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("WORLD LINK", font="DejaVu Sans Mono", font_size=27, color=MINT, weight=BOLD).to_edge(UP, buff=.35)
        film = RoundedRectangle(width=2.4, height=1.0, corner_radius=.06, stroke_color=AMBER, stroke_width=2, fill_color="#181713", fill_opacity=1).move_to(LEFT * 2.8)
        world = RoundedRectangle(width=2.8, height=1.25, corner_radius=.06, stroke_color=MINT, stroke_width=2, fill_color="#122019", fill_opacity=1).move_to(RIGHT * 2.6)
        a = Text("film", font="DejaVu Sans Mono", font_size=20, color=AMBER).move_to(film.get_center())
        b = Text("HERAKLES\nWORLD", font="DejaVu Sans Mono", font_size=18, color=MINT, line_spacing=.8).move_to(world.get_center())
        link = Arrow(film.get_right(), world.get_left(), buff=.18, color=INK, stroke_width=3)
        note = Text("pointer, not a canonical write", font="DejaVu Sans Mono", font_size=13, color=SLATE).to_edge(DOWN, buff=.45)
        self.add(title, film, world, a, b, note)
        self.play(Create(link), run_time=.7)
        self.play(FadeIn(note), run_time=.5)
        self.wait(1.0)
