from turtle import Turtle
from random import choice,randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        self.total_cars = []
        self.c_speed = STARTING_MOVE_DISTANCE
    
    
    def create_car(self):
        chance = randint(1,6)
        if chance == 1: # to avoide generating to much cars
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-260,260)
            new_car.goto(300,random_y)   
            self.total_cars.append(new_car)
        
        
    def moving_ab(self):
        for car in self.total_cars:
            car.backward(self.c_speed)    
            
    def speed_up(self):
        self.c_speed += MOVE_INCREMENT
                