"""
0 1 2 x
x 3 4 x
5 6 7 8 
x x x 9
"""
from random import randint
import sys,pygame,random,math
def disegnaGriglia(r,c):
    while(True):
        size = (500,500)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        pygame.init()
        screen = pygame.display.set_mode(size)
        screen.fill(WHITE)
        area = ((size[0]**2)/(r*c))
        lato = math.sqrt(area)-4
        y = r*c/4
        for _ in range(c):
            x = r*c/4
            for _ in range(r):
                pygame.draw.rect(screen, BLACK, (x, y, lato, lato), 2)
                x += lato-2
            y += lato-2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
def creaDiz(mappa):
    adiacenze ={}
    n = 0
    for i,x in enumerate(mappa): 
        for num,k in enumerate(x):
            if k == 0:
                mappa[i][num] = n
                adiacenze[n] = []
                n += 1
    return adiacenze,mappa
def creaMappa():
    r = randint(3,10)
    c=r
    mappa = [celle(c) for i in range(r)]
    return mappa,r,c 
def celle(c):
    x = [0,-1]
    y = [random.choice(x) for i in range(c)]
    return y
def stampaMappa(mappa):
    for x in mappa:
        str = ""
        for i in x:
            str += " %2d " %i
        print(str)
def adiacenza(mappa,adiacenze):
    for i,x in enumerate(mappa): 
        for num,k in enumerate(x):
            if(k != -1):
                if((num-1 >= 0) & (mappa[i][num-1] != -1)):
                    adiacenze[k].append(mappa[i][num-1])
                if(num+1 < len(x)):
                    if(mappa[i][num+1] != -1):
                        adiacenze[k].append(mappa[i][num+1])  
                if(i+1 < len(mappa)):
                    if(mappa[i+1][num] != -1):
                        adiacenze[k].append(mappa[i+1][num])
                if((i-1 >= 0) & (mappa[i-1][num] != -1)):
                    adiacenze[k].append(mappa[i-1][num])
    return adiacenze
def main():
    mappa,r,c = creaMappa()
    #print(mappa)
    #mappa = [[0,0,0,1],[1,0,0,1],[0,0,0,0],[1,1,1,0]]
    adiacenze,mappa = creaDiz(mappa)
    stampaMappa(mappa)
    adiacenze = adiacenza(mappa,adiacenze)
    print(f"possibili mosse:\n {adiacenze}")  
    disegnaGriglia(r,c) 
if __name__=="__main__":
    main()