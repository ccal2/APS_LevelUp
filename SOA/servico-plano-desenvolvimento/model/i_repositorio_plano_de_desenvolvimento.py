import abc
from typing import Optional


class IRepositorioPlanoDeDesenvolvimento(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def inserir(self, plano_de_desenvolvimento: dict):
        return

    @abc.abstractmethod
    def consultar_plano_de_desenvolvimento(self, id_colaborador: str) -> Optional[dict]:
        return

    @abc.abstractmethod
    def atualizar(self, plano_de_desenvolvimento: dict):
        return

    @abc.abstractmethod
    def remover(self, plano_de_desenvolvimento: dict):
        return
