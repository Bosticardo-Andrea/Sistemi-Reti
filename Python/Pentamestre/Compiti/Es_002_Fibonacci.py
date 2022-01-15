"""
Scrivere una funzione Python ricorsiva che permetta 
di stampare i numeri di Fibonacci minori di un valore scelto dall'utente.
"""
def fibonacci(x):
    if(x < 2):
        return x
    else:
        return(fibonacci(x-2) + fibonacci(x-1))
    

def main():
    num = int(input("Inserisci un numero: "))
    print("fibonacci = ", fibonacci(num))

if __name__=="__main__":
    main()