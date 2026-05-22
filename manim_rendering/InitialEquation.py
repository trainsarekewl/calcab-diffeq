from manim import *

class InitialEquation(Scene):
    def construct(self):
        # full HH equation
        equation = MathTex(
            r"I",                               # [0]  I
            r"=",                               # [1]
            r"C_m \frac{dV_m}{dt}",             # [2]  capacitive term
            r"+",                               # [3]
            r"g_K n^4 (V_m - V_K)",             # [4]  K+ term
            r"+",                               # [5]
            r"g_{Na} m^3 h (V_m - V_{Na})",     # [6]  Na+ term
            r"+",                               # [7]
            r"g_l (V_m - V_l)",                 # [8]  leak term
            font_size=42,
        )
        equation.move_to(ORIGIN)

        # ── Label below the zoomed I ──────────────────────────────────────
        label = Tex(
            r"$I$ is the total current being injected into the neuron from the input",
            font_size=30,
            color=YELLOW,
        )
        label.next_to(ORIGIN, DOWN, buff=1.2)

        # anims
        # fade in
        self.play(FadeIn(equation), run_time=1.5)
        self.wait(0.5)
        original_I_center = equation[0].get_center()

        
        # zoom into I
        self.play(
            equation[0].animate.scale(3).move_to(ORIGIN),
            *[FadeOut(equation[i]) for i in range(1, 9)],
            run_time=1.2,
        )
        self.wait(0.3)



        # label fade in
        self.play(FadeIn(label), run_time=0.8)
        self.wait(2)

        # fade out label and fade back in equation
        self.play(FadeOut(label), run_time=0.5)
        self.play(
            equation[0].animate.scale(1/3).move_to(original_I_center),
            *[FadeIn(equation[i]) for i in range(1, 9)],
            run_time=1.2,
        )
        self.wait(2)