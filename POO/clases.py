class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancar):
        self.enmarcha = arrancar
        if arrancar:
            print("Coche en marcha.")
        else:
            print("Se ha parado el coche.")

    def estado(self):
        print("El coche tiene un largo de {} cm \n un ancho de {} cm \n tiene {} ruedas \n".format(
            self.largoChasis, self.anchoChasis, self.ruedas))
