#made by bosticardo
import socket,os,time,pygame,sys
from threading import Thread
class MyThread(Thread):
    def __init__(self,griglia,g1,g2,giocatori):
        Thread.__init__(self)
        self.runnig = True
        self.griglia = griglia
        self.g1 = g1
        self.g2 = g2
        self.giocatori = giocatori
        self.tipo,self.inizio,self.end = None,None,None
        self.dizioCoordinate = {0:[61.5,61.5],1:[196.5,61.5],2:[331.5,61.5],3:[61.5,196.5],4:[196.5,200],5:[331.5,196.5],6:[61.5,330.5],7:[196.5,330.5],8:[331.5,330.5]}
    def run(self):
        pygame.init()
        size = (400,475)
        fnt2 = pygame.font.SysFont("Times New Roman", 25)
        fnt = pygame.font.SysFont("Times New Roman", 110)
        fnt3 = pygame.font.SysFont("Times New Roman", 50)
        screen = pygame.display.set_mode(size)
        while self.runnig:
            screen.fill((255,255,255))
            pygame.draw.rect(screen,(0,0,0),(130,10,5,380))
            pygame.draw.rect(screen,(0,0,0),(265,10,5,380))
            pygame.draw.rect(screen,(0,0,0),(10,130,380,5))
            pygame.draw.rect(screen,(0,0,0),(10,265,380,5))
            for chiave in self.dizioCoordinate:
                if self.griglia[chiave] == " ":
                    surf_text = fnt.render(str(chiave), True, (0,0,0))
                else:
                    if self.griglia[chiave] == "X":
                        surf_text = fnt.render(self.griglia[chiave], True, (255,0,0))
                    else:
                        surf_text = fnt.render(self.griglia[chiave], True, (0,255,0))
                screen.blit(surf_text, (self.dizioCoordinate[chiave][0]-40,self.dizioCoordinate[chiave][1]-65))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                    break
            TestoG1 = fnt2.render("".join([self.g1," = ",self.giocatori[self.g1]]), True, (255,0,0))
            screen.blit(TestoG1, (10,400))
            TestoG2 = fnt2.render("".join([self.g2," = ",self.giocatori[self.g2]]), True, (0,255,0))
            screen.blit(TestoG2, (10,425))
            if self.tipo != None:
                #screen.fill((255,255,255))
                if self.tipo == 3:
                    risultato = fnt3.render("Pareggio", True, (0,0,0))
                if self.tipo == 1:
                    pygame.draw.line(screen, (0,0,0), self.inizio, self.end, 10)
                    risultato = fnt3.render(f"Hai perso:", True, (255,0,0))
                if self.tipo == 2:
                    pygame.draw.line(screen, (0,0,0), self.inizio, self.end, 10)
                    risultato = fnt3.render(f"Hai vinto", True, (0,255,0))
                screen.blit(risultato, (10,200)) 
            pygame.display.flip()
            """if self.tipo != None:
                self.runnig = False
                break"""
    def linea(self,s,e):
        self.inizio,self.end = self.dizioCoordinate[s],self.dizioCoordinate[e]
def connessione():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("127.0.0.1",8000))
    return s,None
def controllo(x,g,griglia,giocatori):
    while((griglia[x] != " ")):       
        print("Cella occupata")
        x = int(input("Inserici mossa:"))
    griglia[x] = giocatori[g]   
    return x
def disegnaGriglia(griglia,giocatori,g1,g2):
    """Disegno la griglia con i giocatori che si sfidano"""
    print(f"\n{g1} [{giocatori[g1]}] vs {g2} [{giocatori[g2]}]\n")
    print(f" {griglia[0]} | {griglia[1]} | {griglia[2]} ")
    print(f"---+---+---")
    print(f" {griglia[3]} | {griglia[4]} | {griglia[5]} ")
    print(f"---+---+---")
    print(f" {griglia[6]} | {griglia[7]} | {griglia[8]} ")
    print("\n")
def vittoria(griglia,disegno):
    """controllo tutte i  possibili casi in cui si puó vincere"""
    vittoria = False
    if ((griglia[0]==griglia[1]==griglia[2]) & (griglia[0]!=" ")):
        disegno.linea(0,2)
        vittoria = True
    elif ( (griglia[3]==griglia[4]==griglia[5]) & (griglia[3]!=" ")):
        disegno.linea(3,5)
        vittoria = True
    elif ( (griglia[6]==griglia[7]==griglia[8]) & (griglia[6]!=" ")):
        disegno.linea(6,8)
        vittoria = True
    elif ((griglia[0]==griglia[3]==griglia[6]) & (griglia[0]!=" ")):
        disegno.linea(0,6)
        vittoria = True
    elif( (griglia[1]==griglia[4]==griglia[7]) & (griglia[1]!=" ")):
        disegno.linea(1,7)
        vittoria = True
    elif( (griglia[2]==griglia[5]==griglia[8]) & (griglia[2]!=" ")):
        disegno.linea(2,8)
        vittoria = True
    elif ((griglia[0]==griglia[4]==griglia[8]) & (griglia[0]!=" ")):
        disegno.linea(0,8)
        vittoria = True 
    elif(( griglia[2]==griglia[4]==griglia[6]) & (griglia[2]!=" ")):
        disegno.linea(2,6)
        vittoria = True
    return vittoria   
def main():
    connection,address = connessione()
    griglia = {0: " ", 1: " ",2: " ",3: " ",4: " ",5: " ",6: " ",7: " ",8: " "}
    G1  = connection.recv(4096).decode()
    G2 = input("Inserisci Giocatore2[O]: ")
    connection.sendall(G2.encode())
    giocatori = {G1:"X",G2:"O"}
    conta = 1  
    disegnaGriglia(griglia,giocatori,G1,G2)
    disegno = MyThread(griglia,G1,G2,giocatori)
    disegno.start()
    while(True ):
        print(f"{G1}")
        print(f"Tocca a: {G1}")
        m = int(connection.recv(4096).decode())
        griglia[m] = giocatori[G1]
        os.system('cls')
        disegnaGriglia(griglia,giocatori,G1,G2)
        if(vittoria(griglia,disegno)):
            print(f"Ha vinto {G1}")
            disegno.tipo = 1
            break
        if(conta <= 8): 
            conta += 1
        else: 
            disegno.tipo = 3
            break
        print(f"{G2}")
        print(f"Tocca a: {G2}")
        print("Attendi....")
        m = int(input("Inserici mossa: "))
        m = controllo(m,G2,griglia,giocatori)
        connection.sendall(str(m).encode())
        os.system('cls')
        disegnaGriglia(griglia,giocatori,G1,G2)
        if(vittoria(griglia,disegno)):
            print(f"Ha vinto {G2}")
            disegno.tipo = 2
            break
        if(conta <= 8): 
            conta += 1
        else: 
            disegno.tipo = 3
            break 
if __name__=="__main__":
    main()