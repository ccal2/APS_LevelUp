from utils.singleton import SingletonMeta

from model.cadastro_habilidade import CadastroHabilidade


class Fachada(metaclass=SingletonMeta):
    def __init__(self):
        self.cadastro = CadastroHabilidade

    def consultar_habilidades(self, interesses: "list[str]"):
        return self.cadastro.consultar_habilidades_por_interesses(interesses)
