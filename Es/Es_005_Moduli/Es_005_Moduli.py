from collections import deque
import Pile_Code as pc #alias = sinonimo

#p = Pile_Code.Pila() --> senza alias
p = pc.Pila()
c = pc.Coda()
n = int(input("Inserisci il numero di numeri: "))
for _ in range (n):
    c.enqueue(input("Cosa vuoi inserire: "))
      
c.print()