import socket
#socket.AF_INET = IPV4
#socket.SOCK_DGRAM = UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    stringa = input("Inserisci una stringa: ")
    if (stringa == "Exit") | (stringa == "exit"):break
    s.sendto(stringa.encode(),("127.0.0.1",5000))