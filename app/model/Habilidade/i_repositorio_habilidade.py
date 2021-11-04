import abc

from model.habilidade.habilidade import Habilidade
from model.interesse.Interesse import Interesse


class IRepositorioHabilidade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def consultar_habilidades(self, interesses: list[Interesse]) -> list[Habilidade]:
        return
