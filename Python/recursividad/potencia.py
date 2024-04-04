


# "Para entender recursividad hay que entender recursividad"

# pot: int -> int
# entrega el resultado a elevado a b
# ej: pot(2,3) entrega 8
def pot(a,b):
	# CASO BASE:
	if b == 0:
		return 1
	else: # CASO RECURSIVO
		return a * pot(a,b-1)

print(pot(2,959))
