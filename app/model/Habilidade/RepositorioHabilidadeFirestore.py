from typing import Optional
from firebase_admin import firestore
from Utils.constants import *

from model.Habilidade.Habilidade import Habilidade
from model.Habilidade.IRepositorioHabilidade import IRepositorioHabilidade


class RepositorioHabilidadeFirestore(IRepositorioHabilidade):

    def __init__(self):
        self.colecao = firestore.client().collection(DB_HABILIDADES)

    def inserir(self, habilidade: Habilidade):
        habilidadeDict = {
            "nome": habilidade.nome,
            "descricao": habilidade.descricao,
            "nivel": habilidade.nivel,
            "interesses": habilidade.interesses
        }

        self.colecao.document(habilidade.nome).set(habilidadeDict)

    def consultarHabilidade(self, nome: str) -> Optional[Habilidade]:
        documento = self.colecao.document(nome)
        habilidade = documento.get()

        if not habilidade.exists:
            return None

        #...

    def atualizar(self, habilidade: Habilidade):
        return

    def remover(self, habilidade: Habilidade):
        return