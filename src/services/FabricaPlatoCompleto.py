from src.services.abtracts.Fabrica import Fabrica
from src.services.abtracts.Plato import Plato
from .PlatoCompleto import PlatoCompleto


class FabricaPlatoCompleto(Fabrica):


    def crearPlato(self) -> Plato:
        print('fabricando plato completo')
        return PlatoCompleto()
