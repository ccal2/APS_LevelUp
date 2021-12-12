from typing import Optional
from firebase_admin import firestore

from model.i_repositorio_plano_de_desenvolvimento import IRepositorioPlanoDeDesenvolvimento


class RepositorioPlanoDeDesenvolvimentoFirestore(IRepositorioPlanoDeDesenvolvimento):
    def __init__(self):
        self.colecao = firestore.client().collection("planos-de-desenvolvimento")

    def inserir(self, plano_de_desenvolvimento: dict):
        id_colaborador = plano_de_desenvolvimento.get("id_colaborador")

        if id_colaborador is None:
            return

        self.colecao.document(id_colaborador).set(plano_de_desenvolvimento)

    def consultar_plano_de_desenvolvimento(self, id_colaborador: str) -> "Optional[dict]":
        referencia = self.colecao.document(id_colaborador)
        documento = referencia.get()

        if not documento.exists:
            return None

        return documento.to_dict()

    def atualizar(self, plano_de_desenvolvimento: dict):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(plano_de_desenvolvimento)

    def remover(self, plano_de_desenvolvimento: dict):
        id_colaborador = plano_de_desenvolvimento.get("id_colaborador")

        if id_colaborador is None:
            return

        self.colecao.document(id_colaborador).delete()
