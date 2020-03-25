from manimlib.imports import *

class Images(Scene):
    def construct(self):
        img = ImageMobject('E:\\workspace\\github\\manim\\learning\\manim-tutorial\\gauss1.jpg')
        img.scale(2)  # Resize to be twice as big
        img.shift(UP)  # Move the image

        self.play(ShowCreation(img))  # Display the image
