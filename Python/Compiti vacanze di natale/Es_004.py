#made by Andrea Bosticardo
import os #per pulire lo schermo dopo ogni turno
import random
def controllo(x,g,griglia,giocatori):
    numero = [0,7,14,21,28,35]
    """Si effettua il controllo del numero inserito:
     - Nel caso la colonna sia piena
     - Nel caso il numero non si corretto < 0 o > 6"""
    while((x < 0 or x > 6)):
        x = int(input("Numero non valido:"))
    k = len(numero)-1#contatore che parte dal fondo per posizioanre la pedina sopra l'altra
    ok = False
    while((k >= 0) & (ok == False)):
        cella = x + numero[k]
        if(griglia[cella] == " "):#contrllo se la colonna non é piena
            ok = True #esco dal ciclo
        elif(griglia[x] != " "):#colonna piena
            print("fine colonna")#faccio cambiare la colonna e e
            z = x
            while(z == x):
                x = int(input("Numero non valido:"))#controllo che il numero sia valido
                k = len(numero)#resetto il contatore
        k -= 1
    griglia[cella] = giocatori[g]#posiziono la mossa del giocatore al fondo = gravitá       
def disegnaGriglia(griglia,giocatori,g1,g2):
    """Disegno la griglia con i giocatori che si sfidano"""
    print(f"{g1} [{giocatori[g1]}] vs {g2} [{giocatori[g2]}]\n")
    print(" 0   1   2   3   4   5   6")
    print(f" {griglia[0]} | {griglia[1]} | {griglia[2]} | {griglia[3]} | {griglia[4]} | {griglia[5]} | {griglia[6]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[7]} | {griglia[8]} | {griglia[9]} | {griglia[10]} | {griglia[11]} | {griglia[12]} | {griglia[13]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[14]} | {griglia[15]} | {griglia[16]} | {griglia[17]} | {griglia[18]} | {griglia[19]} | {griglia[20]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[21]} | {griglia[22]} | {griglia[23]} | {griglia[24]} | {griglia[25]} | {griglia[26]} | {griglia[27]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[28]} | {griglia[29]} | {griglia[30]} | {griglia[31]} | {griglia[32]} | {griglia[33]} | {griglia[34]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[35]} | {griglia[36]} | {griglia[37]} | {griglia[38]} | {griglia[39]} | {griglia[40]} | {griglia[41]}")
    print("---------------------------------------------------------------------------")
def vittoria(griglia):
    """controllo tutte i  possibili casi in cui si puó vincere"""
    numero = [0,7,14,21,28,35]
    vittoria = False
    
    #controllo lineare
    for i in range(6):
        for k in range(4):
            x = 0
            x = k + numero[i]
            if ((griglia[x]==griglia[x+1]==griglia[x+2]==griglia[x+3]) & (griglia[x]!=" ")):
                vittoria = True   
                
    #controllo collona
    for i in range(7):
        for k in range(3):
            x = i + numero[k]
            if ((griglia[x]==griglia[x+numero[1]]==griglia[x+numero[2]]==griglia[x+numero[3]]) & (griglia[x]!=" ")):
                vittoria = True
                
    #controllo digonali 45^
    numero6 = [0,6,12,18]
    for i in range(6):
        if(i == 4):
            i = 13
        elif( i == 5):
            i = 20
        else:
            i += 3
        if((i == 3) | (i == 20)):
            if ((griglia[i]==griglia[i+numero6[1]]==griglia[i+numero6[2]]==griglia[i+numero6[3]]) & (griglia[i]!=" ")):
                vittoria = True
                
        elif((i == 4) | (i == 13)):
            for k in range(2):
                x = i + numero6[k]
                if ((griglia[x+numero6[0]]==griglia[x+numero6[1]]==griglia[x+numero6[2]]==griglia[x+numero6[3]]) & (griglia[x+numero6[0]]!=" ")):
                    vittoria = True 
                     
        elif((i == 5) | (i == 6)):
            for k in range(3):
                x = i + numero6[k]
                if ((griglia[x+numero6[0]]==griglia[x+numero6[1]]==griglia[x+numero6[2]]==griglia[x+numero6[3]]) & (griglia[x+numero6[0]]!=" ")):
                    vittoria = True  
                         
    
    #controllo digonali -45^
    numero8 = [0,8,16,24]
    for i in range(6):
        if(i == 4):
            i = 7
        elif( i == 5):
            i = 14
        if((i == 14) | (i == 3)):
            if ((griglia[i]==griglia[i+numero8[1]]==griglia[i+numero8[2]]==griglia[i+numero8[3]]) & (griglia[i]!=" ")):
                vittoria = True
                 
        elif((i == 7) | (i == 2)):
            for k in range(2):
                x = i + numero8[k]
                if ((griglia[x+numero8[0]]==griglia[x+numero8[1]]==griglia[x+numero8[2]]==griglia[x+numero8[3]]) & (griglia[x+numero8[0]]!=" ")):
                    vittoria = True 
                   
        elif((i == 0) | (i == 1)):
            for k in range(3):
                x = i + numero8[k]
                if ((griglia[x+numero8[0]]==griglia[x+numero8[1]]==griglia[x+numero8[2]]==griglia[x+numero8[3]]) & (griglia[x+numero8[0]]!=" ")):
                    vittoria = True  
                       

    return vittoria      
def main():#main
    griglia = {} #creo la griglia
    for k in range (6*7): #formatto la griglia
        griglia[k] = " "
    partecipanti = []#inserisco i partecipanti
    partecipanti.append(input("Inserisci Giocatore1[X]: "))
    partecipanti.append(input("Inserisci Giocatore2[O]: "))
    G1 = random.choice(partecipanti)#sorteggio chi inizia
    partecipanti.remove(G1)#rimuovo il sorteggiato
    G2 = partecipanti[0]#metto il rimanente nella secoda posizione
    giocatori = {G1:"X",G2:"O"}
    os.system("cls")#pulisco lo schermo
    disegnaGriglia(griglia,giocatori,G1,G2)#disegno la griglia
    conta = 1 # per contare il numero di mosse effettuate
    while(True):
        print(f"{G1}")
        print(f"Tocca a: {G1}")
        m = int(input("Inserici mossa: "))#faccio inserire la mossa del primo giocatore
        controllo(m,G1,griglia,giocatori)#controllo che la mossa sia valida
        os.system("cls")#pulisco lo schermo
        disegnaGriglia(griglia,giocatori,G1,G2)
        if(vittoria(griglia)):#controllo la vittoria
            print(f"Ha vinto {G1}")
            break#esco dal while se ha vinto il primo gicatore
        if(conta <= 41): 
            conta += 1
        else: #controllo che non abbiamo finito lo spazio sul campo
            break
        #ripeto tutto per il secondo giocatore
        print(f"{G2}")
        print(f"Tocca a: {G2}")
        m = int(input("Inserici mossa: "))
        controllo(m,G2,griglia,giocatori)
        os.system("cls")
        disegnaGriglia(griglia,giocatori,G1,G2)
        if(vittoria(griglia)):
            print(f"Ha vinto {G2}")
            break
        if(conta <= 41): 
            conta += 1
        else: 
            break 
    if(conta >= 41):#decretoil pareggio
        print("Pareggio")
    
if __name__== "__main__":#richiamo il main
    main()