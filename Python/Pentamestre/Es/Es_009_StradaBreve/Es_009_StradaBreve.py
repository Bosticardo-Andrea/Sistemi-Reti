#created by Andrea Bosticardo
from cmath import rect
from random import randint
import sys,pygame,random,math
def disegnaGriglia(r,c,mappa):#disegno la griglia con pygame
    while(True):
        size = (500,500)
        BLACK,WHITE,RED,GREEN = (0, 0, 0),(255, 255, 255),(128,0,0),(0, 255, 0)
        pygame.init()
        screen = pygame.display.set_mode(size)
        screen.fill(BLACK)
        area = ((size[0]**2)/(r*c))
        lato = math.sqrt(area)-2
        y = r*c/4
        fnt = pygame.font.SysFont("Times New Roman", 12)
        for i in range(c):
            x = r*c/4
            for k in range(r):
                if(mappa[i][k] == -1):
                    pygame.draw.rect(screen, BLACK, (x, y, lato, lato),1)
                    pygame.draw.rect(screen, RED, (x, y, lato-3, lato-3))
                    surf_text = fnt.render("X", True, BLACK)
                    screen.blit(surf_text,(x+2,y+2))
                else: 
                    pygame.draw.rect(screen, BLACK, (x, y, lato, lato),1)
                    pygame.draw.rect(screen, GREEN, (x, y, lato-3, lato-3))
                    surf_text = fnt.render(str(mappa[i][k]), True, BLACK)
                    screen.blit(surf_text,(x+2,y+2))
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
    mappa = [celle(r) for _ in range(r)]
    return mappa,r,r
def celle(c):
    y = [random.choice([0,-1,0]) for _ in range(c)]
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
    #mappa = [[0,0,0,1],[1,0,0,1],[0,0,0,0],[1,1,1,0]]
    adiacenze,mappa = creaDiz(mappa)
    stampaMappa(mappa)
    adiacenze = adiacenza(mappa,adiacenze)
    print(f"possibili mosse:\n {adiacenze}")  
    disegnaGriglia(r,c,mappa) 
if __name__=="__main__":
    main()