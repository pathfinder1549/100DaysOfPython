from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.penup()
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(x=new_x, y=new_y)

    def bounce_x(self):
        self.x_move *= -1
    
    def bounce_y(self):
        self.y_move *= -1

    def home(self):
        self.setpos(0,0)
        self.reset_speed()
        self.bounce_x()

    def inc_speed(self):
        self.x_move *= 1.2
        self.y_move *= 1.2
    
    def reset_speed(self):
        self.x_move = 10
        self.y_move = 10