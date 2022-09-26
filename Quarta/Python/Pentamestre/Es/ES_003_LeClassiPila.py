class Pila():
    def __init__(self):
        self.pila=[]
        
    def push(self,elemento):
        self.pila.append(elemento)
    
    def pop(self):
        if len(self.pila) != 0:
            return self.pila.pop()
        else:
            return None
    
    def print(self): 
        print(self.pila)

p1 = Pila()#istanza classe
p1.push(3)
p1.push(10)
p1.print()
x = p1.pop()
p1.print()