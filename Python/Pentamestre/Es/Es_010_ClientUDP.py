import socket
#socket.AF_INET = IPV4
#socket.SOCK_DGRAM = UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
stringa = "Ciao"
s.sendto(stringa,("127.0.0.1",5000))