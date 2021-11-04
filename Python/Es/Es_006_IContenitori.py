#I contenitori

#tupla
tupla = (3,6,-1,10)#tupla di 4 elementi
print(f"tupla: {tupla}") 
print(tupla[0])#primo elemento
#tupla[0]=5 --> non si puó fare é immutabile

#lista
lista = [3,3.1415,"ciao"]#possono avere tipi diversi al loro interno
print(f"lista: {lista}")
numeri_primi = [2,3,5,7,11,13]
print(lista[-1])
lista[0] = 4.5
print(lista) #posso fare slicing come per le stringhe
numeri_primi.append(17)
print(numeri_primi)
print(f"La lunghezza vale {len(numeri_primi)}")

altri_numeri_primi = [19,23,29] 
molti_nuemri_primi = numeri_primi + altri_numeri_primi #concateno le liste
print(molti_nuemri_primi)
print(2*altri_numeri_primi)#ripete 2 volte la lista 

#ciclo for
for numero_primo in numeri_primi:
    print(numero_primo,end="-")#,end="carattere separatore", puó essere qualsiasi cosa
print("FINE")
    
#dizionari
dizionario = {"to get": "prendere", "hello":"ciao","print":"stampa"}#ogni elemento é separato da una virgola e ogni elemento é c'é una chiave e un valore
print(dizionario["hello"])#accedo per chiave

