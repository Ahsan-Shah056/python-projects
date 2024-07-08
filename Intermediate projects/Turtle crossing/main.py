import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_m= CarManager()
score_b= Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")

game = True
while game:
    time.sleep(0.07)
    screen.update()

    car_m.create_car()
    car_m.moving_ab()
    
    
    # time to check the collision of cars with our turtle
    for car in car_m.total_cars:
       if car.distance(player) < 20:
            game = False
            score_b.endgame()
 
    if player.at_end():
        player.reset_game()
        car_m.speed_up()
        score_b.level_up() 
screen.exitonclick()            