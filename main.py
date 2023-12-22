from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Kelvin's Snake Game")
screen.tracer(0)

""" Storing the created class in an object """
snake = Snake()
snake_food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.14)

    snake.snake_move()

    """ Detecting collision with food. """
    if snake.snake_head.distance(snake_food) < 14:
        snake_food.refresh()
        snake.extend()
        scoreboard.increase_score()

    """ Detect collision with wall """
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    """ Detect collision with tail """
    for i in snake.full_snake_body[1:]:
        if snake.snake_head.distance(i) < 10:
            game_is_on = False
            scoreboard.game_over()

# Kelvin1 = Turtle(shape="circle")
# Kelvin1.color("white")
# Kelvin1.shapesize(1)
# Kelvin1.goto(x=-7, y=0)
#
# Kelvin2 = Turtle()
# Kelvin2.color("white")
# Kelvin2.shape("square")
# Kelvin2.shapesize(0.9)
# Kelvin2.goto(x=-20, y=0)
#
# Kelvin3 = Turtle()
# Kelvin3.color("white")
# Kelvin3.shape("square")
# Kelvin3.shapesize(0.9)
# Kelvin1.goto(x=-40, y=0)


screen.exitonclick()
