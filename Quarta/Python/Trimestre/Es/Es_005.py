stringa = "classe quarta A robotica"
#stringa[15] = 'B'
print(stringa)
#le stringhe in python sono IMMUTABILI --> non si possono cambiare
stringa_nuova = stringa[0:14] + "B" + stringa[15:]
print(stringa_nuova)
print(print)
#assegnazione multipla
a,b=4,7
print(f"a vale {a} e b vale {b}")
#scambio
a,b=b,a
print(f"a vale {a} e b vale {b}")