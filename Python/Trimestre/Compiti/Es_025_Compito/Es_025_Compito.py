#3)Scrivi un programma Python che chieda all’utente i suoi dati anagrafici (nome, cognome, data di nascita), 
#li salvi all’interno di un dizionario e infine salvi il dizionario su un file, elemento per elemento.
f = open("./Persona","w")
n = int(input("Quante persone vuoi inserire?: "))
persona = [{"nome":input("inserisci il tuo nome: "),"cognome":input("inserisci il tuo cognome: "),"data":input("inserisci la tua data di nascita [xx/xx/xxxx]: ")} for k in range(n)]
for x in range (n):
    f.write("nome: " + persona[x]["nome"] +"\n")
    f.write("cognome: " + persona[x]["cognome"]+"\n")
    f.write("data: " + persona[x]["data"]+"\n")
    f.write("\n")
f.close()