import turtle
class Stella():
    def __init__(self,speed):
        self.penna = turtle.Turtle()
        self.penna.fillcolor("#ffff00")
        self.penna.speed(speed)
        self.penna.color("#ffff00") 
         
    def show(self,x,y,l):
        self.penna.penup()
        self.penna.goto(x,y)
        self.penna.pendown()
        self.penna.begin_fill()
        for _ in range(5):
            self.penna.forward(l)
            self.penna.right(180)
            self.penna.left(36)
        self.penna.end_fill()