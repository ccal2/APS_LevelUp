from model.plano_de_desenvolvimento import PlanoDeDesenvolvimento
from model.i_repositorio_plano_de_desenvolvimento import IRepositorioPlanoDeDesenvolvimento
from model.repositorio_plano_de_desenvolvimento_firestore import RepositorioPlanoDeDesenvolvimentoFirestore


class CadastroPlanoDeDesenvolvimento:
    def __init__(self, repositorio_plano_de_desenvolvimento: IRepositorioPlanoDeDesenvolvimento = None):
        if repositorio_plano_de_desenvolvimento is None:
            self.repositorio_plano_de_desenvolvimento = RepositorioPlanoDeDesenvolvimentoFirestore()
        else:
            self.repositorio_plano_de_desenvolvimento = repositorio_plano_de_desenvolvimento

    def consultar_plano_de_desenvolvimento(self, id_colaborador: str) -> PlanoDeDesenvolvimento:
        return self.repositorio_plano_de_desenvolvimento.consultar_plano_de_desenvolvimento(id_colaborador)
