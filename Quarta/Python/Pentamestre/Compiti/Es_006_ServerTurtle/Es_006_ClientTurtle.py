"""
    F,50
    R,90
    L,90
La lettera indica il movimento (F,R,L) 
poi metto il numero del movimento
"""
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",8000))
while 1:
    data = input("Messaggio: ")
    s.sendall(data.encode())
s.close()