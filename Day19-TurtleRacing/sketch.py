from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def turn_cw():
    tim.right(10)

def turn_ccw():
    tim.left(10)

def move_backwards():
    tim.backward(10)

def reset_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

tim.shape("arrow")

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_ccw)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_cw)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()
