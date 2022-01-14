from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scrn = Screen()
scrn.setup(width=800, height=600)
scrn.bgcolor("black")
scrn.title("Pong")
scrn.tracer(0)

comp_paddle = Paddle(x_loc=350, y_loc=0)
user_paddle = Paddle(x_loc=-350, y_loc=0)
ball = Ball()

scoreboard = Scoreboard()

scrn.listen()
scrn.onkeypress(user_paddle.move_up, "w")
scrn.onkeypress(user_paddle.move_down, "s")
scrn.onkeypress(comp_paddle.move_up, "Up")
scrn.onkeypress(comp_paddle.move_down, "Down")

game_running = True

while game_running:

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 385:
        scoreboard.inc_l()
        ball.home()

    if ball.xcor() < -385:
        scoreboard.inc_r()
        ball.home()

    if (ball.distance(comp_paddle) < 50 and ball.xcor() > 325) or \
        (ball.distance(user_paddle) < 50 and ball.xcor() < -325):
            ball.bounce_x()
            ball.inc_speed()


    scrn.update()
    time.sleep(0.05)
    # tutorial reduces sleep timer to increase speed
    # DONT TIE GAME FUNCTION TO FRAME RATE!

scrn.exitonclick()