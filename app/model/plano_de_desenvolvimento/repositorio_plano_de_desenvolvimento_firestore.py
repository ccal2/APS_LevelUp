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
            "colaborador": plano_de_desenvolvimento.colaborador.email,
            "habilidades": nomes_habilidades,
        }

        self.colecao.document(plano_de_desenvolvimento.collaborador.email).set(plano_de_desenvolvimento_dict)

    def consultar_plano_de_desenvolvimento(self, id_colaborador: str) -> Optional[PlanoDeDesenvolvimento]:
        documento = self.colecao.document(id_colaborador)
        plano_de_desenvolvimento = documento.get()

        if not plano_de_desenvolvimento.exists:
            return None

        plano_de_desenvolvimento_dict = plano_de_desenvolvimento.to_dict()

        return PlanoDeDesenvolvimento(
            id_colaborador=plano_de_desenvolvimento.get("colaborador"),
            ids_habilidades=plano_de_desenvolvimento_dict.get("habilidades"),
        )

    def atualizar(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(plano_de_desenvolvimento)

    def remover(self, plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        self.colecao.document(plano_de_desenvolvimento.id_colaborador).delete()
