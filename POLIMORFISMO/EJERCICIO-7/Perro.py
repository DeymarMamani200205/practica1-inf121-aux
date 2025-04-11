class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def hacerSonido(self) -> None:
        print(f"{self.nombre} hace un sonido genérico.")

    def moverse(self) -> None:
        print(f"{self.nombre} se mueve de manera genérica.")

    def __str__(self) -> str:
        return f"Animal: {self.nombre}"

class Perro(Animal):
    def __init__(self, nombre: str, edad: int, raza: str):
        super().__init__(nombre)
        self.edad = edad
        self.raza = raza

    def hacerSonido(self) -> None:
        print(f"{self.nombre} dice: ¡Guau Guau!")

    def moverse(self) -> None:
        print(f"{self.nombre} se mueve corriendo.")

    def __str__(self) -> str:
        return f"Perro: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}"

class Gato(Animal):
    def __init__(self, nombre: str, color: str):
        super().__init__(nombre)
        self.color = color

    def hacerSonido(self) -> None:
        print(f"{self.nombre} dice: ¡Miau Miau!")

    def moverse(self) -> None:
        print(f"{self.nombre} se mueve saltando.")

    def __str__(self) -> str:
        return f"Gato: {self.nombre}, Color: {self.color}"

class Pajaro(Animal):
    def __init__(self, nombre: str, tipo: str):
        super().__init__(nombre)
        self.tipo = tipo

    def hacerSonido(self) -> None:
        print(f"{self.nombre} dice: ¡Pío Pío!")

    def moverse(self) -> None:
        print(f"{self.nombre} se mueve volando.")

    def __str__(self) -> str:
        return f"Pájaro: {self.nombre}, Tipo: {self.tipo}"

print("=== Instanciando animales ===")
perro1 = Perro("Max", 5, "Labrador")
gato1 = Gato("Luna", "Gris")
pajaro1 = Pajaro("Tweety", "Canario")
animales = [perro1, gato1, pajaro1]
for animal in animales:
    print(animal)
print("\n=== Sonidos de los animales ===")
for animal in animales:
    animal.hacerSonido()
print("\n=== Movimiento de los animales ===")
for animal in animales:
    animal.moverse()