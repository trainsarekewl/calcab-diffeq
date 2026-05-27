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

        # ── 1. Isolate the leak term ──────────────────────────────────────
        self.play(
            equation[8].animate.scale(2.5).move_to(UP * 2.2),
            *[FadeOut(equation[i]) for i in [0, 1, 2, 3, 4, 5, 6, 7]],
            run_time=1.2,
        )
        self.wait(0.3)

        leak_label = Tex(r"leak current term", font_size=30)
        leak_label.move_to(ORIGIN)
        self.play(FadeIn(leak_label), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(leak_label), run_time=0.5)

        # Split for sub-part highlighting
        l_split = MathTex(
            r"g_l",          # [0]  fixed conductance
            r"(V_m - V_l)",  # [1]  driving force
            font_size=80,
        )
        l_split.move_to(UP * 2.2)
        self.remove(equation[8])
        self.add(l_split)
        self.wait(0.3)

        # ── 2. Driving force: (V_m - V_l) ────────────────────────────────
        driving_force = l_split[1]
        original_driving_force_center = driving_force.get_center()

        self.play(
            driving_force.animate.set_color(YELLOW).scale(1.3).move_to(ORIGIN),
            run_time=0.8,
        )
        self.wait(0.2)

        vl_note = Tex(r"$V_l \approx -65\,\mathrm{mV}$", font_size=32, color=YELLOW)
        vl_note.move_to(DOWN * 0.8)
        self.play(FadeIn(vl_note), run_time=0.7)
        self.wait(2)

        self.play(
            Unwrite(vl_note),
            driving_force.animate.set_color(WHITE).scale(1 / 1.3).move_to(original_driving_force_center),
            run_time=0.8,
        )
        self.wait(0.3)

        # ── 3. Fixed conductance: g_l ─────────────────────────────────────
        g_l = l_split[0]
        original_g_l_center = g_l.get_center()

        self.play(
            g_l.animate.set_color(BLUE_C).scale(1.3).move_to(ORIGIN),
            run_time=0.8,
        )
        self.wait(0.2)

        g_note = Tex(r"fixed conductance — no gating", font_size=32, color=BLUE_C)
        g_note.move_to(DOWN * 0.8)
        self.play(FadeIn(g_note), run_time=0.7)
        self.wait(2)

        self.play(
            Unwrite(g_note),
            g_l.animate.set_color(WHITE).scale(1 / 1.3).move_to(original_g_l_center),
            run_time=0.8,
        )
        self.wait(0.3)

        # ── 4. Restore full equation ──────────────────────────────────────
        self.play(FadeOut(l_split), run_time=0.5)

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