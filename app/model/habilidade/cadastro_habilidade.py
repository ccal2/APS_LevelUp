from model.habilidade.habilidades import Habilidade
from model.interesse.interesses import Interesse
from model.habilidade.i_repositorio_habilidade import IRepositorioHabilidade
from model.habilidade.repositorio_habilidade_firestore import RepositorioHabilidadeFirestore


class CadastroHabilidade:
    def __init__(self, repositorio_habilidade: IRepositorioHabilidade = RepositorioHabilidadeFirestore()):
        self.repositorio_habilidade = repositorio_habilidade

    def consultar_habilidades(self, interesses: "list[Interesse]") -> "list[Habilidade]":
        return self.repositorio_habilidade.consultar_habilidades(interesses)
