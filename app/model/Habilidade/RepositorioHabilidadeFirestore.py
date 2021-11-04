from typing import Optional
from firebase_admin import firestore
from utils.constants import *
from utils.helpers import *

from model.habilidade.Habilidade import Habilidade
from model.interesse.Interesse import Interesse
from model.habilidade.IRepositorioHabilidade import IRepositorioHabilidade
from model.habilidade.HabilidadeDicionarioConversor import HabilidadeDicionarioConversor


class RepositorioHabilidadeFirestore(IRepositorioHabilidade):
    def __init__(self):
        self.colecao = firestore.client().collection(DB_HABILIDADES)

    def consultar_habilidades(self, interesses: list[Interesse]) -> list[Habilidade]:
        ids_interesses = list(map(lambda x: x.titulo, interesses))

        documentos = executar_query_extentida(
            referencia_colecao=self.colecao,
            ids=ids_interesses,
            parametro_query="interesses",
            operacao_query="array_contains_any",
        )

        habilidades = list(
            map(lambda x: HabilidadeDicionarioConversor.dicionario_para_habilidade(x.to_dict()), documentos)
        )

        return habilidades

    def inserir(self, habilidade: Habilidade):
        dicionario_habilidade = HabilidadeDicionarioConversor.habilidade_para_dicionario(habilidade)

        self.colecao.document(habilidade.nome).set(dicionario_habilidade)

    def consultar_habilidade(self, nome: str) -> Optional[Habilidade]:
        referencia = self.colecao.document(nome)
        documento = referencia.get()

        if not documento.exists:
            return None

        habilidade = HabilidadeDicionarioConversor.dicionario_para_habilidade(documento.to_dict())

        return habilidade

    def atualizar(self, habilidade: Habilidade):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(habilidade)

    def remover(self, habilidade: Habilidade):
         self.colecao.document(habilidade.nome).delete()
