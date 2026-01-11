from manim import *

# Practice
# class Hello(Scene):
#     def construct(self):
#         a = Text("Hello", color=BLUE, font_size=48)
#         self.play(FadeIn(a))
#         self.play(FadeOut(a))

# class SquareToCircle(Scene):
#     def construct(self):
#         a = Square(2)
#         a.color = PINK
#         b = Circle(2, color=GREEN)
#         b.set_fill(PINK,1)
#         self.play(Create(a))
#         self.play(Rotate(a, PI/4))
#         self.play(ReplacementTransform(a, b))
#         self.play(FadeOut(b))

# Vide Code
# class Quote(Scene):
#     def construct(self):
#         quote = Paragraph(
#             "\"Whatever the mind of man can conceive and",
#             "believe, it can achieve.\"",
#             "- Napoleon Hill", font_size=36, alignment="left", line_spacing=1)
#         self.play(Write(quote))
#         self.wait(1.5)
#         self.play(FadeOut(quote))

# class Delaying(Scene):
#     def construct(self):
#         delaying = Paragraph("I have been delaying releasing this video "
#                             ,"for so long", font_size=36, alignment="center")
#         self.play(GrowFromCenter(delaying))
#         self.wait(.5)
#         self.play(FadeOut(delaying))

# class Originally(Scene):
#     def construct(self):
#         originally = Paragraph(
#             "Originally, this video was going to be an","Introduction to Me and My Interests",
#             font_size=36, alignment="center"
#         )
#         after = Text("But after recording, I kept Rerecording...", font_size=36)

#         self.play(Write(originally))
#         self.play(ReplacementTransform(originally, after))
#         self.play(Unwrite(after))

# class SaidToMyself(Scene):
#     def construct(self):
#         saidtomyself = Text("And I said to Myself", font_size=32)
#         saidtomyself.set_y(3)
#         sound = Text("“The sound is not good”", font_size=26)
#         sound.set_x(-3)
#         nose = Text("“My nose is stuffy, so my voice…”", font_size=26)
#         nose.set_x(3)
#         grp = VGroup()
#         grp.add(saidtomyself)
#         grp.add(sound)
#         grp.add(nose)

#         excuses = Text("I realize now these were just excuses")

#         self.play(Write(saidtomyself))
#         self.play(GrowFromPoint(sound, [0, 3, 0]))
#         self.wait(.5)
#         self.play(GrowFromPoint(nose, [0, 3, 0]))
#         self.play(ReplacementTransform(grp, excuses))
#         self.play(FadeOut(excuses))

# class Admit(Scene):
#     def construct(self):
#         what = Text("What I didn't want to admit", font_size=40)
#         what.set_y(2)
#         scared = Text("I was Scared", font_size=34)
#         scared.set_x(-4)
#         failure = Text("Failure", font_size=34, color=RED)
#         failure.set_x(4)
#         s = [-2, 0, 0]
#         e = [3, 0, 0]
#         arrow = Arrow(start=s, end=e, color=WHITE)

#         self.play(Write(what))
#         self.play(GrowFromEdge(scared, LEFT))
#         self.play(GrowArrow(arrow))
#         self.play(GrowFromEdge(failure, LEFT))
#         self.play(FadeOut(what, scared, arrow, failure))

# class Fear(Scene):
#     def construct(self):
#         fear = Text("Fear of Failure", font_size=40)
#         mark = Text("?", font_size=48, color=YELLOW)
#         mark.set_y(3)
#         mark2 = Text("?", font_size=48, color=YELLOW)
#         mark2.set_y(-3)
#         mark2.scale(-1, about_edge=X_AXIS)
#         mark3 = Text("?", font_size=48, color=YELLOW)
#         mark3.set_x(-3)
#         mark3.rotate(PI/2)
#         mark4 = Text("?", font_size=48, color=YELLOW)
#         mark4.set_x(3)
#         mark4.rotate(-PI/2)
#         mark_grp = VGroup(mark, mark2, mark3, mark4)
#         self.play(SpinInFromNothing(fear))
#         self.play(FadeIn(mark_grp))
#         self.play(Rotate(mark_grp, PI*2, OUT, ORIGIN))
#         self.play(Circumscribe(fear, shape=Rectangle, color=RED))
#         self.play(FadeOut(
#             mark_grp, fear
#         ))

# class Contents(Scene):
#     def construct(self):
#         contents = Text("Contents", font_size=48)
#         contents.set_y(3)
#         intro = Text("Introduction", font_size=36)
#         intro.set_x(-3)
#         situation = Text("My Situation", font_size=36)
#         situation.set_x(3)
#         s = [-1,0,0]
#         e = [1,0,0]
#         arrow = Arrow(start=s, end=e, color=WHITE)
#         self.play(Write(contents))
#         self.play(GrowFromPoint(intro, [0,3,0]))
#         self.play(GrowArrow(arrow))
#         self.play(ReplacementTransform(intro, situation))
#         self.play(FadeOut(VGroup(self.get_mobject_family_members())))

# class Change(Scene):
#     def construct(self):
#         meme = ImageMobject("fearchange.jpg")
#         meme.scale(0.8)
#         self.play(FadeIn(meme))
#         self.wait(1)
#         self.play(FadeOut(meme))

# class Effort(Scene):
#     def construct(self):
#         belief1 = Text("\"I can achieve anything!\"", font_size=24)
#         belief1.set_x(-3)
#         belief1.set_y(1)
#         belief2 = Text("\"I can achieve anything!\"", font_size=24)
#         belief2.set_x(-3)
#         belief2.set_y(-1)
#         s1 = [-1,1,0]
#         e1 = [2,1,0]
#         s2 = [-1,-1,0]
#         e2 = [2,-1,0]
        
#         arrText1 = Text("Actual Effort", font_size=20)
#         arrow1 = Arrow(s1, e1, color=WHITE)
#         arrText1.next_to(arrow1,UP)
#         arrow1.add(arrText1)

#         arrText2 = Text("No Effort", font_size=20)
#         arrow2 = Arrow(s2, e2, color=WHITE)
#         arrText2.next_to(arrow2,UP)
#         arrow2.add(arrText2)

#         result1 = Text("Achievement", font_size=24, color=GREEN)
#         result1.set_x(3)
#         result1.set_y(1)
#         result2 = Text("Bruh", font_size=24, color=RED)
#         result2.set_x(3)
#         result2.set_y(-1)
        
#         self.play(Write(belief1), Write(belief2))
#         self.play(GrowArrow(arrow1), GrowArrow(arrow2))
#         self.play(Write(result1), Write(result2))
#         self.play(FadeOut(VGroup(self.get_mobject_family_members())))

# class JustGetItDone(Scene):
#     def construct(self):
#         text = Text("Just Get It Done!", font_size=40)
#         self.play(Write(text))
#         self.play(Wiggle(text, scale_value=1.2))
#         self.play(Unwrite(text))