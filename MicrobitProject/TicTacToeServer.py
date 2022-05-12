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
        self.tipo = None
        self.giocatori = giocatori
    def run(self):
        pygame.init()
        size = (400,475)
        fnt2 = pygame.font.SysFont("Times New Roman", 25)
        fnt = pygame.font.SysFont("Times New Roman", 110)
        screen = pygame.display.set_mode(size)
        dizioCoordinate = {0:(37.5,0),1:(172.5,0),2:(307.5,0),3:(37.5,135),4:(172.5,135),5:(307.5,135),6:(37.5,270),7:(172.5,270),8:(307.5,270)}
        """surf_text = fnt.render(self.g2, True, (0, 0, 0))
        screen.blit(surf_text, (10,50))"""
        while self.runnig:
            screen.fill((255,255,255))
            pygame.draw.rect(screen,(0,0,0),(130,10,5,380))
            pygame.draw.rect(screen,(0,0,0),(265,10,5,380))
            pygame.draw.rect(screen,(0,0,0),(10,130,380,5))
            pygame.draw.rect(screen,(0,0,0),(10,265,380,5))
            for chiave in dizioCoordinate:
                if self.griglia[chiave] == " ":
                    surf_text = fnt.render(str(chiave), True, (0,0,0))
                else:
                    if self.griglia[chiave] == "X":
                        surf_text = fnt.render(self.griglia[chiave], True, (255,0,0))
                    else:
                        surf_text = fnt.render(self.griglia[chiave], True, (0,255,0))
                screen.blit(surf_text, dizioCoordinate[chiave])
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            TestoG1 = fnt2.render("".join([self.g1," = ",self.giocatori[self.g1]]), True, (255,0,0))
            screen.blit(TestoG1, (10,400))
            TestoG2 = fnt2.render("".join([self.g2," = ",self.giocatori[self.g2]]), True, (0,255,0))
            screen.blit(TestoG2, (10,425))
            if self.tipo != None:
                screen.fill((255,255,255))
                if self.tipo == 3:
                    risultato = fnt2.render("Pareggio", True, (0,255,0))
                if self.tipo == 1:
                    risultato = fnt2.render(f"vince: {self.g1}", True, (0,255,0))
                if self.tipo == 2:
                    risultato = fnt2.render(f"Vince {self.g2}", True, (0,255,0))
                screen.blit(risultato, (10,200))
            pygame.display.flip() 
    def stop(self,tipo):
        self.tipo = tipo
    def aggiornaGriglia(self,griglia):
        self.griglia = griglia
def connessione():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("127.0.0.1",8000))
    #s.bind(("192.168.43.229",8000))
    s.listen()
    print("In attesa di connessione...")
    connection,address = s.accept()
    return connection,address
def controllo(x,g,griglia,giocatori):
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
def main():
    griglia = {0: " ", 1: " ",2: " ",3: " ",4: " ",5: " ",6: " ",7: " ",8: " "}
    connection,address = connessione()
    G1 = input("Inserisci Giocatore1[X]: ")
    connection.sendall(G1.encode())
    G2 = connection.recv(4096).decode()
    giocatori = {G1:"X",G2:"O"}
    conta = 1  
    disegnaGriglia(griglia,giocatori,G1,G2)
    disegno = MyThread(griglia,G1,G2,giocatori)
    disegno.start()
    while(True ):
        print(f"{G1}")
        print(f"Tocca a: {G1}")
        m = int(input("Inserici mossa: "))
        connection.sendall(str(m).encode())
        controllo(m,G1,griglia,giocatori)
        os.system('cls')
        disegnaGriglia(griglia,giocatori,G1,G2)
        if(vittoria(griglia)):
            print(f"Ha vinto {G1}")
            disegno.stop(1)
            break
        if(conta <= 8): 
            conta += 1
        else: 
            disegno.stop(3)
            break
        print(f"{G2}")
        print(f"Tocca a: {G2}")
        print("Attendi....")
        m = int(connection.recv(4096).decode())
        controllo(m,G2,griglia,giocatori)
        os.system('cls')
        disegnaGriglia(griglia,giocatori,G1,G2)
        if(vittoria(griglia)):
            print(f"Ha vinto {G2}")
            disegno.stop(2)
            break
        if(conta <= 8): 
            conta += 1
        else: 
            disegno.stop(3)
            break 
if __name__=="__main__":
    main()