from targets.vehiculo import Vehiculo
from filtres.autenticacion import Autenticacion
from filtres.autorizacion import Autorizacion
from administrador.programadorTasques import ProgramadorTasques
from clients.mollapp import Mollapp


def main():


    vehiculo = Vehiculo()


    programador = ProgramadorTasques(vehiculo)


    programador.setTarea(Autenticacion())
    programador.setTarea(Autorizacion())


    app = Mollapp()
    app.setProgramadorTasques(programador)


    app.enviarPeticion("Juan")


    vehiculo.ejecucion("Juan")


if __name__ == "__main__":
    main()
