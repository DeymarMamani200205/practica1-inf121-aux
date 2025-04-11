class Videojuego:
    def __init__(self, nombre: str, plataforma: str = None, cantidadJugadores: int = 0):
        self.nombre = nombre
        self.plataforma = plataforma if plataforma is not None else "Desconocida"
        self.cantidadJugadores = cantidadJugadores

    def mostrar(self) -> None:
        print(f"Videojuego: {self.nombre}, Plataforma: {self.plataforma}, Cantidad de Jugadores: {self.cantidadJugadores}")

    def agregarJugadores(self, nuevosJugadores: int) -> None:
        if self.cantidadJugadores == 0:
            self.cantidadJugadores = 1
            print(f"Se agregó 1 jugador a {self.nombre}. Total: {self.cantidadJugadores}")
        else:
            self.cantidadJugadores += nuevosJugadores
            print(f"Se agregaron {nuevosJugadores} jugadores a {self.nombre}. Total: {self.cantidadJugadores}")

    def __str__(self) -> str:
        return f"Videojuego: {self.nombre}, Plataforma: {self.plataforma}, Cantidad de Jugadores: {self.cantidadJugadores}"


print("=== Instanciando videojuegos ===")
videojuego1 = Videojuego("Minecraft", "PC", 0)
videojuego2 = Videojuego("FIFA 23")

videojuegos = [videojuego1, videojuego2]

for juego in videojuegos:
    print(juego)

print("\n=== Mostrando datos de los videojuegos ===")
for juego in videojuegos:
    juego.mostrar()

print("\n=== Agregando jugadores ===")
videojuego1.agregarJugadores(5)
videojuego2.agregarJugadores(3)