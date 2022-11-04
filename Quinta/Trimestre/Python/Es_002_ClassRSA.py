class RSA():
    def __init__(self):
        self.p,self.q = 101,103
        self.n = self.p*self.q
        self.m = self.calcolaMCD_mcm(self.p-1,self.q-1)[1]
        self.c = self.trovaC()
        self.d = self.trovaD()
        print(f"p = {self.p},q = {self.q},n = {self.n},m = {self.m}, c = {self.c},d = {self.d}")

    def calcolaMCD_mcm(self,a,b):
        lista = [a,b]
        while lista[-1] != 0:
            lista.append(lista[-2]%lista[-1])
        return((lista)[-2],int((a*b)/lista[-2]) )
    
    def ricorsiva(self):
        if self.b == 0: return self.a
        else: return self.ricorsiva(self.b,self.a%self.b)

    def trovaD(self):
        for d in range(self.m):
            if ((self.c)*d) % self.m == 1:return d

    def trovaC(self):
        c = 2
        for c in range(2,self.m):
            if self.calcolaMCD_mcm(c,self.m)[0] == 1:return c
    
    def cript(self,str):
        critto = ""
        for a in str:
            critto += chr((ord(a)**self.c)%self.n)
        return critto
    
    def decript(self,str):
        decritto = ""
        for lettera in str:
            decritto += chr((ord(lettera)**self.d)%self.n)
        return decritto

 