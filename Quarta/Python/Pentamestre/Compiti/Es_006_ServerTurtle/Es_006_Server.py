import socket
from threading import Thread
import time,turtle
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("127.0.0.1",8000))
    s.listen()
    print("In attesa di conessione...")
    connection,address = s.accept()
    matita = turtle.Turtle()
    sfondo = turtle.Screen()
    sfondo.bgcolor("light blue") 
    matita.color("white")
    matita.speed(0)
    while 1:
        dati = connection.recv(4096).decode()
        if(dati.lower() == "exit"): break
        dati = dati.split(",")
        if(dati[0].lower() == "f"):
            matita.forward(int(dati[1]))
        elif(dati[0].lower() == "r"):
            matita.right(int(dati[1]))
        else:
            matita.left(int(dati[1]))
    connection.close()
    
    
if __name__=="__main__":
    main()