from turtle import Turtle, Screen, forward

turt = Turtle()
scrn = Screen()

def move_forward():
    turt.forward(50)

scrn.listen()
scrn.onkeypress(move_forward,"space")
scrn.exitonclick()