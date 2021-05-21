from turtle import Turtle
START_ANGLE = 2


class Ball:
    def __init__(self):
        self.ball = []
        self.create_ball()

    def move_ball(self):
        self.ball[0].goto(0, 0)
        self.ball[0].setheading(self.ball[0].heading() + 180)

    def create_ball(self):
        ball = Turtle("circle")
        ball.color("white")
        ball.penup()
        self.ball.append(ball)
        self.ball[0].left(START_ANGLE)

    def move(self):
        self.ball[0].forward(20)

    def bounce1(self):
        """ Bounce from the top wall"""
        if self.ball[0].ycor() >= 380:
            self.ball[0].forward(0)
            self.ball[0].right(self.ball[0].heading() * 2)

    def bounce2(self):
        """ Bounce from the bottom wall"""
        if self.ball[0].ycor() <= -380:
            self.ball[0].forward(0)
            self.ball[0].left((180 - (self.ball[0].heading() / 2)) * 4)

    def bounce3(self):
        """ Bounce from the bottom part of the platform B"""
        self.ball[0].forward(0)
        self.ball[0].right(182 - self.ball[0].heading())

    def bounce4(self):
        """ Bounce from the bottom part of the platform A"""
        self.ball[0].forward(0)
        self.ball[0].right(self.ball[0].heading() + 358)

    def bounce5(self):
        """ Bounce from the top part of the platform A"""
        self.ball[0].forward(0)
        self.ball[0].right((self.ball[0].heading() * 2) + 182)

    def bounce6(self):
        """ Bounce from the top part of the platform B"""
        self.ball[0].forward(0)
        self.ball[0].left(182 - (self.ball[0].heading() * 2))

    def bounce7(self):
        """ Bounce from the top part of the platform B"""
        self.ball[0].forward(0)
        self.ball[0].left((self.ball[0].heading() * 2) + 182)

    def direction(self):
        return self.ball[0].heading()

    def position_x(self):
        return self.ball[0].xcor()

    def position_y(self):
        return self.ball[0].ycor()

