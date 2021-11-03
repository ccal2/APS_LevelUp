import abc
from typing import Optional

from model.habilidade.Habilidade import Habilidade
from model.interesse.Interesse import Interesse


class IRepositorioHabilidade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def consultar_habilidade(self, interesses: list[Interesse]) -> Optional[Habilidade]:
        return
