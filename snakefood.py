from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(1, 1)
        rand1 = random.randint(-280, 280)
        rand2 = random.randint(-280, 280)
        self.goto(rand1, rand2)

    def random_location(self):
        rand1 = random.randint(-280, 280)
        rand2 = random.randint(-280, 280)
        self.goto(rand1, rand2)
