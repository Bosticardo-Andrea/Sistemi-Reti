from operator import index
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
PATH = "C:\\Users\\User\\OneDrive - itiscuneo.eu\\Scuola\\SUPERIORI\\CLASSE 4^A\\PENTAMESTRE\\Sistemi e Reti\\Python\\PCTO\\Presentazione PCTO"
cmaps = {}
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
def readCSV(name):
    f = open(name,"r")
    righe = f.readlines()
    f.close()
    anno,riga,total,GasFuel,LiquidFuel,SolidFuel,Cement,GasFlaring = [],[],[],[],[],[],[],[]
    for el in righe[1:]:
        riga.append(el.split(","))
    for el in riga:
        anno.append(int(el[0]))
        total.append(float(el[1]))
        GasFuel.append(float(el[2]))
        LiquidFuel.append(float(el[3]))
        SolidFuel.append(float(el[4]))
        Cement.append(float(el[5]))
        GasFlaring.append(float(el[6]))
    return anno,total,GasFuel,LiquidFuel,SolidFuel,Cement,GasFlaring
def colorGraphics(valy,valx,axs,fig,pos,pos1):
    valy_normalized = [x/max(valy) for x in valy]
    my_cmap = plt.cm.get_cmap('viridis')
    colors = my_cmap(valy_normalized)
    rects = axs[pos,pos1].bar(valx, valy, color=colors)
    sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(0,max(valy)))
    sm.set_array([])
    fig.colorbar(sm, ax=axs[pos,pos1])
    valx_index = [x for x in valy if x > 0]
    valx_index = valy.index(min(valx_index))
    axs[pos,pos1].set_xlim(valx[valx_index],valx[-1]+1)
    axs[pos,pos1].grid()
    
def main():
    os.chdir(PATH)
    anno,total,GasFuel,LiquidFuel,SolidFuel,Cement,GasFlaring = readCSV("CO2_emissions.csv")
    fig,ax = plt.subplots(figsize=(10,10),layout='constrained')
    ax.plot(anno, GasFuel, label='GasFuel')  
    ax.plot(anno, LiquidFuel, label='LiquidFuel') 
    ax.plot(anno, SolidFuel, label='SolidFuel')  
    ax.plot(anno, Cement, label='Cement') 
    ax.plot(anno, GasFlaring, label='GasFlaring') 
    ax.plot(anno, total, label='Total') 
    ax.set_xlim(anno[total.index(min(total))],anno[total.index(max(total))]+1)
    ax.grid()
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')  
    ax.set_title("Simple Plot") 
    ax.legend();
    plt.show()
    
    fig,axs = plt.subplots(nrows = 3, ncols = 2,figsize=(10,10),layout='constrained')
    #axs[0,0].bar(anno,GasFuel)
    colorGraphics(GasFuel,anno,axs,fig,0,0)
    axs[0,0].set_title(f"Emissione dovute al combustibile a gas dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[0,0].set_xlabel("Anni")
    axs[0,0].set_ylabel("Emissione dovute al combustibile a gas ")
    
    #axs[0,1].bar(anno,LiquidFuel)
    colorGraphics(LiquidFuel,anno,axs,fig,0,1)
    axs[0,1].set_title(f"Emissione dovute al combustibile liquido dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[0,1].set_xlabel("Anni")
    axs[0,1].set_ylabel("Emissione dovute al combustibile liquido")
    
    #axs[1,0].bar(anno,SolidFuel)
    colorGraphics(SolidFuel,anno,axs,fig,1,0)
    axs[1,0].set_title(f"Emissione dovute al combustibile solido dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[1,0].set_xlabel("Anni")
    axs[1,0].set_ylabel("Emissione dovute al combustibile solido")
    
    #axs[1,1].bar(anno,Cement)
    colorGraphics(Cement,anno,axs,fig,1,1)
    axs[1,1].set_title(f"Emissione dovute al cemento dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[1,1].set_xlabel("Anni")
    axs[1,1].set_ylabel("Emissione dovute al cemento")
    
    #axs[2,0].bar(anno,GasFlaring)
    colorGraphics(GasFlaring,anno,axs,fig,2,0)
    axs[2,0].set_title(f"Emissione dovute alle fiammate del gas dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[2,0].set_xlabel("Anni")
    axs[2,0].set_ylabel("Emissione dovute alle fiammate del gas")
    
    #axs[2,1].bar(anno,total)
    colorGraphics(total,anno,axs,fig,2,1)
    axs[2,1].set_title(f"Emissione totali dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[2,1].set_xlabel("Anni")
    axs[2,1].set_ylabel("Emissione totali")
    plt.show()
    
if __name__=="__main__":
    main()