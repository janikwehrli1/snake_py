from turtle import Screen, Turtle
import time
from snake import Snake
from snakefood import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)
screen.bgcolor("green")

mysnake = Snake()
myfood = Food()

screen.listen()
screen.onkey(mysnake.up,"Up")
screen.onkey(mysnake.down, "Down")
screen.onkey(mysnake.left,"Left")
screen.onkey(mysnake.right,"Right")


game_not_end = True
while game_not_end:
    screen.update()
    time.sleep(0.1)
    mysnake.move()



screen.exitonclick()
