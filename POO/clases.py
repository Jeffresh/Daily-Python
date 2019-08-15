class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
        self.__velocidad = 0;

    def arrancar(self, arrancar):
        self.__enmarcha = arrancar

        if self.__enmarcha:
            chequeo = self.__chequeo_interno()
        if arrancar and chequeo :
            print("Coche en marcha.")
        elif self.__enmarcha == True and not chequeo:
            print("No podemos arrancar, chequeo incorrecto.")
        else:
            print("Se ha parado el coche.")

    def acelerar(self):
        if self.__enmarcha:
            self.__velocidad += 1
        else:
            print("El coche no está en marcha, arránquelo primero.")

    def frenar(self):
        if self.__enmarcha:
            self.__velocidad -= 1
        else:
            print("El coche ya está parado.")

    def girar(self, direccion):

        if direccion == "derecha":
            print("Girando a la derecha.")
        if direccion == "izquierda":
            print("Girando a la derecha.")





    def estado(self):
        print("El coche tiene un largo de {} cm \n un ancho de {} cm \n tiene {} ruedas \n".format(
            self.largoChasis, self.anchoChasis, self.ruedas))

    def __chequeo_interno(self):
        print("Realizado chequeo interno")
        self.gasolina = "ok"
        self.aceite ="ok"
        self.puertas ="cerradas"

        if self.gasolina =="ok" and self.aceite =="ok" and self.puertas =="cerradas":
            return True
        else:
            return False

