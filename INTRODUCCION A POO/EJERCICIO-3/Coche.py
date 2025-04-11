class Coche:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
    
    def acelerar(self):
        self.velocidad += 10
    
    def frenar(self):
        self.velocidad -= 5

if __name__ == "__main__":
    coche1 = Coche("BMW", "X5", 80)
    coche2 = Coche("Audi", "A4", 90)
    
    coche1.acelerar()
    coche2.acelerar()
    print(f"Velocidad de {coche1.marca} {coche1.modelo}: {coche1.velocidad}")
    print(f"Velocidad de {coche2.marca} {coche2.modelo}: {coche2.velocidad}")
    
    coche1.frenar()
    coche2.frenar()
    print(f"Velocidad de {coche1.marca} {coche1.modelo}: {coche1.velocidad}")
    print(f"Velocidad de {coche2.marca} {coche2.modelo}: {coche2.velocidad}")