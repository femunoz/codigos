import math
# area: float float float -> float
# calcula el area de un triangulo de lados a,
# b y c. 
# ej: area(3,4,5) entrega 6
# ej: area(6,8,10) entre 24

def area(a,b,c):
	s = (a+b+c)/2
	# en gral: <modulo>.<funcion>(<parametros>)
	a = math.sqrt( s*(s-a)*(s-b)*(s-c) )
	# PROHIBIDO utilizar "print" para reutilizar
	return a

#print(area(3,4,5))
#print(area(6,8,10))

if  area(3,4,5) == 6.0: print ("ok")
else:
	print("AssertionError")
assert area(6,8,10) == 24.0

#perimetro: float float float -> float
# calcula el perimetro de un triangulo de lados a, b yc.
# ej: perimetro(6,6,6) entrega 18
def perimetro(a,b,c):
	return a+b+c

assert perimetro(6,6,6) == 18.0



