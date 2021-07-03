from manim import *


class PointMovingOnShapes(Scene):
    def construct(self):

        # Create a square
        square = Square(color=BLUE)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        # Create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        # Create animations
        self.play(GrowFromCenter(square))
        self.play(Transform(square, circle))  # turn the square into a circle

        self.wait()  # wait for some seconds


class MovingFrame(Scene):
    def construct(self):
        # Write equations
        # equation = MathTex("2x^2-5x+2", "=", "(x-2)(2x-1)")
        equation = MathTex("2x^2-5x+2", "=", "(x-2)(2x-1)")

        # Create animation
        self.play(Write(equation))

        # Add moving frames
        framebox1 = SurroundingRectangle(equation[0], buff=.1)
        framebox2 = SurroundingRectangle(equation[2], buff=.1)

        # Create animations
        self.play(Create(framebox1))  # creating the frame

        self.wait()
        # replace frame 1 with frame 2
        self.play(ReplacementTransform(framebox1, framebox2))

        self.wait()

# manim -p -ql -i manim_test.py MovingFrame
