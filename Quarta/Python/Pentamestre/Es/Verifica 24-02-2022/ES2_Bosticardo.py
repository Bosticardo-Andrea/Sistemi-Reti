"""Create una classe IPAddress che permetta di rappresentare indirizzi ip in notazione decimale puntata. 
La classe deve essere dotata di un metodo che permetta di ottenere la rappresentazione binaria dell'indirizzo ip 
e di un metodo che permetta di determinare se l'indirizzo ip è una subnet mask (in caso affermativo il metodo ritorna True, altrimenti False). 
Ricordate che una subnet mask è un indirizzo ip costituito da soli 1 nella prima parte e da soli 0 nella seconda parte....
La classe deve essere dotata di un terzo metodo che verifica la validità di un indirizzo ip: per esempio 300.123.10.19 non è un ip valido.
Il programma deve avere nome file ES2_COGNOME.py."""

class IPAddress:
    def __init__(self):
        pass
    def bin2dec(self,string):
        somma = 0
        for i,numero in enumerate(string): # enumerate
            somma += 2**(len(string)-1-i)*int(numero)
        return somma
    def dec2bin(self,string,i):
        string = bin(string)[2:]
        return "0" *(i - len(string))+string
    
    def IP_dec2bin(self,string):
        string = string.split(".")
        strBin = "" 
        for el in string:
            strBin += self.dec2bin(int(el),8)+ "."
        return strBin[:-1]
    def IP_bin2dec(self,string):
        strDec = ""
        for el in string.split("."): 
            strDec += str(self.bin2dec(el))+ "."
        return strDec[:-1]
    def IsSubNet(self,string):
        ok = 0
        ok1 = True
        string = self.IP_dec2bin(string)
        string = string.split(".")
        for el in string[::-1]:
            for el1 in el:
                if((el1 == "1") & (ok < 1)):
                    ok += 1
                elif((ok >= 1) & (el1 == "0")):
                    ok1 = False
        return ok1
    def IsValido(self,string):
        string = string.split(".")
        ok = True
        n = 0
        while(ok == True) & (n < len(string)):
            if (int(string[n]) < 0) | (int(string[n]) > 255):
                ok = False
            n+=1
        return ok
def main():
    ip = IPAddress()
    print(ip.IP_dec2bin("192.168.1.1"))
    print(ip.IP_bin2dec(ip.IP_dec2bin("192.168.1.1")))
    print(ip.IsValido("300.123.10.19"))
    print(ip.IsSubNet("255.255.0.0"))
if __name__=="__main__":
    main()