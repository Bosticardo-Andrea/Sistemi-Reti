numeroDiNumeri = int(input("Quanti numeri vuoi inserire: "))
lista = []
while(numeroDiNumeri > 0):    
    numero = int(input("Inserisci un numero: "))
    lista.append(numero)
    numeroDiNumeri = numeroDiNumeri -1
print(lista)
