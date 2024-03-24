from abc import ABC, abstractmethod
from .Plato import Plato


class Fabrica(ABC):

    @abstractmethod
    def crearPlato(self) -> Plato:
        pass

