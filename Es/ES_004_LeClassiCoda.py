class Coda():
    def __init__(self):
        self.coda=[]
        
    def enqueue(self,elemento):
        self.coda.append(elemento)
    
    def dequeue(self):
        if len(self.coda) != 0:
            return self.coda.pop(0)
        else:
            return None
    
    def print(self): 
        print(self.coda)

p1 = Coda()#istanza classe
p1.enqueue(3)
p1.enqueue(10)
p1.print()
x = p1.dequeue()
p1.print()