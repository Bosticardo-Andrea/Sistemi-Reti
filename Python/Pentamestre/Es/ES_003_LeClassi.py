class Pila():
    def __init__(self,lista):
        self.pila=lista
        
    def enqueue(coda,elemento):
        pass
        coda.append(elemento)
    
    def dequeue(coda):
        if len(coda) != 0:
            return coda.pop(0)
        else:
            return None

p1 = Pila([1,2,3])
print(p1)