import socket,random,time
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0",5000))
    print("Sto ascoltando...")
    s.listen()
    connection,address = s.accept()
    print(f"Si é connesso: {address[0]}")
    N,G,a = 999983,954283,random.randint(2,10**6)
    A = (G**a)%N
    connection.sendall("".join([str(N),",",str(G),",",str(A)]).encode())
    B = int(connection.recv(4096).decode())
    K = (B**a)%N
    print(f"N = {N},G = {G},B = {B},A = {A},a = {a}, K = {K}") 
    num = [ord(x) for x in str(K)]
    parola = "ciao"
    cript = [chr(ord(x)+num[i]) for i,x in enumerate(parola)]
    print("".join(cript))
    connection.close()
    s.close()
if __name__=="__main__":
    main()