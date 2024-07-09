from turtle import Turtle


FONT = ('Courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()  # Hide the turtle object
        self.penup()

        # Set starting score at 0.
        self.l_score = 0
        self.r_score = 0
        # self.goto(-100, 200)  # Set the position for the score
        # self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        # self.goto(100, 200)  # Set the position for the score
        # self.write(self.r_score, align="center", font=("courier", 80, "normal"))
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 200)  # Set the position for the left player's score
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)  # Set the position for the right player's score
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))


    def increase_l_score(self):
        self.l_score += 1

    def increase_r_score(self):
        self.r_score += 1


    def clear_score(self):
        self.clear()
