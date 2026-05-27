from manim import *


CAP_COLOR  = YELLOW
NA_COLOR   = "#FF6B35"
K_COLOR    = GREEN_C
LEAK_COLOR = BLUE_C
DIM        = 0.2


def vm(t):
    if t <= 2.0:
        return -70.0
    elif t <= 2.8:
        return -70.0 + 18.75 * (t - 2.0)   # -70 → -55  (stimulus)
    elif t <= 3.5:
        return -55.0 + 135.71 * (t - 2.8)  # -55 → +40  (spike)
    elif t <= 5.0:
        return 40.0 - 80.0 * (t - 3.5)     # +40 → -80  (repolarization)
    elif t <= 7.5:
        return -80.0 + 4.0 * (t - 5.0)     # -80 → -70  (recovery)
    else:
        return -70.0


class ActionPotential(Scene):
    def construct(self):

        # ── Equation ──────────────────────────────────────────────────────────
        eq = MathTex(
            r"I",                               # [0]
            r"=",                               # [1]
            r"C_m \frac{dV_m}{dt}",             # [2]
            r"+",                               # [3]
            r"\bar{g}_K n^4 (V_m - V_K)",       # [4]
            r"+",                               # [5]
            r"g_{Na} m^3 h (V_m - V_{Na})",     # [6]
            r"+",                               # [7]
            r"g_l (V_m - V_l)",                 # [8]
            font_size=34,
        )
        eq.to_edge(UP, buff=0.3)
        for i in [3, 4, 5, 6, 7, 8]:
            eq[i].set_opacity(DIM)

        # ── Axes ──────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 10.5, 2],
            y_range=[-105, 65, 20],
            x_length=10.0,
            y_length=5.0,
            axis_config={"color": GREY_C, "stroke_width": 1.5, "include_numbers": False},
            tips=False,
        )
        axes.shift(DOWN * 1.2)

        vm_lbl = MathTex(r"V_m", font_size=24, color=GREY_A)
        vm_lbl.next_to(axes.get_y_axis().get_top(), UL, buff=0.05)

        # Resting reference line
        rest_h = DashedLine(
            axes.c2p(0, -70), axes.c2p(10.5, -70),
            color=GREY_B, stroke_width=1.0, dash_length=0.12,
        )
        rest_lbl = Tex(r"rest", font_size=18, color=GREY_B)
        rest_lbl.move_to(axes.c2p(0.6, -70) + UP * 0.23)

        # Threshold line (added during Scene 3)
        thresh_h = DashedLine(
            axes.c2p(0, -55), axes.c2p(10.5, -55),
            color=RED_C, stroke_width=1.2, dash_length=0.12,
        )
        thresh_lbl = Tex(r"threshold", font_size=18, color=RED_C)
        thresh_lbl.move_to(axes.c2p(1.1, -55) + UP * 0.23)

        # ── Curve segments ────────────────────────────────────────────────────
        seg_rest  = axes.plot(vm, x_range=[0.0,  2.0],  color=GREY_C,    stroke_width=2.5)
        seg_cap   = axes.plot(vm, x_range=[2.0,  2.8],  color=CAP_COLOR,  stroke_width=3.0)
        seg_na    = axes.plot(vm, x_range=[2.8,  3.5],  color=NA_COLOR,   stroke_width=3.0)
        seg_k     = axes.plot(vm, x_range=[3.5,  5.0],  color=K_COLOR,    stroke_width=3.0)
        seg_hyper = axes.plot(vm, x_range=[5.0,  7.5],  color=K_COLOR,    stroke_width=2.5)
        seg_leak  = axes.plot(vm, x_range=[7.5, 10.0],  color=LEAK_COLOR, stroke_width=2.5)

        # ── SCENE 1: Setup ────────────────────────────────────────────────────
        self.play(FadeIn(eq), run_time=0.9)
        self.play(
            Create(axes),
            FadeIn(vm_lbl),
            Create(rest_h),
            FadeIn(rest_lbl),
            run_time=1.2,
        )
        self.play(Create(seg_rest), run_time=1.5)
        self.wait(0.8)

        # ── SCENE 2: Stimulus — capacitor charges ─────────────────────────────
        self.play(
            Indicate(eq[0], color=WHITE, scale_factor=1.4),
            run_time=0.5,
        )
        self.play(eq[2].animate.set_color(CAP_COLOR), run_time=0.5)
        self.play(Create(seg_cap), run_time=2.0)
        self.wait(0.4)

        # ── SCENE 3: Sodium spike ─────────────────────────────────────────────
        self.play(FadeIn(thresh_h), FadeIn(thresh_lbl), run_time=0.5)
        self.play(
            eq[2].animate.set_color(WHITE),
            eq[5].animate.set_opacity(1),
            eq[6].animate.set_color(NA_COLOR).set_opacity(1),
            run_time=0.5,
        )
        self.play(Create(seg_na), run_time=1.5)
        self.wait(0.4)

        # ── SCENE 4: Na shuts off, K repolarizes ──────────────────────────────
        self.play(
            eq[5].animate.set_opacity(DIM),
            eq[6].animate.set_opacity(DIM).set_color(WHITE),
            eq[3].animate.set_opacity(1),
            eq[4].animate.set_color(K_COLOR).set_opacity(1),
            run_time=0.5,
        )
        self.play(Create(seg_k), run_time=2.5)
        self.wait(0.3)

        # ── SCENE 5: Hyperpolarization ────────────────────────────────────────
        self.play(Create(seg_hyper), run_time=3.0)
        self.wait(0.4)

        # ── SCENE 6: Leak restores rest ───────────────────────────────────────
        self.play(
            eq[3].animate.set_opacity(DIM),
            eq[4].anonimate.set_opacity(DIM).set_color(WHITE),
            eq[7].animate.set_opacity(1),
            eq[8].animate.set_color(LEAK_COLOR).set_opacity(1),
            run_time=0.5,
        )
        self.play(Create(seg_leak), run_time=3.0)
        self.wait(0.5)

        # All terms return to normal
        self.play(
            *[eq[i].animate.set_opacity(1).set_color(WHITE) for i in range(9)],
            run_time=0.8,
        )
        self.wait(2)
