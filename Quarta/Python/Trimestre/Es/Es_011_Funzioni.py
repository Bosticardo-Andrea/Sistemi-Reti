def somma_moltiplicazione(x,y):
    #return {"somma":x+y,"moltiplicazione":x*y}
    return x+y,x*y

#lambda fuction
sm2 = lambda x,y:(x+y,x*y)
sm = lambda f,k:(f+k,f*k)
#s,m = somma_moltiplicazione(10,5)
print(somma_moltiplicazione(10,5))
print(sm(3,5))