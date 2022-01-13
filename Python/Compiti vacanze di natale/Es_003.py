2#Scrivere un programma che data una lista ne stampi una sua permutazione casuale.
import random
def doppie(l1,l2):
    for el in l1:
        k = 0
        for el1 in l2[::-1]:
            if(el == el1):
                k += 1
        if(k == 0):
            l2.append(el)
        elif(k > 1):
            l2.remove(el)
    return l2
def creazionelista():
    l = []
    n = int(input("Inserisci il numero di numeri che vuoi inserire: "))
    for _ in range(n):
        l.append(input("Inserisci elemento: "))
    return l
def main():         
    lista = creazionelista()
    while(True):
        listarandom = [random.choice(lista) for _ in lista]
        listarandom = doppie(lista,listarandom)
        print(listarandom)
        if(input("vuoi continuare[s/n]:") == "n"):
            break

if __name__== "__main__":#richiamo il main
    main()