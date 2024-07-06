from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update()
    
    def update(self):
        self.write(f"Score: {self.score}", align="left", font= ("Arial", 24, "normal"))
    
    def game_end(self):
        self.goto(0,0)
        self.write(f"Game over buddy.", align="left", font= ("Arial", 24, "normal"))
    
    def increase(self):
        self.score +=1
        self.clear()  
        self.update()  