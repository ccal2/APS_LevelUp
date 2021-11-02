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
        nomes_habilidades = list(map(lambda x: x.titulo, planoDeDesenvolvimento.habilidades))

        planoDeDesenvolvimentoDict = {
            "habilidades": nomes_habilidades,
            "colaborador": planoDeDesenvolvimento.colaborador.email,
        }

        self.colecao.document(planoDeDesenvolvimento.collaborador.email).set(planoDeDesenvolvimentoDict)

    def consultarPlanoDeDesenvolvimento(self, emailColaborador: str) -> Optional[PlanoDeDesenvolvimento]:
        documento = self.colecao.document(emailColaborador)
        planoDeDesenvolvimento = documento.get()

        if not planoDeDesenvolvimento.exists:
            return None

        planoDeDesenvolvimentoDict = planoDeDesenvolvimento.dict()

        return PlanoDeDesenvolvimento(
            habilidades=planoDeDesenvolvimentoDict.get("habilidades"),
            colaborador=planoDeDesenvolvimento.get("colaborador")
        )

    def atualizar(self, planoDeDesenvolvimento: PlanoDeDesenvolvimento):
        return

    def remover(self, planoDeDesenvolvimento: PlanoDeDesenvolvimento):
        return
