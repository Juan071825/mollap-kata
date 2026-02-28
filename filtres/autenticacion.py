from filtres.filtro import Filtro

class Autenticacion(Filtro):

    def ejecucion(self, peticion):
        print("Autenticación OK.")