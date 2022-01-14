from turtle import Turtle, Screen
import random

scrn = Screen()
scrn.setup(500,400)
user_bet = scrn.textinput("Make A Bet", "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
roster = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=(-75+30*i))
    roster.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turt in roster:
        if turt.xcor() > 230:
            race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet.lower():
                print(f"You win! The {winning_color} turtle came in first!")
            else:
                print(f"You lose. The {winning_color} turtle came in first.")

        rand_distance = random.randint(0,10)
        turt.forward(rand_distance)

scrn.exitonclick()