import abc
from typing import Optional
from firebase_admin import firestore
from utils.constantes import *

from model.usuario.colaborador.colaborador import Colaborador
from model.usuario.colaborador.i_repositorio_colaborador import IRepositorioColaborador
from model.usuario.colaborador.colaborador_dicionario_conversor import ColaboradorDicionarioConversor


class RepositorioColaboradorFirestore(IRepositorioColaborador):
    def __init__(self):
        self.colecao = firestore.client().collection(DB_COLABORADORES)

    def inserir(self, colaborador: Colaborador):
        dicionario_colaborador = ColaboradorDicionarioConversor.colaborador_para_dicionario(colaborador)

        # Inserir objeto no banco
        self.colecao.document(colaborador.email).set(dicionario_colaborador)

    def consultar_colaborador(self, email: str) -> Optional[Colaborador]:
        # Pegar documento do banco de dados
        referencia = self.colecao.document(email)
        documento = referencia.get()

        if not documento.exists:
            return None

        colaborador = ColaboradorDicionarioConversor.dicionario_para_colaborador(documento.to_dict())

        return colaborador

    def atualizar(self, colaborador: Colaborador):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(colaborador)

    def remover(self, colaborador: Colaborador):
        self.colecao.document(colaborador.email).delete()
