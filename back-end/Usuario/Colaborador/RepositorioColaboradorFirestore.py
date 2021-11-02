import abc
from typing import Optional
from Colaborador import Colaborador
from IRepositorioColaborador import IRepositorioColaborador
from firebase_admin import firestore
from constants import *

class RepositorioColaboradorFirestore(IRepositorioColaborador):

    def __init__(self):
        self.colecao = firestore.client().collection(DB_COLABORADORES)

    def inserir(self, colaborador: Colaborador):
        colaboradorDict = {
            "email": colaborador.email,
            "nome": colaborador.nome,
            "area": colaborador.area,
            "cargo": colaborador.cargo
        }

        self.colecao.document(colaborador.email).set(colaboradorDict)

    def consultarColaborador(self, email: str) -> Optional[Colaborador]:
        documento = self.colecao.document(email)
        colaborador = documento.get()

        if not colaborador.exists:
            return None

        #...

    def atualizar(self, colaborador: Colaborador):
        return

    def remover(self, colaborador: Colaborador):
        return
