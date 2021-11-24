#Creare una lambda function che ritorni True se una stringa è palindroma, False altrimenti.
palindroma = lambda frase : str(frase) == str(frase)[::-1]
frase = input("inserisci una stringa: ")
print(palindroma(frase))
