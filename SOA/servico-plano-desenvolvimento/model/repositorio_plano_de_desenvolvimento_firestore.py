from typing import Optional
from firebase_admin import firestore

from model.plano_de_desenvolvimento import PlanoDeDesenvolvimento
from model.i_repositorio_plano_de_desenvolvimento import IRepositorioPlanoDeDesenvolvimento
from model.conversor_plano_de_desenvolvimento_dicionario import ConversorPlanoDeDesenvolvimentoDicionario


class RepositorioPlanoDeDesenvolvimentoFirestore(IRepositorioPlanoDeDesenvolvimento):
    def __init__(self):
        self.colecao = firestore.client().collection("planos-de-desenvolvimento")

    def inserir(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        dicionario_plano_de_desenvolvimento = ConversorPlanoDeDesenvolvimentoDicionario.plano_de_desenvolvimento_para_dicionario(plano_de_desenvolvimento)
        self.colecao.document(plano_de_desenvolvimento.id_colaborador).set(dicionario_plano_de_desenvolvimento)

    def consultar_plano_de_desenvolvimento(self, email: str) -> Optional[PlanoDeDesenvolvimento]:
        referencia = self.colecao.document(email)
        documento = referencia.get()

        if not documento.exists:
            return None

        plano_de_desenvolvimento = ConversorPlanoDeDesenvolvimentoDicionario.dicionario_para_plano_de_desenvolvimento(documento.to_dict())

        return plano_de_desenvolvimento

    def atualizar(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(plano_de_desenvolvimento)

    def remover(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        self.colecao.document(plano_de_desenvolvimento.id_colaborador).delete()
