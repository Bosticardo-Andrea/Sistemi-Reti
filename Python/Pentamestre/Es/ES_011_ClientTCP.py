import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#SOCK_STREAM = TCP
s.connect(("127.0.0.1",8000))
while 1:
    data = s.recv(4096)
    print(data.decode())
    #if((data.decode() == "exit") or (data.decode() == "Exit")): break
    data = input("Messaggio: ")
    s.sendall(data.encode())
s.close()