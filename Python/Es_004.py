#affettare le stringhe
#slicing
stringa = "classe quarta A robotica"
print(f"il primo carattere é {stringa[0]}")
print(f"il primo carattere é {stringa[-1]}")
#prende i caratteri dal primo numero '0' al quinto = 6-1
print(stringa[0:6])#slicing di stringhe
#dal sesto fino alla fine
print(stringa[6:])
#dal primo fino al -3
print(stringa[:-2])
#prende tutti i caratteri dal 2 al 13 a step di 2
print(stringa[2:13:2])#gap
#inverte la stringa, dall'inizio al fondo con salti di -1
print(stringa[::-1])
