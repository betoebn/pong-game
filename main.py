from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(canvwidth=640, canvheight=640)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle([(-440, -30), (-440, -10), (-440, 10), (-440, 30)])
paddle2 = Paddle([(440, -30), (440, -10), (440, 10), (440, 30)])
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle2.down, "Down")
screen.onkeypress(paddle2.up, "Up")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()

    if 0 <= ball.direction() <= 90 or 90 <= ball.direction() <= 180:
        ball.bounce1()
        for i in range(0, 1):
            if paddle2.segments[i].distance(ball.position_x(), ball.position_y()) < 20:
                ball.bounce3()
            if paddle1.segments[i].distance(ball.position_x(), ball.position_y()) < 20:
                ball.bounce4()
        for i in range(2, 3):
            if paddle1.segments[i].distance(ball.position_x(), ball.position_y()) < 20:
                ball.bounce5()
            if paddle2.segments[i].distance(ball.position_x(), ball.position_y()) < 20:
                ball.bounce6()

    if 270 <= ball.direction() <= 360 or 180 <= ball.direction() <= 270:
        ball.bounce2()
        for i in range(0, 1):
            if paddle2.segments[i].distance(ball.position_x(), ball.position_y()) < 20:
                ball.bounce5()
            if paddle1.segments[i].distance(ball.position_x(), ball.position_y()) < 20:
                ball.bounce5()
        for i in range(2, 3):
            if paddle1.segments[i].distance(ball.position_x(), ball.position_y()) < 20:
                ball.bounce7()
            if paddle2.segments[i].distance(ball.position_x(), ball.position_y()) < 20:
                ball.bounce3()

    if ball.position_x() >= 460:
        scoreboard.score1 += 1
        scoreboard.track_score()
        ball.move_ball()
    if ball.position_x() <= -460:
        scoreboard.score2 += 1
        scoreboard.track_score()
        ball.move_ball()

screen.exitonclick()
