from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.tracer(0)
screen.bgcolor("black")
mysnake = Snake()

game_not_end = True
while game_not_end:
    screen.update()
    time.sleep(0.1)
    mysnake.move()


screen.exitonclick()
