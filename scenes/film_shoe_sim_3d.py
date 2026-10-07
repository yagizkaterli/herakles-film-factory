"""film_shoe_sim_3d.py — BABANIN ATÖLYESİ / HERAKLES SIM (3D film).

Gercek `harness sim kos` kosularini (Rust cekirdek: hos-sim) okur:
  sim/out-42/makbuz.json + olaylar.jsonl  (siparis 42 -> KABUL yolu)
  sim/out-43/makbuz.json + olaylar.jsonl  (siparis 43 -> RED + FIRE yolu)

Sahne hicbir semantik durum uydurmaz: sayaclar, digestler, kararlar ve
nedenler dogrudan makbuz/olay zincirinden gelir; dosya yoksa OLCULMUS
degerler gomulu FALLBACK olarak kullanilir ve bu ekranda isaretlenir.

Para kurali: baba-facing tum ekonomi TL; USD sembolu/tokeni ekranda YOK.
Stil: theatrical cartoon grameri (hop, squash/stretch, title card, muhur
damgasi); telifli karakter kopyasi yok; kernel deterministik (saat yok, RNG yok).
"""

import json
from pathlib import Path

import numpy as np
from manim import *

BG = "#070A0F"
INK = "#E8E2D7"
AMBER = "#E7B86A"
MINT = "#B7F0CD"
SLATE = "#778492"
RED = "#E4573D"
WOOD = "#4A3A2A"
SHIRT = "#171A1E"
SKIN = "#E8B489"
GRAY = "#C9CDCF"
PANEL = "#10161B"

SIM = Path(__file__).resolve().parents[1] / "sim"

# ---------------------------------------------------------------------------
# Olculen sim ciktilarinin gomulu kopyasi (fallback).
# Kaynak: harness sim kos (hos-sim), ts 2026-10-07T07:59:14Z.
# ---------------------------------------------------------------------------
F42 = {
    "ts": "2026-10-07T07:59:14Z",
    "sayaclar": {"adim": 9, "kabul": 8, "yetkisiz": 1, "ihlal": 0, "bicim": 0},
    "son_digest": "9ca44c32e004ece184526c1e4b46cd6a83ab30c9931d6b947ffc3d797a353bf8",
    "zincir_digest": "04b87f7fbb426bbeaf08bbcd93f659dc348e5311a1ca54c2984da3a9d4676a2b",
    "determinizm": {"kosu": 2, "ayni": True},
    "olaylar": [
        {"sira": 1, "tick": 1, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "74282c25b59a6f0d"},
        {"sira": 2, "tick": 2, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "448e731fda2818fa"},
        {"sira": 3, "tick": 3, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "acb160a9cdbc5992"},
        {"sira": 4, "tick": 4, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "4f6839dabb60366c"},
        {"sira": 5, "tick": 5, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "00d104f4b2a0f124"},
        {"sira": 6, "tick": 5, "aktor": "ham_deri", "dx": 1, "dy": 0, "karar": "Red", "neden": "YETKISIZ: aktor ham_deri icin 'Hareket' izni yok", "oz": "00d104f4b2a0f124"},
        {"sira": 7, "tick": 6, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "15748fa07f52f7b8"},
        {"sira": 8, "tick": 7, "aktor": "baba", "dx": 0, "dy": -1, "karar": "Kabul", "neden": "", "oz": "01942a70e76299e0"},
        {"sira": 9, "tick": 8, "aktor": "baba", "dx": 0, "dy": -1, "karar": "Kabul", "neden": "", "oz": "9ca44c32e004ece1"},
    ],
}
F43 = {
    "ts": "2026-10-07T07:59:14Z",
    "sayaclar": {"adim": 10, "kabul": 9, "yetkisiz": 0, "ihlal": 1, "bicim": 0},
    "son_digest": "e44c283afb6d0bc9b90ccbaaf043e37a039cc6570c00549315a85020233de66c",
    "zincir_digest": "16afbbaf0bc7e9b2624dfe27b181e4cd18e021e111e23637ee2e8e79600c2407",
    "determinizm": {"kosu": 2, "ayni": True},
    "olaylar": [
        {"sira": 1, "tick": 1, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "9176c722beb79a3a"},
        {"sira": 2, "tick": 2, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "419345e5e5b18e0b"},
        {"sira": 3, "tick": 3, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "d934ebd87789f001"},
        {"sira": 4, "tick": 4, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "d5a1a9c7596c530b"},
        {"sira": 5, "tick": 5, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "52ba9e33daad652a"},
        {"sira": 6, "tick": 5, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Red", "neden": "IHLAL: CakismaYok: ayakkabi ve kalip43 ayni hucrede (6,0)", "oz": "52ba9e33daad652a"},
        {"sira": 7, "tick": 6, "aktor": "ayakkabi", "dx": 0, "dy": 1, "karar": "Kabul", "neden": "", "oz": "094f10dbaf0dde71"},
        {"sira": 8, "tick": 7, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "16a4ba5bbf4d0422"},
        {"sira": 9, "tick": 8, "aktor": "ayakkabi", "dx": 1, "dy": 0, "karar": "Kabul", "neden": "", "oz": "67635ee374c6fd79"},
        {"sira": 10, "tick": 9, "aktor": "ayakkabi", "dx": 0, "dy": -1, "karar": "Kabul", "neden": "", "oz": "e44c283afb6d0bc9"},
    ],
}

D42 = {"ayakkabi": (0, 0), "ham_deri": (0, 1), "kesimci": (1, 2), "dikici": (2, 2),
       "montajci": (3, 2), "bitirici": (4, 2), "kalip42": (6, 2), "baba": (8, 2)}
D43 = {"ayakkabi": (0, 0), "kalip43": (6, 0), "kesimci": (1, 2), "dikici": (2, 2),
       "montajci": (3, 2), "bitirici": (4, 2), "baba": (8, 2)}

T = {
    "title": "BABANIN ATÖLYESİ — HERAKLES SIM",
    "subtitle": "SİPARİŞ → İŞ GRAFIĞI → KAPI → KABUL · 3D",
    "kernel": "hos-sim · saat yok · RNG yok · BTreeMap sıralı",
    "leg": "0 ATO · 1 KESİM · 2 DİKİŞ · 3 MONTAJ · 4 BİTİRME · 5 KAPI · 6 KABUL · 7 FİRE · 8 MÜHÜR",
    "s42": "SİPARİŞ 42 — doğru kalıp · tek kabul ölçütü: KABUL EDİLMİŞ ürün",
    "s43": "SİPARİŞ 43 — yanlış kalıp kabul rafını kapatmış",
    "yet": "YETKISIZ — ham_deri: bu adım için izin yok (fail-closed: durum değişmedi)",
    "ihl": "IHLAL: CakismaYok — yanlış kalıp kabul rafını kapatmış (6,0); durum değişmedi",
    "acc": "KABUL EDİLDİ",
    "price": "5.000 TL",
    "seal": "BABA ONAYI: MÜHÜR",
    "fire": "RED — FİRE",
    "replay": "AYNI GİRDİ → AYNI ÇIKTI",
    "replay_note": "her senaryo 2 koşu · parmak izleri eşit (determinizm kanıtı)",
    "eco_head": "EKONOMİK ÇEKİRDEK",
    "eco_ref": "1 KABUL EDİLMİŞ AYAKKABI = 5.000 TL",
    "eco_kpi": "maliyet / KABUL EDİLMİŞ AYAKKABI = UNKNOWN",
    "eco_marj": "marj (5.000 TL referans) = UNKNOWN",
    "eco_comp": "bileşenler: malzeme - işçilik - fire - hesaplama = UNKNOWN",
    "eco_cur": "bugünkü hesaplama maliyeti: TL karşılığı KUR MAKBUZU GELİNCE",
    "cl1": "Sadece yapmak yetmez.",
    "cl2": "Doğru numara - doğru kalıp - KABUL EDİLMİŞ ürün.",
    "cl3": "Gelir henüz kanıtlı değil - FAIL-CLOSED",
    "cl4": "HERAKLES SIM · SHOE STUDIO (3D)",
}


def _yukle(ad):
    """sim/<ad>/dosyalarini oku; yoksa olculmus fallback."""
    try:
        m = json.loads((SIM / ad / "makbuz.json").read_text(encoding="utf-8"))
        ol = [json.loads(s) for s in (SIM / ad / "olaylar.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
        olaylar = []
        for e in ol:
            olaylar.append({
                "sira": e["sira"], "tick": e["tick"], "aktor": e["aktor"],
                "dx": e["eylem"]["dx"], "dy": e["eylem"]["dy"],
                "karar": e["karar"], "neden": e.get("neden", ""),
                "oz": e["durum_ozeti"],
            })
        return {
            "ts": m["ts"], "sayaclar": m["sayaclar"], "son_digest": m["son_digest"],
            "zincir_digest": m["zincir_digest"], "determinizm": m["determinizm"],
            "olaylar": olaylar,
        }, "KANONIK (sim/)"
    except Exception:
        return (F42 if ad == "out-42" else F43), "GOMULU-FALLBACK (ölçülmüş değerler)"


class ShoeSim3D(ThreeDScene):
    """hos-sim kosularini 3D sahneye cevirir: is parcasi, istasyonlar, kapi, muhur."""

    def construct(self):
        self.data42, self.st42 = _yukle("out-42")
        self.data43, self.st43 = _yukle("out-43")
        veri47 = "KANONIK" if self.st42.startswith("KANONIK") and self.st43.startswith("KANONIK") else "GOMULU-FALLBACK"
        self.veri_durumu = veri47

        self.camera.background_color = BG
        self.set_camera_orientation(phi=68 * DEGREES, theta=-55 * DEGREES, focal_distance=20)

        self.act_title()
        self.begin_ambient_camera_rotation(rate=0.015)
        self.act_world()
        self.act_run42()
        self.act_reset43()
        self.act_run43()
        self.act_replay()
        self.act_economic()
        self.act_close()

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------
    def txt(self, s, size=14, color=INK, weight=NORMAL, mono=False):
        return Text(s, font=("DejaVu Sans Mono" if mono else "DejaVu Sans"), font_size=size, color=color, weight=weight)

    def fit(self, mob, max_w):
        if mob.width > max_w:
            mob.scale(max_w / mob.width)
        return mob

    def C(self, x, y):
        """Hucre (x,y) -> 3B nokta. y=0 uretim hatti (on), y=2 tezgah (arka)."""
        return np.array([(x - 4) * 1.25, 0.30, (1 - y) * 1.15])

    def squish(self, mob, sx=1.10, sy=0.90):
        self.play(mob.animate.stretch(sx, 0).stretch(sy, 1), run_time=0.14)
        self.play(mob.animate.stretch(1 / sx, 0).stretch(1 / sy, 1), run_time=0.14)

    def note(self, s, color=AMBER, hold=1.6):
        t = self.txt(s, size=15, color=color)
        self.fit(t, 10.6)
        box = RoundedRectangle(width=t.width + 0.6, height=t.height + 0.34, corner_radius=0.12,
                               fill_color=PANEL, fill_opacity=0.96, stroke_color=color, stroke_width=2)
        t.move_to(box.get_center())
        g = VGroup(box, t)
        g.to_edge(DOWN, buff=0.62)
        self.add_fixed_in_frame_mobjects(g)
        self.play(FadeIn(g, shift=UP * 0.15), run_time=0.32)
        self.wait(hold)
        self.play(FadeOut(g), run_time=0.28)

    def stamp2(self, s, color, size=22, y=-0.5):
        t = self.txt(s, size=size, color=color, weight=BOLD)
        box = RoundedRectangle(width=t.width + 0.7, height=t.height + 0.4, corner_radius=0.10,
                               stroke_color=color, stroke_width=4, fill_color=PANEL, fill_opacity=0.85)
        g = VGroup(box, t)
        t.move_to(g.get_center())
        g.rotate(-6 * DEGREES)
        g.move_to(np.array([0.0, y, 0.0]))
        self.add_fixed_in_frame_mobjects(g)
        self.play(FadeIn(g, scale=1.7), run_time=0.24)
        return g

    def hud_set(self, mob, s, size=12, color=MINT, mono=True):
        nt = self.txt(s, size=size, color=color, mono=mono)
        nt.move_to(mob)
        mob.become(nt)
        self.add_fixed_in_frame_mobjects(mob)

    # ------------------------------------------------------------------
    # 3B nesneler
    # ------------------------------------------------------------------
    def shoe3d(self, color=AMBER):
        sole = Prism(dimensions=[0.62, 0.10, 0.30], fill_color=WOOD, fill_opacity=1, stroke_color=INK, stroke_width=1.2)
        upper = Prism(dimensions=[0.36, 0.26, 0.24], fill_color=color, fill_opacity=1, stroke_color=INK, stroke_width=1.2)
        upper.move_to(sole.get_center() + np.array([-0.06, 0.17, 0.0]))
        return VGroup(sole, upper)

    def disc(self, color):
        return Cylinder(radius=0.26, height=0.06, fill_color=color, fill_opacity=1, stroke_color=INK, stroke_width=1.2)

    def worker(self):
        s = Sphere(radius=0.16, resolution=(10, 7), fill_color=SLATE, fill_opacity=1, stroke_color=INK, stroke_width=1)
        cap = Prism(dimensions=[0.18, 0.06, 0.18], fill_color=AMBER, fill_opacity=0.9, stroke_width=0).move_to([0, 0.16, 0])
        return VGroup(s, cap)

    def baba3d(self):
        head = Sphere(radius=0.22, resolution=(12, 8), fill_color=SKIN, fill_opacity=1, stroke_color=INK, stroke_width=1)
        hair = Prism(dimensions=[0.30, 0.11, 0.26], fill_color=GRAY, fill_opacity=1, stroke_width=0).move_to([0, 0.19, 0])
        beard = Prism(dimensions=[0.24, 0.12, 0.10], fill_color=GRAY, fill_opacity=1, stroke_width=0).move_to([0, -0.13, 0.15])
        body = Prism(dimensions=[0.46, 0.58, 0.30], fill_color=SHIRT, fill_opacity=1, stroke_color=INK, stroke_width=1).move_to([0, -0.54, 0])
        return VGroup(head, hair, beard, body)

    def leather(self):
        return Prism(dimensions=[0.50, 0.12, 0.34], fill_color=WOOD, fill_opacity=1, stroke_color=INK, stroke_width=1)

    # ------------------------------------------------------------------
    # perdeler
    # ------------------------------------------------------------------
    def act_title(self):
        box = RoundedRectangle(width=9.8, height=3.0, corner_radius=0.16, fill_color=PANEL, fill_opacity=0.97,
                               stroke_color=AMBER, stroke_width=3)
        rows = VGroup(
            self.txt(T["title"], size=28, color=AMBER, weight=BOLD),
            self.txt(T["subtitle"], size=14, color=INK),
            self.txt(T["kernel"], size=11, color=SLATE, mono=True),
        ).arrange(DOWN, buff=0.26)
        self.fit(rows, 9.0)
        rows.move_to(box.get_center())
        card = VGroup(box, rows)
        self.add_fixed_in_frame_mobjects(card)
        self.play(FadeIn(card, scale=0.96), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(card, shift=UP * 0.2), run_time=0.4)
        # kalici HUD
        self.hud_title = self.txt(T["title"], size=17, color=AMBER, weight=BOLD).to_edge(UP, buff=0.22).to_edge(LEFT, buff=0.35)
        self.hud_kernel = self.txt(T["kernel"], size=11, color=SLATE, mono=True).to_edge(UP, buff=0.28).to_edge(RIGHT, buff=0.35)
        self.hud_line = self.txt("adım 0 · tick 0", size=12, color=MINT, mono=True)
        self.hud_line.next_to(self.hud_title, DOWN, buff=0.10, aligned_edge=LEFT)
        self.hud_leg = self.txt(T["leg"], size=11, color=SLATE).to_edge(DOWN, buff=0.16)
        self.add_fixed_in_frame_mobjects(self.hud_title, self.hud_kernel, self.hud_line, self.hud_leg)

    def act_world(self):
        floor = Prism(dimensions=[11.8, 0.10, 4.0], fill_color="#0E1316", fill_opacity=1, stroke_width=0).move_to([0, -0.05, 0])
        lane = Prism(dimensions=[11.8, 0.02, 0.44], fill_color="#151B21", fill_opacity=1, stroke_width=0).move_to([0, 0.01, 1.15])
        bench = Prism(dimensions=[9.6, 0.06, 0.4], fill_color="#12181D", fill_opacity=1, stroke_width=0).move_to([0, 0.03, -1.15])
        pillars = VGroup()
        renk = {5: AMBER, 6: MINT, 7: RED, 8: SLATE}
        for x in range(9):
            c = renk.get(x, SLATE)
            h = 0.95 if x in (5, 6, 7) else 0.5
            p = Prism(dimensions=[0.07, h, 0.5], fill_color=c, fill_opacity=(0.85 if x in (5, 6, 7) else 0.4), stroke_width=0)
            p.move_to([(x - 4) * 1.25, h / 2, 1.80])
            pillars.add(p)
        gate = Torus(major_radius=0.45, minor_radius=0.07, color=AMBER).rotate(PI / 2, axis=UP).move_to(self.C(5, 0) + np.array([0, 0.45, 0]))
        shelf = Prism(dimensions=[0.95, 0.06, 0.52], fill_color=MINT, fill_opacity=0.45, stroke_width=0).move_to(self.C(6, 0) + np.array([0, -0.24, 0]))
        firepad = Cylinder(radius=0.40, height=0.03, fill_color=RED, fill_opacity=0.5, stroke_width=0).move_to(self.C(7, 0) + np.array([0, -0.26, 0]))
        sealpad = Cylinder(radius=0.34, height=0.03, fill_color=SLATE, fill_opacity=0.55, stroke_width=0).move_to(self.C(8, 0) + np.array([0, -0.26, 0]))
        self.world = VGroup(floor, lane, bench, pillars, gate, shelf, firepad, sealpad)
        self.play(FadeIn(self.world, shift=DOWN * 0.15), run_time=1.0)

        # aktorler (42 dunyasi baslangici)
        self.mobs = {
            "ayakkabi": self.shoe3d().move_to(self.C(0, 0)),
            "ham_deri": self.leather().move_to(self.C(0, 1)),
            "kesimci": self.worker().move_to(self.C(1, 2)),
            "dikici": self.worker().move_to(self.C(2, 2)),
            "montajci": self.worker().move_to(self.C(3, 2)),
            "bitirici": self.worker().move_to(self.C(4, 2)),
            "kalip42": self.disc(MINT).move_to(self.C(6, 2)),
            "baba": self.baba3d().move_to(self.C(8, 2)),
        }
        self.play(LaggedStart(*[FadeIn(m, scale=0.9) for m in self.mobs.values()], lag_ratio=0.08), run_time=1.1)
        self.hud_set(self.hud_line, T["s42"][:64], size=12, color=AMBER)
        self.wait(0.5)

    def act_run42(self):
        self._run(D42, self.data42, tag="42")

    def act_reset43(self):
        self.play(self.mobs["ayakkabi"].animate.move_to(self.C(0, 0)), run_time=0.7)
        self.play(FadeOut(self.mobs["kalip42"]), run_time=0.3)
        kalip43 = self.disc(RED).move_to(self.C(6, 0))
        self.mobs["kalip43"] = kalip43
        self.play(FadeIn(kalip43, scale=0.9), run_time=0.35)
        self.hud_set(self.hud_line, T["s43"][:64], size=12, color=RED)
        self.wait(0.4)

    def act_run43(self):
        self._run(D43, self.data43, tag="43")

    # ------------------------------------------------------------------
    # kosu oynatma
    # ------------------------------------------------------------------
    def _run(self, dunya, veri, tag):
        pos = dict(dunya)
        olaylar = veri["olaylar"]
        n = len(olaylar)
        for i, ev in enumerate(olaylar):
            ak = ev["aktor"]
            dx, dy = ev["dx"], ev["dy"]
            x, y = pos.get(ak, (0, 0))
            if tag == "43" and i == 5:
                self.move_camera(frame_center=self.C(5.5, 0.4), zoom=1.55, run_time=0.8)
            if ev["karar"] == "Kabul":
                nx, ny = x + dx, y + dy
                pos[ak] = (nx, ny)
                self.play(self.mobs[ak].animate.move_to(self.C(nx, ny)), run_time=0.42)
                if i < 2 or (tag == "42" and i == 6):
                    self.squish(self.mobs[ak])
                if tag == "42" and i == 6:  # kabul rafina varis
                    g = self.stamp2(T["acc"], AMBER, 22, y=-0.55)
                    tg = self.stamp2(T["price"], MINT, 20, y=-1.25)
                    self.wait(0.6)
                    self.play(FadeOut(g), FadeOut(tg), run_time=0.3)
                if tag == "42" and i == 8:  # baba muhur
                    s = self.stamp2(T["seal"], MINT, 16, y=-0.55)
                    self.wait(0.7)
                    self.play(FadeOut(s), run_time=0.3)
                if tag == "43" and i == 9:  # fire varis
                    self.note(T["fire"], RED, hold=1.1)
            else:
                tx, ty = x + dx, y + dy
                ring = Torus(major_radius=0.36, minor_radius=0.05, color=RED).rotate(PI / 2, axis=UP).move_to(self.C(tx, ty))
                self.play(GrowFromCenter(ring), run_time=0.16)
                self.play(Indicate(self.mobs[ak], color=RED, scale_factor=1.15), run_time=0.32)
                self.play(FadeOut(ring), run_time=0.18)
                if "YETKISIZ" in ev["neden"]:
                    self.note(T["yet"], AMBER, hold=1.7)
                else:
                    self.note(T["ihl"], RED, hold=1.9)
            self.hud_set(self.hud_line, "adım {}/{} · tick {} · {}".format(i + 1, n, ev["tick"], ev["oz"][:12]))
            if tag == "43" and i == 5:
                self.move_camera(frame_center=np.array([0.0, 0.5, 0.0]), zoom=1.0, run_time=0.8)
        sc = veri["sayaclar"]
        self.hud_set(self.hud_line, "SON: adım {} · kabul {} · yetkisiz {} · ihlal {} · {}".format(
            sc["adim"], sc["kabul"], sc["yetkisiz"], sc["ihlal"], veri["son_digest"][:12]))
        self.wait(0.6)

    # ------------------------------------------------------------------
    # replay / ekonomik cekirdek / kapanis
    # ------------------------------------------------------------------
    def act_replay(self):
        self.move_camera(phi=60 * DEGREES, theta=-46 * DEGREES, zoom=0.92, run_time=1.2)
        box = RoundedRectangle(width=9.6, height=2.9, corner_radius=0.14, fill_color=PANEL, fill_opacity=0.96,
                               stroke_color=MINT, stroke_width=3)
        rows = VGroup(
            self.txt("REPLAY — DETERMİNİZM", size=17, color=MINT, weight=BOLD),
            self.txt("42  son {}  ·  2/2 koşu eşit".format(self.data42["son_digest"][:16]), size=12, color=INK, mono=True),
            self.txt("43  son {}  ·  2/2 koşu eşit".format(self.data43["son_digest"][:16]), size=12, color=INK, mono=True),
            self.txt("zincir  {} …".format(self.data42["zincir_digest"][:16]), size=11, color=SLATE, mono=True),
            self.txt(T["replay_note"], size=12, color=SLATE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.fit(rows, 8.8)
        rows.move_to(box.get_center())
        card = VGroup(box, rows)
        self.add_fixed_in_frame_mobjects(card)
        self.play(FadeIn(card, scale=0.96), run_time=0.6)
        s = self.stamp2(T["replay"], MINT, 22, y=-1.6)
        self.add_fixed_in_frame_mobjects(s)
        self.wait(1.6)
        self.play(FadeOut(card), FadeOut(s), run_time=0.4)

    def act_economic(self):
        tl = self.txt("5.000 TL", size=46, color=AMBER, weight=BOLD)
        tl.move_to(np.array([-2.6, 0.9, 0.0]))
        ref = self.txt(T["eco_ref"], size=13, color=MINT).next_to(tl, DOWN, buff=0.25)
        banko = self.txt("tek kabul: KABUL EDİLMİŞ ürün", size=11, color=SLATE).next_to(ref, DOWN, buff=0.12)
        geo = VGroup(tl, ref, banko)
        box = RoundedRectangle(width=6.4, height=3.0, corner_radius=0.14, fill_color=PANEL, fill_opacity=0.96,
                               stroke_color=INK, stroke_width=3).move_to(np.array([2.4, 0.35, 0.0]))
        head = self.txt(T["eco_head"], size=16, color=AMBER, weight=BOLD).next_to(box.get_top(), DOWN, buff=0.2)
        lines = VGroup(
            self.txt(T["eco_kpi"], size=12, color=INK),
            self.txt(T["eco_marj"], size=12, color=INK),
            self.txt(T["eco_comp"], size=11, color=SLATE),
            self.txt(T["eco_cur"], size=11, color=SLATE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        for l in lines:
            self.fit(l, 5.8)
        lines.next_to(head, DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(geo, box, head, lines)
        self.play(FadeIn(geo, shift=UP * 0.12), run_time=0.5)
        self.play(FadeIn(box), FadeIn(head), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.1) for l in lines], lag_ratio=0.2), run_time=0.9)
        self.squish(tl, sx=1.05, sy=0.95)
        self.wait(1.4)
        self.play(FadeOut(geo), FadeOut(box), FadeOut(head), FadeOut(lines), run_time=0.5)

    def act_close(self):
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=72 * DEGREES, theta=-58 * DEGREES, zoom=0.82, run_time=1.2)
        card = RoundedRectangle(width=10.4, height=3.2, corner_radius=0.16, fill_color=PANEL, fill_opacity=0.97,
                                stroke_color=AMBER, stroke_width=4)
        rows = VGroup(
            self.txt(T["cl1"], size=24, color=AMBER, weight=BOLD),
            self.txt(T["cl2"], size=14, color=INK),
            self.txt(T["cl3"], size=13, color=RED),
            self.txt(T["cl4"], size=13, color=SLATE),
        ).arrange(DOWN, buff=0.22)
        self.fit(rows, 9.6)
        rows.move_to(card.get_center())
        g = VGroup(card, rows)
        self.add_fixed_in_frame_mobjects(g)
        self.play(FadeIn(g, scale=0.97), run_time=0.6)
        ts = self.data42.get("ts", "OLCULEMEDI")
        damga = self.txt("kök: harness sim kos (hos-sim) · ts {} · veri: {}".format(ts, self.veri_durumu),
                         size=10, color=SLATE, mono=True).to_edge(DOWN, buff=0.42)
        self.add_fixed_in_frame_mobjects(damga)
        self.play(FadeIn(damga), run_time=0.3)
        self.wait(1.4)
        self.play(FadeOut(g), FadeOut(damga), run_time=0.4)
