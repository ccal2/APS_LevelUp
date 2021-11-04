from typing import Optional
from firebase_admin import firestore
from utils.constantes import *
from utils.helpers import *

from model.interesse.interesses import Interesse
from model.interesse.i_repositorio_interesse import IRepositorioInteresse
from model.interesse.interesse_dicionario_conversor import InteresseDicionarioConversor


class RepositorioInteresseFirestore(IRepositorioInteresse):
    def __init__(self):
        self.colecao = firestore.client().collection(DB_INTERESSES)

    def inserir(self, interesse: Interesse):
        interesseDict = {
            "titulo": interesse.titulo,
        }

        self.colecao.document(interesse.titulo).set(interesseDict)

    def consultar_interesse(self, titulo: str) -> Optional[Interesse]:
        documento = self.colecao.document(titulo)
        interesse = documento.get()

        if not interesse.exists:
            return None

        # Converter dicionário em instância de Interesse
        interesseDict = interesse.to_dict()

        return Interesse(titulo=interesseDict.get("titulo"))

    def consultar_interesses(self, ids: str) -> "list[Interesse]":
        documentos = executar_query_extentida(
            referencia_colecao=self.colecao,
            ids=ids,
            parametro_query="titulo",
            operacao_query="in",
        )

        interesses = list(
            map(lambda x: InteresseDicionarioConversor.dicionario_para_interesse(x.to_dict()), documentos)
        )

        return interesses

    def atualizar(self, interesse: Interesse):
        return

    def remover(self, interesse: Interesse):
        return
