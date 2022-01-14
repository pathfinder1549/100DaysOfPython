from turtle import Turtle, Screen
import random

def random_color():
    """returns a random color in RGB tuple format"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
    
# tim is a turtle
tim = Turtle()
screen = Screen()
# screen.colormode(255)
# colors = ["red", "blue", "green", "yellow", "purple", "pink", "orange", "black"]


# draw a square
tim.shape("arrow")
tim.color("red")
for i in range(4):
    tim.forward(200)
    tim.right(90)

# draw a dashed line
screen.clearscreen()
tim.home()
tim.shape("arrow")
tim.color("blue")
for j in range(25):
    if j%2 == 0:
        tim.pendown()
    else:
        tim.penup()
    tim.forward(10)

# draw shapes
screen.clearscreen()
screen.colormode(255)
tim.home()
tim.shape("arrow")
for k in range(3,11):
    corner = 360/k
    for kk in range(k):
        tim.color(random_color())
        tim.forward(100)
        tim.right(corner)

# draw random path
screen.clearscreen()
screen.colormode(255)
tim.home()
tim.shape("arrow")
tim.width(5)
tim.speed(10)
for l in range(50):
    tim.setheading(random.randint(0,3) * 90)
    tim.color(random_color())
    tim.forward(20)

# draw spirograph
screen.clearscreen()
screen.colormode(255)
tim.home()
tim.speed(0)
tim.width(1)
n_circ = 150
for m in range(n_circ):
    tim.color(random_color())
    tim.setheading(360/n_circ * m)
    tim.circle(110)
    tim.home()

screen.exitonclick()


