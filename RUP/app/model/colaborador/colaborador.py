from utils.email import Email
from model.plano_de_desenvolvimento.plano_de_desenvolvimento import PlanoDeDesenvolvimento


class Colaborador:
    def __init__(
        self,
        email: Email,
        nome: str,
        area: str,
        cargo: str,
        interesses: "list[str]",
        plano_de_desenvolvimento: PlanoDeDesenvolvimento,
    ):
        self.email = email
        self.nome = nome
        self.area = area
        self.cargo = cargo
        self.interesses = interesses
        self.plano_de_desenvolvimento = plano_de_desenvolvimento
