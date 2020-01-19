from manimlib.imports import *
import os
import pyclbr
import numpy as np


class ResonvingIntegral(Scene):
    def construct(self):
        indefinite_integral_sign = "\\int"
        definite_integral_sign = "\\int_a_b"
        