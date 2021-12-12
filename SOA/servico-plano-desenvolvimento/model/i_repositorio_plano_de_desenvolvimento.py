import abc
from typing import Optional

from model.plano_de_desenvolvimento import PlanoDeDesenvolvimento


class IRepositorioPlanoDeDesenvolvimento(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def inserir(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        return

    @abc.abstractmethod
    def consultar_plano_de_desenvolvimento(self, id_colaborador: str) -> Optional[PlanoDeDesenvolvimento]:
        return

    @abc.abstractmethod
    def atualizar(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        return

    @abc.abstractmethod
    def remover(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        return
