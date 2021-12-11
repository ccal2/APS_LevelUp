class Habilidade:
    def __init__(self, nome: str, descricao: str, nivel: int, interesses: "list[str]"):
        self.nome = nome
        self.descricao = descricao
        self.nivel = nivel
        self.interesses = interesses
