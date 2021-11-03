import abc
from typing import Optional

from model.Interesse.Interesse import Interesse


class IRepositorioInteresse(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def inserir(self, Interesse: Interesse):
        return

    @abc.abstractmethod
    def consultarInteresse(self, id: str) -> Optional[Interesse]:
        return

    @abc.abstractmethod
    def atualizar(self, Interesse: Interesse):
        return

    @abc.abstractmethod
    def remover(self, Interesse: Interesse):
        return
