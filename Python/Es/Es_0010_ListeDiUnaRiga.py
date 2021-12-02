dispari = [k for k in range(0,1000)if(k%2 != 0)]
#print(dispari)

nomi = ["Marco","luca","Mario","Matteo","lucia"]
nomi_m = [nome for nome in nomi if(nome[0]== "M")]
nome_l = [p for p in nomi if(p[0] == "l")]
print(nome_l)
print(nomi_m)