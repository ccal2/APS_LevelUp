from model.habilidade.Habilidade import Habilidade
from model.interesse.Interesse import Interesse
from model.habilidade.IRepositorioHabilidade import IRepositorioHabilidade
from model.habilidade.RepositorioHabilidadeFirestore import RepositorioHabilidadeFirestore


class CadastroHabilidade:
    def __init__(self, repositorio_habilidade: IRepositorioHabilidade = RepositorioHabilidadeFirestore()):
        self.repositorio_habilidade = repositorio_habilidade

    def consultar_habilidades(self, interesses: list[Interesse]) -> list[Habilidade]:
        return self.repositorio_habilidade.consultar_habilidades(interesses)
