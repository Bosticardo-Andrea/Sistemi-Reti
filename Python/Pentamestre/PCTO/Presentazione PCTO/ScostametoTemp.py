#created by Bosticardo Andrea
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
cmaps = {}
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
PATH = "C:\\Users\\User\\OneDrive - itiscuneo.eu\\Scuola\\SUPERIORI\\CLASSE 4^A\\PENTAMESTRE\\Sistemi e Reti\\Python\\PCTO\\Presentazione PCTO"#file path 
#name = file name  JumpsLines = jump of header lines
def readCSV(name):#read CSV or any file
    f = open(name,"r")
    righe = f.readlines()
    f.close()
    anno,scostamento,riga = [],[],[]
    for el in righe[5:]:
        riga.append(el.split(","))
    for el in riga:
        anno.append(int(el[0]))
        scostamento.append(float(el[1]))
    return anno,scostamento
def main():
    os.chdir(PATH)
    anno,scostamento = readCSV("Temperature_Anomaly.csv")
    fig,axs = plt.subplots(nrows = 2, ncols = 1,layout='constrained')
    #color mapping based on data
    #link for all possible color scales: https://matplotlib.org/stable/tutorials/colors/colormaps.html
    scostamento_normalized = [x for x in scostamento]#list containing every single data but the maximum
    my_cmap = plt.cm.get_cmap('seismic')#color scale setting
    colors = my_cmap(scostamento_normalized)
    rects = axs[0].bar(anno, scostamento, color=colors)#create the chart
    sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(min(scostamento),max(scostamento)))#color association based on data
    sm.set_array([])
    fig.colorbar(sm, ax=axs[0])#color bar creation
    axs[0].grid()#grid
    axs[0].set_xlim(anno[0]-1,anno[-1]+1)#x scale limits setting
    axs[0].set_title(f"Scostamento temperatura ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[0].set_xlabel("Anni")
    axs[0].set_ylabel("Scostamento temperatura")
    
    #web page for all types of graphics: https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
    x2 = axs[1].scatter(anno, scostamento, c=scostamento, cmap='RdBu_r')#create the scatter type chart
    axs[1].set_xlim(anno[0]-1,anno[-1]+1)
    fig.colorbar(sm, ax=axs[1])
    axs[1].grid()
    plt.show()
if __name__=="__main__":
    main()