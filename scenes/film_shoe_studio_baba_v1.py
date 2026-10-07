"""SHOE STUDIO - Babanin Atolyesi (HRK-SHOE-STUDIO-001).

Film Factory sahnesi. Kaptan direktifi M1-M5 (HRK-SHOE-STUDIO-001 kapsulu).
Kurallar:
  - Baba-facing tum para anlatimi TL; USD sembolu ekranda YOK.
  - Tek referans deger: 1 KABUL EDILMIS ayakkabi = 5.000 TL.
  - Maliyet bilesenleri icin gercek veri yok -> UNKNOWN gorunur.
  - Deterministik: rastgelelik yok; veri canonical/SHOE-STUDIO-001-data.v1.json'dan gelir.
Styl: theatrical slapstick cartoon grameri (squash/stretch, iris, conveyor gag,
painted workshop, title cards); telifli karakter kopyasi yok; fotogercekci deepfake yok.
"""

import json
from pathlib import Path

from manim import *

BG = "#0B0D10"
INK = "#E8E2D7"
AMBER = "#E7B86A"
MINT = "#B7F0CD"
SLATE = "#778492"
SKIN = "#E9D3B4"
HAIR = "#C9C9C9"
SHIRT = "#171A1E"
APRON = "#7A5C3E"
RED = "#E4573D"
BELT = "#2A3540"
WOOD = "#4A3A2A"
PANEL = "#10161B"

SOURCE = Path(__file__).resolve().parents[1] / "canonical" / "SHOE-STUDIO-001-data.v1.json"

FALLBACK = {
    "schema": "herakles.shoe-studio-film-source.v1",
    "veri_durumu": "VARSAYILAN-UNKNOWN",
    "tl_referans": 5000,
    "accept_kurali": "1 KABUL EDILMIS AYAKKABI = 5.000 TL",
    "akis": ["SIPARIS", "TASARIM", "KESIM", "DIKIS", "MONTAJ", "BITIRME", "KALITE KAPISI", "KABUL"],
    "shoelaw": [
        {"kural": "KALIP NUMARASI SIPARISLE UYUSMALI", "falsifier": "kalip != siparis numarasi -> RED"},
        {"kural": "DIKIS HATTI SAGLAM OLMALI", "falsifier": "kopuk dikis -> RED"},
        {"kural": "SON KONTROL: BABA ONAYI", "falsifier": "baba onayi yok -> RED"},
    ],
    "soy": [
        "GERCEK INTENT",
        "PCA / TYPED IS GRAFIGI",
        "SINIRLI ISCILER",
        "MAKBUZLAR / TELEMETRI",
        "POLITIKA OGRENME / REPLAY",
        "HERAKLES-SCALE (RUST)",
        "HERAKLES SIM REPLAY KERNEL",
        "EKONOMIK CEKIRDEK",
    ],
    "soy_not": "S2: 5 halka kanitli - substrat herakles-scale - kernel HERAKLES SIM deterministik replay",
    "kpi": {"ad": "MALIYET / KABUL EDILMIS AYAKKABI", "deger": "UNKNOWN", "marj": "UNKNOWN"},
    "maliyet_bilesenleri": {"malzeme": "UNKNOWN", "iscilik": "UNKNOWN", "fire": "UNKNOWN", "compute": "UNKNOWN"},
    "compute_tl": "UNKNOWN - KUR MAKBUZU GELINCE",
    "sahne_metinleri": {},
    "provenance": {"kaptan_kapsul_sha256": "7f3ebb73f44403aa158371fe9e2aa21377fc897b665c42329e2a7ee5c7ce17fe"},
}

T = {
    "title": "BABANIN ATÖLYESİ",
    "subtitle": "bir çift ayakkabı = 5.000 TL",
    "baba1": "Oğlum, kabul edilmiş bir ayakkabı bizim için 5.000 TL değerindedir.",
    "yagiz1": "Her sipariş: niyet -> iş -> doğrulama -> makbuz.",
    "gate_red": "Yanlış numara kalite kapısından geçemez; o ürün kabul edilmez.",
    "kpi_say": "Ölçümüz şu: kabul edilmiş ayakkabı başına maliyet, 5.000 TL'ye karşı.",
    "marj_say": "Oğlum, gerçek veri yok; marj şimdilik UNKNOWN, uydurma rakam yazmayız.",
    "kapanis_say": "Doğru numara, doğru model, kabul edilmiş ürün; oğlum, gerisi zamanla.",
    "compute_say": "Bugünkü hesaplamanın TL karşılığı UNKNOWN; kur makbuzu gelince yazacağız.",
    "order": "SİPARİŞ",
    "order2": "42 numara - kahverengi klasik",
    "order3": "tek kabul: KABUL EDİLMİŞ ürün",
    "fire": "FİRE: UNKNOWN",
    "gate": "KALİTE KAPISI",
    "reject": "RED - KALIP NUMARASI UYUŞMUYOR",
    "accept": "KABUL EDİLDİ",
    "price": "5.000 TL",
    "soy": "ANIL-INVEST-SCALE-001 soyu: aynı mekanik, tek sipariş.",
    "kpi_head": "EKONOMİK ÇEKİRDEK",
    "kpi_cost": "maliyet / KABUL EDİLMİŞ AYAKKABI = UNKNOWN",
    "kpi_margin": "marj (5.000 TL referans) = UNKNOWN",
    "kpi_comp": "bileşenler: malzeme - işçilik - fire - hesaplama = UNKNOWN",
    "compute": "bugünkü hesaplama maliyeti: TL karşılığı KUR MAKBUZU GELİNCE",
    "close1": "Sadece yapmak yetmez.",
    "close2": "Doğru numara - doğru kalite - KABUL EDİLMİŞ ürün.",
    "close3": "Gelir henüz kanıtlı değil - FAIL-CLOSED",
    "close4": "HERAKLES SIM - SHOE STUDIO",
    "future_head": "III. GELECEK - HERAKLES SIM SHOE STUDIO",
    "future_chain": "aynı mekanik: gerçek intent - sınırlı iş grafiği - doğrulama - replay - makbuzlar",
    "future_replay": "REPLAY: AYNI GİRDİ - AYNI ÇIKTI (deterministik)",
    "future_note": "ShoeLaw burada makine kuralı olur; usta gözü kayıtlı kalır.",
}


def load_source():
    try:
        data = json.loads(SOURCE.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("schema") != "herakles.shoe-studio-film-source.v1":
            raise ValueError("schema mismatch")
        for k, v in FALLBACK.items():
            data.setdefault(k, v)
        data["veri_durumu"] = "KANONIK"
        return data
    except Exception:
        data = dict(FALLBACK)
        data["veri_durumu"] = "VARSAYILAN-UNKNOWN"
        return data


class ShoeStudioBabaV1(Scene):
    """Painted workshop + theatrical cartoon gramerinde, TL ekonomisine bagli Shoe Studio filmi."""

    def construct(self):
        self.data = load_source()
        self.camera.background_color = BG

        self.act_title()
        self.act_chapter("I. ATÖLYE", "tezgah, deri, kalıp")
        self.act_workshop_and_figures()
        self.act_order()
        self.act_conveyor()
        self.act_chapter("II. KURAL", "kalite kapısından geçmeyen ayakkabı sayılmaz")
        self.act_quality_gate()
        self.act_scale_chain()
        self.act_economic_kernel()
        self.act_future()
        self.act_close()

    def metin(self, key, default):
        """S4 dilimindeki baba-facing metni (varsa) getirir; yoksa sahne varsayilani."""
        m = self.data.get("sahne_metinleri") or {}
        if isinstance(m, dict):
            val = m.get(key)
            if isinstance(val, str) and val.strip():
                return val
        return default

    # ---------------- helpers ----------------

    def txt(self, s, size=16, color=INK, mono=False, weight=NORMAL):
        return Text(s, font=("DejaVu Sans Mono" if mono else "DejaVu Sans"), font_size=size, color=color, weight=weight)

    def fit(self, mob, max_w):
        if mob.width > max_w:
            mob.scale(max_w / mob.width)
        return mob

    def iris(self, start, end, run_time=0.9):
        tracker = ValueTracker(start)
        ring = always_redraw(
            lambda: Annulus(
                inner_radius=max(tracker.get_value(), 0.02),
                outer_radius=12.0,
                fill_color=BG,
                fill_opacity=1.0,
                stroke_color=INK,
                stroke_width=2,
            )
        )
        self.add(ring)
        self.play(tracker.animate.set_value(end), run_time=run_time)
        self.remove(ring)

    def squish(self, mob, sx=1.12, sy=0.86, rt=0.16):
        self.play(mob.animate.stretch(sx, 0).stretch(sy, 1), run_time=rt)
        self.play(mob.animate.stretch(1 / sx, 0).stretch(1 / sy, 1), run_time=rt)

    def panel(self, w, h, color=AMBER, fill=PANEL, opacity=0.96, sw=3):
        return RoundedRectangle(width=w, height=h, corner_radius=0.14, fill_color=fill, fill_opacity=opacity, stroke_color=color, stroke_width=sw)

    def title_card(self, lines, w=9.6, h=3.0, color=AMBER):
        box = self.panel(w, h, color=color, opacity=0.98, sw=4)
        rows = VGroup()
        for i, line in enumerate(lines):
            rows.add(self.txt(line, size=(30 if i == 0 else 17), color=(color if i == 0 else INK), weight=(BOLD if i == 0 else NORMAL)))
        rows.arrange(DOWN, buff=0.26)
        self.fit(rows, w - 0.9)
        rows.move_to(box.get_center())
        return VGroup(box, rows)

    def bubble(self, text, width=5.0, color=INK, size=15):
        t = self.txt(text, size=size, color=color)
        self.fit(t, width - 0.5)
        box = self.panel(t.width + 0.5, t.height + 0.42, color=color, opacity=0.94, sw=2)
        t.move_to(box.get_center())
        return VGroup(box, t)

    def stamp(self, text, color, size=20, angle=-8):
        t = self.txt(text, size=size, color=color, weight=BOLD)
        box = RoundedRectangle(width=t.width + 0.7, height=t.height + 0.44, corner_radius=0.08, stroke_color=color, stroke_width=4, fill_color=BG, fill_opacity=0.0)
        group = VGroup(box, t)
        group.rotate(angle * DEGREES)
        return group

    def slam(self, mob, rt=0.22):
        self.play(FadeIn(mob, scale=1.7), run_time=rt)

    def figure(self, kind="baba"):
        if kind == "baba":
            skin, hair, shirt, beard = SKIN, HAIR, SHIRT, True
            s = 1.0
        else:
            skin, hair, shirt, beard = "#E3C39A", "#3B2F26", "#2E4A3F", False
            s = 0.92
        head = Circle(radius=0.40, fill_color=skin, fill_opacity=1, stroke_color=INK, stroke_width=2)
        parts = [head]
        if beard:
            jaw = Arc(radius=0.32, start_angle=200 * DEGREES, angle=140 * DEGREES, color=hair, stroke_width=13)
            jaw.move_arc_center_to(head.get_center() + DOWN * 0.05)
            parts.append(jaw)
        crown = Arc(radius=0.40, start_angle=15 * DEGREES, angle=150 * DEGREES, color=hair, stroke_width=11)
        crown.move_arc_center_to(head.get_center())
        parts.append(crown)
        parts.append(Dot(head.get_center() + LEFT * 0.13 + UP * 0.05, radius=0.030, color=INK))
        parts.append(Dot(head.get_center() + RIGHT * 0.13 + UP * 0.05, radius=0.030, color=INK))
        smile = Arc(radius=0.16, start_angle=205 * DEGREES, angle=130 * DEGREES, color=INK, stroke_width=3)
        smile.move_arc_center_to(head.get_center() + DOWN * 0.02)
        parts.append(smile)
        if beard:
            parts.append(RoundedRectangle(width=0.15, height=0.045, corner_radius=0.02, fill_color=hair, fill_opacity=1, stroke_width=0).move_to(head.get_center() + DOWN * 0.07))
        torso = RoundedRectangle(width=0.88, height=0.98, corner_radius=0.22, fill_color=shirt, fill_opacity=1, stroke_color=INK, stroke_width=2)
        torso.next_to(head, DOWN, buff=0.05)
        parts.append(torso)
        if kind != "baba":
            parts.append(Rectangle(width=0.56, height=0.72, fill_color=APRON, fill_opacity=1, stroke_color=INK, stroke_width=1.5).next_to(torso.get_top(), DOWN, buff=0.05))
        arm = RoundedRectangle(width=0.17, height=0.62, corner_radius=0.08, fill_color=shirt, fill_opacity=1, stroke_color=INK, stroke_width=2)
        arm.rotate(-28 * DEGREES).next_to(torso, RIGHT, buff=-0.06).shift(DOWN * 0.16)
        parts.append(arm)
        parts.append(Circle(radius=0.10, fill_color=skin, fill_opacity=1, stroke_color=INK, stroke_width=1.5).move_to(arm.get_bottom() + DOWN * 0.06 + RIGHT * 0.04))
        return VGroup(*parts).scale(s)

    def shoe_piece(self, color=AMBER, scale=1.0):
        sole = RoundedRectangle(width=1.34, height=0.16, corner_radius=0.06, fill_color=WOOD, fill_opacity=1, stroke_color=INK, stroke_width=2)
        upper = Polygon(
            [-0.67, 0.08, 0], [0.16, 0.08, 0], [0.30, 0.34, 0],
            [0.22, 0.54, 0], [-0.40, 0.54, 0], [-0.67, 0.32, 0],
            fill_color=color, fill_opacity=1, stroke_color=INK, stroke_width=2,
        )
        return VGroup(sole, upper).scale(scale)

    def workshop(self):
        floor = Rectangle(width=15.0, height=2.8, fill_color="#0E1216", fill_opacity=1, stroke_width=0)
        floor.move_to(DOWN * 2.6)
        bench = RoundedRectangle(width=13.4, height=0.5, corner_radius=0.06, fill_color=WOOD, fill_opacity=1, stroke_color=INK, stroke_width=2)
        bench.move_to(DOWN * 2.05)
        bench_edge = Line(LEFT * 6.7 + DOWN * 1.80, RIGHT * 6.7 + DOWN * 1.80, color=INK, stroke_width=2)
        shelves = VGroup()
        for sx in (-5.4, 5.4):
            shelf = Rectangle(width=2.4, height=0.09, fill_color=SLATE, fill_opacity=1, stroke_width=0)
            shelf.move_to([sx, 1.30, 0])
            shelves.add(shelf)
            for i in range(5):
                last = self.shoe_piece(color=(AMBER if i % 2 == 0 else SLATE), scale=0.34)
                last.move_to([sx - 0.9 + i * 0.45, 1.50, 0])
                shelves.add(last)
        lamp = VGroup(
            Line([2.2, 4.1, 0], [2.2, 3.1, 0], color=SLATE, stroke_width=3),
            Circle(radius=0.22, fill_color=AMBER, fill_opacity=1, stroke_color=INK, stroke_width=2).move_to([2.2, 2.9, 0]),
            Circle(radius=0.75, fill_color=AMBER, fill_opacity=0.13, stroke_width=0).move_to([2.2, 3.0, 0]),
        )
        window = VGroup(
            Rectangle(width=2.9, height=2.0, fill_color="#0E1418", fill_opacity=1, stroke_color=SLATE, stroke_width=3).move_to([-3.2, 2.3, 0]),
            Line([-3.2, 1.3, 0], [-3.2, 3.3, 0], color=SLATE, stroke_width=3),
            Line([-4.65, 2.3, 0], [-1.75, 2.3, 0], color=SLATE, stroke_width=3),
        )
        return VGroup(floor, bench, bench_edge, shelves, lamp, window)

    # ---------------- acts ----------------

    def chapter(self, text, sub=""):
        """S5 title_card grameri: buyuk harf bolum karti + aksan cizgisi."""
        box = self.panel(8.4, 1.72, color=AMBER, opacity=0.98, sw=3)
        rows = VGroup(self.txt(text, size=25, color=AMBER, weight=BOLD))
        if sub:
            rows.add(self.txt(sub, size=13, color=SLATE))
        rows.arrange(DOWN, buff=0.2)
        self.fit(rows, 7.8)
        rows.move_to(box.get_center())
        line = Line(LEFT * 3.3, RIGHT * 3.3, color=AMBER, stroke_width=3).next_to(box, DOWN, buff=0.2)
        return VGroup(box, rows, line)

    def act_chapter(self, text, sub=""):
        card = self.chapter(text, sub)
        self.play(FadeIn(card, scale=0.97), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(card, shift=UP * 0.2), run_time=0.4)

    def act_title(self):
        self.iris(0.0, 12.0, run_time=0.9)
        card = self.title_card([T["title"], T["subtitle"]])
        self.play(FadeIn(card, scale=0.96), run_time=0.7)
        self.wait(1.2)
        self.play(FadeOut(card, shift=UP * 0.3), run_time=0.5)

    def act_workshop_and_figures(self):
        shop = self.workshop()
        self.play(FadeIn(shop, shift=DOWN * 0.2), run_time=1.1)
        baba = self.figure("baba").move_to(LEFT * 3.1 + DOWN * 0.9)
        yagiz = self.figure("yagiz").move_to(RIGHT * 2.2 + DOWN * 0.85)
        self.play(FadeIn(baba, shift=RIGHT * 0.3), FadeIn(yagiz, shift=LEFT * 0.3), run_time=0.9)
        b1 = self.bubble(self.metin("baba_referans", T["baba1"]), width=7.2, size=14)
        b1.next_to(baba, UP, buff=0.22).shift(RIGHT * 1.1)
        self.play(FadeIn(b1, shift=UP * 0.12), run_time=0.5)
        self.wait(1.6)
        self.squish(baba)
        self.squish(baba, sx=1.08, sy=0.9)
        self.play(FadeOut(b1), run_time=0.35)
        b2 = self.bubble(self.metin("yagiz_kabul", T["yagiz1"]), width=7.4, size=14)
        b2.next_to(yagiz, UP, buff=0.22).shift(LEFT * 1.0)
        self.play(FadeIn(b2, shift=UP * 0.12), run_time=0.5)
        self.wait(1.6)
        self.squish(yagiz, sx=1.07, sy=0.92)
        self.play(FadeOut(b2), run_time=0.35)
        b3 = self.bubble(self.metin("kapi_reddi", T["gate_red"]), width=8.0, size=13, color=RED)
        b3.move_to(DOWN * 3.3)
        self.play(FadeIn(b3, shift=UP * 0.12), run_time=0.5)
        self.wait(1.6)
        self.play(FadeOut(b3), run_time=0.35)
        self.play(FadeOut(baba, shift=LEFT * 2.2), FadeOut(yagiz, shift=RIGHT * 2.2), run_time=0.6)

    def act_order(self):
        card = VGroup()
        box = self.panel(5.8, 2.1, color=AMBER, opacity=1.0, sw=3)
        rows = VGroup(
            self.txt(T["order"], size=23, color=AMBER, weight=BOLD),
            self.txt(T["order2"], size=16),
            self.txt(T["order3"], size=12.5, color=SLATE),
        ).arrange(DOWN, buff=0.2)
        self.fit(rows, 5.2)
        rows.move_to(box.get_center())
        card.add(box, rows)
        card.move_to(UP * 0.4)
        self.play(FadeIn(card, shift=DOWN * 0.5), run_time=0.6)
        st = self.stamp("SIPARIS KAYDI", MINT, size=18)
        st.next_to(card, DOWN, buff=0.3)
        self.slam(st)
        self.wait(0.9)
        self.play(FadeOut(card, shift=UP * 0.4), FadeOut(st), run_time=0.45)

    def act_conveyor(self):
        belt = Rectangle(width=12.2, height=0.55, fill_color=BELT, fill_opacity=1, stroke_color=INK, stroke_width=2).move_to(DOWN * 1.25)
        rollers = VGroup(*[
            Circle(radius=0.15, fill_color="#1B232B", fill_opacity=1, stroke_color=SLATE, stroke_width=2).move_to([-5.6 + 1.6 * i, -1.25, 0])
            for i in range(8)
        ])
        belt_group = VGroup(belt, rollers)
        stations = VGroup()
        for x, name in ((-3.2, "KESIM"), (0.0, "DIKIS"), (3.2, "MONTAJ")):
            lab = self.txt(name, size=15, color=AMBER, weight=BOLD).move_to([x, 0.1, 0])
            tick = Line([x, -0.25, 0], [x, -0.95, 0], color=SLATE, stroke_width=2)
            stations.add(VGroup(lab, tick))
        self.play(FadeIn(belt_group, shift=UP * 0.15), LaggedStart(*[FadeIn(s) for s in stations], lag_ratio=0.15), run_time=1.0)
        piece = self.shoe_piece(color=AMBER, scale=0.8).move_to([-5.0, -0.55, 0])
        self.play(FadeIn(piece, scale=0.7), run_time=0.3)
        self.play(piece.animate.shift(RIGHT * 1.8), Indicate(stations[0][0], color=AMBER), run_time=0.7)
        self.play(piece.animate.shift(RIGHT * 3.2), Indicate(stations[1][0], color=AMBER), run_time=0.7)
        self.squish(piece, sx=1.1, sy=0.92)
        self.play(piece.animate.shift(RIGHT * 3.2), Indicate(stations[2][0], color=AMBER), run_time=0.7)
        bad = self.shoe_piece(color=RED, scale=0.8).move_to([1.4, -0.55, 0])
        self.play(FadeIn(bad, scale=0.7), run_time=0.3)
        self.play(bad.animate.shift(RIGHT * 1.2), run_time=0.5)
        self.play(bad.animate.rotate(-70 * DEGREES).shift(DOWN * 2.1), run_time=0.8)
        fire = self.bubble(T["fire"], width=2.5, color=RED, size=14).move_to([1.6, -2.35, 0])
        self.slam(fire, rt=0.2)
        self.wait(0.9)
        self.play(FadeOut(fire), run_time=0.3)
        self.play(FadeOut(belt_group, shift=DOWN * 0.3), FadeOut(stations), FadeOut(piece), FadeOut(bad), run_time=0.7)

    def act_quality_gate(self):
        gate = self.panel(4.6, 3.0, color=INK, opacity=0.98, sw=3).move_to(DOWN * 0.3)
        head = self.txt(T["gate"], size=18, color=AMBER, weight=BOLD).next_to(gate.get_top(), DOWN, buff=0.16)
        rules = VGroup()
        law = self.data.get("shoelaw") or FALLBACK["shoelaw"]
        for i, item in enumerate(law[:3]):
            rule = item.get("kural") if isinstance(item, dict) else str(item)
            row = self.txt(str(rule)[:38], size=11.5, color=INK)
            self.fit(row, 3.6)
            box = Square(side_length=0.22, stroke_color=SLATE, stroke_width=2).next_to(row, LEFT, buff=0.14)
            rules.add(VGroup(box, row))
        rules.arrange(DOWN, buff=0.22, aligned_edge=LEFT).next_to(head, DOWN, buff=0.18)
        self.play(FadeIn(gate, shift=UP * 0.2), FadeIn(head), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(r) for r in rules], lag_ratio=0.16), run_time=0.7)
        belt = Rectangle(width=12.2, height=0.55, fill_color=BELT, fill_opacity=1, stroke_color=INK, stroke_width=2).move_to(DOWN * 2.5)
        self.play(FadeIn(belt), run_time=0.4)
        wrong = self.shoe_piece(color=SLATE, scale=0.78).move_to(LEFT * 5.0 + DOWN * 1.85)
        self.play(FadeIn(wrong, scale=0.7), run_time=0.3)
        self.play(wrong.animate.shift(RIGHT * 6.0), run_time=1.1)
        self.play(Indicate(rules[0], color=RED, scale_factor=1.15), run_time=0.6)
        say = self.bubble(self.metin("kapi_reddi", T["gate_red"]), width=8.4, size=13, color=RED)
        say.move_to(DOWN * 2.55)
        self.play(FadeIn(say, shift=UP * 0.12), run_time=0.45)
        self.wait(1.5)
        self.play(FadeOut(say), run_time=0.3)
        rej = self.stamp(T["reject"], RED, size=16)
        rej.move_to(DOWN * 0.3)
        self.slam(rej)
        self.wait(0.8)
        self.play(FadeOut(rej), wrong.animate.rotate(-60 * DEGREES).shift(DOWN * 1.2).set_opacity(0.25), run_time=0.7)
        good = self.shoe_piece(color=AMBER, scale=0.8).move_to(LEFT * 5.0 + DOWN * 1.85)
        self.play(FadeIn(good, scale=0.7), run_time=0.3)
        self.play(good.animate.shift(RIGHT * 6.0), run_time=1.1)
        self.play(LaggedStart(*[Indicate(r[0], color=MINT, scale_factor=1.2) for r in rules], lag_ratio=0.3), run_time=1.1)
        acc = self.stamp(T["accept"], MINT, size=22)
        acc.move_to(DOWN * 0.3)
        self.slam(acc)
        tag = self.stamp(T["price"], AMBER, size=24, angle=-6)
        tag.next_to(acc, DOWN, buff=0.35)
        self.slam(tag)
        self.squish(good, sx=1.14, sy=0.9)
        self.wait(1.1)
        self.play(FadeOut(VGroup(gate, head, rules, belt, good, wrong, acc, tag)), run_time=0.7)

    def act_scale_chain(self):
        nodes = list(self.data.get("soy") or FALLBACK["soy"])[:8]
        rows = [nodes[:4], nodes[4:8]]
        blocks = VGroup()
        for r, row in enumerate(rows):
            line = VGroup()
            for i, name in enumerate(row):
                box = self.panel(2.55, 0.95, color=(AMBER if r == 0 else MINT), opacity=0.98, sw=2.5)
                label = self.txt(str(name), size=9.5, color=INK)
                self.fit(label, 2.25)
                label.move_to(box.get_center())
                line.add(VGroup(box, label))
            line.arrange(RIGHT, buff=0.3)
            blocks.add(line)
        blocks.arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        blocks.move_to(UP * 0.55)
        head = self.txt("SCALE MEKANİĞİ - AYNI SİPARİŞTE", size=17, color=AMBER, weight=BOLD)
        head.next_to(blocks, UP, buff=0.42)
        self.play(FadeIn(head), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(b, scale=0.94) for b in blocks], lag_ratio=0.22), run_time=1.4)
        dots = VGroup()
        for b in blocks:
            receipt = Dot(radius=0.07, color=MINT).next_to(b, RIGHT, buff=0.12)
            dots.add(receipt)
        for i, (b, d) in enumerate(zip(blocks, dots)):
            self.play(FadeIn(d, scale=0.5), Indicate(b, color=AMBER, scale_factor=1.06), run_time=0.35)
        note = self.bubble(T["soy"], width=7.0, color=MINT, size=13).next_to(blocks, DOWN, buff=0.4)
        sub = self.txt(str(self.data.get("soy_not") or FALLBACK["soy_not"]), size=11, color=SLATE)
        self.fit(sub, 7.6)
        sub.next_to(note, DOWN, buff=0.22)
        self.play(FadeIn(note, shift=UP * 0.1), FadeIn(sub), run_time=0.5)
        self.wait(1.6)
        self.play(FadeOut(VGroup(head, blocks, dots, note, sub)), run_time=0.6)

    def act_economic_kernel(self):
        tl = self.data.get("tl_referans", 5000)
        big = self.txt("{:,} TL".format(int(tl)).replace(",", "."), size=54, color=AMBER, weight=BOLD)
        big.move_to(LEFT * 3.6 + UP * 0.6)
        big_cap = self.txt(T["price"] + " referans deger", size=13, color=SLATE).next_to(big, DOWN, buff=0.35)
        badge = self.txt("1 KABUL EDILMIS AYAKKABI", size=12, color=MINT).next_to(big_cap, DOWN, buff=0.2)
        box = self.panel(6.6, 3.1, color=INK, opacity=0.98, sw=3).move_to(RIGHT * 2.6)
        head = self.txt(T["kpi_head"], size=17, color=AMBER, weight=BOLD).next_to(box.get_top(), DOWN, buff=0.22)
        kpi = self.data.get("kpi") or FALLBACK["kpi"]
        lines = VGroup(
            self.txt(T["kpi_cost"].replace("UNKNOWN", str(kpi.get("deger", "UNKNOWN"))), size=13.5, color=INK),
            self.txt(T["kpi_margin"].replace("UNKNOWN", str(kpi.get("marj", "UNKNOWN"))), size=13.5, color=INK),
            self.txt(T["kpi_comp"], size=11, color=SLATE),
            self.txt(T["compute"], size=11, color=SLATE),
        )
        for l in lines:
            self.fit(l, 6.0)
        lines.arrange(DOWN, buff=0.24, aligned_edge=LEFT).next_to(head, DOWN, buff=0.22)
        self.play(FadeIn(big, scale=0.9), run_time=0.5)
        self.play(FadeIn(big_cap, shift=UP * 0.1), FadeIn(badge, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(box, shift=UP * 0.2), FadeIn(head), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.12) for l in lines], lag_ratio=0.2), run_time=1.0)
        self.squish(big, sx=1.06, sy=0.94)
        self.wait(0.8)
        say_d = self.bubble(self.metin("kpi_cumlesi", T["kpi_say"]), width=9.4, size=13, color=MINT)
        say_d.move_to(DOWN * 2.7)
        self.play(FadeIn(say_d, shift=UP * 0.12), run_time=0.45)
        self.wait(1.6)
        self.play(FadeOut(say_d), run_time=0.3)
        say_e = self.bubble(self.metin("marj_durustlugu", T["marj_say"]), width=9.4, size=13, color=AMBER)
        say_e.move_to(DOWN * 2.7)
        self.play(FadeIn(say_e, shift=UP * 0.12), run_time=0.45)
        self.wait(1.6)
        self.play(FadeOut(say_e), run_time=0.3)
        self.play(FadeOut(VGroup(big, big_cap, badge, box, head, lines)), run_time=0.7)

    def act_future(self):
        """Gelecek: ayni mekanik SIM Shoe Studio icinde - is grafigi, makbuzlar, deterministik replay."""
        head = self.txt(T["future_head"], size=17, color=AMBER, weight=BOLD)
        head.move_to(UP * 2.9)
        self.play(FadeIn(head, shift=DOWN * 0.15), run_time=0.5)
        steps = list(self.data.get("akis") or FALLBACK["akis"])[:8]
        blocks = VGroup()
        for r, row in enumerate((steps[:4], steps[4:8])):
            line = VGroup()
            for name in row:
                box = self.panel(2.5, 0.82, color=SLATE, opacity=0.98, sw=2)
                label = self.txt(str(name), size=9.5, color=INK)
                self.fit(label, 2.2)
                label.move_to(box.get_center())
                line.add(VGroup(box, label))
            line.arrange(RIGHT, buff=0.28)
            blocks.add(line)
        blocks.arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        blocks.move_to(UP * 0.75)
        self.play(LaggedStart(*[FadeIn(b, scale=0.95) for b in blocks], lag_ratio=0.2), run_time=1.3)
        receipts = VGroup()
        scrub = Dot(radius=0.09, color=MINT)
        scrub.move_to(blocks[0][0].get_bottom() + DOWN * 0.22)
        self.add(scrub)
        for b in blocks:
            for node in b:
                r_dot = Dot(radius=0.06, color=MINT).move_to(node.get_bottom() + DOWN * 0.16)
                receipts.add(r_dot)
                self.play(
                    scrub.animate.move_to(node.get_bottom() + DOWN * 0.22),
                    FadeIn(r_dot, scale=0.5),
                    Indicate(node, color=MINT, scale_factor=1.05),
                    run_time=0.28,
                )
        chain = self.txt(T["future_chain"], size=12, color=SLATE)
        self.fit(chain, 11.0)
        chain.next_to(blocks, DOWN, buff=0.75)
        self.play(FadeIn(chain, shift=UP * 0.1), run_time=0.45)
        replay = self.stamp(T["future_replay"], MINT, size=15, angle=0)
        replay.move_to(DOWN * 2.55)
        self.slam(replay)
        self.wait(1.4)
        note = self.bubble(T["future_note"], width=8.6, size=13, color=AMBER)
        note.move_to(DOWN * 3.35)
        self.play(FadeIn(note, shift=UP * 0.12), run_time=0.45)
        self.wait(1.6)
        self.play(FadeOut(VGroup(head, blocks, receipts, scrub, chain, replay, note)), run_time=0.7)

    def act_close(self):
        son = self.bubble(self.metin("kapanis", T["kapanis_say"]), width=10.8, size=17, color=AMBER)
        son.move_to(UP * 2.4)
        self.play(FadeIn(son, shift=UP * 0.12), run_time=0.5)
        self.wait(1.8)
        self.play(FadeOut(son), run_time=0.35)
        card = VGroup()
        box = self.panel(10.6, 3.4, color=AMBER, opacity=0.98, sw=4)
        rows = VGroup(
            self.txt(T["close1"], size=26, color=AMBER, weight=BOLD),
            self.txt(T["close2"], size=15, color=INK),
            self.txt(T["close3"], size=13, color=RED),
            self.txt(T["close4"], size=13, color=SLATE),
        ).arrange(DOWN, buff=0.24)
        self.fit(rows, 9.8)
        rows.move_to(box.get_center())
        card.add(box, rows)
        stamp = self.txt("veri: " + str(self.data.get("veri_durumu")), size=11, color=SLATE, mono=True)
        stamp.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(card, scale=0.97), run_time=0.7)
        self.wait(1.6)
        self.play(FadeIn(stamp), run_time=0.3)
        self.wait(1.0)
        self.iris(12.0, 0.02, run_time=0.9)
        self.play(FadeOut(VGroup(card, stamp)), run_time=0.3)
