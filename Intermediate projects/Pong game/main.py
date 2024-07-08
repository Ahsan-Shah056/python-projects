from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
  
# Screen setup for the game
screen =Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("--Pong Game--")
screen.tracer(0)


#Creating the objects from the classes for playing the game.
r_paddle = Paddle((370,0))   
l_paddle = Paddle((-380,0))
ball = Ball()
scoreboard = Scoreboard()

#Taking inputs from the user to play the game
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game = True

while game:
    time.sleep(ball.move_speed)# used to manipulate the balls speed during the game
    screen.update()
    ball.move()

    #if ball hits the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #when ball collides with the paddle    
    if ball.distance(r_paddle) < 50 and ball.xcor() >345 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        
        
   #if ball gets missed by right paddle
    if ball.xcor() >380:
       ball.reset_pos()  
       scoreboard.l_gain()   
     
    #if ball gets missed by right paddle   
    if ball.xcor() < -380:
        ball.reset_pos()  
        scoreboard.r_gain() 

screen.exitonclick()




 