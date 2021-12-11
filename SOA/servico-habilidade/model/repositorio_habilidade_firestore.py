from typing import Optional
from firebase_admin import firestore
from utils.helpers import executar_query_extentida

from model.habilidade import Habilidade
from model.i_repositorio_habilidade import IRepositorioHabilidade
from model.conversor_habilidade_dicionario import ConversorHabilidadeDicionario


class RepositorioHabilidadeFirestore(IRepositorioHabilidade):
    def __init__(self):
        self.colecao = firestore.client().collection("habilidades")

    def consultar_habilidades_por_interesses(self, interesses: "list[str]") -> "list[Habilidade]":
        documentos = executar_query_extentida(
            referencia_colecao=self.colecao,
            ids=interesses,
            parametro_query="interesses",
            operacao_query="array_contains_any",
        )

        habilidades = list(
            map(lambda x: ConversorHabilidadeDicionario.dicionario_para_habilidade(x.to_dict()), documentos)
        )

        return habilidades

    def inserir(self, habilidade: Habilidade):
        dicionario_habilidade = ConversorHabilidadeDicionario.habilidade_para_dicionario(habilidade)
        self.colecao.document(habilidade.nome).set(dicionario_habilidade)

    def consultar_habilidade(self, nome: str) -> Optional[Habilidade]:
        referencia = self.colecao.document(nome)
        documento = referencia.get()

        if not documento.exists:
            return None

        habilidade = ConversorHabilidadeDicionario.dicionario_para_habilidade(documento.to_dict())

        return habilidade

    def atualizar(self, habilidade: Habilidade):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(habilidade)

    def remover(self, habilidade: Habilidade):
        self.colecao.document(habilidade.nome).delete()
