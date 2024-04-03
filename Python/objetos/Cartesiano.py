# Cartesiano.
# atributos:
# x: float
# y: float

class Cartesiano:

    # CONSTRUCTOR:

    # Cartesiano: float float -> Cartesiano
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # aString: Cartesiano -> str
    # entrega un pto cartesiano en formato de str.
    # ej: para pto1 = Cartesiano(3,4)
    # p1.aString() entrega "(3,4)"
    def aString(self):
        return ( "("+str(self.x) + "," + str(self.y)+")" )


pto1 = Cartesiano(3,4)
pto2 = Cartesiano(5,6)

# ej: quiero imprimir "(3,4)" -> "(" + "3" + "," + "4" + ")"
#print("("+str(pto1.x)+"," +str(pto1.y)+")")

print(pto1.aString())

