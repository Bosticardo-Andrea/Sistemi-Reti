def calcolaMCD_mcm(a,b):
    lista = [a,b]
    while lista[-1] != 0:
       lista.append(lista[-2]%lista[-1])
    return((lista)[-2],int((a*b)/lista[-2]) )

def ricorsiva(a,b):
    if b == 0: return a
    else: return ricorsiva(b,a%b)

def trovaD(m,c):
    for d in range(m):
        if (c*d) % m == 1:return d

def trovaC(m):
    c = 2
    for c in range(2,m):
        if calcolaMCD_mcm(c,m)[0] == 1:return c
def cript(str,c,n):
    critto = ""
    for a in str:
        critto += chr((ord(a)**c)%n)
    return critto
def decript(str,d,n):
    decritto = ""
    for lettera in str:
        decritto += chr((ord(lettera)**d)%n)
    return decritto
def main():
    p,q = 5,13
    n = p*q
    m = calcolaMCD_mcm(p-1,q-1)[1]
    c = trovaC(m)
    d = trovaD(m,c)
    print(f"p = {p},q = {q},n = {n},m = {m}, c = {c},d = {d}")
    critto = cript("c",c,n)
    decritto = decript("⒖",d,n)
    print(f"parola crittata {critto}")
    print(f"parola decrittata {decritto}")
 
if __name__=="__main__":
    main()