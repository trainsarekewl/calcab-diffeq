from manim import *


class ThirdTerm(Scene):
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

        # ── 1. Isolate the Na+ term ────────────────────────────────────────
        self.play(
            equation[6].animate.scale(2.5).move_to(UP * 2.2),
            *[FadeOut(equation[i]) for i in [0, 1, 2, 3, 4, 5, 7, 8]],
            run_time=1.2,
        )
        self.wait(0.3)

        na_label = Tex(r"sodium current term", font_size=30)
        na_label.move_to(ORIGIN)
        self.play(FadeIn(na_label), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(na_label), run_time=0.5)

        # Split for sub-part highlighting
        na_split = MathTex(
            r"g_{Na}",          # [0]  max conductance
            r"m^3 h",           # [1]  gating probability
            r"(V_m - V_{Na})",  # [2]  driving force
            font_size=80,
        )
        na_split.move_to(UP * 2.2)

        self.remove(equation[6])
        self.add(na_split)

        self.wait(0.3)

        # ── 2. Driving force: (V_m - V_Na) ────────────────────────────────
        driving_force = na_split[2]
        original_driving_force_center = driving_force.get_center()

        self.play(
            driving_force.animate.set_color(YELLOW).scale(1.3).move_to(ORIGIN),
            run_time=0.8,
        )
        self.wait(0.2)

        vna_note = Tex(r"$V_{Na} \approx +55\,\mathrm{mV}$", font_size=32, color=YELLOW)
        vna_note.move_to(DOWN * 0.8)
        self.play(FadeIn(vna_note), run_time=0.7)
        self.wait(2)

        self.play(
            Unwrite(vna_note),
            driving_force.animate.set_color(WHITE).scale(1 / 1.3).move_to(original_driving_force_center),
            run_time=0.8,
        )
        self.wait(0.3)

        # ── 3. Max conductance: g_Na ──────────────────────────────────────
        g_na = na_split[0]
        original_g_na_center = g_na.get_center()

        self.play(
            g_na.animate.set_color(BLUE_C).scale(1.3).move_to(ORIGIN),
            run_time=0.8,
        )
        self.wait(0.2)

        g_note = Tex(r"max conductance", font_size=32, color=BLUE_C)
        g_note.move_to(DOWN * 0.8)
        self.play(FadeIn(g_note), run_time=0.7)
        self.wait(2)

        self.play(
            Unwrite(g_note),
            g_na.animate.set_color(WHITE).scale(1 / 1.3).move_to(original_g_na_center),
            run_time=0.8,
        )
        self.wait(0.3)

        # ── 4. Restore full equation ───────────────────────────────────────
        self.play(FadeOut(na_split), run_time=0.5)

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
