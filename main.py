# TODO-1: Create the screen. DONE.
# TODO-2: Create and move the paddle. DONE.
# TODO-3: Create another paddle. DONE.
# TODO-4: Create the ball and make it move. DONE
# TODO-5: Detect collision with top & bottom wall and bounce. Done*
# TODO-6: Detect collision with paddle.
# TODO-7: Detect when paddle misses.
# TODO-8: Keep score.

from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # Turns off animation. Requires manually updating screen. ie screen.update()

# Score
scoreboard = Score()


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

# Screen
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


x = 5
game_is_on = True
while game_is_on:

    # game_speed = 0.1 / x  # Smaller = faster
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()  # Added to move the ball

    # Detect collision with top & bottom wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        # x += 5

    # Detect ball out of bounds for right player.
    if ball.xcor() > 390:
        # x = 5
        ball.out_of_bounds()
        scoreboard.increase_l_score()
        scoreboard.update_score()

    # Detect ball out of bounds for left player.
    if ball.xcor() < -390:
        # x = 5
        ball.out_of_bounds()
        scoreboard.increase_r_score()
        scoreboard.update_score()

screen.exitonclick()
