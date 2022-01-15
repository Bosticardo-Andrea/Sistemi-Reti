#2)Scrivi un programma Python che salvi su un file i primi 100 numeri primi, uno per ogni riga del file. 
from os import close


def primo(num):
    ok = True
    for div in range(2,num-1):
        if((num%div) == 0):
            ok = False
    return ok

f = open("./NumeriPrimi.txt","w")
x = 0
n = 1
while (x < 100):
    if(primo(n)):
        f.write(str(n) + "\n" )
        x = x + 1
    n = n + 1   
f.close()
    
