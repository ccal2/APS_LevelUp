from enum import Enum


class EstadoHabilidade(Enum):
    ADICIONADO = 0
    EM_PROGRESSO = 1
    FINALIZADO = 2

    def descricao(self):
        return self.name.capitalize().replace("_", " ")

class PlanoDeDesenvolvimento:
    def __init__(self, estado_por_habilidade: dict[str, EstadoHabilidade] = {}):
        self.estado_por_habilidade = estado_por_habilidade
