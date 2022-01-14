import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scrn = Screen()
scrn.setup(width=600, height=600)
scrn.tracer(0)

player = Player()
scoreboard = Scoreboard()

scrn.listen()
scrn.onkeypress(player.move, "w")

car_list = []

game_running = True
while game_running:

    if random.randint(0,9) > 7:
        new_car = CarManager()
        car_list.append(new_car)

    if player.ycor() > 280:
        player.reset_pos()
        scoreboard.next_level()
    
    for car in car_list[:]:
        car.move(scoreboard.level)
        if player.distance(car) < 30:
            game_running = False
            scoreboard.game_over()
        if car.xcor() < -300:
            car_list.remove(car)

    time.sleep(0.1)
    scrn.update()

scrn.exitonclick()