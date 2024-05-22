import NodoCadena as nc

# clase Cadena
# atributos:
# primero: NodoCadena


'''
class NodoCadena:

	def __init__(self, carac):
		self.caracter = carac
		self.sgte = None
'''

class Cadena: 

# Constructor de un objeto de la clase Cadena como una lista 
# de caracteres. Recibe una lista nativa de Python. 
# Ej: [“h”,”o”,”l”,”a”]
	def __init__(self, lista):
		self.primero = None


		cont = 0
		for car in lista: # car toma los valores "h" en la primera iteración
					# "o" en la segunda
					# "l" en la 3era.
					# y "a" en la ultima.

			nodo_aux = nc.NodoCadena(car)

			if cont == 0:
				self.primero = nodo_aux

			#nodo_aux2 = nc.NodoCadena(...)
			nodo_aux2.sgte = nodo_aux
			nodo_aux2 = nodo_aux

			cont = cont+1

#Devuelve el largo de la cadena 
#	def largo(self): 

#Retorna True si las cadenas son iguales 
# ej: si c1 = Cadena([“E”,”n”]) y c2 = Cadena([“E”,”n”]),
# c1.esIgual(c2) retorna True.
#	def esIgual(self, x): 

#Retorna el carácter en la posición i 
#	def charAt(self, i): 

#Retorna el string correspondiente a la cadena 
	def string(self):
		nodo_aux = self.primero
		resultado = ""
		while nodo_aux != None:
			resultado = resultado + nodo_aux.caracter 
			nodo_aux = nodo_aux.sgte
		return resultado


c1 = Cadena(["h","o","l","a"])
print(c1.string())
