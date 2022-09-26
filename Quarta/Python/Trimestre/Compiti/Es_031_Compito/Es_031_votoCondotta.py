scelta = lambda x: False if((x == 's') | (x == 'S')) else True
def controllo():
    x = int(input("voto di condotta: "))
    while((x < 2) | (x > 10)):
        x = int(input("voto di condotta: "))
    return x
def main():
    f = open("fileCSV.txt","a")
    ok = True
    n = int(input("quanti ne vuoi inserire: "))
    while(ok):
        for _ in range (n):
            nome = input("inserisci il tuo nome: ")
            voto = controllo()
            f.write(f"{nome[0]}{(len(nome)-1)*'*'} voto: {voto}\n")
        ok = scelta(input("vuoi uscire[s/n]: "))
        if(ok == True):
            n = int(input("quanti ne vuoi inserire: "))
    f.close()
if __name__== "__main__":
    main()
