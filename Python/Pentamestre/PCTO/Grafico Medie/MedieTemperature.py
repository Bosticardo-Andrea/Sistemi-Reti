import matplotlib.pyplot as plt
def main():
    import matplotlib.pyplot as plt
    f = open("dati.csv","r")
    righe = f.readlines()
    f.close()
    riga = []
    for el in righe:
        riga.append(el.split(","))
    giacca,temperatura,mesi,giochi,scuola = [],[],[],[],[]
    mesi=riga[0]
    temperatura = riga[1][1:]
    giacca = riga[2][1:]
    giochi = riga[4][1:]
    scuola = riga[3][1:]
    
    mesi[11] = mesi[11][:-1]
    temperatura[11]=temperatura[11][:-1]
    giacca[11] = giacca[11][:-1]
    giochi[11] = giochi[11][:-1]
    scuola[11] = scuola[11][:-1]
    
    giacca = list(map(int,giacca))
    temperatura = list(map(int,temperatura))
    giacca = list(map(int,giacca))
    giochi = list(map(int,giochi))
    scuola = list(map(int,scuola))
    
    fig,axs = plt.subplots(nrows = 2, ncols = 2,figsize=(20,20))
    axs[0,0].plot(mesi,temperatura,"bo-")
    axs[0,0].grid()
    axs[0,0].set_title("Temperatura mediaa di ogni mese",fontsize = 15)
    axs[0,0].set_xlabel("Mesi")
    axs[0,0].set_ylabel("Temperatura Media")
    
    axs[0,1].plot(mesi,giacca,"bo-")
    axs[0,1].grid()
    axs[0,1].set_title("Media dei giorni in un mese in cui si indossa la giacca",fontsize = 15)
    axs[0,1].set_xlabel("Mesi")
    axs[0,1].set_ylabel("Numero di giorni in cui si esce con la giacca")
    
    axs[1,0].plot(mesi,giochi,"bo-")
    axs[1,0].grid()
    axs[1,0].set_title("Media dei giorni in un mese di quanto si gioca",fontsize = 15)
    axs[1,0].set_xlabel("Mesi")
    axs[1,0].set_ylabel("Numero di giorni in cui si gioca")
    
    axs[1,1].plot(mesi,scuola,"bo-")
    axs[1,1].grid()
    axs[1,1].set_title("Media dei giorni in un mese di quando si va a scuola",fontsize = 15)
    axs[1,1].set_xlabel("Mesi")
    axs[1,1].set_ylabel("Numero di giorni in cui vado a scuola")
    plt.show()
if __name__=="__main__":
    main()