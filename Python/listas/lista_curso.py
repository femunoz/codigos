import Nodo as nodo

n3 = nodo.Nodo("Burgos")
n2 = nodo.Nodo("Aguero",n3)
n1 = nodo.Nodo("Acuna", n2)

#print(n1.info, n2.info, n3.info)

aux = n1

while aux != None:
  print(aux.info)
  aux = aux.sgte
