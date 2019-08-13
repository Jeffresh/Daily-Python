class Coche():
    largoChasis = 250
    anchochasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self, arrancar):
        self.enmarcha = arrancar
        if arrancar:
            print("Coche en marcha.")
        else
            print("Se ha parado el coche.")

    def estado(self):
        print("El coche tiene un largo de {} cm \n un ancho de {} cm \n tiene {} ruedas \n".format(
            self.largoChasis,self.anchochasis,self.ruedas))
