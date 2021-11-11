#Le if
#parole chiave : if/elif/else
voto = int(input("inserisci un voto: "))
if (voto >= 8):
    print("Eccellente")
elif (voto >= 6) & (voto < 8):
    print("Buono")
elif (voto >= 6 ) & (voto < 7 ):
    print("sufficente")
else:
    print("insufficente")
