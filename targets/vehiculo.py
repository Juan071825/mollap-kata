from target import Target

class Vehiculo(Target):


    def ejecucion(self, cliente:str):
        print(f"Puerta abierta {self.cliente}!")


    
if __name__ == '__main__':

    def test_vehiculo():
        vehiculo = Vehiculo()

        return vehiculo.ejecucion("Juan")


    test_vehiculo()