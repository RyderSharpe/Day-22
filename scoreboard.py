from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()  # Hide the turtle object (optional)
        self.penup()
        self.goto(0, 270)  # Set the position for the score (optional)
        self.update_score()
        #self.write(arg=f"Score: {0}", align='Left', font=('Arial', 20, 'normal'))


    def update_score(self):
        #global score
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1


    def clear_score(self):
        self.clear()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER LOSER.",align=ALIGNMENT, font=10)