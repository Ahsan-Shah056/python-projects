import turtle as tu
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen =tu.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("OG Snake Game")
screen.tracer(0)
snake = Snake()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

food = Food()
scoreboard = Scoreboard()
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Checking collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance (segment) <10:
            snake.reset()





screen.exitonclick()
