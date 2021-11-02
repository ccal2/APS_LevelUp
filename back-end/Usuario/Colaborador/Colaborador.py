from Usuario import Usuario
from Interesse.Interesse import Interesse


class Colaborador(Usuario):

    def __init__(self, email: str, nome: str, area: str, cargo: str, interesses: list(Interesse)=[]):
        super().__init__(email, nome)
        self.area = area
        self.cargo = cargo
        self.interesses = interesses
