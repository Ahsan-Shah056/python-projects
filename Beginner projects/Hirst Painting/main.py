import turtle 
import random

turtle.colormode(255)
shack = turtle.Turtle()
shack.speed("fastest")
shack.penup()
shack.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
shack.setheading(225)
shack.forward(300)
shack.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    shack.dot(20, random.choice(color_list))
    shack.forward(50)

    if dot_count % 10 == 0:
        shack.setheading(90)
        shack.forward(50)
        shack.setheading(180)
        shack.forward(500)
        shack.setheading(0)









screen = turtle.Screen()
screen.exitonclick()