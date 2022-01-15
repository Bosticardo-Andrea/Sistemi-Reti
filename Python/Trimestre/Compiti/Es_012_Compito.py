liste = ["ciao","come","va","tutto","bene"]
parolaLunga = liste[0]
for lista in liste:
    if(len(parolaLunga) < len(lista)):
        parolaLunga = lista
print(parolaLunga)