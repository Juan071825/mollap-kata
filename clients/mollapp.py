from administrador.programadorTasques import ProgramadorTasques

from cliente import Cliente

class Mollapp(Cliente()):

    def __init__(self):
        self.programadorTareas = None


    def setProgramadorTasques(self, programadorTareas):
        self.programadorTasques = programadorTareas