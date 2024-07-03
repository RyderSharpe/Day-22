# TODO-1: Create the screen. DONE.
# TODO-2: Create and move the paddle. DONE.
# TODO-3: Create another paddle. DONE.
# TODO-4: Create the ball and make it move.
# TODO-5: Detect collision with wall and bounce.
# TODO-6: Detect collision with paddle.
# TODO-7: Detect when paddle misses.
# TODO-8: Keep score.

from turtle import Screen
from paddles import Paddles
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # Turns off animation. Requires manually updating screen. ie screen.update()

# Define initial positions for the paddles
X_POS_P1 = 350
Y_POS_P1 = 0
X_POS_P2 = -350
Y_POS_P2 = 0

# Create two paddles with their respective positions
r_paddle = Paddles(X_POS_P1, Y_POS_P1)  # Right paddle
l_paddle = Paddles(X_POS_P2, Y_POS_P2)  # Left paddle
# random_paddle = Paddles(0, 0) # FYI, We can create as many paddles as we want.

# Create the ball and set it to the center of the screen.
BALL_X_POS = 0
BALL_Y_POS = 0
ball = Ball(BALL_X_POS, BALL_Y_POS)


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_speed = 0.1


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    ball.ball_move()


screen.exitonclick()
