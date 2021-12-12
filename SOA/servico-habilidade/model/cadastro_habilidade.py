from model.i_repositorio_habilidade import IRepositorioHabilidade
from model.repositorio_habilidade_firestore import RepositorioHabilidadeFirestore


class CadastroHabilidade:
    def __init__(self, repositorio_habilidade: IRepositorioHabilidade = None):
        if repositorio_habilidade is None:
            self.repositorio_habilidade = RepositorioHabilidadeFirestore()
        else:
            self.repositorio_habilidade = repositorio_habilidade

    def consultar_habilidades_por_ids(self, ids: "list[str]") -> "list[dict]":
        return self.repositorio_habilidade.consultar_habilidades_por_ids(ids)

    def consultar_habilidades_por_interesses(self, interesses: "list[str]") -> "list[dict]":
        return self.repositorio_habilidade.consultar_habilidades_por_interesses(interesses)
