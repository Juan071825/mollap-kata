from filtres.filtro import Filtro

class Autorizacion(Filtro):

    def ejecucion(self, peticion):
        print("Autorización OK")