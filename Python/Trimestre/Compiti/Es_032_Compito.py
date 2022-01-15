#1. chiedere stringa utente
#2. snobbo tutto ció che non é una parentesi ()[]{}
#3. parentesi aperta push/parentesi chiusa pop
#4. controllo che non ci siano errori

#str = input("Espressione: ")
def main():
    str = "[(5*2)-(7+3)]"
    ok = True;
    parentesi = {')':'(',']':'[','}':'{'}
    listaparentesia,listaparentesic = [],[]
    for lettera in str:
        if((lettera == '[') | (lettera == '(') | (lettera == '{')):
            listaparentesia.append(lettera)
        elif((lettera == ']') | (lettera == ')') | (lettera == '}')):
            ok = (listaparentesia[-1] == parentesi[lettera])
            elemento = listaparentesia.pop()
    if((ok == True) & (len(listaparentesia)==0)):
        print("É tutto ok")
    else:
        print("Errore")
if __name__== "__main__":
    main()