from manimlib.imports import *
import cv2

class Images(Scene):
    def construct(self):
        img = cv2.imread('E:\\workspace\\github\\manim\\learning\\manim-tutorial\\gauss2.jpg')
        imMob = ImageMobject(img)  # Makes an image mobject of existing image

        imMob.scale(4)
        imMob.shift(UP)

        self.play(ShowCreation(imMob))