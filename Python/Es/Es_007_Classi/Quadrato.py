import turtle
class Quadrato():
    #x,y sono le coordinate del vertice in alto a sinistra
    def __init__(self,x,y,lato):
        self.lato=lato
        self.x = x
        self.y = y
        
    def getArea(self):
        return self.lato**2
    
    def getPerimetro(self):
        return self.lato * 4
    
    def IsAppartiene(self,x,y):
        return((x >= self.x & x <= (self.x+self.lato)) & ((y >= self.y) & (y <= self.y-self.lato)))
    
    def Draw(self):
       pen = turtle.Turtle()
       screen = turtle.Screen()
       pen.goto(self.x,self.y)
       for _ in range(4):
            pen.forward(self.lato)
            pen.right(90)    