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

		if len(lista)==0:
			return None
		self.primero = nc.NodoCadena(lista[0])
		aux = self.primero

		i = 0
		for i in range(1,len(lista)):
			aux.sgte = nc.NodoCadena(lista[i])
			aux = aux.sgte

#Devuelve el largo de la cadena 
	def largo(self):
		n = 0
		if self.primero == None: return 0

		aux = self.primero
		while aux != None:
			aux = aux.sgte
			n=n+1

		return n

#Retorna True si las cadenas son iguales 
# ej: si c1 = Cadena([“E”,”n”]) y c2 = Cadena([“E”,”n”]),
# c1.esIgual(c2) retorna True.
	def esIgual(self, x):

		n = self.largo()

		if n != x.largo(): return False

		#if n == 0: return True

		aux_self = self.primero
		aux_x = x.primero

		for i in range(n):
			if aux_self.caracter != aux_x.caracter:
				return False

			aux_self = aux_self.sgte
			aux_x = aux_x.sgte

		return True


#Retorna el carácter en la posición i 

	def charAt(self, i):
		n = self.largo()

		if n == 0:
			return None
		if i>n:
			return None

		i_aux=1
		aux = self.primero

		while aux!=None:

			if i_aux == i:
				return aux.caracter
			i_aux = i_aux +1
			aux = aux.sgte
		return None


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

c2 = Cadena(["h","o","L","a"])
c3 = Cadena(["H","O","L", "A"])

c4 = Cadena(["h","o","l","A"])
c5 = Cadena(["h","o","l","a","s"])

print(c1.largo())


print(c1.esIgual(c1))
print(c1.esIgual(c2))
print(c1.esIgual(c3))
print(c1.esIgual(c4))
print(c1.esIgual(c5))

print(c2.charAt(3))
