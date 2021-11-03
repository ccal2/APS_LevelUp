import abc
from typing import Optional

from model.Usuario.Colaborador.Colaborador import Colaborador

class IRepositorioColaborador(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def inserir(self, colaborador: Colaborador):
        return

    @abc.abstractmethod
    def consultarColaborador(self, email: str) -> Optional[Colaborador]:
        return

    @abc.abstractmethod
    def atualizar(self, colaborador: Colaborador):
        return

    @abc.abstractmethod
    def remover(self, colaborador: Colaborador):
        return
