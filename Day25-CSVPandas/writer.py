from turtle import Turtle

FONT = ("Ariel", 12, "normal")

class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.speed(0)

    def write_state(self, name, x, y):
        self.setpos(x, y)
        self.write(name, align="center", font=FONT)