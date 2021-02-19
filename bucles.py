class Vehiculo:
    def __init__(self,color,ruedas ):
        self.color = color
        self.ruedas = ruedas
        print (f"Tengo un auto {self.color}")
    def Hola (self):
        print  (f"tengo {self.ruedas}, nomas")

x = Vehiculo ("verde", 4)

x.Hola ()