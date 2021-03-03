from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.high_score = file.read()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):

        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()