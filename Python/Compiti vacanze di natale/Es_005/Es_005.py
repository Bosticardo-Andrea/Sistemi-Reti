"""Scrivere un programma in Python che prenda in input il nome file di
un programma scritto in C. Il programma deve leggere il file e:
1. Contare il numero di righe totali
2. Contare il numero di chiamate alla funzione “printf”
3. Contare il numero di linee di commento.
"""
def main():
    f = open("./main.c","r")
    righe = f.readlines();
    f.close()
    nrighe = len(righe)
    nprintf = 0
    ncomm = 0
    for parola in righe:
        conta = 0
        ok = False
        nprint = ""
        contac = 0
        oks = False
        comm = ""
        for lettera in parola:
            if((lettera == "p") | (ok == True)):
                nprint += lettera
                conta += 1
                ok = True
                if(conta == 6):
                    ok = False
            if((lettera == "/") | (oks == True)):
                comm += lettera
                contac += 1
                oks = True
                if(contac == 2):
                    oks = False       
        if(nprint == "printf"):
            nprintf +=1
        if(comm == "//"):
            ncomm +=1
    print(f"numero di righe: {nrighe}\nnumero di printf: {nprintf}\nnumero di commenti: {ncomm}")

if __name__== "__main__":#richiamo il main
    main()