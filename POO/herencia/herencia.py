class Vehiculo():
    LIMITE_VELOCIDAD = 300
    direcciones = ('recto', 'marcha atras', 'izquierda', 'derecha')

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        self.velocidad = 0
        self.direccion = 'recto'

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):

        if not self.acelera:
            self.acelera = True
            self.frena = False

        if self.velocidad < Vehiculo.LIMITE_VELOCIDAD:
            self.velocidad += 1

    def frenar(self):

        if not self.frena:
            self.frena = True
            self.acelera = False

        if self.velocidad > 0:
            self.velocidad -= 1

    def girar(self, direccion):

        if direccion in Vehiculo.direcciones:
            self.direccion = direccion
            if direccion == "derecha":
                print("Girando a la derecha.")
            if direccion == "izquierda":
                print("Girando a la derecha.")
        else:
            print('dirección incorrecta pruebe [recto, derecha, izquierda, marcha atras]')



    def estado(self):
        print("Marca: {} \nModelo: {}\nArrancado: {} \nAcelerando: {} \nFrenando: {} "
              .format(self.marca, self.modelo, self.arrancar(), self.acelera, self.frena))


class Moto(Vehiculo):
    pass


moto = Moto("Harley Davidson", "Sportster")

moto.estado()
