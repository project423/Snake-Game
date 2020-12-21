from turtle import Screen

from time import sleep

from snake import Snake
from food import Food
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 600

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.tracer(0)

screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    sleep(.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.add_one()
        snake.extend()
    
    #Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect Collision with Tail

    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 15:
            scoreboard.game_over()
            game_is_on = False














screen.exitonclick()