import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
import os
PATH = "C:\\Users\\User\\OneDrive - itiscuneo.eu\\Scuola\\SUPERIORI\\CLASSE 4^A\\PENTAMESTRE\\Sistemi e Reti\\Python\\PCTO\\Presentazione PCTO"
def readCSV(name):
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

os.chdir(PATH)
data_x,data_hight = readCSV("CO2_emissions.csv")

data_hight_normalized = [x / max(data_hight) for x in data_hight]

fig, ax = plt.subplots(figsize=(15, 4))

my_cmap = plt.cm.get_cmap('GnBu')
colors = my_cmap(data_hight_normalized)

rects = ax.bar(data_x, data_hight, color=colors)

sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(0,max(data_hight)))

sm.set_array([])

cbar = plt.colorbar(sm)
cbar.set_label('Color', rotation=270,labelpad=25)

plt.xticks(data_x)    
plt.ylabel("Y")

plt.title('How to plot a bar chart with a colorbar with matplotlib ?')

plt.savefig("bar_chart_with_colorbar_03.png", bbox_inches='tight')

plt.show()