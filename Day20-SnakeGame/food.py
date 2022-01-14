from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed(0)
        rand_x = random.randrange(-260, 260, 20)
        rand_y = random.randrange(-260, 260, 20)
        self.setposition(rand_x, rand_y)

    def refresh(self):
        rand_x = random.randrange(-260, 260, 20)
        rand_y = random.randrange(-260, 260, 20)
        self.setposition(rand_x, rand_y)
