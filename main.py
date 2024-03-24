import random
from src.services.abtracts.Fabrica import Fabrica
from src.services.FabricaPlatoCombinado import FabricaPlatoCombindado 
from src.services.FabricaPlatoCompleto import FabricaPlatoCompleto
from src.services.abtracts import Plato

class Main:

    def generarProgramacionDeComidas(self):
        cantidadPlatos = 15

        for _ in range(cantidadPlatos):
            plato: Plato = None

            if random.randint(1,100) > 70:
                platoCompleto: Fabrica = FabricaPlatoCompleto()
                plato = platoCompleto.crearPlato()
            else:
                platoCombinado: Fabrica = FabricaPlatoCombindado()
                plato = platoCombinado.crearPlato()
            
            plato.generarPlato()


if __name__ == "__main__":
    Main().generarProgramacionDeComidas()

