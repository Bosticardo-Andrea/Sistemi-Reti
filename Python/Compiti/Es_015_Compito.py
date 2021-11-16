def massimo(lista):
    max = lista[0]
    min = lista[0]
    for numero in lista:
        if(max < numero):
            max = numero
        if(min > numero):
            min = numero
    return max,min

lista = [5,8,9,7,1,0,11]
max_min = massimo(lista)
print(f"il massimo della lista é {max_min}")