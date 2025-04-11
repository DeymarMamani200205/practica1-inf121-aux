class Cocinero:
    def __init__(self, nombre: str, sueldoMes: int, horasExtra: int, sueldoHora: float):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora

    def SueldoTotal(self) -> float:
        sueldoPorHora = self.sueldoMes / 160
        return self.sueldoMes + (sueldoPorHora * self.horasExtra)

    def MostrarSiSueldoIgual(self, X: float) -> None:
        if self.sueldoMes == X:
            print(f"Cocinero: {self.nombre}, Sueldo: {self.sueldoMes}")


class Mesero:
    def __init__(self, nombre: str, sueldoMes: int, horasExtra: int, sueldoHora: float, propina: float):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora
        self.propina = propina

    def SueldoTotal(self) -> float:
        sueldoPorHora = self.sueldoMes / 160
        return self.sueldoMes + (sueldoPorHora * self.horasExtra) + self.propina

    def MostrarSiSueldoIgual(self, X: float) -> None:
        if self.sueldoMes == X:
            print(f"Mesero: {self.nombre}, Sueldo: {self.sueldoMes}")


class Administrativo:
    def __init__(self, nombre: str, sueldoMes: int, horasExtra: int, sueldoHora: float, cargo: str):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora
        self.cargo = cargo

    def SueldoTotal(self) -> float:
        sueldoPorHora = self.sueldoMes / 160
        return self.sueldoMes + (sueldoPorHora * self.horasExtra)

    def MostrarSiSueldoIgual(self, X: float) -> None:
        if self.sueldoMes == X:
            print(f"Administrativo: {self.nombre}, Sueldo: {self.sueldoMes}")


cocinero1 = Cocinero("Juan", 2000, 8, 2000.0)
mesero1 = Mesero("Ana", 1500, 6, 1500.0, 200.0)
mesero2 = Mesero("Luis", 1400, 5, 1400.0, 150.0)
admin1 = Administrativo("Marta", 2500, 7, 2500.0, "Gerente")
admin2 = Administrativo("Pedro", 3000, 9, 3000.0, "Contador")

print("Sueldo Total Cocinero 1:", cocinero1.SueldoTotal())
print("Sueldo Total Mesero 1:", mesero1.SueldoTotal())
print("Sueldo Total Mesero 2:", mesero2.SueldoTotal())
print("Sueldo Total Administrativo 1:", admin1.SueldoTotal())
print("Sueldo Total Administrativo 2:", admin2.SueldoTotal())

X = 1500
print(f"\nEmpleados con SueldoMes igual a {X}:")
cocinero1.MostrarSiSueldoIgual(X)
mesero1.MostrarSiSueldoIgual(X)
mesero2.MostrarSiSueldoIgual(X)
admin1.MostrarSiSueldoIgual(X)
admin2.MostrarSiSueldoIgual(X)