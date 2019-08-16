class Coche:

    def desplazamiento(self):
        print("utilizo marchas, y pedales de embrague, freno y acelerador para moverme.")


class Moto:

    def desplazamiento(self):
        print("Utilizo palanca de marchas y puño para moverme.")


class Camion:

    def desplazamiento(self):
        print("Me desplazo igual que el coche pero peso mucho y soy muy grande.")


def desplazamientovehiculo(vehiculo):

    vehiculo.desplazamiento()


vehiculo1 = Coche()
vehiculo2 = Moto()
vehiculo3 = Camion()
vehiculos =[vehiculo1, vehiculo2, vehiculo3]

for vehiculo in vehiculos:
    vehiculo.desplazamiento()
