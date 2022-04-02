import socket
#socket.AF_INET = IPV4
#socket.SOCK_DGRAM = UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",5000)) # solo sui server
dati,id_client = s.recv(4096)#4096 = dimensione in byte del buffer
print(f"{dati.decode()} ricevuti da {id_client}")