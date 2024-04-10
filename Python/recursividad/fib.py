# fib: int -> int
# calcula el n-esimo termino de la suc. de Fibonacci

# Ej: fib(6) entrega 8

def fib(n):
	#CASO BASE:
	if n <= 2:
		return 1
	else:
		# CASO RECURSIVO:
		return fib(n-1)+fib(n-2)

assert fib(6) == 8
