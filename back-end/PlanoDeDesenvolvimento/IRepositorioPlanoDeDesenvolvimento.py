import abc
from typing import Optional
from PlanoDeDesenvolvimento import PlanoDeDesenvolvimento

class IRepositorioPlanoDeDesenvolvimento(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def inserir(self, PlanoDeDesenvolvimento: PlanoDeDesenvolvimento):
        return

    @abc.abstractmethod
    def consultarPlanoDeDesenvolvimento(self, id: str) -> Optional[PlanoDeDesenvolvimento]:
        return

    @abc.abstractmethod
    def atualizar(self, PlanoDeDesenvolvimento: PlanoDeDesenvolvimento):
        return

    @abc.abstractmethod
    def remover(self, PlanoDeDesenvolvimento: PlanoDeDesenvolvimento):
        return
