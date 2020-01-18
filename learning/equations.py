from manimlib.imports import *
import os
import pyclbr


class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)
        self.play(Write(eq1))
        self.play(Write(eq2))


class ExerciseExampleIntegral(Scene):
    def construct(self):
        deriv, integral, v_t, dt, equals, v_T = formula = TexMobject(
            "\\frac{d}{dT}", 
            "\\int_0^T", "v(t)", "\\,dt", 
            "=", "v(T)"
        )

        self.play(Write(formula))


class ExerciseExample(Scene):
    def construct(self):
        eq1=TexMobject(r"\int_{C} (2 + x^2y) \,dx")
        eq2=TexMobject(r"\int_{C} (2 + x^2y) dx = \int_{0}^{\pi} (2 + \cos^2 t \sin^2 t) \sqrt{\left(\frac{dx}{d t}\right)^2 + \left(\frac{dy}{dt}\right)^2} \,dt")
        eq1.shift(2*UP)
        #eq2.shift(1*UP)
        self.play(Write(eq1))
        self.play(Write(eq2))
