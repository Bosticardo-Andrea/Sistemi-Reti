from wsgiref.validate import PartialIteratorWrapper


def push(pila,elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) != 0:
        return pila.pop()
    else:
        return None

pila = ['a','e','i','o','u']
pilaInv = []
pop(pilaInv)
for _ in range(len(pila)):
    push(pilaInv,pop(pila))

print(pilaInv)
