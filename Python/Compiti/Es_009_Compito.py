#Scrivi un programma in Python che permetta all’utente di inserire le coordinate di due punti del piano cartesiano. I punti devono essere salvati all’interno di tuple. Stampa la distanza euclidea tra i due punti.
x = int(input("X: "))
y = int(input("Y: "))
x1 = int(input("X: "))
y1 = int(input("Y: "))
tupla = (x,y,x1,y1)
distanza = (((x1-x)**2) + ((y1-y)**2))**1/2
print(distanza)
