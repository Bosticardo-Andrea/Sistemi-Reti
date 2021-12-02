#Creare una lambda function che ritorni True se una stringa inizia con lettera maiuscola, False altrimenti. 
maiuscolo = lambda lettera :(lettera >= 'A') & (lettera <= 'Z')
frase = input("inserisci una stringa: ")
print(maiuscolo(frase[0]))
