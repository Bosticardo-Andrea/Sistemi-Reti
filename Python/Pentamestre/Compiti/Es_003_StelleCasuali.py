"""
Scrivere un programma in Python nel quale utilizzando il modulo turtle:
- sia presente una funzione che disegni una stella nelle coordinate x e y (passate come parametri alla funzione) 
- disegni 50 stelle sullo screen posizionate in posizioni casuali.
"""

from random import randint, random
import turtle
def stella(x,y,l,penna):
    penna.penup()
    penna.goto(x,y)
    penna.pendown()
    penna.fillcolor("#ffff00")
    penna.begin_fill()
    for _ in range(5):
        penna.forward(l)
        penna.right(180)
        penna.left(36)
    penna.end_fill()

def main():
    penna = turtle.Turtle()
    sfondo = turtle.Screen()
    sfondo.bgcolor("dark blue")
    sfondo.colormode("yellow")
    penna.speed(0)
    penna.color("#ffff00")
    turtle.setup(500,500)
    for _ in range (50):
        stella(randint(-200,200), randint (-200,200), randint(10,50),penna)
    sfondo.exitonclick()
if __name__=="__main__":
    main()