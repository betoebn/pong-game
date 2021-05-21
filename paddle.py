from turtle import Turtle
UP = 90
DOWN = 270


class Paddle:
    def __init__(self, starting_position):
        self.position = starting_position
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in self.position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def up(self):
        for segment in self.segments:
            segment.setheading(UP)
            segment.forward(20)

    def down(self):
        for segment in self.segments:
            segment.setheading(DOWN)
            segment.forward(20)
