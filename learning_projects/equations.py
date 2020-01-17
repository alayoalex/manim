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


class ExerciseExample(Scene):
    def construct(self):
        eq1=TexMobject(r"\int_{C} (2 + x^2y) \mathrm{d}x")
        eq2=TexMobject(r"\int_{C} (2 + x^2y) \mathrm{d}x = \int_{0}^{\pi} (2 + (\cos x)^2 (\sin x)^2) \sqrt{(\frac{\mathrm{d} x}{\mathrm{d} t})^2 + (\frac{\mathrm{d} y}{\mathrm{d} t})^2} \,\mathrm{d}t")
        eq1.shift(2*UP)
        #eq2.shift(1*UP)
        self.play(Write(eq1))
        self.play(Write(eq2))
