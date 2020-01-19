from manimlib.imports import *
import os
import pyclbr


class OrdinaryDifferenciaEquation(Scene):
    def construct(self):
        y = "y"
        psi = "\\psi(x)"
        derivative = "\\frac{d y}{d x}"
        result = "0.2xy"

        eq = TexMobject(derivative, "=", result, 
            tex_to_color_map={
                derivative: BLUE_C,
                result: YELLOW,
            })
        fun = TexMobject(y, "=", psi)

        eq.to_edge(UP)
        fun.next_to(eq, DOWN)

        self.play(Write(eq))
        self.play(GrowFromCenter(fun))