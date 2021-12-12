from typing import Optional
from firebase_admin import firestore
from utils.helpers import executar_query_extentida

from model.i_repositorio_habilidade import IRepositorioHabilidade


class RepositorioHabilidadeFirestore(IRepositorioHabilidade):
    def __init__(self):
        self.colecao = firestore.client().collection("habilidades")

    def inserir(self, habilidade: dict):
        nome = habilidade.get("nome")

        if nome is None:
            return

        self.colecao.document(nome).set(habilidade)

    def consultar_habilidade(self, id: str) -> Optional[dict]:
        referencia = self.colecao.document(id)
        documento = referencia.get()

        if not documento.exists:
            return None

        return documento.to_dict()

    def consultar_habilidades_por_ids(self, ids: "list[str]") -> "list[dict]":
        habilidades = []
        for id in ids:
            habilidade = self.consultar_habilidade(id)
            if habilidade:
                habilidades.append(habilidade)

        return habilidades

    def consultar_habilidades_por_interesses(self, interesses: "list[str]") -> "list[dict]":
        documentos = executar_query_extentida(
            referencia_colecao=self.colecao,
            ids=interesses,
            parametro_query="interesses",
            operacao_query="array_contains_any",
        )

        habilidades = list(map(lambda x: x.to_dict(), documentos))

        return habilidades

    def atualizar(self, habilidade: dict):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(habilidade)

    def remover(self, habilidade: dict):
        nome = habilidade.get("nome")

        if nome is None:
            return

        self.colecao.document(nome).delete()
