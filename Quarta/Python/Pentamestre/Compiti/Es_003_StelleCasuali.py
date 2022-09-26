"""
Scrivere un programma in Python nel quale utilizzando il modulo turtle:
- sia presente una funzione che disegni una stella nelle coordinate x e y (passate come parametri alla funzione) 
- disegni 50 stelle sullo screen posizionate in posizioni casuali.
"""
import random
import turtle
def stella(x,y,l,penna):
    penna.penup()
    penna.goto(x,y)
    penna.pendown()
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
    penna.fillcolor("#ffff00")
    penna.speed(0)
    penna.color("#ffff00")
    turtle.setup(500,500)
    for _ in range (50):
        stella(random.randint(-250,250), random.randint (-250,250), random.randint(10,30),penna)
    sfondo.exitonclick()
    
if __name__=="__main__":
    main()