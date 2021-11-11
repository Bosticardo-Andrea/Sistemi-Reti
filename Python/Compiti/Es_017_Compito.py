def primo(num):
    ok = True
    for div in range(2,num-1):
        if((num%div) == 0):
            ok = False
    return ok
numeriPrimi = []
i=0
numero = 0
while(i <= 101):
    if(primo(numero)):
        numeriPrimi.append(numero)
        i +=1
    numero +=1
print(numeriPrimi)