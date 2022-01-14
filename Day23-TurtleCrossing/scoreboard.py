from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.speed(0)
        self.setpos(x=-250, y=250)
        self.level = 1
        self.level_str = "Level: " + str(self.level)
        self.write(self.level_str, move=False, align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_score()

    def reset_level(self):
        self.level = 1
        self.update_score()
    
    def update_score(self):
        self.level_str = "Level: " + str(self.level)
        self.clear()
        self.write(self.level_str, move=False, align="left", font=FONT)
    
    def game_over(self):
        self.setpos(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)