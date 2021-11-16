def primo(numero):
    ok = True
    conto = numero-1    
    while (ok == True) & (conto > 1):
        if numero % conto == 0:
            ok = False
        conto-=1
    if conto == 0:
        ok = False
    return (ok)

conta = 0
for numero in range(1,1000):
    if primo(numero) == True:
        print(numero)
        conta+=1
print(f"i numeri primi da 1 a 1000 sono: {conta}")