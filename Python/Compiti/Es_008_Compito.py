#Scrivi un programma in Python che permetta all’utente di inserire il suo nome (tramite input) e stampi il nome in cui tutti i caratteri tranne il primo sono sostituiti da un *
nome = input("inserisci il tuo nome: ")
print(nome[0],end="*"*(len(nome)-1))
