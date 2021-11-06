from utils.email import Email

class Usuario:
    def __init__(self, email: Email, nome: str):
        self.email = email
        self.nome = nome
