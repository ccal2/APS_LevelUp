from utils.singleton import SingletonMeta

from model.cadastro_habilidade import CadastroHabilidade


class Fachada(metaclass=SingletonMeta):
    def __init__(self):
        cadastro = CadastroHabilidade

    def consultar_habilidades(self, email: str, senha: str):
        return self.controlador_login_usuario.realizar_login(email, senha)
