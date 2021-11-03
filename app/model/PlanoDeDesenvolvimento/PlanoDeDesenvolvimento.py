from model.Usuario.Colaborador.Colaborador import Colaborador
from model.Habilidade.Habilidade import Habilidade


class PlanoDeDesenvolvimento:

    def __init__(self, colaborador: Colaborador, habilidades: list[Habilidade]=[]):
        self.colaborador = colaborador
        self.habilidades = habilidades
