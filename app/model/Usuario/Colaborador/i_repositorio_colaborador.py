import abc
from typing import Optional

from model.usuario.colaborador.colaborador import Colaborador


class IRepositorioColaborador(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def inserir(self, colaborador: Colaborador):
        return

    @abc.abstractmethod
    def consultar_colaborador(self, email: str) -> Optional[Colaborador]:
        return

    @abc.abstractmethod
    def atualizar(self, colaborador: Colaborador):
        return

    @abc.abstractmethod
    def remover(self, colaborador: Colaborador):
        return
