import abc
from typing import Optional
from PlanoDeDesenvolvimento import PlanoDeDesenvolvimento
from IRepositorioPlanoDeDesenvolvimento import IRepositorioPlanoDeDesenvolvimento
from firebase_admin import firestore
from constants import *

class RepositorioPlanoDeDesenvolvimentoFirestore(IRepositorioPlanoDeDesenvolvimento):

    def __init__(self):
        self.colecao = firestore.client().collection(DB_PLANOS_DE_DESENVOLVIMENTO)

    def inserir(self, planoDeDesenvolvimento: PlanoDeDesenvolvimento):
        planoDeDesenvolvimentoDict = {
            "habilidades": planoDeDesenvolvimento.habilidades,
            "colaborador": planoDeDesenvolvimento.colaborador,
        }

        self.colecao.document(planoDeDesenvolvimento.email).set(planoDeDesenvolvimentoDict)

    def consultarPlanoDeDesenvolvimento(self, id: str) -> Optional[PlanoDeDesenvolvimento]:
        documento = self.colecao.document(id)
        planoDeDesenvolvimento = documento.get()

        if not planoDeDesenvolvimento.exists:
            return None

        return planoDeDesenvolvimento

    def atualizar(self, planoDeDesenvolvimento: PlanoDeDesenvolvimento):
        return

    def remover(self, planoDeDesenvolvimento: PlanoDeDesenvolvimento):
        return
