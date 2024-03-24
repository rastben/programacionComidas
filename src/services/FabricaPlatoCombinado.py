from src.services.abtracts.Fabrica import Fabrica
from src.services.abtracts.Plato import Plato
from .PlatoCombinado import PlatoCombinado


class FabricaPlatoCombindado(Fabrica):


    def crearPlato(self) -> Plato:
        print('fabricando plato combinado')
        return PlatoCombinado()
