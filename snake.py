from turtle import Turtle

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
up = 90
right = 0
down = 270
left = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in starting_pos:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.goto(i)
            self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)