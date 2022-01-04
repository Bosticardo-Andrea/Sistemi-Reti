"""Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei
prezzi di alcuni generi alimentari dal Settembre 2011 a Dicembre
2016. Immagina una spesa costituita da 5 generi alimentari a tua
scelta e crea una lista contenente la serie storica del prezzo della tua
spesa ottenuta sommando i prezzi dei generi alimentari scelti.
Calcola mese / anno in cui la tua spesa ha costi minimi e massimi."""
import random

def separatore(tipologia,righe):
    posizione_alimento = {}
    i = 2
    for x in tipologia:
        posizione_alimento[x] = i
        i += 1
    mesi = {}
    for elemento in righe[1::]: 
        el = elemento.split(";")
        mesi[el[1]] = 0
    anni = {}
    for elemento in righe[1::]: 
        el = elemento.split(";")
        anni[el[0]] = 0
    return anni,mesi,posizione_alimento

def scelta(tipologia):
    print("Scegli un elemento: ")
    c = 0
    dizionario_prodotti = {}
    for x in tipologia:
        print(f"{c}. {x}")
        dizionario_prodotti[c]=x
        c += 1
    spesa = []
    for i in range(5):
        val = int(input(f"inserisi il {i} prodotto: "))
        while(dizionario_prodotti.get(val) == None):
            print("Errore")
            val = (int (input(f"inserisi il {i} prodotto: ")))
        spesa.append(dizionario_prodotti[val])
    return spesa

def main():
    f = open("./prezzi.csv","r")
    righe = f.readlines();
    f.close()

    tipologia = righe[0].split(";")
    tipologia.remove("anno")
    tipologia.remove("mese")
    frase = tipologia[-1]
    frase = frase.split("\n")
    tipologia[-1] = frase[0]

    anni,mesi,posizione_alimento = separatore(tipologia,righe)
    spesa = scelta(tipologia)

    mesiMax,mesiMin = mesi.copy(),mesi.copy()
    totSpesa = []


    print("Storico della spesa:")
    for elemento in righe[1::]: 
        el = elemento.split(";")
        totSpesa.append(float(el[posizione_alimento[spesa[0]]]) + float(el[posizione_alimento[spesa[1]]])+float(el[posizione_alimento[spesa[2]]])+float(el[posizione_alimento[spesa[3]]])+float(el[posizione_alimento[spesa[4]]]))
        print(el[0] + " - " + el[1] + " --> " + str(totSpesa[-1]))
        anni[el[0]] += totSpesa[-1]
        if(mesiMax[el[1]] < totSpesa[-1]):
            mesiMax[el[1]] = totSpesa[-1]
        if(mesi[el[1]] == 0):
            mesiMin[el[1]] = totSpesa[-1]
            mesi[el[1]] = 1
        elif((mesiMin[el[1]] > totSpesa[-1])):
            mesiMin[el[1]] = totSpesa[-1]       
    ok = True
    for anno in anni:
        if(ok == True):
            annoMax,annoMin = anni[anno],anni[anno] 
            ok = False
        if(annoMax < anni[anno]):
            annoMax = anni[anno]
        if(annoMin > anni[anno]):
            annoMin = anni[anno]
    ok = True
    for mese in mesiMax:
        if(ok == True):
            mMax = mese
            mMin = mese
            ok = False
        if(mMax < mese):
            mMax = mese
        if(mMin > mese):
            mMin = mese
    print(f"mese con la spesa maggiore {mMax}")   
    print(f"mese con la spesa minore {mMin}") 
    print(f"anno con la spesa maggiore {annoMax}")  
    print(f"anno con la spesa minore {annoMin}")   

if __name__== "__main__":#richiamo il main
    main()