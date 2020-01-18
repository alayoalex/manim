from manimlib.imports import *
import os
import pyclbr
import numpy as np


class TryShapes(Scene):
    #My own scenes.
    def construct(self):
        pol = Polygon(np.array([0,0,0]),np.array([1,0,0]),np.array([1,1,0]), np.array([0,1,0]))
        self.play(GrowFromCenter(pol))
        self.play(Rotate(pol))


class TryAddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Christ Lives")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("God is Good")
        quote2.set_color(YELLOW)
        author=TextMobject("-Holly Bible")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
        ApplyMethod(author.to_corner,quote2.get_corner(DOWN+RIGHT)+DOWN+2*RIGHT))
        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))


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

