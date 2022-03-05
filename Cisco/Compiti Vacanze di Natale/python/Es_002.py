#Scrivere un programma che data una lista qualsiasi la trasformi in un dizionario avente come chiavi gli indici della lista e come valori gli elementi.
def creazionelista():
    l = []
    n = int(input("Inserisci il numero di numeri che vuoi inserire: "))
    for _ in range(n):
        l.append(input("Inserisci elemento: "))
    return l
#compriension di dizionari --> dict = {x: elemento for k, elemento in enumerate(lista)}
def main():
    lista = creazionelista()
    dict = {}
    for k, elemento in enumerate(lista):#ho sia l'indice che l'elemento
    #for k in range(len(lista)):
        #dict [k] = lista[k]
        dict[k] = elemento
    print(dict)

if __name__== "__main__":#richiamo il main
    main()