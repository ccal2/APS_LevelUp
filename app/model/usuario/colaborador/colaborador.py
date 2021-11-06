from typing import Optional

from model.usuario.usuario import Usuario
from model.interesse.interesses import Interesse
from utils.email import Email


class Colaborador(Usuario):
    def __init__(self, email: Email, nome: str, area: str, cargo: str, interesses: "list[Interesse]" = []):
        super().__init__(email, nome)
        self.area = area
        self.cargo = cargo
        self.interesses = interesses
