from manim import *


class FirstTerm(Scene):
    def construct(self):
        # HH equation
        equation = MathTex(
            r"I",                               # [0]
            r"=",                               # [1]
            r"C_m \frac{dV_m}{dt}",             # [2]
            r"+",                               # [3]
            r"g_K n^4 (V_m - V_K)",             # [4]
            r"+",                               # [5]
            r"g_{Na} m^3 h (V_m - V_{Na})",     # [6]
            r"+",                               # [7]
            r"g_l (V_m - V_l)",                 # [8]
            font_size=42,
        )
        equation.move_to(ORIGIN)

        self.add(equation)
        self.wait(2)

        original_cap_center = equation[2].get_center()



        # zoom 1: C_m dV_m/dt from the HH equation 
        # ---------------------------------------------

        self.play(
            equation[2].animate.scale(2.5).move_to(UP * 1.8),
            *[FadeOut(equation[i]) for i in [0, 1, 3, 4, 5, 6, 7, 8]],
            run_time=1.2,
        )
        self.wait(0.3)

        membrane_label = Tex(
            r"membrane capacitance term",
            font_size=28,
        )
        membrane_label.move_to(ORIGIN)
        self.play(FadeIn(membrane_label), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(membrane_label))
        self.play(FadeOut(equation[2]))
        self.remove(equation)
    


        # V_m = V_inside - V_outside 
        # --------------------------------
        vm_eq = MathTex(
            r"V_m = V_{\mathrm{inside}} - V_{\mathrm{outside}}",
            font_size=48,
        )
        vm_eq.move_to(ORIGIN)

        self.play(Write(vm_eq), run_time=1.0)
        self.wait(0.4)



        # zoom in — scale up and shift up to make room for the note
        # ---------------------------------------------

        self.play(vm_eq.animate.scale(1.25).move_to(UP * 0.6), run_time=1.2)
        self.wait(0.3)

        vm_note = Tex(
            r"$V_{\mathrm{outside}} = 0$, so\\$V_m = V_{\mathrm{inside}} \approx -70\,\mathrm{mV}$ at rest",
            font_size=30,
            color=YELLOW,
        )
        vm_note.move_to(DOWN * 0.3)
        self.play(FadeIn(vm_note), run_time=0.8)
        self.wait(2.5)

        # zoom back out of vm_eq
        self.play(
            Unwrite(vm_note),
            run_time=0.8,
        )
        self.play(Unwrite(vm_eq))



        # Q = C_m V_m
        # ----------------------------
        q_eq = MathTex(r"Q = C_m \, V_m", font_size=48)
        q_eq.move_to(ORIGIN)

        self.play(Write(q_eq), run_time=0.9)
        self.wait(0.4)

        # zoom in
        self.play(q_eq.animate.scale(1.3).move_to(UP * 0.6), run_time=0.8)
        self.wait(0.3)

        q_label = Tex(
            r"$Q$ = charge stored \\ $C_m$ = capacitance (constant) \\$V_m$ = voltage",
            font_size=28,
        )
        q_label.move_to(DOWN * 0.3)
        self.play(FadeIn(q_label), run_time=0.8)
        self.wait(2.5)
        self.play(Unwrite(q_label), run_time=0.8)



        # zoom back out and do derivative ting
        # ----------------------------------------------
        self.play(
            q_eq.animate.scale(1 / 1.3).move_to(UP * 2),
            run_time=0.8,
        )

        # dQ/dt = C_m dV_m/dt
        dq_eq = MathTex(
            r"\frac{dQ}{dt}",       # [0]
            r"=",                   # [1]
            r"C_m",                 # [2]
            r"\frac{dV_m}{dt}",     # [3]
            font_size=48,
        )
        dq_eq.move_to(ORIGIN)

        self.play(
            Write(dq_eq),
            run_time=1.0,
        )
        self.wait(0.4)

        # zoom in on the derivative equation
        self.play(dq_eq.animate.scale(1.2).move_to(UP * 0.8), run_time=0.8)
        self.wait(0.3)

        # highlight the RHS = I_C
        rhs = VGroup(dq_eq[2], dq_eq[3])
        ic_brace = Brace(rhs, DOWN, buff=0.1)
        ic_label = ic_brace.get_tex(r"I_C", buff=0.1)
        ic_label.set_color(YELLOW)

        self.play(
            rhs.animate.set_color(YELLOW),
            GrowFromCenter(ic_brace),
            FadeIn(ic_label),
            run_time=0.9,
        )
        self.wait(0.4)

        ic_meaning = Tex(
            r"Current is $\frac{dQ}{dt}$\\$I_C = C_m\frac{dV_m}{dt}$",
            font_size=30,
            color=BLUE_C,
        )
        ic_meaning.move_to(DOWN * 1.6)
        self.play(FadeIn(ic_meaning), run_time=0.8)
        self.wait(3)

        # clean up
        self.play(
            FadeOut(dq_eq),
            FadeOut(ic_brace),
            FadeOut(ic_label),
            FadeOut(ic_meaning),
            FadeOut(q_eq),
            run_time=0.8,
        )



        # go back to full eq — reset equation[2] to its original scale and position
        equation[2].scale(1 / 2.5).move_to(original_cap_center)

        self.play(FadeIn(equation), run_time=1.2)
        self.wait(2)
