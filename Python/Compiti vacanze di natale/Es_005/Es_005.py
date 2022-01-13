"""Scrivere un programma in Python che prenda in input il nome file di
un programma scritto in C. Il programma deve leggere il file e:
1. Contare il numero di righe totali
2. Contare il numero di chiamate alla funzione “printf”
3. Contare il numero di linee di commento.
"""
def main():
    f = open("./main.c","r")
    righe = f.readlines()
    f.close()
    nrighe = len(righe)
    nprintf,ncomm = 0,0
    for riga in righe:
        if "printf" in riga:
            nprintf+=1
        if ("//" in riga) | ("/*" in riga):
            ncomm += 1
    print(f"numero di righe: {nrighe}\nnumero di printf: {nprintf}\nnumero di commenti: {ncomm}")

if __name__== "__main__":#richiamo il main
    main()