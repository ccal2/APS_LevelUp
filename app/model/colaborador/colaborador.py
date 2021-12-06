from utils.email import Email


class Colaborador:
    def __init__(self, email: Email, nome: str, area: str, cargo: str, interesses: "list[str]" = []):
        self.email = email
        self.nome = nome
        self.area = area
        self.cargo = cargo
        self.interesses = interesses
