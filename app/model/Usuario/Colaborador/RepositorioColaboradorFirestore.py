import abc
from typing import Optional
from firebase_admin import firestore
from Utils.constants import *

from model.Usuario.Colaborador.Colaborador import Colaborador
from model.Interesse.Interesse import Interesse
from model.Usuario.Colaborador.IRepositorioColaborador import IRepositorioColaborador
from model.Conversores.ColaboradorDicionarioConversor import (
    ColaboradorDicionarioConversor,
)


class RepositorioColaboradorFirestore(IRepositorioColaborador):
    def __init__(self):
        self.colecao = firestore.client().collection(DB_COLABORADORES)

    def inserir(self, colaborador: Colaborador):
        dicionarioColaborador = ColaboradorDicionarioConversor.colaboradorParaDicionario(colaborador)

        # Inserir objeto no banco
        self.colecao.document(colaborador.email).set(dicionarioColaborador)

    def consultarColaborador(self, email: str) -> Optional[Colaborador]:
        # Pegar objeto do banco de dados
        documento = self.colecao.document(email)
        objetoColaborador = documento.get()

        if not objetoColaborador.exists:
            return None

        colaborador = ColaboradorDicionarioConversor.dicionarioParaColaborador(objetoColaborador.to_dict())

        return colaborador

    def atualizar(self, colaborador: Colaborador):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(colaborador)

    def remover(self, colaborador: Colaborador):
        self.colecao.document(colaborador.email).delete()
