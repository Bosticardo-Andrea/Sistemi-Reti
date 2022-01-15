#4) Scrivi un programma in Python che chieda all'utente un numero intero n e disegni, tramite turtle, il poligono regolare a n lati.
import turtle
poligono = turtle.Turtle()
sfondo = turtle.Screen()
lati = int(input("Inserisci il numero di lati: "))
angolo = 360/lati
for _ in range (lati):  
    poligono.forward(50)
    poligono.right(angolo)
sfondo.exitonclick()