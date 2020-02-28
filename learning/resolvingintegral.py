from manimlib.imports import *
import os
import pyclbr
import numpy as np


class ResonvingIntegral(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.2)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

        self.wait()

        example_text = TextMobject(
            "Resuelve esta integral",
            tex_to_color_map={"integral": YELLOW}
        )
        example_tex = TexMobject(
            "\\int \\frac{1}{x^4 + 1} dx",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()

        self.play(FadeOutAndShiftDown(example_text))
        example_tex.scale(0.3)
        example_tex.to_corner(UL)
        self.play(Transform(example_tex, example_tex))