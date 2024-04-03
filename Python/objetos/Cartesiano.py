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


pto1 = Cartesiano(3,4)
pto2 = Cartesiano(5,6)

# ej: quiero imprimir "(3,4)" -> "(" + "3" + "," + "4" + ")"
print("("+str(pto1.x)+"," +str(pto1.y)+")")

