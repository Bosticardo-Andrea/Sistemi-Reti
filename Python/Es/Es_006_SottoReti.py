def bin2dec(string):
    somma = 0
    for i,numero in enumerate(string): # enumerate
        somma += 2**(len(string)-1-i)*int(numero)
    return somma
def dec2bin(string,i):
    string = bin(string)[2:]
    return "0" *(i - len(string))+string
def IP_dec2bin(string):
    string = string.split(".")
    strBin = "" 
    for el in string:
        strBin += dec2bin(int(el),8)+ "."
    return strBin[:-1]
def IP_bin2dec(string):
    strDec = ""
    for el in string.split("."): 
        strDec += str(bin2dec(el))+ "."
    return strDec[:-1]
def controlloIP(ip,mask):
    i = 0
    ok = True
    while((i < len(ip)) & (ok == True)):
        if(ip[i] == "."):
            ok = True
        elif((int(ip[i]) > 255) | (int(ip[i]) < 0)):
            ok = False
        i+=1
    if (ok != False):
        ip = IP_dec2bin(ip).split(".")
        listSub=[elmento for k,elmento in enumerate("".join(ip)[::-1]) if(k<32-mask)]
        if "1" in listSub: 
            ok = False
    return ok
def trasformaSub(mask):
    maschera = ""
    if(mask[0] == "/"):
        maschera = mask[1:]
    elif(mask.isdigit() == True):
        maschera = int(mask)
    else:
        if(mask[:3] == "255"):
            mask = IP_dec2bin(mask).split(".")
            mask = "".join(mask)
        else:
            mask = mask.split(".")
            mask = "".join(mask)
        ok,i = False,0,
        while (i < len(mask)) & (ok == False):
            if mask[i] == "0":
                ok = True
                i+=1
        maschera = i-1      
    return int(maschera)
def richieste():
    ip = input("Inserisci IP in modalitá decimale puntata: ")
    #subnet = trasformaSub(input("Inserisci la subnet mask /n: "))
    subnet = trasformaSub(input("Inserisci la subnet mask /n: "))
    print(subnet)
    while controlloIP(ip,subnet) == False:
        ip = input("IP errato!!\nRinserisci: ")
    return ip,subnet
def IP_broadcast(ip,mask):
    ip = IP_dec2bin(ip).split(".")
    ip = "".join(ip)[::-1]
    ip = ("1"*(32-mask)) + (ip[32-mask:]) 
    ip1 = ""
    for k in range(1,5):
        ip1 += ip[8*(k-1):8*k] + "."
    ip1 = ip1[::-1]
    return IP_bin2dec(ip1[1:])
def IPmin(ip,mask):
    ip = IP_broadcast(ip,mask)
    ip = IP_dec2bin(ip)
    return IP_bin2dec(ip[:-1] + "0")
def IPmax(ip,mask):
    ip = IP_dec2bin(ip)
    return IP_bin2dec(ip[:-1] + "1")
def main():
   ip,subnet = richieste()
   broadcast = IP_broadcast(ip,subnet)
   IpMin = IPmin(ip,subnet)
   IpMax = IPmax(ip,subnet)
   print(f"IP = {ip}/{subnet}\nbroadcast = {broadcast}")
   print(f"IP minimo = {IpMin}")
   print(f"IP massimo = {IpMax}")
if __name__ =="__main__":
    main();