from typing import Optional
from firebase_admin import firestore
from utils.constantes import *

from model.plano_de_desenvolvimento.plano_de_desenvolvimento import PlanoDeDesenvolvimento
from model.plano_de_desenvolvimento.i_repositorio_plano_de_desenvolvimento import IRepositorioPlanoDeDesenvolvimento


class RepositorioPlanoDeDesenvolvimentoFirestore(IRepositorioPlanoDeDesenvolvimento):
    def __init__(self):
        self.colecao = firestore.client().collection(DB_PLANOS_DE_DESENVOLVIMENTO)

    def inserir(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        nomes_habilidades = list(map(lambda x: x.titulo, plano_de_desenvolvimento.habilidades))

        plano_de_desenvolvimento_dict = {
            "habilidades": nomes_habilidades,
            "colaborador": plano_de_desenvolvimento.colaborador.email,
        }

        self.colecao.document(plano_de_desenvolvimento.collaborador.email).set(plano_de_desenvolvimento_dict)

    def consultar_plano_de_desenvolvimento(self, email_colaborador: str) -> Optional[PlanoDeDesenvolvimento]:
        documento = self.colecao.document(email_colaborador)
        plano_de_desenvolvimento = documento.get()

        if not plano_de_desenvolvimento.exists:
            return None

        plano_de_desenvolvimento_dict = plano_de_desenvolvimento.to_dict()

        return PlanoDeDesenvolvimento(
            habilidades=plano_de_desenvolvimento_dict.get("habilidades"),
            colaborador=plano_de_desenvolvimento.get("colaborador"),
        )

    def atualizar(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        return

    def remover(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        return
