from typing import Optional
from firebase_admin import firestore
from utils.constantes import *

from model.usuario.administrador.administrador import Administrador
from model.usuario.administrador.i_repositorio_administrador import IRepositorioAdministrador
from model.conversores.conversor_administrador_dicionario import ConversorAdministradorDicionario


class RepositorioAdministradorFirestore(IRepositorioAdministrador):
    def __init__(self):
        self.colecao = firestore.client().collection(DB_ADMINISTRADORES)

    def consultar_administrador(self, email: str) -> Optional[Administrador]:
        referencia = self.colecao.document(email)
        documento = referencia.get()

        if not documento.exists:
            return None

        administrador = ConversorAdministradorDicionario.dicionario_para_administrador(documento.to_dict())

        return administrador
