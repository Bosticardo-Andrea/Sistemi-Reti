#Scrivere un programma che data una lista qualsiasi ne elimini i duplicati.
def creazionelista():
    l = []
    n = int(input("Inserisci il numero di numeri che vuoi inserire: "))
    for _ in range(n):
        l.append(input("Inserisci elemento: "))
    return l

def main():
    lista = creazionelista()
    for k in range(len(lista)):
        for el in lista[k+1:]:
            if(lista[k] == el):
                lista[k] = "-"
    print(lista)

if __name__== "__main__":#richiamo il main
    main()