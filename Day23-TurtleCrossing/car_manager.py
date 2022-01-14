from turtle import Turtle
import random

from player import MOVE_DISTANCE

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.penup()
        self.color(random.choice(COLORS))
        self.setpos(x=300, y=random.randint(-200, 200))

    def move(self, level):
        move_dist = STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT)
        new_x = self.xcor() - move_dist
        self.setpos(x=new_x, y=self.ycor())