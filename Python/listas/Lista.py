# clase Lista

# ATRIBUTOS:
# primero: Nodo

import Nodo as n
'''
class Nodo:
    def __init__(self, info, sgte=None):
        self.info=info
        self.sgte=sgte
'''

class Lista:

	def __init__(self):
		self.primero = None

	# agrega el valor x al final de la lista.
	def append(self,x):
		
		nodo_final = n.Nodo(x)

		aux = self.primero

		if aux == None:
			self.primero = nodo_final
			print("primero: ", x)
		else:
			while aux.sgte != None:
				aux = aux.sgte

			print("x:",x)
			aux.sgte = nodo_final

	# metodo POR HACER:
	def appendLista(self,lista):
		aux = lista.primero

		if aux != None::
             #recorrer la lista que se nos pasa como parametro:
			 while aux.sgte != None:
                 aux = aux.sgte
 
             aux.sgte = lista.primero


	def imprime(self):
		aux = self.primero

		while aux != None:
			print(aux.info)
			aux = aux.sgte

lista = Lista()

lista.append(4)
lista.append(56)
lista.append(1)

lista.imprime()

