"""
Scrivere un programma in Python nel quale utilizzando il modulo turtle:
- sia presente una funzione che disegni una stella nelle coordinate x e y (passate come parametri alla funzione) 
- disegni 50 stelle sullo screen posizionate in posizioni casuali.
"""
import random
import turtle
import Stella as s
def main():
    stella = s.Stella(0)
    sfondo = turtle.Screen()
    sfondo.bgcolor("dark blue")
    sfondo.colormode("yellow")
    turtle.setup(500,500)
    for i in range (50):
        stella.show(random.randint(-200,200), random.randint (-200,200), random.randint(10,40))
    sfondo.exitonclick()
if __name__=="__main__":
    main()