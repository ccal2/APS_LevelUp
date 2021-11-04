from typing import Optional

from model.usuario.usuario import Usuario
from model.interesse.interesses import Interesse


class Colaborador(Usuario):
    def __init__(self, email: str, nome: str, area: str, cargo: str, interesses: list[Interesse] = []):
        super().__init__(email, nome)
        self.area = area
        self.cargo = cargo
        self.interesses = interesses
