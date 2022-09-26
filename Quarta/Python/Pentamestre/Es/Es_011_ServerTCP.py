import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#SOCK_STREAM = TCP
s.bind(("127.0.0.1",8000))
s.listen()
print("In attesa di conessione...")
connection,address = s.accept()
while 1:
    data = input("Mex: ")
    connection.sendall(data.encode())
    #lif((data == "exit") or (data == "Exit")): break
    data = connection.recv(4096)
    print(data.decode())
connection.close()