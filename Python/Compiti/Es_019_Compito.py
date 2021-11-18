#Creare una lambda function che ritorni True se una stringa inizia con lettera maiuscola, False altrimenti. 
maiuscolo = lambda lettera : True if((lettera >= 'A') & (lettera <= 'Z')) else False

frase = input("inserisci una stringa: ")
print(maiuscolo(frase[0]))
