import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)


class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()


# Experimentación
# Crear puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir puntos
print("Puntos:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

# Consultar cuadrantes
print("\nCuadrantes:")
print(f"A pertenece al {A.cuadrante()}")
print(f"C pertenece al {C.cuadrante()}")
print(f"D pertenece al {D.cuadrante()}")

# Consultar vectores
print("\nVectores:")
print(f"Vector AB: {A.vector(B)}")
print(f"Vector BA: {B.vector(A)}")

# Consultar distancias (optativo)
print("\nDistancias:")
print(f"Distancia entre A y B: {A.distancia(B)}")
print(f"Distancia entre B y A: {B.distancia(A)}")

# Determinar el punto más lejano del origen (optativo)
distancias = {
    "A": A.distancia(D),
    "B": B.distancia(D),
    "C": C.distancia(D)
}
punto_mas_lejano = max(distancias, key=distancias.get)
print(f"\nEl punto más lejano del origen es: {punto_mas_lejano}")

# Crear rectángulo con A y B
rectangulo = Rectangulo(A, B)

# Consultar base, altura y área del rectángulo
print("\nRectángulo:")
print(f"Base: {rectangulo.base()}")
print(f"Altura: {rectangulo.altura()}")
print(f"Área: {rectangulo.area()}")