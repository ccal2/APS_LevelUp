from typing import Optional
from firebase_admin import firestore
from utils.helpers import executar_query_extentida

from model.plano_de_desenvolvimento import PlanoDeDesenvolvimento
from model.i_repositorio_plano_de_desenvolvimento import IRepositorioPlanoDeDesenvolvimento
from model.conversor_plano_de_desenvolvimento_dicionario import ConversorPlanoDeDesenvolvimentoDicionario


class RepositorioPlanoDeDesenvolvimentoFirestore(IRepositorioPlanoDeDesenvolvimento):
    def __init__(self):
        self.colecao = firestore.client().collection("planos-de-desenvolvimento")

    def inserir(self, habilidade: PlanoDeDesenvolvimento):
        dicionario_habilidade = ConversorPlanoDeDesenvolvimentoDicionario.habilidade_para_dicionario(habilidade)
        self.colecao.document(habilidade.nome).set(dicionario_habilidade)

    def contultar_plano_de_desenvolvimento(self, email: str) -> Optional[PlanoDeDesenvolvimento]:
        referencia = self.colecao.document(email)
        documento = referencia.get()

        if not documento.exists:
            return None

        habilidade = ConversorPlanoDeDesenvolvimentoDicionario.dicionario_para_habilidade(documento.to_dict())

        return habilidade

    def atualizar(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(plano_de_desenvolvimento)

    def remover(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        self.colecao.document(plano_de_desenvolvimento.id).delete() # TODO: ver se ta certo
