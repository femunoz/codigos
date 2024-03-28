# clase Entero
# atributos:
# valor: int

class Entero:
    # CONSTRUCTOR:
    # Entero: int -> Entero
    # Crea un objeto de clase Entero
    # Ej: Entero(19) crea un objeto Entero de valor 19
    def __init__(self, val):
        self.valor = val

    # suma: Entero -> Entero
    # entrega un Entero cuyo valor es la suma de self con
    # otro_entero
    # Ej: para e1=Entero(10) y e2 =Entero(-5)
    #    e1.suma(e2) entrega un Entero de valor 5
    def suma(self, otro_entero):
        return Entero(self.valor + otro_entero.valor)
    
    # aString: None -> str
    # entrega un str cuyo contenido es el valor del Entero
    # pero como str
    # Ej: e1.aString() entrega "10"
    def aString(self):
        return str(self.valor)

e1 = Entero(10)
e2 = Entero(-5)

print(e1.aString())
e_suma = e1.suma(e2)
print(e_suma.aString())







    
