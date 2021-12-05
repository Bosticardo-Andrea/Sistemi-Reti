#5) Scrivi un programma in Python che chieda all'utente un numero intero n. Il programma deve creare una lista contente due diverse turtle, orientate in direzioni opposte. Ciascuna turtle disegna poi il poligono regolare a n lati.
import turtle
poligono = turtle.Turtle()
poligono1 = turtle.Turtle()
sfondo = turtle.Screen()

turtles = [poligono,poligono1]
lati = int(input("Inserisci il numero di lati: "))
angolo = 360/lati
for _ in range (lati):  
    turtles[0].forward(50)
    turtles[1].forward(50)
    turtles[0].right(angolo)
    turtles[1].left(angolo)
sfondo.exitonclick()