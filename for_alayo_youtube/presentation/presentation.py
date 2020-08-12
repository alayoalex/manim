from manimlib.imports import *


class Presentation(Scene):
    def construct(self):
        #math = TexMobject(r"\Mu")
        math = TexMobject(r"\alpha", r"\lambda", r"\alpha", r"\phi", r"\omicron")
        
        math.set_color_by_gradient(BLUE, RED)
        math.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(math))
        self.wait(1)