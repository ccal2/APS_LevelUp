import abc
from typing import Optional

from model.Habilidade.Habilidade import Habilidade
from model.Interesse.Interesse import Interesse


class IRepositorioHabilidade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def consultarHabilidade(self, interesses: "list[Interesse]") -> Optional[Habilidade]:
        return
