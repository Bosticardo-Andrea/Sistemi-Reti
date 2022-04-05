import matplotlib.pyplot as plt
import os
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap
import pandas as pd
PATH = "C:\\Users\\User\\OneDrive - itiscuneo.eu\\Scuola\\SUPERIORI\\CLASSE 4^A\\PENTAMESTRE\\Sistemi e Reti\\Python\\PCTO\\Presentazione PCTO"

def readCSV(name):
    f = open(name,"r")
    righe = f.readlines()
    f.close()
    year,temp,riga = [],[],[]
    for el in righe[5:]:
        riga.append(el.split(","))
    for el in riga:
        year.append(int(el[0]))
        temp.append(float(el[1]))
    return year,temp
def main():
    os.chdir(PATH)
    year,temp = readCSV("Temperature_Anomaly.csv")
    FIRST = year[0]
    LAST = year[-1]
    cmap = ListedColormap([
        '#08306b', '#08519c', '#2171b5', '#4292c6',
        '#6baed6', '#9ecae1', '#c6dbef', '#deebf7',
        '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a',
        '#ef3b2c', '#cb181d', '#a50f15', '#67000d',
    ])
    fig = plt.figure(figsize=(21,9))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    col = PatchCollection([
        Rectangle((y, 0), 1, 1)
        for y in range(FIRST, LAST + 1)
    ])
    col.set_array(temp)
    col.set_cmap(cmap)
    ax.add_collection(col)
    ax.set_ylim(0, 1)
    ax.set_xlim(FIRST, LAST + 1)
    fig.savefig('warming-stripes.png')
    plt.show()

if __name__=="__main__":
    main()