import abc

from model.habilidade.habilidades import Habilidade
from model.interesse.interesses import Interesse


class IRepositorioHabilidade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def consultar_habilidades(self, ids_interesses: "list[str]") -> "list[Habilidade]":
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
