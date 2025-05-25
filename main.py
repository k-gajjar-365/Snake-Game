from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Score
import time
WIDTH = 600
HEIGHT = 600
screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food.
    if snake.snakes[0].distance(food) <= 15:
       food.refresh()
       snake.extend()
       score.scoring()

    # Detect wall collision
    if snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() < -280 or snake.snakes[0].ycor() > 280 or snake.snakes[0].ycor() < -280:
        snake.reset_snake()
        score.reset_score()
        time.sleep(0.5)

    # Detect collision with its own tail
    # Slicing
    for segment in snake.snakes[1:]:
        if snake.snakes[0].distance(segment) < 10:
            snake.reset_snake()
            score.reset_score()
            time.sleep(0.5)
    
screen.exitonclick()
