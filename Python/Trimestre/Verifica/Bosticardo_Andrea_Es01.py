import random
def casuale():
    x = random.randint(-1,1)
    while(x == 0):
        x = random.randint(-1,1)
    return x
def casualefast():
    return random.choice([-1,1])

somma = 0
movimenti = [casualefast() for _ in range (86400*5)]
for movimento in movimenti:
    somma += movimento
print(somma)

    