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
        with open("snake_data.txt") as file:
            self.high_score = int(file.read())
        self.score_str = f"Score: {self.score} High Score: {self.high_score}"
        self.update_display()
  
    def update_display(self):
        self.clear()
        self.write(arg=self.score_str, move=False, align="center", font=("Arial", "16", "normal"))

    def inc_score(self):
        self.score += 1
        self.score_str = f"Score: {self.score} High Score: {self.high_score}"
        self.update_display()

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", "20", "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_str = f"Score: {self.score} High Score: {self.high_score}"
        self.update_display()