import turtle as tu

Start =[(0,0),(-20,0),(-40,0)]
MOVE_F =20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    
    
    def create_snake(self):
        for position in Start:
           self.add_segment(position)
            
            
    def add_segment(self,position):
        snake =tu.Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake) 
        
    def extend(self):
        self.add_segment(self.segments[-1].position())    
                    
    def move(self):
        for seg in range(len(self.segments)-1 ,0,-1):
            x_cor = self.segments[seg-1].xcor()
            y_cor =self.segments[seg-1].ycor()
            self.segments[seg].goto(x_cor,y_cor)
        self.head.forward(MOVE_F )
    
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)       