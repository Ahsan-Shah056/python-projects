from turtle import *
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_lvl()
        
    def update_lvl(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left' , font = FONT) 
    
        
    def level_up(self):
        self.level +=1 
        self.update_lvl()
        
    def endgame(self):
        self.goto(0,0)
        self.write("Game over ", align='center' , font = FONT) 
            
        
