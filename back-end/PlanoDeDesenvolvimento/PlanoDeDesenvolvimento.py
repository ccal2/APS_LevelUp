from Usuario.Colaborador.Colaborador import Colaborador
from Habilidade.Habilidade import Habilidade


class PlanoDeDesenvolvimento:

    def __init__(self, colaborador: Colaborador, habilidades: list[Habilidade]=[]):
        self.colaborador = colaborador
        self.habilidades = habilidades
