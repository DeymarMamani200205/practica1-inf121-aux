class Computadora:
    def __init__(self):
        self.componentes = {"CPU": "Procesador", "RAM": "Memoria", "Disco": "Almacenamiento"}
        self.encendida = False
    
    def mostrar_componentes(self):
        return self.componentes
    
    def mostrar_estado(self):
        return "Encendida" if self.encendida else "Apagada"
    
    def encender(self):
        self.encendida = True
    
    def apagar(self):
        self.encendida = False

if __name__ == "__main__":
    mi_pc = Computadora()
    print(mi_pc.mostrar_componentes())
    print(mi_pc.mostrar_estado())
    mi_pc.encender()
    print(mi_pc.mostrar_estado())
    mi_pc.apagar()
    print(mi_pc.mostrar_estado())