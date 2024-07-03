from turtle import Turtle

# Constants
WIDTH = 1
HEIGHT = 5  # All turtles start out as 20 x 20, therefore width to be stretched by 5 to achieve 100 pixels


class Paddles(Turtle):

    def __init__(self,x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
