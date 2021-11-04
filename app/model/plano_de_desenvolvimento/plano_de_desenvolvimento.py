from model.usuario.colaborador.colaborador import Colaborador
from model.habilidade.habilidades import Habilidade


class PlanoDeDesenvolvimento:
    def __init__(self, colaborador: Colaborador, habilidades: list[Habilidade] = []):
        self.colaborador = colaborador
        self.habilidades = habilidades
