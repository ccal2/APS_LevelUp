import abc
from typing import Optional

from model.habilidade.habilidades import Habilidade


class IRepositorioHabilidade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def consultar_habilidades(self, interesses: "list[str]") -> "list[Habilidade]":
        return

    @abc.abstractmethod
    def inserir(self, habilidade: Habilidade):
        return

    @abc.abstractmethod
    def consultar_habilidade(self, nome: str) -> Optional[Habilidade]:
        return

    @abc.abstractmethod
    def atualizar(self, habilidade: Habilidade):
        return

    @abc.abstractmethod
    def remover(self, habilidade: Habilidade):
        return
