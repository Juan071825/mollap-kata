from administrador.tareas import Tareas

class ProgramadorTasques():

    def __init__(self, target):
        self.tareas = Tareas()
        self.tareas.setTarget(target)

    def getTarea(self):
        pass

    def setTarea(self):
        pass

    def setTarea(self, filtro):
        self.tareas.addTarea(filtro)


    def ejecutarTareas(self, peticion):
        self.tareas.ejecucion(peticion)