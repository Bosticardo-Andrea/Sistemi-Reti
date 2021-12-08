from operator import xor
import random
def casuale():
    x= random.randint(-1,1)
    while(x == 0):
        x = random.randint(-1,1)
    return x
somma = 0
movimenti = [casuale() for _ in range (86400*5)]
for movimento in movimenti:
    somma += movimento
print(somma)

    