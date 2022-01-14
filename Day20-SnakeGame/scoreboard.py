from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.setposition(x=0, y= 260)
        self.score = 0
        self.score_str = f"Score = {self.score}"
        self.update_display(self.score_str)
  
    def update_display(self, score_str):
        self.clear()
        self.write(arg=score_str, move=False, align="center", font=("Arial", "16", "normal"))

    def inc_score(self):
        self.score += 1
        self.score_str = f"Score = {self.score}"
        self.update_display(self.score_str)

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", "20", "normal"))