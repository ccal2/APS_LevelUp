from model.interesse.interesses import Interesse
from model.usuario.colaborador.colaborador import Colaborador
from model.interesse.i_repositorio_interesse import IRepositorioInteresse
from model.interesse.repositorio_interesse_firestore import RepositorioInteresseFirestore


class CadastroInteresse:
    def __init__(self, repositorio_interesse: IRepositorioInteresse = None):
        if repositorio_interesse is None:
            self.repositorio_interesse = RepositorioInteresseFirestore()
        else:
            self.repositorio_interesse = repositorio_interesse

    def consultar_interesses(self, colaborador: Colaborador) -> "list[Interesse]":
        return self.repositorio_interesse.consultar_interesses(colaborador.ids_interesses)
