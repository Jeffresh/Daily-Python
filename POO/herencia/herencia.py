class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        self.velocidad = 0

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: {} \nModelo: {}\nArrancado: {} \nAcelerando: {} \nFrenando: {} "
              .format(self.marca, self.modelo, self.arrancar(), self.acelera, self.frena))



class Moto(Vehiculo):
    pass


moto = Moto("Harley Davidson", "Sportster")

moto.estado()
