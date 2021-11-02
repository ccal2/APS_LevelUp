from Usuario import Usuario


class Colaborador(Usuario):

    def __init__(self, email: str, nome: str, area: str, cargo: str):
        super().__init__(email, nome)
        self.area = area
        self.cargo = cargo
        self.interesses = []
