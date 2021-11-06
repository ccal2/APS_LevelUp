from model.usuario.usuario import Usuario
from utils.email import Email


class Colaborador(Usuario):
    def __init__(self, email: Email, nome: str, area: str, cargo: str, ids_interesses: "list[str]" = []):
        super().__init__(email, nome)
        self.area = area
        self.cargo = cargo
        self.ids_interesses = ids_interesses
