#made by bosticardo
import socket,os,time,pygame,sys,serial
from tkinter.tix import Tree
import serial.tools.list_ports
from threading import Thread
import tkinter as tk 
class Coda():
    def __init__(self):
        self.coda=[]
    def enqueue(self,elemento):
        self.coda.append(elemento)
    def dequeue(self):
        if len(self.coda) != 0:
            return self.coda.pop(0)
        else:
            return None
    def print(self): 
        print(self.coda)
coda = Coda()
class MyThread(Thread):
    def __init__(self,griglia,g1,g2,giocatori,connect):
        Thread.__init__(self)
        self.running = True
        self.griglia = griglia
        self.g1 = g1
        self.g2 = g2
        self.tipo = None
        self.giocatori = giocatori
        self.posizione = 0
        self.inzio = 0
        self.end = 0
        self.connect = connect
        self.ok = True
        self.dizioCoordinate = {0:[61.5,61.5],1:[196.5,61.5],2:[331.5,61.5],3:[61.5,196.5],4:[196.5,200],5:[331.5,196.5],6:[61.5,330.5],7:[196.5,330.5],8:[331.5,330.5]}
    def run(self):
        pygame.init()
        size = (400,475)
        fnt2 = pygame.font.SysFont("Times New Roman", 25)
        fnt = pygame.font.SysFont("Times New Roman", 110)
        fnt3 = pygame.font.SysFont("Times New Roman", 50)
        screen = pygame.display.set_mode(size)
        while self.running:
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
                screen.blit(surf_text, (self.dizioCoordinate[chiave][0]-20.5,self.dizioCoordinate[chiave][1]-50.5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            TestoG1 = fnt2.render("".join([self.g1," = ",self.giocatori[self.g1]]), True, (255,0,0))
            screen.blit(TestoG1, (10,400))
            TestoG2 = fnt2.render("".join([self.g2," = ",self.giocatori[self.g2]]), True, (0,255,0))
            screen.blit(TestoG2, (10,425))
            mossa = str(coda.dequeue())
            if mossa != None: (mossa)
            if mossa[0] == "a":
                if self.posizione == 6: self.posizione = 0
                elif self.posizione == 7: self.posizione = 1
                elif self.posizione == 8: self.posizione = 2
                else:self.posizione = self.posizione + 3
            if mossa[0] == "b":
                if self.posizione == 2 :self.posizione = 0
                elif self.posizione == 5: self.posizione = 3
                elif self.posizione == 8: self.posizione = 6
                else: self.posizione = self.posizione +  1   
                     
            if (mossa[0] == "m") and (self.ok):
                m = self.posizione
                m = controllo(m,self.g1,self.griglia,self.giocatori)
                if m != None:
                        self.connect.sendall(str(m).encode())
                        self.ok = False
            #print(self.posizione)
            if self.tipo != None:
                if self.tipo == 3:
                    pygame.draw.rect(screen,(255,255,255),(0,400,400,75),0)
                    risultato = fnt3.render("Pareggio", True, (0,0,0))
                if self.tipo == 2:
                    pygame.draw.rect(screen,(255,255,255),(0,400,400,75),0)
                    pygame.draw.line(screen, (0,0,0), self.inizio, self.end, 10)
                    risultato = fnt3.render(f"Hai perso:", True, (255,0,0))
                if self.tipo == 1:
                    pygame.draw.rect(screen,(255,255,255),(0,400,400,75),0)
                    pygame.draw.line(screen, (0,0,0), self.inizio, self.end, 10)
                    risultato = fnt3.render(f"Hai vinto", True, (0,255,0))
                screen.blit(risultato, (10,400)) 
            pygame.draw.rect(screen,(255,0,0),(self.dizioCoordinate[self.posizione][0]-35,self.dizioCoordinate[self.posizione][1]-35,100,100),2)
            pygame.display.flip() 
    def linea(self,s,e):
        self.inizio,self.end = self.dizioCoordinate[s],self.dizioCoordinate[e]

class MyThread2(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
    def run(self):
        
        port,microbit = self.letturaPorte()
        while(port == None): 
            port,microbit = self.letturaPorte()
        while self.running:
            data = microbit.readline().decode()
            if(data != ""): 
                coda.enqueue(data[:-1])
    def letturaPorte(self):
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            #print("{}: {} [{}]".format(port, desc, hwid))
            break
        if ports == []:  port = None
        else: 
            #microbit = serial.Serial(port=port, baudrate=115200, timeout=1)
            microbit = serial.Serial(port="COM8", baudrate=115200, timeout=1)
        return ports,microbit
    def stop(self):
        self.running = False
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('450x200')
        self.title("Nome")
        self.grid_columnconfigure(0, weight=1)
        self.textwidget = tk.Text()
        self.text_input = tk.Entry()
        self.name = None
        self.crea()
    def crea(self):
        welcome_label = tk.Label(self,
                                    text="Inserisci il tuo nome",
                                    font=("Helvetica", 15))
        welcome_label.grid(row=0, column=0, sticky="WE", padx=10, pady=10)                       
        self.text_input.grid(row=1, column=0, sticky="WE", padx=10)
        self.textwidget.insert(tk.END, "Inserire il nome, poi chiudere la finestra\n")
        self.textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
        download_button = tk.Button(text="Enter", command=self.nome)
        download_button.grid(row=1, column=1, sticky="WE", pady=10, padx=10)
    def nome(self,):
        if self.text_input.get():
            user_input = self.text_input.get()
            nome = user_input
            self.name = user_input
            print(self.name)
        else:
            nome = "Inserire il nome, poi chiudere la finestra\n"
        self.textwidget.delete (1.0,"end")
        self.textwidget.insert(tk.END, nome)
        self.textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

def connessione():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("127.0.0.1",8000))
    #s.bind(("192.168.43.165",8000))
    s.listen()
    print("In attesa di connessione...")
    connect,address = s.accept()
    return connect,address
def controllo(x,g,griglia,giocatori):
    """Si effettua il controllo del numero inserito:
    - Nel caso la cella sia occupata
    - Nel caso il numero non si corretto < 0 o > 8"""
    if((griglia[x] == " ")):       
        print("Cella occupata")
        #x = int(input("Inserici mossa:"))
        x = None
    else: griglia[x] = giocatori[g]   
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
    app = GUI()
    app.mainloop()
    G1 = app.name
    #inserisciNome.start()
    griglia = {0: " ", 1: " ",2: " ",3: " ",4: " ",5: " ",6: " ",7: " ",8: " "}
    connect,address = connessione()
    #G1 = input("Inserisci Giocatore1[X]: ")e
    connect.sendall(G1.encode())
    G2 = connect.recv(4096).decode()
    giocatori = {G1:"X",G2:"O"}
    conta = 1  
    disegnaGriglia(griglia,giocatori,G1,G2)
    movimento = MyThread2()
    movimento.start()
    disegno = MyThread(griglia,G1,G2,giocatori,connect)
    disegno.start()
    while(True ):
        print(f"{G1}")
        print(f"Tocca a: {G1}")
        disegno.ok = True
        #m = int(input("Inserici mossa: "))
        #m = controllo(m,G1,griglia,giocatori)
        #connect.sendall(str(m).encode())
        os.system('cls')
        disegnaGriglia(griglia,giocatori,G1,G2)
        ric = True
        while disegno.ok == True:
            if(vittoria(griglia,disegno)):
                print(f"Ha vinto {G1}")
                disegno.tipo = 1
                ric = False
                break
        if ric == False:
            break
        if(conta <= 8): 
            conta += 1
        else: 
            disegno.tipo = 3
            break
        print(f"{G2}")
        print(f"Tocca a: {G2}")
        print("Attendi....")
        m = int(connect.recv(4096).decode())
        griglia[m] = giocatori[G2]
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
    movimento.stop()
    movimento.join()
    time.sleep(3)
    disegno.running = False
    disegno.join()
if __name__=="__main__":
    main() 