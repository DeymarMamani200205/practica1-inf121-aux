class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def mostrar_saludo(self):
        return f"Hola, soy {self.nombre} de {self.ciudad}"
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

if __name__ == "__main__":
    persona1 = Persona("Ana", 25, "Madrid")
    persona2 = Persona("Luis", 16, "Barcelona")
    persona3 = Persona("Sofía", 30, "Valencia")
    
    print(persona1.mostrar_saludo())
    print(persona2.mostrar_saludo())
    print(persona3.mostrar_saludo())
    