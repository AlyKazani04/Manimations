from manim import *

# class Hello(Scene):
#     def construct(self):
#         a = Text("Hello", color=BLUE, font_size=48)
#         self.play(FadeIn(a))
#         self.play(FadeOut(a))

class SquareToCircle(Scene):
    def construct(self):
        a = Square(2)
        a.color = PINK
        b = Circle(2, color=GREEN)
        b.set_fill(PINK,1)
        self.play(Create(a))
        self.play(Rotate(a, PI/4))
        self.play(ReplacementTransform(a, b))
        self.play(FadeOut(b))