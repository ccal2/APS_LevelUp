import abc
from typing import Optional
from firebase_admin import firestore
from utils.constantes import *

from model.usuario.colaborador.colaborador import Colaborador
from model.usuario.colaborador.i_repositorio_colaborador import IRepositorioColaborador
from model.usuario.colaborador.colaborador_dicionario_conversor import ColaboradorDicionarioConversor
from model.interesse.i_repositorio_interesse import IRepositorioInteresse
from model.interesse.repositorio_interesse_firestore import RepositorioInteresseFirestore


class RepositorioColaboradorFirestore(IRepositorioColaborador):
    def __init__(self, repositorio_interesse: IRepositorioInteresse = None):
        self.colecao = firestore.client().collection(DB_COLABORADORES)
        if repositorio_interesse is None:
            self.repositorio_interesse = RepositorioInteresseFirestore()
        else:
            self.repositorio_interesse = repositorio_interesse

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

        dicionario = documento.to_dict()
        interesses = self.repositorio_interesse.consultar_interesses(ids=dicionario.get('interesses'))
        colaborador = ColaboradorDicionarioConversor.dicionario_para_colaborador(dicionario, interesses)

        return colaborador

    def atualizar(self, colaborador: Colaborador):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(colaborador)

    def remover(self, colaborador: Colaborador):
        self.colecao.document(colaborador.email).delete()
