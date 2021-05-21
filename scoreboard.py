from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 360)
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"{self.score1}  Score  {self.score2}", move=False, align="center", font=("Arial", 25, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Your score is: {self.score1 - 1}", move=False, align="center", font=("Arial", 20, "normal"))