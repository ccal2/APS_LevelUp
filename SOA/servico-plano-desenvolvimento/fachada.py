from utils.singleton import SingletonMeta

from model.cadastro_plano_de_desenvolvimento import CadastroPlanoDeDesenvolvimento


class Fachada(metaclass=SingletonMeta):
    def __init__(self):
        self.cadastro = CadastroPlanoDeDesenvolvimento

    def obter_plano_de_desenvolvimento(self, email: str):
        return self.cadastro.consultar_plano_de_desenvolvimento(email)
