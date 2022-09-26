#Scrivere un programma che data una lista qualsiasi la trasformi in un dizionario avente come chiavi gli indici della lista e come valori gli elementi.
def creazionelista():
    l = []
    n = int(input("Inserisci il numero di numeri che vuoi inserire: "))
    for _ in range(n):
        l.append(input("Inserisci elemento: "))
    return l

def main():
    lista = creazionelista()
    dict = {}
    for k in range(len(lista)):
        dict [k+1] = lista[k]
    print(dict)

if __name__== "__main__":#richiamo il main
    main()