from multiprocessing.resource_sharer import stop
import socket
import Es_002_ClassRSA
rsa = Es_002_ClassRSA.RSA()
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("192.168.88.138",5000))
    print("Sto ascoltando...")
    s.listen()
    connection,address = s.accept()
    print(f"Si é connesso: {address[0]}")
    connection.sendall("".join([rsa.n,",",rsa.c]).encode())
    while 1:
        dati = connection.recv(4096)
        print(rsa.decript(dati))
        
if __name__=="__main__":
    main()