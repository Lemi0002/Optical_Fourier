from manim import *


class TestClass(Scene):
    def construct(self):
        square = Square(side_length=5, stroke_color=GREEN,
                        fill_color=BLUE, fill_opacity=0.75)

        self.play(Create(square), run_time=3)
        self.wait()
