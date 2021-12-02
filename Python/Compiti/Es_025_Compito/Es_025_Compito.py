#3)Scrivi un programma Python che chieda all’utente i suoi dati anagrafici (nome, cognome, data di nascita), 
#li salvi all’interno di un dizionario e infine salvi il dizionario su un file, elemento per elemento.
persona = {"nome":input("inserisci il tuo nome "),"cognome":input("inserisci il tuo cognome "),"data":input("inserisci la tua data di nascita ")}
f = open("./Persona","w")
f.write("nome: " + persona["nome"] +"\n")
f.write("cognome: " + persona["cognome"]+"\n")
f.write("data: " + persona["data"]+"\n")
f.close()