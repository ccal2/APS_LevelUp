import abc

from model.habilidade.habilidades import Habilidade
from model.interesse.interesses import Interesse


class IRepositorioHabilidade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def consultar_habilidades(self, interesses: list[Interesse]) -> list[Habilidade]:
        return
