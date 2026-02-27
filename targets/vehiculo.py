from target import Target

class Vehiculo(Target):

    def __init__(self, nombre):
        Target.__init__(self, nombre)


    def ejecucion(self):
        print(f"Puerta abierta {self.nombre}!")