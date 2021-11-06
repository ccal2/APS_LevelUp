from typing import Optional
from firebase_admin import firestore
from utils.constantes import *
from utils.helpers import *

from model.interesse.interesses import Interesse
from model.interesse.i_repositorio_interesse import IRepositorioInteresse
from model.conversores.conversor_interesse_dicionario import ConversorInteresseDicionario


class RepositorioInteresseFirestore(IRepositorioInteresse):
    def __init__(self):
        self.colecao = firestore.client().collection(DB_INTERESSES)

    def inserir(self, interesse: Interesse):
        dicionario_interesse = ConversorInteresseDicionario.interesse_para_dicionario(interesse)

        self.colecao.document(interesse.titulo).set(dicionario_interesse)

    def consultar_interesse(self, titulo: str) -> Optional[Interesse]:
        referencia = self.colecao.document(titulo)
        documento = referencia.get()

        if not documento.exists:
            return None

        interesse = ConversorInteresseDicionario.dicionario_para_interesse(documento.to_dict())

        return interesse

    def consultar_interesses(self, ids: str) -> "list[Interesse]":
        documentos = executar_query_extentida(
            referencia_colecao=self.colecao,
            ids=ids,
            parametro_query="titulo",
            operacao_query="in",
        )

        interesses = list(
            map(lambda x: ConversorInteresseDicionario.dicionario_para_interesse(x.to_dict()), documentos)
        )

        return interesses

    def atualizar(self, interesse: Interesse):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(interesse)

    def remover(self, interesse: Interesse):
        self.colecao.document(interesse.titulo).delete()
