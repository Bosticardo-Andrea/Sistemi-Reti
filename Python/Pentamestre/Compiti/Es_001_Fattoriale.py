"""
Scrivere una funzione Python ricorsiva che 
permetta di calcolare il fattoriale di un numero intero. 
"""
def fattoriale(x):
    if(x == 1):
        return x
    else:
        return(x*(fattoriale(x -1)))
    
def main():
    num = int(input("Inserisci un numero: "))
    print(f"Il fattoriale di {num} é: {fattoriale(num)}")

if __name__=="__main__":
    main()