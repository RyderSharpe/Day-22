from turtle import Turtle

# Constants
WIDTH = 1
HEIGHT = 1   # All turtles start out as 20 x 20, therefore width to be stretched by 5 to achieve 100 pixels

BALL_SPEED = 3

class Ball(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.color("white")
        self.penup()
        self.goto(xpos, ypos)

    def ball_move(self):
        # Get current coordinates
        current_x = self.xcor()
        current_y = self.ycor()

        # Update x and y coordinates for diagonal movement (adjust values for desired speed)
        new_x = current_x + BALL_SPEED  # Move right
        new_y = current_y + BALL_SPEED  # Move up

        # Update the ball's position
        self.goto(new_x, new_y)


