#il for
classi = ["4Arob","3Arob","2Achi","3AInf"]
indirizzi = {"rob":"Smart-robot","chi":"chimica","Inf":"Informatica"}

for indice, classe in enumerate(classi): #cicla sia sul valore che sul indice devo usare 2 variabili
    print(f"La classe numero {indice+1}° é {classe} é dell'indirizzo {indirizzi[classe[-3:]]}",end = "\n\n")
    
    
for numero in range(2,23):
    print(numero)
