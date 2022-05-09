import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.125",5000))
while True:
    dati,address= s.recvfrom(4096)
    print(f"{dati.decode()}\t inviato da: {address}")
    #if (dati == "Exit") | (dati == "exit"):break
    s.sendto(dati,("192.168.0.136",5000))