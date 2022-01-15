def enqueue(coda,elemento):
  pass#non fa  niente
  coda.append(elemento)
  
def dequeue(coda):
    if len(coda) != 0:
      return coda.pop(0)
    else:
      return None

cliente1 = {"nome":"Mario","id":123456}
cliente2 = {"nome":"Luigi","id":456789}
coda = []
enqueue(coda,cliente1)
enqueue(coda,cliente2)
print(coda)
