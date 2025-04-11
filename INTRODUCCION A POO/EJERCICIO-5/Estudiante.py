class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2
    
    def calcular_promedio(self):
        return (self.nota_1 + self.nota_2) / 2
    
    def aprobo(self):
        return self.calcular_promedio() >= 6

if __name__ == "__main__":
    estudiante1 = Estudiante("Carlos", 8, 9)
    estudiante2 = Estudiante("Sofía", 4, 7)
    estudiante3 = Estudiante("Pedro", 5, 6)
    
    print(f"Promedio de {estudiante1.nombre}: {estudiante1.calcular_promedio()} - Aprobó: {estudiante1.aprobo()}")
    print(f"Promedio de {estudiante2.nombre}: {estudiante2.calcular_promedio()} - Aprobó: {estudiante2.aprobo()}")
    print(f"Promedio de {estudiante3.nombre}: {estudiante3.calcular_promedio()} - Aprobó: {estudiante3.aprobo()}")