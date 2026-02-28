from targets.target import Target

class Vehiculo(Target):


    def ejecucion(self, peticion):
        print(f"Puerta abierta {peticion}!")


    
if __name__ == '__main__':

    def test_vehiculo():
        vehiculo = Vehiculo()

        return vehiculo.ejecucion("Juan")


    test_vehiculo()