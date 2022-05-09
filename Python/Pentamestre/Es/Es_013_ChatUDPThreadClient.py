import socket,time
from threading import Thread
class MyThread(Thread):
    def __init__(self,socket):
        Thread.__init__(self)
        self.runnig = True
        self.socket = socket
        self.address = []
    def run(self):
        while self.runnig:
            dati,address= self.socket.recvfrom(4096)#4096 = dimensione in byte del buffer
            self.address = address
            print(f"{dati.decode()}")
    def stop(self):
        self.runnig  =False
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ascolto = MyThread(s)
    ascolto.start()
    while 1:
        stringa = input("Inserisci una stringa: ")
        if (stringa == "Exit") | (stringa == "exit"):
            ascolto.stop()
            ascolto.join()
            break
        if ascolto.address != []:
            s.sendto(stringa.encode(),("192.168.43.229",5000))

if __name__=="__main__":
    main()
