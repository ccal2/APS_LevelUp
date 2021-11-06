class PlanoDeDesenvolvimento:
    def __init__(self, email_colaborador: str, ids_habilidades: "list[str]" = []):
        self.email_colaborador = email_colaborador
        self.ids_habilidades = ids_habilidades
