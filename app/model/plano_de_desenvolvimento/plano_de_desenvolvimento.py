class PlanoDeDesenvolvimento:
    def __init__(self, id_colaborador: str, ids_habilidades: "list[str]" = []):
        self.id_colaborador = id_colaborador
        self.ids_habilidades = ids_habilidades
