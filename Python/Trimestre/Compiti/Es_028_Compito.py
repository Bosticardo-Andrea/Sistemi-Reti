#3) Scrivi un programma in Python in cui chiedi all’utente un numero e comunichi se esso è divisibile per 2, oppure per 3, oppure per 5, oppure per nessuno di essi. 

num = int(input("inserisci un numero: "))
if(num%5 == 0 | num%3 == 0 | num%2 == 0):
    print("Il numero inserito é divisibile per 2/3/5")
elif(num%2 == 0 | num%5 == 0):
    print("Il numero inserito é divisibile per 2/5")
elif(num%2 == 0 | num%3 == 0):
    print("Il numero inserito é divisibile per 2/3")
elif(num%5 == 0 | num%3 == 0):
    print("Il numero inserito é divisibile per 3/5")
elif(num%2 == 0):
    print("Il numero inserito é divisibile per 2")
elif(num%3 == 0):
    print("Il numero inserito é divisibile per 3")
elif(num%5 == 0):
    print("Il numero inserito é divisibile per 5")
else:
    print("Il numero inserito non é divisibile per 2/3/5")

