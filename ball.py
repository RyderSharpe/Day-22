from turtle import Turtle

# Constants
WIDTH = 1
HEIGHT = 1   # All turtles start out as 20 x 20, therefore width to be stretched by 5 to achieve 100 pixels
BALL_X_SPEED = 3
BALL_Y_SPEED = 1
SPEED_INCREMENT = 0.9  # Speed increases by reducing the sleep time by this factor

class Ball(Turtle):


    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.color("white")
        self.penup()
        self.goto(xpos, ypos)
        self.x_move = BALL_X_SPEED
        self.y_move = BALL_Y_SPEED
        self.move_speed = 0.01 # Initialize ball speed when game starts


    def ball_move(self):
        # Update x and y coordinates for diagonal movement (adjust values for desired speed)
        new_x = self.xcor() + self.x_move  # Move right
        new_y = self.ycor() + self.y_move  # Move up
        # Update the ball's position
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= SPEED_INCREMENT  # Increase the ball's speed

    def out_of_bounds(self):
        # Ball resets to middle
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    # def speed(self):
    #     self.x_move += 1
    #     self.y_move += 0.5
