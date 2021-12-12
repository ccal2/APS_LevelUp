import abc
from typing import Optional

class IRepositorioHabilidade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def inserir(self, habilidade: dict):
        return

    @abc.abstractmethod
    def consultar_habilidade(self, id: str) -> Optional[dict]:
        return

    @abc.abstractmethod
    def consultar_habilidades_por_ids(self, ids: "list[str]") -> "list[dict]":
        return

    @abc.abstractmethod
    def consultar_habilidades_por_interesses(self, interesses: "list[str]") -> "list[dict]":
        return

    @abc.abstractmethod
    def atualizar(self, habilidade: dict):
        return

    @abc.abstractmethod
    def remover(self, habilidade: dict):
        return
