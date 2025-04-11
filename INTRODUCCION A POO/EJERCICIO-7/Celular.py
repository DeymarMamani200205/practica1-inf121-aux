class Celular:
    def __init__(self):
        self.aplicaciones = {}
        self.espacio_maximo = 1024
        self.bateria = 100
        self.max_apps = 20
    
    def instalar_app(self, nombre, tamano_mb):
        if len(self.aplicaciones) >= self.max_apps:
            return "No hay espacio para más aplicaciones (límite de 20)"
        if sum(self.aplicaciones.values()) + tamano_mb > self.espacio_maximo:
            return "No hay suficiente espacio en memoria"
        self.aplicaciones[nombre] = tamano_mb
        return f"Aplicación {nombre} instalada con éxito"
    
    def usar_app(self, nombre, minutos):
        if self.bateria <= 0:
            return "Celular apagado"
        if nombre not in self.aplicaciones:
            return "La aplicación no está instalada"
        tamano = self.aplicaciones[nombre]
        ciclos = minutos // 10
        if tamano > 250:
            consumo = ciclos * 5
        elif tamano > 100:
            consumo = ciclos * 2
        else:
            consumo = ciclos * 1
        self.bateria = max(0, self.bateria - consumo)
        if self.bateria == 0:
            return "Celular apagado"
        return f"Usando {nombre}, batería restante: {self.bateria}%"
    
    def bateria_restante(self):
        return f"Batería restante: {self.bateria}%"

if __name__ == "__main__":
    celular = Celular()
    print(celular.instalar_app("Juego1", 300))
    print(celular.instalar_app("Chat", 150))
    print(celular.instalar_app("Notas", 50))
    print(celular.usar_app("Juego1", 20))
    print(celular.usar_app("Chat", 30))
    print(celular.usar_app("Notas", 40))
    print(celular.bateria_restante())
    print(celular.usar_app("Juego1", 200))
    print(celular.usar_app("Chat", 10))