#Creare una lambda function che ritorni True se una stringa è palindroma, False altrimenti.
palindroma = lambda frase :  (True if str(frase) == str(frase)[::-1] else False)

frase = input("inserisci una stringa: ")
print(palindroma(frase))
