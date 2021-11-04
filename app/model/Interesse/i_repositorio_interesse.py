import abc
from typing import Optional

from model.interesse.interesse import Interesse


class IRepositorioInteresse(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def inserir(self, Interesse: Interesse):
        return

    @abc.abstractmethod
    def consultar_interesse(self, titulo: str) -> Optional[Interesse]:
        return

    @abc.abstractmethod
    def consultar_interesses(self, ids: list[str]) -> list[Interesse]:
        return

    @abc.abstractmethod
    def atualizar(self, Interesse: Interesse):
        return

    @abc.abstractmethod
    def remover(self, Interesse: Interesse):
        return
