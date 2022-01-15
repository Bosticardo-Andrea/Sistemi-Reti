#Crea un programma in Python in cui assegni una parola a una variabile stringa e poi stampi le lettere iniziali e finali della parola. 
a = "telefono"
print(a[0],a[-1]) 
#Crea un programma in Python in cui assegni una parola a una variabile stringa e poi stampi tutta la parola tranne le lettere iniziali e finali della parola
print(a[1:-1]) 
#Crea un programma in Python in cui assegni una parola a una variabile stringa e poi stampi tutta la parola alternando una lettera si e una no.
print(a[::2]) 
#Crea un programma in Python in cui assegni una parola a una variabile stringa e poi stampi la parola invertita.
print(a[::-1]) 
#Crea un programma in Python in cui assegni una parola di almeno 8 lettere a una variabile stringa e poi stampi tutta la parola con un carattere ? al posto della terza lettera.
c = a[:2] + '?' + a[3:]
print(c)