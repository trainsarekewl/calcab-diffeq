from manim import *


class SecondTerm(Scene):
    def construct(self):
        equation = MathTex(
            r"I",                               # [0]
            r"=",                               # [1]
            r"C_m \frac{dV_m}{dt}",             # [2]
            r"+",                               # [3]
            r"\bar{g}_K n^4 (V_m - V_K)",       # [4]
            r"+",                               # [5]
            r"g_{Na} m^3 h (V_m - V_{Na})",     # [6]
            r"+",                               # [7]
            r"g_l (V_m - V_l)",                 # [8]
            font_size=42,
        )
        equation.move_to(ORIGIN)

        self.add(equation)
        self.wait(1)

        original_k_center = equation[4].get_center()

        # ── 1. Isolate the K+ term ────────────────────────────────────────
        self.play(
            equation[4].animate.scale(2.5).move_to(UP * 2.2),
            *[FadeOut(equation[i]) for i in [0, 1, 2, 3, 5, 6, 7, 8]],
            run_time=1.2,
        )
        self.wait(0.3)

        k_label = Tex(r"potassium current term", font_size=30)
        k_label.move_to(ORIGIN)
        self.play(FadeIn(k_label), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(k_label), run_time=0.5)

        # Replace scaled equation[4] with a split version for sub-part highlighting
        k_split = MathTex(
            r"\bar{g}_K",    # [0]  max conductance
            r"n^4",          # [1]  gating probability
            r"(V_m - V_K)",  # [2]  driving force
            font_size=80,
        )
        k_split.move_to(UP * 2.2)

        self.remove(equation[4])
        self.add(k_split)

        self.wait(0.3)

        # ── 2. Driving force: (V_m - V_K) ────────────────────────────────
        driving_force = k_split[2]
        original_driving_force_center = driving_force.get_center()

        self.play(
            driving_force.animate.set_color(YELLOW).scale(1.3).move_to(ORIGIN),
            run_time=0.8,
        )
        self.wait(0.2)

        vk_note = Tex(r"$V_K \approx -90\,\mathrm{mV}$", font_size=32, color=YELLOW)
        vk_note.move_to(DOWN * 0.8)
        self.play(FadeIn(vk_note), run_time=0.7)
        self.wait(2)

        self.play(
            Unwrite(vk_note),
            driving_force.animate.set_color(WHITE).scale(1 / 1.3).move_to(original_driving_force_center),
            run_time=0.8,
        )
        self.wait(0.3)

        # ── 3. Max conductance: \bar{g}_K ─────────────────────────────────
        g_bar = k_split[0]
        original_g_bar_center = g_bar.get_center()
        self.play(
            g_bar.animate.set_color(BLUE_C).scale(1.3).move_to(ORIGIN),
            run_time=0.8,
        )
        self.wait(0.2)

        g_note = Tex(r"max conductance", font_size=32, color=BLUE_C)
        g_note.move_to(DOWN * 0.8)
        self.play(FadeIn(g_note), run_time=0.7)
        self.wait(2)

        self.play(
            Unwrite(g_note),
            g_bar.animate.set_color(WHITE).scale(1 / 1.3).move_to(original_g_bar_center),
            run_time=0.8,
        )
        self.wait(0.3)

        # ── 4. Channel probability: n^4 ───────────────────────────────────
        n4 = k_split[1]

        self.play(
            n4.animate.set_color(GREEN).scale(1.3).shift(DOWN * 0.9),
            run_time=0.8,
        )
        self.wait(0.2)

        # Channel diagram: a box representing the channel protein with 4 gate lines
        channel_box = Rectangle(width=3.0, height=1.8, color=GREY_B, stroke_width=3)
        channel_box.move_to(DOWN * 0.5)

        gate_xs = [-1.05, -0.35, 0.35, 1.05]

        gates = VGroup()
        n_labels = VGroup()
        for x in gate_xs:
            center = channel_box.get_center() + RIGHT * x
            gate = Line(center + LEFT * 0.24, center + RIGHT * 0.24, color=RED, stroke_width=6)
            gates.add(gate)
            lbl = MathTex(r"n", font_size=20, color=GREY_A)
            lbl.move_to(channel_box.get_top() + RIGHT * x + UP * 0.22)
            n_labels.add(lbl)

        channel_diagram = VGroup(channel_box, gates, n_labels)
        self.play(FadeIn(channel_diagram), run_time=0.8)
        self.wait(0.6)

        # All four gates open (horizontal → vertical, grey → green)
        open_anims = []
        for i, x in enumerate(gate_xs):
            center = channel_box.get_center() + RIGHT * x
            gate_open = Line(center + DOWN * 0.7, center + UP * 0.7, color=GREEN, stroke_width=6)
            open_anims.append(Transform(gates[i], gate_open))

        self.play(*open_anims, run_time=0.9)
        self.wait(0.4)

        p_note = MathTex(r"P(\text{open}) = n^4", font_size=30, color=GREEN)
        p_note.next_to(channel_box, DOWN, buff=0.35)
        self.play(FadeIn(p_note), run_time=0.7)
        self.wait(1.5)

        # Gate 0 closes — one subunit closed means channel is closed
        center0 = channel_box.get_center() + RIGHT * gate_xs[0]
        gate0_closed = Line(center0 + LEFT * 0.24, center0 + RIGHT * 0.24, color=RED, stroke_width=6)
        self.play(Transform(gates[0], gate0_closed), run_time=0.6)
        self.wait(0.2)

        closed_note = Tex(r"channel closed", font_size=28, color=RED)
        closed_note.next_to(p_note, DOWN, buff=0.2)
        self.play(FadeIn(closed_note), run_time=0.5)
        self.wait(1.2)

        # Clean up channel section
        self.play(
            FadeOut(channel_diagram),
            Unwrite(p_note),
            FadeOut(closed_note),
            n4.animate.set_color(WHITE).scale(1 / 1.3).shift(UP * 0.9),
            run_time=0.9,
        )
        self.wait(0.3)

        # ── 5. Restore full equation ───────────────────────────────────────
        self.play(FadeOut(k_split), run_time=0.5)

        equation2 = MathTex(
            r"I",
            r"=",
            r"C_m \frac{dV_m}{dt}",
            r"+",
            r"\bar{g}_K n^4 (V_m - V_K)",
            r"+",
            r"g_{Na} m^3 h (V_m - V_{Na})",
            r"+",
            r"g_l (V_m - V_l)",
            font_size=42,
        )
        equation2.move_to(ORIGIN)

        self.play(FadeIn(equation2), run_time=1.2)
        self.wait(2)
