from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("white", 14, "normal"))
