class Tareas():

    def __init__(self):
        self.tareas = []
        self.target = None

    def getTareas(self):
        return self.tareas
    
    def getTarget(self):
        return self.target
    
    def addTarea(self, filtre):
        self.tareas.append(filtre)

    def ejecucion(self, peticion):

        for filtre in self.tareas:
            filtre.ejecucion(peticion)

    def setTarget(self, target):
        self.target = target