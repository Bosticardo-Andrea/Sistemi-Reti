import turtle
def quadrato(penna):
    for _ in range(4):
        penna.forward(50)
        penna.right(90)
    penna.forward(50)
    
penna = turtle.Turtle()
sfondo = turtle.Screen()
penna.speed(0)
x  = -50
for _ in range(4):
    for _ in range(4):
        quadrato(penna)
    penna.penup()
    penna.goto(0,x)
    penna.pendown()
    x += -50
sfondo.exitonclick()