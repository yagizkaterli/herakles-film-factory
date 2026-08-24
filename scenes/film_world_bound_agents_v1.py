import json
from pathlib import Path

import numpy as np
from manim import *


SOURCE = Path(__file__).resolve().parents[1] / "canonical" / "world-bound-film-source.v1.json"


class WorldBoundAgentsV1(ThreeDScene):
    """A real HERAKLES World snapshot rendered as a read-only habitat film."""

    def construct(self):
        source = json.loads(SOURCE.read_text(encoding="utf-8"))
        agents = source["agents"]
        stats = source["aggregates"]
        self.camera.background_color = "#04070C"
        self.set_camera_orientation(phi=66 * DEGREES, theta=-58 * DEGREES, focal_distance=22)

        title = Text("A LIVE WORLD FOR BOUNDED WORK", font="DejaVu Sans Mono", font_size=25,
                     color="#E8E2D7", weight=BOLD)
        title.to_edge(UP, buff=.2)
        stamp = Text(f"SNAPSHOT {source['snapshot_id'].split(':')[-1]} · READ-ONLY",
                     font="DejaVu Sans Mono", font_size=10, color="#77909A")
        stamp.to_edge(UP, buff=.02)
        subtitle = Text("LIVE WORKERS · BOUNDED TRACES · RECEIPTS",
                        font="DejaVu Sans Mono", font_size=12, color="#70E5F2")
        subtitle.next_to(title, DOWN, buff=.12)
        self.add_fixed_in_frame_mobjects(title, subtitle, stamp)
        self.play(FadeIn(title), FadeIn(subtitle), FadeIn(stamp), run_time=.55)

        # Habitat floor: the actual World is represented as a bounded field, not a dashboard.
        floor = VGroup()
        for x in range(-6, 7, 2):
            for z in range(-4, 5, 2):
                tile = Prism(dimensions=[1.72, .08, 1.48], fill_color="#0B1217",
                             fill_opacity=.28, stroke_color="#1B2B31", stroke_width=.6)
                tile.move_to([x, -.46, z])
                floor.add(tile)
        self.play(LaggedStart(*[FadeIn(t) for t in floor], lag_ratio=.012), run_time=.9)

        root = Cylinder(radius=.56, height=.22, direction=UP, resolution=24,
                        fill_color="#152B31", fill_opacity=.98, stroke_color="#A3E9F0", stroke_width=2)
        root.move_to([0, -.15, 0])
        root_ring = Torus(major_radius=.8, minor_radius=.025, color="#58C9D8").move_to([0, -.02, 0])
        root_label = Text("WORLD", font="DejaVu Sans Mono", font_size=15, color="#B9F3CB")
        root_label.to_edge(DOWN, buff=.7)
        self.add_fixed_in_frame_mobjects(root_label)
        self.play(FadeIn(root), Create(root_ring), Write(root_label), run_time=.65)

        positions = []
        for i, _ in enumerate(agents):
            angle = TAU * i / len(agents)
            radius = 2.1 + .38 * (i % 3)
            positions.append([radius * np.cos(angle), .22 + .08 * (i % 2), radius * np.sin(angle)])

        limbs = VGroup()
        nodes = VGroup()
        labels = VGroup()
        pulses = []
        for i, (agent, pos) in enumerate(zip(agents, positions)):
            working = agent["status"] == "working"
            color = "#70E5F2" if working else "#64747C"
            line = Line(root.get_center(), pos, color="#2B6570" if working else "#243239", stroke_width=2)
            node = Sphere(radius=.16 if working else .13, resolution=(14, 8), fill_color=color,
                          fill_opacity=.92, stroke_color="#E8FFFF" if working else "#849198", stroke_width=1.5)
            node.move_to(pos)
            short = agent["id"].replace(".service", "").replace("codex-oda@", "oda/")
            label = Text(short[:17], font="DejaVu Sans Mono", font_size=10.5, color=color)
            # Screen-space rails prevent projected labels from collapsing at the root.
            rail_x = -6.15 if i < 8 else 3.35
            rail_y = 2.0 - (i % 8) * .48
            label.move_to([rail_x, rail_y, 0])
            limbs.add(line)
            nodes.add(node)
            labels.add(label)
            if working:
                pulses.append(node)

        self.play(LaggedStart(*[Create(x) for x in limbs], lag_ratio=.025), run_time=1.0)
        self.play(LaggedStart(*[GrowFromCenter(x) for x in nodes], lag_ratio=.035), run_time=1.0)
        self.add_fixed_in_frame_mobjects(labels)
        self.play(LaggedStart(*[FadeIn(x) for x in labels], lag_ratio=.025), run_time=.9)

        live_text = VGroup(
            Text(f"{stats['working_selected']} WORKING", font="DejaVu Sans Mono", font_size=14, color="#70E5F2"),
            Text(f"{stats['idle_selected']} IDLE", font="DejaVu Sans Mono", font_size=14, color="#8A969B"),
            Text(f"{stats['task_count']} TASKS", font="DejaVu Sans Mono", font_size=14, color="#F0BC67"),
        ).arrange(RIGHT, buff=.28)
        live_text.to_edge(LEFT, buff=.24).shift(DOWN * 1.1)
        self.add_fixed_in_frame_mobjects(live_text)
        self.play(LaggedStart(*[Write(x) for x in live_text], lag_ratio=.1), run_time=.55)

        # A pulse is an activity signal only; no hidden reasoning is rendered.
        for node in pulses[:7]:
            self.play(node.animate.scale(1.35).set_opacity(.55), run_time=.12)
            self.play(node.animate.scale(1 / 1.35).set_opacity(.92), run_time=.12)

        trace_dot = Sphere(radius=.08, resolution=(10, 6), fill_color="#F0BC67",
                          stroke_color="#FFF0C8", stroke_width=1).move_to(root.get_center())
        self.add(trace_dot)
        self.play(MoveAlongPath(trace_dot, limbs[0], run_time=.8, rate_func=linear), run_time=.8)
        self.play(FadeOut(trace_dot), run_time=.18)

        # Task parcels are aggregate, source-bound markers.
        task_orbits = VGroup()
        orbit = Circle(radius=3.9, color="#234D56", stroke_width=1).rotate(PI / 2, axis=RIGHT)
        orbit.move_to([0, .2, 0])
        task_orbits.add(orbit)
        self.play(Create(task_orbits), run_time=.65)
        parcels = VGroup()
        parcel = Sphere(radius=.12, resolution=(10, 6), fill_color="#F0BC67",
                        stroke_color="#FFE9B8", stroke_width=1).move_to([3.9, .2, 0])
        parcels.add(parcel)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in parcels], lag_ratio=.1), run_time=.7)
        task_text = Text("TASK COUNT = 60 · ONE AGGREGATE · SOURCE-BOUND",
                         font="DejaVu Sans Mono", font_size=12, color="#F0BC67")
        task_text.to_edge(RIGHT, buff=.18).shift(DOWN * 1.0)
        self.add_fixed_in_frame_mobjects(task_text)
        self.play(Write(task_text), run_time=.4)

        seal = Torus(major_radius=.48, minor_radius=.045, color="#B9F3CB").move_to([0, .62, 0])
        seal_label = Text("RECEIPT", font="DejaVu Sans Mono", font_size=14, color="#B9F3CB")
        seal_label.to_edge(DOWN, buff=.22)
        self.add_fixed_in_frame_mobjects(seal_label)
        self.play(Create(seal), Write(seal_label), run_time=.55)
        footer = Text("A LIVE SNAPSHOT IS A PLACE · NOT A CHAT SCREEN",
                      font="DejaVu Sans Mono", font_size=15, color="#E8E2D7")
        footer.to_edge(DOWN, buff=.02)
        self.add_fixed_in_frame_mobjects(footer)
        self.play(Write(footer), run_time=.55)
        self.wait(1.0)
