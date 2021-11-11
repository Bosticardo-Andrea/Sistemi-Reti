def massimo(lista):
    max = lista[0]
    for numero in lista:
        if(max < numero):
            max = numero
    return max

lista = [5,8,9,7,1,0,11]
max = massimo(lista)
print(f"il massimo della lista é {max}")