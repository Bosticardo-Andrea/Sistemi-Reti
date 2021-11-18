#Genera una lista contenente i quadrati perfetti dispari minori di 1000.
lista = []
n = 0
while (n**2 < 1000):
    if((n**2)%2 != 0):
        lista.append(n**2)
    n += 1
print(lista)
