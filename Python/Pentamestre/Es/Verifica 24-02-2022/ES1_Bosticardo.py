""" Il file medals.csv contiene tutte le medaglie assegnate alle recenti Olimpiadi Invernali. 
Ogni riga corrisponde a una medaglia assegnata. 
Scrivere un programma in Python3 che legga il file e calcoli quante medaglie d'oro,d'argento e di bronzo ha vinto l'Italia (colonna country=Italy). 
I tre valori devono essere salvati in un dizionario e il dizionario deve essere stampato.
Il programma deve avere nome file ES1_COGNOME.py."""

def main():
    medaglie = {"gold":0,"silver":0,"bronze":0}
    f = open("./medals.csv","r")
    righe = f.readlines()
    f.close()
    for riga in righe[1:]:
        parole = riga.split(",")
        if(parole[8].lower() == "italy"):
            medaglie[parole[0].lower()] += 1          
    print(f"medaglie vinte dall'Italia: {medaglie}")
    
if __name__=="__main__":
    main()