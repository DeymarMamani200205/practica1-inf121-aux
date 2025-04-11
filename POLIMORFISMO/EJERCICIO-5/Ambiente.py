class Ambiente:
    def __init__(self, nombre: str):
        self.nombre = nombre
    def mostrar(self) -> None:
        print(f"Ambiente: {self.nombre}")
    def cantidadMuebles(self) -> int:
        return 0
    def __str__(self) -> str:
        return f"Ambiente: {self.nombre}"

class Oficina(Ambiente):
    def __init__(self, nombre: str, nroSillas: int, nroEscritorios: int, nroEstantes: int):
        super().__init__(nombre)
        self.nroSillas = nroSillas
        self.nroEscritorios = nroEscritorios
        self.nroEstantes = nroEstantes

    def mostrar(self) -> None:
        print(f"Oficina: {self.nombre}, Sillas: {self.nroSillas}, Escritorios: {self.nroEscritorios}, Estantes: {self.nroEstantes}")

    def cantidadMuebles(self) -> int:
        return self.nroSillas + self.nroEscritorios + self.nroEstantes

class Aula(Ambiente):
    def __init__(self, nombre: str, capacidad: int, nroPupitres: int):
        super().__init__(nombre)
        self.capacidad = capacidad
        self.nroPupitres = nroPupitres

    def mostrar(self) -> None:
        print(f"Aula: {self.nombre}, Capacidad: {self.capacidad}, Pupitres: {self.nroPupitres}")

    def cantidadMuebles(self) -> int:
        return self.nroPupitres

class Laboratorio(Ambiente):
    def __init__(self, nombre: str, capacidad: int, nroMesas: int, nroSillas: int):
        super().__init__(nombre)
        self.capacidad = capacidad
        self.nroMesas = nroMesas
        self.nroSillas = nroSillas

    def mostrar(self) -> None:
        print(f"Laboratorio: {self.nombre}, Capacidad: {self.capacidad}, Mesas: {self.nroMesas}, Sillas: {self.nroSillas}")

    def cantidadMuebles(self) -> int:
        return self.nroMesas + self.nroSillas

print("=== Instanciando ambientes ===")
oficina1 = Oficina("Oficina A", 5, 3, 2)
oficina2 = Oficina("Oficina B", 4, 2, 1)
aula1 = Aula("Aula 101", 30, 30)
aula2 = Aula("Aula 102", 25, 25)
laboratorio1 = Laboratorio("Lab Química", 20, 10, 20)
ambientes = [oficina1, oficina2, aula1, aula2, laboratorio1]
print("\n=== Datos de cada ambiente ===")
for ambiente in ambientes:
    ambiente.mostrar()
print("\n=== Cantidad de muebles por ambiente ===")
total_muebles = 0
for ambiente in ambientes:
    muebles = ambiente.cantidadMuebles()
    print(f"{ambiente.__class__.__name__} {ambiente.nombre}: {muebles} muebles")
    total_muebles += muebles
print(f"\nTotal de muebles en todos los ambientes: {total_muebles}")