from typing import Optional
from Interesse import Interesse
from IRepositorioInteresse import IRepositorioInteresse
from firebase_admin import firestore
from constants import *

class RepositorioInteresseFirestore(IRepositorioInteresse):

    def __init__(self):
        self.colecao = firestore.client().collection(DB_INTERESSES)

    def inserir(self, interesse: Interesse):
        interesseDict = {
            "titulo": interesse.titulo,
        }

        self.colecao.document(interesse.titulo).set(interesseDict)

    def consultarInteresse(self, titulo: str) -> Optional[Interesse]:
        documento = self.colecao.document(titulo)
        interesse = documento.get()

        if not interesse.exists:
            return None

        # Converter dicionário em instância de Interesse
        interesseDict = interesse.to_dict()

        return Interesse(
            titulo = interesseDict.get('titulo')
        )

    def atualizar(self, interesse: Interesse):
        return

    def remover(self, interesse: Interesse):
        return
