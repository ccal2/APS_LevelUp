from typing import Optional
from firebase_admin import firestore
from utils.constantes import *
from utils.helpers import *

from model.habilidade.habilidades import Habilidade
from model.interesse.interesses import Interesse
from model.habilidade.i_repositorio_habilidade import IRepositorioHabilidade
from model.habilidade.habilidade_dicionario_conversor import HabilidadeDicionarioConversor
from model.interesse.i_repositorio_interesse import IRepositorioInteresse
from model.interesse.repositorio_interesse_firestore import RepositorioInteresseFirestore


class RepositorioHabilidadeFirestore(IRepositorioHabilidade):
    def __init__(self, repositorio_interesse: IRepositorioInteresse = None):
        self.colecao = firestore.client().collection(DB_HABILIDADES)
        if repositorio_interesse is None:
            self.repositorio_interesse = RepositorioInteresseFirestore()
        else:
            self.repositorio_interesse = repositorio_interesse

    def consultar_habilidades(self, interesses: "list[Interesse]") -> "list[Habilidade]":
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

        dicionario = documento.to_dict()
        interesses = self.repositorio_interesse.consultar_interesses(ids=dicionario.get('interesses'))
        habilidade = HabilidadeDicionarioConversor.dicionario_para_habilidade(dicionario, interesses)

        return habilidade

    def atualizar(self, habilidade: Habilidade):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(habilidade)

    def remover(self, habilidade: Habilidade):
        self.colecao.document(habilidade.nome).delete()
