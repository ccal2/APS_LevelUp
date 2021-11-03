import abc
from typing import Optional
from firebase_admin import firestore
from utils.constants import *

from model.usuario.colaborador.Colaborador import Colaborador
from model.usuario.colaborador.IRepositorioColaborador import IRepositorioColaborador
from model.usuario.colaborador.ColaboradorDicionarioConversor import ColaboradorDicionarioConversor


class RepositorioColaboradorFirestore(IRepositorioColaborador):
    def __init__(self):
        self.colecao = firestore.client().collection(DB_COLABORADORES)

    def inserir(self, colaborador: Colaborador):
        dicionario_colaborador = ColaboradorDicionarioConversor.colaborador_para_dicionario(colaborador)

        # Inserir objeto no banco
        self.colecao.document(colaborador.email).set(dicionario_colaborador)

    def consultar_colaborador(self, email: str) -> Optional[Colaborador]:
        # Pegar objeto do banco de dados
        documento = self.colecao.document(email)
        dicionario_colaborador = documento.get()

        if not dicionario_colaborador.exists:
            return None

        colaborador = ColaboradorDicionarioConversor.dicionario_para_colaborador(dicionario_colaborador.to_dict())

        return colaborador

    def atualizar(self, colaborador: Colaborador):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(colaborador)

    def remover(self, colaborador: Colaborador):
        self.colecao.document(colaborador.email).delete()
