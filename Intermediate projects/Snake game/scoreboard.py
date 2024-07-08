from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        with open("data.txt",'r') as f:
            self.high_score = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update()
    
    def update(self):
        """To update the scores"""
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="left", font= ("Arial", 24, "normal"))
    
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",'w') as f:
                f.write(f"{self.high_score}")
            
            
        self.score = 0 # resetting the score    
        self.update()    
  
    
    def increase(self):
        self.score +=1
        self.update()  