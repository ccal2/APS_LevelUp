class Habilidade:
    def __init__(self, nome: str, descricao: str, nivel: int, ids_interesses: "list[str]"):
        self.nome = nome
        self.descricao = descricao
        self.nivel = nivel
        self.ids_interesses = ids_interesses
