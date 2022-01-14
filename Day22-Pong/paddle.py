from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_loc, y_loc):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(x=x_loc, y=y_loc)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)