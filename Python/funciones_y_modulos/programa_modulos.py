import triangulo

a = float(input("Ingrese lado a: "))
b = float(input("Ingrese lado b: "))
c = float(input("Ingrese lado c: "))

# <modulo>.<funcion>(<parametros>)
area = triangulo.area(a,b,c)

print("AREA: ",area)
print("PERIMETRO: ",triangulo.perimetro(a,b,c))
