import abc
from typing import Optional
from Habilidade import Habilidade
from Interesse.Interesse import Interesse

class IRepositorioHabilidade(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def consultarHabilidade(self, interesses: "list[Interesse]") -> Optional[Habilidade]:
        return