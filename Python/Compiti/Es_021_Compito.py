#Data una lista di stringhe estrai da essa la lista di stringhe che sono palindrome e la lista di stringhe che hanno iniziale maiuscola.

palindroma = lambda frase :  (True if str(frase) == str(frase)[::-1] else False)
maiuscolo = lambda lettera : True if((lettera >= 'A') & (lettera <= 'Z')) else False

lista = ["Ciao","anna","Come","otto","tutti","Ingegni"]
palindrome = [nome for nome in lista if palindroma(nome.lower())]
maiuscole = [nome for nome in lista if maiuscolo(nome)]


print(lista)
print(f"Le parole palindrome sono: {palindrome} quelle maiuscole {maiuscole}")