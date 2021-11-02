import abc
from typing import Optional
from Colaborador import Colaborador
from Interesse.Interesse import Interesse
from IRepositorioColaborador import IRepositorioColaborador
from Conversores.ColaboradorDicionarioConversor import ColaboradorDicionarioConversor
from firebase_admin import firestore
from constants import *

class RepositorioColaboradorFirestore(IRepositorioColaborador):

    def __init__(self):
        self.colecao = firestore.client().collection(DB_COLABORADORES)

    def inserir(self, colaborador: Colaborador):
        dicionarioColaborador = ColaboradorDicionarioConversor.colaboradorParaDicionario(Colaborador)

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
