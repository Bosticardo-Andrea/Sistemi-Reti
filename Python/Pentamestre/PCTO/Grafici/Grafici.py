from tkinter import font
import matplotlib.pyplot as plt


f = open("./csv.txt","r")
righe = f.readlines()
f.close()
riga = []
for el in righe:
    riga.append(el.split(","))

mesi,ore,media = [],[],[]
for el in riga[1:]:
    mesi.append(el[0])
    ore.append(float(el[2]))
    media.append(float(el[3][:-1]))
fig,axs = plt.subplots(nrows = 1, ncols = 2,figsize=(20,20))#creo lo schermo e gli do una dimensione
#ax.plot(X,Y,"ro--")#assegno gli assi
axs[0].plot(mesi,ore,"bo-")
axs[0].grid()
axs[0].set_title("Media voti e ore studio",fontsize = 15)
axs[0].set_xlabel("Mesi")
axs[0].set_ylabel("Ore")
axs[1].plot(mesi,media,"bo-")
axs[1].grid()
axs[1].set_title("Media voti e ore studio",fontsize = 15)
axs[1].set_xlabel("Mesi")
axs[1].set_ylabel("Media voti")
plt.savefig("./grafico.png")

    