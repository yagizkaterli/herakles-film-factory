from manim import *

# HTERM · TERNMANAGER — iki yuzey, tek kanit (fabrika ev stili: koyu zemin, mono,
# 854x480@15 konvansiyonu ile -ql render edilir).
# Icerik OLCULMUS yuzeylerden gelir: hterm posta sozlesmesi (jeton + ack zinciri)
# ve ternmanager PENCERE katmani (defter, canli/olu, budama, makine yuzeyi).
BG = "#070A0F"
INK = "#E8E2D7"
DIM = "#9BA7B4"
CYAN = "#86D8FF"
GREEN = "#6EE7A8"
RED = "#FF6B6B"
AMBER = "#F5C86B"
SLAB = "#243447"


def mono(s, size=13, color=INK, weight=NORMAL):
    return Text(s, font="DejaVu Sans Mono", font_size=size, color=color, weight=weight)


class HtermTernmanagerV1(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ---------------- I. BASLIK ----------------
        title = mono("HTERM · TERNMANAGER", 34, INK, BOLD)
        sub = mono("iki yuzey · tek kanit · uyeler bunu ogrenir", 14, DIM)
        title.to_edge(UP, buff=0.45)
        sub.next_to(title, DOWN, buff=0.12)
        stamp = mono("HERAKLES · 07 Eki 2026 · receipts own truth", 10, "#778492")
        stamp.to_edge(DOWN, buff=0.18)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.3)
        self.add(stamp)
        bar = Line([-5.6, 0.55, 0], [5.6, 0.55, 0], color=CYAN, stroke_width=3)
        self.play(Create(bar), run_time=0.4)
        self.wait(0.7)
        self.play(FadeOut(sub), FadeOut(stamp), bar.animate.set_opacity(0.25), run_time=0.4)

        # ---------------- II. POSTA (.hterm) ----------------
        p_head = mono(".hterm · POSTA  (pane'e adresli mektup + jeton + ack)", 16, CYAN, BOLD)
        p_head.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(p_head), run_time=0.4)

        pane = mono("hedef: herdr:wH:pF  (tur=herdr-pane)", 11, INK)
        pane.next_to(p_head, DOWN, buff=0.3)
        self.play(FadeIn(pane), run_time=0.3)

        env = RoundedRectangle(width=4.5, height=1.5, corner_radius=0.12,
                               stroke_color=CYAN, stroke_width=1.6).set_fill(SLAB, 0.85)
        env.next_to(pane, DOWN, buff=0.35).shift(LEFT * 3.0)
        env_l = VGroup(
            mono("govde.schema = kapsul-v2", 9, INK),
            mono("iddia + falsifier + kanit_yolu", 9, DIM),
            mono("jeton-hterm-...-1", 9, AMBER),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.09).move_to(env)
        self.play(FadeIn(env), FadeIn(env_l), run_time=0.5)

        p1 = mono("idle|done  ->  pane send-text", 10, GREEN)
        p2 = mono("working|unknown  ->  posta-kutu + jeton", 10, AMBER)
        paths = VGroup(p1, p2).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        paths.next_to(env, RIGHT, buff=0.5)
        self.play(Write(p1), run_time=0.5)
        self.play(Write(p2), run_time=0.5)

        acks = VGroup(
            mono("issued", 9, CYAN), mono("received", 9, CYAN),
            mono("completed", 9, GREEN), mono("failed", 9, RED),
        ).arrange(RIGHT, buff=0.22)
        acks.next_to(env, DOWN, buff=0.4)
        arrows = VGroup(*[
            Arrow(acks[i].get_right(), acks[i + 1].get_left(), buff=0.05,
                  stroke_width=1.4, color=DIM, max_tip_length_to_length_ratio=0.18)
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(a) for a in acks], lag_ratio=0.15), run_time=0.7)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.2), run_time=0.6)
        ack_note = mono("ack: hterm --terminal-ack <id> received|completed|failed herdr:<pane>", 9, DIM)
        ack_note.next_to(acks, DOWN, buff=0.25)
        self.play(FadeIn(ack_note), run_time=0.35)
        self.wait(0.8)
        self.play(FadeOut(VGroup(p_head, pane, env, env_l, paths, acks, arrows, ack_note)), run_time=0.5)

        # ---------------- III. TERNMANAGER ----------------
        t_head = mono(".ternmanager · PENCERE katmani (headless tern)", 16, CYAN, BOLD)
        t_head.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(t_head), run_time=0.4)

        panel = Rectangle(width=7.6, height=3.5, stroke_color=SLAB, stroke_width=1.5)
        panel.set_fill("#0B1016", 0.9).next_to(t_head, DOWN, buff=0.3)
        lines = VGroup(
            mono("1 pencere (1 canli / 0 olu) · 1 pane · 11 oturum · 0 harici", 10, INK),
            mono("defter /root/.herakles/pencere/defter.json", 9, DIM),
            mono("PENCERELER (headless)", 10, INK, BOLD),
            mono("> ● pencere-birim1-koordinator · pane=1 160x45 · pid=2702433", 9, GREEN),
            mono("  ○ bayat-ornek · pane=0 - · OLCUMEDI", 9, RED),
            mono("OTURUMLAR (tern daemon) · 11", 10, INK, BOLD),
            mono("HARICI (tmux, TERN oncesi) · 0", 10, INK, BOLD),
            mono("n ac · x kapat (olu kaydi budar) · b bol · s shot", 9, DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.11).move_to(panel).shift(DOWN * 0.05)
        self.play(FadeIn(panel), run_time=0.4)
        for ln in lines:
            self.play(FadeIn(ln, shift=UP * 0.06), run_time=0.22)
        dead = lines[4]
        self.play(Indicate(dead, color=RED, scale_factor=1.03), run_time=0.7)

        xkey = mono("[x]  budar: soket + defter kaydi duser", 10, RED)
        xkey.next_to(panel, DOWN, buff=0.28)
        self.play(Write(xkey), run_time=0.5)

        makine = mono("makine yuzeyi: --json --pencere ozet{pencere,canli,olu,pane,oturum,harici}", 9, CYAN)
        makine.next_to(xkey, DOWN, buff=0.14)
        dokum = mono("kanit yuzeyi: --pencere-dokum  (gercek render, sentetik veri yok)", 9, CYAN)
        dokum.next_to(makine, DOWN, buff=0.1)
        self.play(FadeIn(makine), run_time=0.4)
        self.play(FadeIn(dokum), run_time=0.4)
        self.wait(0.9)
        self.play(FadeOut(VGroup(t_head, panel, lines, xkey, makine, dokum)), run_time=0.5)

        # ---------------- IV. KANIT / KAPANIS ----------------
        k_head = mono("KANIT ZINCIRI", 18, INK, BOLD)
        k_head.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(k_head), run_time=0.35)

        caps = VGroup(
            mono("HRK-TERNMANAGER-UI-UX-20261007", 9, DIM),
            mono("HRK-TERNMANAGER-OLU-BUDAMA-20261007", 9, DIM),
            mono("HRK-TERNMANAGER-MAKINE-YUZEYI-20261007", 9, DIM),
            mono("HRK-TERNMANAGER-PENCERE-KATMANI-20261007", 9, DIM),
            mono("HRK-HTERM-TERNMANAGER-FILM-20261007", 9, INK, BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.13).next_to(k_head, DOWN, buff=0.3)

        chain_h = mono("olcum -> capsule -> hff -> png -> receipt (sha256)", 10, CYAN)
        chain_h.next_to(caps, DOWN, buff=0.35)
        bead = Dot(color=GREEN, radius=0.07).next_to(chain_h, LEFT, buff=0.25)
        for c in caps:
            self.play(FadeIn(c), run_time=0.18)
        self.play(FadeIn(chain_h), FadeIn(bead), run_time=0.4)
        self.play(bead.animate.next_to(chain_h, RIGHT, buff=0.25), run_time=0.7)

        final = mono("OGRENME: film + kapsul + makbuz ayni agacta; iddia kanitsiz yazilmaz", 10, AMBER)
        final.next_to(chain_h, DOWN, buff=0.3)
        self.play(Write(final), run_time=0.7)
        self.wait(1.2)
