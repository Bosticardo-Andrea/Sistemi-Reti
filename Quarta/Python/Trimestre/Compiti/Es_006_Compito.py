x = float (input("primo numero: "))
y = float (input("secondo numero: "))
lista = []
lista.append(x**2+y**2)
lista.append((x+y)**2)
lista.append(x**2/y**2)
lista.append((x/y)**2)
print(lista)