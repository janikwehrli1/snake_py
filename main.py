from turtle import Screen
import time
from snake import Snake
from snakefood import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)
screen.bgcolor("green")

mysnake = Snake()
myfood = Food()
myscore = Scoreboard()

screen.listen()
screen.onkey(mysnake.up, "Up")
screen.onkey(mysnake.down, "Down")
screen.onkey(mysnake.left, "Left")
screen.onkey(mysnake.right, "Right")

game_not_end = True
while game_not_end:
    screen.update()
    time.sleep(0.1)
    mysnake.move()

    if mysnake.head.distance(myfood) < 20:
        print("num")
        myfood.random_location()
        mysnake.extend()
        myscore.score_increase()
        myscore.update_scoreboard()


    if mysnake.head.xcor() > 280 or mysnake.head.xcor() < -280 or mysnake.head.ycor() > 280 or mysnake.head.ycor() < -280:
        myscore.reset()
        mysnake.reset()

    for i in mysnake.segments[1:]:
        if mysnake.head.distance(i) < 10:
            myscore.reset()
            mysnake.reset()
screen.exitonclick()
