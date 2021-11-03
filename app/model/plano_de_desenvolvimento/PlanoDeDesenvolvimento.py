from model.usuario.colaborador.Colaborador import Colaborador
from model.habilidade.Habilidade import Habilidade


class PlanoDeDesenvolvimento:
    def __init__(self, colaborador: Colaborador, habilidades: list[Habilidade] = []):
        self.colaborador = colaborador
        self.habilidades = habilidades
