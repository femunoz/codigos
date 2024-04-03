# clase Real
# atributos:
# valor: float
# esPositivo: bool

class Real:

    # Constructor: 
    # Real: float -> Real
    def __init__(self, nroReal):
        self.valor=nroReal

    # suma: Real -> Real
    # entrega un objeto de tipo Real
    # con el valor del resultado de
    # self.valor + objetoReal.valor
    # ej: si r1 = Real(5.5) y r2 = Real(3.1)
    # r1.suma(r2) entrega un nuevo objeto
    # cuyo valor es 8.6
    def suma(self, objetoReal):
        suma_de_valores = self.valor + objetoReal.valor
        objeto_suma = Real(suma_de_valores)
        return objeto_suma
    
    # aString: None -> str
    def aString(self):
        return str(self.valor)

r1 = Real(5.5); r2 = Real(3.1)
sum = r1.suma(r2)

print(sum.aString())


