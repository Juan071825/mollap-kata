from clients.cliente import Cliente
from administrador.programadorTasques import ProgramadorTasques

class Mollapp(Cliente):

    def __init__(self):
        self.programadorTareas = None


    def setProgramadorTasques(self, programadorTareas):
        self.programadorTareas = programadorTareas

    def enviarPeticion(self, peticion):
        self.programadorTareas.ejecutarTareas(peticion)