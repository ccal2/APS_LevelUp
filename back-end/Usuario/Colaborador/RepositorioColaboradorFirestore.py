import abc
from typing import Optional
from Colaborador import Colaborador
from Interesse.Interesse import Interesse
from IRepositorioColaborador import IRepositorioColaborador
from firebase_admin import firestore
from constants import *

class RepositorioColaboradorFirestore(IRepositorioColaborador):

    def __init__(self):
        self.colecao = firestore.client().collection(DB_COLABORADORES)

    def inserir(self, colaborador: Colaborador):
        # Converter Colaborador para dicionário
        ids_interesses = list(map(lambda x: x.titulo, colaborador.interesses))

        colaboradorDict = {
            "email": colaborador.email,
            "nome": colaborador.nome,
            "area": colaborador.area,
            "cargo": colaborador.cargo,
            "interesses": ids_interesses
        }

        # Inserir objeto no banco
        self.colecao.document(colaborador.email).set(colaboradorDict)

    def consultarColaborador(self, email: str) -> Optional[Colaborador]:
        # Pegar objeto do banco de dados
        documento = self.colecao.document(email)
        colaborador = documento.get()

        if not colaborador.exists:
            return None

        colaboradorDict = colaborador.to_dict()

        # Converter dicionário em Colaborador
        ids_interesses = colaboradorDict.get('interesses')
        interesses: list = []
        if ids_interesses != None:
            interesses = list(map(lambda x: Interesse(titulo=x), ids_interesses))

        return Colaborador(
            email = colaboradorDict.get('email'),
            nome = colaboradorDict.get('nome'),
            area = colaboradorDict.get('area'),
            cargo = colaboradorDict.get('cargo'),
            interesses = interesses
        )

    def atualizar(self, colaborador: Colaborador):
        # O método usado para inserir um objeto também pode ser usado para sobrescrevê-lo
        self.inserir(colaborador)

    def remover(self, colaborador: Colaborador):
        self.colecao.document(colaborador.email).delete()
