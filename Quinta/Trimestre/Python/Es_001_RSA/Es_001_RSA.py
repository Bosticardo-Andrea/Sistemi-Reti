from sympy import *
import time
def Calcolaprimi():
    f = open("numeri.txt","w")
    #ciclo calcola primi senza funzione isprime
    """n = 78498
    c = 2
    while n!=0:
        for i in range(2,c):
            if c%i==0:break
        else:  
            f.write(str(c) + "\n") 
            n-=1
        c+=1 """
    for i in range(1,10**6):
        if isprime(i):f.write(str(i) + "\n")
    f.close()
def trovaFattoriAlti(numero,lista):
    ok,fattori = True,[]
    #controllo subito se il numero diviso con  il piú alto della mia lista 
    if(int(numero/lista[-1])) and lista[-1]*int(numero/lista[-1]) == numero: fattori = [int(lista[-1]),int(numero/lista[-1])]
    elif lista[-1]*int(numero/lista[-1]) < numero:
        for i in range(lista[-1],int(numero/2)):
            if isprime(int(numero/i)) and i*int(numero/i) == numero:fattori = [int(i),int(numero/i)]
    else:
        for i in lista[:-1]:
            if isprime(int(numero/i)) and i*int(numero/i) == numero:fattori = [int(i),int(numero/i)]
    return "".join([str(fattori[0]),"*",str(fattori[1])," = ",str(numero)])
def trovaFattori(numero,lista):
    fattori = []
    for i in lista:
        if int(numero/i) in lista and i*int(numero/i) == numero: fattori = [int(i),int(numero/i)]
    return "".join([str(fattori[0]),"*",str(fattori[1])," = ",str(numero)])
def main():
    #Calcolaprimi()
    numero = int(input("inserisci il numero:"))
    while numero < 4:
        print("Errore: inserisci un numero > 4")
        numero = int(input("inserisci il numero:"))
    f,start = open("numeri.txt","r"),time.time()
    lista = f.readlines()
    f.close()
    lista = [int(str(i[:-1])) for i in lista]
    if int(numero/2) < 10**6:print(trovaFattori(numero,lista))
    else:print(trovaFattoriAlti(numero,lista))
    print(f"Tempo di esecuzione = {time.time()-start}")
if __name__== "__main__":
    main()