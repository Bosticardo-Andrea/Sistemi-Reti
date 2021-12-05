#made by bosticardo
def controllo(x,g):
    """Si effettua il controllo del numero inserito:
     - Nel caso la cella sia occupata
     - Nel caso il numero non si corretto < 0 o > 8"""
    while((x < 0 or x > 8)):
        x = int(input("Numero non valido:"))
    while((griglia[x] != " ")):       
        print("Cella occupata")
        x = int(input("Inserici mossa:"))
        while((x < 0 or x > 8)):
            x = int(input("Numero non valido:"))
    griglia[x] = giocatori[g]   
def disegnaGriglia(griglia,giocatori,g1,g2):
    """Disegno la griglia con i giocatori che si sfidano"""
    print(f"\n{g1} [{giocatori[g1]}] vs {g2} [{giocatori[g2]}]\n")
    print(f" {griglia[0]} | {griglia[1]} | {griglia[2]} ")
    print(f"---+---+---")
    print(f" {griglia[3]} | {griglia[4]} | {griglia[5]} ")
    print(f"---+---+---")
    print(f" {griglia[6]} | {griglia[7]} | {griglia[8]} ")
    print("\n")
def vittoria(griglia):
    """controllo tutte i  possibili casi in cui si puó vincere"""
    vittoria = False
    if ((griglia[0]==griglia[1]==griglia[2]) & (griglia[0]!=" ")):
        vittoria = True
    elif ( (griglia[3]==griglia[4]==griglia[5]) & (griglia[3]!=" ")):
       vittoria = True
    elif ( (griglia[6]==griglia[7]==griglia[8]) & (griglia[6]!=" ")):
        vittoria = True
    elif ((griglia[0]==griglia[3]==griglia[6]) & (griglia[0]!=" ")):
        vittoria = True
    elif( (griglia[1]==griglia[4]==griglia[7]) & (griglia[1]!=" ")):
        vittoria = True
    elif( (griglia[2]==griglia[5]==griglia[8]) & (griglia[2]!=" ")):
        vittoria = True
    elif ((griglia[0]==griglia[4]==griglia[8]) & (griglia[0]!=" ")):
        vittoria = True 
    elif(( griglia[2]==griglia[4]==griglia[6]) & (griglia[2]!=" ")):
        vittoria = True
    return vittoria      
griglia = {0: " ", 1: " ",2: " ",3: " ",4: " ",5: " ",6: " ",7: " ",8: " "}
G1 = input("Inserisci Giocatore1[X]: ")
G2 = input("Inserisci Giocatore2[O]: ")
giocatori = {G1:"X",G2:"O"}
disegnaGriglia(griglia,giocatori,G1,G2)
conta = 1
while(True ):
    print(f"{G1}")
    print(f"Tocca a: {G1}")
    m = int(input("Inserici mossa: "))
    controllo(m,G1)
    disegnaGriglia(griglia,giocatori,G1,G2)
    if(vittoria(griglia)):
        print(f"Ha vinto {G1}")
        break
    if(conta <= 8): 
        conta += 1
    else: 
        break
    print(f"{G2}")
    print(f"Tocca a: {G2}")
    m = int(input("Inserici mossa: "))
    controllo(m,G2)
    disegnaGriglia(griglia,giocatori,G1,G2)
    if(vittoria(griglia)):
        print(f"Ha vinto {G2}")
        break
    if(conta <= 8): 
        conta += 1
    else: 
        break 
if(conta >= 8):
    print("Pareggio")