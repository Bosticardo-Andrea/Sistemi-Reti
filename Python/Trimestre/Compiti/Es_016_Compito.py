def primo(num):
    ok = True
    for div in range(2,num//2):
        if((num%div) == 0):
            ok = False
    return ok
numero = int(input("Inserisci un numero "))
print(primo(numero))
if(primo(numero) == True):
    print("É un numero primo")
else:
    print("Non é un numero primo")
    