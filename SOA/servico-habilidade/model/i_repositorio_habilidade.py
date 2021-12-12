import abc
from typing import Optional

from model.habilidade import Habilidade


class IRepositorioHabilidade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def inserir(self, habilidade: Habilidade):
        return

    @abc.abstractmethod
    def consultar_habilidade(self, id: str) -> Optional[Habilidade]:
        return

    @abc.abstractmethod
    def consultar_habilidades_por_ids(self, ids: "list[str]") -> "list[Habilidade]":
        return

    @abc.abstractmethod
    def consultar_habilidades_por_interesses(self, interesses: "list[str]") -> "list[Habilidade]":
        return

    @abc.abstractmethod
    def atualizar(self, habilidade: Habilidade):
        return

    @abc.abstractmethod
    def remover(self, habilidade: Habilidade):
        return
