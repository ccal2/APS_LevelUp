from typing import Optional

from model.colaborador.colaborador import Colaborador
from model.colaborador.i_repositorio_colaborador import IRepositorioColaborador
from model.colaborador.repositorio_colaborador_firestore import RepositorioColaboradorFirestore


class CadastroColaborador:
    def __init__(self, repositorio_colaborador: IRepositorioColaborador = None):
        if repositorio_colaborador is None:
            self.repositorio_colaborador = RepositorioColaboradorFirestore()
        else:
            self.repositorio_colaborador = repositorio_colaborador

    def consultar_colaborador(self, email: str) -> Optional[Colaborador]:
        return self.repositorio_colaborador.consultar_colaborador(email)
