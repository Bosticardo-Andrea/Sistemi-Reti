#lista = [k*n for k in range(11) for n in range (11)]
tavola = [[x*y for x in range (11)]for y in range(11)]
print(tavola)
'''
indice1 = 0
indice2 = 11
for _ in range(11):
    print(lista[indice1 : indice2])
    indice1 += 11
    indice2 += 11
    '''