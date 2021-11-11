operazioni = ["divisione","moltiplicazione","addizione", "sottrazione"]
print(operazioni)
scelta = input("Inserisci l'operazione aritmetica che vuoi fare:" )
x = int(input("numero 1: "))
y = int(input("numero 2: "))
risultato = 0
if scelta == operazioni[0]:
    if(y ==0):
        risultato = "impossibile"
    elif(x == 0 & y ==0):
        risultato = "indefinito"
    else:
        risultato = x/y
elif scelta == operazioni[1]:
    risultato = x*y
elif scelta == operazioni[2]:
    risultato = x+y
elif scelta == operazioni[3]:
    risultato = x-y
    
print(f"Il risultato vale: {risultato}")