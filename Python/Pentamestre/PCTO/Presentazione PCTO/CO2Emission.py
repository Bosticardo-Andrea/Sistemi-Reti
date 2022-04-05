#created by Bosticardo Andrea
from operator import index
import os
from pickle import NONE
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
PATH = "C:\\Users\\User\\OneDrive - itiscuneo.eu\\Scuola\\SUPERIORI\\CLASSE 4^A\\PENTAMESTRE\\Sistemi e Reti\\Python\\PCTO\\Presentazione PCTO"#file path 
cmaps = {}
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
#name = file name  JumpsLines = jump of header lines
def readCSV(name,JumpsLines):#read CSV or any file
    f = open(name,"r")
    righe = f.readlines()
    f.close()
    anno,riga,total,GasFuel,LiquidFuel,SolidFuel,Cement,GasFlaring = [],[],[],[],[],[],[],[]
    for el in righe[JumpsLines:]:
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
#color mapping based on data
def colorGraphics(valy,valx,axs,fig,pos,pos1,scale):#scale = chromatic scale
    #link for all possible color scales: https://matplotlib.org/stable/tutorials/colors/colormaps.html
    if(pos1 != None):#if the graph has more than one column
        valy_normalized = [x/max(valy) for x in valy]#list containing every single data but the maximum
        my_cmap = plt.cm.get_cmap(scale)#color scale setting
        colors = my_cmap(valy_normalized)
        rects = axs[pos,pos1].bar(valx, valy, color=colors)#create the chart
        sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(0,max(valy)))#color association based on data
        sm.set_array([])
        fig.colorbar(sm, ax=axs[pos,pos1])#color bar creation
        valx_index = [x for x in valy if x > 0]
        valx_index = valy.index(min(valx_index))
        axs[pos,pos1].set_xlim(valx[valx_index],valx[-1]+1)#x scale limits setting
        axs[pos,pos1].grid()#grid for all data
    else:
        valy_normalized = [x/max(valy) for x in valy]#list containing every single data but the maximum
        my_cmap = plt.cm.get_cmap(scale)#color scale setting
        colors = my_cmap(valy_normalized)
        rects = axs[pos].bar(valx, valy, color=colors)
        sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(0,max(valy)))#color association based on data
        sm.set_array([])
        fig.colorbar(sm, ax=axs[pos])#color bar creation
        valx_index = [x for x in valy if x > 0]
        valx_index = valy.index(min(valx_index))
        axs[pos].set_xlim(valx[valx_index],valx[-1]+1)#scale limits setting
        axs[pos].grid()#grid for all data
        
def main():
    os.chdir(PATH)
    anno,total,GasFuel,LiquidFuel,SolidFuel,Cement,GasFlaring = readCSV("CO2_emissions.csv",1)
    fig,ax = plt.subplots(figsize=(20,20),layout='constrained')#window creation
    #data entry
    ax.plot(anno, GasFuel, label='GasFuel')  
    ax.plot(anno, LiquidFuel, label='LiquidFuel') 
    ax.plot(anno, SolidFuel, label='SolidFuel')  
    ax.plot(anno, Cement, label='Cement') 
    ax.plot(anno, GasFlaring, label='GasFlaring') 
    ax.plot(anno, total, label='Total') 
    ax.set_xlim(anno[total.index(min(total))],anno[-1]+1)#scale limits setting
    ax.grid()
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')  
    ax.set_title("Simple Plot") 
    ax.legend();#creation of the legend
    #plt.show()
    
    fig,axs = plt.subplots(nrows = 2, ncols = 2,figsize=(10,10),layout='constrained')#window creation
    #axs[0,0].bar(anno,GasFuel)
    colorGraphics(GasFuel,anno,axs,fig,0,0,"viridis")
    axs[0,0].set_title(f"Emissione dovute al combustibile a gas dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[0,0].set_xlabel("Anni")
    axs[0,0].set_ylabel("Emissione dovute al combustibile a gas ")
    
    #axs[0,1].bar(anno,LiquidFuel)
    colorGraphics(LiquidFuel,anno,axs,fig,0,1,"winter")
    axs[0,1].set_title(f"Emissione dovute al combustibile liquido dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[0,1].set_xlabel("Anni")
    axs[0,1].set_ylabel("Emissione dovute al combustibile liquido")
    
    #axs[1,0].bar(anno,SolidFuel)
    colorGraphics(SolidFuel,anno,axs,fig,1,0,"summer")
    axs[1,0].set_title(f"Emissione dovute al combustibile solido dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[1,0].set_xlabel("Anni")
    axs[1,0].set_ylabel("Emissione dovute al combustibile solido")
    
    #axs[1,1].bar(anno,Cement)
    colorGraphics(Cement,anno,axs,fig,1,1,"cool")
    axs[1,1].set_title(f"Emissione dovute al cemento dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs[1,1].set_xlabel("Anni")
    axs[1,1].set_ylabel("Emissione dovute al cemento")
    
    fig1,axs1 = plt.subplots(nrows = 2, ncols = 1,figsize=(10,10),layout='constrained')#window creation
    #axs[2,0].bar(anno,GasFlaring)
    colorGraphics(GasFlaring,anno,axs1,fig1,0,None,"jet")
    axs1[0].set_title(f"Emissione dovute alle fiammate del gas dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs1[0].set_xlabel("Anni")
    axs1[0].set_ylabel("Emissione dovute alle fiammate del gas")
    
    #axs[2,1].bar(anno,total)
    colorGraphics(total,anno,axs1,fig1,1,None,'turbo')
    axs1[1].set_title(f"Emissione totali dal ({anno[0]} - {anno[-1]})",fontsize = 15)
    axs1[1].set_xlabel("Anni")
    axs1[1].set_ylabel("Emissione totali")
    plt.show()#show the graphs
    
if __name__=="__main__":
    main()