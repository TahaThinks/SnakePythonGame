from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

with open("data.txt", mode="r") as file:
    score = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = score
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
