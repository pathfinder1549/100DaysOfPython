from turtle import Screen
from food import Food
from scoreboard import Scoreboard 
from snake import Snake
import time

scrn = Screen()
scrn.setup(width=600, height=600)
scrn.bgcolor("black")
scrn.title("SNAKE GAME")
scrn.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scrn.listen()
scrn.onkey(snake.heading_east,"Right")
scrn.onkey(snake.heading_north, "Up")
scrn.onkey(snake.heading_west, "Left")
scrn.onkey(snake.heading_south, "Down")

game_running = True

while game_running:
    scrn.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh()
        scoreboard.inc_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_running = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()

scrn.exitonclick()