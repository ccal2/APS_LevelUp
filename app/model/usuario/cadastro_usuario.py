from typing import Optional

from model.usuario.usuario import Usuario
from model.usuario.colaborador.i_repositorio_colaborador import IRepositorioColaborador
from model.usuario.colaborador.repositorio_colaborador_firestore import RepositorioColaboradorFirestore
from model.usuario.administrador.i_repositorio_administrador import IRepositorioAdministrador
from model.usuario.administrador.repositorio_administrador_firestore import RepositorioAdministradorFirestore


class CadastroUsuario:
    def __init__(
        self,
        repositorio_colaborador: IRepositorioColaborador = None,
        repositorio_administrador: IRepositorioAdministrador = None,
    ):
        if repositorio_colaborador is None:
            self.repositorio_colaborador = RepositorioColaboradorFirestore()
        else:
            self.repositorio_colaborador = repositorio_colaborador

        if repositorio_administrador is None:
            self.repositorio_administrador = RepositorioAdministradorFirestore()
        else:
            self.repositorio_administrador = repositorio_administrador

    def consultar_usuario(self, email: str) -> Optional[Usuario]:
        administrador = self.repositorio_administrador.consultar_administrador(email)
        if administrador is not None:
            return administrador
        else:
            return self.repositorio_colaborador.consultar_colaborador(email)
