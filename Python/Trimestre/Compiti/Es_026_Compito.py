#1) Utilizzando le list comprehension scrivi un programma che crei una lista con tutte le potenze di due minori o uguali a un valore inserito dall’utente. Stampa la lista.

n = int(input("Inserisci un numero: "))

listaPotenze = [2**x for x in range(1,n)if(2**x <= n)]
print(listaPotenze)