class vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color es {}, {} ruedas".format(self.color, self.ruedas)


class coche(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "{} velocidad es {}, {} cilindrada".format(super().__str__(), self.velocidad, self.cilindrada)


class camioneta(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.carga = carga

    def __str__(self):
        return "{} velocidad es {}, {} cilindrada, {} carga".format(super().__str__(), self.velocidad, self.cilindrada, self.carga)


class bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return "{} tipo {}".format(super().__str__(), self.tipo)


class motocicleta(vehiculo):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.tipo = tipo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "{} tipo {}, velocidad es {}, {} cilindrada".format(super().__str__(), self.tipo, self.velocidad, self.cilindrada)


vehiculos = [
    coche("Rojo", 4, 180, 2000),
    camioneta("Blanco", 4, 120, 2500, 1000),
    bicicleta("Azul", 2, "Montaña"),
    motocicleta("Negro", 2, "Deportiva", 150, 600)
]

def catalogar(vehiculos, ruedas=None):
    if ruedas is None:
        for vehiculo in vehiculos:
            print(type(vehiculo).__name__, ":", vehiculo)
    else:
        contador = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                contador += 1
        if contador > 0:
            print("Se han encontrado", contador, "vehículos con", ruedas, "ruedas:")
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                print(type(vehiculo).__name__, ":", vehiculo)

print("---- Catalogar todos los vehículos ----")
catalogar(vehiculos)

print("\n---- Catalogar solo los de 2 ruedas ----")
catalogar(vehiculos, 2)

print("\n---- Catalogar solo los de 4 ruedas ----")
catalogar(vehiculos, 4)


    