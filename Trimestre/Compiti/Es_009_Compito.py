#Scrivi un programma in Python che permetta all’utente di inserire le coordinate di due punti del piano cartesiano. I punti devono essere salvati all’interno di tuple. Stampa la distanza euclidea tra i due punti.
x = float(input("X: "))
y = float(input("Y: "))
x1 = float(input("X: "))
y1 = float(input("Y: "))
punto = (x,y)
punto1 = (x1,y1)
differenzaX = punto[0] - punto1[0]
differenzaY = punto[1] - punto1[1]
distanza = (((differenzaX)**2) + ((differenzaY)**2))**(1/2)
print(distanza)
