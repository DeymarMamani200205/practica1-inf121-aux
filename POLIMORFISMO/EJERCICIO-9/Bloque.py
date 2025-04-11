class Bloque:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def accion(self) -> None:
        print(f"Se realiza una acción genérica con el bloque de tipo {self.tipo}.")

    def colocar(self, orientacion: str) -> None:
        print(f"El bloque de tipo {self.tipo} se coloca de manera genérica en {orientacion}.")

    def romper(self) -> None:
        print(f"El bloque de tipo {self.tipo} se rompe de manera genérica.")

    def __str__(self) -> str:
        return f"Bloque de tipo: {self.tipo}"

class BloqueCofre(Bloque):
    def __init__(self, capacidad: int, resistencia: int, tipo: str):
        super().__init__(tipo)
        self.capacidad = capacidad
        self.resistencia = resistencia

    def accion(self) -> None:
        print(f"El {self.tipo} se abre y puede almacenar {self.capacidad} ítems.")

    def colocar(self, orientacion: str) -> None:
        print(f"El {self.tipo} se coloca en {orientacion} con una resistencia de {self.resistencia}.")

    def romper(self) -> None:
        print(f"El {self.tipo} se rompe y suelta los ítems almacenados.")

    def __str__(self) -> str:
        return f"BloqueCofre: Tipo: {self.tipo}, Capacidad: {self.capacidad}, Resistencia: {self.resistencia}"

class BloqueTnt(Bloque):
    def __init__(self, tipo: str, daño: int):
        super().__init__(tipo)
        self.daño = daño

    def accion(self) -> None:
        print(f"El {self.tipo} explota causando {self.daño} de daño.")

    def colocar(self, orientacion: str) -> None:
        print(f"El {self.tipo} se coloca en {orientacion} y está listo para explotar.")

    def romper(self) -> None:
        print(f"El {self.tipo} se rompe y puede detonar accidentalmente.")

    def __str__(self) -> str:
        return f"BloqueTnt: Tipo: {self.tipo}, Daño: {self.daño}"

class BloqueHorno(Bloque):
    def __init__(self, color: str, capacidadComida: int, tipo: str):
        super().__init__(tipo)
        self.color = color
        self.capacidadComida = capacidadComida

    def accion(self) -> None:
        print(f"El {self.tipo} de color {self.color} cocina hasta {self.capacidadComida} ítems de comida.")

    def colocar(self, orientacion: str) -> None:
        print(f"El {self.tipo} de color {self.color} se coloca en {orientacion}.")

    def romper(self) -> None:
        print(f"El {self.tipo} se rompe y suelta carbón residual.")

    def __str__(self) -> str:
        return f"BloqueHorno: Tipo: {self.tipo}, Color: {self.color}, Capacidad Comida: {self.capacidadComida}"

print("=== Instanciando bloques ===")
cofre1 = BloqueCofre(27, 5, "Cofre de Roble")
cofre2 = BloqueCofre(54, 6, "Cofre de Abedul")
tnt1 = BloqueTnt("TNT Estándar", 50)
tnt2 = BloqueTnt("TNT Potente", 75)
horno1 = BloqueHorno("Gris", 8, "Horno de Piedra")
horno2 = BloqueHorno("Negro", 12, "Horno de Obsidiana")

bloques = [cofre1, cofre2, tnt1, tnt2, horno1, horno2]

for bloque in bloques:
    print(bloque)

print("\n=== Acciones de los bloques ===")
for bloque in bloques:
    bloque.accion()

print("\n=== Colocando los bloques ===")
orientaciones = ["suelo", "pared", "suelo", "pared", "suelo", "pared"]
for bloque, orientacion in zip(bloques, orientaciones):
    bloque.colocar(orientacion)

print("\n=== Rompiendo los bloques ===")
for bloque in bloques:
    bloque.romper()