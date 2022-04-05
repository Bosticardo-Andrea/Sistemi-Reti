import socket
#socket.AF_INET = IPV4
#socket.SOCK_DGRAM = UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.129",5000)) # solo sui server
while True:
    dati,address= s.recvfrom(4096)#4096 = dimensione in byte del buffer
    print(f"{dati.decode()}\t inviato da: {address}")
    stringa = input("Inserisci una stringa: ")
    if (stringa == "Exit") | (stringa == "exit"):break
    s.sendto(stringa.encode(),(address[0],address[1]))